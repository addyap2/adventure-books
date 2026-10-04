#!/usr/bin/env python3
"""Phase 2: graph skeleton for book 6, 'The Orchard' (standalone).

The branching ENGINE is the proven, validator-clean topology shared by every book (same ids,
edges and flag positions); only the flags, identity and prose are this book's own. We build it by
transforming book 5's skeleton: rename the flags, re-skin the stub prose to the orchard, set the
12 endings from the design bible, and stamp the Frost-Fires identity. Stub prose is placeholder
(identical across A2/B1/B2) — Phase 3 rewrites every line in band. The validator must return 0
errors on the output before any real prose is written.

Flag re-map (role-for-role): has_light->has_fires, dodged_wrecker->dodged_buyer,
paid_wrecker->paid_buyer, found_boat->found_child, rallied_coast->rallied_village;
helped_stranger / gave_shelter / took_shortcut keep their names.

Run: python3 scripts/build_ep06_skeleton.py
"""
import json, os, re, tempfile, runpy, shutil

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
EP05_SRC = os.path.join(ROOT, "scripts", "build_ep05_skeleton.py")
OUT = os.path.join(ROOT, "content", "episode-06.json")

# --- 1. run book 5's skeleton builder into a throwaway file (never touch content/episode-05.json) ---
tmpdir = tempfile.mkdtemp()
tmp_src = os.path.join(tmpdir, "ep05.py")
tmp_out = os.path.join(tmpdir, "episode-05.json")
src = open(EP05_SRC, encoding="utf-8").read()
src = src.replace('OUT = os.path.join(ROOT, "content", "episode-05.json")',
                  'OUT = %r' % tmp_out)
open(tmp_src, "w", encoding="utf-8").write(src)
runpy.run_path(tmp_src, run_name="__main__")
book = json.load(open(tmp_out, encoding="utf-8"))
shutil.rmtree(tmpdir, ignore_errors=True)

# --- 2. flag re-map (role-for-role) ---
FLAG = {"has_light": "has_fires", "dodged_wrecker": "dodged_buyer",
        "paid_wrecker": "paid_buyer", "found_boat": "found_child",
        "rallied_coast": "rallied_village"}
def remap_flags(lst): return [FLAG.get(f, f) for f in (lst or [])]

# --- 3. themed re-skin of placeholder stub/choice prose (longest phrases first) ---
# Placeholder quality only; Phase 3 writes the real three-level prose. Role-preserving.
MAP = [
    ("the old keeper, Nan Bright,", "the old grower, Edith Marsh,"),
    ("Nan Bright", "Edith Marsh"), ("Nan", "Edith"),
    ("the second light on the water", "the light among the far trees"),
    ("the light on the water", "the light among the far trees"),
    ("light on the water", "light in the trees"),
    ("Bosun Carrick", "old Jack Hale"), ("Carrick", "Hale"),
    ("the wrecker", "the buyer"), ("wrecker", "buyer"),
    ("Tam at the coast station", "Tom at the co-op"), ("Tam", "Tom"),
    ("the lifeboat", "the morning crew"), ("lifeboat", "morning crew"),
    ("the cliff path", "the frozen pond"), ("cliff path", "frozen pond"),
    ("the great lamp", "the fires"), ("the lamp", "the fire"), ("lamp", "fire"),
    ("the beacon", "the frost-fire"), ("beacon", "frost-fire"),
    ("the beam", "the fires"), ("beam", "fire"),
    ("the wick", "the straw"), ("wick", "straw"),
    ("the lens", "the pots"), ("lens", "pots"),
    ("signal fires", "torches"),
    ("the lighthouse", "the orchard"), ("lighthouse", "orchard"),
    ("the tower", "the house"), ("tower", "house"),
    ("the stairs", "the back steps"),
    ("the harbour mouth", "the ridge"), ("the harbour", "the village"), ("harbour", "village"),
    ("the cove", "the far rows"), ("cove", "far rows"),
    ("the storm", "the frost"), ("storm", "frost"),
    ("the gale", "the hard cold"), ("gale", "cold"),
    ("the swell", "the cold"), ("swell", "cold"),
    ("the waves", "the dark"), ("waves", "dark"), ("wave", "cold"),
    ("the spray", "the frost"), ("spray", "frost"),
    ("the surf", "the frost"), ("surf", "frost"),
    ("the tideline", "the low ground"), ("the tide", "the frost"), ("tide", "frost"),
    ("the sea", "the night"), ("sea", "night"),
    ("the rocks", "the low ground"), ("rocks", "ground"),
    ("the shore", "the village"), ("shore", "village"),
    ("the coast", "the village"), ("coast", "village"),
    ("the point", "the ridge"), ("offshore", "out in the far rows"),
    ("a ship", "a year's crop"), ("the ship", "the crop"), ("ship", "crop"),
    ("the fisher", "the neighbour"), ("fisher", "neighbour"),
    ("the rope", "the rows"),
    ("Ash", "Wren"),
    ("soaked", "frozen"), ("drown", "freeze"), ("drowned", "frozen"),
    ("the oil", "the oil"),  # kept (orchard fires use oil too)
    ("a boat's lights", "the blossom, white and still,"),
    ("the boat", "the blossom"), ("a boat", "the blossom"), ("boat", "blossom"),
]
def reskin(s):
    for a, b in MAP:
        s = s.replace(a, b)
        s = s.replace(a[0].upper() + a[1:], (b[0].upper() + b[1:]))
    return s

