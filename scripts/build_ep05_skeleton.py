#!/usr/bin/env python3
"""Phase 2: graph skeleton for book 5, 'The Keeper' (standalone).

Every node is id + choices + gotos + flags + ending markers, with one-line stub text per level
(identical across A2/B1/B2 for now). Emits content/episode-05.json. Run the validator on the
output; it must return 0 errors before any real prose is written.

The graph topology reuses the proven, validator-clean engine (same ids, edges and flag positions)
re-skinned for the coast: warmth/water -> the light and its oil, the van/pickup -> the wrecker,
the frozen river / open flats -> the cliff path to the cove, the light in the empty house / the
smoke at the siding -> the second light on the water, the frail neighbour / lone child -> the old
keeper Nan Bright, hurt at the foot of the stairs. All prose (phase 3), cast, world, endings,
lexicon and art are new.

Run: python3 scripts/build_ep05_skeleton.py
"""
import json, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "content", "episode-05.json")

STATE_IN = []
OWN = ["has_light", "dodged_wrecker", "paid_wrecker", "found_boat",
       "rallied_coast", "helped_stranger", "gave_shelter", "took_shortcut"]
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

# ===== ACT I — THE LIGHT GOES OUT =====
node(1, "The worst storm of the year hits after dark. The power fails, and the lighthouse beacon dies with it. On the wet stairs the old keeper, Nan Bright, falls and cannot get up. Out past the point, a boat's small lights lift and fall in the swell. The great lamp must be kept by hand now — and that is on you.", [
    c("Take charge of the light.", 2),
    c("Try the radio for help.", 3),
    c("See to Nan first.", 4)])
node(2, "You gather what the tower has: a can of oil, spare wicks, matches, a storm-lamp. The wind screams in the rail outside.", [
    c("Step out into the storm.", 5),
    c("Decide how to start.", 6),
    c("The hand-lamp's wick is spoiled.", 29)])
node(3, "The radio crackles. Word gets through from Tam at the coast station: no lifeboat can launch into this sea until it eases or dawn comes. Keep the light if you can.", [
    c("Decide how to start.", 6),
    c("But that boat can't wait.", 8)])
node(4, "You get to Nan at the foot of the stairs and make her as easy as you can. But the light is still dark, and shelter alone won't do. You'll need oil and a plan.", [
    c("Go back and get the light going.", 2),
    c("Feel how serious this is.", 8)])
node(5, "Out on the gallery: black sea, rain driven flat, the boat's lights small and struggling past the point, the cove a well of dark below.", [
    c("Tam opens the oil store.", 9),
    c("Knock along the cottages for help.", 10),
    c("Decide how to start.", 6),
    c("Someone's out on the head.", 60)])
node(6, "Get the light going first, or see to the rest?", [
    c("The oil store.", 9),
    c("Straight up to the lamp.", 11),
    c("Rouse the coast for help.", 12)])
node(8, "The storm, and that boat closing on the rocks with no light to steer by. This is real, and it is on you.", [
    c("Decide how to start.", 6),
    c("To the oil store.", 9),
    c("A scramble at the store.", 68)])
node(9, "Tam heaves open the oil store: a barrel of oil, spare wicks, a box of matches, a good storm-lamp, dry rope.", [
    c("Take charge of the oil and wick.", 13, sets="has_light"),
    c("Just a storm-lamp and rope.", 14),
    c("Ask Tam what he knows.", 15),
    c("He presses the last dry lamp on you.", 67)])
node(10, "Along the cottages: old Da Finch, frightened and fumbling in the dark, his lamp dead and no matches.", [
    c("Stop and help him.", 16, sets="helped_stranger"),
    c("Say you must keep the light.", 17)])
node(11, "You get up to the lamp fast with what little you have. A spark, a flicker — but it won't hold without proper oil.", [
    c("Decide how to get real oil.", 21),
    c("The climb takes it out of you.", 18)])
node(12, "You go cottage to cottage, asking for hands on the rope and wood for a signal fire.", [
    c("The coast turns out.", 19, sets="rallied_coast"),
    c("No one stirs; go on alone.", 20)])
node(13, "The oil and wick — enough to keep the lamp burning the night, if you tend it well.", [
    c("Now, up to the lamp.", 21),
    c("Thank Tam.", 15)])
