#!/usr/bin/env python3
"""Phase 4: build 'The Keeper's embedded lexicon.

Words shared with books 1, 3 and 4 reuse their reviewed-draft glosses (kept only where the sense
matches here); new subject words (the storm, the sea, the lighthouse and its lamp, the rescue) get
fresh draft glosses in English + 8 languages. Machine-drafted; native review (phase 5) finalises.

Writes the merged lexicon into content/episode-05.json's `lexicon.entries`.
Run: python3 scripts/build_ep05_lexicon.py
"""
import json, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SRCS = [os.path.join(ROOT, "content", f) for f in
        ("episode-01.json", "episode-03.json", "episode-04.json")]
EP5 = os.path.join(ROOT, "content", "episode-05.json")

# General words already glossed for books 1/3/4, reused here for a consistent learner gloss.
REUSE = [
    "help", "wind", "water", "hold", "path", "whole", "worst", "low", "hour", "press", "flame",
    "toward", "dry", "well", "real", "drop", "lantern", "torn", "refuse", "ahead", "fire", "clean",
    "wet", "reach", "whatever", "steady", "dawn", "wave", "frightened", "fear", "weak", "proper",
    "signal", "soaked", "spent", "stranger", "warm", "family", "kind", "barely", "grey", "weigh",
    "radio", "knock", "promise", "trouble", "share", "rail", "child", "breath", "anyway", "thin",
    "somehow", "wrong", "breathe", "breathing", "chest", "doubt", "cruel", "trick", "relief",
    "quiet", "manage", "doorway", "bone", "spare", "heavy", "legs", "offer", "careful", "crew",
    "pale", "sell", "fetch", "guess", "price", "pour", "money", "wrap", "kindness", "calm", "stove",
    "gull", "con", "shelter", "scramble", "settle", "burn", "teeth", "deep", "feet", "tired",
    "honest", "grip", "mouth", "hook", "plain", "shove", "drag", "figure", "gentle", "lift",
    "scared", "blanket", "brave", "advice", "solid", "strange", "heat", "crowd", "blame", "realise",
    "empty", "pay", "crawl", "silence", "glance", "ache", "plume", "proud", "decent", "worn",
    "clever", "halfway", "save",
]

def e(pos, en, fr, es, pt, it, de, ru, ar, zh):
    return {"pos": pos, "en": en, "fr": fr, "es": es, "pt": pt, "it": it,
            "de": de, "ru": ru, "ar": ar, "zh": zh}

