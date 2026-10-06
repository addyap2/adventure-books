# Content generators (archive)

One-off scripts that **built the books' content** during authoring. Their output is
already baked into `content/` (prose, lexicons, per-passage gists) and committed, so
these are kept only as **worked examples** of how each phase was produced — they are not
part of the build or CI and are not meant to be re-run as-is (their relative paths assume
the repo root).

The live pipeline lives one level up in `scripts/`:

- `build_book.py` — validator + per-level Markdown renderer (the gate; used by CI)
- `check_gists.py` — gist + lexicon consistency guard (used by CI)
- `build-site.mjs` — static site build (`npm run build`)
- `build_og.mjs` — regenerates `web/og-<slug>.png` / `cover-<slug>.png`
- `wordlist_core.txt` — the "assumed-known" word list the validator reads

## What's here, by phase (see docs/authoring-playbook.md)

- `build_*_skeleton.py`, `build_skeleton*.py`, `wire_flags.py`, `fix_choices.py` — graph skeletons
- `phase3_*.py` — three-level prose (B1 first, then A2/B2)
- `build_*_lexicon.py`, `expand_lexicon*.py`, `enrich_*_lexicon.py`, `promote_hard_words.py` — lexicons
- `build_coverage_dict.py` — the `content/dict/<lang>.json` coverage dictionary
- `g_<lang>_ep0N.py`, `build_gists*.py`, `build_gist_fr_full_*.py` — per-passage gists
- `build_art_prompts.py`, `generate_art.py` — art-prep helpers
