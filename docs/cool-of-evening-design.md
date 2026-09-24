# The Cool of Evening — book 4 design & build plan

A **standalone** book. It shares nothing with *The Address*, *The Night Market* or *First Light*
except the method and the house tone — no arc, no carried state, no shared characters, place or
subject (see [authoring-playbook.md](authoring-playbook.md) §1/§3). `state_in = []`,
`arc_flags = []`. The house voice holds: *quiet, humane, a little uncertain — not frightening.*

The platform's through-phrase is "warm light in cold places." Book 4 turns it inside out on
purpose: the danger here is not cold and dark but **heat and glare**, and the mercy people carry
to one another is not warmth but its opposite — **water and shade**. The shape of the kindness is
the same; only the weather is reversed. Where *First Light* was one young person carrying warmth
out into a frozen town, *The Cool of Evening* is one traveller keeping a busload of strangers alive
through the killing hours of a desert afternoon — sharing water, making shade, and deciding, over
and over, what you owe the people stranded beside you.

A new world: a cheap long-distance bus, a single hot road across an empty plain, a breakdown at
noon, and an afternoon that has to be got through together before the sun will let anyone move.

---

## 1. Premise

It is the hottest part of the day. A cheap cross-country bus, hours from the last town and hours
from the next, coughs, shudders and dies on an empty desert road — the engine gone, steam under
the hood. There is no phone signal out here. The driver, **Mr Bello**, is well-meaning and
completely out of his depth; the spare is flat and the radio dead. The one certainty everyone is
given is the same: nothing moves in this heat, help won't come until the sun drops, so sit in
what shade there is and **wait for the cool of the evening**, when a truck might pass or the
engine might start.

But the heat is not something you can simply wait out. On the bus is **Sami**, a child of about
eight travelling alone — put aboard by an aunt to reach a parent in the city — frightened, and
already going quiet and dizzy with the heat and too little water. A child this small will not last
the worst hours without water and shade, and no help can reach the bus until evening. It falls to
you to keep Sami — and whoever else on the bus is in trouble — cool, watered and safe until the
heat breaks.

The afternoon is not empty. A **man in a pickup truck** stops on the shoulder, all smiles,
selling warm bottled water and "lifts to town" at frightening prices to anyone desperate enough —
help that is really a hook, the same machine as any scam. Out across the flats stands **the far
ridge**, close enough to tempt: cut straight across the open ground on foot and you might reach it
in an hour — or the flats might go on forever and the heat take you. And on a low siding under
that ridge, where an old rail-stop has stood empty and shuttered for years, there is **a thread
of smoke and a windmill slowly turning** that no one can explain — the afternoon's quiet pull.

**Theme:** what you owe the strangers stranded beside you. The difference between capping your own
bottle and passing it down the aisle; between surviving alone and surviving together. Nobody is a
villain except the man selling water he doesn't have to spare. The shade in the heat is made of
people.

**The through-line (the quiet pull):** the smoke and the turning windmill at the "abandoned"
siding. Everyone says the place has been shut for years. If you go and look — if you are the kind
of person who checks a chimney that shouldn't be smoking — you find old **Mr Faro**, who moved
quietly back to the empty station-house months ago, telling no one, and who has gone down in the
heat with no one to know. You get him cool and watered in time; and it turns out the old siding
still has what the road has lost — **a deep, cold well and a working radio set**. Saving him saves
the whole bus: water for everyone, and the call that finally brings help. The mystery pays off in
a life saved and a road reopened — and it turns, as ever, on whether you notice and go.

**Recurring faces:** mercy lives in people.
- **Sami** — the lone child the whole afternoon is aimed at; the heart of it.
- **Mr Bello** — the driver; kind, ashamed, out of his depth; first to lend what the bus has.
- **the pickup man** — the trap: cool smile, warm water, cold prices.
- **Auntie Rose** — an older traveller who knows this road and this country; warns you off the
  flats, reads the sky, steadies the bus.
- **Mr Faro** — the smoke at the empty siding; the mystery; the well and the radio.

**The world.** A bleached, enormous sky, ochre sand and a heat-shimmer that eats the horizon —
but every patch of shade, every mouthful of water, every cool blue thing is the accent, and the
goal, the cool of evening, is relief coming down out of a merciless sky. This drives the visual
identity (§7): a sun-scorched, high-noon world where the one precious colour is not fire but
**water-cool**.

---

## 2. What "~120 passages" buys, and the rule that governs it

Same rule as every book: **every passage is written three times (A2/B1/B2) and glossed in eight
languages.** ~120 passages ≈ 360 authored prose units + a ~250-word book lexicon × 8. A passage
earns its place only if it adds **a real decision, a distinct beat, or texture the reader will
feel.** We hold the top of the CYOA band (~100–150) while staying shippable.

---

## 3. Act structure & passage budget

One afternoon, from the breakdown to the cool of evening.

