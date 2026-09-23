# First Light — book 3 design & build plan

A **standalone** book. It shares nothing with *The Address* or *The Night Market* except the
method and the house tone — no arc, no carried state, no shared characters, town or subject
(see [authoring-playbook.md](authoring-playbook.md) §1/§3). `state_in = []`, `arc_flags = []`.
The house voice holds: *quiet, humane, a little uncertain — not frightening. Warm light in cold
places.* Here that phrase is almost literal: a whole town goes dark and cold on the hardest
night of the winter, and the only light left is the kind people make and carry to each other.

Where *The Address* was one stranger crossing a cold city and *The Night Market* one young
person holding a warm stall, *First Light* is one young person carrying warmth **out** into the
dark — from door to door, keeping people alive until dawn. A new world: a small snowed-in town,
a power cut, a cold snap, and a night that has to be got through together.

---

## 1. Premise

It is the coldest night of the winter, and just after dark the power fails across the whole
town — lines down under the ice. The roads are blocked with snow, so the repair crews and any
help from outside can't get through before morning. The heating is off. The phones are patchy.
Everyone is told the same thing: sit tight, keep warm, wait for **first light**, when the crews
will come and the power should return.

But up the hill, **old Mrs Ada** — who was kind to you when you were small — depends on an
electric heater and has a weak chest. Without heat, she will not last a night this cold, and no
ambulance can reach her until the roads are cleared at dawn. It falls to you to go out into the
dark, freezing town — to gather what's needed (a paraffin heater, blankets, hot food, a working
phone, willing hands) and keep Mrs Ada, and whoever else you meet in trouble, warm and safe
until first light.

The night is not empty. There is **a man with a van** selling "emergency" generators and fuel
at frightened prices to anyone desperate enough — help that is really a hook, the same machine
as any scam. There is a **frozen river** that would cut the journey in half and could cut it off
for good. And there is **one warm light burning in the old Harrow house on the hill**, which has
stood empty for years, that no one can explain — the night's quiet pull.

**Theme:** what a town is *for*. The difference between shutting your own door and keeping it
open; between being warm alone and being warm together. Nobody is a villain except the man
selling warmth he doesn't have. The light in the cold is made of people.

**The through-line (the quiet pull):** the light in the "empty" Harrow house. Everyone says the
place has been dark for years. If you go and look — if you are the kind of person who checks a
light that shouldn't be on — you find old **Mr Harrow**, who moved quietly back months ago,
telling no one, and who has fallen in the dark with the cold coming down. You get him warm in
time; and it turns out he is the brother Mrs Ada stopped speaking to a lifetime ago. The mystery
pays off in a life saved and a door reopened — and it turns, as before, on whether you notice
and go.

**Recurring faces:** warmth lives in people.
- **Mrs Ada** — the frail neighbour the whole night is aimed at; the heart of it.
- **Mr Okafor at the corner shop** — opens up by candlelight, first help, lends what he can.
- **the van man** — the trap: warm words, cold prices.
- **a kid, Bex** — a younger child out in it, whom you help and who helps you.
- **Mr Harrow** — the light in the empty house; the mystery.

**The world.** Deep-winter dark and ice, snow on everything, breath in the air — but every
warm-lit window and candle is the accent colour, and the goal, first light, is warmth returning.
This drives the visual identity (§7): a cold blue-black town, candle-gold the one warm colour.

---

## 2. What "~120 passages" buys, and the rule that governs it

Same rule: **every passage is written three times (A2/B1/B2) and glossed in eight languages.**
~120 passages ≈ 360 authored prose units + a ~250-word book lexicon × 8. A passage earns its
place only if it adds **a real decision, a distinct beat, or texture the reader will feel.** We
hold the top of the CYOA band (~100–150) while staying shippable.

---

## 3. Act structure & passage budget

One night, from the blackout to first light.

