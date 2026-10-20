# The Interview — book 10 design & build plan

Book 10 of English Reading Adventures. The second **everyday** story (after *The Dinner*):
high-frequency vocabulary, a single protagonist, a tight clock, and a choice between the
honest road and the easy cheat. Built by transforming the shared 112-node topology
(episode-09, *The Dinner*) — same ids/edges/flag positions/ending valences — into a new
world, identity, flag names and prose.

---

## 1. Premise

It's **one o'clock**, and the interview that could change everything is at **two**. You've
been out of work; the rent is late; your dad — who always said you'd land on your feet — is
counting on you. But the morning has fallen apart: the trains are down, the rain is coming,
and the one document you needed is missing.

A smooth stranger, **Reese**, works the crowd outside the station. For a price he'll sell you
an easy way in — a planted reference, the questions in advance, a story that isn't yours.
And when you finally reach the room, the person on the panel is **Maya** — someone you fell
out with years ago, and haven't spoken to since.

One morning. Get there, as yourself, and earn it straight — or take the shortcut and find out
what it costs.

**Cast:** *you* (2nd person); **Reese** the fixer (the tempter); **Maya** the panellist from
your past (the reconciliation); **Dad** at home (the person you're doing it for — the calls);
a **stranger** you stop for on the way.

---

## 2. What governs the size

Same rule as the collection: ~112 reachable nodes, every one earning its place; no padding.
The shared topology already balances reach, flags and endings — we re-skin, we don't re-plumb.

## 3. Act structure & passage budget (inherited from ep09)

- **Act I — the morning falls apart** (home, the missing document, the ruined commute, Reese's
  first approach, the first good turn). ~nodes 1–39.
- **Act II — the way across the city** (Reese's full pitch, the queue/shortcut, the stranger,
  the waiting room, the other candidates, the face from the past). ~nodes 40–89.
- **Act III — the room, and the reckoning** (the interview itself, the clock, and how the
  morning adds up) + the 12 endings. ~nodes 90–131.

## 4. State model — the 8 flags (Interview ← Dinner)

| # | Pattern | The Interview | ← The Dinner |
|---|---|---|---|
| 1 | `has_X` — the core task resource | `ready` (prepared; your documents in hand) | has_dinner |
| 2 | `dodged_Y` — refuse the con | `dodged_reese` | dodged_dale |
| 3 | `paid_Y` — take the con | `paid_reese` | paid_dale |
| 4 | `found/welcomed_Z` — the relationship | `faced_maya` (own the past with the panellist) | welcomed_nora |
| 5 | `rallied_W` — bring people together | `rallied_room` (turn rival candidates into allies) | rallied_friends |
| 6 | `helped_stranger` — the good turn | `helped_stranger` | helped_stranger |
| 7 | `gave/shared_X` — generosity | `shared_notes` (give a rival your edge) | shared_food |
| 8 | `took_shortcut` — the risky shortcut | `jumped_queue` (cut a corner to beat the clock) | ran_road |

Each flag is set in ≤2 places and read in ≥1; gated choices always leave an ungated path.

## 5. Endings (12) — balanced 4 good / 4 neutral / 4 bad

- **Good:** *You earned it straight* (got the job, honestly) · *The door reopened* (secret —
  the old rift with Maya heals; gated on `faced_maya`) · *You lifted the whole room* (helped the
  other candidates; everyone did better) · *You did it as yourself*.
- **Neutral:** *A kindness came back* · *Not this one, but you made your mark* · *Late, but you
  made it* · *They'll remember you tried*.
- **Bad:** *They found out* (the cheat unravels) · *You left it too late* (missed the slot) ·
  *You froze* · *You didn't go*.

Two secret/clue-gated endings as in every book; the bad crossing-equivalent (`jumped_queue`
gone wrong — you're thrown out for cutting the line / caught sneaking in) is the hard ending.

## 6. Levels & lexicon

- Everyday, high-frequency vocabulary — the register of jobs, time, nerves and the city.
- `language_focus` (draft):
  - **A2:** the present and `going to`; the office, work and the clock.
  - **B1:** the first conditional and modals of advice/obligation; polite requests, arriving, asking.
  - **B2:** inference and register; honesty, nerves and second chances.
- **Lexicon** ~250–270 everyday words, complete in all 9 languages; auto-gloss coverage checked.
- Full per-passage **gists** in all 8 languages (112 each).

## 7. Visual identity

The first **cool-toned everyday** book — the warm light of people against the cold of glass,
institutions and a wet city morning. Warmth is the human moments (a lamp, a steadying call, a
hand); the cold is the station, the tower, the waiting room.

- **name:** *Interview at Two* — **mood:** "A cold morning, a warm chance: the interview that
  could change everything is at two, and the city is against you."
- **palette (draft; final in the JSON `identity`, must pass `check-contrast.mjs`):**
  `ground #12161C`, `surface #1B2129`, `ink #EEF1F4`, `muted #8A94A2`, `line #2A323D`,
  `accent #D98A3D` (warm amber — the human warmth), `accentHot #F0B36A`,
  `secondary #7FA8C9` (a calm steel blue).
- **cover.kind:** `office` — a warm-lit interview-room window in a cool glass tower at dusk, rain
  on the street, one warm window among cold ones. A new scene branch in `scripts/build_og.mjs`.
- **type:** inherited families (Fraunces / Hanken Grotesk / JetBrains Mono).
- **slug:** `the-interview`; **series:** `the-interview`; **episode:** 10. **hero.line** the
  nine-language morph sentence (draft EN: *"The interview that could change everything is at two
  o'clock, and the morning is already against you. Get there, as yourself, and earn it straight."*).

## 8. Build phases & gates

Gate each phase on `python3 scripts/build_book.py content/episode-10.json` coming back clean.

1. **Design sign-off** — this document. → commit.
2. **Graph skeleton** — transform ep09 → ep10 (flag map above, new identity, stub prose).
   *Gate:* validator 0 errors.
3. **Prose — B1 first**, then A2 and B2, in act batches; everyday vocabulary; levelised choices.
   *Gate:* per level, bands clean; no stub text left.
4. **Lexicon** — ~250–270 everyday words, 9 languages; gloss coverage checked.
5. **A2-choice clarity pass.**
6. **Gists** — full per-passage coverage in all eight languages.
7. **Art** — an `office` OG/cover scene; the per-passage scene set painted by ChatGPT to the
   briefs below; reader motif map + catalog entry (declared in `build-illustrations.mjs`).

Built on branch `book-10-the-interview`; merges to `main` only after the definition-of-done.

## 9. Art handoff — scene briefs (locked before writing)

Four portrait SVG scenes, `viewBox="0 0 800 1000"`, within the palette above, collection mood
*"warm light in cold places."* Filenames fixed so art is a pure drop-in:
`the-interview-commute.svg` · `-waiting.svg` · `-room.svg` · `-cafe.svg`.

- **commute** — a rainy, stalled station / city street: departure boards, a hurrying figure, a
  clock; the morning going wrong. Covers the travel/time/rush motifs. Also the **bad** ending.
- **waiting** — an office waiting area: a row of chairs, other candidates, a water cooler, a
  reception desk; Reese leaning in; the nerves and the good turns. Reused widely.
- **room** — the interview: a panel across a table, warm window light behind them, the face from
  your past, the moment of truth. The **neutral** ending.
- **cafe / cover** — a quiet café beat out of the rain (Reese's offer over coffee, or a steadying
  call home); the cover image and the **good** ending (warm, earned).

Endings: good→cafe, neutral→room, bad→commute; cover→cafe. Scene→motif mapping and titles are
set in `web/illustrations/catalog.json` and reproduced in `scripts/build-illustrations.mjs`.
