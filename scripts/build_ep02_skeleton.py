#!/usr/bin/env python3
"""Phase 2: graph skeleton for book 2, 'The Night Market' (standalone).

The machine before the prose: every node is id + choices + gotos + flags + ending markers,
with one-line stub text per level (identical across A2/B1/B2 for now — prose phase replaces
it). Emits content/episode-02.json. Run the validator on the output; it must return 0 errors
before any real prose is written.

Run: python3 scripts/build_ep02_skeleton.py
"""
import json, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "content", "episode-02.json")

# standalone: nothing carried in or out to any other book
STATE_IN = []
OWN = ["kept_quality", "sold_well", "dodged_fixer", "paid_fixer",
       "saved_a_bowl", "helped_neighbour", "gave_freely", "rushed"]
STATE_OUT = OWN[:]
ARC_FLAGS = []

N = []
def node(i, stub, choices): N.append({"id": i, "stub": stub, "choices": choices})
def end(i, stub, val): N.append({"id": i, "stub": stub, "ending": val})
def c(t, g, sets=None, req=None):
    d = {"t": t, "goto": g}
    if sets: d["sets"] = sets if isinstance(sets, list) else [sets]
    if req: d["requires"] = req if isinstance(req, list) else [req]
    return d

# ===== ACT I — LIGHTING UP =====
node(1, "Dusk. Auntie has scalded her hand; tonight you run pitch 24 alone, and the season's fee is due to the market master by dawn or the corner is lost.", [
    c("Light the stall and get started.", 2),
    c("Call Auntie for instructions first.", 3),
    c("Check the money box and the fee.", 4)])
node(2, "You open the stall — burners, lanterns, the counter, the back shelf.", [
    c("The tea woman next door leans over.", 5),
    c("The supplier's van pulls up.", 6),
    c("The big burner won't catch.", 19)])
node(3, "Auntie on the phone: the broth, the good supplier, and — set a bowl for Mr Behn.", [
    c("Ask about the good supplier.", 6),
    c("Ask what else you must know.", 7),
    c("Taste her broth to learn the balance.", 20)])
node(4, "The money box, and the fee card in Auntie's hand.", [
    c("You must match it by dawn. Get cooking.", 2),
    c("Work out what a bowl earns.", 8),
    c("Auntie frets down the line.", 21)])
node(5, "The tea woman at pitch 25 says hello.", [
    c("Chat a moment.", 9),
    c("Get to the supplier.", 6)])
node(6, "The supplier's van: the good pork and greens cost more; the cheap end-of-day stock is half the price and half turned.", [
    c("Buy the good stock.", 10, sets="kept_quality"),
    c("Buy the cheap stock to save money.", 11),
    c("Buy a little of each.", 12)])
node(7, "Auntie goes quiet at the name Behn.", [
    c("Ask who he is.", 13),
    c("Say you will, and hang up.", 6)])
node(8, "A bowl earns little; the fee needs a whole good night.", [
    c("Get cooking.", 2),
    c("Ask the tea woman for tips.", 9)])
node(9, "The tea woman's tips — and a warning about Mr Sould, the fixer.", [
    c("Thank her.", 14),
    c("Sould is already coming over.", 15)])
node(10, "The good stock, stored and cold.", [
    c("Back to the stall.", 16),
    c("Set up the counter.", 18)])
node(11, "The cheap stock, and a smell you don't like.", [
    c("Use it anyway.", 16),
    c("Regret it.", 17)])
node(12, "Some of each, to hedge.", [
    c("Back to the stall.", 16),
    c("Set up the counter.", 18)])
node(13, "The saved bowl — Auntie's thirty-year habit.", [
    c("Set a bowl aside now, as she does.", 18, sets="saved_a_bowl"),
    c("You're too busy for that.", 16)])
node(14, "You thank the tea woman.", [
    c("Back to the stall.", 16),
    c("Open for business.", 31)])
