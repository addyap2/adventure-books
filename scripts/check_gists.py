#!/usr/bin/env python3
"""Guard: per-passage gist + lexicon consistency across every book.

For each content/episode-*.json this checks, for all eight languages:
  - the gist file content/gist/<slug>/<lang>.json exists and is valid JSON,
  - its keys are exactly the book's node ids — no missing passages, no orphan
    keys pointing at nodes that don't exist,
  - no gist value is empty/blank,
and that every lexicon entry carries all eight languages.

It is the automated form of the by-hand audit: it stops a future edit from
silently leaving a passage unglossed, a stray key behind, or a language short.
Exit code 0 = all consistent; 1 = at least one problem (printed).

Run: python3 scripts/check_gists.py
"""
import glob
import json
import os
import sys

LANGS = ["fr", "es", "it", "de", "pt", "ru", "ar", "zh"]
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def check_book(path, problems):
    book = json.load(open(path, encoding="utf-8"))
    slug = book.get("slug")
    label = os.path.basename(path)
    if not slug:
        problems.append(f"{label}: no top-level slug")
        return
    node_ids = {str(n["id"]) for n in book.get("nodes", [])}
    n = len(node_ids)

    for lang in LANGS:
        rel = f"content/gist/{slug}/{lang}.json"
        fp = os.path.join(ROOT, rel)
        if not os.path.exists(fp):
            problems.append(f"{slug}/{lang}: gist file missing ({rel})")
            continue
        try:
            gist = json.load(open(fp, encoding="utf-8"))
        except (OSError, ValueError) as e:
            problems.append(f"{slug}/{lang}: unreadable JSON — {e}")
            continue
        keys = set(gist)
        missing = node_ids - keys
        orphan = keys - node_ids
        if missing:
            problems.append(f"{slug}/{lang}: {len(missing)} passage(s) with no gist, "
                            f"e.g. {sorted(missing, key=int)[:5]}")
        if orphan:
            problems.append(f"{slug}/{lang}: {len(orphan)} gist key(s) for nonexistent "
                            f"nodes, e.g. {sorted(orphan)[:5]}")
        empty = [k for k, v in gist.items() if not (isinstance(v, str) and v.strip())]
        if empty:
            problems.append(f"{slug}/{lang}: {len(empty)} empty gist value(s), "
                            f"e.g. {sorted(empty, key=lambda x: int(x) if x.isdigit() else 0)[:5]}")

    entries = (book.get("lexicon") or {}).get("entries") or {}
    short = {}
    for word, e in entries.items():
        miss = [l for l in LANGS if not (isinstance(e, dict) and e.get(l))]
        if miss:
            short[word] = miss
    if short:
        sample = list(short)[:5]
        problems.append(f"{slug}: {len(short)} lexicon entr(y/ies) missing languages, "
                        f"e.g. " + "; ".join(f"{w}→{short[w]}" for w in sample))

    print(f"  {slug:<20} {n} nodes — 8-lang gists + lexicon checked")


def main():
    problems = []
    books = sorted(glob.glob(os.path.join(ROOT, "content", "episode-*.json")))
    if not books:
        print("No content/episode-*.json found.", file=sys.stderr)
        return 1
    print("Checking gist + lexicon consistency:")
    for path in books:
        check_book(path, problems)
    if problems:
        print("\nINCONSISTENCIES:")
        for p in problems:
            print("  ✗", p)
        print(f"\n{len(problems)} problem(s).")
        return 1
    print("\nAll books consistent: every passage glossed in all 8 languages, "
          "no orphan keys, lexicons complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
