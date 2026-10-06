#!/usr/bin/env python3
"""One-off: build episode 1's chosen per-book lexicon and embed it in the episode JSON.

Words are chosen from the story's own non-core vocabulary (see the validator's advisory
list). Keyed by base form; the reader's suffix rules catch plurals, past tenses and -ly
adverbs. Translations follow the platform's eight languages; nouns carry their article.

NOTE: like every gloss in this project, these translations still want a native speaker's
check before launch — a wrong gloss the learner cannot detect is worse than no gloss.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.join(HERE, "..", "content", "episode-01.json")
SHARED = os.path.join(HERE, "..", "content", "lexicon.json")

# base : [pos, en, fr, es, pt, it, de, ru, ar, zh]
E = {
 "kiosk": ["noun","a very small shop on a street that sells newspapers, drinks and small things","le kiosque","el quiosco","o quiosque","il chiosco","der Kiosk","киоск","كشك","报刊亭"],
 "dust": ["noun","dry dirt like powder that covers things nobody cleans","la poussière","el polvo","a poeira","la polvere","der Staub","пыль","غبار","灰尘"],
 "dusty": ["adjective","covered with dust","poussiéreux","polvoriento","empoeirado","polveroso","staubig","пыльный","مغبر","满是灰尘的"],
 "agency": ["noun","a company that finds work for people, usually for money","l'agence","la agencia","a agência","l'agenzia","die Agentur","агентство","وكالة","中介机构"],
 "calendar": ["noun","a page or book that shows the days and months of a year","le calendrier","el calendario","o calendário","il calendario","der Kalender","календарь","تقويم","日历"],
 "bench": ["noun","a long hard seat for two or more people, often outside","le banc","el banco","o banco","la panchina","die Bank","скамейка","مقعد","长椅"],
 "cleaner": ["noun","a person whose job is to clean a building","l'agent d'entretien","la limpiadora","a faxineira","l'addetta alle pulizie","die Reinigungskraft","уборщица","عاملة نظافة","清洁工"],
 "quay": ["noun","a hard flat place next to water where boats stop; said like KEY","le quai","el muelle","o cais","la banchina","der Kai","набережная","رصيف الميناء","码头"],
 "receipt": ["noun","a small paper that shows you paid for something; said like ri-SEET","le reçu","el recibo","o recibo","la ricevuta","die Quittung","квитанция","إيصال","收据"],
 "reception": ["noun","the desk near the door of a building where visitors go first","la réception","la recepción","a receção","la reception","der Empfang","рецепция","الاستقبال","前台"],
 "receptionist": ["noun","the person who works at the reception desk","le/la réceptionniste","el/la recepcionista","o/a rececionista","il/la receptionist","der Empfangsmitarbeiter","администратор","موظف الاستقبال","前台接待员"],
 "label": ["noun","a small piece of paper or plastic on a thing, with writing on it","l'étiquette","la etiqueta","a etiqueta","l'etichetta","das Etikett","бирка","بطاقة","标签"],
 "interview": ["noun","a meeting where a company asks you questions about a job","l'entretien","la entrevista","a entrevista","il colloquio","das Vorstellungsgespräch","собеседование","مقابلة عمل","面试"],
 # --- new nouns ---
 "cafe": ["noun","a small place where you buy and drink coffee and eat light food","le café","la cafetería","o café","il caffè","das Café","кафе","مقهى","咖啡馆"],
 "information": ["noun","facts you are told or that help you know something","l'information","la información","a informação","l'informazione","die Information","информация","معلومات","信息"],
 "midnight": ["noun","twelve o'clock at night","minuit","la medianoche","a meia-noite","la mezzanotte","die Mitternacht","полночь","منتصف الليل","午夜"],
 "daylight": ["noun","the natural light of day","la lumière du jour","la luz del día","a luz do dia","la luce del giorno","das Tageslicht","дневной свет","ضوء النهار","日光"],
 "diary": ["noun","a book where you write what happens each day, or your plans","le journal / l'agenda","el diario / la agenda","o diário / a agenda","il diario / l'agenda","das Tagebuch / der Kalender","дневник / ежедневник","مذكرات / أجندة","日记 / 记事本"],
 "gown": ["noun","a long loose piece of clothing (here: a dressing gown worn at home)","la robe de chambre","la bata","o roupão","la vestaglia","der Morgenmantel","халат","رداء","长袍"],
 "entrance": ["noun","the door or opening where you go into a place","l'entrée","la entrada","a entrada","l'ingresso","der Eingang","вход","مدخل","入口"],
 "pavement": ["noun","the hard path at the side of a road for people to walk on","le trottoir","la acera","o passeio","il marciapiede","der Bürgersteig","тротуар","رصيف","人行道"],
 "registration": ["noun","the act of putting your name on an official list","l'inscription","el registro","o registo","la registrazione","die Anmeldung","регистрация","تسجيل","登记"],
 "screen": ["noun","the flat part of a phone or computer that shows pictures and words","l'écran","la pantalla","o ecrã","lo schermo","der Bildschirm","экран","شاشة","屏幕"],
 "carpet": ["noun","a thick soft cover for a floor","la moquette / le tapis","la alfombra","o tapete","la moquette","der Teppich","ковёр","سجادة","地毯"],
 "napkin": ["noun","a small piece of cloth or paper for your mouth and hands at a meal","la serviette","la servilleta","o guardanapo","il tovagliolo","die Serviette","салфетка","منديل","餐巾"],
 "aisle": ["noun","the long open path you walk along between rows; said like I'LL","l'allée","el pasillo","o corredor","il corridoio","der Gang","проход","ممر","过道"],
 "departure": ["noun","the act of leaving, especially a train or plane","le départ","la salida","a partida","la partenza","die Abfahrt","отправление","مغادرة","出发"],
 "arrival": ["noun","the act of coming to a place","l'arrivée","la llegada","a chegada","l'arrivo","die Ankunft","прибытие","وصول","到达"],
 "luggage": ["noun","the bags and cases you take when you travel","les bagages","el equipaje","a bagagem","i bagagli","das Gepäck","багаж","أمتعة","行李"],
 "photograph": ["noun","a picture made with a camera","la photo","la fotografía","a fotografia","la fotografia","das Foto","фотография","صورة","照片"],
 "sleeve": ["noun","the part of clothing that covers your arm","la manche","la manga","a manga","la manica","der Ärmel","рукав","كم","袖子"],
 "streetlight": ["noun","a tall lamp that lights a street at night","le lampadaire","la farola","o candeeiro de rua","il lampione","die Straßenlaterne","уличный фонарь","مصباح الشارع","路灯"],
 "ceremony": ["noun","a formal set of actions done on an important occasion","la cérémonie","la ceremonia","a cerimónia","la cerimonia","die Zeremonie","церемония","مراسم","仪式"],
 "chin": ["noun","the front part of your face below your mouth","le menton","la barbilla","o queixo","il mento","das Kinn","подбородок","ذقن","下巴"],
 "conclusion": ["noun","the end of something, or the decision you reach","la conclusion","la conclusión","a conclusão","la conclusione","der Schluss","вывод","استنتاج","结论"],
 "defeat": ["noun","the state of having lost; a failure","la défaite","la derrota","a derrota","la sconfitta","die Niederlage","поражение","هزيمة","失败"],
 "evidence": ["noun","facts or things that show something is true","la preuve","la prueba","a prova","la prova","der Beweis","доказательство","دليل","证据"],
 "expense": ["noun","the money that something costs you","la dépense","el gasto","a despesa","la spesa","die Ausgabe","расход","نفقة","费用"],
 "fortnight": ["noun","two weeks","quinze jours","dos semanas","quinze dias","due settimane","zwei Wochen","две недели","أسبوعان","两周"],
 "invitation": ["noun","a spoken or written offer to come somewhere","l'invitation","la invitación","o convite","l'invito","die Einladung","приглашение","دعوة","邀请"],
 "layout": ["noun","the way the parts of something are arranged","la disposition","la disposición","a disposição","la disposizione","die Anordnung","планировка","تخطيط","布局"],
 "nerve": ["noun","the courage to do something difficult","le cran","el valor","a coragem","il coraggio","der Mut","смелость","جرأة","勇气"],
 "patience": ["noun","the calm you keep while waiting or through trouble","la patience","la paciencia","a paciência","la pazienza","die Geduld","терпение","صبر","耐心"],
 "signature": ["noun","your name written in your own way to sign something","la signature","la firma","a assinatura","la firma","die Unterschrift","подпись","توقيع","签名"],
 "steam": ["noun","the hot white gas that comes off boiling water","la vapeur","el vapor","o vapor","il vapore","der Dampf","пар","بخار","蒸汽"],
 "steel": ["noun","a strong hard metal made mostly of iron","l'acier","el acero","o aço","l'acciaio","der Stahl","сталь","فولاذ","钢"],
 "strap": ["noun","a narrow band of leather or cloth for carrying or fastening","la sangle","la correa","a alça","la cinghia","der Riemen","ремень","حزام","带子"],
 "truth": ["noun","what is really true","la vérité","la verdad","a verdade","la verità","die Wahrheit","правда","الحقيقة","真相"],
 "vehicle": ["noun","a machine such as a car or van that carries people or goods","le véhicule","el vehículo","o veículo","il veicolo","das Fahrzeug","транспортное средство","مركبة","车辆"],
 "windscreen": ["noun","the big glass window at the front of a car","le pare-brise","el parabrisas","o para-brisas","il parabrezza","die Windschutzscheibe","лобовое стекло","الزجاج الأمامي","挡风玻璃"],
 "furniture": ["noun","the tables, chairs and beds in a room","les meubles","los muebles","os móveis","i mobili","die Möbel","мебель","أثاث","家具"],
 "appointment": ["noun","a fixed time to meet or be seen by someone","le rendez-vous","la cita","a marcação","l'appuntamento","der Termin","встреча","موعد","预约"],
 "comment": ["noun","a short spoken or written remark about something","le commentaire","el comentario","o comentário","il commento","der Kommentar","замечание","تعليق","评论"],
 "builder": ["noun","a worker who builds or repairs buildings","l'ouvrier du bâtiment","el constructor","o construtor","il muratore","der Bauarbeiter","строитель","عامل بناء","建筑工人"],
 "lunchtime": ["noun","the time in the middle of the day when people eat lunch","l'heure du déjeuner","la hora del almuerzo","a hora do almoço","l'ora di pranzo","die Mittagszeit","обеденное время","وقت الغداء","午餐时间"],
 "fence": ["noun","a wall of wood or wire around a piece of land","la clôture","la valla","a cerca","la recinzione","der Zaun","забор","سياج","栅栏"],
 "gull": ["noun","a grey and white sea bird","la mouette","la gaviota","a gaivota","il gabbiano","die Möwe","чайка","نورس","海鸥"],
 "handle": ["noun","the part of a door or bag you hold to open or carry it","la poignée","el pomo","a maçaneta","la maniglia","die Klinke","ручка","مقبض","把手"],
 "feet": ["noun","more than one foot (the parts you stand on)","les pieds","los pies","os pés","i piedi","die Füße","ступни","أقدام","脚"],
 # --- verbs (infinitive) ---
 "admit": ["verb","to agree that something is true, often unwillingly","admettre","admitir","admitir","ammettere","zugeben","признавать","يعترف","承认"],
 "afford": ["verb","to have enough money for something","se permettre","permitirse","poder pagar","permettersi","sich leisten","позволить себе","يقدر على تحمل","负担得起"],
 "apologise": ["verb","to say sorry","s'excuser","disculparse","pedir desculpa","scusarsi","sich entschuldigen","извиняться","يعتذر","道歉"],
 "arrange": ["verb","to plan or organise something","organiser","organizar","organizar","organizzare","arrangieren","устраивать","يرتب","安排"],
 "assure": ["verb","to tell someone firmly so they stop worrying","assurer","asegurar","assegurar","assicurare","versichern","заверять","يؤكد","向…保证"],
 "bother": ["verb","to make the effort; or to annoy someone","se donner la peine / déranger","molestarse / molestar","incomodar-se / incomodar","preoccuparsi / disturbare","sich bemühen / stören","беспокоиться / беспокоить","يكلف نفسه / يزعج","费心 / 打扰"],
 "brush": ["verb","to touch or clean lightly with a quick movement","frôler / brosser","rozar / cepillar","roçar / escovar","sfiorare / spazzolare","streifen / bürsten","задевать / чистить","يمسح / يفرشي","轻拂 / 刷"],
 "connect": ["verb","to join one thing to another","relier","conectar","ligar","collegare","verbinden","соединять","يربط","连接"],
 "consider": ["verb","to think about something carefully","considérer","considerar","considerar","considerare","erwägen","обдумывать","يفكر في","考虑"],
 "contain": ["verb","to have something inside","contenir","contener","conter","contenere","enthalten","содержать","يحتوي على","包含"],
 "disappear": ["verb","to go out of sight; to stop being there","disparaître","desaparecer","desaparecer","scomparire","verschwinden","исчезать","يختفي","消失"],
 "frown": ["verb","to move your eyebrows down because you are annoyed or thinking","froncer les sourcils","fruncir el ceño","franzir a testa","aggrottare le sopracciglia","die Stirn runzeln","хмуриться","يعبس","皱眉"],
 "haul": ["verb","to pull or carry something heavy with effort","traîner","arrastrar","arrastar","trascinare","schleppen","тащить","يجر","拖"],
 "improve": ["verb","to become or make better","améliorer","mejorar","melhorar","migliorare","verbessern","улучшать","يحسن","改善"],
 "interrupt": ["verb","to stop someone by speaking or acting in the middle","interrompre","interrumpir","interromper","interrompere","unterbrechen","прерывать","يقاطع","打断"],
 "lean": ["verb","to rest against something, or to bend your body","s'appuyer / se pencher","apoyarse / inclinarse","apoiar-se / inclinar-se","appoggiarsi / piegarsi","sich lehnen","прислоняться / наклоняться","يتكئ / ينحني","倚靠 / 倾身"],
 "navigate": ["verb","to find your way from one place to another","se repérer","orientarse","orientar-se","orientarsi","sich zurechtfinden","ориентироваться","يتنقل","导航"],
 "nod": ["verb","to move your head down and up to mean yes","hocher la tête","asentir con la cabeza","acenar com a cabeça","annuire","nicken","кивать","يومئ برأسه","点头"],
 "pause": ["verb","to stop for a short time before going on","faire une pause","hacer una pausa","fazer uma pausa","fare una pausa","innehalten","делать паузу","يتوقف مؤقتا","停顿"],
 "pretend": ["verb","to act as if something is true when it is not","faire semblant","fingir","fingir","fingere","vorgeben","делать вид","يتظاهر","假装"],
 "recognise": ["verb","to know someone or something because you have seen it before","reconnaître","reconocer","reconhecer","riconoscere","erkennen","узнавать","يتعرف على","认出"],
 "reserve": ["verb","to keep something for later or for a certain person","réserver","reservar","reservar","riservare","reservieren","резервировать","يحجز","预留"],
 "survive": ["verb","to stay alive or keep existing through a hard time","survivre","sobrevivir","sobreviver","sopravvivere","überleben","выживать","ينجو","幸存"],
 "suppose": ["verb","to think something is probably true","supposer","suponer","supor","supporre","annehmen","полагать","يفترض","假定"],
 "switch": ["verb","to change from one thing to another; to turn on or off","changer / éteindre","cambiar / apagar","mudar / desligar","cambiare / spegnere","wechseln / schalten","переключать","يبدل","切换 / 开关"],
 "tape": ["verb","to stick something using sticky tape","scotcher","pegar con cinta","colar com fita","attaccare col nastro","kleben","приклеивать скотчем","يلصق بشريط","用胶带贴"],
 "update": ["verb","to add the newest information to something","mettre à jour","actualizar","atualizar","aggiornare","aktualisieren","обновлять","يحدث","更新"],
 "waste": ["verb","to use time or money badly, for nothing","gaspiller","malgastar","desperdiçar","sprecare","verschwenden","тратить впустую","يهدر","浪费"],
 "achieve": ["verb","to succeed in doing or getting something after effort","réaliser","lograr","alcançar","realizzare","erreichen","достигать","يحقق","实现"],
 "approach": ["verb","to come nearer to someone or something","s'approcher","acercarse","aproximar-se","avvicinarsi","sich nähern","приближаться","يقترب","靠近"],
 "annoy": ["verb","to make someone a little angry","agacer","molestar","irritar","infastidire","ärgern","раздражать","يزعج","惹恼"],
 # --- adjectives ---
 "dignified": ["adjective","calm and serious in a way that earns respect","digne","digno","digno","dignitoso","würdevoll","полный достоинства","وقور","有尊严的"],
 "entire": ["adjective","whole; with no part missing","entier","entero","inteiro","intero","gesamt","весь","كامل","整个的"],
 "necessary": ["adjective","needed; that you must have or do","nécessaire","necesario","necessário","necessario","notwendig","необходимый","ضروري","必要的"],
 "accidental": ["adjective","happening by chance, not on purpose","accidentel","accidental","acidental","accidentale","zufällig","случайный","عرضي","偶然的"],
 "charming": ["adjective","pleasant in a way that makes people like you","charmant","encantador","encantador","affascinante","charmant","обаятельный","ساحر","迷人的"],
 "civilised": ["adjective","polite and reasonable in behaviour","civilisé","civilizado","civilizado","civile","zivilisiert","цивилизованный","متحضر","文明的"],
 "enormous": ["adjective","very big","énorme","enorme","enorme","enorme","riesig","огромный","ضخم","巨大的"],
 "exhausted": ["adjective","very tired","épuisé","agotado","exausto","esausto","erschöpft","измотанный","منهك","筋疲力尽的"],
 "identical": ["adjective","exactly the same","identique","idéntico","idêntico","identico","identisch","одинаковый","متطابق","完全相同的"],
 "inner": ["adjective","on the inside; further in","intérieur","interior","interior","interno","innere","внутренний","داخلي","里面的"],
 "intact": ["adjective","not damaged; complete","intact","intacto","intacto","intatto","intakt","целый","سليم","完好无损的"],
 "obvious": ["adjective","easy to see or understand","évident","obvio","óbvio","ovvio","offensichtlich","очевидный","واضح","显而易见的"],
 "original": ["adjective","first; the earliest, before any change","d'origine","original","original","originale","ursprünglich","первоначальный","أصلي","原来的"],
 "pale": ["adjective","light in colour; (of a face) with little colour","pâle","pálido","pálido","pallido","blass","бледный","شاحب","苍白的"],
 "particular": ["adjective","one special one, not any other","particulier","particular","específico","particolare","bestimmt","особый","معين","特定的"],
 "precise": ["adjective","exact and clear","précis","preciso","preciso","preciso","genau","точный","دقيق","精确的"],
 "reliable": ["adjective","that you can trust to work or be right","fiable","fiable","fiável","affidabile","zuverlässig","надёжный","موثوق","可靠的"],
 "sensible": ["adjective","showing good judgement; wise","sensé","sensato","sensato","sensato","vernünftig","разумный","عاقل","明智的"],
 "sinister": ["adjective","seeming evil or that something bad will happen","sinistre","siniestro","sinistro","sinistro","unheimlich","зловещий","مشؤوم","阴森的"],
 "useless": ["adjective","of no use; not working","inutile","inútil","inútil","inutile","nutzlos","бесполезный","عديم الفائدة","没用的"],
 "vast": ["adjective","extremely large in size or amount","vaste","vasto","vasto","vasto","riesig","обширный","شاسع","广大的"],
 "visible": ["adjective","that can be seen","visible","visible","visível","visibile","sichtbar","видимый","مرئي","可见的"],
 "reasonable": ["adjective","fair and sensible; not too much","raisonnable","razonable","razoável","ragionevole","vernünftig","разумный","معقول","合理的"],
 "considerable": ["adjective","large enough to notice; quite a lot","considérable","considerable","considerável","considerevole","beträchtlich","значительный","كبير","相当大的"],
 "heavy": ["adjective","weighing a lot; hard to lift","lourd","pesado","pesado","pesante","schwer","тяжёлый","ثقيل","重的"],
 "genuine": ["adjective","real; not false","authentique","genuino","genuíno","genuino","echt","подлинный","حقيقي","真正的"],
 "immediate": ["adjective","happening at once, with no delay","immédiat","inmediato","imediato","immediato","sofortig","немедленный","فوري","立即的"],
 "eventual": ["adjective","happening in the end, after some time","final","final","final","finale","schließlich","конечный","نهائي","最终的"],
 "natural": ["adjective","normal; as expected; not made by people","naturel","natural","natural","naturale","natürlich","естественный","طبيعي","自然的"],
 "fair": ["adjective","treating people equally and in the right way","juste","justo","justo","giusto","fair","справедливый","عادل","公平的"],
 "actual": ["adjective","real; that truly exists","réel","real","real","reale","tatsächlich","фактический","فعلي","实际的"],
 "brief": ["adjective","short in time","bref","breve","breve","breve","kurz","краткий","موجز","简短的"],
 "pointed": ["adjective","said in a sharp way to make a clear point","incisif","mordaz","incisivo","pungente","spitz","колкий","لاذع","尖锐的"],
 "unkind": ["adjective","not kind; a little cruel","méchant","poco amable","rude","scortese","unfreundlich","недобрый","قاسٍ","不友善的"],
 "faint": ["adjective","weak; not clear or strong","faible","tenue","tênue","debole","schwach","слабый","خافت","微弱的"],
 "proper": ["adjective","real and correct; of the right kind","vrai / correct","adecuado","adequado","adeguato","richtig","настоящий","لائق","真正的"],
 "standard": ["adjective","normal and usual; the ordinary kind","standard","estándar","padrão","standard","üblich","стандартный","قياسي","标准的"],
 # --- adverbs & function words ---
 "anyway": ["adverb","in spite of that; used to return to a point","de toute façon","de todos modos","de qualquer forma","comunque","trotzdem","всё равно","على أي حال","反正"],
 "rather": ["adverb","quite; to a fairly large degree","plutôt","bastante","bastante","piuttosto","ziemlich","довольно","إلى حد ما","相当"],
 "somehow": ["adverb","in a way you do not know or cannot explain","d'une manière ou d'une autre","de algún modo","de algum modo","in qualche modo","irgendwie","как-то","بطريقة ما","不知怎么地"],
 "afterwards": ["adverb","later; after that","après","después","depois","dopo","danach","потом","بعد ذلك","之后"],
 "altogether": ["adverb","completely; in total","tout à fait / en tout","por completo / en total","completamente / no total","del tutto / in tutto","völlig / insgesamt","совсем / всего","تماما / إجمالا","完全 / 总共"],
 "forever": ["adverb","for all time; without ending","pour toujours","para siempre","para sempre","per sempre","für immer","навсегда","إلى الأبد","永远"],
 "halfway": ["adverb","at or to the middle point","à mi-chemin","a medio camino","a meio caminho","a metà strada","auf halbem Weg","на полпути","في منتصف الطريق","半路"],
 "otherwise": ["adverb","if not; in a different way","sinon","de lo contrario","caso contrário","altrimenti","sonst","иначе","وإلا","否则"],
 "regardless": ["adverb","in spite of everything; without caring about it","malgré tout","a pesar de todo","apesar de tudo","nonostante tutto","ungeachtet dessen","несмотря ни на что","بغض النظر","不管怎样"],
 "whoever": ["pronoun","any person who; the person who","quiconque","quienquiera","quem quer que","chiunque","wer auch immer","кто бы ни","أيا كان","无论谁"],
 "within": ["preposition","inside; before the end of a period","à l'intérieur de / en moins de","dentro de","dentro de","entro","innerhalb","в пределах","خلال","在…之内"],
 "further": ["adverb","at or to a greater distance; more","plus loin","más lejos","mais longe","più lontano","weiter","дальше","أبعد","更远"],
 "neither": ["determiner","not one and not the other of two","ni l'un ni l'autre","ninguno de los dos","nenhum dos dois","né l'uno né l'altro","keiner von beiden","ни тот ни другой","لا هذا ولا ذاك","两者都不"],
 "ought": ["verb","should; used to say the right thing to do (ought to)","devoir (on devrait)","deber (debería)","dever (deveria)","dovere (dovrebbe)","sollen","следует","ينبغي","应该"],
 "behalf": ["noun","in the place of, or for, someone else (on behalf of)","au nom de","en nombre de","em nome de","a nome di","im Namen von","от имени","نيابة عن","代表"],
}

def main():
    book = json.load(open(EP, encoding="utf-8"))
    LANGS = ["fr","es","pt","it","de","ru","ar","zh"]
    entries = {}
    for base, vals in E.items():
        pos, en, *tr = vals
        assert len(tr) == 8, base
        entries[base] = {"pos": pos, "en": en, **dict(zip(LANGS, tr))}
    book["lexicon"] = {
        "_comment": "This book's chosen lexicon. Any word here is tappable wherever it "
                    "appears in the story (base form; the reader resolves inflections). "
                    "Translations still need a native speaker's check before launch.",
        "entries": entries,
    }
    # per-paragraph glossary lists are no longer used for marking (auto-gloss reads the
    # lexicon); drop them so the data has one source of truth.
    for n in book["nodes"]:
        n.pop("glossary", None)
    json.dump(book, open(EP, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    # the shared series lexicon becomes an empty base every book inherits from
    json.dump({"_comment": "Shared base lexicon for the series — words common to every "
               "book. Each book adds its own chosen words in its `lexicon` field.",
               "entries": {}},
              open(SHARED, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"Embedded {len(entries)} chosen words into episode-01.json; emptied shared lexicon.json")

if __name__ == "__main__":
    main()
