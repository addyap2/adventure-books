#!/usr/bin/env python3
"""Merge reviewers' corrected glossary CSVs back into the book's lexicon.

Reads review/glossary/<lang>.csv; for every row with a non-empty `corrected_translation`,
overwrites that language's gloss for the headword. Matches by headword, so column order
does not matter. Run after native review; then re-validate and rebuild.
"""
import json, os, csv, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
EP = os.path.join(ROOT, "content", "episode-01.json")
OUT = os.path.join(ROOT, "review", "glossary")
LANGS = ["fr", "es", "pt", "it", "de", "ru", "ar", "zh"]

book = json.load(open(EP, encoding="utf-8"))
entries = book["lexicon"]["entries"]
changed = 0
for code in LANGS:
    path = os.path.join(OUT, f"{code}.csv")
    if not os.path.exists(path):
        continue
    with open(path, encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            hw = (row.get("headword") or "").strip()
            fix = (row.get("corrected_translation") or "").strip()
            if hw and fix and hw in entries and entries[hw].get(code) != fix:
                entries[hw][code] = fix
                changed += 1

if changed:
    json.dump(book, open(EP, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"Applied {changed} correction(s). Now re-validate and rebuild.")
else:
    print("No corrections found (no non-empty corrected_translation cells).")
    sys.exit(0)