node(14, "A storm-lamp and a coil of rope: some light, but not the beam, and no proper oil secured.", [
    c("Now, find real oil.", 21),
    c("Ask Tam what he knows.", 15)])
node(15, "Bosun Carrick knows this coast: keep off the cliff path, don't trust the wrecker, mind the oil, hold the light.", [
    c("Take it to heart.", 22),
    c("On with it.", 21)])
node(16, "You settle Da Finch with a lit lamp and a blanket, and a promise to come back.", [
    c("On up to the lamp.", 23),
    c("He asks you to check the others.", 12)])
node(17, "You press on to keep the light.", [
    c("The oil store first.", 9),
    c("Straight up to the lamp.", 11)])
node(18, "Soaked and spent yourself, near your own limit.", [
    c("The wrecker's lantern is ahead.", 24),
    c("Push on.", 21)])
node(19, "The coast wakes to itself; a plan forms; someone rolls up a barrel of oil.", [
    c("Lead them up to the light.", 25),
    c("Light the signal fire first.", 36)])
node(20, "No one stirs. You go on alone.", [
    c("The oil store.", 9),
    c("On up to the lamp.", 11)])
node(21, "Light sorted. Now the cove and that boat: the long safe path round the head, or the cliff path straight down.", [
    c("Keep to the path.", 26),
    c("Take the cliff path.", 27),
    c("The wrecker's lantern ahead.", 24)])
node(22, "You resolve to be careful tonight.", [
    c("On the way.", 21),
    c("Back to the store.", 9)])
node(23, "Steadier for the good turn, you go on.", [
    c("On with the watch.", 21),
    c("Rouse more hands.", 12)])
node(24, "The wrecker, lantern swinging, boots in the surf: oil to sell, a strong back to offer, and reasons the light is not your job tonight.", [
    c("Hear him out.", 40),
    c("Go round him.", 26)])
node(25, "You lead a small band up toward the light.", [
    c("The way.", 26),
    c("The light out on the water.", 70)])
node(29, "The hand-lamp's wick is spoiled; only a guttering flame.", [
    c("Out into the storm.", 5),
    c("To the store for better.", 9)])
node(36, "The coast lights one signal fire on the head: a barrel ablaze, shelter, hands warming.", [
    c("Get the beam lit above it.", 25),
    c("Fetch more hands.", 37)])
node(37, "Cottage by cottage, the frightened shore becomes a working one.", [
    c("To the cove.", 26),
    c("The last of the watch.", 90)])
node(60, "Someone points to the head: a figure has gone out toward the point in the storm.", [
    c("Go after them.", 61, sets="helped_stranger"),
    c("No time — the light first.", 62)])
node(61, "You find them clinging in the rocks, half-drowned and lost.", [
    c("Walk them back.", 63),
    c("On to the light.", 33)])
node(62, "You send word for someone else to go, and press on.", [
    c("Decide how to start.", 6),
    c("On toward the cove.", 33)])
node(63, "Their family thank you; a dry coat, a place by the fire.", [
    c("On toward the cove.", 33),
    c("The last of the watch.", 90)])
node(67, "Tam presses the last dry lamp on you and turns back to the crackling radio.", [
    c("On the way.", 21),
    c("His warning first.", 22)])
node(68, "A scramble at the oil store; voices rising, hands grabbing the cans.", [
    c("Calm it, and share it out.", 19),
    c("Get to the oil.", 9)])

# ===== ACT II — THE LONG WATCH =====
node(26, "The head path: black, streaming, hard going, but solid underfoot.", [
    c("Press on.", 30),
    c("Someone's in trouble ahead.", 31),
    c("The whole coast, dark and roaring.", 64)])
node(27, "The cliff path would halve the way to the cove — but it's a ledge in a gale, wet rock over a black drop.", [
    c("Risk the cliff path.", 28, sets="took_shortcut"),
    c("Too dangerous — back to the path.", 26)])
node(28, "Out on the ledge, the drop below, every step a gamble in the wind.", [
    c("Edge on.", 50),
    c("The wind slams the cliff.", 51)])
node(30, "The path along the head, the storm deepening by the hour.", [
    c("A family in a flooding cottage.", 32),
    c("Press on.", 33),
    c("The wind nearly has you off your feet.", 65),
    c("A marker post, half torn away.", 39)])
