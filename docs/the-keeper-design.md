# The Keeper — book 5 design & build plan

A **standalone** book. It shares nothing with *The Address*, *The Night Market*, *First Light* or
*The Cool of Evening* except the method and the house tone — no arc, no carried state, no shared
characters, place or subject (see [authoring-playbook.md](authoring-playbook.md) §1/§3).
`state_in = []`, `arc_flags = []`. The house voice holds: *quiet, humane, a little uncertain —
not frightening. Warm light in cold places.* Here the phrase is almost the whole plot: on a
storm-black coast, the one light that keeps ships off the rocks is the one you have to keep
burning, by hand, till morning.

Where *First Light* carried warmth out into a frozen town and *The Cool of Evening* held a busload
through a killing afternoon, *The Keeper* is one person keeping a single light alive through a
storm — for an old keeper who has gone down, and for a boat somewhere out in the dark. A new
world: a remote lighthouse, a rising gale, a lamp that must not go out, and a night that has to be
watched through to first light.

---

## 1. Premise

The worst storm of the year comes in after dark. The power fails along the coast, and the
lighthouse's automatic beacon dies with it — and at that exact moment, coming down the wet iron
stairs, the old keeper **Nan Bright** falls and cannot get up, her breath short and a leg gone
under her. The great lamp at the top of the tower is old enough to be worked by hand — oil, wick,
a lens that must be wound round like a clock — but it is dark now, and out beyond the point a
boat's small lights are lifting and falling in the swell, trying to find the harbour mouth.

Keeping the light burning is suddenly, entirely on you. Nan cannot climb. The lifeboat cannot
launch into a sea like this until the storm eases or dawn comes. The one thing between that boat
and the rocks is a light — and the only hands to keep it lit are yours. So you climb, and you
keep the watch: find the oil, trim the wick, wind the lens, keep Nan warm and breathing at the
foot of the stairs, and hold the beam steady until first light.

The night is not empty. Down in the cove works a **wrecker** — a man who *wants* the light dark,
so a ship will strike the rocks and the sea will hand him the salvage. He comes up smiling, with
oil to sell and a strong back to offer and reasons the light isn't your problem — help that is
really a hook, the same machine as any con. There is a **cliff path down to the cove** that would
halve the way to the water and could take you straight off the edge in a wind like this. And far
out, past where any harbour boat should be, there is **a second light on the water** that no one
can explain — the night's quiet pull.

**Theme:** what a light is *for*. The difference between a light that guides people home and one
that lures them onto the rocks; between keeping the watch for strangers and barring your own door.
Nobody is a villain except the man who wants the dark. The light in the storm is made of people.

**The through-line (the quiet pull):** the second light out on the water. Everyone says no boat
would be out past the point tonight. If you go and look — if you are the kind of person who
answers a light that shouldn't be there — you find old **Ash**, a fisher who went out before the
weather turned and is now on the rocks with a swamped boat, and you get them off in time; and it
turns out Ash is the son Nan Bright stopped speaking to years ago. The mystery pays off in a life
saved and a door reopened — and it turns, as ever, on whether you notice and go.

**Recurring faces:** the light lives in people.
- **Nan Bright** — the old keeper, hurt at the foot of the stairs; the heart of the night; the
  light is hers, and now yours.
- **Tam at the coast station** — opens the oil store, first help, works the crackling radio.
- **the wrecker** — the trap: a false light, a cold profit in other people's wrecks.
- **old Bosun Carrick** — knows this coast in the dark; warns you off the cliff path.
- **Ash** — the light on the water; the mystery; the door reopened.

**The world.** Storm-black sea and sky, rain driven flat, the tower shuddering — but the beam is
the one warm gold thing that reaches out across all that dark, and the goal, first light, is the
storm breaking and a boat making harbour. This drives the visual identity (§7): a slate-black
coast, beacon-gold the one warm colour.

---

## 2. What "~120 passages" buys, and the rule that governs it

Same rule as every book: **every passage is written three times (A2/B1/B2) and glossed in eight
languages.** ~120 passages ≈ 360 authored prose units + a ~250-word book lexicon × 8. A passage
earns its place only if it adds **a real decision, a distinct beat, or texture the reader will
feel.** We hold the top of the CYOA band (~100–150) while staying shippable.

---

## 3. Act structure & passage budget

One storm night, from the light going dark to first light.

