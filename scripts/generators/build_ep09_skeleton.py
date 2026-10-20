#!/usr/bin/env python3
"""Phase 2: build The Dinner (episode-09) graph skeleton from the shared topology
(episode-08, The Refuge): same ids/edges/flag positions/ending valences, with the
dinner's identity, flag names, and stub prose. Phase 3 writes real prose.
Run: python3 scripts/generators/build_ep09_skeleton.py"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(ROOT, "content", "episode-08.json")
OUT = os.path.join(ROOT, "content", "episode-09.json")

FLAGMAP = {
    "has_stove": "has_dinner",
    "dodged_vane": "dodged_dale",
    "paid_vane": "paid_dale",
    "found_walker": "welcomed_nora",
    "roused_valley": "rallied_friends",
    "gave_shelter": "shared_food",
    "took_cornice": "ran_road",
    # helped_stranger unchanged
}
def rf(f): return FLAGMAP.get(f, f)

IDENTITY = {
    "name": "Dinner at Seven",
    "mood": "A warm kitchen on a winter evening; dinner for the people you love, and two hours to get it right.",
    "palette": {
        "ground": "#1A1210", "surface": "#241A16", "ink": "#F6EFE6",
        "muted": "#A2938A", "line": "#38281F",
        "accent": "#E8903A", "accentHot": "#F4B46A", "secondary": "#93B88A"
    },
    "cover": {
        "kind": "kitchen", "glow": True, "focal": "58% 52%",
        "alt": "A warm, lit kitchen window on a dark winter street at night: steam on the glass, a pot on the hob and a table laid for dinner inside."
    },
    "type": {"display": "Fraunces", "ui": "Hanken Grotesk", "mono": "JetBrains Mono"},
    "hero": {
        "line": {
            "en": "The family come for dinner at seven, and tonight the cooking is all yours. Get a good evening onto the table.",
            "fr": "La famille vient dîner à sept heures, et ce soir, c'est toi qui cuisines. Prépare une belle soirée à table.",
            "es": "La familia viene a cenar a las siete, y esta noche cocinas tú. Pon una buena velada en la mesa.",
            "it": "La famiglia viene a cena alle sette, e stasera cucini tu. Porta in tavola una bella serata.",
            "de": "Die Familie kommt um sieben zum Essen, und heute Abend kochst du. Bring einen schönen Abend auf den Tisch.",
            "pt": "A família vem jantar às sete, e esta noite quem cozinha és tu. Põe uma boa noite na mesa.",
            "ru": "Семья придёт на ужин в семь, и сегодня готовишь ты. Накрой хороший вечер на стол.",
            "zh": "家人七点来吃晚饭，今晚做饭全靠你了。为大家张罗一桌好饭、一个好夜晚。",
            "ar": "تأتي العائلة للعشاء في السابعة، والليلة الطبخ كله عليك. قدِّم أمسية جميلة على المائدة."
        },
        "sub": "A story where you are the hero — and every choice turns you to a new page. Written for people learning English, at your level, with meaning in your language whenever you need it."
    }
}

LANGUAGE_FOCUS = {
    "A2": ["imperatives and the present", "the kitchen, food and time"],
    "B1": ["the first conditional and modals of advice", "planning, helping and inviting"],
    "B2": ["inference and politeness", "hospitality, pride and letting people in"]
}

TITLE = "The Dinner"
SLUG = "the-dinner"
SERIES = "the-dinner"
EPISODE = 9
BLURB = ("It's Gran's birthday and the family come for dinner at seven — but Gran is ill upstairs, "
         "and tonight the cooking is all yours. With a takeaway man offering an easy cheat and the "
         "clock running down, you have two hours to get a good evening onto the table, and to decide "
         "who you let through the door.")


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
    d["state_out"] = ["has_dinner", "dodged_dale", "paid_dale", "welcomed_nora",
                      "rallied_friends", "helped_stranger", "shared_food", "ran_road"]
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
    d["lexicon"] = {"_comment": "The Dinner's chosen lexicon. Grown in phase 4. Base-keyed; everyday words.",
                    "entries": {}}
    json.dump(d, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"wrote episode-09.json: {len(d['nodes'])} nodes, "
          f"{sum(1 for n in d['nodes'] if n.get('ending'))} endings, flags={d['state_out']}")


if __name__ == "__main__":
    main()
