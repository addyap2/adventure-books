# The Orchard — book 6 design & build plan

A **standalone** book. It shares nothing with *The Address*, *The Night Market*, *First Light*,
*The Cool of Evening* or *The Keeper* except the method and the house tone — no arc, no carried
state, no shared characters, place or subject (see [authoring-playbook.md](authoring-playbook.md)
§1/§3). `state_in = []`, `arc_flags = []`. The house voice holds: *quiet, humane, a little
uncertain — not frightening. Warm light in cold places.* Here the phrase is almost literal: on the
coldest night of spring a killing frost comes for an orchard in blossom, and the only thing between
the blossom and the cold is dozens of small fires you light down the rows and keep burning by hand
till the sun comes over the ridge.

Where *First Light* carried warmth out into a frozen town, *The Cool of Evening* held a busload
through a killing afternoon, and *The Keeper* kept one light alive through a storm, *The Orchard* is
one person keeping *many* small fires alive through a frost — for an old grower who has gone down,
and for a whole year's fruit that will be lost by dawn if the blossom freezes. A new world: an
inland orchard, a clear still night and a dropping thermometer, fires that must not go out, and a
cold that has to be out-waited until first light.

---

## 1. Premise

The forecast turns on the one night it must not: clear sky, no wind, and the temperature falling
past freezing just as the trees stand in full blossom. A frost like this blackens the blossom by
morning and takes the whole year's fruit with it — and this orchard is the last thing keeping old
**Edith Marsh** on her land. The old way to beat a frost is to warm the air by hand: light the
**smudge pots** and straw fires down every row and keep them burning so the cold can't settle — a
long night's work, dozens of small fires tended at once. But coming down the dark back steps to
start them, Edith goes over on her bad hip and cannot get up, her breath short and the cold already
coming down.

Saving the blossom is suddenly, entirely on you. Edith cannot walk the rows. No crew comes before
morning. The one thing between the frost and the fruit is fire — and the only hands to light and
feed it are yours. So you go out into the cold and keep the watch: find the oil and the straw, light
the pots down the rows, read the thermometer, keep Edith warm and breathing by the stove, and hold
the fires steady until the sun comes over the ridge.

The night is not empty. Up the lane comes **Mr Rourke**, the man from the company that has been
pressing Edith to sell — and a failed harvest is exactly what he needs. He comes smiling, with a
cheque already written, men he could "lend," and reasons the orchard isn't your problem — help that
is really a hook, the same machine as any con. There is a **shortcut across the frozen millpond** to
the far rows and the fuel shed that would halve the walking and could put you through the ice in the
dark. And out among the far trees there is **a small moving light** that no one can explain —
nobody should be in the orchard tonight — the night's quiet pull.

**Theme:** what it takes to bring something tender through a killing cold. The difference between
the help that saves a thing and the "help" that profits from its loss; between keeping the watch for
next year's fruit — food for people you'll never meet — and staying warm behind your own door.
Nobody is a villain except the man who needs the frost to win. The fire against the cold is made of
people.

**The through-line (the quiet pull):** the small light out among the far trees. Everyone says no one
would be in the orchard on a night like this. If you go and look — if you are the kind of person who
answers a light that shouldn't be there — you find **Wren**, a child who slipped out to see the
fires and is now lost and cold among the far rows, and you get them warm in time; and it turns out
Wren is the grandchild Edith has not seen since she and her own son fell out years ago. The mystery
pays off in a child safe and a door reopened — and it turns, as ever, on whether you notice and go.

**Recurring faces:** the fire lives in people.
- **Edith Marsh** — the old grower, down by the back steps; the heart of the night; the orchard is
  hers, and now yours.
- **Tom at the co-op** — opens the fuel store, first help, works the phone.
- **Mr Rourke** — the trap: a cheque written, a cold profit in someone else's bad year.
- **old Jack Hale** — knows this orchard in the dark; warns you off the frozen pond.
- **Wren** — the light in the trees; the mystery; the door reopened.

**The world.** A frosted orchard under a clear hard sky, the blossom white and brittle, the cold
pooling in the low ground — and down the rows dozens of small ember-orange fires, the one warm thing
against the frost; the goal, first light, is the sun coming over the ridge and the blossom safe. This
drives the visual identity (§7): a deep frost-blue night, ember-orange the one warm colour.

---

## 2. What "~120 passages" buys, and the rule that governs it

Same rule as every book: **every passage is written three times (A2/B1/B2) and glossed in eight
languages.** ~120 passages ≈ 360 authored prose units + a ~250-word book lexicon × 8. A passage
earns its place only if it adds **a real decision, a distinct beat, or texture the reader will
feel.** We hold the top of the CYOA band (~100–150) while staying shippable.

---

## 3. Act structure & passage budget

One frost night, from the cold coming down to first light.

