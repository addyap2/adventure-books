#!/usr/bin/env python3
"""Phase 4: The Interview (episode-10) lexicon. Reuses the everyday words The Dinner
already defines (same translations) where they appear here, and adds the work /
office / interview vocabulary this book needs. Base-keyed; reader resolves inflection.
Run: python3 scripts/generators/phase4_ep10_lexicon.py"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import build_book as bb

P10 = os.path.join(ROOT, "content", "episode-10.json")
P9 = os.path.join(ROOT, "content", "episode-09.json")
LANGS = ["fr", "es", "it", "de", "pt", "ru", "zh", "ar"]

# key: (pos, en, fr, es, it, de, pt, ru, zh, ar)
NEW = [
 ("aching", "adjective", "hurting with a dull, deep pain", "douloureux", "dolorido", "dolente", "schmerzend", "dolorido", "ноющий", "隐隐作痛的", "موجع"),
 ("advert", "noun", "a notice offering a job or thing", "annonce", "anuncio", "annuncio", "Anzeige", "anúncio", "объявление", "广告", "إعلان"),
 ("avoid", "verb", "to keep away from something", "éviter", "evitar", "evitare", "vermeiden", "evitar", "избегать", "避免", "يتجنّب"),
 ("awning", "noun", "a cloth roof over a shop front", "auvent", "toldo", "tenda", "Markise", "toldo", "навес", "遮篷", "مظلّة"),
 ("barrier", "noun", "a gate that controls who passes", "barrière", "barrera", "barriera", "Schranke", "barreira", "турникет", "闸口", "حاجز"),
 ("blank", "noun", "a sudden empty mind; nothing to say", "trou de mémoire", "quedarse en blanco", "vuoto di memoria", "Blackout", "branco", "провал в памяти", "脑子一片空白", "فراغ ذهني"),
 ("breathe", "verb", "to take air in and out", "respirer", "respirar", "respirare", "atmen", "respirar", "дышать", "呼吸", "يتنفّس"),
 ("buzz", "verb", "to make a low shaking sound", "vibrer", "vibrar", "vibrare", "summen", "vibrar", "жужжать", "嗡嗡响", "يهتزّ"),
 ("candidate", "noun", "a person trying for a job", "candidat", "candidato", "candidato", "Bewerber", "candidato", "кандидат", "应聘者", "مرشّح"),
 ("cash", "noun", "money in notes and coins", "espèces", "efectivo", "contanti", "Bargeld", "dinheiro", "наличные", "现金", "نقد"),
 ("cheek", "noun", "the side of the face below the eye", "joue", "mejilla", "guancia", "Wange", "bochecha", "щека", "脸颊", "خدّ"),
 ("cheer", "verb", "to shout or speak warm support", "encourager", "animar", "incoraggiare", "anfeuern", "torcer por", "подбадривать", "鼓励", "يشجّع"),
 ("chest", "noun", "the front of the body above the stomach", "poitrine", "pecho", "petto", "Brust", "peito", "грудь", "胸口", "صدر"),
 ("clerk", "noun", "a person who works at a desk or counter", "employé", "empleado", "impiegato", "Angestellter", "funcionário", "служащий", "职员", "موظف"),
 ("crawl", "verb", "to move very slowly", "ramper", "arrastrarse", "strisciare", "kriechen", "arrastar-se", "ползти", "缓慢挪动", "يزحف"),
 ("cruel", "adjective", "causing pain without pity", "cruel", "cruel", "crudele", "grausam", "cruel", "жестокий", "残酷的", "قاسٍ"),
 ("crush", "noun", "a tight, pushing crowd", "cohue", "aglomeración", "calca", "Gedränge", "aperto", "давка", "拥挤的人群", "زحام"),
 ("dash", "verb", "to run quickly for a short way", "se précipiter", "ir corriendo", "scattare", "flitzen", "correr", "мчаться", "冲", "يندفع"),
 ("duck", "verb", "to move quickly in out of the way", "se faufiler", "meterse", "infilarsi", "sich ducken", "esgueirar-se", "юркнуть", "闪身躲进", "ينزوي"),
 ("elbow", "noun", "the joint in the middle of the arm", "coude", "codo", "gomito", "Ellbogen", "cotovelo", "локоть", "肘", "مرفق"),
 ("envelope", "noun", "a paper cover for a letter", "enveloppe", "sobre", "busta", "Umschlag", "envelope", "конверт", "信封", "مظروف"),
 ("essential", "noun", "a thing you really need", "essentiel", "lo esencial", "essenziale", "das Nötigste", "essencial", "самое нужное", "必需品", "الأساسيات"),
 ("fake", "verb", "to pretend something is real", "feindre", "fingir", "fingere", "vortäuschen", "fingir", "подделывать", "伪装", "يزيّف"),
 ("familiar", "adjective", "known from before; not strange", "familier", "familiar", "familiare", "vertraut", "familiar", "знакомый", "熟悉的", "مألوف"),
 ("figure", "noun", "the shape of a person seen from afar", "silhouette", "figura", "figura", "Gestalt", "figura", "фигура", "身影", "شبح"),
 ("fluster", "verb", "to make someone nervous and confused", "troubler", "aturullar", "confondere", "aus der Fassung bringen", "atrapalhar", "смущать", "慌乱", "يربك"),
 ("focus", "verb", "to give all your attention to one thing", "se concentrer", "concentrarse", "concentrarsi", "sich konzentrieren", "concentrar-se", "сосредоточиться", "专注", "يركّز"),
 ("fog", "verb", "to cover with mist so it's hard to see through", "embuer", "empañar", "appannare", "beschlagen", "embaçar", "запотевать", "起雾", "يُضبّب"),
 ("fold", "verb", "to give up under pressure", "flancher", "venirse abajo", "crollare", "einknicken", "desmoronar", "сломаться", "崩溃放弃", "ينهار"),
 ("folder", "noun", "a cover for holding papers", "chemise", "carpeta", "cartella", "Mappe", "pasta", "папка", "文件夹", "ملف"),
 ("fray", "verb", "to wear thin and start to come apart", "s'effilocher", "deshilacharse", "logorarsi", "ausfransen", "esfiapar", "сдавать (о нервах)", "磨损", "يتهرّأ"),
 ("glare", "verb", "to stare in an angry way", "fusiller du regard", "fulminar con la mirada", "fulminare con lo sguardo", "funkeln", "fuzilar com o olhar", "сверлить взглядом", "怒视", "يحدّق بغضب"),
 ("grand", "adjective", "fine; you'll be all right (informal)", "ça ira", "bien", "a posto", "bestens", "ótimo", "в порядке", "没事的", "بخير"),
 ("handshake", "noun", "a greeting with the hand", "poignée de main", "apretón de manos", "stretta di mano", "Händedruck", "aperto de mão", "рукопожатие", "握手", "مصافحة"),
 ("heal", "verb", "to make a hurt or a quarrel whole again", "guérir", "sanar", "guarire", "heilen", "sarar", "залечить", "愈合", "يلتئم"),
 ("interview", "noun", "a formal talk to decide about a job", "entretien", "entrevista", "colloquio", "Vorstellungsgespräch", "entrevista", "собеседование", "面试", "مقابلة"),
 ("jam", "verb", "to get stuck and not move", "se coincer", "atascarse", "incepparsi", "klemmen", "emperrar", "застревать", "卡住", "ينحشر"),
 ("lanyard", "noun", "a cord round the neck for an ID card", "cordon", "cordón", "cordino", "Schlüsselband", "cordão", "ланъярд", "挂绳", "شريط عنق"),
 ("lifeline", "noun", "a thing that saves you in trouble", "bouée de sauvetage", "tabla de salvación", "ancora di salvezza", "Rettungsanker", "tábua de salvação", "спасательный круг", "救命稻草", "طوق نجاة"),
 ("lobby", "noun", "the entrance hall of a building", "hall", "vestíbulo", "atrio", "Eingangshalle", "saguão", "вестибюль", "大堂", "بهو"),
 ("loose", "adjective", "not held or fixed; coming apart", "en vrac", "suelto", "sciolto", "lose", "solto", "незакреплённый", "松散的", "مُفكَّك"),
 ("loosen", "verb", "to become less tight or tense", "se détendre", "aflojarse", "allentarsi", "sich lockern", "soltar-se", "расслабляться", "放松", "يرتخي"),
 ("mend", "verb", "to repair; to put right again", "réparer", "arreglar", "riparare", "kitten", "consertar", "чинить", "修复", "يصلح"),
 ("mile", "noun", "a measure of distance, about 1.6 km", "mile", "milla", "miglio", "Meile", "milha", "миля", "英里", "ميل"),
 ("mutter", "verb", "to speak low and unclear, often cross", "marmonner", "mascullar", "borbottare", "murmeln", "resmungar", "бормотать", "嘀咕", "يتمتم"),
 ("nerve", "noun", "steady courage under pressure", "sang-froid", "temple", "sangue freddo", "Nervenstärke", "sangue-frio", "выдержка", "胆识", "رباطة جأش"),
 ("nervous", "adjective", "worried and tense about something", "nerveux", "nervioso", "nervoso", "nervös", "nervoso", "нервный", "紧张的", "متوتّر"),
 ("nervy", "adjective", "on edge; easily made anxious", "à cran", "tenso", "teso", "nervös", "tenso", "взвинченный", "心神不宁的", "متوتّر"),
 ("panel", "noun", "the group who ask the questions", "jury", "tribunal", "commissione", "Auswahlkommission", "banca", "комиссия", "面试小组", "لجنة"),
 ("partner", "noun", "a person you work closely with", "associé", "compañero", "socio", "Partner", "parceiro", "напарник", "搭档", "شريك"),
 ("path", "noun", "a narrow way for walking", "sentier", "sendero", "sentiero", "Weg", "caminho", "дорожка", "小路", "ممرّ"),
 ("pretend", "verb", "to act as if something false is true", "faire semblant", "fingir", "far finta", "so tun als ob", "fingir", "притворяться", "假装", "يتظاهر"),
 ("rattle", "verb", "to shake someone's nerve or calm", "déstabiliser", "poner nervioso", "scuotere", "aus der Ruhe bringen", "abalar", "выбивать из колеи", "使慌乱", "يزعزع"),
 ("reference", "noun", "a good word from a past boss", "référence", "referencia", "referenza", "Referenz", "referência", "рекомендация", "推荐信", "تزكية"),
 ("relieved", "adjective", "glad a worry is over", "soulagé", "aliviado", "sollevato", "erleichtert", "aliviado", "испытавший облегчение", "松了口气的", "مرتاح"),
 ("rift", "noun", "a serious break between people", "brouille", "distanciamiento", "frattura", "Zerwürfnis", "rompimento", "разлад", "裂痕", "قطيعة"),
 ("risky", "adjective", "likely to go wrong; not safe", "risqué", "arriesgado", "rischioso", "riskant", "arriscado", "рискованный", "冒险的", "محفوف بالمخاطر"),
 ("role", "noun", "a job or position", "poste", "puesto", "ruolo", "Stelle", "cargo", "должность", "职位", "منصب"),
 ("roof", "noun", "the cover over a building", "toit", "techo", "tetto", "Dach", "teto", "крыша", "屋顶", "سقف"),
 ("settle", "verb", "to become calm and still", "se calmer", "calmarse", "calmarsi", "sich beruhigen", "acalmar", "успокаиваться", "平静下来", "يهدأ"),
 ("shaky", "adjective", "trembling; not steady", "tremblant", "tembloroso", "tremante", "zittrig", "trêmulo", "дрожащий", "发抖的", "مرتجف"),
 ("silent", "adjective", "making no sound; saying nothing", "silencieux", "silencioso", "silenzioso", "still", "silencioso", "молчаливый", "沉默的", "صامت"),
 ("slot", "noun", "a fixed time set aside for you", "créneau", "turno", "slot", "Termin", "horário", "окно (время)", "时段", "موعد"),
 ("staff", "noun", "the people who work at a place", "personnel", "personal", "personale", "Personal", "equipa", "персонал", "员工", "طاقم"),
 ("stream", "verb", "to move steadily in a crowd, like water", "affluer", "fluir", "scorrere", "strömen", "fluir", "течь потоком", "川流", "يتدفّق"),
 ("stumble", "verb", "to make a mistake and lose your flow", "trébucher", "trabarse", "incespicare", "stolpern", "tropeçar", "запнуться", "结巴卡壳", "يتعثّر"),
 ("swear", "verb", "to say firmly that something is true", "jurer", "jurar", "giurare", "schwören", "jurar", "клясться", "发誓", "يقسم"),
 ("sweat", "verb", "to worry and struggle over something", "se casser la tête", "comerse la cabeza", "scervellarsi", "sich abmühen", "ralar-se", "париться", "费劲折腾", "يتعب نفسه"),
 ("text", "noun", "a short written message on a phone", "SMS", "mensaje", "messaggio", "SMS", "mensagem", "сообщение", "短信", "رسالة"),
 ("unready", "adjective", "not prepared", "pas prêt", "sin preparar", "impreparato", "unvorbereitet", "despreparado", "неготовый", "没准备好的", "غير مستعد"),
 ("unsaid", "adjective", "not spoken, though it should have been", "non-dit", "no dicho", "non detto", "ungesagt", "não dito", "несказанный", "没说出口的", "غير مقول"),
 ("usher", "noun", "a person who shows you where to go", "placeur", "ujier", "usciere", "Platzanweiser", "recepcionista", "распорядитель", "引导员", "مُرشِد"),
 ("wire", "noun", "the very last moment before a deadline", "dernière minute", "último momento", "ultimo istante", "letzte Minute", "cima da hora", "последний момент", "最后关头", "آخر لحظة"),
 ("workmate", "noun", "a person you work with", "collègue", "compañero de trabajo", "collega", "Kollege", "colega", "коллега", "同事", "زميل عمل"),
 # --- a few central everyday work words, for ~250 parity ---
 ("job", "noun", "work you are paid to do", "emploi", "empleo", "lavoro", "Job", "emprego", "работа", "工作", "وظيفة"),
 ("work", "noun", "a paid job; effort you put in", "travail", "trabajo", "lavoro", "Arbeit", "trabalho", "работа", "工作", "عمل"),
 ("office", "noun", "a place where people do desk work", "bureau", "oficina", "ufficio", "Büro", "escritório", "офис", "办公室", "مكتب"),
 ("rent", "noun", "money paid to live in a place", "loyer", "alquiler", "affitto", "Miete", "aluguel", "аренда", "房租", "إيجار"),
 ("suit", "noun", "a smart matching jacket and trousers", "costume", "traje", "completo", "Anzug", "terno", "костюм", "西装", "بدلة"),
 ("address", "noun", "where a place is, in words", "adresse", "dirección", "indirizzo", "Adresse", "endereço", "адрес", "地址", "عنوان"),
 ("question", "noun", "something you are asked", "question", "pregunta", "domanda", "Frage", "pergunta", "вопрос", "问题", "سؤال"),
 ("answer", "noun", "what you say to a question", "réponse", "respuesta", "risposta", "Antwort", "resposta", "ответ", "回答", "إجابة"),
 ("nod", "noun", "a small bend of the head to say yes", "signe de tête", "gesto de cabeza", "cenno del capo", "Nicken", "aceno", "кивок", "点头", "إيماءة"),
 ("platform", "noun", "where you wait for a train", "quai", "andén", "binario", "Bahnsteig", "plataforma", "платформа", "站台", "رصيف"),
 ("ticket", "noun", "a paper that lets you travel", "billet", "billete", "biglietto", "Fahrkarte", "bilhete", "билет", "车票", "تذكرة"),
 ("floor", "noun", "one level of a building", "étage", "piso", "piano", "Stockwerk", "andar", "этаж", "楼层", "طابق"),
 ("shirt", "noun", "a top with a collar and buttons", "chemise", "camisa", "camicia", "Hemd", "camisa", "рубашка", "衬衫", "قميص"),
 ("note", "noun", "a short bit of writing to help you", "note", "nota", "appunto", "Notiz", "nota", "заметка", "笔记", "ملاحظة"),
]


def main():
    d10 = json.load(open(P10, encoding="utf-8"))
    dinner = json.load(open(P9, encoding="utf-8"))["lexicon"]["entries"]
    # tokens present in the interview prose
    toks = set()
    for n in d10["nodes"]:
        for lvl in ("A2", "B1", "B2"):
            for w in bb.words(n["text"][lvl]):
                toks.add(w.lower())
            for c in n.get("choices", []):
                for w in bb.words(c["text"][lvl]):
                    toks.add(w.lower())
    entries = {}
    for k, v in dinner.items():                       # reuse the Dinner words that appear here
        if any(bb.resolve(t, {k}) == k for t in toks):
            entries[k] = v
    for row in NEW:                                    # add the work / interview words
        key, pos, en = row[0], row[1], row[2]
        e = {"pos": pos, "en": en}
        for lang, val in zip(LANGS, row[3:]):
            e[lang] = val
        entries[key] = e
    out = {k: entries[k] for k in sorted(entries)}
    d10["lexicon"] = {
        "_comment": "The Interview's chosen lexicon. Everyday work, time, nerves and the "
                    "city — shared everyday words plus the office/interview set. Base-keyed; "
                    "the reader resolves regular inflection.",
        "entries": out,
    }
    json.dump(d10, open(P10, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"lexicon: {len(out)} entries ({len(out)-len(NEW)} reused + {len(NEW)} new) x {len(LANGS)+1} langs")


if __name__ == "__main__":
    main()
