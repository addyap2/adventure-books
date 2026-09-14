#!/usr/bin/env python3
"""Validate a multi-level gamebook episode and render it.

One JSON file per episode is the single source of truth. It holds the branching graph
once and the prose once per CEFR level, so the structure can never drift between the
A2 and B2 versions of the same story — they are the same story.

Usage:
    python3 build_book.py episode-01.json --out-dir build/
    python3 build_book.py episode-01.json --mermaid-only
    python3 build_book.py episode-01.json --out-dir build/ --shuffle --seed 7
    python3 build_book.py --series content/            # cross-episode flag check

Exit codes: 0 = clean or warnings only, 1 = errors found (nothing rendered).
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import random
import re
import sys
from collections import deque

# Working envelope per CEFR level. Mirrors references/cefr-levels.md.
LEVELS = {
    "A1": {"mean_max": 8, "sent_max": 12, "para_min": 15, "para_max": 60},
    "A2": {"mean_max": 12, "sent_max": 18, "para_min": 25, "para_max": 90},
    "B1": {"mean_max": 16, "sent_max": 25, "para_min": 35, "para_max": 130},
    "B2": {"mean_max": 22, "sent_max": 35, "para_min": 50, "para_max": 190},
    "C1": {"mean_max": 99, "sent_max": 99, "para_min": 70, "para_max": 260},
}
VOCAB_CHECK_LEVELS = ("A1", "A2", "B1")

# Translation languages, matching grammatica.antonyaddy.com so a learner meets the
# same eight languages across the platform.
LANGS = {
    "fr": "French", "es": "Spanish", "pt": "Portuguese", "it": "Italian",
    "de": "German", "ru": "Russian", "ar": "Arabic", "zh": "Mandarin Chinese",
}
RTL_LANGS = {"ar"}

HERE = os.path.dirname(os.path.abspath(__file__))
WORDLIST = os.path.join(HERE, "wordlist_core.txt")


def load_core_words() -> set:
    try:
        with open(WORDLIST, encoding="utf-8") as fh:
            return {w.strip().lower() for w in fh if w.strip()}
    except OSError:
        return set()


def in_core(word: str, core: set) -> bool:
    """Match against the core list allowing for regular inflection.

    The list holds base forms; a learner who knows `walk` is not tripped up by
    `walked`, so flagging inflected forms would drown the useful signal in noise.
    """
    if word in core:
        return True
    for suf, repl in (("s", ""), ("es", ""), ("ies", "y"), ("ed", ""), ("ed", "e"),
                      ("ied", "y"), ("ing", ""), ("ing", "e"), ("er", ""), ("er", "e"),
                      ("est", ""), ("ly", ""), ("'s", "")):
        if word.endswith(suf) and len(word) - len(suf) >= 2:
            c = word[: -len(suf)] + repl
            if c in core:
                return True
            if len(c) > 3 and c[-1] == c[-2] and c[:-1] in core:  # stopped -> stop
                return True
    return False


_SUFFIX = (("s", ""), ("es", ""), ("ies", "y"), ("ed", ""), ("ed", "e"), ("ied", "y"),
           ("ing", ""), ("ing", "e"), ("er", ""), ("er", "e"), ("est", ""), ("ly", ""),
           ("ily", "y"), ("ally", "al"), ("ably", "able"), ("ibly", "ible"), ("'s", ""))


def resolve(word: str, keys: set):
    """Return the lexicon key a word maps to (base form or inflection), or None.

    Mirrors the reader's auto-gloss matcher so the validator's view of what is glossed
    equals what a reader can actually tap.
    """
    w = word.lower()
    if w in keys:
        return w
    for suf, repl in _SUFFIX:
        if w.endswith(suf) and len(w) - len(suf) >= 2:
            c = w[: -len(suf)] + repl
            if c in keys:
                return c
            if len(c) > 3 and c[-1] == c[-2] and c[:-1] in keys:  # stopped -> stop
                return c[:-1]
    return None


def sentences(text: str):
    return [p for p in re.split(r"(?<=[.!?])\s+", (text or "").strip()) if p.strip()]


def words(text: str):
    return re.findall(r"[A-Za-z']+", text or "")


class Report:
    def __init__(self):
        self.errors, self.warnings = [], []

    def error(self, m): self.errors.append(m)

    def warn(self, m): self.warnings.append(m)


def book_lexicon(book, shared=None):
    """This book's effective lexicon: a shared base plus the book's own chosen words.

    The book is the unit a learner sits down with, so each carries its own chosen
    lexicon; a small shared base (words common to the whole series) is layered under it.
    """
    def entries_of(obj):
        if not isinstance(obj, dict):
            return {}
        src = obj.get("entries") if "entries" in obj else obj
        return {k.lower(): v for k, v in src.items()
                if not k.startswith("_") and isinstance(v, dict)}

    lex = {}
    lex.update(entries_of(shared))
    lex.update(entries_of(book.get("lexicon")))
    return lex


def appearing_words(node, level, keys):
    """Lexicon keys whose words actually appear in this node's text, in reading order."""
    out, seen = [], set()
    for w in words(per_level(node.get("text"), level) or ""):
        base = resolve(w, keys)
        if base and base not in seen:
            seen.add(base)
            out.append(base)
    return out


