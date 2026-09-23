#!/usr/bin/env python3
"""Phase 2: graph skeleton for book 3, 'First Light' (standalone).

Every node is id + choices + gotos + flags + ending markers, with one-line stub text per level
(identical across A2/B1/B2 for now). Emits content/episode-03.json. Run the validator on the
output; it must return 0 errors before any real prose is written.

Run: python3 scripts/build_ep03_skeleton.py
"""
import json, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "content", "episode-03.json")

STATE_IN = []
OWN = ["has_heater", "dodged_seller", "paid_seller", "found_light",
       "rallied_town", "helped_neighbour", "gave_warmth", "took_shortcut"]
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

# ===== ACT I — THE LIGHTS GO OUT =====
node(1, "Just after dark, every light in the town goes out at once. A power cut. The heating dies. Up the hill, old Mrs Ada, who was kind to you as a child, needs her electric heater — and she has a weak chest.", [
    c("Light a candle and find your coat.", 2),
    c("Try the phone for news.", 3),
    c("Rush straight out to Ada.", 4)])
node(2, "You find a candle, a torch, your coat and boots. The house is already going cold.", [
    c("Step out into the street.", 5),
    c("Decide how to start.", 6),
    c("The torch batteries are dead.", 29)])
node(3, "The phone is patchy. Word gets through: the roads are blocked, help comes at first light, stay in and keep warm.", [
    c("Decide how to start.", 6),
    c("But Ada can't wait that long.", 8)])
node(4, "You rush out with nothing. The cold hits like a wall. You will need supplies to do any good.", [
    c("Go back for supplies.", 2),
    c("Feel how serious this is.", 8)])
node(5, "The dark street: black houses, one candlelit window, snow, deep cold.", [
    c("The corner shop is still open.", 9),
    c("Knock on a neighbour's door.", 10),
    c("Decide how to start.", 6),
    c("A kid is out in the dark, searching.", 60)])
node(6, "Gather supplies first, or rush straight to Ada?", [
    c("The shop, for supplies.", 9),
    c("Rush up the hill.", 11),
    c("Knock on doors to gather help.", 12)])
node(8, "The cold, and Ada with her weak chest in a house with no heat. This is real, and it is on you.", [
    c("Decide how to start.", 6),
    c("To the shop.", 9),
    c("A rumour of panic at the shop.", 68)])
node(9, "Mr Okafor's shop, open by candlelight: a paraffin heater, blankets, a hot flask, batteries.", [
    c("Take the paraffin heater.", 13, sets="has_heater"),
    c("Just candles and batteries.", 14),
    c("Ask Okafor's advice.", 15),
    c("He gives you the last flask.", 67)])
node(10, "A neighbour's door: Mrs Pratt, scared and alone in the dark.", [
    c("Stop and help her.", 16, sets="helped_neighbour"),
    c("Say you must reach Ada.", 17)])
node(11, "You rush up the hill with what you have. Cold, hard going.", [
    c("The way splits: road or river.", 21),
    c("You're cold and short of breath.", 18)])
node(12, "You knock on doors to gather willing hands.", [
    c("Neighbours turn out to help.", 19, sets="rallied_town"),
    c("No one answers; go alone.", 20)])
node(13, "The paraffin heater — heavy, but real warmth for Ada.", [
    c("Now the way to her.", 21),
    c("Thank Okafor.", 15)])
node(14, "Candles and batteries: light, but no heat.", [
    c("Now the way to her.", 21),
    c("Ask Okafor's advice.", 15)])
node(15, "Okafor's advice: steer clear of the van man, don't trust the river ice, take the road.", [
    c("Take it to heart.", 22),
    c("On with it.", 21)])
node(16, "You settle Mrs Pratt with a candle and a blanket, and a promise to come back.", [
    c("On toward Ada.", 23),
    c("She asks you to check on others.", 12)])
node(17, "You press on toward Ada.", [
    c("The shop first.", 9),
    c("Straight up the hill.", 11)])
node(18, "Near the hill, cold and unprepared.", [
    c("The van man's lights are ahead.", 24),
    c("Push on.", 21)])
node(19, "The street wakes to itself; a plan forms; someone has a camping stove.", [
    c("Lead the way to Ada.", 25),
    c("Share one warm room first.", 36)])
node(20, "No one answers. You go on alone.", [
    c("The shop.", 9),
    c("Up the hill.", 11)])
node(21, "Supplies decided. Now the way to Ada: the long road, or the frozen river shortcut.", [
    c("Take the road.", 26),
    c("Cross the river ice.", 27),
    c("The van man's lights ahead.", 24)])
