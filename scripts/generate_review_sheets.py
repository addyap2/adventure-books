#!/usr/bin/env python3
"""Generate native-review sheets from a book's lexicon — one CSV per language.

Each reviewer gets a single file for their language: the headword, its part of speech,
the English definition (the primary sense to preserve), the draft translation to check,
and blank columns to correct it and leave a note. UTF-8 CSV opens cleanly in Excel /
Google Sheets / Numbers. Run per book; writes to review/glossary/<lang>.csv.
"""
import json, os, csv

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
EP = os.path.join(ROOT, "content", "episode-01.json")
OUT = os.path.join(ROOT, "review", "glossary")
os.makedirs(OUT, exist_ok=True)

LANGS = {"fr": "French", "es": "Spanish", "pt": "Portuguese", "it": "Italian",
         "de": "German", "ru": "Russian", "ar": "Arabic", "zh": "Mandarin Chinese"}

book = json.load(open(EP, encoding="utf-8"))
entries = book["lexicon"]["entries"]
words = sorted(entries)

for code, name in LANGS.items():
    path = os.path.join(OUT, f"{code}.csv")
    with open(path, "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["headword", "part_of_speech", "english_definition",
                    f"draft_{code}", "corrected_translation", "reviewer_notes"])
        for hw in words:
            e = entries[hw]
            w.writerow([hw, e.get("pos", ""), e.get("en", ""), e.get(code, ""), "", ""])
    print(f"  {name:20} → review/glossary/{code}.csv  ({len(words)} rows)")

readme = os.path.join(OUT, "README.md")
with open(readme, "w", encoding="utf-8") as fh:
    fh.write(f"""# Glossary review — native-speaker check

One CSV per language ({len(LANGS)} files), each with the same {len(words)} headwords.
These translations were **drafted, not verified**. A wrong gloss the learner cannot
detect is worse than no gloss, so every entry needs a native speaker's eyes before launch.

## How to review

Open your language's file (e.g. `fr.csv`) in Excel, Google Sheets or Numbers.

| column | what to do |
|---|---|
| `headword` | the English word (do not change) |
| `part_of_speech` | its part of speech (do not change) |
| `english_definition` | the sense the translation must match — **preserve this meaning** |
| `draft_<lang>` | the draft translation to check |
| `corrected_translation` | leave blank if the draft is right; otherwise put the correct form here |
| `reviewer_notes` | anything worth flagging (register, article, regional variant, ambiguity) |

Guidance: keep the same **register** (plain, everyday) and the **article** where the
language needs one (the drafts follow "le/la/l'", "el/la", "der/die/das", etc.). If a word
has several senses, translate the one in `english_definition`, not the most common one.

Return the edited CSV. The corrections are merged back with `scripts/apply_review.py`
(headword-matched), so **do not reorder or rename columns**.
""")
print(f"  wrote review/glossary/README.md")
print(f"\n{len(words)} words × {len(LANGS)} languages ready for review.")
