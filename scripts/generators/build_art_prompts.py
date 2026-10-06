#!/usr/bin/env python3
"""Build the per-passage painted-art prompt pack for The Address.

One prompt per passage in a single locked style, tied to its filename so the images
drop straight into the reader's art slot (images/new-city/ep-01/<id>.webp) and replace
the emblems automatically. Emits:
  - docs/art-prompts-passages.md  (style bible + a readable list of all 123 subjects)
  - content/art/episode-01.prompts.csv  (turnkey: id,filename,motif,prompt,alt)

Run: python3 scripts/build_art_prompts.py
"""
import csv, json, os, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
EP = os.path.join(ROOT, "content", "episode-01.json")
IMG_DIR = "images/new-city/ep-01"

# The locked look — identical for every passage; this is what keeps 123 images one book.
STYLE = ("Painterly atmospheric illustration, cinematic nocturne: a cold, unfamiliar city "
         "at night lit by a single warm sodium-amber source against deep navy-and-teal blues; "
         "limited muted palette, soft volumetric fog, gentle film grain and visible painterly "
         "brushwork; faceless viewpoint — show the world from behind or over the shoulder, or "
         "only hands and objects, never a clear face or eye contact; culturally neutral modern "
         "European-ish port city, no readable text or signage, no flags or landmarks; quiet, "
         "uncertain, atmospheric but not frightening.")
PARAMS = "3:2 landscape, subject held in the central 90%, cinematic lighting."
NEGATIVE = ("no text, no lettering, no watermark, no logos, no visible faces or eye contact, "
            "no bright saturated colours, no daytime blue sky, no cartoon style.")

# valence tints for the twelve endings
GOOD = "warm, resolved, a held breath let go"
NEUTRAL = "muted, unresolved, neither win nor loss"
BITTER = "correct but hollow, a warmth withheld"
BAD = "cold, closed, the cost of the night"

# node id -> the single motif (kept in sync with the reader's emblem map, for cross-reference)
MOTIF = {
 1:'station',2:'map',3:'taxi',4:'bus',5:'kiosk',6:'taxi',7:'building',8:'bus',9:'kiosk',10:'bed',
 11:'window',12:'door',13:'bench',14:'lamp',15:'card',16:'bed',17:'building',18:'door',19:'quay',20:'building',
 21:'cup',22:'bench',23:'quay',24:'suit',25:'quay',26:'door',27:'keys',28:'quay',29:'card',30:'desk',
 31:'cup',32:'coin',33:'coin',34:'letter',35:'desk',36:'desk',37:'notebook',38:'desk',39:'coin',40:'board',
 41:'companions',42:'companions',43:'kiosk',44:'kiosk',45:'sign',46:'door',47:'door',48:'bench',49:'lamp',50:'lamp',
 51:'door',52:'window',53:'bus',54:'bridge',55:'quay',56:'card',57:'cup',58:'cup',59:'companions',60:'suit',
 61:'suit',62:'coin',63:'envelopes',65:'taxi',67:'quay',68:'suit',69:'letter',72:'phone',73:'phone',75:'companions',
 77:'station',79:'bus',84:'desk',85:'desk',86:'letter',88:'keys',89:'quay',90:'suit',91:'companions',92:'bridge',
 94:'desk',95:'kiosk',96:'envelopes',97:'window',98:'window',99:'oars',100:'oars',101:'quay',102:'cup',103:'cup',
 104:'bed',105:'bus',106:'fence',107:'suit',108:'taxi',109:'map',110:'quay',111:'bus',112:'door',113:'cup',114:'letter',
 115:'lamp',116:'taxi',117:'notebook',118:'phone',119:'card',120:'desk',121:'coin',122:'taxi',123:'cup',124:'cup',
 125:'companions',126:'bench',127:'notebook',128:'bench',129:'bed',
 141:'desk',142:'desk',143:'notebook',144:'suit',145:'keys',146:'notebook',147:'bench',
}