node(31, "A boat swamped on the slip, an old man tangled in the lines.", [
    c("Help cut him free.", 34, sets="helped_stranger"),
    c("You can't stop — the light.", 33)])
node(32, "A family in a low cottage with the sea coming under the door, no lamp, a child crying.", [
    c("Give them your own lamp and coat.", 55, sets="gave_shelter"),
    c("Promise to send help.", 35),
    c("Try to bank the door against the water.", 54)])
node(33, "On through the worst of the storm.", [
    c("The wrecker again.", 40),
    c("The light out on the water.", 70),
    c("The last of the watch.", 90),
    c("The storm makes you doubt.", 38)])
node(34, "The man's cut free; he presses a dry oilskin on you in thanks.", [
    c("On your way.", 33),
    c("He tells you of the light on the water.", 70)])
node(35, "You promise help and move on.", [
    c("Rouse the coast.", 12),
    c("On through the storm.", 33)])
node(38, "The storm gnaws at your resolve.", [
    c("The last of the watch.", 90),
    c("The wrecker's lantern.", 40)])
node(39, "A marker post, half torn away; which way?", [
    c("The path.", 26),
    c("The light on the water.", 70)])
node(50, "Far out on the ledge, the cove at last seems closer — or does it?", [
    c("Nearly down.", 52),
    c("The rock crumbles under you.", 51)])
node(51, "The ledge, the wind, the black drop; a choice in a heartbeat.", [
    c("You go off the edge.", 129, req="took_shortcut"),
    c("Throw yourself back from the edge while you can.", 53)])
node(52, "You reach the cove, soaked and shaking, but down.", [
    c("Push on, spent.", 90),
    c("You lost the oil in the scramble.", 96)])
node(53, "You crawl back to the path, shaken, the night burning away.", [
    c("The long path after all.", 26),
    c("Too spent to go on.", 131)])
node(54, "You try to bank the door against the water, but there's no lamp to give.", [
    c("Give them your own lamp and coat.", 55, sets="gave_shelter"),
    c("Promise to send help.", 35)])
node(55, "You hand over your own coat and lamp; the family huddle, weak with relief.", [
    c("On, colder now.", 56),
    c("They point you to the light on the water.", 70)])
node(56, "Without your coat, the cold and wet find you fast.", [
    c("Keep moving, keep your head.", 33),
    c("A lit doorway offers a minute.", 57)])
node(57, "A stranger waves you into a doorway, out of the rain for a minute.", [
    c("Warm up, then on.", 33),
    c("Refuse, press on.", 58)])
node(58, "You press on into the storm, soaked to the bone.", [
    c("The last of the watch.", 90),
    c("On toward the cove.", 33)])
node(64, "The whole coast, dark and roaring, everything waiting for the storm to break.", [
    c("Press on along the head.", 30),
    c("The light on the water.", 70)])
node(65, "The wind climbs to its worst; it nearly takes you off your feet.", [
    c("The flooding cottage.", 32),
    c("Press on.", 33)])

# ===== THE WRECKER (the trap) =====
node(40, "The wrecker: easy smile, a can of oil in his fist. 'The light's not your job, friend. Why break yourself for strangers?'", [
    c("Hear the price.", 41),
    c("Refuse and go round.", 42, sets="dodged_wrecker")])
node(41, "The offer is a hook. He leans in: 'That boat's lost anyway. Let the dark do its work, and there's a share in it for you.'", [
    c("Take his deal.", 43, sets="paid_wrecker"),
    c("That line is the tell — refuse.", 42, sets="dodged_wrecker"),
    c("Ask what he really wants.", 44),
    c("The frightened folk press in.", 49)])
node(42, "You leave him to the surf.", [
    c("On the way.", 26),
    c("To the oil store instead.", 9)])
node(43, "You take his oil, his coin. Something in you already knows.", [
    c("Carry it up.", 45),
    c("A doubt already.", 46)])
node(44, "He won't quite say why he wants the light left dark.", [
    c("That's your answer — refuse.", 42, sets="dodged_wrecker"),
    c("Take it anyway.", 43, sets="paid_wrecker")])
node(45, "The oil is fouled with seawater; it won't feed the flame, and the beam gutters low.", [
    c("Try to work it.", 47),
    c("Up to Nan with nothing.", 90)])
