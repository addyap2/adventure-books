# Glossary review — native-speaker check

One CSV per language (8 files), each with the same 232 headwords.
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