# node id -> the specific moment to paint (faceless, object/scene led)
SUBJECT = {
 1:"an almost-empty night railway platform under cold light; a lone traveller with a small case and a letter, seen from behind",
 2:"a tired night clerk at a lit information window sliding across a small hand-drawn map; an unread letter on the counter",
 3:"a wet station forecourt at night, three idling taxis and a bus-stop sign, cold river air, breath visible",
 4:"the warm, near-empty interior of a night bus; a letter reread on an empty seat, dark wet streets sliding past the window",
 5:"a woman pulling down the shutter of a corner kiosk on an empty night street — the only person around",
 6:"the view from a taxi's back seat, the driver laughing over his shoulder, an empty night avenue ahead",
 7:"a grey, dusty, abandoned office building behind builders' hoarding at night; a dark doorway and an old dead sign",
 8:"a night bus halted at its last stop, the driver glancing back; an empty depot, one in the morning, no more buses",
 9:"a kiosk woman pointing down a dark corner toward a distant café light, a letter in her other hand",
 10:"a small, clean, cheap hotel lobby at night; a key on the desk, a yellow agency sign glimpsed across the road",
 11:"looking through a dusty office window: an overturned chair, a stopped calendar, one small light behind a glass door at the back",
 12:"a neighbour's half-open door at night, a figure in a dressing gown, warm hall light spilling onto the step",
 13:"a hard station bench at first light, a coat pulled close, a cleaner's trolley approaching",
 14:"empty repeating night streets and a single street lamp; back near the station at three in the morning, nothing learned",
 15:"a business card taped inside a dark café window, a new address just legible; cold hands raising a phone to photograph it",
 16:"a small clean room at first light, its window looking down on a big yellow agency sign across the road",
 17:"the empty abandoned building at eight in the morning, grey and shut, an hour before the interview",
 18:"a cleaner half-opening an inner glass door onto empty offices, waving you away",
 19:"walking toward the river near two in the morning; new all-glass offices dark across the black water",
 20:"a cold grey morning, exhausted, standing before the empty building",
 21:"a warm, expensive café at night — a cup and a letter on the table — weighing whether to go on",
 22:"a station bench at eight in the morning, numb feet, the pull to simply go home",
 23:"a new riverside building's brass company directory; the fourth name legible only as a name-plate, second floor",
 24:"a too-bright new job-agency office, a yellow sign, a man in a good suit sliding a form across the counter",
 25:"the river quay at half past eight, grey water and gulls, arriving early and almost clean",
 26:"a young woman opening a door at night, pointing toward a night bus at the corner",
 27:"a woman arriving at a riverside door with a key and a coffee — she turns out to be the firm",
 28:"identical dark quay buildings at night; the number you found is only a car park, so you sit by the water",
 29:"a café counter at night, a hand writing an address on a paper napkin",
 30:"a warm reception desk smelling of coffee, a name typed twice on a screen, no interview found",
 31:"a woman near sixty approaching a glass door with a takeaway coffee; a small yellow luggage tag on her bag",
 32:"a plain receipt bearing only a number, money just handed across a counter and gone",
 33:"across a desk, a good-suited man's smile vanishing as the form is pushed back, unpaid",
 34:"quarter past nine on an empty street; a now-useless letter in hand, pockets nearly empty",
 35:"an office over the water; a woman reading your letter, a chair drawn up for you",
 36:"warm office light at last — a desk, a tray of letters to correct, a job honestly begun",
 37:"a hand writing your name on a real sheet of paper; a door held open to the street",
 38:"on an office step, a woman turning and half-smiling, recognised before a word is said, warm morning",
 39:"a locked glass door with an empty office behind it and a receipt bearing only a number",
 40:"a departures board at a station, a two-o'clock train back the way you came",
 41:"an emptying platform; a young traveller with a big backpack rereading a scrap of paper, as lost as you",
 42:"two travellers with cases under station light comparing addresses — for a moment, not alone",
 43:"a newsstand man at night reading your letter among stacks of papers",
 44:"a kiosk man gesturing toward the river, explaining the firm moved years ago",
 45:"a torn old company notice on builders' hoarding, a marker word and an arrow pointing east",
 46:"a narrow side door at night with a thin line of warm light beneath it",
 47:"a woman leaving an office, pulling on her coat, gesturing toward the river",
 48:"a station bench at night; a man with only a paper cup, no bag and no coat, quietly beside you",
 49:"the same closed shop passing twice, a useless map, the city belonging to no one at one in the morning",
 50:"a lone all-night launderette spilling yellow light; an attendant folding towels, sketching a route",
 51:"a glass door at the back, a name half-scraped away, still reading as a surname",
 52:"a lit upstairs window; a child of about ten watching the street, quite calm",
 53:"a night bus surging past, warm yellow windows, only seconds to decide",
 54:"a bridge over black water; dark glass offices on the far bank and one window lit high up, a crescent moon",
 55:"a night watchman leaning from a lit booth at the new offices, waving you in to warm up",
 56:"a closed café at night, a light at the back, someone stacking chairs, a card on the glass",
 57:"a café door opened on its chain; a voice telling you the woman comes each morning for coffee",
 58:"a station cleaner pouring half a cup from a thermos at dawn",
 59:"a modest breakfast table; a fellow traveller warning against the agency across the road",
 60:"a queue before a yellow WORK-FOR-ALL sign at dawn, tired faces, breath in the cold",
 61:"a good-suited man sliding a registration form across a counter, hand out for the money",
 62:"a man leaning on a wall outside, a receipt like yours in hand, never called back",
 63:"a reception tray of returned letters, old crossed-out addresses, one of them yours",
 65:"from a taxi at night, the driver warning about the agencies near the station",
 67:"grey dawn on the river quay: a coffee cart opening, delivery vans, gulls on grey water",
 68:"watching the quay doors; the agency's good-suited man entering a nameless building two doors down",
 69:"an open bag under a lamp — a letter, a little money, a photograph left unturned",
 72:"a phone showing a single bar of battery, night, an unfamiliar city — a kind of countdown",
 73:"an old web page loading a riverside address, then a black dead screen, a paper letter left in hand",
 75:"two travellers deciding to go on together rather than walk the wrong way alone at night",
 77:"a guard switching off station lights bench by bench, the great hall darkening, cold coming in",
 79:"the city sliding dark and wet past a bus window, weighing whether to get off early",
 84:"a kind receptionist reading the night on you — creased coat, tired eyes — but saying nothing",
 85:"an office over the water; your own letter, returned to sender, lying on the desk",
 86:"an explanation across a desk: someone has sent the old address for two years; you came anyway",
 88:"a woman on the office step, coffee and keys in hand, waving you in out of the cold",
 89:"the quay waking — gulls, a coffee cart, vans — time to spare and clean hands after a hard night",
 90:"the agency's good-suited man meeting your eyes, then vanishing into a nameless building",
 91:"another candidate confiding, close by, that they nearly paid the agency too",
 92:"through a window, the bridge you crossed in the dark, now grey and ordinary by day",
 94:"a manager and a blushing young colleague over old letterhead, resolving to fix it",
 95:"a kiosk woman pointing to a passage behind a building, through a courtyard",
 96:"a courtyard tray of envelopes ready to post — all addressed to the wrong old street",
 97:"a child leaning from an upper window, telling you the firm is at the river now",
 98:"a child's directions given from a window — a bus number, an address — then the window closing",
 99:"a lit boathouse by the water at night, long oars carried toward the river, low voices",
 100:"a rower with an oar on the shoulder pointing straight on, past the second bridge",
 101:"a lit, empty glass hall; a guard's cap on an abandoned desk, everything newer than your letter",
 102:"the sky going from black to dishwater grey, feet gone numb, a café light finally coming on",
 103:"a café regular looking up from his tea, recalling the firm — good people, bad with the post",
 104:"a hotel owner warning against the yellow-sign agency across the road",
 105:"the first warm, near-empty bus of the day, a choice of two directions",
 106:"a fenced, weedy empty lot behind the agency — no job that was ever real",
 107:"a woman in the queue folding the form back, calling it a scam, leading others out",
 108:"a taxi through deserted streets, a night café's yellow light on wet tarmac, a fox",
 109:"a man at a window drawing a better map on the back of a receipt, marking the river",
 110:"walking toward the quay in rising light among people who know where they are going",
 111:"a young woman going the same way, offering to show where to get off the bus",
 112:"climbing an office stair, late and breathless, rehearsing an apology",
 113:"a coffee-cart woman adding a free extra shot — a warm cup held in both hands, long night",
 114:"a cold cup left untouched, the letter put away, standing to go on",
 115:"a deserted market square, stalls folded, wet cobbles under a lamp, a fox in the gutter",
 116:"a taxi idling at the curb, engine running, the driver reading a paper",
 117:"a cleaner propping a door with a foot, taking a note for the desk, no promise",
 118:"photographing a half-scraped name on glass, twice, as proof you came",
 119:"stamping in the cold outside a café, staring at the card taped to the glass",
 120:"a question across a desk: why hire a stranger arrived almost by chance",
 121:"recounting the agency that nearly took the last of your money; you were right to walk away",
 122:"a night worker sharing a taxi — ten minutes where someone else knows the way",
 123:"a warm watchman's booth, something poured from a thermos into a tin cup, before nine",
 124:"a café queue where a name is overheard — two second-floor staff, so close now",
 125:"a breakfast decision to walk to the river together",
 126:"a station cleaner of twenty years urging you on, kindly and firmly",
 127:"leaving a name and number with a counter man, noted on the back of a voucher",
 128:"dawn on a bench, back wrecked, not ready to give up; a bus coming your way",
 129:"a hotel man softening, letting you stay by a lobby radiator until day",
 141:("a plain handshake in a plain office, morning light — everything earned", GOOD),
 142:("walking in rested and owing nothing, the river bright through the office window", GOOD),
 143:("a hand closing a notebook with your name in it, the city going on outside", NEUTRAL),
 144:("new carpet, a lanyard, a screen — everything correct and nothing felt", BITTER),
 145:("a borrowed kettle and a spare key on a stranger's table — not hired, not alone", NEUTRAL),
 146:("a closed appointment diary and full chairs in a reception, a kind final shake of the head", BAD),
 147:("grey morning over an empty bench, nine o'clock come and gone, too cold to move", BAD),
}

