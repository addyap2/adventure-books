# Glossary review — native-speaker check

One CSV per language (8 files). Each row is a **drafted, not verified** translation.
A wrong gloss the learner cannot detect is worse than no gloss, so every entry wants a native
speaker's eyes before launch.

Two tiers, marked in the `tier` column:

- **curated** — the 232 chosen *story* words, each with an English definition. These are
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
