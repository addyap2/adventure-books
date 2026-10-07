#!/usr/bin/env python3
"""Phase 4: lexicon for book 8, 'The Refuge'.

Base-keyed glossary, 9 languages. Pools the vetted entries from books 1-7 (which
share most of the night/cold/rescue vocabulary), keeps those whose word actually
appears in book 8, and adds hand-authored refuge/mountain-specific entries. Capped
at ~250, coverage-first so every hard A2/B1 word that the catalogue can cover gets
an entry (no hard-word warnings). Translations need a native speaker's check.

Run: python3 scripts/build_ep08_lexicon.py
"""
import json, os, re
from collections import Counter

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
EP = os.path.join(ROOT, "content", "episode-08.json")
TARGET = 250

# hand-authored refuge / mountain / weather / warmth entries (base-keyed)
REFUGE = {
 "refuge":   {"pos":"noun","en":"a shelter hut in the mountains","fr":"le refuge","es":"el refugio","pt":"o refúgio","it":"il rifugio","de":"die Schutzhütte","ru":"приют","ar":"الملجأ","zh":"山间小屋"},
 "hut":      {"pos":"noun","en":"a small, rough shelter","fr":"la cabane","es":"la cabaña","pt":"a cabana","it":"la capanna","de":"die Hütte","ru":"хижина","ar":"الكوخ","zh":"小屋"},
 "bothy":    {"pos":"noun","en":"a simple stone shelter for walkers","fr":"l'abri de montagne","es":"el refugio de piedra","pt":"o abrigo de pedra","it":"il ricovero di pietra","de":"die Biwakhütte","ru":"каменная хижина","ar":"المأوى الحجري","zh":"石砌山棚"},
 "bivvy":    {"pos":"noun","en":"a very small emergency shelter","fr":"le bivouac","es":"el vivac","pt":"o bivaque","it":"il bivacco","de":"der Biwaksack","ru":"бивуак","ar":"المبيت المكشوف","zh":"露营简棚"},
 "warden":   {"pos":"noun","en":"the person who keeps a refuge","fr":"le gardien","es":"el guarda","pt":"o guarda","it":"il custode","de":"der Hüttenwart","ru":"смотритель","ar":"الحارس","zh":"看守人"},
 "whiteout": {"pos":"noun","en":"a blizzard where everything is lost in white","fr":"le voile blanc","es":"la ventisca cegadora","pt":"o nevão cegante","it":"la tempesta bianca","de":"der Whiteout","ru":"белая мгла","ar":"العاصفة البيضاء","zh":"白毛风"},
 "blizzard": {"pos":"noun","en":"a fierce snowstorm","fr":"le blizzard","es":"la ventisca","pt":"a tempestade de neve","it":"la bufera di neve","de":"der Schneesturm","ru":"метель","ar":"العاصفة الثلجية","zh":"暴风雪"},
 "stove":    {"pos":"noun","en":"a closed fire that heats a room","fr":"le poêle","es":"la estufa","pt":"o fogão","it":"la stufa","de":"der Ofen","ru":"печь","ar":"الموقد","zh":"炉子"},
 "loft":     {"pos":"noun","en":"a sleeping space up under the roof","fr":"la soupente","es":"el altillo","pt":"o sótão","it":"il soppalco","de":"der Dachboden","ru":"чердак","ar":"العلّية","zh":"阁楼"},
 "ladder":   {"pos":"noun","en":"a set of rungs for climbing up","fr":"l'échelle","es":"la escalera de mano","pt":"a escada de mão","it":"la scala a pioli","de":"die Leiter","ru":"лестница","ar":"السُّلّم","zh":"梯子"},
 "cornice":  {"pos":"noun","en":"an overhang of snow at a ridge edge","fr":"la corniche de neige","es":"la cornisa de nieve","pt":"a cornija de neve","it":"la cornice di neve","de":"die Schneewächte","ru":"снежный карниз","ar":"الإفريز الثلجي","zh":"雪檐"},
 "corrie":   {"pos":"noun","en":"a bowl-shaped hollow high on a mountain","fr":"le cirque glaciaire","es":"el circo glaciar","pt":"o circo glaciar","it":"il circo glaciale","de":"das Kar","ru":"кар","ar":"الدائرة الجبلية","zh":"冰斗"},
 "slope":    {"pos":"noun","en":"the sloping side of a hill","fr":"la pente","es":"la ladera","pt":"a encosta","it":"il pendio","de":"der Hang","ru":"склон","ar":"المنحدر","zh":"山坡"},
 "ridge":    {"pos":"noun","en":"the long top edge of a mountain","fr":"la crête","es":"la cresta","pt":"a crista","it":"la cresta","de":"der Grat","ru":"гребень","ar":"الحافة","zh":"山脊"},
 "glen":     {"pos":"noun","en":"a narrow mountain valley","fr":"le vallon","es":"la cañada","pt":"o vale estreito","it":"la valletta","de":"das Bergtal","ru":"горная долина","ar":"الوادي","zh":"山谷"},
 "kindling": {"pos":"noun","en":"small dry sticks for starting a fire","fr":"le petit bois","es":"la leña menuda","pt":"os gravetos","it":"la legna minuta","de":"das Anmachholz","ru":"растопка","ar":"الحطب الصغير","zh":"引火柴"},
 "grate":    {"pos":"noun","en":"the metal frame that holds a fire","fr":"la grille du foyer","es":"la rejilla del hogar","pt":"a grelha da lareira","it":"la grata del focolare","de":"der Feuerrost","ru":"колосник","ar":"مِشبك الموقد","zh":"炉箅"},
 "mitts":    {"pos":"noun","en":"thick gloves for the cold","fr":"les moufles","es":"las manoplas","pt":"as mitenes","it":"le manopole","de":"die Fäustlinge","ru":"варежки","ar":"القفّازات","zh":"连指手套"},
 "surveyor": {"pos":"noun","en":"a person who measures and values land","fr":"l'arpenteur","es":"el agrimensor","pt":"o agrimensor","it":"il geometra","de":"der Landvermesser","ru":"землемер","ar":"المسّاح","zh":"测量员"},
 "shepherd": {"pos":"noun","en":"a person who looks after sheep","fr":"le berger","es":"el pastor","pt":"o pastor","it":"il pastore","de":"der Schäfer","ru":"пастух","ar":"الراعي","zh":"牧羊人"},
 "radio":    {"pos":"noun","en":"a device for talking over a distance","fr":"la radio","es":"la radio","pt":"o rádio","it":"la radio","de":"das Funkgerät","ru":"рация","ar":"جهاز اللاسلكي","zh":"无线电"},
 "drift":    {"pos":"noun","en":"a bank of snow heaped by the wind","fr":"la congère","es":"el ventisquero","pt":"o monte de neve","it":"il cumulo di neve","de":"die Schneewehe","ru":"сугроб","ar":"كثيب الثلج","zh":"雪堆"},
 "glass":    {"pos":"noun","en":"a barometer; an instrument that reads the weather","fr":"le baromètre","es":"el barómetro","pt":"o barómetro","it":"il barometro","de":"das Barometer","ru":"барометр","ar":"البارومتر","zh":"气压表"},
 "draw":     {"pos":"verb","en":"(of a fire) to pull air so it burns well","fr":"tirer","es":"tirar","pt":"puxar o ar","it":"tirare","de":"ziehen","ru":"тянуть","ar":"يسحب الهواء","zh":"抽风"},
 "bank":     {"pos":"verb","en":"to heap a fire so it burns low and long","fr":"couvrir le feu","es":"cubrir el fuego","pt":"abafar o fogo","it":"coprire il fuoco","de":"das Feuer abdecken","ru":"загребать жар","ar":"يغطّي الجمر","zh":"封火"},
 "fuel":     {"pos":"noun","en":"what you burn to make heat","fr":"le combustible","es":"el combustible","pt":"o combustível","it":"il combustibile","de":"der Brennstoff","ru":"топливо","ar":"الوقود","zh":"燃料"},
 "wick":     {"pos":"noun","en":"the cord in a lamp that carries the flame","fr":"la mèche","es":"la mecha","pt":"o pavio","it":"lo stoppino","de":"der Docht","ru":"фитиль","ar":"الفتيل","zh":"灯芯"},
 "oil":      {"pos":"noun","en":"lamp fuel; a smooth liquid that burns","fr":"le pétrole lampant","es":"el queroseno","pt":"o petróleo","it":"il cherosene","de":"das Lampenöl","ru":"керосин","ar":"زيت المصباح","zh":"灯油"},
 "team":     {"pos":"noun","en":"a group who work together, here a rescue team","fr":"l'équipe","es":"el equipo","pt":"a equipa","it":"la squadra","de":"die Mannschaft","ru":"команда","ar":"الفريق","zh":"救援队"},
 "mountain": {"pos":"noun","en":"a very high, steep hill","fr":"la montagne","es":"la montaña","pt":"a montanha","it":"la montagna","de":"der Berg","ru":"гора","ar":"الجبل","zh":"山"},
 "sacking":  {"pos":"noun","en":"rough cloth, used for cover or wrapping","fr":"la toile à sac","es":"la arpillera","pt":"a serapilheira","it":"la tela da sacchi","de":"das Sackleinen","ru":"мешковина","ar":"الخيش","zh":"粗麻布"},
 "draught":  {"pos":"noun","en":"a current of cold air through a gap","fr":"le courant d'air","es":"la corriente de aire","pt":"a corrente de ar","it":"la corrente d'aria","de":"der Luftzug","ru":"сквозняк","ar":"تيّار الهواء البارد","zh":"穿堂冷风"},
 "valley":   {"pos":"noun","en":"the low land between hills or mountains","fr":"la vallée","es":"el valle","pt":"o vale","it":"la valle","de":"das Tal","ru":"долина","ar":"الوادي","zh":"山谷"},
 "adult":    {"pos":"noun","en":"a fully grown person","fr":"l'adulte","es":"el adulto","pt":"o adulto","it":"l'adulto","de":"der Erwachsene","ru":"взрослый","ar":"البالغ","zh":"成年人"},
 "bar":      {"pos":"verb","en":"to shut or block firmly","fr":"verrouiller","es":"atrancar","pt":"trancar","it":"sbarrare","de":"verriegeln","ru":"запирать на засов","ar":"يُوصد","zh":"闩住"},
 "bunkroom": {"pos":"noun","en":"a room full of built-in beds","fr":"le dortoir","es":"el dormitorio común","pt":"o dormitório","it":"la camerata","de":"der Schlafsaal","ru":"спальный зал","ar":"غرفة الأسرّة","zh":"集体寝室"},
 "bunk":     {"pos":"noun","en":"a narrow built-in bed","fr":"la couchette","es":"la litera","pt":"o beliche","it":"la cuccetta","de":"die Pritsche","ru":"койка","ar":"السرير المثبّت","zh":"铺位"},
 "cache":    {"pos":"noun","en":"a hidden store of supplies","fr":"la réserve","es":"el depósito oculto","pt":"o depósito escondido","it":"la scorta nascosta","de":"das Versteck","ru":"тайник","ar":"المخزن المخبّأ","zh":"储备点"},
 "choke":    {"pos":"verb","en":"to block, or to struggle to burn or breathe","fr":"s'étouffer","es":"ahogarse","pt":"sufocar","it":"soffocare","de":"ersticken","ru":"глохнуть","ar":"يختنق","zh":"噎住"},
 "condemn":  {"pos":"verb","en":"to declare a building unfit to use","fr":"déclarer insalubre","es":"declarar en ruina","pt":"condenar o edifício","it":"dichiarare inagibile","de":"für unbewohnbar erklären","ru":"признать непригодным","ar":"يحكم بعدم الصلاحية","zh":"判为危房"},
 "loose":    {"pos":"adjective","en":"not firmly fixed; unstable","fr":"meuble","es":"suelto","pt":"solto","it":"instabile","de":"locker","ru":"рыхлый","ar":"غير ثابت","zh":"松动的"},
 "mile":     {"pos":"noun","en":"a unit of distance, about 1.6 kilometres","fr":"le mille","es":"la milla","pt":"a milha","it":"il miglio","de":"die Meile","ru":"миля","ar":"الميل","zh":"英里"},
 "rescue":   {"pos":"noun","en":"the saving of someone from danger","fr":"le sauvetage","es":"el rescate","pt":"o resgate","it":"il soccorso","de":"die Rettung","ru":"спасение","ar":"الإنقاذ","zh":"救援"},
 "smoky":    {"pos":"adjective","en":"full of smoke","fr":"enfumé","es":"humeante","pt":"fumarento","it":"fumoso","de":"rauchig","ru":"дымный","ar":"مليء بالدخان","zh":"冒烟的"},
 "walker":   {"pos":"noun","en":"a person who walks in the hills; a hiker","fr":"le randonneur","es":"el senderista","pt":"o caminhante","it":"l'escursionista","de":"der Wanderer","ru":"турист","ar":"المتنزّه","zh":"徒步者"},
}

