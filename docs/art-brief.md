# Adventure Book — art brief for the section illustrations

Each section of the story is presented as a **moment card**: one illustration, the
paragraph, and the choices. The illustration is the first thing the reader sees on every
screen, so it carries the mood and the "keep going" pull. This brief tells you exactly
what to produce and how to name it so it drops into the app with no code change.

## The one rule that matters most: consistency

A learner sees 8–15 of these per sitting, one after another. They must feel like one
hand drew all of them. Consistency of palette, light, and framing matters far more than
the polish of any single image. Agree the look on the first five, lock it, then hold it
for all 400.

## Format and delivery

| | Spec |
|---|---|
| **Moment images** | 3:2 landscape, **1200 × 800 px** |
| **Cover image** (one per episode) | 4:5 portrait, **1080 × 1350 px** |
| **File format** | WebP, quality ~80 |
| **Weight budget** | ≤ 120 KB per moment, ≤ 180 KB cover. Hard ceiling 200 KB — this is a phone-first app on mobile data. |
| **Colour** | sRGB |
| **No text in the image** | the app renders all words; text baked into art can't be translated or levelled |

The card crops the image slightly on very tall phones, so **keep the subject in the
central 90%** — nothing important in the outer 5% on any edge.

## Naming — this is how art reaches the app

Drop files into the repo at:

```
images/<series>/ep-<NN>/<paragraph-id>.webp
images/<series>/ep-<NN>/cover.webp
```

For episode 1 that is:

```
images/new-city/ep-01/1.webp     ← the opening (paragraph 1)
images/new-city/ep-01/7.webp     ← paragraph 7
images/new-city/ep-01/cover.webp ← the episode cover
…
```

The number is the **paragraph id** shown in each section of the rendered story files
(`build/episode-01.A2.md` etc.). Add a file, push, and it appears — the build scans the
folder automatically. No JSON to edit. Until a file exists, the app shows a clean
gradient placeholder, so partial delivery looks intentional, not broken.

> One caveat for the dev side: don't run the paragraph-shuffle step on episodes that have
> art, or the ids stop matching the filenames. On the web app the numbers aren't shown to
> readers, so there's no reason to shuffle.

## Palette — match the app, don't fight it

The app's own colours. Illustrations should live in this range so art and interface read
as one product.

| Token | Light | Dark |
|---|---|---|
| Ground | `#f6f3ee` warm cream | `#121417` near-black |
| Primary accent | `#2f5d50` deep teal | `#86c9b4` soft teal |
| Warm accent | `#c9683c` burnt orange | `#e08a5c` |
| Ink / line | `#1d1b19` | `#eceae6` |

Each image renders on **both** a light and a dark card, so avoid pure-white or
pure-black fills that clash with one of them. A limited palette per image — one or two
dominant hues plus a single warm light source — reads best and is easiest to keep
consistent. The burnt-orange accent is the "warm light" note; use it sparingly (a lamp,
a lit window, a sign) to draw the eye.

## Direction for this series ("new-city")

Someone arrives alone in an unfamiliar city at night and has to find their way. The mood
is **quiet, atmospheric, a little uncertain — not frightening.** Warm light in cold
places. Empty streets, stations, a river at dawn. The reader is always "you", so:

- **Show the world, not the hero's face.** Frame from behind or over the shoulder, or
  show just hands, feet, a reflection. A faceless viewpoint lets every learner be "you" —
  and sidesteps depicting a specific age, gender or ethnicity, which matters for a
  mixed-nationality audience.
- **Culturally neutral.** A generic modern European-ish city that could be many places.
  No flags, no signage in a specific language, no landmarks that name a country.
- **One clear subject per image** — the thing the paragraph is about. The wet coat. The
  black notebook. The yellow luggage label. The empty office with one light on.

## Which sections to illustrate first

You don't need all 40 at once. These are the beats that carry the most weight — do these
first and the story already feels illustrated:

| id | The moment | Why it matters |
|---|---|---|
| 1 | Arriving at the empty night station, letter in hand | The opening — sets the whole mood |
| 7 | Rosewater Street: the grey building, dusty windows, dead sign | The story's central image |
| 11 | Looking through the window at the one light still on | Quiet tension |
| 15 | The café card in the window: the new address | A key discovery |
| 23 | Mill Quay at dawn — new glass buildings by the water | The world opening up |
| 24 | The too-bright agency, the man in the good suit | The one that's a trap |
| 31 | The woman with the coffee, the yellow R. ROWE label | The secret-ending clue |
| 36 / 38 | The good endings — being taken on | The payoff |
| 39 / 40 | The bad endings — the empty office, the 2 o'clock train | The cost |

Endings deserve your best work: they're what the reader replays to reach.

## Accessibility

Supply a one-line **alt description** per image (a sentence naming what's shown) in a
sidecar list — the dev can wire it in. It matters for screen-reader users and for
learners who read the description as extra input.

## Checklist before you hand off a batch

- [ ] 1200×800 (moments) / 1080×1350 (cover), WebP, ≤120/180 KB
- [ ] subject inside the central 90%
- [ ] no baked-in text
- [ ] reads on both a cream and a near-black card
- [ ] no face, or faceless viewpoint
- [ ] nothing that names a specific country
- [ ] filename is the paragraph id, in `images/new-city/ep-01/`
