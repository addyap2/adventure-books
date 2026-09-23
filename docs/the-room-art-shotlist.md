# The Room — art shot-list (episode 2)

Companion to [art-brief.md](art-brief.md) (specs, palette, direction) and the flagship
[art-shotlist.md](art-shotlist.md) (the model this follows). **This file is the
authoritative map**: which passages share which image, and where each file goes.

## How the files reach the app

Drop a file at `images/new-city/ep-02/<node-id>.webp` and it appears on that passage
automatically — no code change (see [scripts/build-site.mjs](../scripts/build-site.mjs),
which scans the folder). The story shares images **by scene**: one picture serves every
passage set in the same place or built on the same beat.

- Each scene below has a **hero id** — name the file after that (e.g. `40.webp`).
- To show it on the other passages in that scene, **copy the same file** to each of their
  ids (`cp 40.webp 41.webp`, etc. — commands per scene below).
- The **cover** is `cover.svg` (vector). Everything else is 3:2, 1200×800 WebP, ≤200 KB.
- Any passage without a file shows a clean placeholder, so **partial delivery is fine** —
  ship a scene at a time.

**Total: 31 images** — 18 scenes + 12 endings + the cover — covering all 120 passages.

## The world (how book 2 differs from book 1)

Book 1 was one cold **night**; book 2 is one cold winter **day**, dawn to dark. Same city,
seen bright and grey and indifferent instead of dark and empty. The single warm light is no
longer a street lamp but **a lit doorway with a room behind it** — that is the recurring
visual key and the cover. Palette per the book's `identity` block (a colder, bluer set than
*The Address*; the warm accent is a hearth amber that means *a door that opens*).

**Recurring faces** (keep them consistent; always faceless or from behind): **Mrs Halloran**
(grey-eyed, straight-backed, the canal landlady), **Mr Vann** (the letting agent — warm smile,
good suit, always in motion), **the kiosk woman** (carried from book 1), **Dania** (a fellow
new-hire, a case and a folded advert). The property beat objects: **the coat on the hook**,
**the tin of buttons**, **the notebook of addresses**, **the photograph at the window**.

---

## Wave 1 — lock the look (do these first; agree the style, then hold it)

| hero | scene | serves passages | faceless alt-line |
|---|---|---|---|
| `cover` | Episode cover *(4:5)* | — | A lit doorway in a grey winter street, seen from across the road; a figure with a small case, from behind, drawn toward the warm light. |
| `1` | The cheap hotel at dawn | 1, 2, 10 | A cheap hotel room at first light; a note on the floor by the door, a little money laid out on the bed. |
| `50` | The canal building — Halloran's stair | 50, 110, 116 | A steep swept stair over an old rope-works; at the top, an open door and one warm lit window. |
| `51` | The room over the rope-works | 51, 52, 53, 54, 55, 56, 59, 60, 61, 62, 84 | A room with good light off the water; a coat on a hook, a tin of buttons on the sill, a box half-packed by the wall. |
| `40` | Vann's letting office (the trap) | 8, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 65, 66, 68 | A too-bright letting office; a queue of tired hopefuls under a board of glossy rooms; a man in a good suit, over the shoulder. |
| `25` | The market square by day | 18, 19, 20, 25, 26, 115 | A crowded market square in grey daylight; stalls, a clock, a lane leading off toward the water. |
| `104` | Halloran in the doorway at dusk | 100, 104, 105, 106, 107, 108, 109, 111 | A woman in a lit doorway at dusk, the warm room behind her; a hand holding folded money. |
| `120` | Good ending — the room given | 120 | A window catch being fixed in warm lamplight; the grey water below, a kettle, a life beginning. |

## Wave 2 — the rest of the day's places

| hero | scene | serves passages | faceless alt-line |
|---|---|---|---|
| `3` | The corner kiosk | 3, 5, 16, 17 | A corner kiosk by day; a folded local paper passed across, two adverts ringed in pencil, a third scored through. |
| `4` | The phone listing / Vann's ad | 4, 9 | A phone screen held in cold hands, a too-bright room glowing cheap and perfect. |
| `6` | The canal side, morning | 6, 11, 12, 13 | A grey canal in morning light; an old rope-works, washing on a line, the smell of tar and cold water. |
| `7` | The two circled ads *(object beat)* | 7, 14, 15 | A local paper open on a knee, two rooms ringed in pencil, a whole city between them. |
| `21` | The bedsit — the grim room | 21, 30, 31, 32, 33, 34, 35, 39, 103 | A damp stair and a small grey room; a window onto a blank brick wall, a landlord's keys jingling. |
| `76` | The stairwell / the neighbour | 63, 64, 76, 77, 78, 79, 92, 113 | A stairwell; splitting shopping bags and a small child's hand, three floors still to climb. |
| `70` | The good flat / the reference | 70, 71, 72, 73, 74, 75, 101 | A clean bright flat two flights up, morning at the window; a phone held to the ear on the stair. |