| Act | Beat | Depth | Budget |
|---|---|---|---|
| **I — The lights go out** (dusk→first cold) | The blackout hits; candles and torches; the realisation about Mrs Ada up the hill; the phones patchy; how you start — the shop, a neighbour, straight up the hill; Mr Okafor's candlelit shop; the van man's first, friendly appearance; gathering the first supplies | The first fork: gather properly vs. rush up empty-handed; the heater/supply choice (has_heater); the seller's soft opening; learning the town has no help coming till dawn | ~30 |
| **II — Into the dark town** (deep night, the cold deepening) | Crossing the black frozen streets; the frozen-river shortcut; people in trouble on the way (a stuck car, a scared family, the kid Bex); the van man's pressure rising; knocking on doors to rally help; the strange light in the Harrow house; fuel and time running low | The frozen-river temptation (took_shortcut); a neighbour in need (helped_neighbour); giving away your own warmth (gave_warmth); the seller's plain offer (dodged/paid_seller); rallying the street (rallied_town); the Harrow-light mystery seeded and deepened | ~62 |
| **III — Toward first light** (before dawn) | The final push to Mrs Ada; the seller's last offer; whether you go and check the light; keeping the fire in till the power hums back; the grey line of dawn and the crews' headlights | The arrival scene: is she warm in time; the mystery resolved (Harrow found); the town's night added up; first light and what it finds | ~16 |
| **Endings** | see §5 | — | 12 |

**Target: ~120 passages, 12 endings.**

---

## 4. State model (the flags)

`state_in = []` — nothing carried. **Eight own flags**, each *set* at a clear moment and *read*
at a clear payoff; every gated choice keeps an ungated "otherwise" path (validator-enforced).

| Flag | Earned when | Pays off at |
|---|---|---|
| `has_heater` | you get a real paraffin/gas heater by decent means (the shop, a neighbour) | keeping Mrs Ada warm — the *warm till first light* win |
| `dodged_seller` | you refuse the van man's overpriced "emergency" fuel or generator | the clean-win gate; no con, no waste |
| `paid_seller` | you buy from the van man | the *fleeced in the dark* bad ending — money gone, still cold |
| `found_light` | you go and investigate the light in the empty Harrow house | the secret *light in the empty house* ending — a life saved |
| `rallied_town` | you knock on doors and get neighbours sharing fires, food and light | the communal *the whole street, awake* win |
| `helped_neighbour` | you stop to help someone else in trouble on the way | the *kindness returned* neutral ending |
| `gave_warmth` | you give your own blanket or coal to someone who has nothing | the *shared what little you had* neutral ending |
| `took_shortcut` | you cross the frozen river to save time | the *the ice gave way* bad ending |

`state_out` lists all eight (self-consistent JSON); it carries no meaning to any other book.
`arc_flags = []`.

---

## 5. Endings (12) — balanced 4 good / 4 neutral / 4 bad

Two are **secret** (clue/relationship-gated). Bespoke prose × 3 levels + bespoke art.

**Win (4)**
- *Warm till first light* — `has_heater`: you get Mrs Ada safely through the cold; at dawn the
  power hums back and the crews' lights come up the hill. The warm win.
- *The light in the empty house* — **secret**, `found_light`: you check the light no one can
  explain, find Mr Harrow fallen and freezing, and get him warm in time — and reopen a door
  between him and Mrs Ada that had been shut for a lifetime. The mystery pays off.
- *The whole street, awake* — `rallied_town`: no single heroic move, but you turned a frightened
  dark street into neighbours sharing one warm room, and everyone comes through together.
- *You did what you could* — `dodged_seller`: you refused the con, kept your head and your money,
  and got the essentials by decent means. Not perfect, but clean, honest, and enough.

**Neutral / bittersweet (4)**
- *The kindness returned* — `helped_neighbour`: you fell short of the whole night's goal, but a
  neighbour you stopped for takes you and Mrs Ada in by their fire. Warmth without the full win.
- *Shared what little you had* — `gave_warmth`: you gave your own warmth away and end the night
  cold yourself, but not alone — and something in the town has shifted. A start, not a save.
- *One more hour* — ungated fallback: you scrape through the worst of it; the power flickers back
  late and grudging. Not triumphant — just, in the end, relieved.
- *The town remembers* — ungated fallback: you didn't manage everything, but the street saw you
  go out into the dark when others didn't. You are, from tonight, someone the town knows.

**Lose (4)**
- *Fleeced in the dark* — `paid_seller`: you paid the van man for a generator that won't start
  and fuel that won't burn. The money's gone, and the cold is exactly where it was.
