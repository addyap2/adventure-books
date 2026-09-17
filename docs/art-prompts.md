# The Address — image-generation prompt sheet

For the visual partner. These turn the **actual passages** into ready-to-generate prompts,
organised **by scene** (33 images) so the set stays consistent — not one-per-passage
(see `art-shotlist.md` for why). Companion specs live in `art-brief.md`; the recurring
cast, props and consistency technique are in `art-reference-sheet.md`.

> **Which passages each image serves** is defined authoritatively in `art-shotlist.md`
> (with the exact `cp` commands). The `(also: …)` hints below are indicative — if they
> ever disagree with the shot-list, the shot-list wins.

## How to use this

1. **Lock the look on Wave 1 first.** Generate the cover + the seven Wave 1 images, pick the
   winning style, and **fix a seed / style-reference** you reuse for everything after. Consistency
   matters more than any single image.
2. **Every prompt = the STYLE HEADER (below) + the image's own lines.** Paste the header in front
   of each prompt so palette, mood, and the faceless rule carry through.
3. **Deliver** as WebP, 3:2 **1200×800** (cover 4:5 **1080×1350**), ≤120 KB (cover ≤180 KB), sRGB.
   File at `images/new-city/ep-01/<id>.webp`; for the "also covers" ids, drop a **copy of the same
   file** under each (e.g. `cp 7.webp 45.webp`). Passages with no file show a clean placeholder.
4. **No video per passage** (phone-first, mobile-data budget). If you want motion, keep it to a
   subtle drift on the **cover** and **endings** only.

## STYLE HEADER — paste before every prompt

```
Atmospheric editorial illustration, painterly but restrained, soft cinematic light.
A generic modern European-ish port city, night into early morning. Limited palette per
image: warm cream and deep-teal grounds, ink-dark shadows, and ONE warm burnt-orange
light source (a lamp, a lit window, a sign). Mood: quiet, uncertain, humane — never
frightening; "warm light in cold places". FACELESS viewpoint — never show a face: frame
from behind or over the shoulder, or show only hands, feet, a reflection, or the empty
scene. Culturally neutral: no flags, no readable signage, no country-specific landmarks.
Nothing important in the outer 5%. 3:2 landscape.
Negative: no text, no lettering or numbers, no faces, no watermark, no logos, no gore.
```

---

## Wave 1 — lock the look

### `cover.webp` — episode cover *(4:5 portrait)*
**Prompt:** A lone traveller seen from behind with a small suitcase, standing at the mouth of a vast, almost-empty night railway station; a single warm lamp far down the platform; cold blue light on wet stone. Portrait 4:5, cinematic depth.
**Alt:** A lone figure with a suitcase, seen from behind, small against a vast dark station.

### `1.webp` — the empty night station *(also: 2, 41, 42, 43, 44, 77)*
**Prompt:** An almost-empty railway platform at eleven o'clock at night; a single traveller from behind holding a folded letter; long cold perspective of pillars and dark tracks; one warm light glowing far ahead.
**Alt:** An almost-empty platform under cold light; a single traveller with a letter.

### `7.webp` — Rosewater Street, the dead address *(also: 11 uses its own; 45, 46, 51, 95, 96, 118)*
**Prompt:** A grey building behind builders' hoarding on a dark, empty street; thick dust on the inside of tall windows; an old painted company sign above a door that has no handle; a faint warm glow from one window deep inside.
**Alt:** A grey building behind hoarding, dust on dark windows, a dead sign, a doorless door.

### `15.webp` — the café card *(also: 9 uses its own; 56, 57, 102, 103, 119, 127)*
**Prompt:** A dark café shopfront at night, closed; a small business card taped inside the window beside the opening hours; rain beading on the glass; the cold reflection of a hand and a phone's faint glow; interior unlit.
**Alt:** A business card taped inside a dark café window, a new address just legible.

### `24.webp` — the "Work For Everyone" agency *(also: 60, 61, 32, 33, 62, 90, 68)*
**Prompt:** A too-bright, too-new employment office seen over the shoulder from the doorway; cheap fresh carpet, a large plain yellow sign, a man in a good suit at a desk (from behind or side — faceless); the fluorescent warmth feels a little wrong.
**Alt:** A too-bright office with new carpet and a yellow sign; a man in a good suit, over the shoulder.

