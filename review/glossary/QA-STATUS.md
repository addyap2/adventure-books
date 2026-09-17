# Glossary review — status

Tracks what has been checked and what still needs a native speaker, per language.
(Full instructions for reviewers are in `README.md`.)

**Content coverage: complete for all 8 languages** — every language has the full curated
lexicon (232 words), the coverage dictionary (516 words) and whole-book passage gists (123).
Nothing is missing. What remains is **quality**: native review, and for ru/ar/zh a first
read of any kind (they are machine-authored throughout).

| Language | Self-QA (Claude) | Native review | Notes |
|---|---|---|---|
| French (fr)   | ✅ done | ⬜ pending | Read as sound; `shot` corrected to *la dose*. |
| Spanish (es)  | ✅ done | ⬜ pending | Sound; `shot` → *la dosis*. |
| Italian (it)  | ✅ done | ⬜ pending | Sound; `shot` → *la dose*. |
| German (de)   | ✅ done | ⬜ pending | Sound. |
| Portuguese (pt) | ✅ done | ⬜ pending | **Variety not standardised** — see below. |
| Russian (ru)  | ⬜ — | ⬜ **required** | All three layers present (lexicon 232, dict 516, gists 123) — **all machine-authored, none read by Claude**; needs a full native pass. |
| Arabic (ar)   | ⬜ — | ⬜ **required** | All three layers present (lexicon 232, dict 516, gists 123), machine-authored; native pass required (RTL — check sense + form). |
| Mandarin (zh) | ⬜ — | ⬜ **required** | All three layers present (lexicon 232, dict 516, gists 123), machine-authored; needs a full native pass. |

## What the self-QA was

A correctness pass by Claude on the five languages it can read reliably (fr, es, it, de, pt),
across both tiers (curated + coverage). The drafts read as largely correct; only the everyday
word **`shot`** was reworded (to the "a dose of coffee" sense) in fr/es/it. This does **not**
replace native review — it's an interim quality lift so human reviewers of those five start
from a cleaner draft. **Russian, Arabic and Mandarin have had no such pass and are the priority
for native speakers.**

## Passage gists (the "See the meaning" fallback)

All 8 languages now have a whole-book passage gist (`content/gist/<lang>.json`, 123 each).
fr/es/it/de/pt were authored in the vouched-five languages; **ru/ar/zh are machine-authored
from the same source meaning and are the top priority for a native pass** — they ship as
best-effort (the reader treats gists as the best-effort tier) but are not launch-final until
reviewed. Built by `scripts/build_gists.py` (five) and `scripts/build_gists_ruarzh.py` (three).

## Portuguese — pick one variety

The Portuguese drafts currently **mix European and Brazilian** forms (e.g. European *comboio,
autocarro, telemóvel, fato, rececionista* alongside Brazilian *faxineira, tênue*). A single
variety must be chosen. This was left for the PT reviewer rather than forced — decide EU or BR
and standardise the whole file to it (spelling included: *tênue*/*ténue*, *fato*/*terno*, etc.).

## Priority order for reviewers

1. **All languages: the `curated` rows first** — they are authoritative and gate launch.
2. **ru / ar / zh, both tiers** — no self-QA has touched these.
3. pt: settle the variety.
4. Coverage rows in the self-QA'd languages — lowest priority (already skimmed).