| Act | Beat | Depth | Budget |
|---|---|---|---|
| **I — The frost comes** (clear dusk → the fall) | The thermometer drops past freezing; Edith goes down by the back steps; the blossom seen white and still; how you start — the fuel shed, the phone to Tom, or straight to the rows; what the orchard holds (pots, straw, oil, the old thermometer); Rourke's first, friendly appearance; old Jack reading the sky | The first fork: light the fires properly vs. rush a few half-ready; the fuel/pot choice (`has_fires`); Rourke's soft opening; learning no crew comes till morning | ~30 |
| **II — The long cold** (the deepest hours) | Working the rows and the fires; the frozen-pond shortcut to the far rows and fuel shed; people in trouble on the way (a neighbour whose own fire has failed, a stranded driver in the lane, the near rows starting to frost); Rourke's pressure rising; rousing the village for hands and torches; the light among the far trees; oil and time running low | The frozen-pond temptation (`took_shortcut`); a stranger in need (`helped_stranger`); giving away your own coat or fuel (`gave_shelter`); Rourke's plain offer (`dodged_buyer`/`paid_buyer`); rallying the village (`rallied_village`); the light-in-the-trees mystery seeded and deepened | ~62 |
| **III — Toward first light** (before dawn) | The final push to keep the fires fed; Rourke's last offer; whether you go to the light in the trees; keeping Edith warm and the pots banked till the sky greys; the frost lifting and the sun coming over the ridge | The close: did the fires hold and the blossom come through; the mystery resolved (Wren found); the night added up; first light and what it finds | ~16 |
| **Endings** | see §5 | — | 12 |

**Target: ~120 passages, 12 endings.**

---

## 4. State model (the flags)

`state_in = []` — nothing carried. **Eight own flags**, each *set* at a clear moment and *read* at a
clear payoff; every gated choice keeps an ungated "otherwise" path (validator-enforced). This is the
proven flag machine, re-skinned honestly for the orchard (warmth/water → the fires and their oil,
the van/pickup → the buyer, the frozen river/open flats → the frozen pond, the light in the empty
house / the light on the water → the light in the trees).

| Flag | Earned when | Pays off at |
|---|---|---|
| `has_fires` | you get the frost-fires properly lit down the rows by decent means (find the oil and straw, light and bank the pots, read the thermometer) | holding the fires through the night — the *blossom held* win |
| `dodged_buyer` | you refuse Rourke's cheque, men or "help" | the clean-win gate; no con, no sale |
| `paid_buyer` | you take Rourke's deal | the *you signed it away* bad ending — complicit, the orchard lost |
| `found_child` | you go and answer the small light among the far trees | the secret *the light in the trees* ending — a child saved |
| `rallied_village` | you rouse the village for hands on the pots and torches down the rows | the communal *the whole village, awake* win |
| `helped_stranger` | you stop to help someone else in trouble in the cold | the *kindness returned* neutral ending |
| `gave_shelter` | you give your own coat, lamp or fuel to someone with none | the *shared what you had* neutral ending |
| `took_shortcut` | you cross the frozen millpond to the far rows in the dark | the *the ice took it* bad ending |

`state_out` lists all eight (self-consistent JSON); it carries no meaning to any other book.
`arc_flags = []`.

---

## 5. Endings (12) — balanced 4 good / 4 neutral / 4 bad

Two are **secret** (clue/relationship-gated). Bespoke prose × 3 levels + bespoke art.

**Win (4)**
- *The blossom held* — `has_fires`: you kept the fires burning down the rows all night; at first
  light the sun comes over the ridge, the frost lifts, and the blossom — and the whole year's fruit
  — comes through. The warm win.
- *The light in the trees* — **secret**, `found_child`: you answered the light no one could explain,
  found Wren lost and cold among the far rows and got them warm in time — and reopened a door between
  Edith and the son she had not spoken to in years. The mystery pays off.
- *The whole village, awake* — `rallied_village`: no single heroic move, but you turned a sleeping
  village into people with torches down every row, and everyone brought the night through together.
- *You did what you could* — `dodged_buyer`: you refused the con, kept your head, and saved what you
  could by decent means. Not perfect, but clean, honest, and enough.

**Neutral / bittersweet (4)**
- *The kindness returned* — `helped_stranger`: you fell short of the whole orchard, but the neighbour
  you stopped for helps you save the near rows and gets Edith warm. Rescue without the full win.
- *Shared what you had* — `gave_shelter`: you gave your own coat and fuel away and end the night cold
  yourself, but not alone — and something in the village has shifted. A start, not a save.
- *One more hour* — ungated fallback: you scrape through the worst of it; the wind turns at last and
  a thin dawn saves part of the blossom. Not triumphant — just, in the end, relieved.
- *The orchard remembers* — ungated fallback: you didn't save it all, but the village saw you out
  among the trees when others slept. You are, from tonight, someone this place knows.

**Lose (4)**
- *You signed it away* — `paid_buyer`: you took Rourke's deal, and by morning the orchard is no
  longer Edith's to save; the frost did the rest. The cheque is cold, and so is the ground by
  morning.