MUST = ["refuge","hut","bothy","warden","whiteout","blizzard","stove","loft","ladder",
        "cornice","corrie","slope","ridge","glen","kindling","grate","mitts","surveyor",
        "shepherd","radio","drift","glass","draw","bank","fuel","wick","oil","team",
        "mountain","sacking","draught",
        # common hard words elsewhere in the book
        "snow","storm","wind","cold","dark","dawn","lamp","flame","fire","wood","coat",
        "blanket","frozen","chest","breath","steady","frightened","relief","grip","huddle",
        "gnaw","crawl","cruel","brave","rotten","slick","curl","torch","grandchild","kindness",
        "pale","soaked","chilled"]

SUFFIX = (("s",""),("es",""),("ies","y"),("ed",""),("ed","e"),("ied","y"),
          ("ing",""),("ing","e"),("er",""),("er","e"),("est",""),("ly",""),
          ("ily","y"),("ally","al"),("ably","able"),("ibly","ible"),("'s",""))

def in_core(word, core):
    if word in core: return True
    for suf,repl in SUFFIX:
        if word.endswith(suf) and len(word)-len(suf) >= 2:
            c = word[:-len(suf)]+repl
            if c in core: return True
            if len(c) > 3 and c[-1]==c[-2] and c[:-1] in core: return True
    return False