## Wave 3 — the corners, the objects, and the dusk

| hero | scene | serves passages | faceless alt-line |
|---|---|---|---|
| `28` | Dania — looking together | 27, 28, 29, 90, 91, 118 | Two travellers on a bench comparing two adverts; a case at each foot, the city around them. |
| `85` | The coat, the photograph, the notebook *(object beat)* | 57, 58, 80, 81, 82, 83, 85, 86 | A coat pocket open: a photograph of the same window, a notebook of addresses in a careful hand. |
| `36` | The far room-share (dead end) | 36, 37, 38 | A closed door at the ragged edge of the city; a long empty road leading back. |
| `112` | Vann's address — the car park *(object beat)* | 102, 112, 117 | A cold key in an open hand before a builder's hoarding; a car park where a door should be. |
| `96` | Dusk — the deadline | 96, 97, 98, 99, 114, 119 | A wet square as the light goes; stalls folding away, one lit doorway far off. |

## Endings (12) — bespoke; these are what readers replay to reach

| hero | valence | scene | faceless alt-line |
|---|---|---|---|
| `120` | good | A home, honestly | *(Wave 1)* Warm lamplight, a window catch being fixed, the water below — a life beginning. |
| `121` | good *(secret)* | The room returned | A woman sitting hard on a half-packed box, a notebook held in both hands, a chair drawn up. |
| `122` | good | On your own terms | A bare room, a borrowed chair, a single key on a windowsill in clean morning light. |
| `123` | good | Vouched for | A bright flat door opening, a name on the paper, a hand accepting a key. |
| `124` | neutral | A room, not a home | A grey room, a figure lying on a bed with a coat still on, a blank wall for a view. |
| `125` | neutral | The kindness returned | A small warm box room off a stranger's hall; a child's shy hello at the door. |
| `126` | neutral | Remembered | A landlady in a lit doorway, remembering a face; a name spoken, a "come back Monday". |
| `127` | neutral | One more week | A cheap hotel room again, a coat hung up, an alarm set on a bedside table. |
| `128` | bad | The deposit gone | An open hand in the dark holding a useless key; a receipt, a phone that rings out. |
| `129` | bad | No one to vouch | A polite closed door in fading light; empty hands, an empty street. |
| `130` | bad | Too late to look | Rooms marked LET on a phone as the last light goes; a trudge back to the hotel. |
| `131` | bad | Thinking about leaving | A cold platform imagined in the dark; a two-o'clock train, a ticket not bought. |

---

## Copy commands (once each hero image exists)

```bash
cd images/new-city/ep-02
# Wave 1
for id in 2 10; do cp 1.webp $id.webp; done
for id in 110 116; do cp 50.webp $id.webp; done
for id in 52 53 54 55 56 59 60 61 62 84; do cp 51.webp $id.webp; done
for id in 8 41 42 43 44 45 46 47 48 49 65 66 68; do cp 40.webp $id.webp; done
for id in 18 19 20 26 115; do cp 25.webp $id.webp; done
for id in 100 105 106 107 108 109 111; do cp 104.webp $id.webp; done
# Wave 2
for id in 5 16 17; do cp 3.webp $id.webp; done
for id in 9; do cp 4.webp $id.webp; done
for id in 11 12 13; do cp 6.webp $id.webp; done
for id in 14 15; do cp 7.webp $id.webp; done
for id in 30 31 32 33 34 35 39 103; do cp 21.webp $id.webp; done
for id in 63 64 77 78 79 92 113; do cp 76.webp $id.webp; done
for id in 71 72 73 74 75 101; do cp 70.webp $id.webp; done
# Wave 3
for id in 27 29 90 91 118; do cp 28.webp $id.webp; done
for id in 57 58 80 81 82 83 86; do cp 85.webp $id.webp; done
for id in 37 38; do cp 36.webp $id.webp; done
for id in 102 117; do cp 112.webp $id.webp; done
for id in 97 98 99 114 119; do cp 96.webp $id.webp; done
```

Endings (120–131) each keep their own bespoke file; no copying.
