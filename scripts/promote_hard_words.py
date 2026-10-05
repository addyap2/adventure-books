#!/usr/bin/env python3
"""Promote genuinely hard words out of the 'assumed-known' core wordlist and back
into the per-book lexicons as tappable glosses.

When the band warnings were cleared, ~410 words were added to wordlist_core.txt so
the validator would treat them as known and stop flagging them. Most are ordinary
English, but some are genuinely hard for an A2/B1 learner (ochre, beacon, draught,
treacherous...). For those we'd rather give a real tap-gloss than assume them.

This script, for each hard word:
  - removes it (and any inflected form) from scripts/wordlist_core.txt,
  - adds a full lexicon entry (en + 8 languages) to every book whose prose actually
    uses it (detected with the reader's own inflection resolver).

Idempotent. Run: python3 scripts/promote_hard_words.py
"""
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_book as bb  # resolver + word tokeniser, so detection matches the reader

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
WORDLIST = os.path.join(HERE, "wordlist_core.txt")
LANGS = ["fr", "es", "pt", "it", "de", "ru", "ar", "zh"]

# base form -> full entry (pos, en, then the 8 languages)
PROMOTE = {
 "ablaze": ("adjective", "burning strongly; on fire", "en flammes", "en llamas", "em chamas", "in fiamme", "in Flammen", "в огне", "مشتعل", "熊熊燃烧"),
 "ajar": ("adjective", "slightly open", "entrouvert", "entreabierto", "entreaberto", "socchiuso", "angelehnt", "приоткрытый", "موارب", "半开着"),
 "beacon": ("noun", "a guiding light, especially for ships", "le phare", "el faro", "o farol", "il faro", "das Leuchtfeuer", "маяк", "منارة", "灯塔之光"),
 "blister": ("verb", "to swell or peel from heat", "cloquer", "ampollarse", "empolar", "coprirsi di bolle", "Blasen werfen", "покрываться пузырями", "يتقرّح", "起泡"),
 "bosun": ("noun", "a ship's officer in charge of the crew and gear", "le maître d'équipage", "el contramaestre", "o contramestre", "il nostromo", "der Bootsmann", "боцман", "رئيس البحّارة", "水手长"),
 "dishwater": ("noun", "dirty water left after washing dishes", "l'eau de vaisselle", "el agua de fregar", "a água de lavar louça", "l'acqua dei piatti", "das Spülwasser", "помои", "ماء غسل الصحون", "洗碗水"),
 "draught": ("noun", "a current of cold air indoors", "le courant d'air", "la corriente de aire", "a corrente de ar", "la corrente d'aria", "der Luftzug", "сквозняк", "تيار هواء", "穿堂风"),
 "gnaw": ("verb", "to bite at steadily; to wear away", "ronger", "roer", "roer", "rodere", "nagen", "грызть", "ينهش", "啃噬"),
 "grudging": ("adjective", "given unwillingly; reluctant", "réticent", "reacio", "relutante", "riluttante", "widerwillig", "неохотный", "متردّد", "勉强的"),
 "guttering": ("adjective", "(of a flame) burning low and unsteadily", "vacillant", "vacilante", "vacilante", "guizzante", "flackernd", "мерцающий", "مرتجف", "忽明忽暗的"),
 "hoarding": ("noun", "a tall temporary fence around a building site", "la palissade", "la valla de obra", "o tapume", "la recinzione", "der Bauzaun", "строительный забор", "سياج مؤقت", "工地围挡"),
 "hoarse": ("adjective", "rough and harsh in voice", "rauque", "ronco", "rouco", "rauco", "heiser", "хриплый", "أجشّ", "沙哑"),
 "ochre": ("adjective", "a yellow-brown earth colour", "ocre", "ocre", "ocre", "ocra", "ockerfarben", "охристый", "لون مغرة", "赭色"),
 "outlast": ("verb", "to last longer than", "durer plus longtemps que", "durar más que", "durar mais que", "durare più di", "überdauern", "пережить", "يدوم أطول من", "比…持久"),
 "pathless": ("adjective", "having no path", "sans chemin", "sin senda", "sem trilho", "senza sentiero", "weglos", "бездорожный", "بلا مسار", "无路可循的"),
 "rasp": ("verb", "to say in a rough, grating voice", "dire d'une voix râpeuse", "decir con voz áspera", "dizer com voz áspera", "dire con voce roca", "krächzen", "хрипеть", "يقول بصوت خشن", "嘶哑地说"),
 "rosewater": ("noun", "water scented with roses", "l'eau de rose", "el agua de rosas", "a água de rosas", "l'acqua di rose", "das Rosenwasser", "розовая вода", "ماء الورد", "玫瑰水"),
 "seawater": ("noun", "salt water from the sea", "l'eau de mer", "el agua de mar", "a água do mar", "l'acqua di mare", "das Meerwasser", "морская вода", "ماء البحر", "海水"),
 "bathwater": ("noun", "the water in a bath", "l'eau du bain", "el agua del baño", "a água do banho", "l'acqua del bagno", "das Badewasser", "вода для ванны", "ماء الحمّام", "洗澡水"),
 "shadeless": ("adjective", "with no shade from the sun", "sans ombre", "sin sombra", "sem sombra", "senz'ombra", "schattenlos", "без тени", "بلا ظل", "没有遮荫的"),
 "sputter": ("verb", "to make soft spitting sounds", "crachoter", "chisporrotear", "crepitar", "sputacchiare", "stottern", "фыркать", "يبصق متقطّعاً", "噼啪作响"),
 "tideline": ("noun", "the mark the sea leaves on the shore", "la laisse de mer", "la línea de marea", "a linha de maré", "la linea di marea", "die Gezeitenlinie", "линия прилива", "خط المد", "潮痕线"),
 "trackless": ("adjective", "with no track or path", "sans piste", "sin camino", "sem caminho", "senza traccia", "ohne Pfade", "бездорожный", "بلا دروب", "无径可循的"),
 "treacherous": ("adjective", "dangerous and not to be trusted", "traître", "traicionero", "traiçoeiro", "infido", "tückisch", "коварный", "غادر", "暗藏危险的"),
 "unlit": ("adjective", "not lit; dark", "non éclairé", "sin luz", "sem luz", "non illuminato", "unbeleuchtet", "неосвещённый", "غير مضاء", "没点灯的"),
 "wrung": ("verb", "twisted hard to squeeze water out", "essoré", "escurrido", "torcido", "strizzato", "ausgewrungen", "выжатый", "معصور", "拧干的"),
 "yawn": ("verb", "to open wide; (of a gap) to gape", "bâiller", "abrirse / bostezar", "abrir-se / bocejar", "spalancarsi", "gähnen / klaffen", "зиять", "يفغر", "张开大口"),
 "snug": ("adjective", "warm, close and comfortable", "douillet", "acogedor", "aconchegante", "comodo e caldo", "behaglich", "уютный", "دافئ ومريح", "暖和舒适"),
 "blessed": ("adjective", "very welcome; a relief", "béni", "bendito", "abençoado", "benedetto", "wohltuend", "благодатный", "مبارَك", "令人宽慰的"),
 "hedge": ("noun", "a row of bushes forming a boundary", "la haie", "el seto", "a sebe", "la siepe", "die Hecke", "живая изгородь", "سياج نباتي", "树篱"),
}


