#!/usr/bin/env python3
"""Even out lexicon depth: enrich The Night Market (episode-02) toward ~250 entries.

Adds concrete, high-tap content words that recur in the prose but weren't glossed —
market/stall nouns plus common verbs and adjectives. Words shared with other books
reuse the same gloss for consistency. Base-keyed. Idempotent.

Run: python3 scripts/enrich_ep02_lexicon.py
"""
import json, os

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "episode-02.json")
LANGS = ["fr", "es", "pt", "it", "de", "ru", "ar", "zh"]

NEW = {
 # --- nouns (shared glosses reused from other books) ---
 "night": ("noun", "the dark hours when the sun is down", "la nuit", "la noche", "a noite", "la notte", "die Nacht", "ночь", "الليل", "夜晚"),
 "light": ("noun", "brightness that lets you see", "la lumière", "la luz", "a luz", "la luce", "das Licht", "свет", "ضوء", "光"),
 "door": ("noun", "the way in and out of a room", "la porte", "la puerta", "a porta", "la porta", "die Tür", "дверь", "باب", "门"),
 "money": ("noun", "coins and notes you pay with", "l'argent", "el dinero", "o dinheiro", "il denaro", "das Geld", "деньги", "مال", "钱"),
 "crowd": ("noun", "a large group of people together", "la foule", "la multitud", "a multidão", "la folla", "die Menge", "толпа", "حشد", "人群"),
 "voice": ("noun", "the sound you make when you speak", "la voix", "la voz", "a voz", "la voce", "die Stimme", "голос", "صوت", "嗓音"),
 "corner": ("noun", "where two walls or streets meet", "le coin", "la esquina", "a esquina", "l'angolo", "die Ecke", "угол", "زاوية", "角落"),
 "heart": ("noun", "the organ that pumps blood; your feelings", "le cœur", "el corazón", "o coração", "il cuore", "das Herz", "сердце", "قلب", "心"),
 # --- nouns (market/stall, new) ---
 "bowl": ("noun", "a round, deep dish for food", "le bol", "el cuenco", "a tigela", "la ciotola", "die Schüssel", "миска", "وعاء", "碗"),
 "coin": ("noun", "a round piece of metal money", "la pièce", "la moneda", "a moeda", "la moneta", "die Münze", "монета", "عملة معدنية", "硬币"),
 "market": ("noun", "a place where people buy and sell", "le marché", "el mercado", "o mercado", "il mercato", "der Markt", "рынок", "سوق", "市场"),
 "counter": ("noun", "the long table where you are served", "le comptoir", "el mostrador", "o balcão", "il bancone", "die Theke", "прилавок", "منضدة", "柜台"),
 "price": ("noun", "the money something costs", "le prix", "el precio", "o preço", "il prezzo", "der Preis", "цена", "سعر", "价格"),
 "hand": ("noun", "the part of the arm with fingers", "la main", "la mano", "a mão", "la mano", "die Hand", "рука", "يد", "手"),
 "name": ("noun", "what someone or something is called", "le nom", "el nombre", "o nome", "il nome", "der Name", "имя", "اسم", "名字"),
 "food": ("noun", "what you eat", "la nourriture", "la comida", "a comida", "il cibo", "das Essen", "еда", "طعام", "食物"),
 "shelf": ("noun", "a flat board for holding things", "l'étagère", "el estante", "a prateleira", "lo scaffale", "das Regal", "полка", "رفّ", "架子"),
 "number": ("noun", "a figure like 1, 2, 3", "le nombre", "el número", "o número", "il numero", "die Zahl", "число", "رقم", "数字"),
 "noise": ("noun", "a loud or unpleasant sound", "le bruit", "el ruido", "o barulho", "il rumore", "der Lärm", "шум", "ضجيج", "噪音"),
 "woman": ("noun", "an adult female person", "la femme", "la mujer", "a mulher", "la donna", "die Frau", "женщина", "امرأة", "女人"),
 "rain": ("noun", "water falling from the sky", "la pluie", "la lluvia", "a chuva", "la pioggia", "der Regen", "дождь", "مطر", "雨"),
 "taste": ("noun", "the flavour of food", "le goût", "el sabor", "o sabor", "il sapore", "der Geschmack", "вкус", "طعم", "味道"),
 "greens": ("noun", "green leafy vegetables", "les légumes verts", "las verduras", "os legumes verdes", "le verdure", "das Grüngemüse", "зелень", "خضار", "青菜"),
 "hour": ("noun", "sixty minutes", "l'heure", "la hora", "a hora", "l'ora", "die Stunde", "час", "ساعة", "小时"),
 "smoke": ("noun", "the grey cloud from a fire", "la fumée", "el humo", "o fumo", "il fumo", "der Rauch", "дым", "دخان", "烟"),
 "season": ("noun", "a part of the year; a busy time of year", "la saison", "la temporada", "a estação", "la stagione", "die Jahreszeit", "сезон", "موسم", "季节"),
 "order": ("noun", "a request for food or goods", "la commande", "el pedido", "o pedido", "l'ordine", "die Bestellung", "заказ", "طلب", "点单"),
 # --- verbs (shared reused) ---
 "hold": ("verb", "to keep something in your hands", "tenir", "sostener", "segurar", "tenere", "halten", "держать", "يمسك", "握住"),
 "pull": ("verb", "to move something toward you", "tirer", "tirar de", "puxar", "tirare", "ziehen", "тянуть", "يسحب", "拉"),
 "reach": ("verb", "to arrive at; to stretch out to", "atteindre", "alcanzar", "alcançar", "raggiungere", "erreichen", "достигать", "يصل إلى", "到达"),
 "keep": ("verb", "to go on having or doing", "garder", "mantener", "manter", "tenere", "behalten", "сохранять", "يبقي", "保持"),
 "turn": ("verb", "to move so you face another way", "tourner", "girar", "virar", "girare", "drehen", "поворачивать", "يستدير", "转"),
 "feel": ("verb", "to sense through touch or emotion", "sentir", "sentir", "sentir", "sentire", "fühlen", "чувствовать", "يشعر", "感觉"),
 "think": ("verb", "to use your mind", "penser", "pensar", "pensar", "pensare", "denken", "думать", "يفكّر", "想"),
 "cross": ("verb", "to go from one side to the other", "traverser", "cruzar", "atravessar", "attraversare", "überqueren", "пересекать", "يعبر", "穿过"),
 "hear": ("verb", "to notice a sound", "entendre", "oír", "ouvir", "udire", "hören", "слышать", "يسمع", "听见"),
 "watch": ("verb", "to look at for a time", "regarder", "mirar", "observar", "guardare", "beobachten", "наблюдать", "يراقب", "注视"),
 # --- verbs (new) ---
 "count": ("verb", "to say numbers; to add up", "compter", "contar", "contar", "contare", "zählen", "считать", "يعدّ", "数"),
 "take": ("verb", "to get hold of and carry", "prendre", "tomar", "pegar", "prendere", "nehmen", "брать", "يأخذ", "拿"),
 "tell": ("verb", "to say something to someone", "dire", "decir", "dizer", "dire", "sagen", "говорить", "يخبر", "告诉"),
 "make": ("verb", "to create or produce", "faire", "hacer", "fazer", "fare", "machen", "делать", "يصنع", "做"),
 "call": ("verb", "to say loudly; to telephone", "appeler", "llamar", "chamar", "chiamare", "rufen", "звать", "ينادي", "呼喊"),
 "drop": ("verb", "to let something fall", "laisser tomber", "dejar caer", "deixar cair", "lasciar cadere", "fallen lassen", "ронять", "يُسقط", "掉落"),
 "wait": ("verb", "to stay until something happens", "attendre", "esperar", "esperar", "aspettare", "warten", "ждать", "ينتظر", "等待"),
 "trust": ("verb", "to believe someone is honest", "faire confiance", "confiar", "confiar", "fidarsi", "vertrauen", "доверять", "يثق", "信任"),
 "catch": ("verb", "to take hold of a moving thing", "attraper", "atrapar", "apanhar", "prendere al volo", "fangen", "ловить", "يمسك", "接住"),
 "lose": ("verb", "to no longer have; to not win", "perdre", "perder", "perder", "perdere", "verlieren", "терять", "يخسر", "失去"),
 "hope": ("verb", "to want something to happen", "espérer", "esperar", "esperar", "sperare", "hoffen", "надеяться", "يأمل", "希望"),
 # --- adjectives (shared reused) ---
 "cold": ("adjective", "low in temperature; not warm", "froid", "frío", "frio", "freddo", "kalt", "холодный", "بارد", "寒冷"),
 "warm": ("adjective", "a little hot; comfortable", "chaud", "cálido", "quente", "caldo", "warm", "тёплый", "دافئ", "温暖"),
 "tired": ("adjective", "needing rest", "fatigué", "cansado", "cansado", "stanco", "müde", "усталый", "متعب", "疲惫"),
 "quiet": ("adjective", "with little or no sound", "silencieux", "silencioso", "silencioso", "silenzioso", "still", "тихий", "هادئ", "安静"),
 "safe": ("adjective", "not in danger", "en sécurité", "seguro", "seguro", "al sicuro", "sicher", "в безопасности", "آمن", "安全"),
 "empty": ("adjective", "with nothing inside", "vide", "vacío", "vazio", "vuoto", "leer", "пустой", "فارغ", "空"),
 # --- adjectives (new) ---
 "small": ("adjective", "little in size", "petit", "pequeño", "pequeno", "piccolo", "klein", "маленький", "صغير", "小"),
 "cheap": ("adjective", "low in price", "bon marché", "barato", "barato", "economico", "billig", "дешёвый", "رخيص", "便宜"),
 "hungry": ("adjective", "wanting food", "affamé", "hambriento", "esfomeado", "affamato", "hungrig", "голодный", "جائع", "饿"),
 "honest": ("adjective", "truthful; not cheating", "honnête", "honesto", "honesto", "onesto", "ehrlich", "честный", "صادق", "诚实"),
 "busy": ("adjective", "with a lot to do", "occupé", "ocupado", "ocupado", "occupato", "beschäftigt", "занятый", "مشغول", "忙碌"),
 "loud": ("adjective", "making a lot of sound", "fort", "ruidoso", "barulhento", "rumoroso", "laut", "громкий", "صاخب", "吵闹"),
 "quick": ("adjective", "fast", "rapide", "rápido", "rápido", "rapido", "schnell", "быстрый", "سريع", "快"),
 "easy": ("adjective", "not hard to do", "facile", "fácil", "fácil", "facile", "leicht", "лёгкий", "سهل", "容易"),
 "ready": ("adjective", "prepared", "prêt", "listo", "pronto", "pronto", "bereit", "готовый", "جاهز", "准备好"),
 "calm": ("adjective", "quiet and not worried", "calme", "tranquilo", "calmo", "calmo", "ruhig", "спокойный", "هادئ", "冷静"),
 "full": ("adjective", "holding all it can", "plein", "lleno", "cheio", "pieno", "voll", "полный", "ممتلئ", "满"),
 "short": ("adjective", "little in length or time", "court", "corto", "curto", "corto", "kurz", "короткий", "قصير", "短"),
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
    print(f"the-night-market lexicon: +{len(added)} → {len(lex)} entries")


if __name__ == "__main__":
    main()