### `23.webp` — Mill Quay at dawn *(also: 25 uses its own; 89, 110, 113, 67, 100, 101, 54-day)*
**Prompt:** New glass office buildings along a grey river at first light; gulls on the water; a coffee cart just opening with a small warm glow; calm, cold dawn with a thin warm band on the horizon.
**Alt:** New glass buildings along grey water at first light; gulls, a coffee cart.

### `31.webp` — the woman with the coffee *(the secret-ending clue)*
**Prompt:** Early morning at a glass office door on the quay; a woman from behind/side (faceless) with a coffee in one hand and keys in the other; a small yellow luggage label on her bag; soft dawn light, one warm reflection.
**Alt:** A woman reaching a glass door, coffee in hand; a small yellow luggage label on her bag.

### `36.webp` — a good ending: taken on
**Prompt:** Inside a modest river-side office at last; warm lamplight; a chair drawn up to a desk that holds a tray of letters waiting to be fixed; the grey river soft through the window; quiet relief.
**Alt:** Warm light through an office window; a desk, a chair drawn up, a tray of letters to fix.

---

## Wave 2 — the rest of the night

### `3.webp` — outside the station / taxi rank *(also: 6, 65, 108)*
**Prompt:** Outside a station at night; wet road mirroring the lights; two or three taxis waiting, drivers watching; a bus stop nearby; cold damp air, the river implied; from a newcomer's viewpoint.
**Alt:** Wet road at night, taxis waiting, breath in the cold.

### `4.webp` — on the night bus *(also: 8, 53, 79, 105)*
**Prompt:** The warm, almost-empty interior of a night bus; rows of empty seats; dark wet streets sliding past the windows; a letter held in a lap, hands only.
**Alt:** The warm, near-empty interior of a night bus; dark streets past the window.

### `5.webp` — lost in the night streets *(also: 49, 50, 115, 116)*
**Prompt:** A narrow, empty night street where the map has stopped meaning anything; one warm yellow light from an all-night launderette spilling onto wet cobbles; a lone figure from behind.
**Alt:** Narrow empty streets, one all-night light spilling yellow onto wet stone.

### `11.webp` — the one light still on *(also: shares with 7's building)*
**Prompt:** Looking through a dust-smeared office window into darkness; empty desks, one overturned chair, a calendar stopped long ago; a single small warm light on behind a glass door at the very back.
**Alt:** Through a dusty window: empty desks and one small light on behind a glass door.

### `12.webp` — number 16 *(also: 26, 52, 97, 98, 111)*
**Prompt:** A neighbour's doorway on a dark terraced street at night; a man in a dressing gown half-seen at the door (faceless), warm hall light behind him; an upstairs window lit with a child's small silhouette.
**Alt:** A neighbour's doorway at night; an upstairs window lit, a child's shape behind the glass.

### `54.webp` — the river at night *(also: 19, 28, 55, 99, 123)*
**Prompt:** A bridge over black water at night; on the far bank new glass offices stand dark and clean; one window lit high up, a single warm square; cold blue, reflections breaking on the water.
**Alt:** A bridge over black water; dark glass offices, one window lit high up.

### `13.webp` — the station bench *(also: 22, 48, 58, 126, 128)*
**Prompt:** A hard station bench under cold overhead light; a coat pulled close and a paper cup, the person from behind/side (faceless); the vast empty hall around; the long wait for dawn.
**Alt:** A hard bench under station light; a coat pulled close, a paper cup, the long wait.

### `16.webp` — the hotel room *(also: 10, 59, 104, 125, 129)*
**Prompt:** A small, clean, cheap hotel room at night; a good bed; through the window, across the road, a glowing yellow agency sign; warm lamp inside, cold blue outside.
**Alt:** A small clean room; a window onto a yellow agency sign across the road.

### `69.webp` — the letter, reread *(also: 21, 34, 72, 73, 114)*
**Prompt:** Close, top-down on two cupped hands over an open shoulder bag on the knees; inside, a folded typed letter, a few thin banknotes, and a phone showing one bar of battery; a photograph face-down, unturned; cold night light with one warm edge; the whole decision held in the palms. Hands only — no face.
**Alt:** Hands and an open bag: a folded letter, a little money, a dying phone — the choice in the palm.

---

## Wave 3 — the morning, the office, the trap's end

### `30.webp` — reception *(also: 63, 84, 124, 112)*
**Prompt:** A warm, quiet reception desk in a river-side office in the morning; on the desk a tray of returned letters with addresses crossed out by hand; a receptionist from behind/side (faceless); coffee-warm light.
**Alt:** A warm reception desk; a tray of returned letters, old addresses crossed out.

