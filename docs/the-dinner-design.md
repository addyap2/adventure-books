# The Dinner — book 9 design & build plan

A **standalone** book, and a deliberate change of key. The first eight books are all dramatic
survival nights (a cold city, a market, a snowed-in town, a desert bus, a storm at sea, a frost, a
flood, a mountain blizzard). **The Dinner is everyday.** Same engine — you are the hero, every
choice turns the page, 12 endings, three levels, eight languages — but the stakes are ordinary and
warm, and the vocabulary is the **highest-frequency, most useful everyday English** a learner needs:
*food, kitchen, shop, cook, pot, plate, table, guest, time, late, money, help, friend, family, door,
phone.* No arc, no carried state (`state_in = []`, `arc_flags = []`). The house voice still holds:
*quiet, humane, a little funny, kind.*

Where the other books ask "can you keep someone alive through the night?", this one asks a smaller,
truer question most of us actually face: **can you get a good evening onto the table for the people
you love, when everything that can go wrong does?**

---

## 1. Premise

It is Gran's birthday, and the whole family is coming for dinner at seven. Gran — **Ivy**, who has
cooked this dinner for thirty years — is in bed upstairs with a bad cold, and for the first time the
cooking is all yours. It is five o'clock. There is a chicken to roast, potatoes to do, a cake half
made, a table to lay, and two hours on the clock.

Then it starts. The shop is out of the one thing you need. A pot boils over. The oven plays up. A
neighbour knocks, needing a hand. Your phone is nearly dead, and Gran keeps calling down the recipe
from upstairs. None of it is the end of the world — but all of it, together, with the clock running,
is a lot. Getting a good dinner on the table for seven is suddenly, entirely on you.

The evening is not empty. **Dale** from the takeaway on the corner has a friendly offer: buy his
food, tip it into your own dishes, and let the family think you cooked it — "no one will ever know,
love." It is the easy way out, and it is a kind of cheating, the same small con dressed up as help.
There is a **shortcut to the shop across the main road** that would save ten minutes and could get
you hurt in the dark and the rain. And there is a **knock at the gate, and a figure in the dark** —
someone no one quite expected tonight.

**Theme:** what it takes to make an ordinary good evening for other people. The difference between
real hospitality and faking it; between stopping to help a neighbour and keeping your head down;
between pride and letting people in. Nobody is a villain — not even Dale. The dinner, in the end, is
made of people.

**The through-line (the quiet pull):** the knock at the gate. You weren't sure she'd come. It is
**Nora**, the sister you fell out with years ago and haven't really spoken to since. If you are the
kind of person who opens the door, and makes a place at the table, the evening becomes something
more than a dinner — a door, shut for years, quietly opening again over the pudding.

**Recurring faces:** the evening lives in people.
- **Gran Ivy** — ill upstairs; the dinner is hers; the heart of the night, calling down the recipe.
- **Mrs Okafor at the corner shop** — stays open late, first help, finds you what you need.
- **Dale from the takeaway** — the easy cheat: buy it, pass it off, no one will know.
- **old Joan next door** — has cooked a thousand dinners; warns you off the main road and the rush.
- **Nora** — the knock at the gate; the sister; the door reopened.

**The world.** A warm kitchen on a dark winter evening — steam on the window, the radio on, a pot on
the hob, the smell of a cake — against a cold, wet street outside. The one warm bright room, and a
table being laid for the people you love. The goal, "first light" made homely, is **seven o'clock
and the family round the table**. This drives the visual identity (§7): a warm, homely kitchen
palette — amber lamplight and herb green — not a cold night.

---

## 2. What "~120 passages" buys, and the rule that governs it

Same rule as every book: **every passage is written three times (A2/B1/B2) and glossed in eight
languages.** ~120 passages ≈ 360 authored prose units + a ~250-word book lexicon × 8 — here tilted
hard to **everyday, high-frequency words** a beginner meets every day. A passage earns its place only
if it adds a real decision, a distinct beat, or a warm bit of texture.

---

## 3. Act structure & passage budget

One evening, from five o'clock to seven and the family at the table.