node(22, "You resolve to be careful tonight.", [
    c("On the way.", 21),
    c("Back to the shop.", 9)])
node(23, "Warmer inside for the good turn, you go on.", [
    c("On with the night.", 21),
    c("Gather more help.", 12)])
node(24, "The van man's van, headlights blazing, a frightened crowd around it.", [
    c("Hear what he's selling.", 40),
    c("Go round him.", 26)])
node(25, "You lead a small band up toward the hill.", [
    c("The way.", 26),
    c("The strange light on the hill.", 70)])
node(29, "The torch batteries are dead; only the candle.", [
    c("Out into the street.", 5),
    c("To the shop for more.", 9)])
node(36, "The street shares one warm room: a stove, soup, candlelight.", [
    c("Get Ada down to it.", 25),
    c("Fetch more neighbours.", 37)])
node(37, "Door by door, the dark street becomes a lit one.", [
    c("To the hill.", 26),
    c("The last stretch.", 90)])
node(60, "A kid, Bex, out in the dark, looking for a little brother.", [
    c("Help Bex look.", 61, sets="helped_neighbour"),
    c("No time — Ada first.", 62)])
node(61, "You find the small brother in a cold shed, frightened.", [
    c("Get them home.", 63),
    c("On to Ada.", 33)])
node(62, "You send Bex home and press on.", [
    c("Decide how to start.", 6),
    c("On toward the hill.", 33)])
node(63, "The kids' family thank you; a warm doorway, a hot drink.", [
    c("On toward the hill.", 33),
    c("The last stretch.", 90)])
node(67, "Okafor presses the last flask on you and starts to close up.", [
    c("On the way.", 21),
    c("His advice first.", 22)])
node(68, "A rumour of panic ripples down the queue at the shop.", [
    c("Calm it, and rally them.", 19),
    c("Into the shop.", 9)])

# ===== ACT II — INTO THE DARK TOWN =====
node(26, "The long road: black, iced, hard going, but solid underfoot.", [
    c("Press on.", 30),
    c("Someone's stuck ahead.", 31),
    c("The whole town, dark and quiet.", 64)])
node(27, "The frozen river shortcut would halve the way. The ice creaks.", [
    c("Risk the ice.", 28, sets="took_shortcut"),
    c("Too dangerous — back to the road.", 26)])
node(28, "Out on the ice, the black river below, every step a gamble.", [
    c("Edge across.", 50),
    c("The ice groans.", 51)])
node(30, "The road at night, the cold deepening by the hour.", [
    c("A family shivering at a dark window.", 32),
    c("Press on.", 33),
    c("You can see your breath.", 65),
    c("A signpost, half-buried in snow.", 39)])
node(31, "A car stuck in the snow, an old man at the wheel.", [
    c("Help push it clear.", 34, sets="helped_neighbour"),
    c("You can't stop — Ada.", 33)])
node(32, "A family with no heat, a baby crying in the cold.", [
    c("Give them your blanket.", 55, sets="gave_warmth"),
    c("Promise to send help.", 35),
    c("Try to warm the room.", 54)])
node(33, "On toward the hill.", [
    c("The van man again.", 40),
    c("The Harrow light.", 70),
    c("The last stretch.", 90),
    c("The cold makes you doubt.", 38)])
node(34, "The old man's car is free; he presses a flask on you.", [
    c("On your way.", 33),
    c("He tells you of the hill.", 70)])
node(35, "You promise help and move on.", [
    c("Rally the street.", 12),
    c("On toward the hill.", 33)])
node(38, "The cold gnaws at your resolve.", [
    c("The last stretch.", 90),
    c("The van man's lights.", 40)])
node(39, "A signpost half-buried in snow; which way?", [
    c("The road.", 26),
    c("The light on the hill.", 70)])
node(50, "Halfway across, the far bank close.", [
    c("Nearly there.", 52),
    c("The ice cracks.", 51)])
node(51, "The ice groans, then splits. A choice in a heartbeat.", [
    c("The ice gives way.", 129, req="took_shortcut"),
    c("Scramble back to the bank.", 53)])
node(52, "You reach the far bank, soaked to the knee, shaking.", [
    c("Push on, freezing.", 90),
    c("You lost the heater in the scramble.", 96)])
node(53, "You crawl back to the road, shaken, time lost.", [
    c("The long road after all.", 26),
    c("Too shaken to go on.", 131)])
node(54, "You try to warm the family's room, but there's no heat to give.", [
    c("Give them your blanket.", 55, sets="gave_warmth"),
    c("Promise to send help.", 35)])