def validate_lexicon(lexicon, rep):
    """Every lexicon entry must be complete in English and all eight languages.

    Glossing is automatic now — any lexicon word is tappable wherever it appears — so the
    only invariant to guard is that no entry leaves a language blank. A learner who taps
    a word and gets nothing is worse than one who cannot tap it. Returns the key set.
    """
    for w in sorted(lexicon):
        entry = lexicon[w] or {}
        gaps = [c for c in ("en", *LANGS) if not str(entry.get(c, "")).strip()]
        if gaps:
            rep.error(f"Lexicon entry {w!r} is missing: {', '.join(gaps)}.")
    return set(lexicon)


def per_level(value, level, fallback_ok=True):
    """Read a field that may be a dict keyed by level, or a plain value."""
    if isinstance(value, dict):
        return value.get(level) if not fallback_ok else value.get(level)
    return value


# ---------------------------------------------------------------- validation


def validate_structure(book: dict, rep: Report):
    nodes = book.get("nodes")
    if not isinstance(nodes, list) or not nodes:
        rep.error("`nodes` is missing or empty.")
        return {}

    by_id = {}
    for i, n in enumerate(nodes):
        nid = n.get("id")
        if not isinstance(nid, int) or nid < 1:
            rep.error(f"Node #{i} has a missing or non-positive integer id: {nid!r}")
            continue
        if nid in by_id:
            rep.error(f"Duplicate paragraph number {nid}.")
            continue
        by_id[nid] = n

    start = book.get("start", 1)
    if start not in by_id:
        rep.error(f"start = {start} but there is no paragraph {start}.")

    state_in = set(book.get("state_in") or [])
    state_out = set(book.get("state_out") or [])

    for nid, n in sorted(by_id.items()):
        choices = n.get("choices") or []
        ending = n.get("ending")

        if ending is not None:
            if ending not in ("good", "bad", "neutral"):
                rep.warn(f"§{nid} ending is {ending!r}; expected good, bad or neutral.")
            if choices:
                rep.error(f"§{nid} is an ending but still offers choices.")
        else:
            if not choices:
                rep.error(f"§{nid} has no choices and no `ending` — the reader is stranded.")
            elif not (2 <= len(choices) <= 4):
                rep.warn(f"§{nid} offers {len(choices)} choices; 2–4 reads best.")

        targets, ungated = [], 0
        for j, c in enumerate(choices):
            goto = c.get("goto")
            if goto not in by_id:
                rep.error(f"§{nid} choice {j + 1} points at §{goto}, which does not exist.")
            else:
                targets.append(goto)
            if goto == nid:
                rep.warn(f"§{nid} choice {j + 1} points at itself.")

            req = c.get("requires") or []
            if isinstance(req, str):
                req = [req]
            if not req:
                ungated += 1
            for f in req:
                # A gate may read a flag carried in from an earlier episode, or one set
                # earlier in this one — the delayed consequence inside a single episode
                # is the same mechanism at a shorter range.
                if f not in state_in and f not in state_out:
                    rep.error(
                        f"§{nid} choice {j + 1} requires flag {f!r}, which is declared "
                        f"in neither `state_in` nor `state_out`. Declare it, or the "
                        f"reader can never see this choice."
                    )
            sets = c.get("sets") or []
            if isinstance(sets, str):
                sets = [sets]
            for f in sets:
                if f not in state_out:
                    rep.error(
                        f"§{nid} choice {j + 1} sets flag {f!r}, which is not declared "
                        f"in `state_out`. Later episodes will never know to look for it."
                    )

        if choices and ungated == 0:
            rep.error(
                f"§{nid}: every choice is gated behind a flag. A reader without those "
                f"flags reaches a paragraph with nothing to do. Leave one choice ungated "
                f"as the 'otherwise' path."
            )

        if len(targets) > 1 and len(set(targets)) == 1:
            rep.error(
                f"§{nid}: every choice leads to §{targets[0]}. The reader is deciding "
                f"nothing — send at least one branch somewhere different."
            )

    # Reachability, ignoring flag gates (the most generous reading of the graph)
    if start in by_id:
        seen, depth, q = {start}, {start: 0}, deque([start])
        while q:
            cur = q.popleft()
            for c in by_id[cur].get("choices") or []:
                t = c.get("goto")
                if t in by_id and t not in seen:
                    seen.add(t)
                    depth[t] = depth[cur] + 1
                    q.append(t)
        orphans = sorted(set(by_id) - seen)
        if orphans:
            rep.error("Unreachable from the start: " + ", ".join(f"§{o}" for o in orphans)
                      + ". Either link them in or delete them.")
        for nid, n in sorted(by_id.items()):
            if n.get("ending") and depth.get(nid, 99) < 3:
                rep.warn(f"§{nid} is an ending only {depth.get(nid)} step(s) from the "
                         f"start — very abrupt unless it is a deliberate dead end.")

    endings = [n for n in by_id.values() if n.get("ending")]
    if len(endings) < 3:
        rep.warn(f"Only {len(endings)} ending(s). Three to five gives replay value, and "
                 f"the reread is where the language lands.")
    kinds = {n.get("ending") for n in endings}
    if endings and not ("good" in kinds and "bad" in kinds):
        rep.warn("Endings are all the same valence. At least one clearly good and one "
                 "clearly bad is what makes the choices feel consequential.")
    return by_id