| Act | Beat | Depth | Budget |
|---|---|---|---|
| **I — The light goes out** (storm hits → the fall) | The beacon dies; Nan falls on the stairs; the boat's lights seen offshore; how you start — the oil store, the radio to Tam, or straight up the tower; what the tower holds; the wrecker's first, friendly appearance; Bosun Carrick reading the weather | The first fork: get the light going properly vs. rush up half-ready; the oil/lamp choice (`has_light`); the wrecker's soft opening; learning no lifeboat comes till dawn | ~30 |
| **II — The long watch** (deep storm, the worst hours) | Working the lamp and the tower; the cliff-path shortcut to the cove; people in trouble on the way (a stranded fisher, a family in a flooding cottage, the boat closing on the rocks); the wrecker's pressure rising; rousing the coast for hands and signal fires; the second light on the water; oil and time running low | The cliff-path temptation (`took_shortcut`); a stranger in need (`helped_stranger`); giving away your own lamp/coat (`gave_shelter`); the wrecker's plain offer (`dodged`/`paid_wrecker`); rallying the coast (`rallied_coast`); the light-on-the-water mystery seeded and deepened | ~62 |
| **III — Toward first light** (before dawn) | The final push to hold the beam; the wrecker's last offer; whether you go to the light on the water; keeping Nan warm and the wick trimmed till the sky greys; the storm breaking and the lifeboat's lamp coming round the point | The close: did the light hold and the boat make harbour; the mystery resolved (Ash found); the night added up; first light and what it finds | ~16 |
| **Endings** | see §5 | — | 12 |

**Target: ~120 passages, 12 endings.**

---

## 4. State model (the flags)

`state_in = []` — nothing carried. **Eight own flags**, each *set* at a clear moment and *read* at
a clear payoff; every gated choice keeps an ungated "otherwise" path (validator-enforced). This is
the proven flag machine, re-skinned honestly for the coast (warmth/water → the light and its oil,
the van/pickup → the wrecker, the frozen river/open flats → the cliff path, the light in the empty
house / the smoke at the siding → the light on the water).

| Flag | Earned when | Pays off at |
|---|---|---|
| `has_light` | you get the great lamp burning properly by decent means (find the oil, trim the wick, wind the lens) | holding the beam through the night — the *the light held* win |
| `dodged_wrecker` | you refuse the wrecker's oil, money or "help" | the clean-win gate; no con, no dark |
| `paid_wrecker` | you take the wrecker's deal | the *you lit the wrong way* bad ending — complicit, a ship struck |
| `found_boat` | you go and answer the second light out on the water | the secret *the light on the water* ending — a life saved |
| `rallied_coast` | you rouse the shore for hands on the rope and signal fires | the communal *the whole coast, awake* win |
| `helped_stranger` | you stop to help someone else in trouble in the storm | the *kindness returned* neutral ending |
| `gave_shelter` | you give your own coat, lamp or shelter to someone with none | the *shared what you had* neutral ending |
| `took_shortcut` | you take the cliff path down to the cove in the gale | the *the rocks took it* bad ending |

`state_out` lists all eight (self-consistent JSON); it carries no meaning to any other book.
`arc_flags = []`.

---

## 5. Endings (12) — balanced 4 good / 4 neutral / 4 bad

Two are **secret** (clue/relationship-gated). Bespoke prose × 3 levels + bespoke art.

**Win (4)**
- *The light held* — `has_light`: you kept the beam burning all night; at first light the storm
  breaks, the lifeboat comes round the point, and the boat you were lighting makes the harbour
  mouth. The warm win.
- *The light on the water* — **secret**, `found_boat`: you answered the light no one could explain,
  found old Ash swamped on the rocks and got them off in time — and reopened a door between Ash and
  Nan Bright that had been shut for years. The mystery pays off.
- *The whole coast, awake* — `rallied_coast`: no single heroic move, but you turned a frightened
  shore into people on the rope and signal fires along the head, and everyone came through together.
- *You did what you could* — `dodged_wrecker`: you refused the con, kept your head, and kept the
  light by decent means. Not perfect, but clean, honest, and enough.

**Neutral / bittersweet (4)**
- *The kindness returned* — `helped_stranger`: you fell short of the whole night's goal, but the
  fisher you stopped for gets you and Nan to safety and helps hold the light. Rescue without the
  full win.
- *Shared what you had* — `gave_shelter`: you gave your own coat and lamp away and end the night
  cold yourself, but not alone — and something on the coast has shifted. A start, not a save.
- *One more hour* — ungated fallback: you scrape through the worst of it; the storm eases late and
  grudging, the boat limps in on its own. Not triumphant — just, in the end, relieved.
- *The coast remembers* — ungated fallback: you didn't manage everything, but the shore saw you
  climb to the lamp when others barred their doors. You are, from tonight, someone this coast knows.

