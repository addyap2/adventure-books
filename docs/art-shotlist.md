# The Address — art shot-list (episode 1)

Companion to [art-brief.md](art-brief.md) (specs, palette, direction) and
[art-prompts.md](art-prompts.md) (ready-to-generate prompts). **This file is the
authoritative map**: which passages share which image, and where each file goes.

## How the files reach the app

Drop a file at `images/new-city/ep-01/<node-id>.webp` and it appears on that passage
automatically — no code change. The story shares images **by scene**: one picture serves
every passage set in the same place or built on the same beat. So:

- Each scene below has a **hero id** — name the file after that (e.g. `7.webp`).
- To show it on the *other* passages in that scene, **copy the same file** to each of
  their ids (e.g. `cp 7.webp 17.webp`). The commands are listed per scene below.
- The **cover** is `cover.svg` (vector; the reader loads it for the cover panel and the
  library card). Everything else is 3:2, 1200×800 WebP.
- Any passage without a file shows a clean gradient placeholder that reads as intentional,
  so **partial delivery is fine** — ship a scene at a time.

**Total: 33 images** — 20 scenes + 12 endings + the cover — covering all 123 passages.
Not 123 one-offs: fewer, consistent images make it feel like one book.

The recurring cast, wardrobe, props and the consistency technique are in
[art-reference-sheet.md](art-reference-sheet.md) — read that **before** generating, so
Ada Rowe, Mara, the agency man and the key objects look the same every time they appear.

---

## Wave 1 — lock the look (do these first; agree the style, then hold it)

The beats that carry the most weight. Freeze palette, light and framing here.

| hero | scene | serves passages | faceless alt-line |
|---|---|---|---|
| `cover` | Episode cover *(4:5)* | — | A lone figure with a suitcase, from behind, small against a vast dark station. |
| `1` | The empty night station | 1, 2, 41, 42, 109 | An almost-empty platform under cold light; a single traveller with a letter. |
| `7` | Rosewater Street — the dead address | 7, 17, 18, 20, 45, 96 | A grey building behind hoarding; dust on dark windows; a dead sign; a doorless door. |
| `15` | The Blue Kettle café card | 15, 56, 57, 102, 103, 119, 127 | A business card taped inside a dark café window, a new address just legible. |
| `24` | The "Work For Everyone" agency | 24, 32, 33, 60, 61, 62, 90, 107 | A too-bright office, new carpet, a yellow sign; a man in a good suit, over the shoulder. |
| `23` | Mill Quay at dawn | 23, 67, 89, 100, 101, 110, 113 | New glass buildings along grey water at first light; gulls, a coffee cart. |
| `31` | The woman with the coffee | 27, 31, 88 | A woman reaching a glass door, coffee in hand; a small yellow label reading R. ROWE. |
| `36` | Good ending — taken on | 36 | Warm light through an office window; a desk, a chair drawn up, a tray of letters to fix. |

## Wave 2 — the rest of the night's places

| hero | scene | serves passages | faceless alt-line |
|---|---|---|---|
| `3` | Outside the station / taxi rank | 3, 6, 65, 108, 122 | Wet road at night, taxis waiting, breath in the cold. |
| `4` | On the night bus | 4, 8, 53, 79, 105 | The warm, near-empty interior of a night bus; dark streets past the window. |
| `5` | Lost in the night streets | 5, 14, 49, 50, 115, 116 | Narrow empty streets, one all-night light spilling yellow onto wet stone. |
| `11` | The one light still on / the scraped name | 11, 46, 51, 118 | Through a dusty window: one small light behind a glass door; a name half-scraped off it. |
| `12` | Number 16 | 12, 26, 52, 97, 98, 111 | A neighbour's doorway at night; an upstairs window lit, a child's shape behind the glass. |
| `54` | The river at night | 19, 28, 54, 55, 99, 123 | A bridge over black water; dark glass offices, one window lit high up. |
| `13` | The station bench | 13, 22, 48, 58, 77, 126, 128 | A hard bench under station light; a coat pulled close, a paper cup, the long wait. |
| `16` | The hotel room | 10, 16, 59, 75, 104, 125, 129 | A small clean room; a window onto a yellow agency sign across the road. |
| `69` | The letter, reread *(object beat)* | 21, 34, 69, 72, 73, 114 | Hands and an open bag: a folded letter, a little money, a dying phone — the choice in the palm. |
| `9` | The stranger who points the way | 9, 29, 43, 44, 47, 95 | A shuttered corner kiosk at night; the only person about, a hand pointing the way. |

## Wave 3 — the morning, the office, the trap's end

