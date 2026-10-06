#!/usr/bin/env python3
"""Phase 4: lexicon for book 7, 'High Water'.

Base-keyed glossary, 9 languages. Built by pooling the vetted entries from books 1-6
(which share most of High Water's night/rescue vocabulary), keeping those whose word
actually appears in book 7, and adding hand-authored flood-specific entries. Capped at
~250, with every validator-flagged 'hard word' guaranteed present so a reader can tap it.
Translations need a native speaker's check before launch.

Run: python3 scripts/build_ep07_lexicon.py
"""
import json, os, re
from collections import Counter

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
EP07 = os.path.join(ROOT, "content", "episode-07.json")
TARGET = 250

# --- hand-authored flood-specific entries (base-keyed) ---
FLOOD = {
 "flood":    {"pos":"noun","en":"a great overflow of water onto dry land","fr":"l'inondation","es":"la inundación","pt":"a cheia","it":"l'inondazione","de":"die Überschwemmung","ru":"наводнение","ar":"الفيضان","zh":"洪水"},
 "river":    {"pos":"noun","en":"a large natural stream of water","fr":"la rivière","es":"el río","pt":"o rio","it":"il fiume","de":"der Fluss","ru":"река","ar":"النهر","zh":"河"},
 "bank":     {"pos":"noun","en":"the raised ground along the side of a river","fr":"la berge","es":"la orilla","pt":"a margem","it":"la riva","de":"das Ufer","ru":"берег","ar":"الضفة","zh":"河岸"},
 "weir":     {"pos":"noun","en":"a low dam built across a river","fr":"le déversoir","es":"el azud","pt":"o açude","it":"la chiusa","de":"das Wehr","ru":"плотина","ar":"السد المنخفض","zh":"堰"},
 "sandbag":  {"pos":"noun","en":"a sack filled with sand, used to hold back water","fr":"le sac de sable","es":"el saco de arena","pt":"o saco de areia","it":"il sacco di sabbia","de":"der Sandsack","ru":"мешок с песком","ar":"كيس الرمل","zh":"沙袋"},
 "pump":     {"pos":"noun","en":"a machine that moves water","fr":"la pompe","es":"la bomba","pt":"a bomba","it":"la pompa","de":"die Pumpe","ru":"насос","ar":"المضخة","zh":"水泵"},
 "plank":    {"pos":"noun","en":"a long flat piece of wood","fr":"la planche","es":"el tablón","pt":"a tábua","it":"l'asse","de":"das Brett","ru":"доска","ar":"اللوح الخشبي","zh":"木板"},
 "inch":     {"pos":"noun","en":"a small unit of length, about 2.5 centimetres","fr":"le pouce","es":"la pulgada","pt":"a polegada","it":"il pollice","de":"der Zoll","ru":"дюйм","ar":"البوصة","zh":"英寸"},
 "leak":     {"pos":"verb","en":"to let water pass through a hole or gap","fr":"fuir","es":"filtrarse","pt":"vazar","it":"colare","de":"undicht sein","ru":"протекать","ar":"يتسرّب","zh":"漏水"},
 "unbuilt":  {"pos":"adjective","en":"not yet built","fr":"pas encore construit","es":"sin construir","pt":"por construir","it":"non ancora costruito","de":"noch nicht gebaut","ru":"непостроенный","ar":"غير مبنيّ","zh":"尚未垒起的"},
 "spade":    {"pos":"noun","en":"a tool for digging","fr":"la bêche","es":"la pala","pt":"a pá","it":"la vanga","de":"der Spaten","ru":"лопата","ar":"المجراف","zh":"铁锹"},
 "sack":     {"pos":"noun","en":"a large bag of strong cloth","fr":"le sac","es":"el saco","pt":"o saco","it":"il sacco","de":"der Sack","ru":"мешок","ar":"الكيس","zh":"麻袋"},
 "sacking":  {"pos":"noun","en":"rough cloth used to make sacks","fr":"la toile à sac","es":"la arpillera","pt":"a serapilheira","it":"la tela da sacchi","de":"das Sackleinen","ru":"мешковина","ar":"الخيش","zh":"粗麻布"},
 "doorstep": {"pos":"noun","en":"the step in front of a door","fr":"le pas de la porte","es":"el umbral","pt":"a soleira","it":"la soglia","de":"die Türschwelle","ru":"порог","ar":"عتبة الباب","zh":"门阶"},
 "overflow": {"pos":"verb","en":"to flow over the edge or top","fr":"déborder","es":"desbordarse","pt":"transbordar","it":"traboccare","de":"über die Ufer treten","ru":"выходить из берегов","ar":"يفيض","zh":"泛滥"},
 "current":  {"pos":"noun","en":"the flow of water in a river","fr":"le courant","es":"la corriente","pt":"a corrente","it":"la corrente","de":"die Strömung","ru":"течение","ar":"التيار","zh":"水流"},
 "race":     {"pos":"noun","en":"a fast, narrow channel of water","fr":"le bief","es":"el canal de agua","pt":"o canal de água","it":"la gora","de":"der Mühlbach","ru":"быстрый поток","ar":"مجرى الماء السريع","zh":"急流水道"},
 "bridge":   {"pos":"noun","en":"a structure built over a river to cross it","fr":"le pont","es":"el puente","pt":"a ponte","it":"il ponte","de":"die Brücke","ru":"мост","ar":"الجسر","zh":"桥"},
 "pallet":   {"pos":"noun","en":"a wooden base for stacking and moving goods","fr":"la palette","es":"el palé","pt":"a palete","it":"il bancale","de":"die Palette","ru":"поддон","ar":"المنصة الخشبية","zh":"货盘"},
 "yard":     {"pos":"noun","en":"an enclosed work area beside a building","fr":"la cour","es":"el patio","pt":"o estaleiro","it":"il cortile","de":"der Hof","ru":"двор","ar":"الساحة","zh":"场院"},
 "dealer":   {"pos":"noun","en":"a person who buys and sells things for money","fr":"le marchand","es":"el comerciante","pt":"o negociante","it":"il venditore","de":"der Händler","ru":"торговец","ar":"التاجر","zh":"商贩"},
 "mud":      {"pos":"noun","en":"soft, wet earth","fr":"la boue","es":"el barro","pt":"a lama","it":"il fango","de":"der Schlamm","ru":"грязь","ar":"الوحل","zh":"泥"},
 "kerb":     {"pos":"noun","en":"the raised edge where a path meets a road","fr":"la bordure du trottoir","es":"el bordillo","pt":"o meio-fio","it":"il cordolo","de":"die Bordsteinkante","ru":"бордюр","ar":"حافة الرصيف","zh":"路缘"},
 "bail":     {"pos":"verb","en":"to throw water out of something by hand","fr":"écoper","es":"achicar","pt":"escoar a água","it":"aggottare","de":"ausschöpfen","ru":"вычерпывать","ar":"ينزح الماء","zh":"舀水"},
 "barrow":   {"pos":"noun","en":"a small cart you push by hand","fr":"la brouette","es":"la carretilla","pt":"o carrinho de mão","it":"la carriola","de":"die Schubkarre","ru":"тачка","ar":"عربة اليد","zh":"手推车"},
 "drown":    {"pos":"verb","en":"to die under water, unable to breathe","fr":"se noyer","es":"ahogarse","pt":"afogar-se","it":"annegare","de":"ertrinken","ru":"утонуть","ar":"يغرق","zh":"溺水"},
 "rise":     {"pos":"verb","en":"to go up; to become higher","fr":"monter","es":"subir","pt":"subir","it":"salire","de":"steigen","ru":"подниматься","ar":"يرتفع","zh":"上涨"},
 "bucket":   {"pos":"noun","en":"a round open container for carrying water","fr":"le seau","es":"el cubo","pt":"o balde","it":"il secchio","de":"der Eimer","ru":"ведро","ar":"الدلو","zh":"水桶"},
 "rotten":   {"pos":"adjective","en":"decayed; gone soft and weak","fr":"pourri","es":"podrido","pt":"podre","it":"marcio","de":"morsch","ru":"гнилой","ar":"متعفّن","zh":"腐烂的"},
 "cheque":   {"pos":"noun","en":"a written order to pay money from a bank","fr":"le chèque","es":"el cheque","pt":"o cheque","it":"l'assegno","de":"der Scheck","ru":"чек","ar":"الشيك","zh":"支票"},
 "gnaw":     {"pos":"verb","en":"to wear away slowly, as if by biting","fr":"ronger","es":"carcomer","pt":"roer","it":"rodere","de":"nagen","ru":"грызть","ar":"ينهش","zh":"啃噬"},
 "grip":     {"pos":"verb","en":"to hold on to something tightly","fr":"agripper","es":"agarrar","pt":"agarrar","it":"afferrare","de":"packen","ru":"крепко держать","ar":"يمسك بإحكام","zh":"紧握"},
 "huddle":   {"pos":"verb","en":"to crowd close together for warmth","fr":"se blottir","es":"acurrucarse","pt":"aconchegar-se","it":"rannicchiarsi","de":"sich zusammenkauern","ru":"жаться друг к другу","ar":"يتجمّعون متلاصقين","zh":"挤作一团"},
 "length":   {"pos":"noun","en":"a long stretch or section of something","fr":"un tronçon","es":"el tramo","pt":"o trecho","it":"il tratto","de":"der Abschnitt","ru":"отрезок","ar":"مقطع","zh":"一段"},
 "prime":    {"pos":"verb","en":"to fill a pump with water so it will work","fr":"amorcer","es":"cebar","pt":"escorvar","it":"adescare","de":"ansaugen lassen","ru":"заливать насос","ar":"يملأ المضخة للتشغيل","zh":"给水泵灌引水"},
 "sag":      {"pos":"verb","en":"to sink or droop under weight","fr":"s'affaisser","es":"combarse","pt":"ceder","it":"cedere","de":"durchhängen","ru":"проседать","ar":"يترهّل","zh":"下陷"},
 "slick":    {"pos":"adjective","en":"smooth and slippery","fr":"glissant","es":"resbaladizo","pt":"escorregadio","it":"scivoloso","de":"glatt","ru":"скользкий","ar":"زَلِق","zh":"滑溜的"},
 "awash":    {"pos":"adjective","en":"covered or flooded with water","fr":"inondé","es":"anegado","pt":"alagado","it":"allagato","de":"überflutet","ru":"затопленный","ar":"مغمور بالماء","zh":"被水淹没的"},
 "boatyard": {"pos":"noun","en":"a place where boats are built and kept","fr":"le chantier naval","es":"el astillero","pt":"o estaleiro","it":"il cantiere navale","de":"die Bootswerft","ru":"лодочная верфь","ar":"حوض القوارب","zh":"船坞"},
 "chill":    {"pos":"verb","en":"to make cold right through","fr":"glacer","es":"helar","pt":"gelar","it":"gelare","de":"durchkälten","ru":"студить","ar":"يُبرِّد","zh":"使发冷"},
 "flame":    {"pos":"noun","en":"the bright burning part of a fire","fr":"la flamme","es":"la llama","pt":"a chama","it":"la fiamma","de":"die Flamme","ru":"пламя","ar":"اللهب","zh":"火焰"},
 "roll":     {"pos":"verb","en":"to move by turning over, or to push on wheels","fr":"rouler","es":"hacer rodar","pt":"fazer rolar","it":"far rotolare","de":"rollen","ru":"катить","ar":"يدحرج","zh":"滚动"},
 "spadeful": {"pos":"noun","en":"the amount a spade holds","fr":"une pelletée","es":"una palada","pt":"uma pá cheia","it":"una badilata","de":"eine Schaufel voll","ru":"полная лопата","ar":"ملء المجراف","zh":"一锹的量"},
 "curl":     {"pos":"verb","en":"to bend into a small, rounded shape","fr":"se recroqueviller","es":"ovillarse","pt":"encolher-se","it":"raggomitolarsi","de":"sich zusammenrollen","ru":"сворачиваться","ar":"يتكوّر","zh":"蜷缩"},
 "shed":     {"pos":"noun","en":"a small hut for storing tools","fr":"la remise","es":"el cobertizo","pt":"o barracão","it":"il capanno","de":"der Schuppen","ru":"сарай","ar":"السقيفة","zh":"棚屋"},
 "shove":    {"pos":"noun","en":"a hard, sudden push","fr":"la poussée","es":"el empujón","pt":"o empurrão","it":"la spinta","de":"der Stoß","ru":"толчок","ar":"الدفعة","zh":"猛推"},
 "teeth":    {"pos":"noun","en":"the hard white parts in the mouth","fr":"les dents","es":"los dientes","pt":"os dentes","it":"i denti","de":"die Zähne","ru":"зубы","ar":"الأسنان","zh":"牙齿"},
 "truck":    {"pos":"noun","en":"a large road vehicle for carrying loads","fr":"le camion","es":"el camión","pt":"o camião","it":"il camion","de":"der Lastwagen","ru":"грузовик","ar":"الشاحنة","zh":"卡车"},
}

