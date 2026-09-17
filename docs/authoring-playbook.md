# Adventure Book — authoring playbook (the footprint)

This is the repeatable recipe for producing a new book to the same standard as the
flagship, *The Address*. The design decisions are settled once (here and in
[flagship-design.md](flagship-design.md)); a new book **fills the shape**, it does not
re-litigate it. Follow the phases in order; each ends at a gate that must pass before the
next begins. That is what lets us produce more, in detail, with no open questions.

To start one, the instruction is simply: **"Design book N following the playbook."**

---

## 1. What a book is (the fixed shape)

| Element | Locked value | Why |
|---|---|---|
| Length | ~120–150 passages | A full CYOA-scale book that stays writable and testable |
| Levels | **A2 / B1 / B2**, prose per level over one shared graph | The mixed-class promise; matches the audience. See design bible §6/§6a |
| Endings | **12**, balanced **4 good / 4 neutral / 4 bad** | Earned replay; two may be secret (clue-gated) |
| Flags | **≤ 8**, each earned at one moment and paid off at another | Branches that matter, still testable |
| Glossary | **per-book lexicon ~250 words**, keyed by base form, 8 languages | Auto-gloss makes every word tappable wherever it appears |
| Series link | `state_out` → next book's `state_in` | Each book is "episode N of an arc" |
| Tone | Restrained, humane, "warm light in cold places" | The house voice; never breezy or generic |
| Art | ~30 images, **by location**, in waves; endings bespoke | See [art-brief.md](art-brief.md) + per-book shot-list |

**The one caveat to hold in mind (bible §6b):** CEFR governs the *language*, not the
branching *inference*. The choices carry the comprehension puzzle and are shared across
levels, so at A2 the **choice text** must be unambiguous and low-inference — a required
check in the native/pedagogy review.

---

## 2. The pipeline (phases and gates)

Each phase is a commit; each gate is `python3 scripts/build_book.py content/<book>.json --lexicon content/lexicon.json` coming back clean, plus the human sign-off noted.

1. **Design bible** — premise, three-act beat map + passage budget, the ≤8 flags (where each is earned/paid off), the 12 endings, the through-line, recurring faces, `state_in`/`state_out`.
   *Gate:* author approves the story. → commit `docs/<book>-design.md`.
2. **Graph skeleton** — every node as id + choices + gotos + flags + ending markers, with one-line stub text. Prove the machine before writing a word of real prose.
   *Gate:* validator 0 errors — reachable, no stranding, flags declared, endings valenced 4/4/4, no all-same-target choices.
3. **Prose — B1 first**, then polish B1 into band, then **A2** (simplify), then **B2** (enrich). Levelise every choice.
   *Gate:* per level, validator band-clean (A2 mean ≤12/sent ≤18; B1 ≤16/≤25; B2 ≤22/≤35); no `⟨pending⟩` slots left.
4. **Lexicon** — grow to ~250 concrete, high-tap words (nouns, common verbs, adjectives), base-keyed; skip proper nouns, contractions, B2-only flourishes.
   *Gate:* validator reports every entry complete in English + 8 languages; auto-gloss coverage advisory acceptably low.
5. **Native-language review** — *launch gate.* Generate sheets, hand to speakers, merge back, re-validate.
6. **Art** — the visual team works the per-book shot-list in waves; files drop in by convention.

I (Claude) do phases 1–4 and prep 5–6; people do 5 and 6. Phases 5–6 are run **once per book** on the same rails — routine, not open questions.

---

## 3. What to reuse vs. re-author for a new book

**Reuse as-is (generic engine — never re-write):**
- `web/index.html` — the reader (auto-gloss, per-book lexicon, per-moment placeholder art).
- `scripts/build-site.mjs` — the static build + manifest + image scan.
- `scripts/build_book.py` — the validator and Markdown renderer (all bands and gates).
- `scripts/generate_review_sheets.py` + `scripts/apply_review.py` — the native-review round-trip.
- `docs/flagship-design.md`, `docs/art-brief.md`, this playbook — the standards.

**Re-author per book (same pattern, new content):**
- `content/<book>.json` — the graph + three-level prose + embedded `lexicon`. The flagship's
  `build_skeleton*.py` / `phase3_*.py` / `expand_lexicon*.py` are **worked examples** of how
  each phase was built for book 1; a new book produces its own equivalents (or writes the JSON
  directly), following the identical phase order and gates.
- `docs/<book>-design.md` and `docs/<book>-art-shotlist.md`.

**New series vs. same series:** same series (`new-city`) → reuse the shared base `lexicon.json`
and carry `state_in`. New series → new folder convention `images/<series>/…` and its own base.

---

## 4. Hand-off templates (already built, reusable every book)

**Native review** — `python3 scripts/generate_review_sheets.py` writes one CSV per language to
`review/glossary/<lang>.csv` (+ a README for reviewers): headword · part of speech · English
definition · draft translation · blank *corrected* + *notes* columns. Reviewers edit only the
blanks; `scripts/apply_review.py` merges corrections back by headword. Then re-validate + rebuild.
*Also review each A2 choice for clarity here (the §6b check).*