**Lose (4)**
- *You lit the wrong way* — `paid_wrecker`: you took the wrecker's deal, and the light served the
  wrong master; a ship struck the rocks in the dark and the sea took what it wanted. The money's
  cold, and so is the shore by morning.
- *The rocks took it* — `took_shortcut`: the cliff path was a trap; the wind nearly takes you off
  the edge, and it takes the night — you reach the cove soaked, broken and far too late.
- *Dark too long* — ungated fallback: you spent the night on the wrong things, and the light went
  dark too long; by dawn there is wreckage on the shore and a search along the tideline.
- *You barred the door* — ungated fallback: you stayed safe and dry inside and never climbed to the
  lamp. Nothing bad happened to *you*. You will think about it for a long time.

At least one clearly good and one clearly bad (validator warns otherwise). ✔

---

## 6. Levels & lexicon

- **Three levels** (A2/B1/B2), prose per level over one shared graph; validator holds each passage
  in band. **On-demand passage gist** per the flagship (French first, then the pivotal beats + 12
  endings; others as translators arrive).
- **Book lexicon ~250 words**, base-keyed, English + 8 languages, embedded in the JSON — tilted to
  **this** subject: storm and sea (*storm, gale, wind, wave, tide, rock, cliff, spray, surf,
  harbour, shore, coast, drown*), the light and the lamp (*light, lamp, beam, wick, oil, flame,
  lens, glass, spark, dark*), and the crisis (*keeper, tower, boat, sail, oar, rope, signal, wreck,
  rescue, lifeboat, soaked*). Shares no file with the other books; a recurring word is re-authored
  to a consistent gloss for the learner's sake.
- **The A2-choice caveat (bible §6b):** the branching inference is identical across levels, so at
  A2 the **choice text** must be unambiguous and low-inference. Required when levelising the choices.

**Language focus** (per level, for the classroom):
- A2 — *imperatives and going to; the sea, weather and the body.*
- B1 — *the first conditional and modals of advice; warning, helping and planning.*
- B2 — *inference, obligation and conditionals; duty, risk and responsibility.*

---

## 7. Visual identity (per book)

Its own world: a **storm-black coast** at night, one lighthouse throwing a single gold beam across
a wild sea. The visual sibling of the other night books, but colder and wetter — slate and spray,
with the beam the one warm thing.

- **name:** *Tempest* — **mood:** "A storm-black coast; the only light is the beam that keeps ships
  off the rocks."
- **palette:** a storm set — a deep slate blue-black **ground** and **surface**, a cold sea-spray
  **secondary**, and a single warm **beacon-gold accent** (the beam, the lit lamp, the choice
  `§ N`, glossed underlines, the progress bar) — distinct from the other books by being colder and
  greyer, the gold sharp against wet slate. Final values in the JSON `identity` block.
- **cover.kind:** `beacon` (a lighthouse throwing a gold beam over a stormy sea, spray at the rocks)
  with `glow: true`. A new scene branch is added to `scripts/build_og.mjs` for it, so the social
  card and library cover are a genuinely different picture — a tower, a beam, a black sea — not a
  recolour.
- **type:** inherited families (Fraunces / Hanken Grotesk / JetBrains Mono).
- **slug:** `the-keeper`; **series:** `the-keeper`; **episode:** 5. **hero.line** the
  eight-language morph sentence; **sub** the same learner promise.

Shipping = write its JSON (prose + lexicon + `identity` + `slug`) and its OG card, plus the free
per-passage emblem set (a storm/coast motif set added to the reader's per-book `__ART`) and a
wordless `cover-the-keeper.png` for the library card. One zero-config route `/b/the-keeper`
serves it.

---

## 8. Build phases & gates

Gate each phase on `python3 scripts/build_book.py content/episode-05.json --lexicon
content/lexicon.json` coming back clean.

1. **Design sign-off** — this document. → commit.
2. **Graph skeleton** — ~120 nodes, ids + choices + gotos + flags + endings, one-line stubs.
   *Gate:* validator 0 errors; reachable; 12 endings 4/4/4; 8 flags each set+read; every gated
   choice keeps an ungated path.
3. **Prose — B1 first**, then A2 (simplify) and B2 (enrich), in act batches; levelise choices.
   *Gate:* per level, bands clean; no stub text left.
4. **Lexicon** — ~250 words, complete in 9 languages; auto-gloss coverage checked.
5. **A2-choice clarity pass** — each A2 choice checked unambiguous and low-inference. ✓ done
6. **Art** — free per-passage emblems (a storm/coast motif set) + a `beacon` OG/cover scene;
   painted art optional, dropped in later at `images/the-keeper/ep-05/<id>.webp`.

Built on branch `book-05-the-keeper`; merges to `main` only after the definition-of-done.