| hero | scene | serves passages | faceless alt-line |
|---|---|---|---|
| `30` | Mill Quay reception | 30, 63, 84, 91, 112, 117, 124 | A warm reception desk; a tray of returned letters, old addresses crossed out by hand. |
| `85` | Ms Rowe's office | 35, 85, 86, 92, 94, 120, 121 | A desk over the water; a folder, and on top a returned letter; a chair drawn up for you. |
| `25` | The waking quay | 25 | The quay waking: coffee cart, vans, gulls; a cup held in clean hands. |
| `106` | The empty lot (the scam's end) | 68, 106 | A fenced empty lot — weeds, a burnt mattress — where a job was promised. |

## Wave 4 — the endings (bespoke; your best work, one image each, no sharing)

Endings are what readers replay to reach.

| id | ending | faceless alt-line |
|---|---|---|
| `38` | Good — the step-greeting (secret) | On the office step, a woman turning, recognised before she has said a word. |
| `141` | Good — hired on merit | A plain handshake in a plain office; morning light, everything earned. |
| `142` | Good — the best night (secret) | Walking in clear-eyed and rested; the river bright through the window. |
| `37` | Neutral — spring work | A name written by hand on real paper; a door held open to the street. |
| `143` | Neutral — remembered | A hand closing a notebook with your name in it; the city going on outside. |
| `144` | Neutral — processed, not seen | New carpet, a lanyard, a screen; everything correct and nothing felt. |
| `145` | Neutral — the kindness returned | A borrowed kettle and a spare key on a stranger's table; not hired, not alone. |
| `39` | Bad — the dead phone number | A locked glass door, an empty office behind it, a receipt with only a number. |
| `40` | Bad — the train home | A departures board; a two-o'clock train the way you came, and just enough for the fare. |
| `146` | Bad — too late | A closed diary and full chairs in a reception; a kind, final shake of the head. |
| `147` | Bad — the bench at dawn | Grey morning over an empty bench; nine o'clock gone, feet still too cold to move. |

---

## The copy commands (run from `images/new-city/ep-01/` after you drop each hero file)

```sh
cp 1.webp   2.webp;  cp 1.webp  41.webp;  cp 1.webp  42.webp;  cp 1.webp 109.webp
cp 3.webp   6.webp;  cp 3.webp  65.webp;  cp 3.webp 108.webp;  cp 3.webp 122.webp
cp 4.webp   8.webp;  cp 4.webp  53.webp;  cp 4.webp  79.webp;  cp 4.webp 105.webp
cp 5.webp  14.webp;  cp 5.webp  49.webp;  cp 5.webp  50.webp;  cp 5.webp 115.webp;  cp 5.webp 116.webp
cp 7.webp  17.webp;  cp 7.webp  18.webp;  cp 7.webp  20.webp;  cp 7.webp  45.webp;  cp 7.webp  96.webp
cp 9.webp  29.webp;  cp 9.webp  43.webp;  cp 9.webp  44.webp;  cp 9.webp  47.webp;  cp 9.webp  95.webp
cp 11.webp 46.webp;  cp 11.webp 51.webp;  cp 11.webp 118.webp
cp 12.webp 26.webp;  cp 12.webp 52.webp;  cp 12.webp 97.webp;  cp 12.webp 98.webp;  cp 12.webp 111.webp
cp 13.webp 22.webp;  cp 13.webp 48.webp;  cp 13.webp 58.webp;  cp 13.webp 77.webp;  cp 13.webp 126.webp;  cp 13.webp 128.webp
cp 15.webp 56.webp;  cp 15.webp 57.webp;  cp 15.webp 102.webp;  cp 15.webp 103.webp;  cp 15.webp 119.webp;  cp 15.webp 127.webp
cp 16.webp 10.webp;  cp 16.webp 59.webp;  cp 16.webp 75.webp;  cp 16.webp 104.webp;  cp 16.webp 125.webp;  cp 16.webp 129.webp
cp 23.webp 67.webp;  cp 23.webp 89.webp;  cp 23.webp 100.webp;  cp 23.webp 101.webp;  cp 23.webp 110.webp;  cp 23.webp 113.webp
cp 24.webp 32.webp;  cp 24.webp 33.webp;  cp 24.webp 60.webp;  cp 24.webp 61.webp;  cp 24.webp 62.webp;  cp 24.webp 90.webp;  cp 24.webp 107.webp
cp 30.webp 63.webp;  cp 30.webp 84.webp;  cp 30.webp 91.webp;  cp 30.webp 112.webp;  cp 30.webp 117.webp;  cp 30.webp 124.webp
cp 31.webp 27.webp;  cp 31.webp 88.webp
cp 54.webp 19.webp;  cp 54.webp 28.webp;  cp 54.webp 55.webp;  cp 54.webp 99.webp;  cp 54.webp 123.webp
cp 69.webp 21.webp;  cp 69.webp 34.webp;  cp 69.webp 72.webp;  cp 69.webp 73.webp;  cp 69.webp 114.webp
cp 85.webp 35.webp;  cp 85.webp 86.webp;  cp 85.webp 92.webp;  cp 85.webp 94.webp;  cp 85.webp 120.webp;  cp 85.webp 121.webp
cp 106.webp 68.webp
```

(`cover`, `25`, and every ending stand alone — no copies.)

## Delivery checklist (per the brief)

- [ ] 1200×800 (moments) WebP ~q80, ≤120 KB; cover is `cover.svg` (vector)
- [ ] subject in the central 90%; no baked-in text
- [ ] reads on both a cream and a near-black card; faceless viewpoint
- [ ] nothing that names a specific country
- [ ] recurring cast matches [art-reference-sheet.md](art-reference-sheet.md)
- [ ] one alt line supplied per image (draft above — refine as you draw)
- [ ] filed at `images/new-city/ep-01/<hero>.webp`; copies made per the commands above
