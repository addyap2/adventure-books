#!/usr/bin/env python3
"""Even out lexicon depth: enrich First Light (episode-03) toward ~250 entries.

Adds concrete, high-tap content words (nouns, common verbs, adjectives) that recur
in the prose but weren't yet glossed — so a learner can tap them. Base-keyed; the
reader resolves inflections. Only words that actually appear are added. Idempotent.

Run: python3 scripts/enrich_ep03_lexicon.py
"""
import json, os

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "episode-03.json")
LANGS = ["fr", "es", "pt", "it", "de", "ru", "ar", "zh"]

# base -> (pos, en, fr, es, pt, it, de, ru, ar, zh)
NEW = {
 # --- nouns ---
 "night": ("noun", "the dark hours when the sun is down", "la nuit", "la noche", "a noite", "la notte", "die Nacht", "ночь", "الليل", "夜晚"),
 "light": ("noun", "brightness that lets you see", "la lumière", "la luz", "a luz", "la luce", "das Licht", "свет", "ضوء", "光"),
 "heat": ("noun", "the quality of being hot; warmth", "la chaleur", "el calor", "o calor", "il calore", "die Wärme", "тепло", "حرارة", "热"),
 "fire": ("noun", "burning flames that give heat and light", "le feu", "el fuego", "o fogo", "il fuoco", "das Feuer", "огонь", "نار", "火"),
 "window": ("noun", "a glass opening in a wall", "la fenêtre", "la ventana", "a janela", "la finestra", "das Fenster", "окно", "نافذة", "窗户"),
 "door": ("noun", "the way in and out of a room", "la porte", "la puerta", "a porta", "la porta", "die Tür", "дверь", "باب", "门"),
 "house": ("noun", "a building where people live", "la maison", "la casa", "a casa", "la casa", "das Haus", "дом", "منزل", "房子"),
 "room": ("noun", "a space inside a building with walls", "la pièce", "la habitación", "o quarto", "la stanza", "das Zimmer", "комната", "غرفة", "房间"),
 "town": ("noun", "a place with houses, shops and streets", "la ville", "el pueblo", "a cidade", "la città", "die Stadt", "городок", "بلدة", "镇子"),
 "street": ("noun", "a road in a town with buildings", "la rue", "la calle", "a rua", "la strada", "die Straße", "улица", "شارع", "街道"),
 "road": ("noun", "a way for cars and people to travel", "la route", "la carretera", "a estrada", "la strada", "die Straße", "дорога", "طريق", "路"),
 "river": ("noun", "a wide stream of water", "la rivière", "el río", "o rio", "il fiume", "der Fluss", "река", "نهر", "河"),
 "shop": ("noun", "a place where you buy things", "le magasin", "la tienda", "a loja", "il negozio", "der Laden", "магазин", "متجر", "商店"),
 "coat": ("noun", "a warm piece of clothing for outdoors", "le manteau", "el abrigo", "o casaco", "il cappotto", "der Mantel", "пальто", "معطف", "外套"),
 "soup": ("noun", "a hot liquid food", "la soupe", "la sopa", "a sopa", "la zuppa", "die Suppe", "суп", "حساء", "汤"),
 "money": ("noun", "coins and notes you pay with", "l'argent", "el dinero", "o dinheiro", "il denaro", "das Geld", "деньги", "مال", "钱"),
 "water": ("noun", "the clear liquid we drink", "l'eau", "el agua", "a água", "l'acqua", "das Wasser", "вода", "ماء", "水"),
 "fear": ("noun", "the feeling of being afraid", "la peur", "el miedo", "o medo", "la paura", "die Angst", "страх", "خوف", "恐惧"),
 "crowd": ("noun", "a large group of people together", "la foule", "la multitud", "a multidão", "la folla", "die Menge", "толпа", "حشد", "人群"),
 "voice": ("noun", "the sound you make when you speak", "la voix", "la voz", "a voz", "la voce", "die Stimme", "голос", "صوت", "嗓音"),
 "boot": ("noun", "a strong shoe that covers the ankle", "la botte", "la bota", "a bota", "lo stivale", "der Stiefel", "сапог", "حذاء طويل", "靴子"),
 "corner": ("noun", "where two walls or streets meet", "le coin", "la esquina", "a esquina", "l'angolo", "die Ecke", "угол", "زاوية", "角落"),
 "heart": ("noun", "the organ that pumps blood; your feelings", "le cœur", "el corazón", "o coração", "il cuore", "das Herz", "сердце", "قلب", "心"),
 "floor": ("noun", "the surface you stand on indoors", "le sol", "el suelo", "o chão", "il pavimento", "der Boden", "пол", "أرضية", "地板"),
 "wall": ("noun", "the side of a room or building", "le mur", "la pared", "a parede", "il muro", "die Wand", "стена", "جدار", "墙"),
 "lump": ("noun", "a small solid piece", "le morceau", "el trozo", "o pedaço", "il pezzo", "der Klumpen", "кусок", "كتلة", "块"),
 "metal": ("noun", "a hard material like iron or steel", "le métal", "el metal", "o metal", "il metallo", "das Metall", "металл", "معدن", "金属"),
 "wheel": ("noun", "a round part that turns to move something", "la roue", "la rueda", "a roda", "la ruota", "das Rad", "колесо", "عجلة", "轮子"),
 "stranger": ("noun", "a person you do not know", "l'inconnu", "el desconocido", "o desconhecido", "lo sconosciuto", "der Fremde", "незнакомец", "غريب", "陌生人"),
 "gift": ("noun", "something you give to someone", "le cadeau", "el regalo", "o presente", "il regalo", "das Geschenk", "подарок", "هدية", "礼物"),
 "power": ("noun", "electricity; strength or control", "le courant", "la electricidad", "a energia", "la corrente", "der Strom", "электричество", "الكهرباء", "电力"),
 "finger": ("noun", "one of the parts of your hand", "le doigt", "el dedo", "o dedo", "il dito", "der Finger", "палец", "إصبع", "手指"),
 "lamp": ("noun", "a device that gives light", "la lampe", "la lámpara", "o candeeiro", "la lampada", "die Lampe", "лампа", "مصباح", "灯"),
 "bird": ("noun", "an animal with feathers that can fly", "l'oiseau", "el pájaro", "o pássaro", "l'uccello", "der Vogel", "птица", "طائر", "鸟"),
 "truck": ("noun", "a large vehicle for carrying loads", "le camion", "el camión", "o camião", "il camion", "der Lastwagen", "грузовик", "شاحنة", "卡车"),
 "phone": ("noun", "a device for talking to someone far away", "le téléphone", "el teléfono", "o telefone", "il telefono", "das Telefon", "телефон", "هاتف", "电话"),
 "shoulder": ("noun", "where the arm joins the body", "l'épaule", "el hombro", "o ombro", "la spalla", "die Schulter", "плечо", "كتف", "肩膀"),
 "baby": ("noun", "a very young child", "le bébé", "el bebé", "o bebé", "il bambino", "das Baby", "младенец", "رضيع", "婴儿"),
 "brother": ("noun", "a boy or man with the same parents as you", "le frère", "el hermano", "o irmão", "il fratello", "der Bruder", "брат", "أخ", "兄弟"),
 "sister": ("noun", "a girl or woman with the same parents as you", "la sœur", "la hermana", "a irmã", "la sorella", "die Schwester", "сестра", "أخت", "姐妹"),
 # --- verbs ---
 "knock": ("verb", "to hit a door to be let in", "frapper", "llamar a la puerta", "bater à porta", "bussare", "klopfen", "стучать", "يطرق", "敲"),
 "climb": ("verb", "to go up something", "grimper", "subir", "subir", "arrampicarsi", "klettern", "взбираться", "يتسلّق", "爬"),
 "carry": ("verb", "to hold and move something", "porter", "llevar", "carregar", "portare", "tragen", "нести", "يحمل", "搬运"),
 "hold": ("verb", "to keep something in your hands", "tenir", "sostener", "segurar", "tenere", "halten", "держать", "يمسك", "握住"),
 "push": ("verb", "to press something away from you", "pousser", "empujar", "empurrar", "spingere", "schieben", "толкать", "يدفع", "推"),
 "pull": ("verb", "to move something toward you", "tirer", "tirar de", "puxar", "tirare", "ziehen", "тянуть", "يسحب", "拉"),
 "reach": ("verb", "to arrive at; to stretch out to", "atteindre", "alcanzar", "alcançar", "raggiungere", "erreichen", "достигать", "يصل إلى", "到达"),
 "save": ("verb", "to keep someone safe from harm", "sauver", "salvar", "salvar", "salvare", "retten", "спасать", "ينقذ", "拯救"),
 "keep": ("verb", "to go on having or doing", "garder", "mantener", "manter", "tenere", "behalten", "сохранять", "يبقي", "保持"),
 "turn": ("verb", "to move so you face another way", "tourner", "girar", "virar", "girare", "drehen", "поворачивать", "يستدير", "转"),
 "feel": ("verb", "to sense through touch or emotion", "sentir", "sentir", "sentir", "sentire", "fühlen", "чувствовать", "يشعر", "感觉"),
 "think": ("verb", "to use your mind", "penser", "pensar", "pensar", "pensare", "denken", "думать", "يفكّر", "想"),
 "cross": ("verb", "to go from one side to the other", "traverser", "cruzar", "atravessar", "attraversare", "überqueren", "пересекать", "يعبر", "穿过"),
 "promise": ("verb", "to say you will surely do something", "promettre", "prometer", "prometer", "promettere", "versprechen", "обещать", "يعِد", "承诺"),
 "listen": ("verb", "to pay attention to a sound", "écouter", "escuchar", "ouvir", "ascoltare", "zuhören", "слушать", "يصغي", "聆听"),
 "hear": ("verb", "to notice a sound", "entendre", "oír", "ouvir", "udire", "hören", "слышать", "يسمع", "听见"),
 "watch": ("verb", "to look at for a time", "regarder", "mirar", "observar", "guardare", "beobachten", "наблюдать", "يراقب", "注视"),
 "burn": ("verb", "to be on fire; to give heat", "brûler", "arder", "arder", "bruciare", "brennen", "гореть", "يحترق", "燃烧"),
 "throw": ("verb", "to send through the air with your hand", "jeter", "lanzar", "atirar", "lanciare", "werfen", "бросать", "يرمي", "扔"),
 "grab": ("verb", "to take hold of suddenly", "saisir", "agarrar", "agarrar", "afferrare", "greifen", "хватать", "يمسك بسرعة", "抓住"),
 "worry": ("verb", "to feel afraid something bad may happen", "s'inquiéter", "preocuparse", "preocupar-se", "preoccuparsi", "sich sorgen", "волноваться", "يقلق", "担心"),
 "drink": ("verb", "to take liquid into your mouth", "boire", "beber", "beber", "bere", "trinken", "пить", "يشرب", "喝"),
 "melt": ("verb", "to turn from solid to liquid with heat", "fondre", "derretir", "derreter", "sciogliere", "schmelzen", "таять", "يذوب", "融化"),
 "slip": ("verb", "to slide and lose your footing", "glisser", "resbalar", "escorregar", "scivolare", "ausrutschen", "поскользнуться", "ينزلق", "滑倒"),
 "lean": ("verb", "to rest against or bend toward", "s'appuyer", "apoyarse", "encostar-se", "appoggiarsi", "sich lehnen", "прислоняться", "يتّكئ", "倚靠"),
 "shake": ("verb", "to move quickly to and fro; to tremble", "trembler", "temblar", "tremer", "tremare", "zittern", "дрожать", "يرتجف", "颤抖"),
 "hurt": ("verb", "to cause or feel pain", "faire mal", "doler", "doer", "far male", "wehtun", "болеть", "يؤلم", "疼"),
 "build": ("verb", "to make something by putting parts together", "construire", "construir", "construir", "costruire", "bauen", "строить", "يبني", "建造"),
 # --- adjectives ---
 "warm": ("adjective", "a little hot; comfortable", "chaud", "cálido", "quente", "caldo", "warm", "тёплый", "دافئ", "温暖"),
 "cold": ("adjective", "low in temperature; not warm", "froid", "frío", "frio", "freddo", "kalt", "холодный", "بارد", "寒冷"),
 "dark": ("adjective", "with little or no light", "sombre", "oscuro", "escuro", "buio", "dunkel", "тёмный", "مظلم", "黑暗"),
 "thin": ("adjective", "not thick; narrow", "mince", "delgado", "fino", "sottile", "dünn", "тонкий", "رقيق", "薄"),
 "weak": ("adjective", "not strong", "faible", "débil", "fraco", "debole", "schwach", "слабый", "ضعيف", "虚弱"),
 "grey": ("adjective", "the colour between black and white", "gris", "gris", "cinzento", "grigio", "grau", "серый", "رمادي", "灰色"),
 "gold": ("adjective", "a warm yellow, the colour of the metal", "doré", "dorado", "dourado", "dorato", "golden", "золотой", "ذهبي", "金色"),
 "strange": ("adjective", "unusual; not familiar", "étrange", "extraño", "estranho", "strano", "seltsam", "странный", "غريب", "奇怪"),
 "tired": ("adjective", "needing rest", "fatigué", "cansado", "cansado", "stanco", "müde", "усталый", "متعب", "疲惫"),
 "quiet": ("adjective", "with little or no sound", "silencieux", "silencioso", "silencioso", "silenzioso", "still", "тихий", "هادئ", "安静"),
 "thick": ("adjective", "wide from side to side; dense", "épais", "grueso", "grosso", "spesso", "dick", "толстый", "سميك", "厚"),
 "deep": ("adjective", "going a long way down", "profond", "profundo", "fundo", "profondo", "tief", "глубокий", "عميق", "深"),
 "soft": ("adjective", "not hard; gentle", "doux", "suave", "macio", "morbido", "weich", "мягкий", "ناعم", "柔软"),
 "empty": ("adjective", "with nothing inside", "vide", "vacío", "vazio", "vuoto", "leer", "пустой", "فارغ", "空"),
 "safe": ("adjective", "not in danger", "en sécurité", "seguro", "seguro", "al sicuro", "sicher", "в безопасности", "آمن", "安全"),
 "alive": ("adjective", "living; not dead", "vivant", "vivo", "vivo", "vivo", "lebendig", "живой", "حيّ", "活着"),
 "dead": ("adjective", "no longer living", "mort", "muerto", "morto", "morto", "tot", "мёртвый", "ميت", "死去"),
 "clean": ("adjective", "free from dirt", "propre", "limpio", "limpo", "pulito", "sauber", "чистый", "نظيف", "干净"),
 "bright": ("adjective", "giving a lot of light; shining", "lumineux", "brillante", "brilhante", "luminoso", "hell", "яркий", "ساطع", "明亮"),
 "strong": ("adjective", "having great power or force", "fort", "fuerte", "forte", "forte", "stark", "сильный", "قوي", "强壮"),
 "wrong": ("adjective", "not right; mistaken", "faux", "equivocado", "errado", "sbagliato", "falsch", "неправильный", "خاطئ", "错误"),
 "afraid": ("adjective", "feeling fear; scared", "effrayé", "asustado", "assustado", "spaventato", "ängstlich", "испуганный", "خائف", "害怕"),
}


def main():
    d = json.load(open(P, encoding="utf-8"))
    lex = d["lexicon"]["entries"]
    added = []
    for base, tpl in NEW.items():
        if base in lex:
            continue
        pos, en, *tr = tpl
        e = {"pos": pos, "en": en}
        for lang, t in zip(LANGS, tr):
            e[lang] = t
        lex[base] = e
        added.append(base)
    d["lexicon"]["entries"] = {k: lex[k] for k in sorted(lex)}
    json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"first-light lexicon: +{len(added)} → {len(lex)} entries")


if __name__ == "__main__":
    main()
