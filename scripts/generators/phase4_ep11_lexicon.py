#!/usr/bin/env python3
"""Phase 4: Moving Day (episode-11) lexicon. Reuses the everyday words The Interview
already defines (same translations) where they appear here, and adds the moving /
home / carrying vocabulary this book needs. Base-keyed; reader resolves inflection.
Run: python3 scripts/generators/phase4_ep11_lexicon.py"""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import build_book as bb

P11 = os.path.join(ROOT, "content", "episode-11.json")
P10 = os.path.join(ROOT, "content", "episode-10.json")
LANGS = ["fr", "es", "it", "de", "pt", "ru", "zh", "ar"]

# key: (pos, en, fr, es, it, de, pt, ru, zh, ar)
NEW = [
 ("ache", "verb", "to hurt with a dull, steady pain", "faire mal", "doler", "dolere", "schmerzen", "doer", "ныть", "隐隐作痛", "يؤلم"),
 ("alongside", "preposition", "next to; together with", "à côté de", "junto a", "accanto a", "neben", "ao lado de", "рядом с", "与……一起", "إلى جانب"),
 ("anyhow", "adverb", "in a careless, untidy way", "n'importe comment", "de cualquier manera", "alla rinfusa", "wie's gerade kommt", "de qualquer jeito", "кое-как", "胡乱地", "بأي شكل"),
 ("blanket", "noun", "a thick cover to keep warm", "couverture", "manta", "coperta", "Decke", "cobertor", "одеяло", "毯子", "بطانية"),
 ("box", "noun", "a container with stiff sides for packing", "carton", "caja", "scatola", "Karton", "caixa", "коробка", "箱子", "صندوق"),
 ("caretaker", "noun", "a person who looks after a building", "gardien", "conserje", "custode", "Hausmeister", "zelador", "смотритель", "看管人", "حارس"),
 ("carry", "verb", "to hold and move something", "porter", "llevar", "portare", "tragen", "carregar", "нести", "搬运", "يحمل"),
 ("chain", "noun", "a line of people passing things along", "chaîne", "cadena", "catena", "Kette", "corrente", "цепочка", "链条式传递", "سلسلة"),
 ("clap", "verb", "to pat warmly, as on the back", "taper", "dar palmadas", "dare una pacca", "klopfen", "dar tapinhas", "похлопать", "拍", "يربت"),
 ("couple", "noun", "two, or a few", "deux ou trois", "un par", "un paio", "ein paar", "um par", "пара", "几个", "اثنان"),
 ("cupboard", "noun", "a cabinet for storing things", "placard", "armario", "armadio", "Schrank", "armário", "шкаф", "橱柜", "خزانة"),
 ("damage", "noun", "harm done to something", "dégâts", "daños", "danni", "Schaden", "estragos", "повреждение", "损坏", "ضرر"),
 ("deposit", "noun", "money paid up front to hold a deal", "acompte", "señal", "caparra", "Anzahlung", "sinal", "задаток", "定金", "عربون"),
 ("dusk", "noun", "the dim light at the end of the day", "crépuscule", "anochecer", "crepuscolo", "Dämmerung", "anoitecer", "сумерки", "黄昏", "الغسق"),
 ("fade", "verb", "to grow slowly dimmer or weaker", "baisser", "apagarse", "svanire", "schwinden", "esvair-se", "угасать", "渐暗", "يخبو"),
 ("flat", "noun", "a set of rooms to live in; an apartment", "appartement", "piso", "appartamento", "Wohnung", "apartamento", "квартира", "公寓", "شقة"),
 ("footstep", "noun", "the sound of a foot on the ground", "pas", "paso", "passo", "Schritt", "passo", "шаг", "脚步声", "خطوة"),
 ("fraught", "adjective", "tense and close to going wrong", "tendu", "tenso", "teso", "angespannt", "tenso", "напряжённый", "紧张的", "متوتّر"),
 ("fret", "verb", "to worry over small things", "se tracasser", "inquietarse", "agitarsi", "sich sorgen", "afligir-se", "волноваться", "烦躁", "يقلق"),
 ("gate", "noun", "a door in a fence or wall", "portail", "verja", "cancello", "Tor", "portão", "ворота", "大门", "بوابة"),
 ("haul", "noun", "a long, hard stretch of carrying", "corvée", "trajín", "faticata", "Schufterei", "lida", "тяжёлая работа", "苦力活", "جهد شاق"),
 ("heavy", "adjective", "weighing a lot", "lourd", "pesado", "pesante", "schwer", "pesado", "тяжёлый", "重", "ثقيل"),
 ("hop", "verb", "to jump down lightly and quickly", "sauter", "bajar de un salto", "saltare giù", "springen", "saltar", "спрыгнуть", "跳下", "يقفز"),
 ("jumbled", "adjective", "mixed up and in no order", "en désordre", "revuelto", "alla rinfusa", "durcheinander", "desarrumado", "вперемешку", "杂乱的", "مبعثر"),
 ("kerb", "noun", "the edge of a pavement by the road", "bordure", "bordillo", "cordolo", "Bordstein", "meio-fio", "бордюр", "路缘", "حافة الرصيف"),
 ("kettle", "noun", "a pot for boiling water", "bouilloire", "hervidor", "bollitore", "Wasserkocher", "chaleira", "чайник", "水壶", "غلّاية"),
 ("key", "noun", "a metal thing that opens a lock", "clé", "llave", "chiave", "Schlüssel", "chave", "ключ", "钥匙", "مفتاح"),
 ("lift", "verb", "to raise something up", "soulever", "levantar", "sollevare", "heben", "levantar", "поднимать", "抬起", "يرفع"),
 ("load", "noun", "the things carried in one go", "chargement", "carga", "carico", "Ladung", "carga", "груз", "一趟货", "حمولة"),
 ("lurch", "verb", "to lean or swing suddenly", "basculer", "tambalearse", "sbandare", "schwanken", "cambalear", "накрениться", "猛地一晃", "يترنّح"),
 ("mate", "noun", "a friend", "pote", "amigo", "amico", "Kumpel", "amigo", "приятель", "伙计", "صاحب"),
 ("mover", "noun", "a person moving house", "déménageur", "persona que se muda", "chi trasloca", "Umziehender", "quem se muda", "переезжающий", "搬家的人", "من ينقل بيته"),
 ("neighbour", "noun", "a person who lives near you", "voisin", "vecino", "vicino", "Nachbar", "vizinho", "сосед", "邻居", "جار"),
 ("nightfall", "noun", "the moment darkness comes", "tombée de la nuit", "anochecer", "calar della notte", "Einbruch der Nacht", "cair da noite", "наступление ночи", "入夜", "حلول الليل"),
 ("overloaded", "adjective", "piled with too much to carry", "surchargé", "sobrecargado", "sovraccarico", "überladen", "sobrecarregado", "перегруженный", "超载的", "محمَّل بزيادة"),
 ("pack", "verb", "to put things into boxes or a van", "emballer", "empacar", "impacchettare", "packen", "empacotar", "упаковывать", "打包", "يحزم"),
 ("rail", "noun", "a bar for the hand on stairs", "rampe", "barandilla", "corrimano", "Geländer", "corrimão", "перила", "扶手", "درابزين"),
 ("rhythm", "noun", "a steady, repeating pattern of work", "rythme", "ritmo", "ritmo", "Rhythmus", "ritmo", "ритм", "节奏", "إيقاع"),
 ("roll", "verb", "to turn up (your sleeves) to work", "retrousser", "remangarse", "rimboccare", "hochkrempeln", "arregaçar", "засучивать", "卷起", "يشمّر"),
 ("sleeve", "noun", "the part of clothing for your arm", "manche", "manga", "manica", "Ärmel", "manga", "рукав", "袖子", "كُمّ"),
 ("smash", "verb", "to break into pieces", "fracasser", "destrozar", "fracassare", "zerschlagen", "espatifar", "разбить", "摔碎", "يحطّم"),
 ("sofa", "noun", "a long, soft seat for several people", "canapé", "sofá", "divano", "Sofa", "sofá", "диван", "沙发", "أريكة"),
 ("sore", "adjective", "painful, especially from effort", "endolori", "dolorido", "indolenzito", "wund", "dolorido", "ноющий", "酸痛的", "مؤلم"),
 ("stack", "verb", "to pile things on top of each other", "empiler", "apilar", "impilare", "stapeln", "empilhar", "складывать", "堆叠", "يكدّس"),
 ("stairwell", "noun", "the space the stairs run through", "cage d'escalier", "hueco de la escalera", "tromba delle scale", "Treppenhaus", "vão da escada", "лестничная клетка", "楼梯间", "بيت الدرج"),
 ("steep", "adjective", "rising sharply; hard to climb", "raide", "empinado", "ripido", "steil", "íngreme", "крутой", "陡", "شديد الانحدار"),
 ("stiffness", "noun", "being hard to bend or move", "raideur", "rigidez", "rigidità", "Steifheit", "rigidez", "скованность", "僵硬", "تيبّس"),
 ("strain", "noun", "the force of too much effort", "effort excessif", "esfuerzo", "sforzo", "Überanstrengung", "esforço", "перенапряжение", "过度用力", "إجهاد"),
 ("stuff", "noun", "things in general; belongings", "affaires", "cosas", "roba", "Zeug", "coisas", "вещи", "东西", "أغراض"),
 ("sway", "verb", "to move slowly from side to side", "osciller", "bambolearse", "oscillare", "schwanken", "balançar", "покачиваться", "摇晃", "يتمايل"),
 ("tape", "verb", "to seal with sticky tape", "scotcher", "precintar", "nastrare", "zukleben", "colar com fita", "заклеивать скотчем", "用胶带封", "يلصق بشريط"),
 ("tiredness", "noun", "the feeling of needing rest", "fatigue", "cansancio", "stanchezza", "Müdigkeit", "cansaço", "усталость", "疲惫", "تعب"),
 ("trolley", "noun", "a cart on wheels for carrying loads", "chariot", "carretilla", "carrello", "Sackkarre", "carrinho", "тележка", "手推车", "عربة"),
 ("tumble", "verb", "to fall suddenly and roll", "dégringoler", "caer rodando", "ruzzolare", "purzeln", "despencar", "катиться кувырком", "翻滚落下", "يتدحرج"),
 ("twinge", "verb", "to give a short, sharp pain", "élancer", "dar punzadas", "fitta", "zwicken", "dar pontadas", "кольнуть", "刺痛", "يومض ألماً"),
 ("van", "noun", "a covered truck for carrying goods", "camionnette", "furgoneta", "furgone", "Lieferwagen", "carrinha", "фургон", "厢式货车", "شاحنة صغيرة"),
 ("wardrobe", "noun", "a tall cupboard for hanging clothes", "armoire", "armario ropero", "guardaroba", "Kleiderschrank", "guarda-roupa", "шкаф для одежды", "衣柜", "خزانة ملابس"),
 ("wedge", "verb", "to force tightly into a space", "coincer", "encajar", "incastrare", "einklemmen", "entalar", "втиснуть", "楔入", "يحشر"),
 ("wobble", "verb", "to move unsteadily from side to side", "vaciller", "tambalearse", "traballare", "wackeln", "oscilar", "шататься", "摇晃", "يترنّح"),
 ("wrap", "verb", "to cover by folding around", "envelopper", "envolver", "avvolgere", "einwickeln", "embrulhar", "заворачивать", "裹", "يلفّ"),
 ("pitch", "verb", "to join in and help with work", "mettre la main à la pâte", "arrimar el hombro", "dare una mano", "mit anpacken", "dar uma mãozinha", "подключиться", "出力帮忙", "يشارك في العمل"),
 ("heaviest", "adjective", "the most heavy of all", "le plus lourd", "el más pesado", "il più pesante", "am schwersten", "o mais pesado", "самый тяжёлый", "最重的", "الأثقل"),
 # --- a few more everyday words, for ~250 parity ---
 ("settle", "verb", "to make someone comfortable and calm", "installer", "acomodar", "sistemare", "unterbringen", "acomodar", "устраивать", "安顿", "يُرِيح"),
 ("lower", "verb", "to let something down slowly", "descendre", "bajar", "abbassare", "herablassen", "baixar", "опускать", "放低", "يُنزل"),
 ("shoulder", "noun", "the top of the arm, used to carry", "épaule", "hombro", "spalla", "Schulter", "ombro", "плечо", "肩膀", "كتف"),
 ("bare", "adjective", "empty; with nothing in or on it", "nu", "vacío", "spoglio", "leer", "vazio", "пустой", "空荡荡", "فارغ"),
 ("spare", "adjective", "extra; not being used", "de rechange", "de sobra", "in più", "übrig", "de reserva", "запасной", "多余的", "احتياطي"),
 ("worn", "adjective", "tired out; or old and rubbed smooth", "épuisé", "agotado", "sfinito", "erschöpft", "esgotado", "измотанный", "疲惫；磨旧的", "منهك"),
 ("strong", "adjective", "having great physical power", "fort", "fuerte", "forte", "stark", "forte", "сильный", "强壮", "قوي"),
 ("trip", "noun", "one journey there and back", "aller-retour", "viaje", "viaggio", "Gang", "viagem", "ходка", "一趟", "رحلة"),
 ("knock", "verb", "to hit a door to be answered", "frapper", "llamar", "bussare", "klopfen", "bater", "стучать", "敲", "يطرق"),
 ("lend", "verb", "to let someone use what is yours", "prêter", "prestar", "prestare", "leihen", "emprestar", "одолжить", "借给", "يُعير"),
 ("raw", "adjective", "sore and rubbed from use", "à vif", "en carne viva", "scorticato", "wund", "em carne viva", "стёртый", "磨破的", "مسلوخ"),
 ("prop", "verb", "to hold something open or up", "caler", "apuntalar", "puntellare", "aufstützen", "escorar", "подпирать", "支住", "يسند"),
 ("winded", "adjective", "out of breath", "essoufflé", "sin aliento", "senza fiato", "außer Atem", "sem fôlego", "запыхавшийся", "喘不过气", "لاهث"),
 ("wince", "verb", "to flinch from sudden pain", "grimacer", "hacer una mueca", "trasalire", "zusammenzucken", "estremecer", "морщиться", "龇牙皱眉", "يجفل"),
 ("lap", "noun", "the top of the legs when seated", "genoux", "regazo", "grembo", "Schoß", "colo", "колени", "膝上", "حِضن"),
 ("store", "noun", "a cupboard or room for keeping things", "réserve", "trastero", "ripostiglio", "Abstellraum", "arrecadação", "кладовая", "储物间", "مخزن"),
 ("patient", "adjective", "able to wait calmly", "patient", "paciente", "paziente", "geduldig", "paciente", "терпеливый", "耐心的", "صبور"),
]


