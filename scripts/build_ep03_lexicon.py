#!/usr/bin/env python3
"""Phase 4: build First Light's embedded lexicon.

Words shared with book 1 reuse its reviewed-draft glosses (dropping any whose sense differs
here); new subject words (cold, snow, light, heat, the town and the crisis) get fresh draft
glosses in English + 8 languages. Machine-drafted; native review (phase 5) finalises them.

Writes the merged lexicon into content/episode-03.json's `lexicon.entries`.
Run: python3 scripts/build_ep03_lexicon.py
"""
import json, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
EP1 = os.path.join(ROOT, "content", "episode-01.json")
EP3 = os.path.join(ROOT, "content", "episode-03.json")

REUSE = [
    "afford", "altogether", "anyway", "arrow", "ashamed", "bother", "breath", "brush",
    "builder", "cleaner", "drag", "dust", "exhausted", "faded", "feet", "flask", "freeze",
    "further", "glad", "glance", "glow", "halfway", "haul", "heavy", "inner", "neither",
    "nerve", "otherwise", "pale", "photograph", "queue", "realise", "reasonable", "refuse",
    "settle", "somehow", "steady", "survive", "torn", "truth", "useless", "warmth", "wrap",
]

def e(pos, en, fr, es, pt, it, de, ru, ar, zh):
    return {"pos": pos, "en": en, "fr": fr, "es": es, "pt": pt, "it": it,
            "de": de, "ru": ru, "ar": ar, "zh": zh}

