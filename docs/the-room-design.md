# The Room — book 2 design & build plan

*Episode 2 of the New City arc.* This is the design to build against, produced by filling the
shape the playbook fixes ([authoring-playbook.md](authoring-playbook.md)) and the flagship
settles ([flagship-design.md](flagship-design.md)). Story first, then structure, then prose,
then languages, then art. The tone is inherited and non-negotiable: *quiet, atmospheric, a
little uncertain — not frightening. Warm light in cold places.*

Book 1 (*The Address*) ended with you hired at **Kessler and Rowe**, told to "fix the letters."
Book 2 begins three days later. You carry into it who you became on that first night:
`state_in` = { `dodged_scam`, `told_truth`, `knows_name` }.

---

## 1. Premise

You have the job. You do **not** have anywhere to live. The cheap hotel by the yellow agency
sign wants its room back by **Saturday night** — there is a booking after yours — and Kessler
and Rowe paid you one week in advance, which is exactly enough for a deposit and nothing spare.
So you have **one grey Saturday**, dawn to dark, and a pocket of money you cannot afford to
lose, to find a room in a city that does not know you.

The trouble is not that there are no rooms. It is that a stranger with **no local references
and no one to vouch for them** is invisible to the good landlords and irresistible to the bad
ones. One listing is too good — a bright room, cheap, keys today, deposit first. It is the same
machine as the "Work For Everyone" agency, wearing a better suit: **the letting agent** who
takes your deposit for a room that was never his to let.

**The through-line (the pull across 125 passages):** the one *real* room you are shown — up a
back stair, over the old rope-works by the canal — was left in a hurry. The last tenant's things
are half-packed and abandoned: a coat, a tin of buttons, **a notebook of addresses**. The
landlady, **Mrs Halloran**, is oddly quick to let it again and oddly reluctant to say where the
last tenant went. *Who left, why the rush, and why won't she say?* The answer is not sinister —
it is sad and ordinary, and it turns on the same thing book 1 did: whether you are the sort of
person who returns a stranger's lost things or keeps your head down. Returning the notebook is
how you are *seen*, and being seen is how you get the room.

**Theme (continued):** the difference between a **room** and a **home** — between being
*processed* by a market and being *taken in* by a person. Nobody is a villain except the people
selling shelter they don't have. The city is cold and bright and busy; the warmth is in the few
who look at a stranger and decide to help.

**Recurring faces:** warmth lives in people, so faces carry across.
- **Ms Rowe** — no longer a stranger on a step but your *employer*. If you were honest with her
  in book 1 (`told_truth`), her word can vouch for you now; the whole arc of book 1 pays a
  literal dividend.
- **the kiosk woman** — the city fixture from book 1, still at her corner; still the first
  person who actually helps.
- **Mrs Halloran** — new warm anchor: the canal-side landlady with the real room and the thing
  she won't say.
- **Dania** — new: a fellow new-hire at Kessler and Rowe, also new to the city, also looking;
  the "fellow traveller" figure. You can look together or apart.

**The world flips.** Book 1 was one night; book 2 is one **short winter day** — the same city
seen cold and bright and indifferent instead of cold and dark and empty. The single warm light
is no longer a street lamp but a **lit doorway with a room behind it**. This drives the visual
identity (§7).

---

## 2. What "125 passages" buys, and the rule that governs it

Same rule as the flagship: **every passage is written three times (A2/B1/B2) and glossed in
eight languages.** 125 passages ≈ 375 authored prose units + a ~250-word book lexicon × 8
languages. So a passage earns its place only if it adds **a real decision, a distinct beat, or
texture the reader will feel** — never padding between two choices.

We sit slightly below the flagship's 150 on purpose: book 2 is one day, not one night-plus-
morning, and a tighter graph keeps the second book shippable while holding the top of the CYOA
band (~100–150).

---

## 3. Act structure & passage budget

Three acts across one Saturday, plus the ending fan.

| Act | Beat | Depth | Budget |
|---|---|---|---|
| **I — Morning** (dawn→midday) | The hotel and the Saturday-night deadline; the money you must not lose; the kiosk woman's paper vs. the glossy online listing; Dania at the corner, also looking; the letting agent's too-good ad; how you'll spend the one day and the one purse | The inventory-of-money beat; the first fork between the cheap real world and the shiny trap; deciding whether to look with Dania or alone | ~30 |
| **II — The Viewings** (midday→dusk) | Crossing the city to see rooms: the agent's office (the scam given room to tempt — a queue, a plausible pitch, a deposit "to hold it"); a grim real bedsit; the good flat that needs a **guarantor** you don't have; the canal room over the rope-works, Mrs Halloran, and the last tenant's abandoned things; neighbours in the stairwell | A second false lead so the map has real dead ends; the scam's pitch given space; the guarantor wall (where `told_truth`/Ms Rowe pays off); the mystery of the vanished tenant seeded and deepened; a kindness offered to a neighbour | ~62 |
| **III — The Decision** (dusk→night) | Which door you knock on last; the deposit handed over (or not); asking Ms Rowe to vouch; returning (or keeping) the notebook; Mrs Halloran's answer | The interview-scale scene of book 1, here the *decision* scene: honesty vs. haste, the keepsake returned, the landlady's verdict | ~21 |
| **Endings** | see §5 | 5 → 12 | 12 |

