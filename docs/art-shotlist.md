# The Address — art shot-list (episode 1)

Companion to [art-brief.md](art-brief.md), which holds the specs, palette, naming and
direction. This is the **shot list**: what to draw, in what order, and where each file goes.

## How the files reach the app

Drop a file at `images/new-city/ep-01/<paragraph-id>.webp` and it appears on that
paragraph automatically — no code change. The story shares images **by location**: one
picture serves every passage set in the same place. So:

- Each row below has a **hero id** — name the file after that (e.g. `7.webp`).
- To show the image on the *other* passages in that location, **copy the same file** to
  each of their ids (e.g. `cp 7.webp 45.webp`). Any passage without a file shows a clean
  gradient placeholder, which reads as intentional — so partial delivery is fine.
- The **cover** is `cover.webp` (4:5 portrait, 1080×1350). Everything else is 3:2, 1200×800.

Target: **~30 images** (≈15 locations + a few key beats + 12 endings + cover) — not 123.

---

## Wave 1 — lock the look (do these first, agree the style, then hold it)

These are the beats that carry the most weight; the brief calls them out. Freeze palette,
light and framing here before going on.

| hero id | location / beat | draft alt-text (one faceless line) |
|---|---|---|
| `cover` | Episode cover | A lone figure with a suitcase, seen from behind, small against a vast dark station. |
| `1` | The empty night station | An almost-empty platform under cold light; a single traveller with a letter. |
| `7` | Rosewater Street — the dead address | A grey building behind builders' hoarding, dust on the inside of dark windows, an old sign above a door with no handle. |
| `15` | The Blue Kettle café card | A business card taped inside a dark café window, a new address just legible on it. |
| `24` | The "Work For Everyone" agency | A too-bright office with new carpet and a yellow sign; a man in a good suit, seen over the shoulder. |
| `23` | Mill Quay at dawn | New glass buildings along grey water at first light; gulls, a coffee cart. |
| `31` | The woman with the coffee | A woman reaching a glass door, coffee in one hand; a small yellow luggage label reading R. ROWE. |
| `36` | A good ending — taken on | Warm light through an office window at last; a desk, a chair drawn up, a tray of letters to fix. |

## Wave 2 — the rest of the night's places

| hero id | location / beat | also covers | draft alt-text |
|---|---|---|---|
| `3` | Outside the station / taxi rank | 6, 65, 108 | Wet road at night, taxis waiting, breath in the cold, the river smell almost visible. |
| `4` | On the night bus | 8, 53, 79, 105 | The warm, near-empty interior of a night bus; dark streets sliding past the window. |
| `5` | Lost in the night streets | 49, 50, 115, 116 | Narrow empty streets, one all-night light (a launderette) spilling yellow onto wet stone. |
| `11` | The one light still on | 51, 96 | Looking through a dusty window into an empty office; one small light on behind a glass door at the back. |
| `12` | Number 16 | 26, 52, 97, 98, 111 | A neighbour's doorway at night; an upstairs window lit, a child's shape behind the glass. |
| `54` | The river at night | 19, 28, 55, 99, 100, 101, 123-night | A bridge over black water; new glass offices dark on the far bank, one window lit high up. |
| `13` | The station bench | 22, 48, 58, 126, 128 | A hard bench under station light; a coat pulled close, a paper cup, the long wait for dawn. |
| `16` | The hotel room | 10, 59, 104, 125, 129 | A small clean room, a good bed, a window looking down on a yellow agency sign across the road. |

## Wave 3 — the morning, the office, the trap's end

| hero id | location / beat | also covers | draft alt-text |
|---|---|---|---|
| `30` | Mill Quay reception | 63, 84, 124, 112 | A warm reception desk; a tray of returned letters, old addresses crossed out by hand. |
| `85` | Ms Rowe's office | 86, 92, 94, 120, 121 | A desk over the water; a folder, and on top a returned letter; a chair drawn up for you. |
| `25` | The waking quay | 67, 89, 110, 113 | The quay coming to life at dawn: coffee cart, delivery vans, gulls on grey water. |
| `106` | The empty lot | 60, 61, 62, 90, 107 | A fenced empty lot behind the agency — weeds, a burnt mattress, no job that was ever real. |
| `9` | The kiosk woman | 47, 56, 57, 102, 103, 119, 127 | A woman pulling down a kiosk shutter on a dark corner; the only person on the street. |

## Wave 4 — the remaining endings (bespoke; your best work)

Endings are what readers replay to reach — one image each, no sharing.

| id | ending | draft alt-text |
|---|---|---|
| `38` | Good — the step-greeting (secret) | On the office step, a woman turning, half-smiling, recognised before she has said a word. |
| `141` | Good — hired on merit | A plain handshake in a plain office; morning light, nothing dramatic, everything earned. |
| `142` | Good — the best night (secret) | Walking in clear-eyed and rested; the river bright through the window behind the desk. |
| `37` | Neutral — spring work | A name written by hand on a real sheet of paper; a door held open to the street. |
| `143` | Neutral — remembered | A hand closing a notebook with your name in it; the city going on outside. |
| `144` | Neutral — processed, not seen | New carpet, a lanyard, a screen; everything correct and nothing felt. |
| `145` | Neutral — the kindness returned | A borrowed kettle and a spare key on a stranger's table; not hired, not alone. |
| `39` | Bad — the dead phone number | A locked glass door, an empty office behind it, a receipt with only a number on it. |
| `40` | Bad — the train home | A departures board; a two-o'clock train the way you came, and just enough for the fare. |
| `146` | Bad — too late | A closed diary and full chairs in a reception; a kind, final shake of the head. |
| `147` | Bad — the bench at dawn | Grey morning over an empty bench; nine o'clock come and gone, feet still too cold to move. |

---

## Delivery checklist (per the brief)

- [ ] 1200×800 (moments) / 1080×1350 (cover), WebP ~q80, ≤120/180 KB
- [ ] subject in the central 90%; no baked-in text
- [ ] reads on both a cream and a near-black card; faceless viewpoint
- [ ] nothing that names a specific country
- [ ] one alt line supplied per image (draft above — refine as you draw)
- [ ] filed at `images/new-city/ep-01/<id>.webp`; copies made for the "also covers" ids