NEW = {
 # --- cold, snow, weather ---
 "frost": e("noun", "a thin white layer of ice that forms in the cold",
   "le givre", "la escarcha", "a geada", "la brina", "der Frost", "иней", "صقيع", "霜"),
 "frozen": e("adjective", "turned hard by cold; covered in ice",
   "gelé", "congelado", "congelado", "gelato", "gefroren", "замёрзший", "متجمد", "结冰的"),
 "ice": e("noun", "water that has frozen hard and solid",
   "la glace", "el hielo", "o gelo", "il ghiaccio", "das Eis", "лёд", "جليد", "冰"),
 "freezing": e("adjective", "extremely cold",
   "glacial", "helador", "gélido", "gelido", "eiskalt", "ледяной", "متجمد البرودة", "极冷的"),
 "shiver": e("verb", "to shake a little because you are cold or afraid",
   "frissonner", "tiritar", "tremer", "rabbrividire", "zittern", "дрожать", "يرتجف", "发抖"),
 "numb": e("adjective", "unable to feel, usually from cold",
   "engourdi", "entumecido", "dormente", "intorpidito", "taub", "онемевший", "مخدّر", "麻木的"),
 "bitter": e("adjective", "(of cold) very sharp and hard to bear",
   "mordant", "glacial", "cortante", "pungente", "beißend", "пронизывающий", "قارس", "刺骨的"),
 "thaw": e("verb", "to become warmer and less frozen",
   "dégeler", "descongelarse", "descongelar", "sgelare", "auftauen", "оттаивать", "يذوب", "解冻"),
 "snow": e("noun", "soft white flakes of frozen water that fall from the sky",
   "la neige", "la nieve", "a neve", "la neve", "der Schnee", "снег", "ثلج", "雪"),

 # --- light & heat ---
 "candle": e("noun", "a stick of wax with a string that burns to give light",
   "la bougie", "la vela", "a vela", "la candela", "die Kerze", "свеча", "شمعة", "蜡烛"),
 "candlelight": e("noun", "the soft light made by a candle",
   "la lueur des bougies", "la luz de las velas", "a luz das velas", "il lume di candela",
   "das Kerzenlicht", "свет свечи", "ضوء الشمعة", "烛光"),
 "lantern": e("noun", "a light inside a cover, made to carry",
   "la lanterne", "el farol", "a lanterna", "la lanterna", "die Laterne", "фонарь", "فانوس", "灯笼"),
 "torch": e("noun", "a small electric light you hold in your hand",
   "la lampe de poche", "la linterna", "a lanterna de mão", "la torcia", "die Taschenlampe",
   "фонарик", "مصباح يدوي", "手电筒"),
 "flame": e("noun", "the bright hot part of a fire",
   "la flamme", "la llama", "a chama", "la fiamma", "die Flamme", "пламя", "لهب", "火焰"),
 "heater": e("noun", "a machine that makes a room warm",
   "le radiateur", "el calefactor", "o aquecedor", "la stufa", "das Heizgerät",
   "обогреватель", "مدفأة", "取暖器"),
 "paraffin": e("noun", "an oil burned in some heaters and lamps",
   "le pétrole lampant", "la parafina", "a parafina", "la paraffina", "das Petroleum",
   "керосин", "الكيروسين", "煤油"),
 "fuel": e("noun", "something burned to make heat or power",
   "le carburant", "el combustible", "o combustível", "il combustibile", "der Brennstoff",
   "топливо", "وقود", "燃料"),
 "stove": e("noun", "a small machine you cook on or heat a room with",
   "le réchaud", "el hornillo", "o fogão", "il fornello", "der Ofen", "печка", "موقد", "炉子"),
 "generator": e("noun", "a machine that makes electricity",
   "le générateur", "el generador", "o gerador", "il generatore", "der Generator",
   "генератор", "مولّد", "发电机"),
 "electricity": e("noun", "the power that runs lights and machines",
   "l'électricité", "la electricidad", "a eletricidade", "l'elettricità", "der Strom",
   "электричество", "كهرباء", "电"),
 "wire": e("noun", "a thin metal line that carries electricity",
   "le fil", "el cable", "o fio", "il filo", "der Draht", "провод", "سلك", "电线"),

 # --- the town & the crisis ---
 "crew": e("noun", "a group of people who work together",
   "l'équipe", "la cuadrilla", "a equipa", "la squadra", "die Mannschaft",
   "бригада", "طاقم", "队伍"),
 "shopkeeper": e("noun", "a person who owns or runs a shop",
   "le commerçant", "el tendero", "o lojista", "il negoziante", "der Ladenbesitzer",
   "лавочник", "صاحب المتجر", "店主"),
 "neighbour": e("noun", "a person who lives near you",
   "le voisin", "el vecino", "o vizinho", "il vicino", "der Nachbar", "сосед", "جار", "邻居"),
 "signpost": e("noun", "a sign that shows the way to a place",
   "le panneau", "el poste indicador", "a placa de sinalização", "il cartello", "der Wegweiser",
   "указатель", "لافتة إرشادية", "路标"),
 "slope": e("noun", "ground that goes up or down at an angle",
   "la pente", "la cuesta", "a encosta", "il pendio", "der Hang", "склон", "منحدر", "斜坡"),
 "hill": e("noun", "a high piece of land, smaller than a mountain",
   "la colline", "la colina", "a colina", "la collina", "der Hügel", "холм", "تلة", "小山"),
 "doorway": e("noun", "the open space where a door is",
   "l'embrasure de la porte", "el umbral", "o vão da porta", "la soglia", "die Türöffnung",
   "дверной проём", "مدخل الباب", "门口"),
 "roof": e("noun", "the cover on top of a building",
   "le toit", "el tejado", "o telhado", "il tetto", "das Dach", "крыша", "سقف", "屋顶"),
 "shed": e("noun", "a small wooden building for storing things",
   "la remise", "el cobertizo", "o galpão", "il capanno", "der Schuppen", "сарай", "سقيفة", "棚子"),
 "ambulance": e("noun", "a vehicle that takes ill people to hospital",
   "l'ambulance", "la ambulancia", "a ambulância", "l'ambulanza", "der Krankenwagen",
   "скорая помощь", "سيارة إسعاف", "救护车"),
 "blocked": e("adjective", "closed off so nothing can pass",
   "bloqué", "bloqueado", "bloqueado", "bloccato", "blockiert", "перекрытый", "مسدود", "堵住的"),
 "scarf": e("noun", "a strip of cloth worn round the neck for warmth",
   "l'écharpe", "la bufanda", "o cachecol", "la sciarpa", "der Schal", "шарф", "وشاح", "围巾"),
 "gloves": e("noun", "coverings that keep the hands warm",
   "les gants", "los guantes", "as luvas", "i guanti", "die Handschuhe", "перчатки", "قفازات", "手套"),
 "blanket": e("noun", "a thick cover to keep you warm",
   "la couverture", "la manta", "o cobertor", "la coperta", "die Decke", "одеяло", "بطانية", "毯子"),
 "wool": e("noun", "the soft warm fibre from a sheep, used for clothes",
   "la laine", "la lana", "a lã", "la lana", "die Wolle", "шерсть", "صوف", "羊毛"),
 "gear": e("noun", "the equipment you need for a job or activity",
   "l'équipement", "el equipo", "o equipamento", "l'attrezzatura", "die Ausrüstung",
   "снаряжение", "معدات", "装备"),
 "shelter": e("noun", "a safe place out of the cold or danger",
   "l'abri", "el refugio", "o abrigo", "il riparo", "der Unterschlupf", "укрытие", "مأوى", "避难所"),

 # --- money & the scam ---
 "cash": e("noun", "money in coins and notes",
   "l'argent liquide", "el efectivo", "o dinheiro", "i contanti", "das Bargeld",
   "наличные", "نقد", "现金"),
 "robbery": e("noun", "the crime of taking money unfairly or by force",
   "le vol", "el robo", "o roubo", "la rapina", "der Raub", "грабёж", "سرقة", "抢劫"),
 "cheat": e("verb", "to trick someone, especially to take their money",
   "escroquer", "engañar", "enganar", "imbrogliare", "betrügen", "обманывать", "يغش", "欺骗"),
 "fleece": e("verb", "to charge someone far too much money",
   "arnaquer", "desplumar", "depenar", "spennare", "abzocken", "обдирать", "يسلب", "宰客"),
 "refund": e("noun", "money given back to you",
   "le remboursement", "el reembolso", "o reembolso", "il rimborso", "die Rückerstattung",
   "возврат денег", "استرداد", "退款"),
 "junk": e("noun", "worthless, useless things",
   "la camelote", "la chatarra", "a tralha", "la robaccia", "der Schrott", "хлам", "خردة", "破烂"),
 "hook": e("noun", "a hidden trap in something that looks like help",
   "le piège", "el anzuelo", "o anzol", "l'amo", "der Haken", "крючок", "خطاف", "圈套"),
 "trick": e("noun", "a clever act meant to fool or cheat someone",
   "le tour", "el truco", "o truque", "il trucco", "der Trick", "уловка", "خدعة", "把戏"),

 # --- the body in the cold ---
 "chest": e("noun", "the front of the body between neck and stomach; the lungs",
   "la poitrine", "el pecho", "o peito", "il petto", "die Brust", "грудь", "صدر", "胸口"),
 "bone": e("noun", "one of the hard parts inside the body",
   "l'os", "el hueso", "o osso", "l'osso", "der Knochen", "кость", "عظم", "骨头"),
 "knee": e("noun", "the joint in the middle of the leg",
   "le genou", "la rodilla", "o joelho", "il ginocchio", "das Knie", "колено", "ركبة", "膝盖"),
 "wrist": e("noun", "the joint between the hand and the arm",
   "le poignet", "la muñeca", "o pulso", "il polso", "das Handgelenk", "запястье", "معصم", "手腕"),
 "collar": e("noun", "the part of a coat or shirt around the neck",
   "le col", "el cuello", "a gola", "il colletto", "der Kragen", "воротник", "ياقة", "衣领"),
 "teeth": e("noun", "the hard white parts in the mouth used to bite",
   "les dents", "los dientes", "os dentes", "i denti", "die Zähne", "зубы", "أسنان", "牙齿"),
 "ache": e("verb", "to hurt with a dull, steady pain",
   "faire mal", "doler", "doer", "dolere", "schmerzen", "ныть", "يؤلم", "疼痛"),
 "breathing": e("noun", "the act of taking air in and out",
   "la respiration", "la respiración", "a respiração", "il respiro", "die Atmung",
   "дыхание", "التنفس", "呼吸"),

 # --- verbs ---
 "weigh": e("verb", "to think carefully about something before deciding",
   "peser", "sopesar", "ponderar", "soppesare", "abwägen", "взвешивать", "يزن", "权衡"),
 "gather": e("verb", "to bring people or things together",
   "rassembler", "reunir", "juntar", "radunare", "sammeln", "собирать", "يجمع", "聚集"),
 "rally": e("verb", "to bring people together to help or act",
   "rallier", "reunir", "mobilizar", "radunare", "zusammenrufen", "сплотить", "يحشد", "召集"),
 "scramble": e("verb", "to move quickly and with difficulty, using hands and feet",
   "se démener", "trepar a gatas", "trepar às pressas", "arrampicarsi", "sich abmühen",
   "карабкаться", "يتسلق بصعوبة", "手脚并用地爬"),
 "crawl": e("verb", "to move slowly on hands and knees",
   "ramper", "gatear", "rastejar", "strisciare", "kriechen", "ползти", "يزحف", "爬行"),
 "grip": e("verb", "to hold something very tightly",
   "agripper", "agarrar", "agarrar", "afferrare", "packen", "хватать", "يمسك بإحكام", "紧握"),
 "cling": e("verb", "to hold on tightly and not let go",
   "s'accrocher", "aferrarse", "agarrar-se", "aggrapparsi", "sich klammern",
   "цепляться", "يتشبث", "紧抓"),
 "crunch": e("verb", "to make a sharp, crushing sound underfoot",
   "crisser", "crujir", "ranger", "scricchiolare", "knirschen", "хрустеть", "يطقطق", "嘎吱作响"),
 "groan": e("verb", "to make a long, low sound of strain or pain",
   "gémir", "gemir", "gemer", "gemere", "ächzen", "стонать", "يئنّ", "呻吟"),
 "kneel": e("verb", "to go down onto your knees",
   "s'agenouiller", "arrodillarse", "ajoelhar-se", "inginocchiarsi", "knien",
   "становиться на колени", "يركع", "跪下"),
 "fetch": e("verb", "to go and bring something back",
   "aller chercher", "traer", "ir buscar", "andare a prendere", "holen", "приносить", "يحضر", "去拿"),
 "manage": e("verb", "to cope, or to succeed in doing something hard",
   "se débrouiller", "arreglárselas", "arranjar-se", "cavarsela", "zurechtkommen",
   "справляться", "يتدبّر", "应付"),
 "ignore": e("verb", "to take no notice of something",
   "ignorer", "ignorar", "ignorar", "ignorare", "ignorieren", "игнорировать", "يتجاهل", "无视"),
 "blame": e("verb", "to say that someone is at fault",
   "blâmer", "culpar", "culpar", "incolpare", "beschuldigen", "винить", "يلوم", "责怪"),
 "pile": e("verb", "to put a lot of things on top of each other",
   "empiler", "amontonar", "amontoar", "ammucchiare", "stapeln", "наваливать", "يكوّم", "堆"),
 "shove": e("verb", "to push roughly",
   "pousser", "empujar", "empurrar", "spingere", "schubsen", "толкать", "يدفع بقوة", "猛推"),
 "whisper": e("verb", "to speak very softly",
   "chuchoter", "susurrar", "sussurrar", "sussurrare", "flüstern", "шептать", "يهمس", "低语"),
 "warn": e("verb", "to tell someone about a danger",
   "avertir", "advertir", "avisar", "avvertire", "warnen", "предупреждать", "يحذّر", "警告"),
 "spread": e("verb", "to move out over a wider area",
   "se répandre", "extenderse", "espalhar-se", "diffondersi", "sich ausbreiten",
   "распространяться", "ينتشر", "蔓延"),

 # --- adjectives ---
 "silent": e("adjective", "with no sound at all",
   "silencieux", "silencioso", "silencioso", "silenzioso", "still", "безмолвный", "صامت", "寂静的"),
 "solid": e("adjective", "hard and firm; safe to stand on",
   "solide", "sólido", "sólido", "solido", "fest", "твёрдый", "صلب", "结实的"),
 "scared": e("adjective", "afraid",
   "effrayé", "asustado", "assustado", "spaventato", "verängstigt", "испуганный", "خائف", "害怕的"),
 "frightened": e("adjective", "feeling fear; afraid",
   "apeuré", "asustado", "amedrontado", "impaurito", "verängstigt", "напуганный", "مذعور", "受惊的"),
 "soaked": e("adjective", "completely wet",
   "trempé", "empapado", "encharcado", "fradicio", "durchnässt", "промокший", "مبلل تمامًا", "湿透的"),
 "steep": e("adjective", "rising or falling sharply",
   "raide", "empinado", "íngreme", "ripido", "steil", "крутой", "شديد الانحدار", "陡的"),
 "tempting": e("adjective", "making you want it, even if it may be unwise",
   "tentant", "tentador", "tentador", "allettante", "verlockend", "заманчивый", "مغرٍ", "诱人的"),
 "stubborn": e("adjective", "not willing to change or give way",
   "têtu", "terco", "teimoso", "testardo", "stur", "упрямый", "عنيد", "固执的"),
 "hopeful": e("adjective", "feeling that good things may happen",
   "plein d'espoir", "esperanzado", "esperançoso", "speranzoso", "hoffnungsvoll",
   "полный надежды", "متفائل", "满怀希望的"),
 "brave": e("adjective", "ready to face danger or pain",
   "courageux", "valiente", "corajoso", "coraggioso", "mutig", "храбрый", "شجاع", "勇敢的"),
 "cruel": e("adjective", "causing pain to others without care",
   "cruel", "cruel", "cruel", "crudele", "grausam", "жестокий", "قاسٍ", "残忍的"),
 "rare": e("adjective", "not often found or seen",
   "rare", "raro", "raro", "raro", "selten", "редкий", "نادر", "稀有的"),
 "awkward": e("adjective", "hard to carry, hold or manage",
   "encombrant", "incómodo", "desajeitado", "scomodo", "sperrig", "неудобный", "صعب المناولة", "笨重的"),
 "shallow": e("adjective", "not deep",
   "peu profond", "poco profundo", "raso", "poco profondo", "flach", "неглубокий", "ضحل", "浅的"),
 "tight": e("adjective", "held firmly and closely",
   "serré", "apretado", "apertado", "stretto", "fest", "тугой", "محكم", "紧的"),
 "elderly": e("adjective", "old",
   "âgé", "anciano", "idoso", "anziano", "älter", "пожилой", "مسنّ", "年老的"),
 "uneasy": e("adjective", "worried that something is wrong",
   "mal à l'aise", "inquieto", "inquieto", "a disagio", "unbehaglich", "тревожный", "قلق", "不安的"),

 # --- other nouns ---
 "doubt": e("noun", "a feeling that something may not be true or right",
   "le doute", "la duda", "a dúvida", "il dubbio", "der Zweifel", "сомнение", "شك", "怀疑"),
 "panic": e("noun", "sudden strong fear that spreads fast",
   "la panique", "el pánico", "o pânico", "il panico", "die Panik", "паника", "ذعر", "恐慌"),
 "relief": e("noun", "the good feeling when worry or pain stops",
   "le soulagement", "el alivio", "o alívio", "il sollievo", "die Erleichterung",
   "облегчение", "راحة", "宽慰"),
 "safety": e("noun", "the state of being safe from harm",
   "la sécurité", "la seguridad", "a segurança", "la sicurezza", "die Sicherheit",
   "безопасность", "سلامة", "安全"),
 "loss": e("noun", "the fact of no longer having something",
   "la perte", "la pérdida", "a perda", "la perdita", "der Verlust", "потеря", "خسارة", "损失"),
 "punishment": e("noun", "something bad done to you for doing wrong",
   "la punition", "el castigo", "o castigo", "la punizione", "die Strafe", "наказание", "عقاب", "惩罚"),
 "lifetime": e("noun", "the whole length of a person's life",
   "la vie entière", "toda una vida", "uma vida inteira", "una vita intera", "das ganze Leben",
   "целая жизнь", "عمر كامل", "一辈子"),
 "rumour": e("noun", "a story people repeat that may not be true",
   "la rumeur", "el rumor", "o boato", "la voce", "das Gerücht", "слух", "شائعة", "谣言"),
 "advice": e("noun", "what someone tells you that you should do",
   "le conseil", "el consejo", "o conselho", "il consiglio", "der Rat", "совет", "نصيحة", "建议"),
 "path": e("noun", "a narrow way to walk along",
   "le sentier", "el sendero", "o caminho", "il sentiero", "der Pfad", "тропа", "مسار", "小路"),
 "figure": e("noun", "the shape of a person, seen from far off or in the dark",
   "la silhouette", "la figura", "a figura", "la figura", "die Gestalt", "фигура", "شبح", "身影"),
 "dawn": e("noun", "the first light of the morning",
   "l'aube", "el amanecer", "o amanhecer", "l'alba", "die Morgendämmerung", "рассвет", "الفجر", "黎明"),
 "spare": e("adjective", "kept extra, ready to be used if needed",
   "de rechange", "de repuesto", "sobressalente", "di riserva", "übrig",
   "запасной", "احتياطي", "备用的"),
 "sell": e("verb", "to give something in exchange for money",
   "vendre", "vender", "vender", "vendere", "verkaufen", "продавать", "يبيع", "卖"),
 "worst": e("adjective", "the most bad; least good of all",
   "le pire", "el peor", "o pior", "il peggiore", "der schlimmste", "худший", "الأسوأ", "最糟的"),

 # --- high-frequency content words the coverage pass flagged ---
 "battery": e("noun", "a small store of power for a torch or machine",
   "la pile", "la pila", "a pilha", "la pila", "die Batterie", "батарейка", "بطارية", "电池"),
 "headlight": e("noun", "a bright lamp on the front of a car or van",
   "le phare", "el faro", "o farol", "il faro", "der Scheinwerfer", "фара", "مصباح أمامي", "车头灯"),
 "child": e("noun", "a young person, not yet grown up",
   "l'enfant", "el niño", "a criança", "il bambino", "das Kind", "ребёнок", "طفل", "小孩"),
 "clever": e("adjective", "quick to understand; sometimes too smart for its own good",
   "malin", "astuto", "esperto", "astuto", "schlau", "хитрый", "ذكي", "精明的"),
 "foolish": e("adjective", "not sensible; likely to lead to trouble",
   "insensé", "insensato", "tolo", "sciocco", "töricht", "глупый", "أحمق", "愚蠢的"),
}


def main():
    ep1 = json.load(open(EP1, encoding="utf-8"))["lexicon"]["entries"]
    book = json.load(open(EP3, encoding="utf-8"))
    entries, missing = {}, []
    for w in REUSE:
        if w in ep1:
            entries[w] = ep1[w]
        else:
            missing.append(w)
    for w, v in NEW.items():
        entries[w.strip()] = v
    book["lexicon"]["entries"] = dict(sorted(entries.items()))
    json.dump(book, open(EP3, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"Lexicon written: {len(entries)} entries "
          f"({len([w for w in REUSE if w in ep1])} reused, {len(NEW)} new).")
    if missing:
        print("WARNING reuse words not in book 1:", ", ".join(missing))


if __name__ == "__main__":
    main()