### `85.webp` — Ms Rowe's office *(also: 86, 92, 94, 120, 121)*
**Prompt:** An office over the water in clear morning light; a desk with a folder and, squared on top, a returned letter; two chairs; the night's bridge just visible through the window; calm.
**Alt:** A desk over the water; a folder, and on top a returned letter; a chair drawn up.

### `25.webp` — the waking quay *(secondary to 23; use if a distinct frame is wanted)*
**Prompt:** The quay coming alive at dawn: delivery vans along wet stone, gulls, a coffee cart's small warm light; a figure from behind with clean hands holding a paper cup; a hopeful cold morning.
**Alt:** The quay waking: coffee cart, vans, gulls; a cup held in clean hands.

### `106.webp` — the empty lot (the scam's end)
**Prompt:** A fenced empty lot behind a city street in flat daylight; weeds, a burnt mattress, scattered litter; no building, no job; grey even light; quiet desolation.
**Alt:** A fenced empty lot — weeds, a burnt mattress — where a job was promised.

### `9.webp` — the kiosk woman
**Prompt:** A woman pulling down the metal shutter of a small street kiosk late at night (from behind/side, faceless); a dark empty corner; one streetlight; she is the only person on the street.
**Alt:** A woman pulling down a kiosk shutter on a dark corner; the only person on the street.

---

## Wave 4 — the endings (bespoke, your best work)

### `38.webp` — good, the step-greeting *(secret)*
**Prompt:** On an office step in soft morning light, a woman (faceless, caught mid-turn) as if recognised before a word is spoken; coffee and keys in hand; a warm, surprised stillness.
**Alt:** On the step, a woman turning, recognised before she has said a word.

### `141.webp` — good, hired on merit
**Prompt:** A plain handshake in a plain morning office, hands only; even window light; nothing dramatic — everything earned.
**Alt:** A plain handshake in a plain office; morning light, everything earned.

### `142.webp` — good, the best night *(secret)*
**Prompt:** Walking into a bright river-side office, rested and clear, seen from behind; the river luminous through the glass; a clean, earned brightness.
**Alt:** Walking in clear-eyed and rested; the river bright through the window.

### `37.webp` — neutral, spring work
**Prompt:** A name written by hand on a real sheet of paper (hands, pen, close in); beyond, a door held open to a bright street; a quiet "not yet, but soon".
**Alt:** A name written by hand on real paper; a door held open to the street.

### `143.webp` — neutral, remembered
**Prompt:** A hand closing a notebook with a handwritten name on the open page; the ordinary city going on through a window behind; small and human.
**Alt:** A hand closing a notebook with your name in it; the city going on outside.

### `144.webp` — neutral, processed, not seen
**Prompt:** New carpet, a lanyard on a desk, a glowing screen; a figure from behind (faceless) standing in it; everything correct and a little cold; deliberately flat, even light.
**Alt:** New carpet, a lanyard, a screen; everything correct and nothing felt.

### `145.webp` — neutral, the kindness returned
**Prompt:** A borrowed kettle and a spare key on a stranger's small table, two mugs; warm modest lamplight; not hired, but not alone.
**Alt:** A borrowed kettle and a spare key on a stranger's table; not hired, not alone.

### `39.webp` — bad, the dead phone number
**Prompt:** A locked glass office door at midday; through it an empty room stripped of furniture; a receipt held in a hand bearing only a number; flat daylight, no warmth.
**Alt:** A locked glass door, an empty office behind it, a receipt with only a number.

### `40.webp` — bad, the train home
**Prompt:** A station departures board rendered as abstract split-flap shapes (no readable text); a two-o'clock platform; a figure from behind with a suitcase, leaving; grey resignation.
**Alt:** A departures board; a two-o'clock train the way you came, and just enough for the fare.

### `146.webp` — bad, too late
**Prompt:** A reception at twenty past nine; a closed diary, chairs full of other people; a receptionist's kind, final small gesture (faceless); the river indifferent through the window.
**Alt:** A closed diary and full chairs; a kind, final shake of the head.

### `147.webp` — bad, the bench at dawn
**Prompt:** Grey morning over an empty station bench; a cold paper cup; feet and legs only, still; nine o'clock light; the reason for coming quietly gone.
**Alt:** Grey morning over an empty bench; nine o'clock gone, feet still too cold to move.
