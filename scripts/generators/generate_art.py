#!/usr/bin/env python3
"""Generate the per-passage painted art from content/art/episode-01.prompts.csv
using OpenAI's image API, and drop each result at the path the reader already
expects (images/<series>/ep-NN/<id>.webp) — see scripts/build_art_prompts.py.

Reads OPENAI_API_KEY from the environment (or a local .env file, gitignored —
see .env.example). Never pass the key on the command line.

Usage:
  .venv/bin/python3 scripts/generate_art.py --ids 1,2,3        # pilot a few
  .venv/bin/python3 scripts/generate_art.py                    # all 123, skips existing
  .venv/bin/python3 scripts/generate_art.py --force            # regenerate everything
  .venv/bin/python3 scripts/generate_art.py --quality high     # low|medium|high (cost/quality)
"""
import argparse, base64, csv, io, json, os, sys, time, urllib.request, urllib.error

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CSV_PATH = os.path.join(ROOT, "content", "art", "episode-01.prompts.csv")
API_URL = "https://api.openai.com/v1/images/generations"


def load_env_file():
    path = os.path.join(ROOT, ".env")
    if not os.path.exists(path):
        return
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def generate(prompt, api_key, size, quality, retries=3):
    body = json.dumps({
        "model": "gpt-image-1",
        "prompt": prompt,
        "size": size,
        "quality": quality,
        "n": 1,
    }).encode("utf-8")
    req = urllib.request.Request(API_URL, data=body, method="POST", headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    })
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read())
            return base64.b64decode(data["data"][0]["b64_json"])
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")
            if e.code == 429 and attempt < retries:
                time.sleep(5 * attempt)
                continue
            raise RuntimeError(f"HTTP {e.code}: {detail}") from None
        except urllib.error.URLError as e:
            if attempt < retries:
                time.sleep(3 * attempt)
                continue
            raise RuntimeError(str(e)) from None


def to_webp(png_bytes, out_path, target_w=1200, target_h=800):
    from PIL import Image
    im = Image.open(io.BytesIO(png_bytes)).convert("RGB")
    im = im.resize((target_w, target_h), Image.LANCZOS)
    quality = 82
    while quality >= 40:
        buf = io.BytesIO()
        im.save(buf, format="WEBP", quality=quality)
        if buf.tell() <= 200_000 or quality <= 40:
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "wb") as f:
                f.write(buf.getvalue())
            return buf.tell(), quality
        quality -= 10


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", help="comma-separated passage ids to (re)generate; default: all")
    ap.add_argument("--force", action="store_true", help="regenerate even if the webp already exists")
    ap.add_argument("--size", default="1536x1024", help="OpenAI image size (3:2 landscape)")
    ap.add_argument("--quality", default="medium", choices=["low", "medium", "high", "auto"])
    ap.add_argument("--sleep", type=float, default=1.0, help="seconds between requests")
    args = ap.parse_args()

    load_env_file()
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        sys.exit("OPENAI_API_KEY is not set. Put it in .env (see .env.example) or export it.")

    rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8")))
    wanted = {s.strip() for s in args.ids.split(",")} if args.ids else None

    done, skipped, failed = 0, 0, []
    for row in rows:
        if wanted is not None and row["id"] not in wanted:
            continue
        out_path = os.path.join(ROOT, row["filename"])
        if os.path.exists(out_path) and not args.force:
            skipped += 1
            continue
        print(f"[{row['id']}] {row['motif']}: generating...", flush=True)
        try:
            png_bytes = generate(row["prompt"], api_key, args.size, args.quality)
            size_bytes, quality = to_webp(png_bytes, out_path)
            print(f"  -> {row['filename']} ({size_bytes//1024} KB, webp q{quality})")
            done += 1
        except Exception as e:
            print(f"  !! failed: {e}", file=sys.stderr)
            failed.append(row["id"])
        time.sleep(args.sleep)

    print(f"\nDone: {done} generated, {skipped} skipped (already existed), {len(failed)} failed.")
    if failed:
        print("Failed ids:", ", ".join(failed))
        sys.exit(1)


if __name__ == "__main__":
    main()