node(46, "The oil smells wrong — salt, thin, cut.", [
    c("Up to the lamp.", 90),
    c("Back to have it out with him.", 48)])
node(47, "The wrecker's lantern is already gone down the cove. He was never helping.", [
    c("Up to the lamp, fooled.", 90),
    c("Fling the fouled can into the surf.", 48)])
node(48, "The wrecker's gone. The cove's empty. Only the storm, and what you gave him.", [
    c("Up to the lamp.", 90),
    c("Stand a moment in the dark.", 38)])
node(49, "The frightened folk press their coins on him; you see the whole trick.", [
    c("Hear the price anyway.", 41),
    c("Refuse and go round.", 42, sets="dodged_wrecker")])

# ===== THE LIGHT ON THE WATER (the mystery) =====
node(70, "Far out past the point, a second light lifts and falls where no boat should be. No one can explain it.", [
    c("Go and answer it.", 71),
    c("Leave it — the light first.", 90)])
node(71, "You get down to the cove. You call out. No answer but the sea — then a boat's shape on the rocks.", [
    c("Wade out to it.", 72),
    c("Call again and wait.", 73),
    c("The boat's stove in, half under.", 78)])
node(72, "On the rocks: old Ash, tangled in a swamped boat, barely holding on.", [
    c("Get them off and warm.", 74, sets="found_boat"),
    c("Run for help.", 75)])
node(73, "A weak voice answers over the wind.", [
    c("Wade out.", 72),
    c("Fetch help.", 75)])
node(74, "You drag Ash clear, wrap them, bring them round. They gasp it out: keep the light — there may be others out there.", [
    c("Ash speaks of Nan.", 76),
    c("Get you both back to the tower.", 90)])
node(75, "You run — but no lifeboat comes till dawn. It is you or no one.", [
    c("Go back for them.", 72),
    c("Up to the lamp, torn.", 90)])
node(76, "Ash looks at you: 'The keeper up there — Nan? That's my mother. We haven't spoken in years.'", [
    c("Resolve to bring them together.", 77),
    c("Up with the news.", 90)])
node(77, "You decide to get them face to face before the night is out.", [
    c("Back to the tower.", 90),
    c("Get Ash steady first.", 74)])
node(78, "The boat is stove in, half under, the sea working at it.", [
    c("Wade closer.", 72),
    c("A name painted on the bow.", 79)])
node(79, "A name on the bow — Nan's own boat, thought lost years ago. A weak sound from under the hull.", [
    c("Follow the sound, and find them.", 74, sets="found_boat"),
    c("The years in it.", 69)])
node(69, "Years of a shut door between them. Then a cough, and breathing, from under the hull.", [
    c("Follow the breathing, and find them.", 74, sets="found_boat"),
    c("It's too much — back to the light.", 90)])

# ===== ACT III — TOWARD FIRST LIGHT (the lamp & the close) =====
node(90, "The last of the worst storm, back at the tower, soaked through, Nan grey at the foot of the stairs, the lamp burning low.", [
    c("See to the light.", 91),
    c("The wrecker's last offer.", 80),
    c("Help arrives behind you.", 92)])
node(80, "The wrecker, one last time: 'Still fighting it? Let it go dark. Last chance to be on the winning side.'", [
    c("Take his deal.", 43, sets="paid_wrecker"),
    c("Refuse for good.", 91, sets="dodged_wrecker")])
node(91, "At the lamp: the flame low, the lens still, the boat's lights close to the rocks now.", [
    c("Get the beam full and turning.", 93),
    c("Check on Nan below.", 94),
    c("A light flares far out to sea.", 98)])
node(92, "Help reaches the tower behind you — hands, oil, a plan.", [
    c("To the lamp together.", 93),
    c("Hold the watch.", 100),
    c("A lamp on the water, far off.", 107)])
node(93, "Keeping the beam: what you carried decides what you can do now.", [
    c("The oil and wick.", 95),
    c("Coax the guttering flame.", 96)])
node(94, "Nan wakes, weak but glad to see your face.", [
    c("Get the light full.", 93),
    c("Break out the oil.", 95)])
node(95, "The oil does it: the wick trims true, the lens winds round, and the beam swings out full and gold.", [
    c("Hold the watch.", 100),
    c("Help arrives.", 92)])