| Act | Beat | Depth | Budget |
|---|---|---|---|
| **I — The engine dies** (the breakdown → first heat) | The bus dies on the empty road; the failed spare and dead radio; the realisation about Sami; no signal; how you start — take charge of the water, make shade from the bus, or set straight off for the ridge; Mr Bello's shame and what the bus has aboard; the pickup man's first, friendly appearance; Auntie Rose reading the road | The first fork: organise the bus vs. rush off alone; the water/supply choice (`has_water`); the seller's soft opening; learning no help comes till the sun drops | ~30 |
| **II — The long afternoon** (deep heat, the worst hours) | Working the stalled bus and the roadside; the far-ridge shortcut across the open flats; people in trouble on the way (a passenger who wanders off, a second stranded traveller, the child failing in the heat); the pickup man's pressure rising; going seat to seat to pool water and share shade; the smoke at the siding; water and time running low | The open-flats temptation (`took_shortcut`); a stranger in need (`helped_stranger`); giving away your own water (`gave_water`); the seller's plain offer (`dodged`/`paid_seller`); rallying the bus (`rallied_bus`); the smoke mystery seeded and deepened | ~62 |
| **III — Toward the cool of evening** (the sun dropping) | The final push for Sami; the pickup man's last offer; whether you cross to check the smoke; keeping everyone watered and shaded until the light goes long; the first cool breath of evening and a truck's dust on the road | The arrival scene: is Sami safe in time; the mystery resolved (Faro found, the well and radio); the afternoon added up; the cool of evening and what it finds | ~16 |
| **Endings** | see §5 | — | 12 |

**Target: ~120 passages, 12 endings.**

---

## 4. State model (the flags)

`state_in = []` — nothing carried. **Eight own flags**, each *set* at a clear moment and *read* at
a clear payoff; every gated choice keeps an ungated "otherwise" path (validator-enforced). This is
book 3's proven flag machine, re-skinned honestly for the desert (warmth→water, van→pickup,
frozen river→open flats, the light in the empty house→the smoke at the empty siding).

| Flag | Earned when | Pays off at |
|---|---|---|
| `has_water` | you secure a real, shared water supply by decent means (rationing the bus's stock well, a passenger's shared stash, the well at the siding) | keeping Sami watered — the *everyone drinks* win |
| `dodged_seller` | you refuse the pickup man's overpriced water or "lift" | the clean-win gate; no con, no waste |
| `paid_seller` | you buy from the pickup man | the *robbed on the road* bad ending — money gone, still thirsty |
| `found_well` | you go and investigate the smoke and windmill at the empty siding | the secret *the well that wasn't dry* ending — a life saved, water for all |
| `rallied_bus` | you go seat to seat and get the passengers pooling water, making shade and watching the weak | the communal *all of us in the shade* win |
| `helped_stranger` | you stop to help someone else in trouble during the afternoon | the *kindness returned* neutral ending |
| `gave_water` | you give your own water to someone who has none | the *shared your last mouthful* neutral ending |
| `took_shortcut` | you set off walking across the open flats in the full heat | the *the flats went on forever* bad ending |

`state_out` lists all eight (self-consistent JSON); it carries no meaning to any other book.
`arc_flags = []`.

---

## 5. Endings (12) — balanced 4 good / 4 neutral / 4 bad

Two are **secret** (clue/relationship-gated). Bespoke prose × 3 levels + bespoke art.

**Win (4)**
- *Everyone drinks* — `has_water`: you kept the bus watered and shaded through the worst hours; the
  sun drops, a truck comes down the road, and Sami reaches the city safe. The clean warm win.
- *The well that wasn't dry* — **secret**, `found_well`: you cross to the smoke no one can explain,
  find Mr Faro fallen and failing in the heat, and get him cool in time — and his deep well and old
  radio save the whole bus. The mystery pays off, with a quiet grace note of an old face recognised.
- *All of us in the shade* — `rallied_bus`: no single heroic move, but you turned a busload of
  frightened strangers into people sharing water and shade and watching over the weak; everyone
  comes through together.
- *You did what you could* — `dodged_seller`: you refused the con, kept your head and your money,
  and got water by decent means. Not perfect, but clean, honest, and enough.

**Neutral / bittersweet (4)**
- *The kindness returned* — `helped_stranger`: you fell short of the whole afternoon's goal, but the
  stranger you stopped for comes back with a vehicle and carries you and Sami to town. Rescue
  without the full win.
- *Shared your last mouthful* — `gave_water`: you gave your own water away and end the day parched
  yourself, but not alone — and something on that bus has shifted. A start, not a save.
- *One more mile* — ungated fallback: you scrape through the worst of it; a truck finally comes,
  late and grudging. Not triumphant — just, in the end, relieved.
- *The road remembers* — ungated fallback: you didn't manage everything, but the bus saw you get up
  and act when others sat still. You are, from today, someone this road knows.

**Lose (4)**
- *Robbed on the road* — `paid_seller`: you paid the pickup man for water that's warm and half-gone
  and a lift that never comes back. The money's gone, and the thirst is exactly where it was.
- *The flats went on forever* — `took_shortcut`: the open ground was a trap; the heat and the
  distance nearly take you, and they take the afternoon — you get back too late, if you get back.