MUST = ["lane","flood","dawn","soaked","torch","stack","weir","breath","plank","inch",
        "leak","relief","steady","feet","frightened","grandchild","kindness","pack","pale",
        "sandbag","crew","frozen","unbuilt","chest","pump","river","bank",
        "rotten","cheque","gnaw","grip","huddle","length","prime","sag","slick",
        "awash","boatyard","chill","flame","roll","spadeful",
        "curl","shed","shove","teeth","truck"]

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
    """The lexicon key a word maps to (base form via suffix stripping), or None."""
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
    d7 = json.load(open(EP07, encoding="utf-8"))
    core = {w.strip().lower() for w in open(os.path.join(ROOT,"scripts","wordlist_core.txt"),encoding="utf-8") if w.strip()}

    # words + frequency. Vocab check runs on A2/B1 (and choices, shown at every level).
    freq = Counter(); checked = Counter()
    for n in d7["nodes"]:
        for lvl in ("A2","B1","B2"):
            for w in re.findall(r"[a-z]+(?:'[a-z]+)?", n["text"][lvl].lower()):
                freq[w]+=1
                if lvl in ("A2","B1"): checked[w]+=1
        for c in n.get("choices",[]):
            for w in re.findall(r"[a-z]+", c["text"]["A2"].lower()):
                freq[w]+=1; checked[w]+=1
    present = set(freq)

    # pool vetted entries from books 1-6
    pool = {}
    for ep in range(1,7):
        d = json.load(open(os.path.join(ROOT,"content","episode-0%d.json"%ep), encoding="utf-8"))
        for k,v in d["lexicon"]["entries"].items():
            pool.setdefault(k,v)
    catalogue = dict(pool); catalogue.update(FLOOD)   # everything we could include
    cat_keys = set(catalogue)

    def ep_freq(base):
        return sum(freq[f] for f in forms(base) if f in freq) + freq.get(base,0)

    # 1) COVERAGE: every hard A2/B1 word must resolve to an included key, if the catalogue can.
    needed = set()
    for w in checked:
        if in_core(w, core):           # a learner handles it via a known base
            continue
        k = resolve(w, cat_keys)       # is there a catalogue entry that covers it?
        if k: needed.add(k)
    entries = {k: catalogue[k] for k in needed}

    # 2) flood entries present in the book (book-specific flavour, always wanted)
    for k,v in FLOOD.items():
        if k not in entries and (forms(k)&present or k in present):
            entries[k]=v

    # 3) fill the rest to TARGET with the most-used pooled words
    hits = [k for k in pool if (forms(k)&present or k in present) and k not in entries]
    hits.sort(key=lambda k: ep_freq(k), reverse=True)
    for k in hits:
        if len(entries) >= TARGET: break
        entries[k]=pool[k]

    # 4) belt-and-braces: MUST words
    for k in MUST:
        if k not in entries and k in catalogue: entries[k]=catalogue[k]

    entries = {k:entries[k] for k in sorted(entries)}
    d7["lexicon"]["entries"] = entries
    json.dump(d7, open(EP07,"w",encoding="utf-8"), indent=2, ensure_ascii=False)
    # report any hard word the catalogue simply can't cover (would need authoring)
    uncov = sorted({w for w in checked if not in_core(w,core) and not resolve(w,set(entries))})
    print("high-water lexicon: %d entries. Uncovered hard words: %s" % (
        len(entries), uncov or "none"))

if __name__ == "__main__":
    main()