**Target: ~125 passages, 12 endings.**

---

## 4. State model (the flags)

`state_in` carried from book 1: **`dodged_scam`, `told_truth`, `knows_name`** — read here so
the first night has consequences on the third day.

**Eight own flags, no more**, each earned at a clear moment and read at a clear payoff. Every
flag is *set* somewhere **and** *read* (gates a choice) somewhere — the validator enforces it.

| Flag | Earned when | Pays off at |
|---|---|---|
| `kept_money` | you spend the day cheaply — walk not taxi, ignore the paid-listings site | affording a real deposit at dusk (good end *On your own terms*) |
| `dodged_letting_scam` | you refuse the agent's "deposit to hold it" (**the trap**) | the best-ending gate; a clean, unconned arrival |
| `paid_letting_scam` | you hand the agent a deposit for the too-good room | the *deposit gone* bad ending — broke, conned twice-shy too late |
| `has_reference` | you ask Ms Rowe (or a colleague) to vouch for you | unlocks the good flat that needs a guarantor (good end *Vouched for*) |
| `found_keepsake` | you pick up the last tenant's notebook from the canal room | the secret *room returned* ending (you give it back) |
| `helped_neighbour` | you do a small kindness in the stairwell (carry shopping, mind a child) | the *kindness returned* neutral ending — a spare room offered |
| `rushed` | you take the first room without really seeing it | the *a room, not a home* neutral ending — a technical win that reads flat |
| `warm_welcome` | you are honest with Mrs Halloran about being new and having no one | the warmest ending — she gives you the room on trust |

**How the carried-in flags read here:**
- `told_truth` → gates asking Ms Rowe to vouch: she trusts you *because* you were honest on
  your first night. (§ the reference thread.)
- `knows_name` → gates a warm recognition beat and the *Remembered* neutral ending.
- `dodged_scam` → gates spotting the letting agent's pitch for what it is a beat sooner — the
  street-sense you paid for last time.

**Discipline:** every flag-gated choice is accompanied by an ungated "otherwise" path; no
paragraph is reachable in a state that offers nothing to do. Validator-enforced on every push.

`state_out` (everything book 2 can set, so book 3 can read it): all eight own flags.
**`arc_flags`** (carried forward for book 3 to read via its `state_in`): `dodged_letting_scam`,
`warm_welcome`, `found_keepsake` — who you became finding your first home.

---

## 5. Endings (12) — balanced 4 good / 4 neutral / 4 bad

Replay is where the language lands, so endings get the best writing and bespoke art. Two are
**secret** (clue/relationship-gated), rewarding readers who both *noticed* and *chose well*.

**Win (4)**
- *A home, honestly* — gated `warm_welcome`: Mrs Halloran gives you the canal room on trust
  because you were straight about having no one. The warmest ending; carries into the arc.
- *The room returned* — **secret**, gated `found_keepsake`: you return the notebook; the last
  tenant was Mrs Halloran's own son, gone to sea, and the address you carry back to her is how
  she takes you in. The mystery pays off.
- *On your own terms* — gated `kept_money` + `dodged_letting_scam`: no favours, no con — you
  secure a modest real room by your own careful means. Clean and independent, a little bare.
- *Vouched for* — gated `has_reference`: Ms Rowe's word unlocks the good flat that needed a
  guarantor. You are new, but you are *known*.

**Neutral / bittersweet (4)**
- *A room, not a home* — gated `rushed`: you take the first thing sight-unseen. It is yours, it
  is fine, it is empty. A technical win that reads as a loss — the sharpest ending in the book.
- *The kindness returned* — gated `helped_neighbour`: no room secured, but a neighbour you
  helped offers their box room. Warmth without winning.
- *Remembered* — gated `knows_name` (from book 1): no room today, but a landlady keeps your
  name and says come back Monday. You are becoming someone the city recognises.
- *Back to the hotel, one more week* — ungated fallback: you find nothing, but you have learned
  the city's map and its prices. Not a loss, just not yet.