book = json.load(open(EP, encoding="utf-8"))
node_ids = [n["id"] for n in book["nodes"]]
missing = [i for i in node_ids if i not in SUBJECT]
assert not missing, f"no prompt subject for nodes {missing}"

def alt_of(subject):
    return subject[0].upper() + subject[1:] + "."

rows = []
for nid in node_ids:
    s = SUBJECT[nid]
    valence = None
    if isinstance(s, tuple):
        s, valence = s
    mood = f" Mood: {valence}." if valence else ""
    prompt = f"{STYLE} Scene: {s}.{mood} {PARAMS} Negative prompt: {NEGATIVE}"
    rows.append({
        "id": nid,
        "filename": f"{IMG_DIR}/{nid}.webp",
        "motif": MOTIF.get(nid, ""),
        "prompt": prompt,
        "alt": alt_of(s),
    })

os.makedirs(os.path.join(ROOT, "content", "art"), exist_ok=True)
csv_path = os.path.join(ROOT, "content", "art", "episode-01.prompts.csv")
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["id", "filename", "motif", "prompt", "alt"])
    w.writeheader()
    w.writerows(rows)

md = [
 "# The Address — painted-art prompt pack (per passage)",
 "",
 "One prompt for every one of the 123 passages, in a single locked style. Generate each with",
 "any image model, export **WebP 1200×800, ≤120 KB**, and drop it at the filename shown — the",
 "reader loads it automatically and it replaces the emblem for that passage. No code changes.",
 "",
 "## The one rule: consistency",
 "All 123 must feel like one hand. Lock the style below, generate the first five, agree the look,",
 "then hold it. Reuse a **style reference image** (or a fixed seed / `--sref`) across the whole set,",
 "and keep a **character reference** for the recurring people (Ms Rowe ~60 with a takeaway coffee;",
 "the good-suited agency man; the kiosk woman; the fellow traveller Mara; the girl at the window) —",
 "always faceless or from behind.",
 "",
 "## Locked style (prepend to every prompt — already baked into the CSV)",
 "",
 "> " + STYLE,
 "",
 "**Framing:** " + PARAMS,
 "",
 "**Negative:** " + NEGATIVE,
 "",
 "## Delivery",
 "- WebP, quality ~80, ≤120 KB (hard ceiling 200 KB — phone-first, mobile data).",
 "- 3:2, 1200×800; keep the subject in the central 90% (cards crop on tall phones).",
 "- File path: `" + IMG_DIR + "/<passage-id>.webp` (e.g. `1.webp`).",
 "- Full ready-to-run prompts (style + scene + negative) are in "
 "`content/art/episode-01.prompts.csv`.",
 "",
 "## The 123 passages",
 "",
]
for r in rows:
    md.append(f"- **§{r['id']}** · _{r['motif']}_ · `{r['id']}.webp` — {r['alt']}")
md_path = os.path.join(ROOT, "docs", "art-prompts-passages.md")
open(md_path, "w", encoding="utf-8").write("\n".join(md) + "\n")

print(f"Wrote {len(rows)} prompts:")
print(f"  {os.path.relpath(csv_path, ROOT)}")
print(f"  {os.path.relpath(md_path, ROOT)}")
