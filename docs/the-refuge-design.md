# The Refuge — book 8 design & build plan

A **standalone** book. It shares nothing with *The Address*, *The Night Market*, *First Light*,
*The Cool of Evening*, *The Keeper* or *The Orchard* except the method and the house tone — no arc,
no carried state, no shared characters, place or subject (see [authoring-playbook.md](authoring-playbook.md)
§1/§3). `state_in = []`, `arc_flags = []`. The house voice holds: *quiet, humane, a little
uncertain — not frightening. Warm light in cold places.* Here the phrase is almost literal: a
whiteout blizzard closes over a high mountain refuge at dusk, and for miles the only warmth and the
only light is the stove you keep burning and the storm-lamp you keep in the window till the cloud
lifts at first light.

Where *First Light* carried warmth out into a frozen town, *The Keeper* held one light alive through
a storm at sea, and *The Orchard* kept many small fires through a frost, *The Refuge* is one person
holding a single hut — its warmth for a hurt walker who has gone down inside, its lit window the one
beacon for anyone caught out on the mountain. A new world: a storm-locked alpine refuge, a whiteout
coming down with the dark, a stove that must not go out, a lamp that must stay in the window, and a
cold that has to be out-waited until the weather breaks.

---

## 1. Premise

The forecast turns on the one night it must not. A walker reaches the high **refuge hut** — a stone
bothy on the shoulder of the mountain, a day's walk from the glen road — just as a whiteout comes
down with the dark: wind, driving snow, and visibility gone to an arm's length. Inside, the old
warden **Marta** has kept this refuge for thirty winters; the hut's warm stove and the storm-lamp in
its one window are, on a night like this, the only beacon between a lost walker and the cold. But
coming down the loft ladder to bank the stove, Marta goes over and cannot get up, her breath short
and the chill already reaching in under the door.

Keeping the refuge is suddenly, entirely on you. Marta cannot work the stove or the lamp. No rescue
team can climb before morning — not in this. The one thing between the mountain and the people it
holds tonight is the hut: so you keep the watch — find the fuel and the dry wood, get the stove
drawing and the lamp bright in the window, read the falling glass, keep Marta warm and breathing,
and hold the refuge until the cloud lifts and the first light comes grey over the ridge.

The night is not empty. Up out of the storm comes **Vane**, a surveyor for the company that has been
pressing to have the old refuge condemned and the glen sold for a lodge — and a hut that fails on a
bad night is exactly what he needs. He comes smiling, out of the snow, with reasons the refuge isn't
your problem, a bottle to share and fuel to sell — help that is really a hook, the same machine as
any con. There is a **shortcut over the corniced edge of the corrie** to the far store and the fuel
cache that would halve the walking and could put you through a breaking cornice in the dark. And out
on the slope there is **a small moving light** that no one can explain — nobody should be on the
mountain tonight — the night's quiet pull.

**Theme:** what it takes to bring someone through a killing cold. The difference between the help
that saves a life and the "help" that profits from its loss; between keeping the light in the window
for a stranger you'll never meet and barring the door to keep the warmth for yourself. Nobody is a
villain except the man who needs the refuge to fail. The warmth against the cold is made of people.

**The through-line (the quiet pull):** the small light out on the slope. Everyone says no one would
be on the mountain on a night like this. If you go out to it — if you are the kind of person who
answers a light that shouldn't be there — you find **Rowan**, who set out late to reach the hut and
is now lost and freezing below the cornice, and you get them in and warm in time; and it turns out
Rowan is the grandchild Marta has not seen since she and her own child fell out years ago. The
mystery pays off in a walker safe and a door reopened — and it turns, as ever, on whether you notice
and go.

**Recurring faces:** the warmth lives in people.
- **Marta** — the old warden, down by the loft ladder; the heart of the night; the refuge is hers,
  and now yours.