NEW = {
 # --- the storm & the sea ---
 "storm": e("noun", "very bad weather with strong wind and rain",
   "la tempête", "la tormenta", "a tempestade", "la tempesta", "der Sturm", "шторм", "عاصفة", "风暴"),
 "gale": e("noun", "a very strong wind",
   "la bourrasque", "el vendaval", "o vendaval", "la burrasca", "der Sturmwind",
   "штормовой ветер", "ريح عاتية", "狂风"),
 "sea": e("noun", "the great body of salt water around the land",
   "la mer", "el mar", "o mar", "il mare", "das Meer", "море", "البحر", "海"),
 "tide": e("noun", "the daily rise and fall of the sea",
   "la marée", "la marea", "a maré", "la marea", "die Gezeiten", "прилив", "المدّ", "潮汐"),
 "swell": e("noun", "the slow, heavy rise and fall of the sea",
   "la houle", "el oleaje", "a ondulação", "l'onda lunga", "die Dünung", "зыбь", "موج متطاول", "涌浪"),
 "surf": e("noun", "the white waves breaking on the shore",
   "le ressac", "el oleaje", "a rebentação", "la risacca", "die Brandung",
   "прибой", "الأمواج المتكسّرة", "拍岸浪"),
 "spray": e("noun", "small drops of water blown from the waves",
   "les embruns", "el rocío del mar", "os salpicos", "gli spruzzi", "die Gischt",
   "брызги", "رذاذ البحر", "浪花"),
 "spume": e("noun", "foam torn from the tops of waves by the wind",
   "l'écume", "la espuma", "a espuma", "la schiuma", "der Schaum", "пена", "زَبَد", "浪沫"),
 "foam": e("noun", "the white bubbles on breaking water",
   "l'écume", "la espuma", "a espuma", "la schiuma", "der Schaum", "пена", "رغوة", "泡沫"),
 "wreck": e("noun", "a ship destroyed at sea or on the rocks",
   "l'épave", "el naufragio", "o naufrágio", "il relitto", "das Wrack", "крушение", "حطام", "沉船"),

 # --- the coast ---
 "coast": e("noun", "the land at the edge of the sea",
   "la côte", "la costa", "a costa", "la costa", "die Küste", "берег", "الساحل", "海岸"),
 "shore": e("noun", "the land along the edge of the sea",
   "le rivage", "la orilla", "a costa", "la riva", "das Ufer", "берег", "الشاطئ", "岸"),
 "harbour": e("noun", "a safe place where boats can shelter",
   "le port", "el puerto", "o porto", "il porto", "der Hafen", "гавань", "ميناء", "港口"),
 "cove": e("noun", "a small, sheltered bay",
   "la crique", "la cala", "a enseada", "la cala", "die Bucht", "бухта", "خليج صغير", "小海湾"),
 "cliff": e("noun", "a high, steep face of rock",
   "la falaise", "el acantilado", "a falésia", "la scogliera", "die Klippe",
   "утёс", "جُرف", "悬崖"),
 "rock": e("noun", "a large, hard mass of stone",
   "le rocher", "la roca", "a rocha", "lo scoglio", "der Fels", "скала", "صخرة", "岩石"),
 "ledge": e("noun", "a narrow flat shelf of rock",
   "la corniche", "el saliente", "a saliência", "il cornicione", "der Felsvorsprung",
   "уступ", "حافّة", "岩架"),
 "point": e("noun", "a narrow piece of land reaching into the sea",
   "la pointe", "la punta", "a ponta", "il promontorio", "die Landspitze",
   "мыс", "رأس بحري", "海角"),
 "edge": e("noun", "the line where something ends; the brink",
   "le bord", "el borde", "a borda", "il bordo", "der Rand", "край", "حافّة", "边缘"),
 "drown": e("verb", "to die under water because you cannot breathe",
   "se noyer", "ahogarse", "afogar-se", "annegare", "ertrinken", "тонуть", "يغرق", "溺水"),

 # --- the light & the lamp ---
 "light": e("noun", "brightness that lets you see; a thing that shines",
   "la lumière", "la luz", "a luz", "la luce", "das Licht", "свет", "ضوء", "光"),
 "dark": e("noun", "the absence of light",
   "l'obscurité", "la oscuridad", "a escuridão", "il buio", "die Dunkelheit",
   "темнота", "الظلام", "黑暗"),
 "lamp": e("noun", "a device that gives light",
   "la lampe", "la lámpara", "a lâmpada", "la lampada", "die Lampe", "лампа", "مصباح", "灯"),
 "beam": e("noun", "a strong line of light shining out",
   "le faisceau", "el haz de luz", "o facho de luz", "il fascio di luce", "der Lichtstrahl",
   "луч", "شعاع", "光束"),
 "wick": e("noun", "the cord in a lamp or candle that burns",
   "la mèche", "la mecha", "o pavio", "lo stoppino", "der Docht", "фитиль", "فتيل", "灯芯"),
 "oil": e("noun", "a liquid fuel that burns to give light or heat",
   "l'huile", "el aceite", "o óleo", "l'olio", "das Öl", "масло", "زيت", "油"),
 "lens": e("noun", "a shaped piece of glass that bends light",
   "la lentille", "la lente", "a lente", "la lente", "die Linse", "линза", "عدسة", "透镜"),
 "glass": e("noun", "the hard, clear material in a window",
   "le verre", "el vidrio", "o vidro", "il vetro", "das Glas", "стекло", "زجاج", "玻璃"),
 "spark": e("noun", "a tiny bit of fire; a small flash of light",
   "l'étincelle", "la chispa", "a faísca", "la scintilla", "der Funke", "искра", "شرارة", "火花"),
 "glow": e("noun", "a soft, steady light",
   "la lueur", "el resplandor", "o brilho", "il bagliore", "das Glühen", "свечение", "توهّج", "微光"),

 # --- the lighthouse & the rescue ---
 "tower": e("noun", "a tall, narrow building",
   "la tour", "la torre", "a torre", "la torre", "der Turm", "башня", "برج", "塔"),
 "keeper": e("noun", "a person who looks after something, like a lighthouse",
   "le gardien", "el guardián", "o guardião", "il guardiano", "der Wärter",
   "смотритель", "الحارس", "看守人"),
 "lighthouse": e("noun", "a tower with a light that warns ships off the rocks",
   "le phare", "el faro", "o farol", "il faro", "der Leuchtturm", "маяк", "منارة", "灯塔"),
 "boat": e("noun", "a small vessel for travelling on water",
   "le bateau", "el barco", "o barco", "la barca", "das Boot", "лодка", "قارب", "船"),
 "ship": e("noun", "a large vessel for travelling on the sea",
   "le navire", "el buque", "o navio", "la nave", "das Schiff", "корабль", "سفينة", "轮船"),
 "sail": e("noun", "a sheet of cloth that catches the wind to move a boat",
   "la voile", "la vela", "a vela", "la vela", "das Segel", "парус", "شراع", "帆"),
 "oar": e("noun", "a long pole with a flat end, used to row a boat",
   "la rame", "el remo", "o remo", "il remo", "das Ruder", "весло", "مجداف", "桨"),
 "rope": e("noun", "thick, strong cord",
   "la corde", "la cuerda", "a corda", "la corda", "das Seil", "верёвка", "حبل", "绳子"),
 "lifeboat": e("noun", "a boat kept to rescue people in danger at sea",
   "le canot de sauvetage", "el bote salvavidas", "o barco salva-vidas",
   "la scialuppa di salvataggio", "das Rettungsboot", "спасательная шлюпка",
   "قارب النجاة", "救生艇"),
 "wrecker": e("noun", "a person who makes ships crash to steal from them",
   "le naufrageur", "el raquero", "o saqueador de naufrágios", "il predone di relitti",
   "der Strandräuber", "грабитель судов", "ناهب السفن", "劫掠沉船者"),
 "oilskin": e("noun", "a heavy waterproof coat for bad weather at sea",
   "le ciré", "el impermeable", "a capa impermeável", "la cerata", "das Ölzeug",
   "непромокаемый плащ", "معطف مشمّع", "油布雨衣"),
 "barrel": e("noun", "a large round wooden or metal container",
   "le tonneau", "el barril", "o barril", "il barile", "das Fass", "бочка", "برميل", "桶"),
 "watch": e("noun", "a period of keeping guard, awake and alert",
   "la veille", "la guardia", "a vigília", "la veglia", "die Wache", "вахта", "مناوبة", "值守"),
 "cottage": e("noun", "a small, simple house",
   "la chaumière", "la cabaña", "a casinha", "il cottage", "das Häuschen",
   "домик", "كوخ", "小屋"),
 "gallery": e("noun", "the narrow walkway around the top of a lighthouse",
   "la galerie", "la galería", "a galeria", "la galleria", "der Umgang",
   "галерея", "شُرفة", "回廊"),
 "matches": e("noun", "small sticks that make fire when struck",
   "les allumettes", "los fósforos", "os fósforos", "i fiammiferi", "die Streichhölzer",
   "спички", "أعواد ثقاب", "火柴"),

 # --- the body & action in the storm ---
 "cold": e("adjective", "having a low temperature; not warm",
   "froid", "frío", "frio", "freddo", "kalt", "холодный", "بارد", "冷的"),
 "rain": e("noun", "water falling from the clouds",
   "la pluie", "la lluvia", "a chuva", "la pioggia", "der Regen", "дождь", "مطر", "雨"),
 "climb": e("verb", "to go up, using effort",
   "grimper", "subir", "subir", "arrampicarsi", "klettern", "взбираться", "يتسلّق", "攀爬"),
 "wade": e("verb", "to walk through water",
   "patauger", "vadear", "vadear", "guadare", "waten", "брести", "يخوض", "涉水"),
 "cling": e("verb", "to hold on very tightly",
   "s'accrocher", "aferrarse", "agarrar-se", "aggrapparsi", "sich klammern",
   "цепляться", "يتشبّث", "紧抓"),
 "gasp": e("verb", "to breathe in suddenly and hard",
   "haleter", "jadear", "arquejar", "ansimare", "keuchen", "задыхаться", "يلهث", "喘气"),
 "huddle": e("verb", "to crowd close together for warmth or safety",
   "se blottir", "acurrucarse", "aconchegar-se", "rannicchiarsi", "sich zusammendrängen",
   "жаться", "يتلاصق", "挤作一团"),
 "shiver": e("verb", "to shake because you are cold or afraid",
   "frissonner", "temblar", "tremer", "rabbrividire", "zittern", "дрожать", "يرتجف", "发抖"),
 "tangle": e("verb", "to twist together into a knot that is hard to undo",
   "emmêler", "enredar", "emaranhar", "aggrovigliare", "verwickeln",
   "запутывать", "يتشابك", "缠住"),
 "coat": e("noun", "a warm piece of clothing worn on top",
   "le manteau", "el abrigo", "o casaco", "il cappotto", "der Mantel", "пальто", "معطف", "外套"),
 "soak": e("verb", "to make completely wet",
   "tremper", "empapar", "ensopar", "inzuppare", "durchnässen", "промокать", "يبلّل تمامًا", "浸湿"),

 # --- other high-tap content words ---
 "storm-lamp": e("noun", "a lamp built to keep burning in wind and rain",
   "la lampe-tempête", "el farol de tormenta", "o candeeiro de tempestade",
   "la lampada da tempesta", "die Sturmlaterne", "штормовой фонарь", "مصباح العاصفة", "防风灯"),
 "roar": e("verb", "to make a long, deep, loud sound",
   "rugir", "rugir", "rugir", "ruggire", "tosen", "реветь", "يزأر", "咆哮"),
 "swamp": e("verb", "to fill with water and sink",
   "submerger", "inundar", "inundar", "sommergere", "überfluten",
   "затоплять", "يغمر", "淹没"),
 "stove-in": e("adjective", "smashed inward, as a broken hull",
   "défoncé", "destrozado", "arrombado", "sfondato", "eingeschlagen",
   "проломленный", "محطّم", "撞破的"),
 "steer": e("verb", "to guide the direction of a boat or vehicle",
   "diriger", "gobernar", "dirigir", "governare", "steuern", "править", "يوجّه", "掌舵"),
 "spare": e("verb", "to give something you can do without",
   "accorder", "ofrecer", "ceder", "concedere", "erübrigen", "уделять", "يجود بـ", "分出"),
 "trim": e("verb", "to make neat by cutting a little; to adjust a wick",
   "tailler", "recortar", "aparar", "regolare", "stutzen", "подрезать", "يقلّم", "修剪"),
 "gutter": e("verb", "(of a flame) to burn low and unsteadily",
   "vaciller", "titilar", "bruxulear", "tremolare", "flackern",
   "мигать", "يخفت", "摇曳将灭"),

 # --- coverage top-up (words the prose leans on) ---
 "hull": e("noun", "the main body of a boat or ship",
   "la coque", "el casco", "o casco", "lo scafo", "der Rumpf", "корпус", "بدن السفينة", "船体"),
 "wreckage": e("noun", "the broken pieces left after a wreck",
   "les débris", "los restos", "os destroços", "i rottami", "die Trümmer",
   "обломки", "حطام", "残骸"),
 "coax": e("verb", "to gently and patiently get something to work or move",
   "amadouer", "engatusar", "persuadir", "blandire", "locken", "уговаривать", "يستدرج", "耐心哄弄"),
 "flicker": e("verb", "to shine or burn unsteadily",
   "vaciller", "parpadear", "tremeluzir", "tremolare", "flackern",
   "мерцать", "يومض", "闪烁"),
 "feed": e("verb", "to give something what it needs to keep going",
   "alimenter", "alimentar", "alimentar", "alimentare", "nähren",
   "питать", "يغذّي", "供给"),
 "ease": e("verb", "to become less strong or less painful",
   "se calmer", "amainar", "abrandar", "attenuarsi", "nachlassen",
   "стихать", "يخفّ", "减弱"),
 "swing": e("verb", "to move back and forth, or round, from a fixed point",
   "balancer", "balancear", "balançar", "oscillare", "schwingen",
   "качать", "يتأرجح", "摆动"),
 "slam": e("verb", "to hit or shut with great force and noise",
   "claquer", "golpear", "bater com força", "sbattere", "schlagen",
   "ударять", "يصفق بعنف", "猛击"),
 "struggle": e("verb", "to fight hard against difficulty",
   "lutter", "forcejear", "debater-se", "lottare", "kämpfen",
   "бороться", "يكافح", "挣扎"),
 "batter": e("verb", "to hit again and again, hard",
   "battre", "azotar", "fustigar", "battere", "prügeln",
   "колотить", "يلطم", "猛烈拍打"),
 "spread": e("verb", "to reach or move over a wider area",
   "se répandre", "extenderse", "espalhar-se", "diffondersi", "sich ausbreiten",
   "распространяться", "ينتشر", "蔓延"),
 "foul": e("adjective", "dirty or spoiled; unpleasant",
   "souillé", "sucio", "imundo", "sporco", "verdorben", "испорченный", "فاسد", "污浊的"),
 "heave": e("verb", "to lift, pull or throw with great effort",
   "hisser", "levantar con esfuerzo", "içar", "sollevare a fatica", "wuchten",
   "тянуть с усилием", "يجرّ بجهد", "用力拉"),
 "onto": e("preposition", "to a position on the top or surface of",
   "sur", "sobre", "para cima de", "su", "auf", "на", "على", "到…上"),
}


def main():
    src = {}
    for f in SRCS:
        src.update(json.load(open(f, encoding="utf-8"))["lexicon"]["entries"])
    book = json.load(open(EP5, encoding="utf-8"))
    entries, missing = {}, []
    for w in REUSE:
        if w in src:
            entries[w] = src[w]
        else:
            missing.append(w)
    for w, v in NEW.items():
        entries[w.strip()] = v
    book["lexicon"]["entries"] = dict(sorted(entries.items()))
    json.dump(book, open(EP5, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"Lexicon written: {len(entries)} entries "
          f"({len([w for w in REUSE if w in src])} reused, {len(NEW)} new).")
    if missing:
        print("WARNING reuse words not in books 1/3/4:", ", ".join(missing))


if __name__ == "__main__":
    main()