node(15, "Sould's first, friendly approach.", [
    c("Hear him out.", 61),
    c("Wave him off politely.", 16)])
node(16, "The stall is ready; the market fills up.", [
    c("Open for business.", 31),
    c("Set a bowl aside first.", 13),
    c("The regulars will want the usual.", 22)])
node(17, "You bin the worst of the cheap stock.", [
    c("Back to the stall.", 16),
    c("Open for business.", 31)])
node(18, "The saved bowl waits on the back shelf.", [
    c("Open for business.", 31),
    c("Back to the stall.", 16)])
node(19, "The burner splutters and won't light.", [
    c("Coax it alight yourself.", 5),
    c("The tea woman helps.", 9)])
node(20, "You taste the broth — salt, ginger, the deep note.", [
    c("To the supplier.", 6),
    c("Back to the stall.", 16)])
node(21, "Auntie frets about the fee down the line.", [
    c("Reassure her, and cook.", 2),
    c("Work out the numbers.", 8)])
node(22, "The regulars will expect Auntie's usual.", [
    c("Open for business.", 31),
    c("Ask the tea woman who's who.", 9)])

# ===== ACT I — FIRST CUSTOMERS & PRICING =====
node(31, "The first customers; how do you price the bowls?", [
    c("A fair price.", 32),
    c("Charge high for the tourists.", 33),
    c("Auntie's usual price.", 34),
    c("A nervous first big order.", 23)])
node(32, "A fair price it is.", [
    c("Serve them.", 35),
    c("A grumble anyway.", 36)])
node(33, "You mark the price up.", [
    c("A grumble at the price.", 36),
    c("Serve them.", 35)])
node(34, "Auntie's usual price, to the penny.", [
    c("Serve them.", 35),
    c("A regular smiles.", 37)])
node(35, "Serving the first bowls.", [
    c("A customer praises it.", 37),
    c("A customer finds it bland.", 38),
    c("A child counts out coins.", 24)])
node(36, "Someone grumbles about the price.", [
    c("Drop it back to fair.", 32),
    c("Hold firm.", 39)])
node(37, "A customer loves the broth.", [
    c("The takings grow.", 39),
    c("The crowd builds.", 41)])
node(38, "A customer says it's bland.", [
    c("The takings grow.", 39),
    c("The crowd builds.", 41)])
node(39, "The first takings in the box.", [
    c("Count so far.", 40),
    c("The crowd builds.", 41)])
node(40, "A start — a long way to the fee.", [
    c("Into the rush.", 41),
    c("A word with the tea woman.", 9)])
node(41, "The crowd builds; the rush begins.", [
    c("Meet the rush.", 42),
    c("The arcade packs in.", 43),
    c("Orders shouted from all sides.", 26)])
node(23, "A family of six, all ordering at once.", [
    c("Take it carefully.", 35),
    c("Rush it through.", 45)])
node(24, "A child counts coins for one bowl.", [
    c("Serve them kindly.", 37),
    c("Shoo them on.", 38)])

# ===== ACT II — THE LONG RUSH =====
node(42, "The rush: orders pile up faster than your hands.", [
    c("Work steadily, keep it right.", 44),
    c("Rush it — cut a corner to go faster.", 45, sets="rushed"),
    c("Call for a hand.", 46)])
node(43, "The arcade is shoulder to shoulder.", [
    c("Meet the rush.", 42),
    c("Work steadily.", 44)])
node(44, "You find a rhythm at the burners.", [
    c("Work steadily and win the crowd over.", 47, sets="sold_well"),
    c("Just keep up.", 49)])
node(45, "You serve one half-done, and short a coin.", [
    c("Keep going.", 47),
    c("A customer notices.", 48),
    c("You burn your hand in the hurry.", 28)])
node(46, "You call out for help.", [
    c("Send the market kid on an errand.", 73),
    c("The tea woman is swamped too.", 58)])
