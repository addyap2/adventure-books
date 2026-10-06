# Visual / graphics audit prompt

A ready-to-use prompt for a repo-aware AI assistant (e.g. ChatGPT with
repository access) to run a rigorous, site-wide visual and graphics audit of
English Reading Adventures. Paste everything in the fenced block below into the
assistant, with this repository connected.

The highest-value part is the **contrast matrix**: every book's palette hex
values live in `content/episode-0N.json`, so the assistant can compute real WCAG
ratios instead of guessing — which is exactly where the dark palettes tend to
hide problems.

---

```text
You have full read access to this repository ("English Reading Adventures," a
static site of branching reading-adventure stories for English learners). Conduct
a rigorous, site-wide visual / graphics audit from the source. Be specific and
critical — find problems, cite exact files and line numbers, and propose concrete
fixes with real values. Do not pad or reassure.

── HOW THE VISUAL SYSTEM IS BUILT (read these) ─────────────────────────────
• Books/content: content/episode-01.json … episode-07.json. Each has an
  `identity` object: name, mood, palette{ground, surface, ink, muted, line,
  accent, accentHot, secondary}, cover{kind, glow, focal, alt}, type{display,
  ui, mono}, hero{line{en+8 languages}, sub}. 7 books, slugs: the-address
  (kind nocturne), the-night-market (lantern), first-light (candlelight),
  cool-of-evening (dusk), the-keeper (beacon), the-orchard (frostfire),
  high-water (highwater). Each book is its own "world" — must feel DISTINCT yet
  part of ONE system.
• Covers + social cards: all hand-built SVG line-art in scripts/build_og.mjs
  (functions *Scene(c), plus ogHTML/coverHTML; scene chosen by cover.kind).
  Rendered to web/cover-<slug>.png and web/og-<slug>.png.
• Reader UI: web/index.html (template → dist/read/<slug>.html). Landing:
  web/library.html (→ dist/index.html). It skins CSS variables from each
  book's palette; defines window.__MOTIFS (per-passage SVG emblems) and
  window.__ART[series] (node→motif map); has large outcome "ending" scenes
  tinted good=green / neutral=amber / bad=blue (search "ending scenes by
  outcome"). Default dark "nocturne" theme + opt-in light "paper" theme.
  Arabic (ar) is right-to-left; ru/zh/ar are non-Latin scripts.
• Type: Fraunces (display/serif), Hanken Grotesk (UI), JetBrains Mono (labels).
• Build: scripts/build-site.mjs → dist/. Content validator: scripts/build_book.py.
If you can run `node scripts/build-site.mjs` and/or render the pages/PNGs, do so
and include what you observe; otherwise audit statically from the source above.

── AUDIT THESE DIMENSIONS ──────────────────────────────────────────────────
1.  System coherence — do all 7 books read as one family? Shared grid, spacing,
    components, label style, iconography voice.
2.  Per-book identity — distinct AND legible? Any palette too close to another,
    muddy, or off-concept for its story?
3.  Colour & contrast — READ the hex values from each palette and COMPUTE WCAG
    contrast ratios for the real text/UI pairings in BOTH themes: ink-on-ground,
    ink-on-surface, muted-on-ground, accent-on-ground, accent text on buttons,
    line/border visibility. List every pair that fails AA (4.5 normal / 3.0
    large) with its ratio, per book. Check the light theme too.
4.  Typography — hierarchy, pairing, sizes, measure/line-length, rhythm, the
    mono labels, italics/display usage; flag likely widows/overflow (e.g. long
    titles in the OG card title-size logic, long hero lines).
5.  Illustration craft — inspect the *Scene() SVG code AND the rendered PNGs:
    consistency of line weight/stroke style across scenes, reused vs one-off
    primitives, focal clarity, scale, anything weaker or off-voice than its
    siblings (compare beaconScene / frostfireScene / highwaterScene etc.).
    Review __MOTIFS and each __ART map for coverage, repetition, wrong-fit
    emblems, or missing nodes.
6.  Layout / spacing / components — reading column, choice buttons, chips,
    cards, whitespace, alignment.
7.  Responsive / mobile — phone-first: touch targets, reflow, truncation,
    any horizontal-scroll risk.
8.  Accessibility — contrast (above); visible focus states; image alt text
    (identity.cover.alt + inline SVG aria/role); prefers-reduced-motion;
    and especially correct RTL handling for Arabic and clean CJK/Cyrillic/
    Arabic rendering given the chosen fonts.
9.  Social / OG cards — legibility at feed size, title fit, safe margins, scrim
    legibility over the scene, does each sell its book.
10. Brand marks / motion — favicon (web/favicon.svg), logo, transitions.

── CROSS-CHECK FOR CONSISTENCY GAPS ────────────────────────────────────────
Diff the 7 `identity` objects against each other: any book missing fields the
others have, inconsistent value conventions, or palette outliers. Flag anything
where one book silently diverges from the house pattern.

── OUTPUT ──────────────────────────────────────────────────────────────────
1. Executive summary (5–8 lines): overall verdict + the 3 highest-impact fixes.
2. Prioritised findings table — Priority (P0 blocker / P1 / P2 polish),
   Location (file:line), Issue, Why it matters, Concrete fix (with a specific
   value/hex/px/ratio). Most severe first. Omit a dimension if genuinely fine.
3. Contrast matrix — per book, the failing pairs with computed ratios (dark +
   light).
4. Per-book scorecard (1–5): identity, legibility, illustration, contrast.
5. "Working well" — 3–5 real strengths to preserve.
6. System-level recommendations — tokens, type scale, contrast rules,
   illustration guidelines that would raise the whole site at once.

Propose specific values, never vague directions. If you change a palette hex,
give the new value and its resulting contrast ratio.
```
