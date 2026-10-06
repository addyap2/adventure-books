#!/usr/bin/env python3
"""Even out lexicon depth: enrich The Orchard (episode-06) toward ~250 entries.

Adds concrete, high-tap content words that recur but weren't glossed. Shared words
reuse the same gloss as other books. Base-keyed. Idempotent.

Run: python3 scripts/enrich_ep06_lexicon.py
"""
import json, os

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "episode-06.json")
LANGS = ["fr", "es", "pt", "it", "de", "ru", "ar", "zh"]

NEW = {
 # shared (reused glosses)
 "night": ("noun", "the dark hours when the sun is down", "la nuit", "la noche", "a noite", "la notte", "die Nacht", "ночь", "الليل", "夜晚"),
 "door": ("noun", "the way in and out of a room", "la porte", "la puerta", "a porta", "la porta", "die Tür", "дверь", "باب", "门"),
 "voice": ("noun", "the sound you make when you speak", "la voix", "la voz", "a voz", "la voce", "die Stimme", "голос", "صوت", "嗓音"),
 "hand": ("noun", "the part of the arm with fingers", "la main", "la mano", "a mão", "la mano", "die Hand", "рука", "يد", "手"),
 "phone": ("noun", "a device for talking to someone far away", "le téléphone", "el teléfono", "o telefone", "il telefono", "das Telefon", "телефон", "هاتف", "电话"),
 "keep": ("verb", "to go on having or doing", "garder", "mantener", "manter", "tenere", "behalten", "сохранять", "يبقي", "保持"),
 "turn": ("verb", "to move so you face another way", "tourner", "girar", "virar", "girare", "drehen", "поворачивать", "يستدير", "转"),
 "take": ("verb", "to get hold of and carry", "prendre", "tomar", "pegar", "prendere", "nehmen", "брать", "يأخذ", "拿"),
 "think": ("verb", "to use your mind", "penser", "pensar", "pensar", "pensare", "denken", "думать", "يفكّر", "想"),
 "feel": ("verb", "to sense through touch or emotion", "sentir", "sentir", "sentir", "sentire", "fühlen", "чувствовать", "يشعر", "感觉"),
 "make": ("verb", "to create or produce", "faire", "hacer", "fazer", "fare", "machen", "делать", "يصنع", "做"),
 "call": ("verb", "to say loudly; to telephone", "appeler", "llamar", "chamar", "chiamare", "rufen", "звать", "ينادي", "呼喊"),
 "wait": ("verb", "to stay until something happens", "attendre", "esperar", "esperar", "aspettare", "warten", "ждать", "ينتظر", "等待"),
 "push": ("verb", "to press something away from you", "pousser", "empujar", "empurrar", "spingere", "schieben", "толкать", "يدفع", "推"),
 "small": ("adjective", "little in size", "petit", "pequeño", "pequeno", "piccolo", "klein", "маленький", "صغير", "小"),
 "full": ("adjective", "holding all it can", "plein", "lleno", "cheio", "pieno", "voll", "полный", "ممتلئ", "满"),
 "short": ("adjective", "little in length or time", "court", "corto", "curto", "corto", "kurz", "короткий", "قصير", "短"),
 # new nouns
 "fruit": ("noun", "the sweet part of a plant, grown to eat", "le fruit", "la fruta", "a fruta", "la frutta", "das Obst", "фрукт", "فاكهة", "水果"),
 "store": ("noun", "a shop; a supply kept for later", "le magasin", "la tienda", "a loja", "il negozio", "der Laden", "лавка", "متجر", "店铺"),
 "place": ("noun", "a particular spot or area", "l'endroit", "el lugar", "o lugar", "il luogo", "der Ort", "место", "مكان", "地方"),
 "moment": ("noun", "a very short time", "le moment", "el momento", "o momento", "il momento", "der Augenblick", "момент", "لحظة", "片刻"),
 "morning": ("noun", "the early part of the day", "le matin", "la mañana", "a manhã", "la mattina", "der Morgen", "утро", "صباح", "早晨"),
 "people": ("noun", "human beings; persons", "les gens", "la gente", "as pessoas", "la gente", "die Leute", "люди", "الناس", "人们"),
 "work": ("noun", "a job; effort to do something", "le travail", "el trabajo", "o trabalho", "il lavoro", "die Arbeit", "работа", "عمل", "工作"),
 "head": ("noun", "the top part of the body, with the face", "la tête", "la cabeza", "a cabeça", "la testa", "der Kopf", "голова", "رأس", "头"),
 "face": ("noun", "the front of the head", "le visage", "la cara", "o rosto", "il viso", "das Gesicht", "лицо", "وجه", "脸"),
 "eyes": ("noun", "the parts of the body you see with", "les yeux", "los ojos", "os olhos", "gli occhi", "die Augen", "глаза", "عينان", "眼睛"),
 "step": ("noun", "one movement of the foot; a stair", "le pas", "el paso", "o passo", "il passo", "der Schritt", "шаг", "خطوة", "一步"),
 "smile": ("noun", "a happy look made with the mouth", "le sourire", "la sonrisa", "o sorriso", "il sorriso", "das Lächeln", "улыбка", "ابتسامة", "微笑"),
 "friend": ("noun", "someone you like and know well", "l'ami", "el amigo", "o amigo", "l'amico", "der Freund", "друг", "صديق", "朋友"),
 # new verbs
 "move": ("verb", "to go from one place to another", "bouger", "mover", "mover", "muoversi", "sich bewegen", "двигаться", "يتحرّك", "移动"),
 "look": ("verb", "to turn your eyes to see", "regarder", "mirar", "olhar", "guardare", "schauen", "смотреть", "ينظر", "看"),
 "leave": ("verb", "to go away from; to let stay behind", "partir / laisser", "irse / dejar", "sair / deixar", "lasciare / partire", "verlassen", "покидать", "يترك", "离开"),
 "stop": ("verb", "to end moving or doing", "arrêter", "parar", "parar", "fermarsi", "aufhören", "останавливаться", "يتوقّف", "停止"),
 "start": ("verb", "to begin", "commencer", "empezar", "começar", "iniziare", "anfangen", "начинать", "يبدأ", "开始"),
 "decide": ("verb", "to make up your mind", "décider", "decidir", "decidir", "decidere", "entscheiden", "решать", "يقرّر", "决定"),
 "know": ("verb", "to have information in your mind", "savoir", "saber", "saber", "sapere", "wissen", "знать", "يعرف", "知道"),
 # new adjectives
 "hard": ("adjective", "not soft; difficult", "dur", "duro", "duro", "duro", "hart", "твёрдый", "صعب", "硬"),
 "long": ("adjective", "measuring a lot end to end; lasting a long time", "long", "largo", "longo", "lungo", "lang", "длинный", "طويل", "长"),
 "good": ("adjective", "of high quality; kind", "bon", "bueno", "bom", "buono", "gut", "хороший", "جيد", "好"),
 "alone": ("adjective", "with no one else", "seul", "solo", "sozinho", "solo", "allein", "один", "وحيد", "独自"),
 "black": ("adjective", "the darkest colour", "noir", "negro", "preto", "nero", "schwarz", "чёрный", "أسود", "黑色"),
 "white": ("adjective", "the lightest colour", "blanc", "blanco", "branco", "bianco", "weiß", "белый", "أبيض", "白色"),
 "alive": ("adjective", "living; not dead", "vivant", "vivo", "vivo", "vivo", "lebendig", "живой", "حيّ", "活着"),
 "slow": ("adjective", "not fast", "lent", "lento", "lento", "lento", "langsam", "медленный", "بطيء", "慢"),
 "close": ("adjective", "near", "proche", "cercano", "próximo", "vicino", "nah", "близкий", "قريب", "近"),
 "lost": ("adjective", "unable to find the way; no longer had", "perdu", "perdido", "perdido", "perso", "verloren", "потерянный", "ضائع", "迷失"),
 "gone": ("adjective", "no longer here; left", "parti", "ido", "ido", "andato", "weg", "ушедший", "مفقود", "不见了"),
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
    print(f"the-orchard lexicon: +{len(added)} → {len(lex)} entries")


if __name__ == "__main__":
    main()