- **Kerr at the glen post** — first voice on the radio, works the set, cannot send anyone till dawn.
- **Vane** — the trap: a condemned refuge is cheap land; a cold profit in someone else's bad night.
- **old Doune** — the shepherd who knows this mountain in the dark; warns you off the cornice.
- **Rowan** — the light on the slope; the mystery; the door reopened.

**The world.** A stone refuge on a dark mountain, the whiteout driving past the one lit window, the
cold pooling under the door — and inside, the orange draw of a stove and a lamp kept bright against
the glass, the one warm thing in all that white dark; the goal, first light, is the cloud lifting
grey over the ridge and everyone brought through. This drives the visual identity (§7): a cold
blue-white alpine night, a single warm amber window.

---

## 2. What "~120 passages" buys, and the rule that governs it

Same rule as every book: **every passage is written three times (A2/B1/B2) and glossed in eight
languages.** ~120 passages ≈ 360 authored prose units + a ~250-word book lexicon × 8. A passage
earns its place only if it adds **a real decision, a distinct beat, or texture the reader will
feel.** We hold the top of the CYOA band (~100–150) while staying shippable.

---

## 3. Act structure & passage budget

One storm night, from the whiteout coming down to first light.

| Act | Beat | Depth | Budget |
|---|---|---|---|
| **I — The storm comes** (dusk → the fall) | The glass drops and the whiteout closes in; Marta goes down by the loft ladder; the one window seen bright against the white dark; how you start — the fuel store, the radio to Kerr, or straight to the stove; what the hut holds (stove, dry wood, lamp-oil, the storm-lamp, the falling glass); Vane's first, friendly arrival out of the snow; old Doune reading the sky | The first fork: get the stove and window-lamp properly going vs. rush a weak flame; the fuel/wood choice (`has_stove`); Vane's soft opening; learning no team climbs till morning | ~30 |
| **II — The long cold** (the deepest hours) | Working the stove and the window-lamp; the corniced shortcut to the far store and fuel cache; people in trouble on the way (a walker whose own lamp has failed, a party benighted below the hut, the stove starting to choke); Vane's pressure rising; rousing the valley for hands and torches; the light on the slope; fuel and time running low | The cornice temptation (`took_cornice`); a stranger in need (`helped_stranger`); giving away your own coat or fuel (`gave_shelter`); Vane's plain offer (`dodged_vane`/`paid_vane`); rousing the valley (`roused_valley`); the light-on-the-slope mystery seeded and deepened | ~62 |
| **III — Toward first light** (before dawn) | The final push to keep the stove fed and the lamp bright; Vane's last offer; whether you go out to the light on the slope; keeping Marta warm and the stove banked till the sky greys; the wind dropping and the cloud lifting over the ridge | The close: did the warmth and the lamp hold and everyone come through; the mystery resolved (Rowan found); the night added up; first light and what it finds | ~16 |
| **Endings** | see §5 | — | 12 |

**Target: ~120 passages, 12 endings.**

---

## 4. State model (the flags)

`state_in = []` — nothing carried. **Eight own flags**, each *set* at a clear moment and *read* at a
clear payoff; every gated choice keeps an ungated "otherwise" path (validator-enforced). This is the
proven flag machine, re-skinned honestly for the refuge (the fires/oil → the stove and its fuel, the
buyer/pickup → the surveyor, the frozen pond/open flats → the corniced edge, the light in the trees
/ on the water → the light on the slope).

| Flag | Earned when | Pays off at |
|---|---|---|
| `has_stove` | you get the stove drawing and the lamp bright in the window by decent means (find the fuel and dry wood, light and bank the stove, read the glass) | holding the refuge through the night — the *brought through* win |
| `dodged_vane` | you refuse Vane's bottle, fuel or "help" | the clean-win gate; no con, no sale |
| `paid_vane` | you take Vane's deal | the *you signed it away* bad ending — complicit, the refuge condemned |
| `found_walker` | you go out and answer the small light on the slope | the secret *the light on the slope* ending — a walker saved |
| `roused_valley` | you rouse the valley for hands and torches on the hill | the communal *the whole valley, awake* win |
| `helped_stranger` | you stop to help someone else in trouble in the cold | the *kindness returned* neutral ending |
| `gave_shelter` | you give your own coat, lamp or fuel to someone with none | the *shared what you had* neutral ending |
| `took_cornice` | you cross the corniced edge of the corrie in the dark | the *the cornice went* bad ending |