**Art** — a per-book `docs/<book>-art-shotlist.md` (see the flagship's
[art-shotlist.md](art-shotlist.md) as the model): images grouped by location and wave, each with
a **hero paragraph id** for the filename, the other ids it covers, and a draft faceless alt-line.
Wave 1 locks the look; later waves fill in; endings are bespoke.

---

## 5. Definition of done (per book)

- [ ] Validator: **0 errors**; bands clean at all three levels; no `⟨pending⟩` text
- [ ] **`identity` block** declared (palette + `cover.kind`) — validator enforces; the reader skins itself to it (see §7)
- [ ] 12 endings, balanced 4/4/4; ≤8 flags, **each flag both set and read** (or listed in
      `arc_flags` if a later book reads it — validator enforces); all nodes reachable; 2–4 choices/node
- [ ] Lexicon ~250, complete in 9 languages, base-keyed; auto-gloss coverage checked
- [ ] **Native review applied** for all 8 languages (launch gate) — and A2 choices clarity-checked
- [ ] Art: at least Wave 1 delivered and the look locked; endings illustrated
- [ ] `state_out` set for the next book; series base lexicon updated if a word is now shared
- [ ] Deployed: WIP on a branch (preview only) until the review gate passes, **then** merged to `main`

---

## 6. Branch & deploy discipline

Build every book on a **branch**, never `main`. `main` is production and auto-deploys to the
live site, so it must only ever hold review-passed, learner-ready content. The branch builds as a
Vercel **preview**. A book merges to `main` only after its definition-of-done is fully checked —
in particular the native-review gate. (The flagship *The Address* lives on branch `flagship`;
production `main` remains the finished 40-passage original until the flagship clears its gates.)

---

## 7. Visual identity (per book)

Every book is its own world. Declare it once in the book JSON as `identity`; the reader reads
it at runtime and skins itself — **one reader renders every book, no per-book code.**

```json
"identity": {
  "name": "New City Nocturne",
  "mood": "A cold city at night; one warm window is the only light.",
  "palette": {
    "ground": "#0E1320", "surface": "#121a2c", "ink": "#F4EFE6",
    "muted": "#8A93A6", "line": "#26304a",
    "accent": "#E8A24C", "accentHot": "#F4BE72", "secondary": "#86C9B4"
  },
  "cover": { "kind": "nocturne", "glow": true },
  "type": { "display": "Fraunces", "ui": "Hanken Grotesk", "mono": "JetBrains Mono" }
}
```

- **palette** — all `#rrggbb`; all required except `accentHot`. `ground` (page), `surface`
  (reading card), `ink` (body text), `muted`, `line`, `accent` (the book's one warm "light" —
  it drives the lit-window, the choice `§ N`, glossed-word underlines, the progress bar and
  every glow), `secondary` (taglines / the dawn note). The reader maps these to its CSS tokens
  and applies them **scoped so the universal light "paper" reading mode still overrides** — so
  each book owns its night-world, and any reader who prefers paper still gets paper.
- **cover.kind** names the cover/landing treatment (`nocturne` for *The Address*); `glow` shows
  the single warm window.
- **type** is declarative for now (the three families are loaded globally); switching families
  needs the matching Google-Fonts `<link>` added too.

**Where identity is consumed**
- **Reader** (`read.html`) — fully dynamic via `applyIdentity(book)`; nothing hand-coded.
- **Book landing** (`/<slug>`) and the **library card** — currently hand-set to *match* the
  identity; when book two is templated these will be generated from it. Until then the JSON is
  the source of truth: keep those two surfaces in sync with it.

The validator enforces the block: palette keys present and hex-valid, `cover.kind` warned if
absent. A book with no identity fails the build.

**Every book is a standalone one-off.** There is no episode arc or shared series framing in the
UI — nothing says "Episode 2 of…". Each book is its own world with its own identity. (`episode`
stays in the data only as a shelf-ordering hint; it is never shown.) Also declare:

- `slug` (top-level) — the book's route, `/b/<slug>`.
- `identity.hero` — `{ line: {en, fr, es, it, de, pt, ru, zh, ar}, sub }`: the landing's
  eight-language morph sentence and the sub-line beneath it.

**How the three surfaces build themselves from data**
- **Reader** and **`/b/<slug>` landing** — dynamic from the JSON at runtime (palette, copy, CTA).
- **Library card** and **`/b/<slug>` prerender** (static meta + OG) — generated by the site build
  from the manifest, which now carries each book's `slug`, `blurb`, `levels` and `identity`.
- **Social card** — run `node scripts/build_og.mjs` locally to (re)generate `web/og-<slug>.png`
  from the book's identity, and **commit the PNG** (Vercel's build has no browser). The build
  copies it and stamps it into that book's `/b/<slug>` page meta.

So shipping book two = write its JSON (prose + lexicon + `identity` + `slug`) and commit its
OG PNG. No new code, no routing edits — one zero-config route `/b/:slug` serves them all.