def resolve(word, keys):
    if word in keys: return word
    for suf,repl in SUFFIX:
        if word.endswith(suf) and len(word)-len(suf) >= 2:
            c = word[:-len(suf)]+repl
            if c in keys: return c
            if len(c) > 3 and c[-1]==c[-2] and c[:-1] in keys: return c[:-1]
    return None

def forms(b):
    s={b,b+"s",b+"es",b+"d",b+"ed",b+"ing"}
    if b.endswith("e"): s|={b[:-1]+"ing",b+"d"}
    if b.endswith("y"): s|={b[:-1]+"ies"}
    return s

def main():
    d = json.load(open(EP, encoding="utf-8"))
    core = {w.strip().lower() for w in open(os.path.join(ROOT,"scripts","wordlist_core.txt"),encoding="utf-8") if w.strip()}

    freq = Counter(); checked = Counter()
    for n in d["nodes"]:
        for lvl in ("A2","B1","B2"):
            for w in re.findall(r"[a-z]+(?:'[a-z]+)?", n["text"][lvl].lower()):
                freq[w]+=1
                if lvl in ("A2","B1"): checked[w]+=1
        for c in n.get("choices",[]):
            for w in re.findall(r"[a-z]+", c["text"]["A2"].lower()):
                freq[w]+=1; checked[w]+=1
    present = set(freq)

    pool = {}
    for ep in range(1,8):
        b = json.load(open(os.path.join(ROOT,"content","episode-0%d.json"%ep), encoding="utf-8"))
        for k,v in b["lexicon"]["entries"].items():
            pool.setdefault(k,v)
    catalogue = dict(pool); catalogue.update(REFUGE)
    cat_keys = set(catalogue)

    def ep_freq(base):
        return sum(freq[f] for f in forms(base) if f in freq) + freq.get(base,0)

    needed = set()
    for w in checked:
        if in_core(w, core): continue
        k = resolve(w, cat_keys)
        if k: needed.add(k)
    entries = {k: catalogue[k] for k in needed}
    for k,v in REFUGE.items():
        if k not in entries and (forms(k)&present or k in present):
            entries[k]=v
    hits = [k for k in pool if (forms(k)&present or k in present) and k not in entries]
    hits.sort(key=lambda k: ep_freq(k), reverse=True)
    for k in hits:
        if len(entries) >= TARGET: break
        entries[k]=pool[k]
    for k in MUST:
        if k not in entries and k in catalogue: entries[k]=catalogue[k]

    entries = {k:entries[k] for k in sorted(entries)}
    d["lexicon"]["entries"] = entries
    json.dump(d, open(EP,"w",encoding="utf-8"), indent=2, ensure_ascii=False)
    uncov = sorted({w for w in checked if not in_core(w,core) and not resolve(w,set(entries))})
    print("the-refuge lexicon: %d entries. Uncovered hard words: %s" % (len(entries), uncov or "none"))

if __name__ == "__main__":
    main()