node(47, "Mid-rush, the box filling.", [
    c("Keep serving.", 49),
    c("A brief lull.", 50),
    c("A regular asks for Auntie.", 27)])
node(48, "A customer clocks the short change.", [
    c("Apologise and fix it.", 51),
    c("Brazen it out.", 54)])
node(49, "The stock is running low.", [
    c("Eke it out in small bowls.", 56),
    c("Send for more.", 55),
    c("The steamer runs dry.", 29)])
node(50, "A brief lull; wipe down.", [
    c("Back to serving.", 49),
    c("Take a breath.", 52),
    c("A quiet stretch.", 30)])
node(51, "You make the short change right.", [
    c("Back to serving.", 49),
    c("On through the rush.", 57)])
node(52, "You breathe; the box is filling.", [
    c("Count so far.", 40),
    c("Back in.", 57)])
node(54, "The customer leaves angry, and talks.", [
    c("Back to serving.", 49),
    c("On through the rush.", 57)])
node(55, "You send the kid for more stock.", [
    c("The kid returns, hungry.", 73),
    c("On through the rush.", 57)])
node(56, "You eke out smaller bowls.", [
    c("On through the rush.", 57),
    c("A quiet moment.", 59)])
node(57, "The rush rolls on.", [
    c("The tea woman's urn spills.", 58),
    c("A quiet moment.", 59)])
node(58, "The tea woman's urn goes over — she's in trouble.", [
    c("Drop everything and help her.", 88, sets="helped_neighbour"),
    c("You can't; keep serving.", 60)])
node(59, "A quiet moment; the back shelf, the empty stool.", [
    c("Check the saved bowl.", 91),
    c("Back to work.", 60),
    c("The stool has been empty all night.", 96)])
node(60, "The rush peaks and breaks.", [
    c("The stock is nearly gone.", 80),
    c("Rain sweeps the arcade.", 79),
    c("A new stall opposite undercuts you.", 86)])
node(26, "Orders shouted from every side at once.", [
    c("Meet the rush.", 42),
    c("Work steadily.", 44)])
node(27, "A regular asks where Auntie is.", [
    c("Tell them the truth.", 49),
    c("Just serve, and smile.", 50)])
node(28, "You burn your hand, as Auntie did.", [
    c("Wrap it and carry on.", 47),
    c("The tea woman helps.", 58)])
node(29, "The steamer runs dry; refill it.", [
    c("Eke it out.", 56),
    c("On through the rush.", 57)])
node(30, "A quiet stretch to wipe down and think.", [
    c("Take a breath.", 52),
    c("On through the rush.", 57)])

# ===== FIXER (Mr Sould) =====
node(61, "Sould's pitch: he collects fees, settles trouble, lends to the stuck.", [
    c("Listen to the offer.", 62),
    c("Refuse now.", 63, sets="dodged_fixer"),
    c("Stallholders line up to pay him.", 66)])
node(62, "The offer: a loan to be safe, or a quiet word with a rival — a price never quite named.", [
    c("Take the loan.", 64, sets="paid_fixer"),
    c("Refuse it.", 63, sets="dodged_fixer"),
    c("Ask what it costs.", 65)])
node(63, "You send him off.", [
    c("Back to the stall.", 16),
    c("Into the night's work.", 60)])
node(64, "You take his money — relief, then unease.", [
    c("Back to the stall.", 16),
    c("On toward closing.", 101)])
node(65, "He smiles and still won't name the price.", [
    c("That's the tell — refuse.", 63, sets="dodged_fixer"),
    c("Take it anyway.", 64, sets="paid_fixer")])
node(66, "Stallholders queue to hand Sould their fees.", [
    c("Hear his offer.", 62),
    c("A stallholder warns you.", 67)])
node(67, "'Sould never forgets a debt,' the stallholder murmurs.", [
    c("Refuse him.", 63, sets="dodged_fixer"),
    c("Still hear him out.", 62)])
