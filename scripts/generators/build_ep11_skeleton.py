#!/usr/bin/env python3
"""Phase 2: build Moving Day (episode-11) graph skeleton from the shared topology
(episode-10, The Interview): same ids/edges/flag positions/ending valences, with
Moving Day's identity, flag names, and stub prose. Phase 3 writes real prose.
Run: python3 scripts/generators/build_ep11_skeleton.py"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(ROOT, "content", "episode-10.json")
OUT = os.path.join(ROOT, "content", "episode-11.json")

FLAGMAP = {
    "ready": "moved_in",
    "dodged_reese": "dodged_bray",
    "paid_reese": "paid_bray",
    "faced_maya": "welcomed_cass",
    "rallied_room": "rallied_block",
    "shared_notes": "shared_load",
    "jumped_queue": "overloaded",
    # helped_stranger unchanged
}
def rf(f): return FLAGMAP.get(f, f)

IDENTITY = {
    "name": "Home by Dark",
    "mood": "The last day in the old place and the first in the new; boxes, bare rooms, and a short autumn afternoon to get your mum home before dark.",
    "palette": {
        "ground": "#14110D", "surface": "#201A14", "ink": "#F2ECE2",
        "muted": "#9C9286", "line": "#322820",
        "accent": "#CE7A4A", "accentHot": "#E9A05F", "secondary": "#88A0B8"
    },
    "cover": {
        "kind": "moving", "glow": True, "focal": "52% 54%",
        "alt": "A small removal van at the kerb at dusk, its back open and boxes on the wet pavement, with a warm-lit doorway and a figure carrying a box toward it."
    },
    "type": {"display": "Fraunces", "ui": "Hanken Grotesk", "mono": "JetBrains Mono"},
    "hero": {
        "line": {
            "en": "You're moving your mum into a new place today, and the light is going. Get her home before dark — the honest way, with whoever will carry it with you.",
            "fr": "Aujourd'hui, tu installes ta mère dans un nouveau logement, et le jour baisse. Ramène-la chez elle avant la nuit — honnêtement, avec ceux qui voudront bien porter avec toi.",
            "es": "Hoy trasladas a tu madre a un piso nuevo, y la luz se va. Llévala a casa antes de que anochezca, de forma honrada, con quien quiera cargar contigo.",
            "it": "Oggi trasferisci tua madre in una casa nuova, e la luce se ne va. Portala a casa prima del buio, in modo onesto, con chi vorrà portare il peso con te.",
            "de": "Heute ziehst du deine Mutter in eine neue Wohnung, und das Licht schwindet. Bring sie vor der Dunkelheit heim — ehrlich, mit allen, die mit dir tragen wollen.",
            "pt": "Hoje mudas a tua mãe para uma casa nova, e a luz está a ir-se. Leva-a a casa antes de escurecer, de forma honesta, com quem quiser carregar contigo.",
            "ru": "Сегодня ты перевозишь маму в новую квартиру, и свет уходит. Успей привезти её домой до темноты — честно, с теми, кто готов нести это вместе с тобой.",
            "zh": "今天你要把妈妈搬进新家，而天色正在暗下来。赶在天黑前把她安顿好——用正当的法子，和愿意陪你一起扛的人。",
            "ar": "اليوم تنقل أمك إلى بيت جديد، والضوء يخبو. أوصلها إلى البيت قبل حلول الظلام — بطريقة نزيهة، مع كل من يريد أن يحمل الحمل معك."
        },
        "sub": "A story where you are the hero — and every choice turns you to a new page. Written for people learning English, at your level, with meaning in your language whenever you need it."
    }
}

LANGUAGE_FOCUS = {
    "A2": ["the present and 'going to'", "the house, moving and carrying"],
    "B1": ["the first conditional and modals of ability", "lifting, lending and letting go"],
    "B2": ["inference and register", "home, memory and starting over"]
}

TITLE = "Moving Day"
SLUG = "moving-day"
SERIES = "moving-day"
EPISODE = 11
BLURB = ("Today you're moving your mum into a new ground-floor flat — she can't manage the "
         "stairs any more, and it all has to be done before dark. With the van running late, a "
         "removal man ramping up his price, and a box of your dad's things gone missing, you "
         "have one short afternoon to get her home honestly — and to decide who you let carry "
         "the load with you.")


def stub(nid, ending=None):
    s = (f"[stub ending §{nid} — {ending} — prose to be written]" if ending
         else f"[stub §{nid} — prose to be written]")
    return {"A2": s, "B1": s, "B2": s}


def main():
    d = json.load(open(SRC, encoding="utf-8"))
    d["series"] = SERIES; d["episode"] = EPISODE; d["title"] = TITLE
    d["slug"] = SLUG; d["blurb"] = BLURB
    d["identity"] = IDENTITY; d["language_focus"] = LANGUAGE_FOCUS
    d["state_in"] = []; d["arc_flags"] = []
    d["state_out"] = ["moved_in", "dodged_bray", "paid_bray", "welcomed_cass",
                      "rallied_block", "helped_stranger", "shared_load", "overloaded"]
    for n in d["nodes"]:
        nid = n["id"]; end = n.get("ending")
        n["text"] = stub(nid, end)
        for j, c in enumerate(n.get("choices") or []):
            goto = c.get("goto"); ct = f"[choice {j+1} → §{goto}]"
            c["text"] = {"A2": ct, "B1": ct, "B2": ct}
            if c.get("sets"): c["sets"] = [rf(f) for f in c["sets"]]
            if c.get("requires"):
                r = c["requires"]
                c["requires"] = rf(r) if isinstance(r, str) else [rf(f) for f in r]
    d["lexicon"] = {"_comment": "Moving Day's chosen lexicon. Grown in phase 4. Base-keyed; everyday words.",
                    "entries": {}}
    json.dump(d, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"wrote episode-11.json: {len(d['nodes'])} nodes, "
          f"{sum(1 for n in d['nodes'] if n.get('ending'))} endings, flags={d['state_out']}")


if __name__ == "__main__":
    main()
