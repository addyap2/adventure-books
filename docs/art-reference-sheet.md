# The Address — reference & character sheet

Read this **before** generating anything. The one thing that makes 33 images feel like one
book is that the recurring people, props and places look the same every time they appear.
This sheet locks them. It sits alongside [art-brief.md](art-brief.md) (specs, palette),
[art-shotlist.md](art-shotlist.md) (which passage uses which image) and
[art-prompts.md](art-prompts.md) (the per-image prompts).

## The golden rule: faceless, so "you" is anyone

The reader **is** the hero, so no character is ever shown face-on. People are seen from
behind, from the side, over the shoulder, or as **hands / a silhouette / a reflection**.
This is not a limitation — it's the look. It keeps every learner able to be "you", avoids
fixing an age/gender/ethnicity for a worldwide audience, and removes the single hardest
consistency problem (a repeating face). Identify characters by **wardrobe, posture and
props**, never by face.

## Locked style (freeze this on Wave 1, then never drift)

- **Medium:** atmospheric editorial illustration, painterly but restrained, soft cinematic light.
- **World:** a generic modern European-ish port city, night → early morning. No flags, no
  readable signage, no country-specific landmarks.
- **Palette (matches the app):** warm-cream and deep-teal grounds, ink-dark shadows, and
  **one** warm burnt-orange light source per image (a lamp, a lit window, a sign). Avoid
  pure white / pure black — each image must read on both a cream and a near-black card.
- **Mood:** quiet, uncertain, humane — never frightening. "Warm light in cold places."
- **Frame:** 3:2, one clear subject, subject inside the central 90%, no baked-in text.

The full paste-in **STYLE HEADER** lives at the top of `art-prompts.md`; put it in front of
every prompt so this carries through.

## Recurring cast (by wardrobe + prop, never by face)

| Who | Appears in (scenes) | How to keep them consistent |
|---|---|---|
| **You** (the traveller) | everywhere | Plain dark buttoned coat; a **small hard suitcase** early, a **shoulder bag** later; always from behind or hands-only. The **folded letter** is your recurring prop. |
| **Ada Rowe** (~60, the boss) | `31`, `85`, `88`, and 27/35 | Long neutral coat; **coffee cup in one hand, keys in the other**; a **small yellow luggage label "R. ROWE"** on her bag — this label is the secret-ending clue and must look identical wherever it shows. Calm, upright, brisk-kind. Side/behind only. |
| **Mara** (young traveller) | met at `1`; recurs via `16`, `30` | Big soft **backpack**, a creased **scrap of paper** she keeps rereading; a scarf. Same age-read and pack shape each time. Behind/side. |
| **The agency man** | `24` (and its copies 32/33/60/61/62/90/107), `106`/`68` | A **good, slightly-too-sharp suit**; a clipboard/registration form; an open hand reaching for money. Over-the-shoulder or from behind. He reads as *wrong-smooth*, not menacing. |
| **The night strangers** (kiosk woman, newsstand man, café woman, counter man) | `9` cluster (9/29/43/44/47/95) | Treat as **one visual family**: working people at the edge of a pool of light, one warm gesture — a hand pointing, a shutter half-down, a cup poured. Muted work clothes. They are minor; keep them a consistent *type*, don't individualise. |
| **The child at №16** | `12` (26/52/97/98/111) | A **small silhouette at a lit upstairs window**, curtain edge, calm. Same window, same warm interior glow. |
| **The bench man** (missed the last train) | `13` (esp. 48), ending `145` | A closed coat, a **paper cup**, no bag; stillness. In `145` his kindness returns — a spare key and kettle. |
| **The cleaner** (agente d'entretien) | `30` (117), station `13` (58) | Tabard/overall, a **thermos**, keys; props a door open with her foot. Practical, unhurried. |

## Recurring props & motifs (must match across images)

- **The letter** — a typed, folded sheet; the story's spine. Same paper, same fold (`1`, `4`, `69`, `85`).
- **The yellow "R. ROWE" luggage label** — the secret clue; identical every time (`31`).
- **The café card** — a small business card taped *inside* dark glass, new address just legible (`15`).
- **The returned letters** — a reception tray of envelopes with the **Rosewater address crossed out by hand** (`30`, `63`, `96`).
- **The receipt with only a number** — no name, no address (`24`/`32`, ending `39`).
- **The one warm-lit window** — a single burnt-orange square in a dark façade; the recurring note of hope (`7`, `11`, `54`).

## Recurring locations (continuity notes)

- **The station** — the same cold pillared hall and platform in `1`, `13` (bench), `3` (just outside). Keep the architecture and light identical.
- **Rosewater Street** — one grey hoarding-wrapped building; `7`, `11` (its window), `96` (its courtyard) are the *same* place at different angles.
- **The river / Mill Quay** — the same bend of water and glass towers by night (`54`) and at dawn (`23`, `25`); Rowe's office (`85`) and reception (`30`) look out on it.

## How to hold consistency in the tool (pick one)

1. **Midjourney v7** — generate the cover + Wave 1, pick the winner, then reuse its
   **`--sref`** (style reference) on *every* later prompt; use **`--cref`** from a locked
   render of Ada / Mara / the agency man for their scenes; tune with `--sw`/`--cw`.
2. **Flux.1 (dev) + a small LoRA** — the strongest route at this volume: train a **style
   LoRA** on your 5–8 locked Wave-1 frames, and (optionally) a tiny **object/character
   LoRA** for the yellow label + the letter + Ada. Then batch all 33 in that locked look.
3. **Reference-edit models (e.g. Gemini/"Nano Banana")** — good at *"keep this exact
   subject, put it in a new scene"*: hold the label, the letter and Ada across scenes by
   feeding the locked reference image each time.

Whichever you choose: **freeze a seed/style ref after Wave 1**, paste the STYLE HEADER on
every prompt, and treat all output as drafts — a human curation pass (keep / regenerate)
is non-negotiable.

## First steps (the order that avoids rework)

1. Generate 3–4 candidate looks for the **cover + `1` + `7`**; pick one; freeze the style ref.
2. Do the rest of **Wave 1** (`15`, `24`, `23`, `31`, `36`) in that locked look; confirm on
   both a cream and a near-black card.
3. Render the **reference frames** for Ada Rowe, Mara, the agency man, and the two key
   objects (the yellow label, the letter). These become your `--cref`/LoRA anchors.
4. Batch **Waves 2–3**, then the **endings** (your best, one each).
5. Curate, regenerate the misses, export WebP per the brief, and file per `art-shotlist.md`.