def validate_level(book: dict, by_id: dict, level: str, rep: Report, core: set,
                   glossed: set = frozenset()):
    lim = LEVELS.get(level)
    if lim is None:
        rep.warn(f"Unknown level {level!r}; skipping its language checks.")
        return {}
    stats, flagged = {}, {}

    for nid, n in sorted(by_id.items()):
        text = per_level(n.get("text"), level)
        if not text or not text.strip():
            rep.error(f"§{nid} has no {level} text. Every level needs every paragraph, "
                      f"or a reader at {level} hits a hole mid-story.")
            continue
        for j, c in enumerate(n.get("choices") or []):
            ct = per_level(c.get("text"), level)
            if not ct or not ct.strip():
                rep.error(f"§{nid} choice {j + 1} has no {level} text.")
            elif len(words(ct)) > lim["sent_max"]:
                rep.warn(f"[{level}] §{nid} choice {j + 1} is {len(words(ct))} words, "
                         f"above the ceiling of {lim['sent_max']}. Choices are written "
                         f"last and drift above level most often.")

        ws, ss = words(text), sentences(text)
        if not ss:
            continue
        L = [len(words(s)) for s in ss]
        mean, longest = sum(L) / len(L), max(L)
        stats[nid] = {"words": len(ws), "sentences": len(ss),
                      "mean": round(mean, 1), "longest": longest}

        if mean > lim["mean_max"]:
            rep.warn(f"[{level}] §{nid}: mean sentence {mean:.1f} words, above the "
                     f"working average of {lim['mean_max']}.")
        if longest > lim["sent_max"]:
            rep.warn(f"[{level}] §{nid}: longest sentence {longest} words, above the "
                     f"ceiling of {lim['sent_max']}. Split it.")
        if len(ws) > lim["para_max"]:
            rep.warn(f"[{level}] §{nid}: {len(ws)} words, above the paragraph max of "
                     f"{lim['para_max']}. One paragraph should be one beat.")
        if len(ws) < lim["para_min"] and not n.get("ending"):
            rep.warn(f"[{level}] §{nid}: only {len(ws)} words — thin for {level}.")

        if core and level in VOCAB_CHECK_LEVELS:
            for s in ss:
                toks = words(s)
                for k, w in enumerate(toks):
                    if k > 0 and w[:1].isupper():
                        continue  # mid-sentence capital: almost certainly a name
                    lw = w.lower()
                    if len(lw) <= 3 or resolve(lw, glossed) or in_core(lw, core):
                        continue
                    flagged.setdefault(lw, []).append(nid)

    if flagged:
        top = sorted(flagged.items(), key=lambda kv: (-len(kv[1]), kv[0]))[:20]
        rep.warn(f"[{level}] hard words not in the lexicon (advisory — add them so a "
                 f"reader can tap them, or leave them as worth the effort): "
                 + ", ".join(f"{w} (§{v[0]})" for w, v in top))
    return stats


