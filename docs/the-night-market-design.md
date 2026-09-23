# The Night Market — book 2 design & build plan

A **standalone** book. It shares nothing with *The Address* except the method and the house
tone — no arc, no carried state, no shared characters, city or subject (see
[authoring-playbook.md](authoring-playbook.md) §1/§3). `state_in = []`, `arc_flags = []`.
The house voice still holds: *quiet, humane, a little uncertain — warm light in cold places*.
Here the "cold place" is not an empty city at night but the cold hour before dawn at the end
of a long night's work, and the warm light is a stall's own lantern.

Where *The Address* was one stranger crossing a cold, empty city, *The Night Market* is one
young person holding a single warm spot in a loud, crowded one. Deliberately the opposite
world: heat, steam, noise, food, people pressing in — the same learner, a wholly new subject.

---

## 1. Premise

Your aunt has run the same dumpling-and-broth stall at the night market for thirty years —
pitch 24, on the corner by the fish arch. Two days ago she scalded her hand badly. Tonight
is the last night of the season, and the **pitch fee** for keeping the spot next season is due
to the market master **by the time the lanterns go out at dawn**. Miss it and the corner she
has held for thirty years goes to whoever pays first in the morning.

So it falls to you — who can just about cook her food and has never once run the stall alone —
to work one whole night: light the burners, judge the broth, price the bowls, read the crowd,
handle the money, and take **enough by dawn** to keep pitch 24 in the family.

The trouble is not that no one comes. It is that a long market night is full of small choices
that each cost or save you a little, and a few people who would rather your money than your
custom. Chief among them is **Mr Sould, the market "fixer"** — who collects fees, settles
"trouble," and offers a tired stallholder a quick loan or a quiet word with a rival, at a price
that is never really named until it is too late. He is the night's trap, the same machine as any
scam: help that is really a hook.

