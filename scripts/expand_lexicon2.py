#!/usr/bin/env python3
"""Phase 4: grow episode 1's chosen lexicon to cover the expanded story.

Adds ~90 concrete, high-tap-value words introduced by the new passages (nouns first,
then common verbs and adjectives), keyed by base form so the reader's suffix rules catch
inflections. Skips proper nouns, contractions, and B2-only literary flourishes. Appends to
the book's own lexicon; the existing 142 entries are untouched.

NOTE: like every gloss here, these 8-language translations are a draft and MUST pass a
native speaker's check before launch — a wrong gloss the learner cannot detect is worse
than no gloss.
"""
import json, os

EP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "episode-01.json")
book = json.load(open(EP, encoding="utf-8"))
L = ["fr", "es", "pt", "it", "de", "ru", "ar", "zh"]

# base : [pos, en, fr, es, pt, it, de, ru, ar, zh]
E = {
 # --- concrete nouns ---
 "cart": ["noun","a small vehicle on wheels for selling or carrying things","le chariot","el carrito","o carrinho","il carretto","der Wagen","тележка","عربة","手推车"],
 "queue": ["noun","a line of people waiting for something","la file d'attente","la cola","a fila","la fila","die Schlange","очередь","طابور","队伍"],
 "lobby": ["noun","the open area just inside the entrance of a building","le hall","el vestíbulo","o átrio","l'atrio","die Lobby","вестибюль","بهو","大堂"],
 "breath": ["noun","the air you take into and let out of your body","le souffle","el aliento","o fôlego","il respiro","der Atem","дыхание","نفَس","呼吸"],
 "flask": ["noun","a container that keeps a drink hot or cold","la thermos","el termo","a garrafa térmica","il thermos","die Thermoskanne","термос","ترمس","保温瓶"],
 "tray": ["noun","a flat object for carrying or holding things","le plateau","la bandeja","o tabuleiro","il vassoio","das Tablett","поднос","صينية","托盘"],
 "van": ["noun","a covered vehicle for carrying goods","la camionnette","la furgoneta","a carrinha","il furgone","der Lieferwagen","фургон","شاحنة صغيرة","厢式货车"],
 "warmth": ["noun","the quality of being warm; gentle heat","la chaleur","el calor","o calor","il calore","die Wärme","тепло","دفء","温暖"],
 "watchman": ["noun","a person who guards a building, especially at night","le gardien","el vigilante","o guarda-noturno","il guardiano","der Wächter","сторож","حارس","看守人"],
 "folder": ["noun","a cover for holding papers together","le dossier","la carpeta","a pasta","la cartella","der Ordner","папка","مجلد","文件夹"],
 "hoarding": ["noun","a temporary wooden fence around a building site","la palissade","la valla de obra","o tapume","la recinzione","der Bauzaun","строительный забор","سياج مؤقت","工地围栏"],
 "boathouse": ["noun","a building beside water where boats are kept","le hangar à bateaux","el cobertizo para botes","o abrigo de barcos","la rimessa per barche","das Bootshaus","лодочный сарай","بيت القوارب","船屋"],
 "launderette": ["noun","a shop with machines where you pay to wash clothes","la laverie","la lavandería","a lavandaria","la lavanderia a gettoni","der Waschsalon","прачечная самообслуживания","مغسلة","自助洗衣店"],
 "kettle": ["noun","a container for boiling water","la bouilloire","el hervidor","a chaleira","il bollitore","der Wasserkocher","чайник","غلاية","水壶"],
 "radiator": ["noun","a metal heater on a wall that warms a room","le radiateur","el radiador","o radiador","il radiatore","der Heizkörper","радиатор","مشعاع","暖气片"],
 "newsstand": ["noun","a small stall that sells newspapers","le kiosque à journaux","el quiosco de prensa","a banca de jornais","l'edicola","der Zeitungskiosk","газетный киоск","كشك جرائد","报摊"],
 "oar": ["noun","a long pole with a flat end for rowing a boat","la rame","el remo","o remo","il remo","das Ruder","весло","مجداف","桨"],
 "swindle": ["noun","a clever trick to take someone's money","l'arnaque","la estafa","a fraude","la truffa","der Betrug","афёра","احتيال","骗局"],
 "rucksack": ["noun","a bag you carry on your back","le sac à dos","la mochila","a mochila","lo zaino","der Rucksack","рюкзак","حقيبة ظهر","背包"],
 "stall": ["noun","a small open shop or table in a market","l'étal","el puesto","a banca","la bancarella","der Stand","прилавок","بسطة","摊位"],
 "weed": ["noun","a wild plant growing where it is not wanted","la mauvaise herbe","la mala hierba","a erva daninha","l'erbaccia","das Unkraut","сорняк","عشب ضار","杂草"],
 "mattress": ["noun","the soft part of a bed you lie on","le matelas","el colchón","o colchão","il materasso","die Matratze","матрас","مرتبة","床垫"],
 "cobble": ["noun","a rounded stone used to cover old streets","le pavé","el adoquín","a pedra da calçada","il ciottolo","der Pflasterstein","булыжник","حجر رصف","鹅卵石"],
 "gutter": ["noun","the low edge of a road where rain water runs away","le caniveau","la cuneta","a sarjeta","il rigagnolo","die Gosse","сточный жёлоб","مجرى الماء","路边水沟"],
 "kerb": ["noun","the raised edge between a pavement and a road","le bord du trottoir","el bordillo","o meio-fio","il cordolo","der Bordstein","бордюр","حافة الرصيف","路缘"],
 "dashboard": ["noun","the panel of controls in front of a driver","le tableau de bord","el salpicadero","o painel de instrumentos","il cruscotto","das Armaturenbrett","приборная панель","لوحة القيادة","仪表板"],
 "concourse": ["noun","a large open hall in a station or airport","le hall","el vestíbulo","o átrio","l'atrio","die Bahnhofshalle","вестибюль вокзала","بهو المحطة","车站大厅"],
 "docket": ["noun","a small paper or note that records something","le bon","el comprobante","o talão","lo scontrino","der Beleg","квитанция","إيصال","单据"],
 "envelope": ["noun","the paper cover for a letter","l'enveloppe","el sobre","o envelope","la busta","der Umschlag","конверт","مظروف","信封"],
 "letterhead": ["noun","the printed name and address at the top of a firm's paper","l'en-tête","el membrete","o cabeçalho","la carta intestata","der Briefkopf","фирменный бланк","ترويسة الرسالة","信头"],
 "panel": ["noun","a flat piece of wood, glass or metal","le panneau","el panel","o painel","il pannello","die Tafel","панель","لوح","嵌板"],
 "scrap": ["noun","a small piece of something, especially paper","le bout","el trozo","o pedaço","il pezzetto","der Fetzen","клочок","قصاصة","碎片"],
 "arrow": ["noun","a sign shaped like → that shows a direction","la flèche","la flecha","a seta","la freccia","der Pfeil","стрелка","سهم","箭头"],
 "glow": ["noun","a soft, steady light","la lueur","el resplandor","o brilho","il bagliore","der Schein","свечение","توهج","微光"],
 "thread": ["noun","a thin line of something; the line of an idea","le fil","el hilo","o fio","il filo","der Faden","нить","خيط","线索"],
 "attendant": ["noun","a person whose job is to help or serve in a place","l'employé","el encargado","o funcionário","l'addetto","der Angestellte","служащий","موظف","服务员"],
 "colleague": ["noun","a person you work with","le collègue","el colega","o colega","il collega","der Kollege","коллега","زميل","同事"],
 "candidate": ["noun","a person hoping to be chosen for a job","le candidat","el candidato","o candidato","il candidato","der Bewerber","кандидат","مرشح","应聘者"],
 "regular": ["noun","a customer who comes to a place often","l'habitué","el cliente habitual","o cliente habitual","il cliente abituale","der Stammkunde","завсегдатай","زبون دائم","常客"],
 "development": ["noun","a group of new buildings built together","le complexe immobilier","el complejo","o empreendimento","il complesso edilizio","die Wohnanlage","новостройка","مجمع","开发项目"],
 "battery": ["noun","the part that stores power for a phone or car","la batterie","la batería","a bateria","la batteria","der Akku","аккумулятор","بطارية","电池"],
 "reference": ["noun","a number or word used to find something on a list","la référence","la referencia","a referência","il riferimento","die Referenznummer","учётный номер","رقم مرجعي","编号"],
 "fox": ["noun","a wild animal like a small dog, with red-brown fur","le renard","el zorro","a raposa","la volpe","der Fuchs","лиса","ثعلب","狐狸"],
 "shutter": ["noun","a metal or wooden cover that closes over a window or shop","le rideau métallique","la persiana","o gradeamento","la saracinesca","der Rollladen","ставень","مصراع","卷帘"],
 "pity": ["noun","a sad feeling for someone else's trouble","la pitié","la lástima","a pena","la pietà","das Mitleid","жалость","شفقة","怜悯"],
 # --- verbs ---
 "pour": ["verb","to make a liquid flow out of a container","verser","verter","despejar","versare","gießen","наливать","يصب","倒"],
 "fold": ["verb","to bend something so one part lies over another","plier","doblar","dobrar","piegare","falten","складывать","يطوي","折叠"],
 "wave": ["verb","to move your hand to say hello or goodbye","faire signe de la main","saludar con la mano","acenar","salutare con la mano","winken","махать","يلوّح","挥手"],
 "slide": ["verb","to move smoothly along a surface","glisser","deslizar","deslizar","scivolare","gleiten","скользить","ينزلق","滑动"],
 "sigh": ["verb","to let out a long breath, often when tired or sad","soupirer","suspirar","suspirar","sospirare","seufzen","вздыхать","يتنهد","叹气"],
 "shrug": ["verb","to raise your shoulders to show you don't know or care","hausser les épaules","encogerse de hombros","encolher os ombros","alzare le spalle","mit den Schultern zucken","пожимать плечами","يهز كتفيه","耸肩"],
 "hum": ["verb","to sing with your lips closed; to make a low, steady sound","fredonner","tararear","cantarolar","canticchiare","summen","напевать","يدندن","哼"],
 "idle": ["verb","(of an engine) to run gently while the vehicle waits","tourner au ralenti","estar al ralentí","ficar em ponto morto","stare al minimo","im Leerlauf laufen","работать на холостом ходу","يعمل في وضع الخمول","怠速运转"],
 "scrape": ["verb","to rub against a surface with a rough sound","racler","raspar","raspar","raschiare","kratzen","скрести","يكشط","刮"],
 "stack": ["verb","to put things one on top of another","empiler","apilar","empilhar","impilare","stapeln","складывать в стопку","يكدّس","堆叠"],
 "wrap": ["verb","to put something around another thing to cover it","envelopper","envolver","embrulhar","avvolgere","einwickeln","заворачивать","يلفّ","包裹"],
 "breathe": ["verb","to take air in and let it out","respirer","respirar","respirar","respirare","atmen","дышать","يتنفس","呼吸"],
 "freeze": ["verb","to become very cold; to stop still suddenly","geler","congelarse","gelar","gelare","frieren","замерзать","يتجمد","冻僵"],
 "settle": ["verb","to sit or rest comfortably; to sort something out","s'installer","acomodarse","acomodar-se","sistemarsi","sich niederlassen","устраиваться","يستقر","安顿"],
 "overhear": ["verb","to hear what others say without them knowing","surprendre une conversation","oír por casualidad","ouvir por acaso","sentire per caso","zufällig hören","подслушать","يسمع مصادفةً","无意中听到"],
 "rehearse": ["verb","to practise words or actions before doing them","répéter","ensayar","ensaiar","provare","proben","репетировать","يتدرّب","排练"],
 "murmur": ["verb","to say something in a low, soft voice","murmurer","murmurar","murmurar","mormorare","murmeln","бормотать","يتمتم","低声说"],
 "glance": ["verb","to look at something quickly","jeter un coup d'œil","echar un vistazo","dar uma olhadela","dare un'occhiata","kurz blicken","взглянуть","يلمح","瞥一眼"],
 "trot": ["verb","to move at a quick, light run","trotter","trotar","trotar","trottare","traben","бежать трусцой","يهرول","小跑"],
 "weep": ["verb","to cry","pleurer","llorar","chorar","piangere","weinen","плакать","يبكي","哭泣"],
 "drag": ["verb","to pull something heavy along","traîner","arrastrar","arrastar","trascinare","schleppen","тащить","يجرّ","拖"],
 "suspect": ["verb","to think something is probably true, without being sure","soupçonner","sospechar","suspeitar","sospettare","vermuten","подозревать","يشتبه","怀疑"],
 "realise": ["verb","to suddenly understand something","se rendre compte","darse cuenta","aperceber-se","rendersi conto","erkennen","осознавать","يدرك","意识到"],
 "refuse": ["verb","to say firmly that you will not do or accept something","refuser","rechazar","recusar","rifiutare","ablehnen","отказываться","يرفض","拒绝"],
 "vanish": ["verb","to disappear suddenly and completely","disparaître","desvanecerse","desaparecer","svanire","verschwinden","исчезать","يتلاشى","消失"],
 # --- adjectives ---
 "ordinary": ["adjective","normal; not special","ordinaire","corriente","comum","ordinario","gewöhnlich","обычный","عادي","普通的"],
 "unfamiliar": ["adjective","not known to you","inconnu","desconocido","desconhecido","sconosciuto","unbekannt","незнакомый","غير مألوف","陌生的"],
 "shuttered": ["adjective","closed with a metal or wooden cover","aux volets fermés","con la persiana bajada","fechado com grade","con la saracinesca abbassata","mit geschlossenen Läden","с закрытыми ставнями","مغلق بالمصاريع","关着卷帘的"],
 "faded": ["adjective","with the colour or print gone pale","délavé","descolorido","desbotado","sbiadito","verblasst","выцветший","باهت","褪色的"],
 "torn": ["adjective","pulled apart or damaged; ripped","déchiré","roto","rasgado","strappato","zerrissen","порванный","ممزق","撕破的"],
 "creased": ["adjective","with untidy folds or lines pressed into it","froissé","arrugado","amarrotado","spiegazzato","zerknittert","мятый","مجعد","起皱的"],
 "crumpled": ["adjective","crushed into untidy folds","chiffonné","estrujado","amassado","accartocciato","zerknüllt","смятый","مكرمش","皱巴巴的"],
 "burnt": ["adjective","damaged or marked by fire","brûlé","quemado","queimado","bruciato","verbrannt","сгоревший","محترق","烧焦的"],
 "blurred": ["adjective","not clear; with unclear edges","flou","borroso","desfocado","sfocato","verschwommen","размытый","ضبابي","模糊的"],
 "ashamed": ["adjective","feeling bad about something you have done","honteux","avergonzado","envergonhado","vergognoso","beschämt","пристыженный","خجل","羞愧的"],
 "proud": ["adjective","pleased with yourself; or too sure of your own worth","fier","orgulloso","orgulhoso","orgoglioso","stolz","гордый","فخور","自豪的"],
 "glad": ["adjective","pleased and happy about something","content","contento","contente","contento","froh","рад","سعيد","高兴的"],
 "steady": ["adjective","firm and not shaking; regular","stable","firme","firme","fermo","ruhig","устойчивый","ثابت","稳定的"],
 "restful": ["adjective","calm and peaceful; giving rest","reposant","relajante","tranquilo","riposante","erholsam","умиротворяющий","مريح","宁静的"],
 "decent": ["adjective","good and honest; kind","honnête","decente","decente","perbene","anständig","порядочный","لائق","正派的"],
 "punctual": ["adjective","arriving exactly on time","ponctuel","puntual","pontual","puntuale","pünktlich","пунктуальный","دقيق المواعيد","准时的"],
 "hollow": ["adjective","empty inside; without real feeling or value","creux","hueco","oco","vuoto","hohl","пустой","أجوف","空洞的"],
 "lone": ["adjective","single; on its own","solitaire","solitario","solitário","solitario","einzeln","одинокий","وحيد","孤单的"],
 "tiny": ["adjective","extremely small","minuscule","diminuto","minúsculo","minuscolo","winzig","крошечный","ضئيل","微小的"],
 "stark": ["adjective","plain and clear, often in a harsh way","cru","crudo","cru","netto","schroff","резкий","صارخ","鲜明的"],
}

entries = book["lexicon"]["entries"]
added = 0
for base, vals in E.items():
    pos, en, *tr = vals
    assert len(tr) == 8, base
    if base in entries:
        continue
    entries[base] = {"pos": pos, "en": en, **dict(zip(L, tr))}
    added += 1

json.dump(book, open(EP, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(f"Lexicon: +{added} words → {len(entries)} total (needs native review).")