node(96, "No proper oil. You coax the guttering flame, shield it with your body, keep it just alive.", [
    c("Hold the watch.", 100),
    c("It may not be enough.", 97)])
node(97, "The flame is low, and it may be more than shielding can hold.", [
    c("Hold on to first light.", 100),
    c("Send for the rallied help.", 12)])
node(98, "Far out to sea, a light flares and falls where no boat should be.", [
    c("See to the light first.", 93),
    c("The light nags at you.", 99)])
node(99, "The light on the water, out where everyone swears no boat would be.", [
    c("The lamp first.", 94),
    c("Hold the watch.", 100)])
node(100, "The long hold: you keep the beam turning, keep Nan breathing, watch through the storm.", [
    c("Watch for first light.", 101),
    c("The light on the water still nags.", 70),
    c("The night's worst hour.", 102)])
node(101, "The wind drops a note. The sky greys at the edge. A lamp swings round the point — the lifeboat, at last.", [
    c("First light, and what it finds.", 110),
    c("Dawn over the wild sea.", 105)])
node(102, "The worst hour, before the storm breaks.", [
    c("Watch for first light.", 101),
    c("Other lamps along the head.", 103)])
node(103, "Along the head, lamps and figures — the coast got through too.", [
    c("First light.", 110),
    c("The lifeboat's lamp coming round.", 104)])
node(104, "The lifeboat's lamp and a plume of spray come round the point at last.", [
    c("First light.", 110),
    c("What the night came to.", 114)])
node(105, "Dawn over the wild sea, grey and clean, the storm blowing itself out.", [
    c("First light.", 110),
    c("Help reaches the tower.", 92),
    c("The first gull over the water.", 106)])
node(106, "The first gull over the water, absurd after the night.", [
    c("First light.", 110),
    c("Help reaches the tower.", 92)])
node(107, "From the tower, far off on the water, a lamp lifting and falling.", [
    c("To the lamp.", 93),
    c("Hold the watch.", 100)])

# ===== CLOSING HUBS =====
node(110, "First light: what the night comes to.", [
    c("The boat made harbour; the light held.", 120, req="has_light"),
    c("You answered the light, and saved Ash.", 121, req="found_boat"),
    c("Weigh the rest.", 111)])
node(111, "The night adds up.", [
    c("The whole coast came through together.", 122, req="rallied_coast"),
    c("You did it clean — no con.", 123, req="dodged_wrecker"),
    c("Weigh the rest.", 112)])
node(112, "What else the night held.", [
    c("A stranger you helped sees you home.", 124, req="helped_stranger"),
    c("You gave your own lamp away.", 125, req="gave_shelter"),
    c("Weigh the rest.", 113)])
node(113, "What the night leaves you.", [
    c("The storm eases at last, late.", 126),
    c("The coast saw you climb to the lamp.", 127),
    c("The worst of it.", 114)])
node(114, "The hard end of the night.", [
    c("You took the wrecker's deal — a ship struck.", 128, req="paid_wrecker"),
    c("You were simply too late.", 130),
    c("The storm broke before real harm.", 126)])

