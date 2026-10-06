#!/usr/bin/env python3
"""Even out lexicon depth: top The Address (episode-01) up to ~250 entries.
Base-keyed; shared words reuse the same gloss as other books. Idempotent.
Run: python3 scripts/enrich_ep01_lexicon.py"""
import json, os

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "episode-01.json")
LANGS = ["fr", "es", "pt", "it", "de", "ru", "ar", "zh"]

NEW = {
 "street": ("noun", "a road in a town with buildings", "la rue", "la calle", "a rua", "la strada", "die Straße", "улица", "شارع", "街道"),
 "river": ("noun", "a wide stream of water", "la rivière", "el río", "o rio", "il fiume", "der Fluss", "река", "نهر", "河"),
 "name": ("noun", "what someone or something is called", "le nom", "el nombre", "o nome", "il nome", "der Name", "имя", "اسم", "名字"),
 "woman": ("noun", "an adult female person", "la femme", "la mujer", "a mulher", "la donna", "die Frau", "женщина", "امرأة", "女人"),
 "morning": ("noun", "the early part of the day", "le matin", "la mañana", "a manhã", "la mattina", "der Morgen", "утро", "صباح", "早晨"),
 "window": ("noun", "a glass opening in a wall", "la fenêtre", "la ventana", "a janela", "la finestra", "das Fenster", "окно", "نافذة", "窗户"),
 "number": ("noun", "a figure like 1, 2, 3", "le nombre", "el número", "o número", "il numero", "die Zahl", "число", "رقم", "数字"),
 "cold": ("adjective", "low in temperature; not warm", "froid", "frío", "frio", "freddo", "kalt", "холодный", "بارد", "寒冷"),
 "warm": ("adjective", "a little hot; comfortable", "chaud", "cálido", "quente", "caldo", "warm", "тёплый", "دافئ", "温暖"),
 # new
 "letter": ("noun", "a written message sent to someone", "la lettre", "la carta", "a carta", "la lettera", "der Brief", "письмо", "رسالة", "信"),
 "city": ("noun", "a large town", "la ville", "la ciudad", "a cidade", "la città", "die Stadt", "город", "مدينة", "城市"),
 "desk": ("noun", "a table for writing or working at", "le bureau", "el escritorio", "a secretária", "la scrivania", "der Schreibtisch", "письменный стол", "مكتب", "书桌"),
 "glass": ("noun", "the hard clear material in windows; a cup", "le verre", "el vidrio", "o vidro", "il vetro", "das Glas", "стекло", "زجاج", "玻璃"),
 "coffee": ("noun", "a hot drink made from roasted beans", "le café", "el café", "o café", "il caffè", "der Kaffee", "кофе", "قهوة", "咖啡"),
 "address": ("noun", "the details of where a place is", "l'adresse", "la dirección", "a morada", "l'indirizzo", "die Adresse", "адрес", "عنوان", "地址"),
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
    print(f"the-address lexicon: +{len(added)} → {len(lex)} entries")


if __name__ == "__main__":
    main()