- *The ice gave way* — `took_shortcut`: the frozen river was a trap; it nearly takes you, and it
  takes the night — you reach the hill soaked, frozen, and far too late.
- *Too late up the hill* — ungated fallback: you spent the night on the wrong things, and reach
  Mrs Ada cold and failing; by dawn she is being carried down to a waiting ambulance.
- *You kept your door shut* — ungated fallback: you stayed warm and safe behind your own door and
  never went out. Nothing bad happened to *you*. You will think about it for a long time.

At least one clearly good and one clearly bad (validator warns otherwise). ✔

---

## 6. Levels & lexicon

- **Three levels** (A2/B1/B2), prose per level over one shared graph; validator holds each
  passage in band. **On-demand passage gist** per the flagship (French first, then the pivotal
  beats + 12 endings; others as translators arrive).
- **Book lexicon ~250 words**, base-keyed, English + 8 languages, embedded in the JSON — tilted
  to **this** subject: cold and snow (*frost, ice, freeze, snow, blizzard, shiver*), light and
  heat (*candle, torch, lantern, heater, paraffin, coal, blanket, fire, spark*), the town and
  the crisis (*power cut, line, crew, neighbour, hill, van, generator*). Shares no file with
  the other books; a recurring word is re-authored to a consistent gloss.
- **The A2-choice caveat (bible §6b):** the branching inference is identical across levels, so at
  A2 the **choice text** must be unambiguous and low-inference. Required in the native review.
- **Native-language review is the launch gate.**

**Language focus** (per level, for the classroom):
- A2 — *imperatives and going to; the home, weather, and warmth.*
- B1 — *first conditional and modals of advice; helping, warning, and planning.*
- B2 — *inference, obligation and conditionals; community, risk and responsibility.*

---

## 7. Visual identity (per book)

Its own world: a **frozen town in a blackout**, dark and blue with cold, one warm window the
only light. The visual opposite of *The Night Market*'s heat and of *The Address*'s city.

- **name:** *Cold Snap* — **mood:** "A frozen town gone dark; the only light is the warmth people
  carry to each other."
- **palette:** an icy-dark set — a deep blue-black ground and surface, a cold snow-white/ice-blue
  **secondary**, and a single warm **candle-gold accent** (the flame, the lit window, the choice
  `§ N`, glossed underlines, the progress bar) — distinct from book 1's amber-on-navy and book 2's
  ember-on-brown by being colder and bluer, with the warmth reserved and small. Final values in
  the JSON `identity` block.
- **cover.kind:** `candlelight` (a single warm-lit window in a dark, snow-covered street) with
  `glow: true`. A new scene branch is added to `scripts/build_og.mjs` for it, so the social card
  is a genuinely different picture — a frozen street, one gold window — not a recolour.
- **type:** inherited families (Fraunces / Hanken Grotesk / JetBrains Mono).
- **slug:** `first-light`; **hero.line** the eight-language morph sentence; **sub** the same
  learner promise.

Shipping = write its JSON (prose + lexicon + `identity` + `slug`) and its OG card, plus the
free per-passage emblem set (a cold-snap motif set, added to the reader's per-book `__ART`).
One zero-config route `/b/first-light` serves it.

---

## 8. Build phases & gates

Gate each phase on `python3 scripts/build_book.py content/episode-03.json --lexicon
content/lexicon.json` coming back clean.

1. **Design sign-off** — this document. → commit.
2. **Graph skeleton** — ~120 nodes, ids + choices + gotos + flags + endings, one-line stubs.
   *Gate:* validator 0 errors; reachable; 12 endings 4/4/4; 8 flags each set+read; every gated
   choice keeps an ungated path.
3. **Prose — B1 first**, then A2 (simplify) and B2 (enrich), in act batches; levelise choices.
   *Gate:* per level, bands clean; no stub text left.
4. **Lexicon** — ~250 words, complete in 9 languages; auto-gloss coverage checked.
5. **Native review** — 8-language pass + A2-choice clarity. *Launch gate.*
6. **Art** — free per-passage emblems (cold-snap motif set) + a `candlelight` OG scene; painted
   art optional, dropped in later at `images/first-light/ep-03/<id>.webp`.

Built on branch `book-03-first-light`; merges to `main` only after the definition-of-done.