# ---------------------------------------------------------------- rendering


def mermaid(book: dict) -> str:
    lines = ["```mermaid", "graph TD"]
    for n in sorted(book["nodes"], key=lambda x: x["id"]):
        nid = n["id"]
        if n.get("ending"):
            lines.append(f'  N{nid}["{nid}: {n["ending"].upper()} END"]')
        for c in n.get("choices") or []:
            gate = ""
            req = c.get("requires") or []
            if req:
                gate = "|" + "+".join(req if isinstance(req, list) else [req]) + "|"
            lines.append(f"  N{nid} -->{gate} N{c.get('goto')}")
    lines.append("```")
    return "\n".join(lines)


def render(book: dict, level: str, lexicon=None, gloss_lang=None) -> str:
    nodes = sorted(book["nodes"], key=lambda n: n["id"])
    endings = [n for n in nodes if n.get("ending")]
    title = book.get("title", "Untitled")
    ep = book.get("episode")
    head = f"# {title}" + (f" — Episode {ep}" if ep else "")
    focus = per_level(book.get("language_focus"), level) or []
    bits = [f"**Level:** {level}"]
    if focus:
        bits.append("**Language focus:** " + ", ".join(focus))
    bits.append(f"**{len(nodes)} paragraphs, {len(endings)} endings**")

    out = [head, "", " · ".join(bits), "",
           "> Start at paragraph 1. At the end of each paragraph, choose what to do "
           "and go to the paragraph number next to your choice.", "", "---", ""]
    for n in nodes:
        out += [f"### {n['id']}", "", (per_level(n.get('text'), level) or "").strip(), ""]
        gl = appearing_words(n, level, set(lexicon or {}))
        if gl:
            for w in gl:
                entry = (lexicon or {}).get(w, {})
                en = entry.get("en") or "(no gloss yet)"
                line = f"*{w}* — {en}"
                if gloss_lang and entry.get(gloss_lang):
                    line += f"  ·  **{gloss_lang}:** {entry[gloss_lang]}"
                out.append(line + "  ")
            out.append("")
        if n.get("ending"):
            out += ["**— THE END —**", ""]
        for c in n.get("choices") or []:
            req = c.get("requires") or []
            req = [req] if isinstance(req, str) else req
            gate = f" *(only if {', '.join(req)})*" if req else ""
            out.append(f"- {per_level(c.get('text'), level)}{gate} "
                       f"→ **go to {c.get('goto')}**")
        if n.get("choices"):
            out.append("")
    out += ["---", "", "## Story map", "", mermaid(book), ""]
    return "\n".join(out)