`state_out` lists all eight (self-consistent JSON); it carries no meaning to any other book.
`arc_flags = []`.

---

## 5. Endings (12) — balanced 4 good / 4 neutral / 4 bad

Two are **secret** (clue/relationship-gated). Bespoke prose × 3 levels + the outcome ending-scene
art (good / neutral / bad), with painted art optional later.

**Win (4)**
- *Brought through* — `has_stove`: you kept the stove drawing and the lamp bright in the window all
  night; at first light the cloud lifts over the ridge, the team reaches you, and everyone the
  mountain held tonight is brought through warm. The warm win.
- *The light on the slope* — **secret**, `found_walker`: you answered the light no one could explain,
  found Rowan lost and freezing below the cornice and got them in and warm in time — and reopened a
  door between Marta and the child she had not spoken to in years. The mystery pays off.
- *The whole valley, awake* — `roused_valley`: no single heroic move, but you turned a sleeping
  valley into people with torches on the hill, and everyone brought the night through together.
- *You did what you could* — `dodged_vane`: you refused the con, kept your head, and held the refuge
  by decent means. Not perfect, but clean, honest, and enough.

**Neutral / bittersweet (4)**
- *The kindness returned* — `helped_stranger`: you fell short of holding it all, but the walker you
  stopped for helps you keep the hut and gets Marta warm. Rescue without the full win.
- *Shared what you had* — `gave_shelter`: you gave your own coat and fuel away and end the night cold
  yourself, but not alone — and something in the valley has shifted. A start, not a save.
- *One more hour* — ungated fallback: you scrape through the worst of it; the wind drops at last and
  a thin dawn brings the team up the hill. Not triumphant — just, in the end, relieved.
- *The mountain remembers* — ungated fallback: you didn't bring everyone through, but the valley saw
  you out on the hill when others barred their doors. You are, from tonight, someone this place
  knows.

**Lose (4)**
- *You signed it away* — `paid_vane`: you took Vane's deal, and by morning the refuge is condemned
  and no longer anyone's to keep; the cold did the rest. The money is in your hand, and the window
  is dark.
- *The cornice went* — `took_cornice`: the corniced edge was a trap; it breaks under you in the dark
  and takes the night — you reach the far side, if at all, hurt, soaked and far too late.
- *Dark too long* — ungated fallback: you spent the night on the wrong things, and the stove went out
  too long; by dawn the hut is cold and the night is lost.
- *You barred the door* — ungated fallback: you kept the warmth for yourself and never put the lamp
  in the window. Nothing bad happened to *you*. You will think about it for a long time.

At least one clearly good and one clearly bad (validator warns otherwise). ✔

---

## 6. Levels & lexicon

- **Three levels** (A2/B1/B2), prose per level over one shared graph; validator holds each passage
  in band. **On-demand passage gist** per the flagship — full per-passage coverage in all eight
  languages, as the other books now carry.
- **Book lexicon ~250 words**, base-keyed, English + 8 languages, embedded in the JSON — tilted to
  **this** subject: the storm and cold (*storm, snow, wind, whiteout, cloud, cold, ice, freeze,
  chill, ridge, slope, summit, glass, dawn*), the mountain (*mountain, refuge, hut, bothy, stone,
  loft, ladder, corrie, cornice, path, track, valley, glen*), and the warmth (*stove, fire, flame,
  fuel, wood, oil, lamp, light, window, smoke, ember, warm, burn*). Shares no file with the other
  books; a recurring word is re-authored to a consistent gloss for the learner's sake.