node(68, "Sould's patient smile as closing nears.", [
    c("Take his loan.", 64, sets="paid_fixer"),
    c("Refuse, and take your chances.", 110, sets="dodged_fixer")])

# ===== THE KID =====
node(73, "The kid runs your errand, then eyes the bowls, hungry.", [
    c("Give the kid a bowl.", 74, sets="gave_freely"),
    c("Pay only in coins.", 75)])
node(74, "The kid eats, wide-eyed and grateful.", [
    c("Back to the rush.", 57),
    c("The kid sticks around.", 76),
    c("The kid tells you their name.", 77)])
node(75, "The kid pockets the coins, still hungry.", [
    c("Back to the rush.", 57),
    c("The kid sticks around.", 76)])
node(76, "The kid hangs about, quietly useful.", [
    c("Back to the rush.", 57),
    c("On into the night.", 60),
    c("The kid guards the stall.", 78)])
node(77, "The kid tells you their name, and where they sleep.", [
    c("Back to the rush.", 57),
    c("The kid sticks around.", 76)])
node(78, "The kid watches the stall while you cook.", [
    c("Back to the rush.", 57),
    c("On into the night.", 60)])

# ===== NEIGHBOUR (result) =====
node(88, "You mop, relight, and set the tea woman right.", [
    c("Back to your stall.", 59),
    c("On into the night.", 60)])

# ===== RAIN / STOCK / RIVAL =====
node(79, "Rain sweeps the arcade; the crowd thins.", [
    c("Pull the awning and wait it out.", 81),
    c("Call people in with cheap late bowls.", 82)])
node(80, "The stock is nearly gone.", [
    c("The pot's nearly dry.", 83),
    c("Stretch the last broth.", 84)])
node(81, "You wait out the rain.", [
    c("The market quietens.", 85),
    c("Toward closing.", 101)])
node(82, "Cheap late bowls pull a small crowd.", [
    c("The market quietens.", 85),
    c("Toward closing.", 101)])
node(83, "The pot is nearly dry.", [
    c("Make it stretch.", 84),
    c("The market quietens.", 85)])
node(84, "You stretch the last of the broth.", [
    c("The market quietens.", 85),
    c("Toward closing.", 101)])
node(85, "The market quietens toward closing.", [
    c("Watch the empty stool.", 91),
    c("Toward closing.", 101),
    c("Dawn grey on the roofs.", 105)])
node(86, "A new stall opposite undercuts your price.", [
    c("Match their price.", 87),
    c("Hold your price.", 89)])
node(87, "A price war eats your profit.", [
    c("Hold from here.", 89),
    c("They burn out by dawn.", 90)])
node(89, "You hold your price; the regulars stay.", [
    c("The market quietens.", 85),
    c("Toward closing.", 101)])
node(90, "The rival burns out before dawn.", [
    c("The market quietens.", 85),
    c("Toward closing.", 101)])

# ===== THE SAVED BOWL / MR BEHN =====
node(91, "Near closing: the empty stool, the saved bowl on the shelf.", [
    c("Watch the stool.", 93),
    c("Sould comes for the fee.", 92),
    c("You remember Auntie saying his name.", 97)])
node(92, "Sould's last offer, if you're short.", [
    c("Take his loan.", 64, sets="paid_fixer"),
    c("Refuse, and take your chances.", 110, sets="dodged_fixer"),
    c("His smile at closing.", 68)])
node(93, "An old man approaches the empty stool.", [
    c("Offer him the saved bowl.", 94, req="saved_a_bowl"),
    c("Offer a fresh bowl.", 95),
    c("You have nothing left.", 110),
    c("An old photo by the till.", 98)])
node(94, "You set the saved bowl before him. His face changes.", [
    c("Serve it, and he stays.", 121, req="saved_a_bowl"),
    c("Just talk to him.", 95)])
node(95, "You serve Behn, and he tells you a little.", [
    c("Toward closing.", 110),
    c("What his return means.", 100)])