node(55, "You wrap the baby in your own blanket; the family weeps thanks.", [
    c("On, colder now.", 56),
    c("They point you to the hill.", 70)])
node(56, "Without your blanket, the cold finds you fast.", [
    c("Keep moving to stay warm.", 33),
    c("A lit doorway offers shelter.", 57)])
node(57, "A stranger waves you in from a lit doorway for a minute.", [
    c("Warm up, then on.", 33),
    c("Refuse, press on.", 58)])
node(58, "You press on into the dark, teeth chattering.", [
    c("The last stretch.", 90),
    c("On toward the hill.", 33)])
node(64, "The whole town is dark and strangely quiet, waiting for the light.", [
    c("Press on down the road.", 30),
    c("The light in the Harrow house.", 70)])
node(65, "The temperature drops further; frost on your coat.", [
    c("The shivering family.", 32),
    c("Press on.", 33)])

# ===== THE VAN MAN (the trap) =====
node(40, "The van man: warm smile, cold stock. Generators, fuel, heaters — tonight only, cash only.", [
    c("Hear the price.", 41),
    c("Refuse and go round.", 42, sets="dodged_seller")])
node(41, "The price is robbery. He leans in: 'Your Ada won't last, friend. How much is she worth?'", [
    c("Pay him.", 43, sets="paid_seller"),
    c("That line is the tell — refuse.", 42, sets="dodged_seller"),
    c("Ask if it even works.", 44),
    c("The crowd's fear presses in.", 49)])
node(42, "You leave him to the frightened crowd.", [
    c("On the way.", 26),
    c("To the shop instead.", 9)])
node(43, "You hand over the cash. A heavy generator, a can of fuel.", [
    c("Haul it up the hill.", 45),
    c("A doubt already.", 46)])
node(44, "He won't quite promise it works.", [
    c("That's your answer — refuse.", 42, sets="dodged_seller"),
    c("Buy it anyway.", 43, sets="paid_seller")])
node(45, "The generator is dead weight, and it won't start in the cold.", [
    c("Try and try.", 47),
    c("On to Ada with nothing.", 90)])
node(46, "The fuel smells wrong — watery, thin.", [
    c("On to Ada.", 90),
    c("Back to argue.", 48)])
node(47, "The generator coughs and dies. The fuel was bad.", [
    c("On to Ada, fleeced.", 90),
    c("Leave it in the snow.", 48)])
node(48, "The van is gone. The crowd is gone. Only the cold, and your empty pockets.", [
    c("On to Ada.", 90),
    c("Stand a moment in the dark.", 38)])
node(49, "The frightened crowd shoves cash at him; you see the whole trick.", [
    c("Hear the price anyway.", 41),
    c("Refuse and go round.", 42, sets="dodged_seller")])

# ===== THE LIGHT IN THE HARROW HOUSE (the mystery) =====
node(70, "The old Harrow house, dark for years — but one window glows warm tonight. No one can explain it.", [
    c("Go and see.", 71),
    c("Leave it — Ada first.", 90)])
node(71, "You knock. No answer. The door is off the latch.", [
    c("Go in.", 72),
    c("Call out and wait.", 73),
    c("Years of dust and cold inside.", 78)])
node(72, "Inside: cold, bare, and old Mr Harrow on the floor by a guttering candle.", [
    c("Get him warm.", 74, sets="found_light"),
    c("Run for help.", 75)])
node(73, "A weak voice inside calls out.", [
    c("Go in.", 72),
    c("Fetch help.", 75)])
node(74, "You wrap Harrow, coax the fire, bring him round.", [
    c("He speaks of Ada.", 76),
    c("Get you both to Ada.", 90)])
node(75, "You run — but no help is coming till dawn. It is you or no one.", [
    c("Go back in.", 72),
    c("On to Ada, torn.", 90)])
node(76, "Harrow: 'Ada. My sister. We haven't spoken in forty years.'", [
    c("Resolve to bring them together.", 77),
    c("On to Ada with the news.", 90)])
node(77, "You decide to reunite them tonight.", [
    c("Down to Ada.", 90),
    c("Warm Harrow first.", 74)])
node(78, "The house holds years of cold and silence.", [
    c("Deeper in.", 72),
    c("An old photograph on the wall.", 79)])
node(79, "A photograph: Ada and Harrow, young, laughing together.", [
    c("Get him warm.", 74),
    c("The years between them.", 69)])
node(69, "Forty years of a shut door, ending tonight, one way or another.", [
    c("He speaks of Ada.", 76),
    c("Get him warm.", 74)])