- *Too late in the heat* — ungated fallback: you spent the hours on the wrong things, and Sami goes
  down in the heat; by evening the child is being carried to a truck, limp and grey.
- *You kept your bottle capped* — ungated fallback: you stayed in your seat and kept your own water
  and never got up. Nothing bad happened to *you*. You will think about it for a long time.

At least one clearly good and one clearly bad (validator warns otherwise). ✔

---

## 6. Levels & lexicon

- **Three levels** (A2/B1/B2), prose per level over one shared graph; validator holds each passage
  in band. **On-demand passage gist** per the flagship (French first, then the pivotal beats + 12
  endings; others as translators arrive).
- **Book lexicon ~250 words**, base-keyed, English + 8 languages, embedded in the JSON — tilted to
  **this** subject: heat and sun (*heat, sun, shade, shadow, glare, haze, sweat, burn, dry, dust,
  sand, ridge, horizon*), water and the body (*water, bottle, thirst, drink, sip, ration, dizzy,
  faint, breath, cool*), the road and the crisis (*bus, road, engine, breakdown, driver, passenger,
  seat, wheel, radio, well, pump, windmill, pickup, spare*). Shares no file with the other books;
  a recurring word is re-authored to a consistent gloss for the learner's sake.
- **The A2-choice caveat (bible §6b):** the branching inference is identical across levels, so at
  A2 the **choice text** must be unambiguous and low-inference. Required in the native review.
- **Native-language review is the launch gate.**

**Language focus** (per level, for the classroom):
- A2 — *imperatives and going to; the body, heat and water; giving directions.*
- B1 — *the first conditional and modals of advice; warning, sharing and planning.*
- B2 — *inference, obligation and conditionals; strangers, risk and responsibility.*

---

## 7. Visual identity (per book)

Its own world: **a desert road at high noon** — an enormous bleached sky, ochre ground, a
heat-shimmer eating the horizon, one stalled bus and one far ridge. The deliberate visual opposite
of the three night books: where they were dark grounds with one warm light, this is a *light*,
sun-blasted world where the one precious colour is **cool**.

- **name:** *High Noon* — **mood:** "A desert road at the hottest hour; the only mercy is the
  water and shade people share."
- **palette:** a hot, high-key set — a pale bleached-sky / sand **ground** and a slightly paler
  reading **surface**, a dark espresso-brown **ink** for legibility on the light card, and a single
  cool **water-teal accent** (the § markers, glossed underlines, the progress bar, the cool-water
  glow) set against a warm sun-ochre **secondary**. This inverts the house pattern on purpose: the
  accent is not the fire but the water. Final values in the JSON `identity` block.
  **Chosen: the bright high-noon light theme.** *Build note:* the reader is dark-first and applies
  the book palette scoped so the universal light "paper" mode can still override. I verify this
  light high-key palette reads cleanly in the reader before wiring; the documented fallback, only
  if it genuinely breaks, is a **dusk-desert** dark variant (a deep warm indigo-ochre ground with
  the same water-teal accent).
- **cover.kind:** a new `highsun` scene added to `scripts/build_og.mjs` (and the browser-canvas
  generator) — a low far ridge under a white sun, a heat-shimmer road, a stalled bus and a lone
  figure — so the social card and library cover are a genuinely different picture, not a recolour.
  `glow: true` is the sun's glare rather than a window.
- **type:** inherited families (Fraunces / Hanken Grotesk / JetBrains Mono).
- **slug:** `cool-of-evening`; **series:** `cool-of-evening`; **episode:** 4. **hero.line** the
  eight-language morph sentence; **sub** the same learner promise.

Shipping = write its JSON (prose + lexicon + `identity` + `slug`) and its OG card, plus the free
per-passage emblem set (a desert/heat motif set added to the reader's per-book `__ART`) and a
wordless `cover-cool-of-evening.png` for the library card. One zero-config route `/b/cool-of-evening` serves it.

---

## 8. Build phases & gates

Gate each phase on `python3 scripts/build_book.py content/episode-04.json --lexicon
content/lexicon.json` coming back clean.

1. **Design sign-off** — this document. → commit.
2. **Graph skeleton** — ~120 nodes, ids + choices + gotos + flags + endings, one-line stubs.
   *Gate:* validator 0 errors; reachable; 12 endings 4/4/4; 8 flags each set+read; every gated
   choice keeps an ungated path.
3. **Prose — B1 first**, then A2 (simplify) and B2 (enrich), in act batches; levelise choices.
   *Gate:* per level, bands clean; no stub text left.
4. **Lexicon** — ~250 words, complete in 9 languages; auto-gloss coverage checked.
5. **Native review** — 8-language pass + A2-choice clarity. *Launch gate.*
6. **Art** — free per-passage emblems (a desert/heat motif set) + a `highsun` OG/cover scene;
   painted art optional, dropped in later at `images/cool-of-evening/ep-04/<id>.webp`.

Built on branch `book-04-cool-of-evening`; merges to `main` only after the definition-of-done.