def main():
    d11 = json.load(open(P11, encoding="utf-8"))
    src = json.load(open(P10, encoding="utf-8"))["lexicon"]["entries"]
    toks = set()
    for n in d11["nodes"]:
        for lvl in ("A2", "B1", "B2"):
            for w in bb.words(n["text"][lvl]):
                toks.add(w.lower())
            for c in n.get("choices", []):
                for w in bb.words(c["text"][lvl]):
                    toks.add(w.lower())
    entries = {}
    for k, v in src.items():
        if any(bb.resolve(t, {k}) == k for t in toks):
            entries[k] = v
    for row in NEW:
        key, pos, en = row[0], row[1], row[2]
        e = {"pos": pos, "en": en}
        for lang, val in zip(LANGS, row[3:]):
            e[lang] = val
        entries[key] = e
    out = {k: entries[k] for k in sorted(entries)}
    d11["lexicon"] = {
        "_comment": "Moving Day's chosen lexicon. Everyday home, moving, carrying and "
                    "letting-go vocabulary — shared everyday words plus the moving set. "
                    "Base-keyed; the reader resolves regular inflection.",
        "entries": out,
    }
    json.dump(d11, open(P11, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"lexicon: {len(out)} entries ({len(out)-len(NEW)} reused + {len(NEW)} new) x {len(LANGS)+1} langs")


if __name__ == "__main__":
    main()