- *The ice took it* — `took_shortcut`: the frozen pond was a trap; you go through in the dark, and it
  takes the night — you reach the far rows soaked, shaking and far too late.
- *Cold too long* — ungated fallback: you spent the night on the wrong things, and the fires went out
  too long; by dawn the blossom is black and the year is lost.
- *You stayed inside* — ungated fallback: you stayed warm indoors and never lit a fire. Nothing bad
  happened to *you*. You will think about it for a long time.

At least one clearly good and one clearly bad (validator warns otherwise). ✔

---

## 6. Levels & lexicon

- **Three levels** (A2/B1/B2), prose per level over one shared graph; validator holds each passage
  in band. **On-demand passage gist** per the flagship (French first, then the pivotal beats + 12
  endings; others as translators arrive).
- **Book lexicon ~250 words**, base-keyed, English + 8 languages, embedded in the JSON — tilted to
  **this** subject: frost and cold (*frost, cold, ice, freeze, chill, clear, still, air, ground,
  dew, dawn, ridge*), the orchard (*orchard, tree, branch, blossom, bud, fruit, row, bark, root,
  harvest, crop, grower*), and the fire (*fire, flame, pot, straw, oil, smoke, ember, spark, warm,
  light, lantern, burn*). Shares no file with the other books; a recurring word is re-authored to a
  consistent gloss for the learner's sake.
- **The A2-choice caveat (bible §6b):** the branching inference is identical across levels, so at A2
  the **choice text** must be unambiguous and low-inference. Required in the native review.
- **Native-language review is the launch gate.**

**Language focus** (per level, for the classroom):
- A2 — *imperatives and going to; the cold, the garden and the body.*
- B1 — *the first conditional and modals of advice; warning, helping and planning.*
- B2 — *inference, obligation and conditionals; care, risk and responsibility.*

---

## 7. Visual identity (per book)

Its own world: a **frosted orchard** under a clear, hard night sky, rows of blossoming trees with
small fires burning down them. The visual sibling of the other night books, but still and crystalline
rather than stormy — frost-blue and starlight, with the fires the one warm thing.

- **name:** *Frost Fires* — **mood:** "A frosted orchard at night; the only warmth is the fires you
  light down the rows to save the blossom."
- **palette:** a frost set — a deep frost blue-black **ground** and **surface**, a cold
  moonlit-blue **secondary** (the frost, the starlight), and a single warm **ember-orange accent**
  (the fires, the lit pot, the choice `§ N`, glossed underlines, the progress bar) — distinct from
  the other books by pairing a colder, bluer night with a redder, coal-ember warm than the amber
  books. Draft values (final in the JSON `identity` block): `ground #0E1626`, `surface #17212F`,
  `ink #EFF1EA`, `muted #8C95A4`, `line #26324A`, `accent #E87C3A`, `accentHot #F4A25C`,
  `secondary #9CC4D6`.
- **cover.kind:** `frostfire` (rows of blossoming trees at night, small ember fires down the rows,
  a ridge where the dawn will come) with `glow: true`. A new scene branch is added to
  `scripts/build_og.mjs` for it, so the social card and library cover are a genuinely different
  picture — trees, fires, frost — not a recolour.
- **type:** inherited families (Fraunces / Hanken Grotesk / JetBrains Mono).
- **slug:** `the-orchard`; **series:** `the-orchard`; **episode:** 6. **hero.line** the
  eight-language morph sentence (draft EN: *"The frost comes for the blossom tonight. Light the
  fires down the rows and keep them burning till first light."*); **sub** the same learner promise.

Shipping = write its JSON (prose + lexicon + `identity` + `slug`) and its OG card, plus the free
per-passage emblem set (a frost/orchard motif set added to the reader's per-book `__ART`) and a
wordless `cover-the-orchard.png` for the library card. One zero-config route `/b/the-orchard`
serves it.

---

## 8. Build phases & gates

Gate each phase on `python3 scripts/build_book.py content/episode-06.json --lexicon
content/lexicon.json` coming back clean.

1. **Design sign-off** — this document. → commit.
2. **Graph skeleton** — ~120 nodes, ids + choices + gotos + flags + endings, one-line stubs.
   *Gate:* validator 0 errors; reachable; 12 endings 4/4/4; 8 flags each set+read; every gated
   choice keeps an ungated path.
3. **Prose — B1 first**, then A2 (simplify) and B2 (enrich), in act batches; levelise choices.
   *Gate:* per level, bands clean; no stub text left.
4. **Lexicon** — ~250 words, complete in 9 languages; auto-gloss coverage checked.
5. **Native review** — 8-language pass + A2-choice clarity. *Launch gate.* ✓ done
6. **Art** — free per-passage emblems (a frost/orchard motif set) + a `frostfire` OG/cover scene;
   painted art optional, dropped in later at `images/the-orchard/ep-06/<id>.webp`.

Built on branch `book-06-the-orchard`; merges to `main` only after the definition-of-done.
