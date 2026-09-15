# The Address — flagship design & build plan

This is the design that turns *The Address* from a 40-passage episode into the **~150-passage
flagship** that every future book in the series will be modelled on. It is a spec to approve
and build against — story first, then structure, then prose, then languages, then art.

The existing 40 passages are the **spine**. We are not rewriting them; we are deepening the
world around them. The tone is fixed and non-negotiable: *quiet, atmospheric, a little
uncertain — not frightening. Warm light in cold places.* A learner should want to keep going
because they need to know what happens, and pick correctly because they understood the paragraph.

---

## 1. Premise (unchanged)

You arrive alone, at night, in an unfamiliar port city, carrying one letter: a job with
**Kessler and Rowe, 14 Rosewater Street, Tuesday at nine**. The letter is two years out of
date — the firm moved to **3 Mill Quay**, by the river. Between the midnight station and the
nine-o'clock interview lies one night in a city that does not know you. Some people help.
One place — the **"Work For Everyone" agency** — is a trap. Whether you arrive, and *how*,
depends on what you notice and who you trust.

**Theme:** being a stranger; the difference between being *processed* and being *seen*;
persistence rewarded. Nobody is a villain except the people selling false hope.

**The through-line (added):** *why is the letter two years out of date — who in that office is
still posting the old address?* This quiet mystery, already latent in the spine (§35: "Someone
in this office is still sending out the old letters"), becomes the night's forward pull. It
gives the reader a *reason to talk to people* all night, and it pays off thematically: the same
carelessness that misdirected you is the first thing you are hired to fix (§36). Atmosphere sets
the mood; this thread supplies propulsion across 150 passages.

**Recurring faces (added):** warmth must live in people, because the city is deliberately
faceless. Four anchors recur so the night has relationships, not just locations: **the kiosk
woman** (first help), **the number-16 family** (the father in the gown; his daughter by
daylight), **the night-shift man** at the station, and **Ms Rowe** herself. Two of them reappear
across acts so a face you were kind (or curt) to earlier answers for it later.

---

## 2. What "150 passages" buys, and the rule that governs it

Genre benchmark: a full *livre dont vous êtes le héros* (Fighting Fantasy) is ~400 numbered
sections; Choose Your Own Adventure is ~100–150. At ~150 we sit at the top of the CYOA band —
a genuinely full book — while staying inside the one rule that matters here:

> **Every passage is written three times (A2/B1/B2) and glossed in eight languages.**
> 150 passages ≈ **450 authored prose units + a ~250-word book lexicon × 8 languages.**

So every new passage must justify that triple cost. The test for adding a passage:
**does it add a real decision, a distinct beat, or texture the reader will feel?** If it only
pads the route between two decisions, it does not go in.

---

## 3. Act structure & passage budget

Three acts, one night and one morning, plus an ending fan. Current passage ids in **bold**.

| Act | Beat | New depth to add | Budget |
|---|---|---|---|
| **I — Arrival** (dusk→midnight) | The station **(1)**, information desk **(2)**, the taxi rank / bus **(3,4,6)**, the walk & the kiosk woman **(5,9)**, sleeping the first choices | The other arrivals on the platform; what's in your bag (a small inventory beat); the night-shift faces; the first sense the letter is wrong | ~30 (of which 9 exist) |
| **II — The Night** (midnight→dawn) | Rosewater St **(7,11,18)**, number 16 **(12,26)**, the river at night **(19,28)**, the station bench / hotel **(13,16)**, the **agency scam thread (10,24,32,33,39)**, the Blue Kettle café **(9,15,29)** | A second helper and a second false lead so the map has real dead ends; the scam given room to tempt (a queue of hopefuls, a plausible pitch); a quiet night-watchman or fellow traveller who gives the river clue | ~65 (of which ~19 exist) |
| **III — The Morning** (dawn→09:00+) | Mill Quay **(23,25,31)**, reception **(30)**, meeting Rowe on the step **(27)**, the interview itself **(35,36,37)** | The interview as a *real scene* with 2–3 sub-decisions (what you say about last night, whether you mention the agency, an honesty vs polish fork); the walk along the waking quay | ~40 (of which ~9 exist) |
| **Endings** | see §5 | expand from 5 → 12 | ~12 |

Target: **~150 passages, 12 endings.**

---

## 4. State model (the flags)

Today: `has_card`, `knows_name`. A 150-passage graph needs more state for branches to *matter* —
but the engine stores flags as a simple set, and the validator insists every gated choice keeps
an ungated "otherwise" path, so we stay disciplined. **Eight flags, no more**, each earned at a
clear moment and read at a clear payoff:

| Flag | Earned when | Pays off at |
|---|---|---|
| `knows_river` | anyone tells you they moved to the river | shortcut past dead night-searches |
| `has_card` | you photograph the café card (**15**) | the `has_card` express route (**17→25**) |
| `knows_name` | you read the *R. ROWE* luggage label (**31**) | the secret step-greeting ending (**38**) |
| `dodged_scam` | you refuse the agency (**33**) | best ending gate; a lighter, richer arrival |
| `paid_scam` | you pay the agency (**32**) | broke arc; the locked-office bad end (**39**) |
| `rested` | you take the hotel room / sleep well (**16**) | interview poise; an extra dialogue option |
| `rough_night` | you sleep on the bench / walk all night (**13,14,22**) | exhaustion beats; a harder, still-winnable path |
| `told_truth` | you tell Rowe the whole night (**36**) | the warmest ending; carries into the arc |

`state_out` (carried into episode 2): `dodged_scam`, `told_truth`, `knows_name` — who you
became on your first night follows you into the city.

**Discipline:** every flag-gated choice is accompanied by an ungated one; no paragraph can be
reached in a state that offers nothing to do. The validator enforces this on every push.

**Every flag must earn its keep (template rule, validator-enforced):** a flag has to be *set*
somewhere **and** *read* (gate a choice) somewhere — a flag set but never read is dead weight.
The one exception is an **arc-carrier**: a flag whose payoff is in a *later* book (read via that
book's `state_in`), listed in the episode's `arc_flags` field, which the validator skips. It
also errors if a choice `requires` a flag that nothing sets and no earlier episode carries in
(a gate no reader can open). In "The Address": `knows_river` gates a shortcut to the river
(§8, §14) and `rough_night` gates the tired-out interview option (§120) and the give-up ending
(§22→§147); `arc_flags` = `dodged_scam, told_truth, knows_name, paid_scam`.

---

## 5. Endings (12)

Replay is where the language lands, so endings are the reward and get the best writing and art.
Twelve is the sweet spot: enough that each meaningful state-combination lands its own ending,
few enough that each earns bespoke prose × 3 levels + bespoke art. Hard cap ~15.

**Win (4)**
- *Hired, told the truth* (**36**, exists) — the warm one; sets `told_truth`, carries into the arc.
- *The step-greeting* secret end (**38**, exists) — gated `knows_name`.
- *Hired on merit* (**new**) — a clean interview, no story told; competent, a little cooler.
- *The best night* (**new**, secret) — arrived `rested` **and** `dodged_scam` **and** `knows_name`.

**Neutral / bittersweet (4)**
- *Spring work* (**37**, exists) — no job now, but real paper, a real "call me then".
- *Remembered* (**new**) — no job, but your name is known and you are in the city.
- *Processed, not seen* (**new**) — every shortcut taken, you *get* the job, and it feels like
  nothing. A technical win that reads as a loss — the sharpest ending in the book.
- *The kindness returned* (**new**) — no job, but a face you helped in the night helps you back;
  you have somewhere to stay. Warmth without winning.

**Lose (4)**
- *The dead phone number* (**39**, exists) — gated `paid_scam`; broke, conned.
- *The two-o'clock train home* (**40**, exists) — you give up and leave.
- *Too late* (**new**) — you reach Mill Quay at 09:20 to a closed diary and a polite no.
- *The bench at dawn* (**new**) — a `rough_night` that never recovers; you never reach the interview.

At least one clearly good and one clearly bad (validator warns otherwise). The two secret ends
reward readers who both *noticed* (clues) and *chose well* (dodged the scam) — the whole
pedagogy: understanding the paragraph changes the outcome.

---

## 6. Levels & lexicon

- **Three levels** as now (A2/B1/B2), same prose-per-level model; validator holds each passage
  inside its CEFR band (sentence length, paragraph length).
- **Two glossing tiers** so a learner can tap *any* word, not only rare ones:
  - **Featured (curated) lexicon** — the ~250 chosen story words, keyed by base form, with an
    English definition + native-reviewed translations. Dotted in the accent; rich gloss card.
  - **Coverage dictionary** — the book's high-frequency *everyday* words (`content/dict/<lang>.json`,
    lazy-loaded per language, no back end), so common vocabulary is tappable too. Faint underline;
    quick translation, tagged "dictionary". Built by frequency to **~500 words** (the hold point):
    that lifts tappable words/passage from ~1–3 to **~16–26** and covers ~54% of all content tokens —
    i.e. nearly every *frequent* word. Beyond ~500 is a long tail of rare words + proper nouns with
    fast-diminishing per-passage value and rising translation risk, so we stop hand-adding there.
    For true tail-completeness later, bundle an **open dictionary dataset** (Wiktionary/Kaikki-derived)
    as a build step rather than typing more batches.
  Curated is authoritative; coverage is quick best-effort and still flows through the review sheets.
  - **Word depth is deliberately quiet:** only curated words are underlined (dotted); everyday
    coverage words are tappable but unmarked, so per-word help never crowds the reading.
- **On-demand passage gist** (`content/gist/<lang>.json`) — because per-word glosses lose context
  (idioms, sense), each *pivotal or dense* passage carries a 1–2 sentence **meaning in the reader's
  language**, revealed only by a "See the meaning" button ("where needed", never by default, so
  English stays the thing being read). **French now covers all 123 passages**; es/it/de/pt cover the
  pivotal beats + 12 endings (26); ru/ar/zh await native translators. The button simply doesn't
  appear where a gist is missing, so partial-language coverage degrades gracefully.
- **Native-language review is the launch gate.** Machine-drafted glosses in 8 languages ship to
  a speaker's check first — a wrong gloss the learner cannot detect is worse than none. This is
  the one hard gate between "done" and "launched", and it is what makes the flagship trustworthy.

### 6a. Why three levels (A2/B1/B2), and no more

The set is deliberate, and it is the standard for every book in the series:

- **It matches the audience — who are also the protagonist.** The reader is a new arrival looking
  for work in a system that does not see them; that is exactly who elementary-to-intermediate
  learners often are. A2 as the floor fits them; B2 as the ceiling serves the classroom's stronger
  readers. The band is aimed where the learners actually sit.
- **It delivers the core promise cleanly.** "A mixed-level class reads the same story and discusses
  it together" works best across a contiguous A2 → B1 → B2 span — one band apart each, no gaps.
- **Three respects the 3× cost.** Every level is a full prose rewrite plus a gloss pass. For a
  series of 10–15 books, a fourth level is +33% of authoring on every book, forever.

**Not A1, not C1, by default.** A1 fights the format — a near-beginner cannot hold the multi-clause
paragraph the genre's "understand it to choose correctly" mechanic depends on; A2 is the sensible
floor. C1 is diminishing returns — B2 is already sophisticated and this realist subject has a
natural vocabulary ceiling, so C1 readers read B2 comfortably. The validator already defines A1 and
C1 bands, so a specific market can be served later **without re-architecting** — the extensibility
is there; we simply do not pay for it now.

### 6b. The caveat: CEFR governs the language, not the puzzle

CEFR bands make the *sentences* level-appropriate, but the branching graph, the flags, and — above
all — **the inference needed to pick the right choice are identical across all three levels** (same
graph, same decisions). So the *cognitive* demand (reading a scam correctly, noticing the letters
matter) is constant while the *language* gets easier. A true A2 reader can meet words they can read
but reasoning that runs ahead of them.

**Design rule that follows from this:** get the **A2 *choices*, not only the A2 prose, right.** At
A2 the choice text must be unambiguous and low-inference, so the difficulty the learner meets is
language — never a logic puzzle they cannot yet read their way through. **This is a required check
in the pedagogy/native review** (see §6, launch gate): review each A2 choice for clarity and single,
obvious meaning, independently of whether the prose passes its band.

---

## 7. Art (for the visual team)

The existing [art brief](art-brief.md) already specs format, palette, naming and direction.
For a 150-passage book, illustrate in **waves by act**, not all at once:

- **Wave 1 (lock the look):** the 9 priority beats already listed in the brief + the cover.
  Agree the style on these, freeze it, then hold it.
- **Wave 2–4:** one image per *distinct location* (station, bus, Rosewater St, number 16, the
  river at night, the café, the station bench, the agency, Mill Quay, reception) rather than one
  per passage — passages that share a location share art. ~25–35 images total, not 150.
- Endings get bespoke images (they are what readers replay to reach).

Drop files as `images/new-city/ep-01/<paragraph-id>.webp`; they appear automatically, no code
change. Partial delivery looks intentional (clean placeholders until then).

---

## 8. Build phases & review gates

Each phase ends at a gate that must pass before the next begins. This is what keeps a 150-node
book *right*.

1. **Design sign-off** — you approve this document (story, acts, endings, state model).
2. **Graph skeleton** — all ~150 nodes as ids + choices + gotos + flags + ending markers, with
   one-line stub text per node. **Gate:** validator passes (reachable, no stranding, flags
   declared, endings valenced, no all-same-target choices). We prove the *machine* before writing
   a word of real prose.
3. **Prose — B1 first**, in batches of ~25 passages, then derive A2 (simplify) and B2 (enrich).
   **Gate:** validator's CEFR bands clean per batch.
4. **Lexicon** — expand to ~250 words as prose lands; auto-gloss coverage checked by the validator.
5. **Native review** — the 8-language pass. **Launch gate.**
6. **Art** — waves 1–4 from the visual team.

I (Claude) draft the graph and all three prose levels and the lexicon; you steer story and taste
at each gate; native speakers verify language; your team illustrates. This is **multi-session
work by design** — the gates are the point.

---

## 9. This book as the template

Everything above — the act discipline, the eight-flag ceiling, the ending taxonomy, the
per-book lexicon + auto-gloss, the phase gates, the validator-as-CI, the art waves — is the
**pattern every future book copies**. Book 2 is "episode 2 of the arc": it opens with
`state_in` = { `dodged_scam`, `told_truth`, `knows_name` } and continues the same person's life
in the same city. Get this one right and the next one is a fill-in-the-shape.