node(96, "The stool has stood empty the whole night.", [
    c("Watch it a while.", 91),
    c("Back to work.", 60)])
node(97, "You remember Auntie's face at his name.", [
    c("Watch the stool.", 93),
    c("Serve whoever comes.", 95)])
node(98, "An old photo tucked by the till: Auntie, younger, and a man.", [
    c("Offer the saved bowl.", 94),
    c("Offer a fresh bowl.", 95)])
node(100, "What Mr Behn's return means to the stall.", [
    c("Toward closing.", 110),
    c("Talk with him a while.", 95)])

# ===== CLOSING & THE COUNT =====
node(101, "Closing time nears; you count the takings against the fee.", [
    c("Face the master's round.", 110),
    c("Watch the stool once more.", 93),
    c("The master works stall by stall.", 102)])
node(102, "The market master's slow round, stall by stall.", [
    c("Your turn comes.", 110),
    c("Others who fell short pack up.", 103)])
node(103, "Stalls that missed the fee are packing up.", [
    c("Your turn.", 110),
    c("The lanterns come down.", 104)])
node(104, "The lanterns are lowered one by one.", [
    c("Face the master.", 110),
    c("The last of the night.", 114)])
node(105, "Dawn grey spreads over the market roofs.", [
    c("Watch the stool.", 91),
    c("Toward closing.", 101)])
node(110, "The master stops at pitch 24. The fee is due.", [
    c("Pay from a proud, honest night.", 120, req=["sold_well", "kept_quality"]),
    c("Pay it cleanly, no fixer, no debt.", 122, req=["sold_well", "dodged_fixer"]),
    c("You're not sure you've made it.", 111)])
node(111, "You lay out what the night brought.", [
    c("You fell short, but you made the name.", 123, req="kept_quality"),
    c("You made it — but by cutting corners.", 124, req="rushed"),
    c("Weigh the rest.", 112)])
node(112, "The fee still isn't quite there.", [
    c("Sould has already covered it — for a price.", 128, req="paid_fixer"),
    c("The tea woman offers to cover you.", 125, req="helped_neighbour"),
    c("Weigh the last of it.", 113)])
node(113, "Down to the last of your choices.", [
    c("The kid's family fill your last bowls.", 126, req="gave_freely"),
    c("The master gives you till next week.", 127),
    c("The worst of it.", 114)])
node(114, "Nothing left to set against the fee.", [
    c("You're short; the pitch is lost.", 129),
    c("The pot ran dry hours ago.", 130),
    c("You think about handing it back.", 131)])

# ===== ENDINGS (12: 4 good / 4 neutral / 4 bad) =====
end(120, "GOOD — Sold out, and proud. Honest good food to the last bowl; the fee paid, pitch 24 kept, the name intact.", "good")
end(121, "GOOD — The last bowl (secret). Mr Behn returns at dawn; the saved bowl is served, and you learn who he is to Auntie. Something long cold is warmed.", "good")
end(122, "GOOD — On your own terms. You make the fee cleanly — no fixer, no debt, no corners cut. The corner is yours, earned.", "good")
end(123, "GOOD — A name, not just a night. You fell short of the full fee, but you made the stall's name tonight, and you're given grace to keep the corner.", "good")
end(124, "NEUTRAL — The money, not the name. You hit the fee by cutting corners. You keep the pitch, but the regulars saw, and thirty years of trust is thinner tonight.", "neutral")
end(125, "NEUTRAL — Covered, this once. You fall short, but the tea woman covers your fee, no strings, because you stood by her. Warmth without the win.", "neutral")
end(126, "NEUTRAL — The kindness fed back. No fee tonight, but the child you fed brings a hungry crew who'll come back. A start, not a save.", "neutral")
end(127, "NEUTRAL — One more week. You scrape close; the master gives you till the next market day. Not a loss — just not yet.", "neutral")
end(128, "BAD — In Sould's book. The fee's covered tonight, but you owe the fixer now, and that is the worse debt. You kept the pitch and lost the ground under it.", "bad")
end(129, "BAD — Short by dawn. The takings don't reach the fee. Pitch 24, held thirty years, is lost.", "bad")
end(130, "BAD — The pot ran dry. You ran out hours before dawn and stood at a cold empty stall while the market went on around you.", "bad")
end(131, "BAD — You couldn't hold it. The night beat you, and you think about handing the stall back for good.", "bad")

