#!/usr/bin/env python3
"""Phase 2: build The Interview (episode-10) graph skeleton from the shared topology
(episode-09, The Dinner): same ids/edges/flag positions/ending valences, with the
interview's identity, flag names, and stub prose. Phase 3 writes real prose.
Run: python3 scripts/generators/build_ep10_skeleton.py"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(ROOT, "content", "episode-09.json")
OUT = os.path.join(ROOT, "content", "episode-10.json")

FLAGMAP = {
    "has_dinner": "ready",
    "dodged_dale": "dodged_reese",
    "paid_dale": "paid_reese",
    "welcomed_nora": "faced_maya",
    "rallied_friends": "rallied_room",
    "shared_food": "shared_notes",
    "ran_road": "jumped_queue",
    # helped_stranger unchanged
}
def rf(f): return FLAGMAP.get(f, f)

IDENTITY = {
    "name": "Interview at Two",
    "mood": "A cold morning, a warm chance: the interview that could change everything is at two, and the city is against you.",
    "palette": {
        "ground": "#12161C", "surface": "#1B2129", "ink": "#EEF1F4",
        "muted": "#8A94A2", "line": "#2A323D",
        "accent": "#D98A3D", "accentHot": "#F0B36A", "secondary": "#7FA8C9"
    },
    "cover": {
        "kind": "office", "glow": True, "focal": "56% 50%",
        "alt": "A warm-lit interview-room window high in a cool glass tower at dusk, rain on the street below, one warm window among the cold ones."
    },
    "type": {"display": "Fraunces", "ui": "Hanken Grotesk", "mono": "JetBrains Mono"},
    "hero": {
        "line": {
            "en": "The interview that could change everything is at two o'clock, and the morning is already against you. Get there, as yourself, and earn it straight.",
            "fr": "L'entretien qui peut tout changer est à quatorze heures, et la matinée est déjà contre toi. Arrives-y en restant toi-même, et mérite-le honnêtement.",
            "es": "La entrevista que podría cambiarlo todo es a las dos, y la mañana ya está en tu contra. Llega allí siendo tú mismo, y gánatelo con honradez.",
            "it": "Il colloquio che potrebbe cambiare tutto è alle due, e la mattinata è già contro di te. Arrivaci restando te stesso, e meritatelo con onestà.",
            "de": "Das Vorstellungsgespräch, das alles verändern könnte, ist um zwei, und der Morgen ist schon gegen dich. Komm hin, bleib du selbst, und verdien es dir ehrlich.",
            "pt": "A entrevista que pode mudar tudo é às duas, e a manhã já está contra ti. Chega lá sendo tu mesmo, e merece-a com honestidade.",
            "ru": "Собеседование, которое может изменить всё, — в два часа, а утро уже против тебя. Доберись туда, оставаясь собой, и заслужи это честно.",
            "zh": "那场可能改变一切的面试在两点，而这个上午已经处处跟你作对。赶到那里，做你自己，堂堂正正地赢下它。",
            "ar": "المقابلة التي قد تُغيّر كل شيء في الساعة الثانية، والصباح بالفعل ضدّك. اوصل إلى هناك كما أنت، واستحقّها بنزاهة."
        },
        "sub": "A story where you are the hero — and every choice turns you to a new page. Written for people learning English, at your level, with meaning in your language whenever you need it."
    }
}

LANGUAGE_FOCUS = {
    "A2": ["the present and 'going to'", "the office, work and the clock"],
    "B1": ["the first conditional and modals of advice", "arriving, asking and keeping calm"],
    "B2": ["inference and register", "honesty, nerves and second chances"]
}

TITLE = "The Interview"
SLUG = "the-interview"
SERIES = "the-interview"
EPISODE = 10
BLURB = ("The job you need is one interview away — at two o'clock today. But the trains are "
         "down, a document is missing, and a smooth stranger is offering an easy way to fake "
         "your way in. With the clock running and someone from your past on the panel, you "
         "have one morning to get there as yourself — and earn it honestly.")


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
    d["state_out"] = ["ready", "dodged_reese", "paid_reese", "faced_maya",
                      "rallied_room", "helped_stranger", "shared_notes", "jumped_queue"]
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
    d["lexicon"] = {"_comment": "The Interview's chosen lexicon. Grown in phase 4. Base-keyed; everyday words.",
                    "entries": {}}
    json.dump(d, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"wrote episode-10.json: {len(d['nodes'])} nodes, "
          f"{sum(1 for n in d['nodes'] if n.get('ending'))} endings, flags={d['state_out']}")


if __name__ == "__main__":
    main()