- **The A2-choice caveat (bible §6b):** the branching inference is identical across levels, so at A2
  the **choice text** must be unambiguous and low-inference. Required when levelising the choices.

**Language focus** (per level, for the classroom):
- A2 — *imperatives and going to; the weather, the hut and the body.*
- B1 — *the first conditional and modals of advice; warning, helping and planning.*
- B2 — *inference, obligation and conditionals; care, risk and responsibility.*

---

## 7. Visual identity (per book)

Its own world: a **stone refuge** on a dark mountain in a whiteout, one window warm against the
driving snow. The visual sibling of the other night books, but alpine and blizzard-blown rather than
still — ice-blue and starless white dark, with the single window the one warm thing.

- **name:** *Whiteout* — **mood:** "A storm-locked mountain refuge at night; the only warmth and the
  only light for miles is the one you keep."
- **palette:** a cold alpine set — a deep blue-black **ground** and **surface**, a cold ice-blue
  **secondary** (the snow, the whiteout, the starlight behind the cloud), and a single warm
  **amber-gold accent** (the stove, the lit window, the choice `§ N`, glossed underlines, the
  progress bar) — distinct from the other books by pairing the coldest, bluest-white night in the
  set with a clean amber-gold window rather than an ember-red or dusk-orange warm. Draft values
  (final in the JSON `identity` block): `ground #0B1420`, `surface #13202F`, `ink #F2F5F7`,
  `muted #8A97A8`, `line #223247`, `accent #F0A338`, `accentHot #F7C070`, `secondary #A9C7DE`.
- **cover.kind:** `refuge` (a dark mountain, driving snow across it, one stone hut with a single warm
  lit window, a ridge where the dawn will come) with `glow: true`. A new scene branch is added to
  `scripts/build_og.mjs` for it, so the social card and library cover are a genuinely different
  picture — mountain, snow, lit window — not a recolour.
- **type:** inherited families (Fraunces / Hanken Grotesk / JetBrains Mono).
- **slug:** `the-refuge`; **series:** `the-refuge`; **episode:** 7. **hero.line** the eight-language
  morph sentence (draft EN: *"The storm has the mountain tonight. Keep the stove lit and the lamp in
  the window, and hold the refuge till first light."*); **sub** the same learner promise.

Shipping = write its JSON (prose + lexicon + `identity` + `slug`) and its OG card, plus the free
per-passage emblem set (a mountain/storm/hut motif set added to the reader's per-book `__ART`) and a
wordless `cover-the-refuge.png` for the library card. The universal outcome ending-scenes already
cover the 12 endings. One zero-config route `/b/the-refuge` serves it.

---

## 8. Build phases & gates

Gate each phase on `python3 scripts/build_book.py content/episode-08.json --lexicon
content/lexicon.json` coming back clean.

1. **Design sign-off** — this document. → commit.
2. **Graph skeleton** — ~120 nodes, ids + choices + gotos + flags + endings, one-line stubs,
   transformed from the shared topology (ep06) with the refuge's identity and flag names.
   *Gate:* validator 0 errors; reachable; 12 endings 4/4/4; 8 flags each set+read; every gated
   choice keeps an ungated path.
3. **Prose — B1 first**, then A2 (simplify) and B2 (enrich), in act batches; levelise choices.
   *Gate:* per level, bands clean; no stub text left.
4. **Lexicon** — ~250 words, complete in 9 languages; auto-gloss coverage checked.
5. **A2-choice clarity pass** — each A2 choice checked unambiguous and low-inference.
6. **Gists** — full per-passage gist coverage in all eight languages.
7. **Art** — free per-passage emblems (a mountain/storm/hut motif set) + a `refuge` OG/cover scene;
   the universal good/neutral/bad ending-scenes already apply; painted art optional, dropped in later
   at `images/the-refuge/ep-07/<id>.webp`.

Built on branch `book-07-the-refuge`; merges to `main` only after the definition-of-done.