# --- 4. the 12 endings, verbatim from the design bible (ids & valence preserved) ---
ENDINGS = {
 120: ("The blossom held. You kept the fires burning down the rows all night; at first light the sun comes over the ridge, the frost lifts, and the blossom — and the whole year's fruit — comes through.", "good"),
 121: ("The light in the trees. You answered the light no one could explain, found Wren lost and cold among the far rows and got them warm in time — and reopened a door between Edith and the son she had not spoken to in years.", "good"),
 122: ("The whole village, awake. No single heroic move — but you turned a sleeping village into people with torches down every row, and everyone brought the night through together.", "good"),
 123: ("You did what you could. You refused the con, kept your head, and saved what you could by decent means. Not perfect. But clean, honest, and enough.", "good"),
 124: ("The kindness returned. You fell short of the whole orchard, but the neighbour you stopped for helps you save the near rows and gets Edith warm. Rescue without the full win.", "neutral"),
 125: ("Shared what you had. You gave your own coat and fuel away and end the night cold yourself, but not alone — and something in the village has shifted. A start, not a save.", "neutral"),
 126: ("One more hour. You scrape through the worst of it; the wind turns at last and a thin dawn saves part of the blossom. Not triumphant — just, in the end, relieved.", "neutral"),
 127: ("The orchard remembers. You didn't save it all, but the village saw you out among the trees when others slept. You are, from tonight, someone this place knows.", "neutral"),
 128: ("You signed it away. You took the buyer's deal, and by morning the orchard is no longer Edith's to save; the frost did the rest. The cheque is cold, and so is the ground by morning.", "bad"),
 129: ("The ice took it. The frozen pond was a trap; you go through in the dark, and it takes the night — you reach the far rows frozen, shaking, and far too late.", "bad"),
 130: ("Cold too long. You spent the night on the wrong things, and the fires went out too long; by dawn the blossom is black and the year is lost.", "bad"),
 131: ("You stayed inside. You stayed warm indoors and never lit a fire. Nothing bad happened to you. You will think about it for a long time.", "bad"),
}
VAL_TAG = {"good": "GOOD", "neutral": "NEUTRAL", "bad": "BAD"}