**The through-line (the night's quiet pull):** every night for years your aunt has set **one
bowl aside**, uneaten, on the back shelf — "for Mr Behn," she says, and will say no more. Mr
Behn's stool at the counter has been empty for a season. *Who is he, why the saved bowl, and
why did he stop coming?* Tonight, if you keep the habit alive, he comes back — and the answer
is not dramatic but human, and it turns, as book 1 did, on whether you are the kind of person
who keeps a small kindness going when no one is watching.

**Theme:** the difference between **taking the money and keeping the name** — between a night's
takings and thirty years of trust; between being fed and being *seen* at a counter. Nobody is a
villain except the man selling shortcuts. The warmth lives in the other stallholders, a hungry
child, a returning regular, and the aunt's voice on the phone.

**Recurring faces (within this book):** **Auntie Sim** (on the phone / in memory — the stall's
keeper), **the tea woman at pitch 25** (first help, the neighbour), **Mr Sould** (the fixer, the
trap), **the kid** (a market child who runs errands for scraps — the kindness), and **Mr Behn**
(the empty stool, the mystery).

---

## 2. What "~120 passages" buys, and the rule that governs it

Same rule as the flagship: **every passage is written three times (A2/B1/B2) and glossed in
eight languages.** ~120 passages ≈ 360 authored prose units + a ~250-word book lexicon × 8.
A passage earns its place only if it adds **a real decision, a distinct beat, or texture the
reader will feel.** We hold the top of the CYOA band (~100–150) while staying shippable.

---

## 3. Act structure & passage budget

One night, dusk to dawn, in and around pitch 24.

| Act | Beat | Depth | Budget |
|---|---|---|---|
| **I — Lighting up** (dusk→first rush) | Auntie's phone instructions; opening the stall; the ingredient choice (the good supplier vs. the cheap, off one); Mr Sould's first friendly approach; the tea woman next door; the first customers and the first prices; the saved bowl on the back shelf | The money-and-quality fork (kept_quality); learning to read a customer; the fixer's soft opening; the saved-bowl habit introduced | ~30 |
| **II — The long rush** (the crowd, the night deepens) | The press of the crowd; running low on stock; a spill or a burn; a hungry child; a rival stall undercutting; rain sweeping the arcade; the fixer's pressure rising; Mr Behn's empty stool | A second temptation (cut a corner to go faster → rushed); the neighbour crisis (helped_neighbour); the hungry kid (gave_freely); the fixer's loan offered plainly (dodged/paid); the mystery deepened | ~62 |
| **III — Closing** (the lanterns lower toward dawn) | Counting the takings against the fee; the fixer's last offer; whether the saved bowl is still there; Mr Behn's return; the master's round at dawn | The count scene (hit_target); the fixer resolved; the bowl returned; the master's verdict | ~16 |
| **Endings** | see §5 | — | 12 |

**Target: ~120 passages, 12 endings.**

---

## 4. State model (the flags)

`state_in = []` — nothing carried. **Eight own flags**, each *set* at a clear moment and *read*
at a clear payoff; every gated choice keeps an ungated "otherwise" path (validator-enforced).

| Flag | Earned when | Pays off at |
|---|---|---|
| `kept_quality` | you cook with the good, costlier ingredients, not the cheap off ones | the "sold out, and proud" win; a discerning regular's return |
| `hit_target` | your takings reach the pitch fee by dawn | the win endings (you keep pitch 24) |
| `dodged_fixer` | you refuse Mr Sould's loan / "quiet word" | the clean-win gate; no debt, no strings |
| `paid_fixer` | you take Sould's loan or pay for his "help" | the debt bad ending — the fee's met but you're his now |
| `saved_a_bowl` | you keep one bowl aside for Mr Behn, as Auntie does | the secret "the last bowl" ending — he returns |
| `helped_neighbour` | you drop everything to help the tea woman (or another stall) in a crisis | the "covered, this once" neutral ending |
| `gave_freely` | you feed the hungry child who cannot pay | the "kindness fed back" neutral ending |
| `rushed` | you cut a corner — serve it half-done, short someone's change — to move faster | the "money, not the name" neutral ending |

`state_out` lists all eight (so the JSON is self-consistent for the `sets` check); it carries no
meaning to any other book. `arc_flags = []`.

---

## 5. Endings (12) — balanced 4 good / 4 neutral / 4 bad

Two are **secret** (clue/relationship-gated). Bespoke prose × 3 levels + bespoke art.

**Win (4)**
- *Sold out, and proud* — `hit_target` + `kept_quality`: honest good food, sold to the last bowl;
  the fee paid, pitch 24 kept, the name intact.
- *The last bowl* — **secret**, `saved_a_bowl`: Mr Behn comes back at dawn; the saved bowl is
  served; you learn who he is to Auntie, and something long cold is warmed. The mystery pays off.
- *On your own terms* — `hit_target` + `dodged_fixer`: you make the fee cleanly, no fixer, no debt.
- *A name, not just a night* — `kept_quality` (fell short of the full fee): you didn't quite make
  it, but you made the stall's name tonight, and the master — or a neighbour — gives you grace.

**Neutral / bittersweet (4)**
- *The money, not the name* — `rushed`: you hit the fee by cutting corners; you keep the pitch,
  but the regulars saw, and thirty years of trust is a little thinner tonight. The sharpest ending.
- *Covered, this once* — `helped_neighbour`: you fall short, but the tea woman covers your fee,
  no strings, because you stood by her. Warmth without the full win.
- *The kindness fed back* — `gave_freely`: no fee tonight, but the child you fed brings a hungry
  crew who'll come back; a start, not a save.
- *One more week* — ungated fallback: you scrape close; the master gives you till next market day.
  Not a loss, not yet.

**Lose (4)**
- *In Sould's book* — `paid_fixer`: the fee's covered tonight, but you owe the fixer now, and that
  is the worse debt. You kept the pitch and lost the ground under it.
- *Short by dawn* — ungated fallback: the takings don't reach the fee; pitch 24 is lost.
- *The pot ran dry* — ungated fallback: you ran out of stock hours before dawn (bad planning /
  cut corners) and stood at a cold empty stall while the market went on around you.
- *You couldn't hold it* — ungated fallback: the night beat you; you think about handing the
  stall back for good.

At least one clearly good and one clearly bad (validator warns otherwise). ✔

---

## 6. Levels & lexicon

- **Three levels** (A2/B1/B2), prose per level over one shared graph; validator holds each
  passage in band. **On-demand passage gist** per the flagship (French first, then the pivotal
  beats + 12 endings; others as translators arrive).
- **Book lexicon ~250 words**, base-keyed, English + 8 languages, embedded in the JSON — tilted
  to **this** subject: cooking and the stall (*broth, dumpling, steam, ladle, burner, boil, chop,
  spice, bowl, steamer*), the market (*stall, pitch, awning, lantern, crowd, stallholder, master,
  arch*), money (*fee, takings, change, price, profit, loan, owe*), night and weather. It shares
  no file with book 1; a word that recurs is re-authored to a consistent gloss.
- **The A2-choice caveat (bible §6b):** branching inference is identical across levels, so at A2
  the **choice text** must be unambiguous and low-inference. Required in the native review.
- **Native-language review is the launch gate.** Machine-drafted glosses ship to a speaker first.

**Language focus** (per level, for the classroom):
- A2 — *present continuous and imperatives; food, cooking and prices.*
- B1 — *quantifiers and comparatives; buying, selling and making change.*
- B2 — *inference and negotiation; obligation, debt and keeping a name.*

---

## 7. Visual identity (per book)

Its own world: a **warm, crowded, lantern-lit night market**, the visual opposite of *The
Address*'s cold empty streets. Declared once as `identity`; the reader skins itself to it.

- **name:** *Lantern Night* — **mood:** "A loud warm market in the dark; one stall's lantern is
  the light you keep."
- **palette:** a warm-dark set — a deep ember-brown ground and surface, warm paper-lantern
  **accent** (a red-gold that means the burner's glow, the choice `§ N`, glossed underlines, the
  progress bar), and a **jade/steam-green secondary** (the tea woman, the dawn note). Distinct
  from book 1's navy-night + cold amber. Final values in the JSON `identity` block.
- **cover.kind:** `lantern` (a stall glowing in a dark market) with `glow: true`. A new scene
  branch is added to `scripts/build_og.mjs` for it (nocturne = book 1; lantern = this book), so
  the social card is a genuinely different picture, not a recolour.
- **type:** inherited families (Fraunces / Hanken Grotesk / JetBrains Mono).
- **slug:** `the-night-market`; **hero.line** the eight-language morph sentence; **sub** the same
  learner promise.

Shipping = write its JSON (prose + lexicon + `identity` + `slug`) and commit its OG PNG
(`node scripts/build_og.mjs`). One zero-config route `/b/:slug` serves it.

---

## 8. Build phases & gates

Gate each phase on `python3 scripts/build_book.py content/episode-02.json --lexicon
content/lexicon.json` coming back clean.

1. **Design sign-off** — this document. → commit.
2. **Graph skeleton** — ~120 nodes, ids + choices + gotos + flags + endings, one-line stubs.
   *Gate:* validator 0 errors; reachable; 12 endings 4/4/4; 8 flags set+read; every gated node
   keeps an ungated path.
3. **Prose — B1 first**, then A2 (simplify), then B2 (enrich), in act batches; levelise choices.
   *Gate:* per level, bands clean; no stub text left.
4. **Lexicon** — ~250 words, complete in 9 languages; auto-gloss coverage checked.
5. **Native review** — 8-language pass + A2-choice clarity. *Launch gate.*
6. **Art** — per-book shot-list, waves by act; endings bespoke; files at
   `images/night-market/ep-02/<id>.webp` (`series` = `night-market` is the image namespace;
   `episode` = 2 is only the unshown shelf-order hint that places it after *The Address*).

Built on branch `book-02-night-market`; merges to `main` only after the definition-of-done.
