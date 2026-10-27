# Moving Day — book 11 design & build plan

Book 11 of English Reading Adventures. The third **everyday** story (after *The Dinner* and
*The Interview*): high-frequency vocabulary, a single protagonist, a tight clock, and a choice
between the honest road and the easy cheat. Built by transforming the shared 112-node topology
(episode-10, *The Interview*): same ids/edges/flag positions/ending valences, with a new world,
identity, flag names and prose.

---

## 1. Premise

It's early afternoon, and you're moving your mum, **Edie**, into a new ground-floor flat — she
can't manage the stairs in the old place any more, and it all has to be done **before dark**.
The van is late, the key to the new flat won't turn, and the removal man, **Bray**, keeps
raising his price to muscle it all in for you.

Somewhere in the chaos a box with your late dad's things goes missing. An old neighbour needs
a hand. And then **Cass** — your sister, who you fell out with years ago — turns up on the
doorstep to help carry.

One short afternoon. Get Mum home before dark, honestly, and decide who you let carry the load
with you.

**Cast:** *you* (2nd person); **Bray** the removal man (the tempter); **Cass** your estranged
sister (the reconciliation); **Edie**, your mum, waiting at the new place (the person you're
doing it for); a **neighbour** you stop to help.

---

## 2. What governs the size

Same rule as the collection: ~112 reachable nodes, every one earning its place; no padding.
The shared topology already balances reach, flags and endings — we re-skin, we don't re-plumb.

## 3. Act structure & passage budget (inherited from ep10)

- **Act I — the old place empties** (the bare rooms, the late van, the first boxes, Bray's first
  approach, the first good turn). ~nodes 1–39.
- **Act II — the load and the street** (Bray's full pitch, the overload shortcut, the neighbour,
  the stuck door, the block pitching in, the sister on the doorstep). ~nodes 40–89.
- **Act III — the new place, before dark** (carrying the last of it in, the fading light, and how
  the day adds up) + the 12 endings. ~nodes 90–131.

## 4. State model — the 8 flags (Moving Day ← The Interview)

