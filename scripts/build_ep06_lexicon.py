#!/usr/bin/env python3
"""Phase 4: build 'The Orchard's embedded lexicon.

Words shared with books 1-5 reuse their reviewed-draft glosses (kept only where the sense matches
here); new subject words (the orchard, the blossom, the frost and the fires) get fresh draft
glosses in English + 8 languages. Machine-drafted; native review (phase 5) finalises.

Writes the merged lexicon into content/episode-06.json's `lexicon.entries`.
Run: python3 scripts/build_ep06_lexicon.py
"""
import json, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SRCS = [os.path.join(ROOT, "content", f) for f in
        ("episode-01.json", "episode-02.json", "episode-03.json",
         "episode-04.json", "episode-05.json")]
EP6 = os.path.join(ROOT, "content", "episode-06.json")

# General words already glossed for books 1-5, reused here for a consistent learner gloss.
REUSE = [
    "cold", "light", "oil", "frost", "help", "dark", "whole", "hold", "watch", "warm", "frozen",
    "lantern", "worst", "low", "hour", "ice", "dry", "fire", "coat", "dawn", "real", "flame",
    "press", "save", "fuel", "lamp", "thin", "toward", "ahead", "reach", "proper", "family",
    "refuse", "frightened", "water", "steady", "fear", "well", "clean", "breath", "cottage",
    "child", "pale", "stove", "promise", "deep", "spent", "ridge", "weigh", "kind", "weak", "coax",
    "share", "grey", "feed", "charge", "matches", "ground", "doubt", "barely", "money", "relief",
    "stranger", "sun", "chest", "offer", "torn", "grip", "crew", "freezing", "heat", "burn", "edge",
    "feet", "breathing", "whatever", "shelter", "knock", "heavy", "legs", "barrel", "sell",
    "trouble", "wrong", "tired", "fetch", "guess", "price", "anyway", "doorway", "wrap", "calm",
    "con", "warmth", "plain", "drop", "onto", "kindness", "stretch", "teeth", "blanket", "scramble",
    "pot", "till", "blame", "careful", "advice", "firm", "crowd", "pour", "soaked", "grab", "gather",
    "shed", "spare", "aside", "settle", "quiet", "silent", "hook", "cruel", "trade", "empty",
    "crawl", "huddle", "bone", "figure", "warning", "shove", "dust", "silence", "curled", "flicker",
    "glance", "ache", "truck", "lean", "proud", "brave", "trick", "decent", "honest", "neighbour",
    "scrape",
]

def e(pos, en, fr, es, pt, it, de, ru, ar, zh):
    return {"pos": pos, "en": en, "fr": fr, "es": es, "pt": pt, "it": it,
            "de": de, "ru": ru, "ar": ar, "zh": zh}