# --- 5. transform every node ---
for n in book["nodes"]:
    if "ending" in n and n["id"] in ENDINGS:
        text, val = ENDINGS[n["id"]]
        n["ending"] = val
        n["text"] = {lv: "[stub] %s — %s" % (VAL_TAG[val], text) for lv in ("A2", "B1", "B2")}
        continue
    # re-skin stub text
    n["text"] = {lv: reskin(v) for lv, v in n["text"].items()}
    for ch in n.get("choices", []):
        ch["text"] = {lv: reskin(v) for lv, v in ch["text"].items()}
        if "sets" in ch: ch["sets"] = remap_flags(ch["sets"])
        if "requires" in ch: ch["requires"] = remap_flags(ch["requires"])

# --- 6. identity & meta (The Orchard / Frost Fires) ---
book["series"] = "the-orchard"
book["episode"] = 6
book["title"] = "The Orchard"
book["slug"] = "the-orchard"
book["blurb"] = ("A killing frost comes on the coldest night of spring, just as the orchard stands "
    "in blossom — and the old grower is hurt at the foot of the back steps. Lighting and feeding the "
    "fires down the rows is on you now. You have until first light to keep them burning, and the "
    "blossom alive, against the cold.")
book["state_out"] = ["has_fires", "dodged_buyer", "paid_buyer", "found_child",
                     "rallied_village", "helped_stranger", "gave_shelter", "took_shortcut"]
book["identity"] = {
    "name": "Frost Fires",
    "mood": "A frosted orchard at night; the only warmth is the fires you light down the rows to save the blossom.",
    "palette": {
        "ground": "#0E1626", "surface": "#17212F", "ink": "#EFF1EA",
        "muted": "#8C95A4", "line": "#26324A",
        "accent": "#E87C3A", "accentHot": "#F4A25C", "secondary": "#9CC4D6"
    },
    "cover": {"kind": "frostfire", "glow": True},
    "type": {"display": "Fraunces", "ui": "Hanken Grotesk", "mono": "JetBrains Mono"},
    "hero": {
        "line": {
            "en": "The frost comes for the blossom tonight. Light the fires down the rows and keep them burning till first light.",
            "fr": "Cette nuit, le gel vient pour les fleurs. Allume les feux le long des rangs et garde-les allumés jusqu'à l'aube.",
            "es": "Esta noche la helada viene por la flor. Enciende los fuegos entre las hileras y mantenlos ardiendo hasta el amanecer.",
            "it": "Stanotte il gelo viene per i fiori. Accendi i fuochi lungo i filari e tienili accesi fino alle prime luci.",
            "de": "Heute Nacht kommt der Frost für die Blüte. Zünde die Feuer entlang der Reihen an und halte sie bis zum ersten Licht am Brennen.",
            "pt": "Esta noite a geada vem pela flor. Acende os fogos ao longo das fileiras e mantém-nos acesos até ao amanhecer.",
            "ru": "Этой ночью мороз идёт за цветом. Зажги костры вдоль рядов и не дай им погаснуть до первого света.",
            "zh": "今夜寒霜要来夺走花朵。沿着树行点起火堆，守着它们烧到天明。",
            "ar": "الليلة يأتي الصقيع على الأزهار. أوقد النيران على امتداد الصفوف وأبقِها مشتعلة حتى أول ضوء."
        },
        "sub": "A story where you are the hero — and every choice turns you to a new page. Written for people learning English, at your level, with meaning in your language whenever you need it."
    }
}
book["language_focus"] = {
    "A2": ["imperatives and going to", "the cold, the garden and the body"],
    "B1": ["the first conditional and modals of advice", "warning, helping and planning"],
    "B2": ["inference, obligation and conditionals", "care, risk and responsibility"]
}
book["lexicon"] = {
    "_comment": "The Orchard's chosen lexicon. Grown in phase 4. Base-keyed; the reader resolves inflections. Translations need a native speaker's check before launch.",
    "entries": {}
}

json.dump(book, open(OUT, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("Wrote %s: %d nodes, %d endings." % (
    OUT, len(book["nodes"]), sum(1 for n in book["nodes"] if n.get("ending"))))
