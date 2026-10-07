#!/usr/bin/env python3
"""Phase 2: build The Refuge (episode-07) graph skeleton by transforming the shared
topology from The Orchard (episode-06): same node ids / edges / flag positions /
ending valences, with the refuge's identity, flag names, and one-line stub prose.
Phase 3 replaces the stubs with real A2/B1/B2 prose.

Run: python3 scripts/generators/build_ep07_skeleton.py
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(ROOT, "content", "episode-06.json")
OUT = os.path.join(ROOT, "content", "episode-07.json")

FLAGMAP = {
    "has_fires": "has_stove",
    "dodged_buyer": "dodged_vane",
    "paid_buyer": "paid_vane",
    "found_child": "found_walker",
    "rallied_village": "roused_valley",
    "took_shortcut": "took_cornice",
    # helped_stranger, gave_shelter unchanged
}
def rf(f): return FLAGMAP.get(f, f)

IDENTITY = {
    "name": "Whiteout",
    "mood": "A storm-locked mountain refuge at night; the only warmth and the only light for miles is the one you keep.",
    "palette": {
        "ground": "#0B1420", "surface": "#13202F", "ink": "#F2F5F7",
        "muted": "#8A97A8", "line": "#223247",
        "accent": "#F0A338", "accentHot": "#F7C070", "secondary": "#A9C7DE"
    },
    "cover": {
        "kind": "refuge", "glow": True, "focal": "60% 58%",
        "alt": "A dark mountain in a whiteout at night: driving snow across the slope and a single stone refuge hut with one warm lit window."
    },
    "type": {"display": "Fraunces", "ui": "Hanken Grotesk", "mono": "JetBrains Mono"},
    "hero": {
        "line": {
            "en": "The storm has the mountain tonight. Keep the stove lit and the lamp in the window, and hold the refuge till first light.",
            "fr": "Cette nuit, la tempête tient la montagne. Garde le poêle allumé et la lampe à la fenêtre, et tiens le refuge jusqu'à l'aube.",
            "es": "Esta noche la tormenta tiene la montaña. Mantén la estufa encendida y la lámpara en la ventana, y resiste en el refugio hasta el amanecer.",
            "it": "Stanotte la tempesta ha la montagna. Tieni la stufa accesa e la lampada alla finestra, e reggi il rifugio fino alle prime luci.",
            "de": "Heute Nacht hat der Sturm den Berg. Halte den Ofen am Brennen und die Lampe im Fenster, und halte die Hütte bis zum ersten Licht.",
            "pt": "Esta noite a tempestade tem a montanha. Mantém o fogão aceso e o candeeiro à janela, e aguenta o refúgio até ao amanhecer.",
            "ru": "Этой ночью буря завладела горой. Держи печь растопленной и лампу в окне, и выстой приют до первого света.",
            "zh": "今夜风暴占住了这座山。让炉火不灭，把灯留在窗口，守住这座山间小屋，直到天明。",
            "ar": "الليلة العاصفة تُطبق على الجبل. أبقِ الموقد مشتعلاً والمصباح في النافذة، واصمد في الملجأ حتى أول ضوء."
        },
        "sub": "A story where you are the hero — and every choice turns you to a new page. Written for people learning English, at your level, with meaning in your language whenever you need it."
    }
}

LANGUAGE_FOCUS = {
    "A2": ["imperatives and going to", "the weather, the hut and the body"],
    "B1": ["the first conditional and modals of advice", "warning, helping and planning"],
    "B2": ["inference, obligation and conditionals", "care, risk and responsibility"]
}

TITLE = "The Refuge"
SLUG = "the-refuge"
SERIES = "the-refuge"
EPISODE = 7
BLURB = ("A whiteout closes over a high mountain refuge at dusk, and the old warden is hurt "
         "inside. Keeping the stove lit and the lamp in the window — the one beacon for anyone "
         "caught out on the mountain — is on you now. You have until first light to hold the "
         "refuge, and whoever the storm sends, against the cold.")


def stub(nid, ending=None):
    if ending:
        s = f"[stub ending §{nid} — {ending} — prose to be written]"
    else:
        s = f"[stub §{nid} — prose to be written]"
    return {"A2": s, "B1": s, "B2": s}


def main():
    d = json.load(open(SRC, encoding="utf-8"))
    d["series"] = SERIES
    d["episode"] = EPISODE
    d["title"] = TITLE
    d["slug"] = SLUG
    d["blurb"] = BLURB
    d["identity"] = IDENTITY
    d["language_focus"] = LANGUAGE_FOCUS
    d["state_in"] = []
    d["arc_flags"] = []
    d["state_out"] = ["has_stove", "dodged_vane", "paid_vane", "found_walker",
                      "roused_valley", "helped_stranger", "gave_shelter", "took_cornice"]

    for n in d["nodes"]:
        nid = n["id"]
        end = n.get("ending")
        n["text"] = stub(nid, end)
        for j, c in enumerate(n.get("choices") or []):
            goto = c.get("goto")
            ct = f"[choice {j+1} → §{goto}]"
            c["text"] = {"A2": ct, "B1": ct, "B2": ct}
            if "sets" in c and c["sets"]:
                c["sets"] = [rf(f) for f in c["sets"]]
            if "requires" in c and c["requires"]:
                r = c["requires"]
                c["requires"] = rf(r) if isinstance(r, str) else [rf(f) for f in r]

    d["lexicon"] = {"_comment": "The Refuge's chosen lexicon. Grown in phase 4. Base-keyed; the reader resolves inflections.",
                    "entries": {}}

    json.dump(d, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    nodes = len(d["nodes"]); endings = sum(1 for n in d["nodes"] if n.get("ending"))
    print(f"wrote episode-07.json: {nodes} nodes, {endings} endings, flags={d['state_out']}")


if __name__ == "__main__":
    main()