| Act | Beat | Depth | Budget |
|---|---|---|---|
| **I — Five o'clock** (the cooking lands on you) | Ivy ill upstairs; the clock at five; the chicken, the spuds, the half-made cake, the table; how you start — the shop, a call to a friend, or straight to the cooking; what the kitchen holds; Dale's first friendly offer; old Joan reading the clock | The first fork: cook it properly vs rush it; the shop/ingredients choice (`has_dinner`); Dale's soft opening; learning Gran can't come down to help | ~30 |
| **II — The long two hours** (it all goes wrong at once) | Working the hob and the oven; the shortcut to the shop across the main road; people needing a hand (a locked-out neighbour, a friend who turns up early, a dish that catches); Dale's pressure; getting friends to pitch in; the knock at the gate; time and money running low | The main-road shortcut (`ran_road`); a neighbour in a fix (`helped_stranger`); giving away your own food (`shared_food`); Dale's plain offer (`dodged_dale`/`paid_dale`); rallying friends (`rallied_friends`); the knock-at-the-gate mystery seeded | ~62 |
| **III — Toward seven** (the last stretch) | The final push to get it all on the table; Dale's last offer; whether you open the gate; keeping Ivy's recipe and the cake going till the hour; the family arriving; seven o'clock | The close: did a good dinner make it to the table; the mystery resolved (Nora welcomed in); the evening added up; seven o'clock and who is round the table | ~16 |
| **Endings** | see §5 | — | 12 |

**Target: ~120 passages, 12 endings.**

---

## 4. State model (the flags)

`state_in = []`. **Eight own flags**, each *set* at a clear moment and *read* at a clear payoff;
every gated choice keeps an ungated path (validator-enforced). The proven flag machine, re-skinned
honestly and gently for a kitchen (the warmth/fires → the dinner; the con man → the takeaway cheat;
the deadly shortcut → the dash across the main road; the light out in the dark → the knock at the
gate).