# ===== assemble =====
def leveled(s): return {"A2": s, "B1": s, "B2": s}
nodes = []
for n in N:
    out = {"id": n["id"], "text": leveled("[stub] " + n["stub"])}
    if "ending" in n:
        out["ending"] = n["ending"]
    else:
        out["choices"] = []
        for ch in n["choices"]:
            co = {"text": leveled(ch["t"]), "goto": ch["goto"]}
            if "sets" in ch: co["sets"] = ch["sets"]
            if "requires" in ch: co["requires"] = ch["requires"]
            out["choices"].append(co)
    nodes.append(out)
nodes.sort(key=lambda x: x["id"])

book = {
    "schema": "adventure-book/episode@1",
    "series": "night-market",
    "episode": 2,
    "title": "The Night Market",
    "slug": "the-night-market",
    "blurb": "Your aunt has hurt her hand, so for one night the family's dumpling stall is yours — and you must take enough by dawn to keep the pitch she has held for thirty years.",
    "identity": {
        "name": "Lantern Night",
        "mood": "A loud warm market in the dark; one stall's lantern is the light you keep.",
        "palette": {
            "ground": "#1A0F0A", "surface": "#271711", "ink": "#F6ECDD",
            "muted": "#A28C77", "line": "#3C2618",
            "accent": "#E85A34", "accentHot": "#F5934F", "secondary": "#74BE95"
        },
        "cover": {"kind": "lantern", "glow": True},
        "type": {"display": "Fraunces", "ui": "Hanken Grotesk", "mono": "JetBrains Mono"},
        "hero": {
            "line": {
                "en": "One night, one stall, and a fee due by dawn.",
                "fr": "Une nuit, un étal, et une redevance à payer avant l'aube.",
                "es": "Una noche, un puesto y una cuota que pagar al amanecer.",
                "it": "Una notte, una bancarella e una quota da pagare all'alba.",
                "de": "Eine Nacht, ein Stand und eine Gebühr, fällig bis zum Morgengrauen.",
                "pt": "Uma noite, uma banca e uma taxa a pagar até ao amanhecer.",
                "ru": "Одна ночь, один прилавок и плата, которую нужно внести к рассвету.",
                "zh": "一个夜晚，一个摊位，天亮前要交的摊位费。",
                "ar": "ليلة واحدة، وكشك واحد، ورسوم مستحقة قبل الفجر."
            },
            "sub": "A story where you are the hero — and every choice turns you to a new page. Written for people learning English, at your level, with meaning in your language whenever you need it."
        }
    },
    "levels": ["A2", "B1", "B2"],
    "start": 1,
    "language_focus": {
        "A2": ["present continuous and imperatives", "food, cooking and prices"],
        "B1": ["quantifiers and comparatives", "buying, selling and making change"],
        "B2": ["inference and negotiation", "obligation, debt and keeping a name"]
    },
    "state_in": STATE_IN,
    "state_out": STATE_OUT,
    "arc_flags": ARC_FLAGS,
    "nodes": nodes,
    "lexicon": {
        "_comment": "The Night Market's chosen lexicon. Grown in phase 4. Base-keyed; the reader resolves inflections. Translations need a native speaker's check before launch.",
        "entries": {}
    }
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(book, open(OUT, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(f"Wrote {OUT}: {len(nodes)} nodes, {sum(1 for n in nodes if n.get('ending'))} endings.")
