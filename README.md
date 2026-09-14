# Adventure Book

Branching choose-your-own-adventure stories for English learners — a *livre dont vous
êtes le héros* where the reader picks what happens next, written so that picking
correctly requires understanding the paragraph.

Every story is written at **three CEFR levels over one shared graph**, with a glossary in
**eight languages**. A learner can switch level mid-story and keep their place, because
A2 and B2 readers are moving through the same paragraph numbers and making the same
decisions — which means a mixed-level class can read "the same story" and discuss it
together afterwards.

## Layout

```
content/
  episode-01.json     one episode: the graph once, the prose once per level
  lexicon.json        every glossed word, translated once for the whole series
web/index.html        the reader (static, no framework, no dependencies)
scripts/
  build_book.py       validator and per-level Markdown renderer
  build-site.mjs      builds dist/ for deployment
dist/                 generated — do not edit
```

`content/` is the single source of truth. Prose is generated from it, so the paragraph a
reader sees can never disagree with the graph the app loads.

## Working on it

```bash
npm run build          # build dist/
npm run dev            # build and serve locally
npm run validate       # flags and lexicon coverage across the whole series

# validate one episode and render Markdown for every level
python3 scripts/build_book.py content/episode-01.json \
    --lexicon content/lexicon.json --out-dir build/
```

The validator refuses to render a broken episode. It checks that every `goto` resolves,
every paragraph is reachable, endings carry no choices, no paragraph's choices all lead
to the same place, every flag-gated node keeps an ungated "otherwise" path, every level
has every paragraph, every glossed word exists in the lexicon in all eight languages, and
that sentence and paragraph lengths sit inside each level's band. It runs on every push.

## Content model

- **Episode** — 25–40 paragraphs, one sitting, its own 4–5 endings. A series is ten to
  fifteen of them. One 500-paragraph graph would be unwritable and untestable; episodes
  ship independently.
- **Flags** — three to five per series, carried between episodes (`state_in` /
  `state_out`) or within one. A choice may be gated on a flag, but every paragraph keeps
  one ungated choice, so no reader is ever stranded by a rare combination.
- **Lexicon** — bare headwords on the node, translations once in `lexicon.json`. A word
  that appears in six episodes is translated once and can never disagree with itself.

Full spec: `references/schema.md` in the `adventure-chapter-writer` skill.

## Translations

French, Spanish, Portuguese, Italian, German, Russian, Arabic, Mandarin Chinese —
matching grammatica.antonyaddy.com. The English definition is primary; the translation is
the safety net beneath it. **Every translation needs a speaker's check before launch.** A
wrong gloss is worse than no gloss, because the learner cannot detect it.

## Deployment

Static. Vercel builds with `npm run build` and serves `dist/`.