# ===== ACT III — TOWARD FIRST LIGHT (Ada & the close) =====
node(90, "The last stretch to Ada's door on the hill, breath ragged in the cold.", [
    c("Let yourself in.", 91),
    c("The van man's last offer.", 80),
    c("Help arrives behind you.", 92)])
node(80, "The van man on the hill: 'Still cold up here? Last chance, friend.'", [
    c("Pay him.", 43, sets="paid_seller"),
    c("Refuse for good.", 91, sets="dodged_seller")])
node(91, "Inside Ada's: dark, cold, her breathing shallow under thin blankets.", [
    c("Set up warmth.", 93),
    c("Check she's alright.", 94),
    c("Her window looks toward the hill.", 98)])
node(92, "The street's help reaches the hill behind you.", [
    c("In to Ada together.", 93),
    c("Hold the night.", 100),
    c("Fires seen from her window.", 107)])
node(93, "Warmth: what you carried decides what you can do now.", [
    c("The heater.", 95),
    c("Candles, blankets, body heat.", 96)])
node(94, "Ada wakes, weak but glad to see your face.", [
    c("Get her warm.", 93),
    c("Set up the heater.", 95)])
node(95, "The paraffin heater catches; the little room begins to thaw.", [
    c("Hold the night.", 100),
    c("Help arrives.", 92)])
node(96, "No heater. You pile blankets, share heat, keep her talking.", [
    c("Hold the night.", 100),
    c("It may not be enough.", 97)])
node(97, "The cold is deep, and it may be more than blankets can hold.", [
    c("Hold on to dawn.", 100),
    c("Send for the rallied help.", 12)])
node(98, "From her window you can see the dark hill — and the one warm light.", [
    c("Get her warm first.", 93),
    c("The light nags at you.", 99)])
node(99, "The light on the hill, burning where no one lives.", [
    c("Warm Ada first.", 94),
    c("Hold the night.", 100)])
node(100, "The long hold to dawn: you keep the warmth in, keep her breathing easy.", [
    c("Watch for first light.", 101),
    c("The light on the hill nags.", 70),
    c("The night's longest hour.", 102)])
node(101, "The sky greys. The crews' headlights climb the hill. The power hums back.", [
    c("First light, and what it finds.", 110),
    c("Dawn over the frozen town.", 105)])
node(102, "The longest hour, before the dark thins.", [
    c("Watch for first light.", 101),
    c("Neighbours' fires down the hill.", 103)])
node(103, "Down the hill, small fires and candles — the town got through.", [
    c("First light.", 110),
    c("The lanterns of the dawn crew.", 104)])
node(104, "Headlights and grit trucks climb toward you at last.", [
    c("First light.", 110),
    c("What the night came to.", 114)])
node(105, "Dawn over the frozen town, pale and clean.", [
    c("First light.", 110),
    c("Help reaches the hill.", 92),
    c("The first birdsong.", 106)])
node(106, "The first birdsong, absurd over the ice.", [
    c("First light.", 110),
    c("Help reaches the hill.", 92)])
node(107, "From Ada's window, the neighbours' fires burn all down the hill.", [
    c("In to Ada.", 93),
    c("Hold the night.", 100)])

# ===== CLOSING HUBS =====
node(110, "First light: what the night comes to.", [
    c("Ada is warm and safe; the heater held.", 120, req="has_heater"),
    c("You found the light, and saved Harrow.", 121, req="found_light"),
    c("Weigh the rest.", 111)])
node(111, "The night adds up.", [
    c("The whole street came through together.", 122, req="rallied_town"),
    c("You did it clean — no con.", 123, req="dodged_seller"),
    c("Weigh the rest.", 112)])
node(112, "What else the night held.", [
    c("A neighbour takes you both in.", 124, req="helped_neighbour"),
    c("You gave your warmth away.", 125, req="gave_warmth"),
    c("Weigh the rest.", 113)])
node(113, "What the night leaves you.", [
    c("The power flickers back, late.", 126),
    c("The town saw you go out.", 127),
    c("The worst of it.", 114)])
node(114, "The hard end of the night.", [
    c("You paid the van man — fleeced.", 128, req="paid_seller"),
    c("You were simply too late.", 130),
    c("The power came back before real harm.", 126)])