| # | Pattern | Moving Day | ← The Interview |
|---|---|---|---|
| 1 | `has_X` — the core task | `moved_in` (everything carried in) | ready |
| 2 | `dodged_Y` — refuse the con | `dodged_bray` | dodged_reese |
| 3 | `paid_Y` — take the con | `paid_bray` | paid_reese |
| 4 | `found/welcomed_Z` — the relationship | `welcomed_cass` (make up with your sister) | faced_maya |
| 5 | `rallied_W` — bring people together | `rallied_block` (the neighbours pitch in) | rallied_room |
| 6 | `helped_stranger` — the good turn | `helped_stranger` | helped_stranger |
| 7 | `gave/shared_X` — generosity | `shared_load` (lend a hand / give away what you can't take) | shared_notes |
| 8 | `took_shortcut` — the risky shortcut | `overloaded` (pile it high to save trips) | jumped_queue |

Each flag set in ≤2 places and read in ≥1; gated choices always leave an ungated path.

## 5. Endings (12) — balanced 4 good / 4 neutral / 4 bad

- **Good:** *Home by dark* (all moved in) · *The door reopened* (secret — the rift with Cass
  heals; gated on `welcomed_cass`) · *The whole block pitched in* (rallied) · *You did it straight*
  (saw off Bray).
- **Neutral:** *A kindness came back* · *Lighter than you came* (gave things away, travel light)
  · *A bit late, but home* · *They'll remember you tried*.
- **Bad:** *Bray took you for a ride* (paid, overcharged, your things held over you) · *You should've
  made two trips* (`overloaded` gone wrong — a fall, the precious box broken) · *Half in, half out*
  (ran out of light) · *You walked away*.

Two secret/clue-gated endings as in every book; the bad shortcut outcome (`overloaded` → a drop
on the stairs) is the hard ending.

## 6. Levels & lexicon

- Everyday, high-frequency vocabulary — the register of home, lifting, letting go and starting over.
- `language_focus` (draft):
  - **A2:** the present and `going to`; the house, moving and carrying.
  - **B1:** the first conditional and modals of ability/obligation; lifting, lending and letting go.
  - **B2:** inference and register; home, memory and starting over.
- **Lexicon** ~250–270 everyday words, complete in all 9 languages; auto-gloss coverage checked.
- Full per-passage **gists** in all 8 languages (112 each).

## 7. Visual identity

The third everyday book, and a day that runs from afternoon to dusk: warm cardboard light against
a cooling autumn sky, a home emptying and a home filling.

- **name:** *Home by Dark* — **mood:** "The last day in the old place and the first in the new;
  boxes, bare rooms, and a short autumn afternoon to get your mum home before dark."
- **palette (draft; final in the JSON `identity`, must pass `check-contrast.mjs`):**
  `ground #14110D`, `surface #201A14`, `ink #F2ECE2`, `muted #9C9286`, `line #322820`,
  `accent #CE7A4A` (warm terracotta / cardboard), `accentHot #E9A05F`,
  `secondary #88A0B8` (a cool dusk blue — the evening sky, the new place).
- **cover.kind:** `moving` — a small removal van at the kerb at dusk, its back open, boxes on the
  pavement, a warm-lit doorway, a figure carrying a box toward it. A new scene branch in
  `scripts/build_og.mjs`.
- **type:** inherited families (Fraunces / Hanken Grotesk / JetBrains Mono).
- **slug:** `moving-day`; **series:** `moving-day`; **episode:** 11. **hero.line** the nine-language
  morph sentence (draft EN: *"You're moving your mum into a new place today, and the light is going.
  Get her home before dark — the honest way, with whoever will carry it with you."*).

## 8. Build phases & gates

Gate each phase on `python3 scripts/build_book.py content/episode-11.json` coming back clean.

1. **Design sign-off** — this document. → commit.
2. **Graph skeleton** — transform ep10 → ep11 (flag map above, new identity, stub prose).
   *Gate:* validator 0 errors.
3. **Prose — B1 first**, then A2 and B2, in act batches; everyday vocabulary; levelised choices.
   *Gate:* per level, bands clean; no stub text left.
4. **Lexicon** — ~250–270 everyday words, 9 languages; gloss coverage checked.
5. **A2-choice clarity pass.**
6. **Gists** — full per-passage coverage in all eight languages.
7. **Art** — a `moving` OG/cover scene; the per-passage scene set painted by ChatGPT to the briefs
   below; reader motif map + catalog entry (declared in `build-illustrations.mjs`).

Built on branch `book-11-moving-day`; merges to `main` only after the definition-of-done.

## 9. Art handoff — scene briefs (locked before writing)

Four portrait SVG scenes, `viewBox="0 0 800 1000"`, within the palette above, collection mood
*"warm light in cold places."* Filenames fixed so art is a pure drop-in:
`moving-day-empty.svg` · `-van.svg` · `-stairwell.svg` · `-newplace.svg`.

- **empty** — the old flat emptying: bare rooms, pale rectangles where pictures hung, a few last
  boxes, dusty afternoon light through an uncurtained window. Covers the taking-stock / letting-go
  motifs. Also the **bad** ending.
- **van** — the street at dusk: a small removal van, back open, boxes stacked on the wet pavement,
  Bray by the tailgate, a cooling sky. The load, the con, the shortcut.
- **stairwell** — a dim stairwell / doorway: someone carrying a box, a stuck key in a new door,
  the neighbour, and Cass on the step. The **neutral** ending. Reused widely.
- **newplace / cover** — the new ground-floor flat filling with warm lamplight at dusk, a box
  half-unpacked, a chair by the window; home. The cover image and the **good** ending.

Endings: good→newplace, neutral→stairwell, bad→empty; cover→newplace. Scene→motif mapping and
titles are set in `web/illustrations/catalog.json` and reproduced in `scripts/build-illustrations.mjs`.