NEW = {
 # --- the orchard ---
 "orchard": e("noun", "a piece of land where fruit trees grow",
   "le verger", "el huerto", "o pomar", "il frutteto", "der Obstgarten",
   "фруктовый сад", "بستان", "果园"),
 "tree": e("noun", "a tall plant with a trunk, branches and leaves",
   "l'arbre", "el árbol", "a árvore", "l'albero", "der Baum", "дерево", "شجرة", "树"),
 "blossom": e("noun", "the flowers on a fruit tree",
   "la fleur", "la flor", "a flor", "il fiore", "die Blüte", "цвет", "زهر", "花"),
 "bud": e("noun", "a flower or leaf before it opens",
   "le bourgeon", "el brote", "o botão", "la gemma", "die Knospe", "почка", "برعم", "花蕾"),
 "branch": e("noun", "an arm of a tree, growing from the trunk",
   "la branche", "la rama", "o ramo", "il ramo", "der Ast", "ветка", "غصن", "树枝"),
 "bloom": e("verb", "to open into flower",
   "fleurir", "florecer", "florescer", "fiorire", "blühen", "цвести", "يزهر", "开花"),
 "petal": e("noun", "one of the soft coloured parts of a flower",
   "le pétale", "el pétalo", "a pétala", "il petalo", "das Blütenblatt",
   "лепесток", "بتلة", "花瓣"),
 "root": e("noun", "the part of a plant that grows underground",
   "la racine", "la raíz", "a raiz", "la radice", "die Wurzel", "корень", "جذر", "根"),
 "bark": e("noun", "the hard outer covering of a tree",
   "l'écorce", "la corteza", "a casca", "la corteccia", "die Rinde", "кора", "لحاء", "树皮"),
 "row": e("noun", "a line of things side by side",
   "la rangée", "la hilera", "a fileira", "la fila", "die Reihe", "ряд", "صفّ", "一排"),
 "lane": e("noun", "a narrow road or path",
   "le chemin", "el camino", "a azinhaga", "il viottolo", "der Feldweg",
   "просёлок", "ممرّ", "小路"),
 "pond": e("noun", "a small area of still water",
   "la mare", "el estanque", "o lago", "lo stagno", "der Teich", "пруд", "بركة", "池塘"),
 "hedge": e("noun", "a row of bushes forming a boundary",
   "la haie", "el seto", "a sebe", "la siepe", "die Hecke", "живая изгородь", "سياج", "树篱"),
 "gate": e("noun", "a door in a wall or fence",
   "le portail", "la verja", "o portão", "il cancello", "das Tor", "ворота", "بوّابة", "门"),
 "field": e("noun", "an open area of land for crops or grass",
   "le champ", "el campo", "o campo", "il campo", "das Feld", "поле", "حقل", "田地"),

 # --- the frost & the spring night ---
 "spring": e("noun", "the season after winter, when plants grow",
   "le printemps", "la primavera", "a primavera", "la primavera", "der Frühling",
   "весна", "الربيع", "春天"),
 "bitter": e("adjective", "(of cold) very sharp and hard to bear",
   "mordant", "glacial", "cortante", "pungente", "beißend",
   "пронизывающий", "قارس", "刺骨的"),
 "nip": e("noun", "a sharp, biting feeling of cold",
   "le mordant", "la mordedura del frío", "o frio cortante", "il pizzicore",
   "die eisige Kälte", "мороз", "لسعة البرد", "刺骨寒意"),
 "thaw": e("verb", "to become warmer and less frozen",
   "dégeler", "descongelarse", "descongelar", "sgelare", "auftauen",
   "оттаивать", "يذوب", "解冻"),
 "mist": e("noun", "a thin cloud low to the ground",
   "la brume", "la neblina", "a neblina", "la foschia", "der Nebel", "туман", "ضباب", "薄雾"),
 "star": e("noun", "a point of light in the night sky",
   "l'étoile", "la estrella", "a estrela", "la stella", "der Stern", "звезда", "نجمة", "星"),

 # --- the fires & the fight ---
 "fire": e("noun", "the flames, heat and light of something burning",
   "le feu", "el fuego", "o fogo", "il fuoco", "das Feuer", "огонь", "نار", "火"),
 "ember": e("noun", "a small piece of burning or glowing coal or wood",
   "la braise", "la brasa", "a brasa", "la brace", "die Glut", "уголёк", "جمرة", "余烬"),
 "smoke": e("noun", "the grey cloud that rises from a fire",
   "la fumée", "el humo", "o fumo", "il fumo", "der Rauch", "дым", "دخان", "烟"),
 "smudge-pot": e("noun", "a pot that burns to make heat and smoke among the trees",
   "le brasero", "el brasero", "o braseiro", "il braciere", "der Frostschutzofen",
   "дымовой горшок", "موقد الدخان", "熏烟炉"),
 "straw": e("noun", "dry stalks of cut grain, used for fuel or bedding",
   "la paille", "la paja", "a palha", "la paglia", "das Stroh", "солома", "قشّ", "稻草"),
 "kindle": e("verb", "to start a fire burning",
   "allumer", "encender", "acender", "accendere", "entzünden",
   "разжигать", "يُشعل", "点燃"),
 "tend": e("verb", "to look after and keep going",
   "entretenir", "cuidar", "cuidar", "accudire", "pflegen", "ухаживать", "يعتني بـ", "照料"),
 "bucket": e("noun", "a round open container with a handle",
   "le seau", "el cubo", "o balde", "il secchio", "der Eimer", "ведро", "دلو", "水桶"),
 "spark": e("noun", "a tiny bit of fire; a small flash of light",
   "l'étincelle", "la chispa", "a faísca", "la scintilla", "der Funke", "искра", "شرارة", "火花"),
 "scorch": e("verb", "to burn the surface of something",
   "roussir", "chamuscar", "chamuscar", "bruciacchiare", "versengen",
   "опалять", "يلفح", "烤焦"),

 # --- people & the crisis ---
 "grower": e("noun", "a person who grows fruit or crops",
   "le cultivateur", "el cultivador", "o cultivador", "il coltivatore", "der Züchter",
   "садовод", "المزارع", "果农"),
 "buyer": e("noun", "a person who buys, especially to resell",
   "l'acheteur", "el comprador", "o comprador", "il compratore", "der Aufkäufer",
   "скупщик", "المشتري", "买家"),
 "village": e("noun", "a small group of houses in the country",
   "le village", "el pueblo", "a aldeia", "il villaggio", "das Dorf",
   "деревня", "قرية", "村庄"),
 "crop": e("noun", "the plants a farmer grows for food or money",
   "la récolte", "la cosecha", "a colheita", "il raccolto", "die Ernte",
   "урожай", "محصول", "庄稼"),
 "harvest": e("noun", "the fruit or crop gathered in; the gathering of it",
   "la moisson", "la cosecha", "a colheita", "il raccolto", "die Ernte",
   "жатва", "الحصاد", "收成"),
 "ruin": e("verb", "to spoil or destroy completely",
   "ruiner", "arruinar", "arruinar", "rovinare", "ruinieren", "губить", "يدمّر", "毁掉"),
 "shelter": e("noun", "a place that protects from weather or danger",
   "l'abri", "el refugio", "o abrigo", "il riparo", "der Unterschlupf",
   "укрытие", "ملجأ", "庇护所"),
 "lose": e("verb", "to fail to keep; to no longer have",
   "perdre", "perder", "perder", "perdere", "verlieren", "терять", "يفقد", "失去"),

 # --- coverage top-up (words the prose leans on) ---
 "ablaze": e("adjective", "burning strongly; on fire",
   "en flammes", "en llamas", "em chamas", "in fiamme", "in Flammen",
   "в огне", "مشتعل", "燃烧着的"),
 "blaze": e("verb", "to burn brightly and strongly",
   "flamber", "arder", "arder", "ardere", "lodern", "пылать", "يتوهّج", "熊熊燃烧"),
 "brittle": e("adjective", "hard but easily broken",
   "cassant", "quebradizo", "quebradiço", "fragile", "spröde",
   "хрупкий", "هشّ", "易碎的"),
 "chill": e("verb", "to make cold",
   "refroidir", "enfriar", "arrefecer", "raffreddare", "kühlen",
   "охлаждать", "يبرّد", "使变冷"),
 "damp": e("adjective", "a little wet",
   "humide", "húmedo", "húmido", "umido", "feucht", "влажный", "رطب", "潮湿的"),
 "cheque": e("noun", "a written order to pay money from a bank",
   "le chèque", "el cheque", "o cheque", "l'assegno", "der Scheck",
   "чек", "شيك", "支票"),
 "armful": e("noun", "as much as you can carry in your arms",
   "une brassée", "una brazada", "uma braçada", "una bracciata", "ein Armvoll",
   "охапка", "حُضن", "一抱"),
 "grandchild": e("noun", "the child of your son or daughter",
   "le petit-enfant", "el nieto", "o neto", "il nipote", "das Enkelkind",
   "внук", "حفيد", "孙辈"),
 "bless": e("verb", "to wish good upon; to thank warmly",
   "bénir", "bendecir", "abençoar", "benedire", "segnen", "благословлять", "يبارك", "祝福"),
 "crack": e("verb", "to break with a sharp sound; to split",
   "craquer", "agrietarse", "rachar", "incrinarsi", "knacken",
   "трескаться", "يتشقّق", "裂开"),
 "sting": e("verb", "to cause a sharp, small pain",
   "piquer", "picar", "picar", "pungere", "stechen", "жалить", "يلسع", "刺痛"),
 "swing": e("verb", "to move back and forth, or round, from a fixed point",
   "balancer", "balancear", "balançar", "oscillare", "schwingen",
   "качать", "يتأرجح", "摆动"),
 "beg": e("verb", "to ask for something very anxiously",
   "supplier", "suplicar", "implorar", "supplicare", "flehen",
   "умолять", "يتوسّل", "乞求"),
 "spread": e("verb", "to reach or move over a wider area",
   "se répandre", "extenderse", "espalhar-se", "diffondersi", "sich ausbreiten",
   "распространяться", "ينتشر", "蔓延"),
 "ease": e("verb", "to become less strong or less painful",
   "se calmer", "amainar", "abrandar", "attenuarsi", "nachlassen",
   "стихать", "يخفّ", "减弱"),
}


def main():
    src = {}
    for f in SRCS:
        try:
            src.update(json.load(open(f, encoding="utf-8"))["lexicon"]["entries"])
        except Exception:
            pass
    book = json.load(open(EP6, encoding="utf-8"))
    entries, missing = {}, []
    for w in REUSE:
        if w in src:
            entries[w] = src[w]
        else:
            missing.append(w)
    for w, v in NEW.items():
        entries[w.strip()] = v
    book["lexicon"]["entries"] = dict(sorted(entries.items()))
    json.dump(book, open(EP6, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"Lexicon written: {len(entries)} entries "
          f"({len([w for w in REUSE if w in src])} reused, {len(NEW)} new).")
    if missing:
        print("WARNING reuse words not in books 1-5:", ", ".join(missing))


if __name__ == "__main__":
    main()