def entry(tpl):
    pos, en, *tr = tpl
    e = {"pos": pos, "en": en}
    for lang, t in zip(LANGS, tr):
        e[lang] = t
    return e


def appears(base, node_texts):
    """True if any token in the book's prose resolves to `base`."""
    for txt in node_texts:
        for w in bb.words(txt):
            if bb.resolve(w.lower(), {base}) == base:
                return True
    return False


def main():
    bases = set(PROMOTE)
    # 1) remove promoted words (and their inflections) from the core wordlist
    core = [w.strip() for w in open(WORDLIST, encoding="utf-8") if w.strip()]
    kept, removed = [], []
    for w in core:
        if w in bases or any(bb.resolve(w, {b}) == b for b in bases):
            removed.append(w)
        else:
            kept.append(w)
    open(WORDLIST, "w", encoding="utf-8").write("\n".join(sorted(set(kept))) + "\n")
    print(f"core wordlist: removed {len(removed)} form(s) → {sorted(removed)}")

    # 2) add each promoted word to the lexicon of every book that uses it
    for path in sorted(glob.glob(os.path.join(ROOT, "content", "episode-*.json"))):
        book = json.load(open(path, encoding="utf-8"))
        slug = book.get("slug")
        texts = [t for n in book["nodes"] for t in (n.get("text") or {}).values()]
        lex = book["lexicon"]["entries"]
        added = []
        for base, tpl in PROMOTE.items():
            if base in lex:
                continue
            if appears(base, texts):
                lex[base] = entry(tpl)
                added.append(base)
        if added:
            book["lexicon"]["entries"] = {k: lex[k] for k in sorted(lex)}
            json.dump(book, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"  {slug:<20} +{len(added)} lexicon: {sorted(added)}")


if __name__ == "__main__":
    main()