# ===== ENDINGS (12: 4 good / 4 neutral / 4 bad) =====
end(120, "GOOD — The light held. You kept the beam burning all night; at first light the storm breaks, the lifeboat comes round the point, and the boat you were lighting makes the harbour mouth. It is safe because you climbed to the lamp and stayed.", "good")
end(121, "GOOD — The light on the water (secret). You answered the light no one could explain, found old Ash swamped on the rocks and got them off in time — and reopened a door between Ash and Nan Bright that had been shut for years.", "good")
end(122, "GOOD — The whole coast, awake. No single heroic move — but you turned a frightened shore into people on the rope and signal fires along the head, and everyone came through the night together.", "good")
end(123, "GOOD — You did what you could. You refused the con, kept your head, and kept the light by decent means. Not perfect. But clean, honest, and enough.", "good")
end(124, "NEUTRAL — The kindness returned. You fell short of the whole night's goal, but the fisher you stopped for gets you and Nan to safety and helps hold the light. Rescue without the full win.", "neutral")
end(125, "NEUTRAL — Shared what you had. You gave your own coat and lamp away and end the night cold yourself, but not alone — and something on the coast has shifted. A start, not a save.", "neutral")
end(126, "NEUTRAL — One more hour. You scrape through the worst of it; the storm eases late and grudging, and the boat limps in on its own. Not triumphant — just, in the end, relieved.", "neutral")
end(127, "NEUTRAL — The coast remembers. You didn't manage everything, but the shore saw you climb to the lamp when others barred their doors. You are, from tonight, someone this coast knows.", "neutral")
end(128, "BAD — You lit the wrong way. You took the wrecker's deal, and the light served the wrong master; a ship struck the rocks in the dark, and the sea took what it wanted. The money's cold, and so is the shore by morning.", "bad")
end(129, "BAD — The rocks took it. The cliff path was a trap; the wind nearly takes you off the edge, and it takes the night — you reach the cove soaked, broken, and far too late.", "bad")
end(130, "BAD — Dark too long. You spent the night on the wrong things, and the light went dark too long; by dawn there is wreckage on the shore and a search along the tideline.", "bad")
end(131, "BAD — You barred the door. You stayed safe and dry inside and never climbed to the lamp. Nothing bad happened to you. You will think about it for a long time.", "bad")

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
    "series": "the-keeper",
    "episode": 5,
    "title": "The Keeper",
    "slug": "the-keeper",
    "blurb": "The worst storm of the year kills the power, the lighthouse beacon dies, and the old keeper is hurt at the foot of the stairs — just as a boat's lights struggle offshore. Keeping the great lamp burning by hand is on you now. You have until first light to hold the beam, and whoever the sea sends, against the dark.",
    "identity": {
        "name": "Tempest",
        "mood": "A storm-black coast; the only light is the beam that keeps ships off the rocks.",
        "palette": {
            "ground": "#0B141B", "surface": "#14212B", "ink": "#EAF1F5",
            "muted": "#7C8B98", "line": "#223341",
            "accent": "#F3D27E", "accentHot": "#FBEBBE", "secondary": "#86B3C4"
        },
        "cover": {"kind": "beacon", "glow": True},
        "type": {"display": "Fraunces", "ui": "Hanken Grotesk", "mono": "JetBrains Mono"},
        "hero": {
            "line": {
                "en": "The light goes out in the storm. A boat out past the rocks needs the beam you keep burning.",
                "fr": "La lumière s'éteint dans la tempête. Au large des rochers, un bateau a besoin du feu que vous gardez allumé.",
                "es": "La luz se apaga en la tormenta. Más allá de las rocas, un barco necesita el faro que mantienes encendido.",
                "it": "La luce si spegne nella tempesta. Oltre gli scogli, una barca ha bisogno del faro che tieni acceso.",
                "de": "Das Licht erlischt im Sturm. Draußen hinter den Felsen braucht ein Boot den Schein, den du am Brennen hältst.",
                "pt": "A luz apaga-se na tempestade. Para lá dos rochedos, um barco precisa do farol que manténs aceso.",
                "ru": "Свет гаснет в шторм. Там, за скалами, лодке нужен луч, который ты не даёшь погаснуть.",
                "zh": "灯在风暴中熄灭了。礁石之外，一条船需要你守住的那束光。",
                "ar": "ينطفئ الضوء في العاصفة. خلف الصخور، يحتاج قاربٌ إلى النور الذي تُبقيه مشتعلاً."
            },
            "sub": "A story where you are the hero — and every choice turns you to a new page. Written for people learning English, at your level, with meaning in your language whenever you need it."
        }
    },
    "levels": ["A2", "B1", "B2"],
    "start": 1,
    "language_focus": {
        "A2": ["imperatives and going to", "the sea, weather and the body"],
        "B1": ["the first conditional and modals of advice", "warning, helping and planning"],
        "B2": ["inference, obligation and conditionals", "duty, risk and responsibility"]
    },
    "state_in": STATE_IN,
    "state_out": STATE_OUT,
    "arc_flags": ARC_FLAGS,
    "nodes": nodes,
    "lexicon": {
        "_comment": "The Keeper's chosen lexicon. Grown in phase 4. Base-keyed; the reader resolves inflections. Translations need a native speaker's check before launch.",
        "entries": {}
    }
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(book, open(OUT, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(f"Wrote {OUT}: {len(nodes)} nodes, {sum(1 for n in nodes if n.get('ending'))} endings.")
