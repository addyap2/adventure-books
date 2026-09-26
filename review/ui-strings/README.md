# UI strings review — native-speaker check

Interface copy that is shown translated (not story text). Right now this is the **home page**
— the hero (tagline + intro) and the three "how it works" steps (heading + body), which
morph through the eight site languages on `web/library.html`. The English is authoritative;
each translated draft wants a native speaker's eyes before launch, exactly like the glossary
(`../glossary/`).

## The files

`home-hero.csv` — the home page (hero + how-it-works steps), one row per (string × language).
`book-hero.csv` — the book-page hero sub-line (shared by all books), one row per language.
Both use the same columns.

| column | what to do |
|---|---|
| `string_id` | which string (`tagline`, `intro`, `step1_heading`, `step1_body`, …) — do not change |
| `location` | where it appears — do not change |
| `language` | fr / es / pt / it / de / ru / ar / zh — do not change |
| `english_source` | the meaning to preserve — **match this**, keep it natural, not literal |
| `draft` | the current draft translation (also live in the hero) |
| `corrected_translation` | leave blank if the draft is right; otherwise put the correct form here |
| `reviewer_notes` | register, tone, article, RTL/punctuation, regional variant, anything to flag |

Keep it a warm, plain marketing voice — it is the first line a learner reads. The tagline
should stay short and rhythmic. `A2` / `B1` / `B2` stay as-is in every language.

## Priority

Same as the glossary: **ru / ar / zh** are machine-authored and are the top priority for a
native pass; **pt** also needs its variety settled (the draft is European Portuguese — decide
EU or BR and make it consistent with the glossary's choice).

## Applying corrections

There is no auto-merge script for these yet (there are only 16 rows). Hand the edited CSV
back and the `corrected_translation` values get pasted into the `S` array in
`web/library.html` (the hero morph) — matched by `string_id` + `language`.