| Flag | Earned when | Pays off at |
|---|---|---|
| `has_dinner` | you get a real, proper dinner going by decent means (get the shopping, cook Ivy's recipe, keep the hob and oven going, lay the table) | a good evening on the table — the *dinner made* win |
| `dodged_dale` | you turn down Dale's buy-it-and-fake-it offer | the clean-win gate; no cheat, no lie |
| `paid_dale` | you take Dale's deal and pass his food off as your own | the *they found out* bad ending — the lie at the table |
| `welcomed_nora` | you open the gate and make a place for the sister who turns up | the secret *the door reopened* ending — a family mended |
| `rallied_friends` | you get friends and family to pitch in on the cooking | the communal *everyone in the kitchen* win |
| `helped_stranger` | you stop to help a neighbour in a fix | the *kindness returned* neutral ending |
| `shared_food` | you give away your own food or portion to someone with none | the *there's always enough* neutral ending |
| `ran_road` | you take the dangerous shortcut across the main road | the *you should've gone round* bad ending |

`state_out` lists all eight (self-consistent JSON); it carries no meaning to any other book.
`arc_flags = []`.

---

## 5. Endings (12) — balanced 4 good / 4 neutral / 4 bad

Two are **secret** (relationship-gated). Bespoke prose × 3 levels; the universal good/neutral/bad
ending-scenes apply; painted art optional later.

**Win (4)**
- *Dinner made* — `has_dinner`: you cooked a real dinner, by yourself, and got it on the table for
  seven. Ivy comes down in her dressing gown to a full table and the smell of her own recipe. The
  warm win.
- *The door reopened* — **secret**, `welcomed_nora`: you opened the gate and made a place for Nora,
  and a quarrel that lasted years quietly ends over the pudding. The dinner became something more.
- *Everyone in the kitchen* — `rallied_friends`: no single clever thing, but you turned a panic into
  a kitchen full of people chopping and laughing, and the evening came together in all of them.
- *You did it honestly* — `dodged_dale`: you refused the easy cheat and made what you could, for
  real. Not a perfect dinner, maybe. But it's yours, and honest, and that's enough.

**Neutral / bittersweet (4)**
- *The kindness returned* — `helped_stranger`: dinner isn't perfect, but the neighbour you stopped
  for turns up with their own dish and a hand, and the evening is saved between you.
- *There's always enough* — `shared_food`: you gave food away and end up a bit short yourself, but
  the table is fuller of people than of plates, and no one minds. A warm, smaller evening.
- *A bit late, but good* — ungated fallback: it all runs late and a little rough, but everyone eats,
  and laughs about it, and it turns out fine in the end. Not grand — just nice.
- *They'll remember you tried* — ungated fallback: it wasn't your best cooking, but the family saw
  you take it on for Gran, at the last minute, and that's the part they'll talk about for years.

**Lose (4)**
- *They found out* — `paid_dale`: you passed Dale's takeaway off as your own, and halfway through
  dinner someone recognises the box in the bin. The evening goes quiet in a way you won't forget.
- *You should've gone round* — `ran_road`: you ran across the main road to save ten minutes, and it
  went wrong — a fall, a near miss, the shopping in the gutter. You get home late, shaken, and empty-handed.
- *Burnt, and too late* — ungated fallback: you spent the time on the wrong things, the oven caught,
  and seven o'clock comes with nothing ready. The family are kind about the chips you order. You're not.
- *You gave up* — ungated fallback: you ordered a takeaway, laid it out, and ate alone before anyone
  came — then said you weren't well. Nothing went wrong, exactly. The table just stayed empty.

At least one clearly good and one clearly bad (validator warns otherwise). ✔

---

## 6. Levels & lexicon

- **Three levels** (A2/B1/B2), prose per level over one shared graph; validator holds each passage
  in band. **On-demand passage gist** — full per-passage coverage in all eight languages, as the
  other books carry.
- **Book lexicon ~250 words**, base-keyed, English + 8 languages, embedded in the JSON — tilted to
  **everyday life and the kitchen**: food and cooking (*food, cook, bake, boil, fry, roast, pot,
  pan, oven, hob, plate, bowl, knife, fork, cake, bread, chicken, potato, salt, taste*), the home
  (*kitchen, table, chair, door, window, room, light, fridge, cupboard, clock*), shopping and people
  (*shop, money, bag, list, buy, pay, queue, neighbour, friend, family, guest, help, wait, late*).
  The most useful 250 words a beginner can tap. Shares no file with the other books.
- **The A2-choice caveat:** the branching inference is identical across levels, so at A2 the choice
  text must be unambiguous and low-inference. Required when levelising the choices.

**Language focus** (per level, for the classroom):
- A2 — *imperatives and the present; the kitchen, food and time.*
- B1 — *the first conditional and modals of advice; planning, helping and inviting.*
- B2 — *inference and politeness; hospitality, pride and letting people in.*

---

## 7. Visual identity (per book)

Its own world, and the first **warm** one: a kitchen on a winter evening, lit and steamy, against
the cold wet street outside. The warm light here is the whole room, not one small flame.

- **name:** *Dinner at Seven* — **mood:** "A warm kitchen on a winter evening; dinner for the people
  you love, and two hours to get it right."
- **palette:** a warm homely set — a deep warm brown **ground** and **surface**, a soft herb-green
  **secondary** (the kitchen, the greens, the calm), and a warm amber **accent** (the lamp, the
  oven glow, the choice `§ N`, glossed underlines, the progress bar) — the warmest palette in the
  set, the only one that reads as *indoors and cosy* rather than a cold night out. Draft values
  (final in the JSON `identity` block): `ground #1A1210`, `surface #241A16`, `ink #F6EFE6`,
  `muted #A2938A`, `line #38281F`, `accent #E8903A`, `accentHot #F4B46A`, `secondary #93B88A`.
- **cover.kind:** `kitchen` (a warm-lit kitchen window on a dark street, steam on the glass, a laid
  table or a pot on the hob) with `glow: true`. A new scene branch is added to `scripts/build_og.mjs`.
- **type:** inherited families (Fraunces / Hanken Grotesk / JetBrains Mono).
- **slug:** `the-dinner`; **series:** `the-dinner`; **episode:** 9. **hero.line** the eight-language
  morph sentence (draft EN: *"The family come for dinner at seven, and tonight the cooking is all
  yours. Get a good evening onto the table."*); **sub** the same learner promise.

Shipping = write its JSON (prose + lexicon + `identity` + `slug`) and its OG card, plus the free
per-passage emblem set (a kitchen/food motif set) and a wordless `cover-the-dinner.png`. The
universal outcome ending-scenes already cover the 12 endings. One zero-config route `/b/the-dinner`
serves it.

---

## 8. Build phases & gates

Gate each phase on `python3 scripts/build_book.py content/episode-09.json --lexicon
content/lexicon.json` coming back clean.

1. **Design sign-off** — this document. → commit.
2. **Graph skeleton** — ~120 nodes, transformed from the shared topology (ep08) with the dinner's
   identity and flag names, one-line stubs. *Gate:* validator 0 errors.
3. **Prose — B1 first**, then A2 (simplify) and B2 (enrich), in act batches; everyday vocabulary;
   levelise choices. *Gate:* per level, bands clean; no stub text left.
4. **Lexicon** — ~250 everyday words, complete in 9 languages; auto-gloss coverage checked.
5. **A2-choice clarity pass.**
6. **Gists** — full per-passage gist coverage in all eight languages.
7. **Art** — a kitchen/food emblem set + a `kitchen` OG/cover scene; the universal ending-scenes
   apply; painted art optional later.

Built on branch `book-09-the-dinner`; merges to `main` only after the definition-of-done.

---

## 9. Art handoff — scene illustrations (and the template for the next book)

This records **what shipped** for book 9's visuals and the **drop-in brief** used to upgrade
them, so the next book can follow the same hand-off. There are three art surfaces in the repo;
know which one you're touching.

**The three surfaces**

1. **Per-passage scene art** (what the reader shows in the left panel). Driven by
   `web/illustrations/catalog.json` → each book maps every passage's *motif* (from
   `window.__ART[series]` in `web/index.html`) to a **scene SVG**, with a per-motif
   `sceneTitles`. The Dinner reuses **four** portrait SVGs across its 23 motifs:
   `the-dinner-kitchen.svg` · `-street.svg` · `-doorway.svg` · `-table.svg`
   (`viewBox="0 0 800 1000"`, shown `object-fit:cover`). Endings: good→table, neutral→kitchen,
   bad→street; cover→table.
2. **Reproducibility.** `scripts/build-illustrations.mjs` rewrites `catalog.json` wholesale on
   every run. Books whose scenes it *generates* live in its `books` array; books whose art is
   **hand-made** (The Address, The Dinner) have their catalog entry **declared explicitly** in
   that script so a regen reproduces them instead of wiping them. If you add/replace hand-made
   scenes, keep the four filenames fixed so neither `catalog.json` nor that script needs editing.
3. **Social / OG card.** `web/og-<slug>.png` (1200×630) from `scripts/build_og.mjs` (per-book
   scene branch — The Dinner's is `kitchen`); collection cards from
   `scripts/build-collection-social.mjs` (update its story-count string when the book count
   changes). Optional higher fidelity per passage: painted WebP at
   `images/<series>/ep-NN/<id>.webp` overrides the scene for that node — see `docs/art-brief.md`.

**Upgrade brief (paste to an agent/tool with repo access).** Replace the four scene SVGs *in
place*, portrait `0 0 800 1000`, within the book palette (`ground #1A1210`, `surface #241A16`,
`ink #F6EFE6`, `muted #A2938A`, `line #38281F`, `accent #E8903A`, `accentHot #F4B46A`,
`secondary #93B88A`), collection mood *"warm light in cold, dark places."* Scene briefs:

- **kitchen** — the heart: warm lit kitchen at night; hob with a steaming pot, oven, counter,
  rainy window, pendant light. (Into the kitchen / On the hob / A proper dinner / A knock at the
  gate / Many hands / Two hours to seven / Looking in on Gran / A warm welcome / A call for help;
  neutral ending.)
- **street** — dark wet night street; glowing street lamp, dark houses with one gold-lit window,
  oncoming car headlights, a lone figure. (Out in the rain / The main road / A light down the
  street / The long way home / The corner shop / Good advice / Which way to go; bad ending.)
- **doorway** — a warm open doorway spilling light onto a wet step, a figure before it in the
  rain — the Nora/stranger/reunion thread and the secret good ending "the door reopened." (An open
  door / A helping hand / The easy way out / Someone counting on you / After all these years.)
- **table** — the payoff + cover: a dinner table laid under warm light — roast, plates, bread,
  candle, pendant glow. (The table laid / Enough to share; good ending.)

**Do not change:** the four filenames; `catalog.json` scene map & titles; `window.__ART[series]`
and `__MOTIFS`; the JSON/gists/lexicon; the other books' art. **Verify:** `npm run build` passes
(it validates every catalog asset exists + contrast); spot-check the four scenes in the reader.

**Template for the next book:** pick 3–5 scenes that cover the story's motifs, title each motif,
map endings (good/neutral/bad), either register the book in `build-illustrations.mjs`'s `books`
array (generated vector scenes) or declare its entry explicitly (hand-made art), add its OG scene
branch to `build_og.mjs`, and bump the collection-card count. Keep filenames stable so art is a
pure drop-in.