def shuffle_ids(book: dict, seed: int):
    ids = sorted(n["id"] for n in book["nodes"])
    start = book.get("start", 1)
    rng = random.Random(seed)
    pool = list(range(2, len(ids) + 1))
    rng.shuffle(pool)
    mapping = {start: 1}
    for old, new in zip([i for i in ids if i != start], pool):
        mapping[old] = new
    for n in book["nodes"]:
        n["id"] = mapping[n["id"]]
        for c in n.get("choices") or []:
            if c.get("goto") in mapping:
                c["goto"] = mapping[c["goto"]]
    book["start"] = 1
    book["nodes"].sort(key=lambda n: n["id"])
    return mapping


# ---------------------------------------------------------------- series check


def check_series(folder: str, lexicon_path=None) -> int:
    files = sorted(glob.glob(os.path.join(folder, "*.json")))
    eps, problems = [], []
    for f in files:
        try:
            b = json.load(open(f, encoding="utf-8"))
        except Exception as e:
            problems.append(f"{os.path.basename(f)}: unreadable ({e})")
            continue
        if "nodes" not in b:
            continue
        eps.append((b.get("episode", 0), os.path.basename(f), b))
    eps.sort()
    available = set()
    print(f"{len(eps)} episode(s) in {folder}\n")
    for num, name, b in eps:
        need = set(b.get("state_in") or [])
        gives = set(b.get("state_out") or [])
        missing = need - available
        if missing:
            problems.append(
                f"Episode {num} ({name}) reads flags no earlier episode sets: "
                + ", ".join(sorted(missing))
            )
        levels = b.get("levels") or []
        print(f"  ep {num:>2}  {name:<24} levels={','.join(levels) or '?':<12} "
              f"nodes={len(b.get('nodes', [])):<4} in={sorted(need) or '-'} "
              f"out={sorted(gives) or '-'}")
        available |= gives
    dead = set()
    for num, name, b in eps:
        dead |= set(b.get("state_out") or [])
    used = set()
    for num, name, b in eps:
        used |= set(b.get("state_in") or [])
        for n in b.get("nodes", []):          # gates inside the episode count as reads
            for c in n.get("choices") or []:
                r = c.get("requires") or []
                used |= {r} if isinstance(r, str) else set(r)
    never_read = dead - used
    print()

    shared = json.load(open(lexicon_path, encoding="utf-8")) if lexicon_path else None
    per_lang = {}
    total = 0
    for _, name, b in eps:
        lex = book_lexicon(b, shared)
        total += len(lex)
        for w in sorted(lex):
            for c in [c for c in ("en", *LANGS) if not str((lex[w] or {}).get(c, "")).strip()]:
                per_lang.setdefault(c, []).append(f"{w} ({name})")
    print(f"Lexicon: {total} entr{'y' if total == 1 else 'ies'} across "
          f"{len(eps)} book(s) (each book's own + shared base).")
    if per_lang:
        for c, ws in sorted(per_lang.items()):
            problems.append(f"{len(ws)} entr{'y' if len(ws) == 1 else 'ies'} missing "
                            f"{c}: {', '.join(ws[:8])}" + (" …" if len(ws) > 8 else ""))
    else:
        print("  all entries complete in all languages.")
    print()

    for p in problems:
        print(f"ERROR   {p}")
    if never_read:
        print("warning flags set but never read by any episode: "
              + ", ".join(sorted(never_read)))
    print(f"\n{len(problems)} error(s).")
    return 1 if problems else 0


