# Glossary review — status

Tracks what has been checked and what still needs a native speaker, per language.
(Full instructions for reviewers are in `README.md`.)

| Language | Self-QA (Claude) | Native review | Notes |
|---|---|---|---|
| French (fr)   | ✅ done | ⬜ pending | Read as sound; `shot` corrected to *la dose*. |
| Spanish (es)  | ✅ done | ⬜ pending | Sound; `shot` → *la dosis*. |
| Italian (it)  | ✅ done | ⬜ pending | Sound; `shot` → *la dose*. |
| German (de)   | ✅ done | ⬜ pending | Sound. |
| Portuguese (pt) | ✅ done | ⬜ pending | **Variety not standardised** — see below. |
| Russian (ru)  | ⬜ — | ⬜ **required** | Not machine-checkable by Claude; needs a native speaker. |
| Arabic (ar)   | ⬜ — | ⬜ **required** | Needs a native speaker (RTL; sense + form). |
| Mandarin (zh) | ⬜ — | ⬜ **required** | Needs a native speaker. |

## What the self-QA was

A correctness pass by Claude on the five languages it can read reliably (fr, es, it, de, pt),
across both tiers (curated + coverage). The drafts read as largely correct; only the everyday
word **`shot`** was reworded (to the "a dose of coffee" sense) in fr/es/it. This does **not**
replace native review — it's an interim quality lift so human reviewers of those five start
from a cleaner draft. **Russian, Arabic and Mandarin have had no such pass and are the priority
for native speakers.**

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
