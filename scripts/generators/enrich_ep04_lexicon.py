#!/usr/bin/env python3
"""Even out lexicon depth: top The Cool of Evening (episode-04) up to ~250 entries.
Base-keyed; shared words reuse the same gloss as other books. Idempotent.
Run: python3 scripts/enrich_ep04_lexicon.py"""
import json, os

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "episode-04.json")
LANGS = ["fr", "es", "pt", "it", "de", "ru", "ar", "zh"]

NEW = {
 "people": ("noun", "human beings; persons", "les gens", "la gente", "as pessoas", "la gente", "die Leute", "люди", "الناس", "人们"),
 "eyes": ("noun", "the parts of the body you see with", "les yeux", "los ojos", "os olhos", "gli occhi", "die Augen", "глаза", "عينان", "眼睛"),
 "face": ("noun", "the front of the head", "le visage", "la cara", "o rosto", "il viso", "das Gesicht", "лицо", "وجه", "脸"),
 "head": ("noun", "the top part of the body, with the face", "la tête", "la cabeza", "a cabeça", "la testa", "der Kopf", "голова", "رأس", "头"),
 "look": ("verb", "to turn your eyes to see", "regarder", "mirar", "olhar", "guardare", "schauen", "смотреть", "ينظر", "看"),
 "take": ("verb", "to get hold of and carry", "prendre", "tomar", "pegar", "prendere", "nehmen", "брать", "يأخذ", "拿"),
 "turn": ("verb", "to move so you face another way", "tourner", "girar", "virar", "girare", "drehen", "поворачивать", "يستدير", "转"),
 "wait": ("verb", "to stay until something happens", "attendre", "esperar", "esperar", "aspettare", "warten", "ждать", "ينتظر", "等待"),
 "stop": ("verb", "to end moving or doing", "arrêter", "parar", "parar", "fermarsi", "aufhören", "останавливаться", "يتوقّف", "停止"),
 "need": ("verb", "to have to have something", "avoir besoin de", "necesitar", "precisar", "aver bisogno di", "brauchen", "нуждаться", "يحتاج", "需要"),
 "alone": ("adjective", "with no one else", "seul", "solo", "sozinho", "solo", "allein", "один", "وحيد", "独自"),
 "close": ("adjective", "near", "proche", "cercano", "próximo", "vicino", "nah", "близкий", "قريب", "近"),
 "slow": ("adjective", "not fast", "lent", "lento", "lento", "lento", "langsam", "медленный", "بطيء", "慢"),
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
    print(f"cool-of-evening lexicon: +{len(added)} → {len(lex)} entries")


if __name__ == "__main__":
    main()