# ---------------------------------------------------------------- main


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("book", nargs="?", help="path to an episode .json")
    ap.add_argument("--series", help="folder of episode files: check flags across them")
    ap.add_argument("--out-dir", help="write one Markdown file per level here")
    ap.add_argument("--mermaid-only", action="store_true")
    ap.add_argument("--shuffle", action="store_true",
                    help="reassign paragraph numbers pseudo-randomly (do this last)")
    ap.add_argument("--seed", type=int, default=1234)
    ap.add_argument("--write-json", help="write the (possibly shuffled) JSON here")
    ap.add_argument("--lexicon", help="shared lexicon.json for the series")
    ap.add_argument("--gloss-lang", choices=sorted(LANGS),
                    help="also show this language's translation in the rendered preview")
    args = ap.parse_args()

    if args.series:
        return check_series(args.series, args.lexicon)
    if not args.book:
        ap.error("give an episode .json, or --series FOLDER")

    with open(args.book, encoding="utf-8") as fh:
        book = json.load(fh)

    if args.mermaid_only:
        print(mermaid(book))
        return 0

    rep = Report()
    by_id = validate_structure(book, rep)
    levels = book.get("levels") or ([book["level"]] if book.get("level") else ["A2"])
    core = load_core_words()

    # effective lexicon = optional shared base (--lexicon) + this book's own chosen words
    shared = json.load(open(args.lexicon, encoding="utf-8")) if args.lexicon else None
    lexicon = book_lexicon(book, shared)
    glossed = validate_lexicon(lexicon, rep) if lexicon else set()
    if lexicon:
        covered = sum(1 for w in glossed)
        print(f"note    {covered} lexicon words tappable in this book "
              f"({len(book.get('lexicon', {}).get('entries', {}))} its own).")

    stats = ({lv: validate_level(book, by_id, lv, rep, core, glossed) for lv in levels}
             if by_id else {})

    for e in rep.errors:
        print(f"ERROR   {e}")
    for w in rep.warnings:
        print(f"warning {w}")

    for lv in levels:
        if not stats.get(lv):
            continue
        print(f"\n{lv} paragraphs")
        print(f"{'§':>5}  {'words':>5}  {'sents':>5}  {'mean':>5}  {'longest':>7}  role")
        for nid, s in sorted(stats[lv].items()):
            n = by_id[nid]
            role = f"{n['ending']} ending" if n.get("ending") \
                else f"{len(n.get('choices') or [])} choices"
            print(f"{nid:>5}  {s['words']:>5}  {s['sentences']:>5}  {s['mean']:>5}  "
                  f"{s['longest']:>7}  {role}")

    print(f"\n{len(rep.errors)} error(s), {len(rep.warnings)} warning(s).")
    if rep.errors:
        print("Nothing rendered — fix the errors above and run again.")
        return 1

    if args.shuffle:
        mapping = shuffle_ids(book, args.seed)
        print("Renumbered (old → new): "
              + ", ".join(f"{o}→{n}" for o, n in sorted(mapping.items())))

    if args.write_json:
        json.dump(book, open(args.write_json, "w", encoding="utf-8"),
                  indent=2, ensure_ascii=False)
        print(f"Wrote {args.write_json}")

    if args.out_dir:
        os.makedirs(args.out_dir, exist_ok=True)
        stem = os.path.splitext(os.path.basename(args.book))[0]
        for lv in levels:
            p = os.path.join(args.out_dir, f"{stem}.{lv}.md")
            open(p, "w", encoding="utf-8").write(
                render(book, lv, lexicon, args.gloss_lang))
            print(f"Wrote {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
