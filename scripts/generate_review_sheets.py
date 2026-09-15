#!/usr/bin/env python3
"""Generate native-review sheets — one CSV per language, covering BOTH glossing tiers.

Each reviewer gets a single file for their language with every draft translation to check:
the CURATED story words (authoritative — the launch gate) and the COVERAGE everyday-word
dictionary (best-effort). A `tier` column keeps them apart; corrections merge back to the
right place via scripts/apply_review.py. UTF-8 CSV opens cleanly in Excel/Sheets/Numbers.
"""
import json, os, csv

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
EP = os.path.join(ROOT, "content", "episode-01.json")
DICT = os.path.join(ROOT, "content", "dict")
OUT = os.path.join(ROOT, "review", "glossary")
os.makedirs(OUT, exist_ok=True)

LANGS = {"fr": "French", "es": "Spanish", "pt": "Portuguese", "it": "Italian",
         "de": "German", "ru": "Russian", "ar": "Arabic", "zh": "Mandarin Chinese"}

book = json.load(open(EP, encoding="utf-8"))
curated = book["lexicon"]["entries"]
cur_words = sorted(curated)

for code, name in LANGS.items():
    cov = {}
    p = os.path.join(DICT, f"{code}.json")
    if os.path.exists(p):
        cov = json.load(open(p, encoding="utf-8"))
    cov_words = sorted(cov)
    path = os.path.join(OUT, f"{code}.csv")
    with open(path, "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["tier", "headword", "part_of_speech", "english_definition",
                    f"draft_{code}", "corrected_translation", "reviewer_notes"])
        for hw in cur_words:                       # authoritative tier first
            e = curated[hw]
            w.writerow(["curated", hw, e.get("pos", ""), e.get("en", ""), e.get(code, ""), "", ""])
        for hw in cov_words:                       # everyday coverage tier
            w.writerow(["coverage", hw, "", "", cov[hw], "", ""])
    print(f"  {name:20} → review/glossary/{code}.csv  "
          f"({len(cur_words)} curated + {len(cov_words)} coverage = {len(cur_words)+len(cov_words)})")

total = len(cur_words) + len(sorted(json.load(open(os.path.join(DICT, 'fr.json'))) if os.path.exists(os.path.join(DICT,'fr.json')) else {}))
readme = os.path.join(OUT, "README.md")
with open(readme, "w", encoding="utf-8") as fh:
    fh.write(f"""# Glossary review — native-speaker check

One CSV per language ({len(LANGS)} files). Each row is a **drafted, not verified** translation.
A wrong gloss the learner cannot detect is worse than no gloss, so every entry wants a native
speaker's eyes before launch.

Two tiers, marked in the `tier` column:

- **curated** — the {len(cur_words)} chosen *story* words, each with an English definition. These are
  **authoritative and the launch priority** — please review these first and thoroughly.
- **coverage** — the everyday-word dictionary (common vocabulary, quick translations, no English
  definition). Best-effort; review as time allows. Skimming for outright errors is enough.

## How to review

Open your language's file (e.g. `fr.csv`) in Excel, Google Sheets or Numbers.

| column | what to do |
|---|---|
| `tier` | curated (priority) or coverage — do not change |
| `headword` | the English word — do not change |
| `part_of_speech` | its part of speech (curated only) — do not change |
| `english_definition` | the sense to preserve (curated only) — **match this meaning** |
| `draft_<lang>` | the draft translation to check |
| `corrected_translation` | leave blank if the draft is right; otherwise put the correct form here |
| `reviewer_notes` | anything worth flagging (register, article, regional variant, ambiguity) |

Keep the plain, everyday **register** and the **article** where the language needs one. If a word
has several senses, translate the one in `english_definition` (curated), or the sense the story
uses (coverage — it's a story about arriving in a city at night to find a job).

Return the edited CSV. Corrections merge back with `scripts/apply_review.py` (matched by tier +
headword), so **do not reorder or rename columns**.
""")
print(f"  wrote review/glossary/README.md")
print(f"\nReady for review: {len(cur_words)} curated + coverage per language, {len(LANGS)} languages.")
