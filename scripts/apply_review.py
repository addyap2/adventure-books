#!/usr/bin/env python3
"""Merge reviewers' corrected glossary CSVs back into the right place, by tier.

Reads review/glossary/<lang>.csv; for every row with a non-empty `corrected_translation`,
overwrites that language's gloss for the headword — a `curated` row updates the episode's
lexicon (content/episode-01.json), a `coverage` row updates that language's dictionary
(content/dict/<lang>.json). Matches by tier + headword, so column order does not matter.
Run after native review; then re-validate and rebuild.
"""
import json, os, csv, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
EP = os.path.join(ROOT, "content", "episode-01.json")
DICT = os.path.join(ROOT, "content", "dict")
OUT = os.path.join(ROOT, "review", "glossary")
LANGS = ["fr", "es", "pt", "it", "de", "ru", "ar", "zh"]

book = json.load(open(EP, encoding="utf-8"))
curated = book["lexicon"]["entries"]
cur_changed = 0
cov_changed = 0

for code in LANGS:
    path = os.path.join(OUT, f"{code}.csv")
    if not os.path.exists(path):
        continue
    cov_path = os.path.join(DICT, f"{code}.json")
    cov = json.load(open(cov_path, encoding="utf-8")) if os.path.exists(cov_path) else {}
    cov_dirty = False
    with open(path, encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            hw = (row.get("headword") or "").strip()
            fix = (row.get("corrected_translation") or "").strip()
            tier = (row.get("tier") or "curated").strip()
            if not hw or not fix:
                continue
            if tier == "curated":
                if hw in curated and curated[hw].get(code) != fix:
                    curated[hw][code] = fix; cur_changed += 1
            else:
                if cov.get(hw) != fix:
                    cov[hw] = fix; cov_dirty = True; cov_changed += 1
    if cov_dirty:
        json.dump(cov, open(cov_path, "w", encoding="utf-8"),
                  ensure_ascii=False, separators=(",", ":"), sort_keys=True)

if cur_changed:
    json.dump(book, open(EP, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

if cur_changed or cov_changed:
    print(f"Applied {cur_changed} curated + {cov_changed} coverage correction(s). "
          f"Now re-validate and rebuild.")
else:
    print("No corrections found (no non-empty corrected_translation cells).")
    sys.exit(0)