**Lose (4)**
- *The deposit gone* — gated `paid_letting_scam`: the room was never his to let; the money that
  was your deposit is gone and Saturday night is here.
- *No one to vouch* — ungated fallback: no money kept, no reference, no honesty leverage; every
  good door is a polite no and the day runs out.
- *Too late to look* — ungated fallback: you spent the daylight chasing the wrong lead; by dark
  the real rooms are taken.
- *You think about leaving* — ungated fallback (echoes book 1's two-o'clock train): the city
  will not house you, and you wonder whether it wants you at all.

At least one clearly good and one clearly bad (validator warns otherwise). ✔

---

## 6. Levels & lexicon

- **Three levels** (A2/B1/B2), prose per level over one shared graph; validator holds each
  passage inside its CEFR band. Same model as the flagship (bible §6/§6a).
- **Book lexicon ~250 words**, base-keyed, English + 8 languages, embedded in the book JSON.
  New book, new world → its **own** lexicon, tilted to the subject: *rent, deposit, landlord,
  tenant, guarantor, reference, lease, stairwell, damp, notice, spare, afford* and the concrete
  furniture of rooms and streets by day. It re-uses none of book 1's file (the shared base is
  empty), but shared *words* that recur (kiosk, letter, address) are re-authored to the same
  glosses for consistency.
- **The A2-choice caveat (bible §6b):** the branching inference is identical across levels, so
  at A2 the **choice text** must be unambiguous and low-inference. Required check in review.
- **On-demand passage gist** (`content/gist/<lang>.json`) — as the flagship: French first over
  all passages; es/it/de/pt over the pivotal beats + 12 endings; ru/ar/zh await translators.
- **Native review is the launch gate** — machine-drafted glosses in 8 languages ship to a
  speaker's check first. The one hard gate between "done" and "launched."

**Language focus** (declared per level in the JSON, for the classroom):
- A2 — *present simple, have/have got; money and prices; rooms and furniture.*
- B1 — *future forms and first conditional; renting, agreements, comparisons.*
- B2 — *inference, conditionals and hedging; trust, obligation and the housing market.*

---

## 7. Visual identity (per book)

Book 2 is its own world: the same city, but **cold winter daylight** instead of night. Declared
once as `identity`; the one reader skins itself to it — no per-book code.

- **name:** *Rope-Works Winter* — **mood:** "A cold bright city by day; one lit doorway with a
  warm room behind it."
- **palette:** a daytime-cold set — pale bone-grey ground, colder blues, and the single warm
  **accent moved to a hearth amber** that now means *a door that opens*, the choice `§ N`,
  glossed underlines, the progress bar. `secondary` is a canal-green.
  - `ground` `#E9E6DE` … actually **night is the reader's default and paper is the override**,
    so identity ships the *night* palette of this world (a colder, bluer night than book 1's),
    and the universal paper mode still overrides. Final values in the JSON `identity` block.
- **cover.kind:** `daybreak` (a lit doorway in a grey street) with `glow: true` for the warm room.
- **type:** inherited families (Fraunces / Hanken Grotesk / JetBrains Mono), declared.
- **slug:** `the-room`; **hero.line** the eight-language morph sentence for the landing; **sub**
  the same learner promise as book 1.

Shipping book 2 = write its JSON (prose + lexicon + `identity` + `slug`) and commit its OG PNG
(`node scripts/build_og.mjs`). No new code, no routing edits — `/b/the-room` serves it.

---

## 8. Build phases & gates (this book)

Each phase is a commit; each gate is `python3 scripts/build_book.py content/episode-02.json
--lexicon content/lexicon.json` coming back clean.

1. **Design sign-off** — this document. → commit.
2. **Graph skeleton** — all ~125 nodes as ids + choices + gotos + flags + ending markers, with
   one-line stub text. *Gate:* validator 0 errors (reachable, no stranding, flags declared both
   ends, endings valenced 4/4/4, 2–4 choices/node, every gated node keeps an ungated path).
3. **Prose — B1 first**, in batches, then derive **A2** (simplify) and **B2** (enrich); levelise
   every choice. *Gate:* per level, bands clean; no stub text left.
4. **Lexicon** — grow to ~250, complete in 9 languages; auto-gloss coverage checked.
5. **Native review** — 8-language pass + A2-choice clarity check. *Launch gate.*
6. **Art** — per-book shot-list, waves by act; endings bespoke; files drop in by convention at
   `images/new-city/ep-02/<id>.webp`.

Claude drafts phases 1–4 and preps 5–6; people run 5–6. Built on branch `book-02-the-room`;
merges to `main` only after the definition-of-done (playbook §5) is fully checked.