# ===== ENDINGS (12: 4 good / 4 neutral / 4 bad) =====
end(120, "GOOD — Warm till first light. You get Mrs Ada safely through the cold; at dawn the power hums back and the crews' lights come up the hill. She is warm, and alive, because you went out.", "good")
end(121, "GOOD — The light in the empty house (secret). You checked the light no one could explain, found Mr Harrow fallen and freezing, and got him warm in time — and reopened a door between him and his sister Ada that had been shut for forty years.", "good")
end(122, "GOOD — The whole street, awake. No single heroic move — but you turned a frightened dark street into neighbours sharing one warm room, and everyone came through the night together.", "good")
end(123, "GOOD — You did what you could. You refused the con, kept your head and your money, and got the essentials by decent means. Not perfect. But clean, honest, and enough.", "good")
end(124, "NEUTRAL — The kindness returned. You fell short of the whole night's goal, but a neighbour you stopped for takes you and Ada in by their fire. Warmth without the full win.", "neutral")
end(125, "NEUTRAL — Shared what little you had. You gave your own warmth away and end the night cold yourself, but not alone — and something in the town has shifted. A start, not a save.", "neutral")
end(126, "NEUTRAL — One more hour. You scrape through the worst of it; the power flickers back late and grudging. Not triumphant — just, in the end, relieved.", "neutral")
end(127, "NEUTRAL — The town remembers. You didn't manage everything, but the street saw you go out into the dark when others didn't. You are, from tonight, someone the town knows.", "neutral")
end(128, "BAD — Fleeced in the dark. You paid the van man for a generator that won't start and fuel that won't burn. The money's gone, and the cold is exactly where it was.", "bad")
end(129, "BAD — The ice gave way. The frozen river was a trap. It nearly takes you, and it takes the night — you reach the hill soaked, frozen, and far too late.", "bad")
end(130, "BAD — Too late up the hill. You spent the night on the wrong things, and reach Mrs Ada cold and failing; by dawn she is being carried down to a waiting ambulance.", "bad")
end(131, "BAD — You kept your door shut. You stayed warm and safe behind your own door and never went out. Nothing bad happened to you. You will think about it for a long time.", "bad")

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
    "series": "first-light",
    "episode": 3,
    "title": "First Light",
    "slug": "first-light",
    "blurb": "The power fails across a snowed-in town on the coldest night of the winter. Up the hill, a frail neighbour needs heat to survive. You have until first light to keep her — and whoever else you meet — warm and alive.",
    "identity": {
        "name": "Cold Snap",
        "mood": "A frozen town gone dark; the only light is the warmth people carry to each other.",
        "palette": {
            "ground": "#0A111F", "surface": "#131E30", "ink": "#EEF2F7",
            "muted": "#7E8CA0", "line": "#223350",
            "accent": "#F2C065", "accentHot": "#FADB92", "secondary": "#8FC7E8"
        },
        "cover": {"kind": "candlelight", "glow": True},
        "type": {"display": "Fraunces", "ui": "Hanken Grotesk", "mono": "JetBrains Mono"},
        "hero": {
            "line": {
                "en": "The lights go out. Someone up the hill needs the warmth you carry.",
                "fr": "Les lumières s'éteignent. Là-haut, quelqu'un a besoin de la chaleur que vous portez.",
                "es": "Las luces se apagan. Alguien en la colina necesita el calor que llevas.",
                "it": "Le luci si spengono. Su in collina qualcuno ha bisogno del calore che porti.",
                "de": "Die Lichter gehen aus. Oben am Hügel braucht jemand die Wärme, die du trägst.",
                "pt": "As luzes apagam-se. Lá na colina, alguém precisa do calor que levas.",
                "ru": "Свет гаснет. Там, на холме, кому-то нужно тепло, которое ты несёшь.",
                "zh": "灯全灭了。山上有人需要你带去的那点温暖。",
                "ar": "تنطفئ الأضواء. في أعلى التل، شخص يحتاج إلى الدفء الذي تحمله."
            },
            "sub": "A story where you are the hero — and every choice turns you to a new page. Written for people learning English, at your level, with meaning in your language whenever you need it."
        }
    },
    "levels": ["A2", "B1", "B2"],
    "start": 1,
    "language_focus": {
        "A2": ["imperatives and going to", "the home, weather and warmth"],
        "B1": ["the first conditional and modals of advice", "helping, warning and planning"],
        "B2": ["inference, obligation and conditionals", "community, risk and responsibility"]
    },
    "state_in": STATE_IN,
    "state_out": STATE_OUT,
    "arc_flags": ARC_FLAGS,
    "nodes": nodes,
    "lexicon": {
        "_comment": "First Light's chosen lexicon. Grown in phase 4. Base-keyed; the reader resolves inflections. Translations need a native speaker's check before launch.",
        "entries": {}
    }
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(book, open(OUT, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(f"Wrote {OUT}: {len(nodes)} nodes, {sum(1 for n in nodes if n.get('ending'))} endings.")
