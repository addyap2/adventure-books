#!/usr/bin/env python3
"""Phase 2: graph skeleton for book 4, 'The Cool of Evening' (standalone).

Every node is id + choices + gotos + flags + ending markers, with one-line stub text per level
(identical across A2/B1/B2 for now). Emits content/episode-04.json. Run the validator on the
output; it must return 0 errors before any real prose is written.

The graph topology reuses book 3's proven, validator-clean engine (same ids, edges and flag
positions) re-skinned for the desert: warmth->water, the van man->the pickup man, the frozen
river->the open flats, the light in the empty house->the smoke at the empty siding, the frail
neighbour up the hill (Ada)->the lone child on the bus (Sami). All prose (phase 3), cast, world,
endings, lexicon and art are new.

Run: python3 scripts/build_ep04_skeleton.py
"""
import json, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "content", "episode-04.json")

STATE_IN = []
OWN = ["has_water", "dodged_seller", "paid_seller", "found_well",
       "rallied_bus", "helped_stranger", "gave_water", "took_shortcut"]
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

# ===== ACT I — THE ENGINE DIES =====
node(1, "At the hottest hour, the bus coughs and dies on an empty desert road — hours from anywhere, no signal. On board is Sami, a child of about eight travelling alone, already going quiet with the heat. There is not much water.", [
    c("Take charge of the water.", 2),
    c("Try the radio for help.", 3),
    c("Get Sami into shade first.", 4)])
node(2, "You gather what the bus has: a few water bottles, a first-aid box, a canvas tarp that could make shade. The heat is already building.", [
    c("Step out onto the road.", 5),
    c("Decide how to start.", 6),
    c("The tarp is torn and short.", 29)])
node(3, "The radio is dead and there is no signal. Word passes back from Mr Bello: nothing moves in this heat, help comes at evening, sit tight and stay cool.", [
    c("Decide how to start.", 6),
    c("But Sami can't wait that long.", 8)])
node(4, "You move Sami into the thin shade of the bus, but shade alone won't be enough. You'll need water and a plan to do any good.", [
    c("Go back and organise supplies.", 2),
    c("Feel how serious this is.", 8)])
node(5, "The road: white glare, ochre flats to the horizon, the far ridge shimmering, heat you can almost lean on.", [
    c("Mr Bello opens the bus's stores.", 9),
    c("Ask along the seats for water.", 10),
    c("Decide how to start.", 6),
    c("A passenger has wandered off down the road.", 60)])
node(6, "Sort out supplies first, or get straight to keeping Sami cool?", [
    c("The bus's stores.", 9),
    c("Straight to Sami.", 11),
    c("Go seat to seat to gather help.", 12)])
node(8, "The heat, and Sami going quiet and dizzy with no water. This is real, and it is on you.", [
    c("Decide how to start.", 6),
    c("To the bus's stores.", 9),
    c("A rush on the water at the front.", 68)])
node(9, "Mr Bello opens the luggage bay, ashamed: a crate of water bottles, a first-aid box, a big canvas tarp, spare rags.", [
    c("Take charge of the water crate.", 13, sets="has_water"),
    c("Just the tarp and rags.", 14),
    c("Ask Bello what he knows.", 15),
    c("He hands you the last cool bottle.", 67)])
node(10, "Along the seats: old Mr Danso, confused and dry-mouthed, plucking at his collar in the heat.", [
    c("Stop and help him.", 16, sets="helped_stranger"),
    c("Say you must see to Sami.", 17)])
node(11, "You get to Sami fast with what little you have. It steadies the child a moment — but it won't last without more water.", [
    c("Decide how to reach more water.", 21),
    c("The heat presses on you too.", 18)])
node(12, "You go seat to seat, asking people to pool their water and share the shade.", [
    c("The passengers turn out to help.", 19, sets="rallied_bus"),
    c("No one moves; go on alone.", 20)])
node(13, "The water crate — heavy, precious, enough if it is shared and rationed well.", [
    c("Now, get it to Sami and the weak.", 21),
    c("Thank Bello.", 15)])
node(14, "The tarp and rags: shade, but no water secured.", [
    c("Now the way to more water.", 21),
    c("Ask Bello what he knows.", 15)])
node(15, "Auntie Rose knows this road: keep off the open flats, don't trust the pickup man, ration every drop, wait out the sun.", [
    c("Take it to heart.", 22),
    c("On with it.", 21)])
node(16, "You settle Mr Danso in the shade with a mouthful of water and a promise to check back.", [
    c("On toward Sami.", 23),
    c("He asks you to check the others.", 12)])
node(17, "You press on to see to Sami.", [
    c("The bus's stores first.", 9),
    c("Straight to the child.", 11)])
node(18, "Parched and light-headed yourself, near your own limit.", [
    c("The pickup man's dust is ahead.", 24),
    c("Push on.", 21)])
node(19, "The bus wakes to itself; a plan forms; someone has a big water carrier.", [
    c("Lead the way to Sami.", 25),
    c("Set up one shaded spot first.", 36)])
node(20, "No one moves. You go on alone.", [
    c("The bus's stores.", 9),
    c("On to the water.", 11)])
node(21, "Supplies decided. Now, real water: the long walk by the road, or the shortcut straight across the open flats to the ridge.", [
    c("Keep to the road.", 26),
    c("Cut across the flats.", 27),
    c("The pickup man's dust ahead.", 24)])
node(22, "You resolve to be careful this afternoon.", [
    c("On the way.", 21),
    c("Back to the stores.", 9)])
node(23, "Steadier for the good turn, you go on.", [
    c("On with the afternoon.", 21),
    c("Gather more help.", 12)])
node(24, "The pickup man, parked on the shoulder, engine ticking: bottled water, a lift to town, a frightened little crowd around him.", [
    c("Hear what he's selling.", 40),
    c("Go round him.", 26)])
node(25, "You lead a small group toward Sami and the shade.", [
    c("The way.", 26),
    c("The smoke out at the siding.", 70)])
node(29, "The tarp is torn and too short; only the rags for shade.", [
    c("Out onto the road.", 5),
    c("To the stores for better.", 9)])
node(36, "The bus makes one shaded spot: the tarp rigged, bottles pooled, the weak in the middle.", [
    c("Get Sami into it.", 25),
    c("Fetch more passengers.", 37)])
node(37, "Seat by seat, the frightened bus becomes an organised one.", [
    c("To the water.", 26),
    c("The last stretch of the heat.", 90)])
node(60, "Someone points down the road: a passenger has wandered off toward the shimmer, dazed by the heat.", [
    c("Go after them.", 61, sets="helped_stranger"),
    c("No time — Sami first.", 62)])
node(61, "You find them stumbling in a dry gully, sun-struck and lost.", [
    c("Walk them back.", 63),
    c("On to Sami.", 33)])
node(62, "You send word for someone else to go, and press on.", [
    c("Decide how to start.", 6),
    c("On toward the water.", 33)])
node(63, "Their family on the bus thank you; a shared bottle, a place in the shade.", [
    c("On toward the water.", 33),
    c("The last stretch of the heat.", 90)])
node(67, "Bello presses the last cool bottle on you and turns back to the engine.", [
    c("On the way.", 21),
    c("His warning first.", 22)])
node(68, "A rush on the water at the front of the bus; voices rising, hands grabbing.", [
    c("Calm it, and get them sharing.", 19),
    c("Get to the crate.", 9)])

# ===== ACT II — THE LONG AFTERNOON =====
node(26, "The road: baking tarmac, mirage pools ahead, hard going but a clear line to follow.", [
    c("Press on.", 30),
    c("Someone's stuck ahead.", 31),
    c("The whole plain, empty and shimmering.", 64)])
node(27, "The flats would halve the way to the ridge — but the ground is open, trackless, and the heat sits on it like a hand.", [
    c("Risk the flats.", 28, sets="took_shortcut"),
    c("Too dangerous — back to the road.", 26)])
node(28, "Out on the open flats, the ridge no closer, the shimmer swallowing the road behind you.", [
    c("Push on across.", 50),
    c("The horizon warps and slides.", 51)])
node(30, "The road under the white sun, the heat deepening by the hour.", [
    c("A family stalled at the roadside.", 32),
    c("Press on.", 33),
    c("The sun sits on your neck like a weight.", 65),
    c("A signpost, paint blistered off.", 39)])
node(31, "A car stalled in the sand, an old man slumped at the wheel.", [
    c("Help get it moving.", 34, sets="helped_stranger"),
    c("You can't stop — Sami.", 33)])
node(32, "A stalled family, out of water, a small child crying and red in the heat.", [
    c("Give them your own water.", 55, sets="gave_water"),
    c("Promise to send help.", 35),
    c("Try to make them shade.", 54)])
node(33, "On through the worst of the heat.", [
    c("The pickup man again.", 40),
    c("The smoke at the siding.", 70),
    c("The last stretch of the heat.", 90),
    c("The heat makes you doubt.", 38)])
node(34, "The car's free; the old man presses a warm bottle on you in thanks.", [
    c("On your way.", 33),
    c("He tells you of the siding.", 70)])
node(35, "You promise help and move on.", [
    c("Rally the bus.", 12),
    c("On through the heat.", 33)])
node(38, "The heat gnaws at your resolve.", [
    c("The last stretch of the heat.", 90),
    c("The pickup man's dust.", 40)])
node(39, "A signpost, paint blistered white; which way?", [
    c("The road.", 26),
    c("The smoke at the siding.", 70)])
node(50, "Far out, the ridge at last seems closer — or does it?", [
    c("Nearly there.", 52),
    c("The ground shimmers and lies.", 51)])
node(51, "The flats go on and on; your head swims, the horizon breaks apart. A choice in a heartbeat.", [
    c("You go down in the open.", 129, req="took_shortcut"),
    c("Turn back for the road while you still can.", 53)])
node(52, "You reach the ridge's foot, staggering, tongue thick, but there.", [
    c("Push on, spent.", 90),
    c("You dropped the water somewhere back there.", 96)])
node(53, "You struggle back to the road, shaken, the afternoon burning away.", [
    c("The long road after all.", 26),
    c("Too spent to go on.", 131)])
node(54, "You try to rig them some shade, but there's no water to give.", [
    c("Give them your own water.", 55, sets="gave_water"),
    c("Promise to send help.", 35)])
node(55, "You hand over your own bottle; the family drink, weak with relief.", [
    c("On, drier now.", 56),
    c("They point you to the siding.", 70)])
node(56, "Without your water, the heat finds you fast.", [
    c("Keep moving, keep your head.", 33),
    c("A strip of shade offers a minute's rest.", 57)])
node(57, "A stranger waves you into a strip of shade for a minute.", [
    c("Rest, then on.", 33),
    c("Refuse, press on.", 58)])
node(58, "You press on into the glare, mouth like paper.", [
    c("The last stretch of the heat.", 90),
    c("On toward the water.", 33)])
node(64, "The whole plain lies empty and shimmering, everything waiting for the sun to drop.", [
    c("Press on down the road.", 30),
    c("The smoke at the siding.", 70)])
node(65, "The sun climbs to its worst; the tar softens, the air burns.", [
    c("The stalled family.", 32),
    c("Press on.", 33)])

# ===== THE PICKUP MAN (the trap) =====
node(40, "The pickup man: cool smile, warm bottles, a lift to town — today only, cash only.", [
    c("Hear the price.", 41),
    c("Refuse and go round.", 42, sets="dodged_seller")])
node(41, "The price is robbery. He leans out: 'That kid won't last, friend. What's a child worth to you?'", [
    c("Pay him.", 43, sets="paid_seller"),
    c("That line is the tell — refuse.", 42, sets="dodged_seller"),
    c("Ask if the water's even cold.", 44),
    c("The crowd's fear presses in.", 49)])
node(42, "You leave him to the frightened crowd.", [
    c("On the way.", 26),
    c("To the bus's stores instead.", 9)])
node(43, "You hand over the cash. Warm bottles, a promise of a lift.", [
    c("Carry them back.", 45),
    c("A doubt already.", 46)])
node(44, "He won't quite say the water's clean or cold.", [
    c("That's your answer — refuse.", 42, sets="dodged_seller"),
    c("Buy it anyway.", 43, sets="paid_seller")])
node(45, "The bottles are hot as bathwater, and the 'lift' never comes.", [
    c("Try to flag him back.", 47),
    c("On to Sami with nothing.", 90)])
node(46, "The water tastes wrong — brackish, warm, thin.", [
    c("On to Sami.", 90),
    c("Back to argue.", 48)])
node(47, "The pickup's dust is already on the horizon. The lift was never coming.", [
    c("On to Sami, fleeced.", 90),
    c("Leave the hot bottles in the sand.", 48)])
node(48, "The pickup's gone. The crowd's scattered. Only the heat, and your empty pockets.", [
    c("On to Sami.", 90),
    c("Stand a moment in the glare.", 38)])
node(49, "The frightened crowd shoves cash at him; you see the whole trick.", [
    c("Hear the price anyway.", 41),
    c("Refuse and go round.", 42, sets="dodged_seller")])

# ===== THE SMOKE AT THE SIDING (the mystery) =====
node(70, "The old rail-stop siding, shut for years — but a thread of smoke rises and a windmill turns. No one can explain it.", [
    c("Go and see.", 71),
    c("Leave it — Sami first.", 90)])
node(71, "You reach it. You knock. No answer. The door stands ajar.", [
    c("Go in.", 72),
    c("Call out and wait.", 73),
    c("Years of dust and heat-crack inside.", 78)])
node(72, "Inside, dim and stifling: old Mr Faro, down on the floor by a dead radio, barely moving.", [
    c("Get him cool and watered.", 74, sets="found_well"),
    c("Run for help.", 75)])
node(73, "A weak voice inside answers.", [
    c("Go in.", 72),
    c("Fetch help.", 75)])
node(74, "You get water into Faro, fan him, bring him round. He points: the deep well out back — and the radio, if you can raise it.", [
    c("He speaks of the road.", 76),
    c("Get you both back to the bus.", 90)])
node(75, "You run — but there is no help out here till evening. It is you or no one.", [
    c("Go back in.", 72),
    c("On to Sami, torn.", 90)])
node(76, "Faro looks at you: 'You came off the noon bus? There's an old friend of mine aboard, I'd bet — Rose. Tell her Faro's still here.'", [
    c("Resolve to bring them together.", 77),
    c("On to Sami with the news.", 90)])
node(77, "You decide to get them face to face before the day is out.", [
    c("Back to the bus.", 90),
    c("Get Faro steady first.", 74)])
node(78, "The place holds years of dust, dry heat, and silence.", [
    c("Deeper in.", 72),
    c("An old photo, curled on the wall.", 79)])
node(79, "A photo: Faro and a young woman by this very windmill, both laughing. A weak sound from the back room.", [
    c("Follow the sound, and find him.", 74, sets="found_well"),
    c("The years in the dust.", 69)])
node(69, "Years of a shut-up house. Then breathing, slow and shallow, from the back room.", [
    c("Follow the breathing, and find him.", 74, sets="found_well"),
    c("It's too much — back to Sami.", 90)])

# ===== ACT III — TOWARD THE COOL OF EVENING (Sami & the close) =====
node(90, "The last of the worst heat, back at the bus, your breath dry, Sami pale in the shade.", [
    c("See to the child.", 91),
    c("The pickup man's last offer.", 80),
    c("Help arrives behind you.", 92)])
node(80, "The pickup man rolls back: 'Still stuck? Still thirsty? Last chance, friend.'", [
    c("Pay him.", 43, sets="paid_seller"),
    c("Refuse for good.", 91, sets="dodged_seller")])
node(91, "At Sami's side: the child hot, breathing fast and shallow, lips cracked.", [
    c("Set up real cooling.", 93),
    c("Check the child over.", 94),
    c("A glint far off catches your eye.", 98)])
node(92, "Help reaches the bus behind you — hands, water, a plan.", [
    c("To Sami together.", 93),
    c("Hold through the worst.", 100),
    c("Dust on the road, far off.", 107)])
node(93, "Cooling the child: what you carried decides what you can do now.", [
    c("The water crate.", 95),
    c("Wet rags, shade, sips.", 96)])
node(94, "Sami wakes, weak but calmer to see your face.", [
    c("Get the child cool.", 93),
    c("Break out the water.", 95)])
node(95, "The water crate does it: steady sips, wet cloths, the fever-heat easing.", [
    c("Hold through the worst.", 100),
    c("Help arrives.", 92)])
node(96, "No crate. You wet rags in your own last water, share the shade, keep the child talking.", [
    c("Hold through the worst.", 100),
    c("It may not be enough.", 97)])
node(97, "The heat is deep, and it may be more than rags can hold.", [
    c("Hold on to evening.", 100),
    c("Send for the rallied help.", 12)])
node(98, "Far off across the flats, a thread of smoke and a turning windmill.", [
    c("See to Sami first.", 93),
    c("The smoke nags at you.", 99)])
node(99, "The smoke, rising where everyone swears no one lives.", [
    c("Sami first.", 94),
    c("Hold through the worst.", 100)])
node(100, "The long hold: you keep the child cool, keep the water going round, wait out the sun.", [
    c("Watch for the sun to drop.", 101),
    c("The smoke still nags.", 70),
    c("The afternoon's worst hour.", 102)])
node(101, "The glare softens. The sun tips west. Dust rises on the road — a truck, at last.", [
    c("The cool of evening, and what it finds.", 110),
    c("Evening over the flats.", 105)])
node(102, "The worst hour, before the heat breaks.", [
    c("Watch for the sun to drop.", 101),
    c("Others' vehicles far down the road.", 103)])
node(103, "Down the road, dust and glints — others got through too.", [
    c("The cool of evening.", 110),
    c("The lights of the coming truck.", 104)])
node(104, "Headlights and a plume of dust climb toward you at last.", [
    c("The cool of evening.", 110),
    c("What the afternoon came to.", 114)])
node(105, "Evening over the flats, gold and clean, the heat lifting.", [
    c("The cool of evening.", 110),
    c("Help reaches the bus.", 92),
    c("The first cool breath of wind.", 106)])
node(106, "The first cool breath of wind, unbelievable after the day.", [
    c("The cool of evening.", 110),
    c("Help reaches the bus.", 92)])
node(107, "From the bus, far off on the road, a rising plume of dust.", [
    c("To Sami.", 93),
    c("Hold through the worst.", 100)])

# ===== CLOSING HUBS =====
node(110, "The cool of evening: what the afternoon comes to.", [
    c("Sami is safe; you kept the water going.", 120, req="has_water"),
    c("You found the smoke, and saved Faro.", 121, req="found_well"),
    c("Weigh the rest.", 111)])
node(111, "The afternoon adds up.", [
    c("The whole bus came through together.", 122, req="rallied_bus"),
    c("You did it clean — no con.", 123, req="dodged_seller"),
    c("Weigh the rest.", 112)])
node(112, "What else the afternoon held.", [
    c("A stranger you helped carries you on.", 124, req="helped_stranger"),
    c("You gave your own water away.", 125, req="gave_water"),
    c("Weigh the rest.", 113)])
node(113, "What the afternoon leaves you.", [
    c("A truck comes at last, late.", 126),
    c("The bus saw you get up and act.", 127),
    c("The worst of it.", 114)])
node(114, "The hard end of the afternoon.", [
    c("You paid the pickup man — fleeced.", 128, req="paid_seller"),
    c("You were simply too late.", 130),
    c("A truck came before real harm.", 126)])

# ===== ENDINGS (12: 4 good / 4 neutral / 4 bad) =====
end(120, "GOOD — Everyone drinks. You kept the bus watered and shaded through the worst of the heat; the sun drops, a truck finds you, and Sami reaches the city safe. The child is alive because you got up out of your seat.", "good")
end(121, "GOOD — The well that wasn't dry (secret). You crossed to the smoke no one could explain, found Mr Faro fallen in the heat, and got him cool in time — and his deep well and old radio saved the whole bus, with a quiet grace note: an old friend, recognised after all these years.", "good")
end(122, "GOOD — All of us in the shade. No single heroic move — but you turned a busload of frightened strangers into people sharing water and shade and watching the weak, and everyone came through the afternoon together.", "good")
end(123, "GOOD — You did what you could. You refused the con, kept your head and your money, and got water by decent means. Not perfect. But clean, honest, and enough.", "good")
end(124, "NEUTRAL — The kindness returned. You fell short of the whole afternoon's goal, but the stranger you stopped for comes back with a vehicle and carries you and Sami to town. Rescue without the full win.", "neutral")
end(125, "NEUTRAL — Shared your last mouthful. You gave your own water away and end the day parched yourself, but not alone — and something on that bus has shifted. A start, not a save.", "neutral")
end(126, "NEUTRAL — One more mile. You scrape through the worst of it; a truck finally comes, late and grudging. Not triumphant — just, in the end, relieved.", "neutral")
end(127, "NEUTRAL — The road remembers. You didn't manage everything, but the bus saw you get up and act when others sat still. You are, from today, someone this road knows.", "neutral")
end(128, "BAD — Robbed on the road. You paid the pickup man for water that's warm and half-gone and a lift that never comes back. The money's gone, and the thirst is exactly where it was.", "bad")
end(129, "BAD — The flats went on forever. The open ground was a trap; the heat and the distance nearly take you, and they take the afternoon — you get back too late, if you get back at all.", "bad")
end(130, "BAD — Too late in the heat. You spent the afternoon on the wrong things, and Sami goes down in the heat; by evening the child is being carried, limp and grey, to a waiting truck.", "bad")
end(131, "BAD — You kept your bottle capped. You stayed in your seat and kept your own water and never got up. Nothing bad happened to you. You will think about it for a long time.", "bad")

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
    "series": "cool-of-evening",
    "episode": 4,
    "title": "The Cool of Evening",
    "slug": "cool-of-evening",
    "blurb": "A cheap bus dies at noon on an empty desert road, hours from anywhere. A child travelling alone is failing in the heat, and no help will come until the sun drops. You have the long afternoon to keep them — and a busload of strangers — watered, shaded and alive.",
    "identity": {
        "name": "High Noon",
        "mood": "A desert road at the hottest hour; the only mercy is the water and shade people share.",
        "palette": {
            "ground": "#E7DBC0", "surface": "#F5EEDC", "ink": "#2C2417",
            "muted": "#8B7B5E", "line": "#D8C7A2",
            "accent": "#0E7C7B", "accentHot": "#3FA9A2", "secondary": "#C77A1E"
        },
        "cover": {"kind": "highsun", "glow": True},
        "type": {"display": "Fraunces", "ui": "Hanken Grotesk", "mono": "JetBrains Mono"},
        "hero": {
            "line": {
                "en": "The bus dies in the heat. A child aboard needs the water and shade you can find.",
                "fr": "Le bus tombe en panne dans la chaleur. À bord, un enfant a besoin de l'eau et de l'ombre que vous trouverez.",
                "es": "El autobús se avería con el calor. A bordo, un niño necesita el agua y la sombra que puedas encontrar.",
                "it": "L'autobus si ferma nella calura. A bordo, un bambino ha bisogno dell'acqua e dell'ombra che riuscirai a trovare.",
                "de": "Der Bus bleibt in der Hitze liegen. An Bord braucht ein Kind das Wasser und den Schatten, die du findest.",
                "pt": "O autocarro avaria no calor. A bordo, uma criança precisa da água e da sombra que conseguires encontrar.",
                "ru": "Автобус глохнет на жаре. В салоне ребёнку нужны вода и тень, которые ты сможешь найти.",
                "zh": "大巴在烈日下抛锚了。车上有个孩子，需要你去找来的水和阴凉。",
                "ar": "تتعطّل الحافلة في الحرّ. على متنها طفل يحتاج إلى ما تجده من ماءٍ وظلّ."
            },
            "sub": "A story where you are the hero — and every choice turns you to a new page. Written for people learning English, at your level, with meaning in your language whenever you need it."
        }
    },
    "levels": ["A2", "B1", "B2"],
    "start": 1,
    "language_focus": {
        "A2": ["imperatives and going to", "the body, heat and water"],
        "B1": ["the first conditional and modals of advice", "warning, sharing and planning"],
        "B2": ["inference, obligation and conditionals", "strangers, risk and responsibility"]
    },
    "state_in": STATE_IN,
    "state_out": STATE_OUT,
    "arc_flags": ARC_FLAGS,
    "nodes": nodes,
    "lexicon": {
        "_comment": "The Cool of Evening's chosen lexicon. Grown in phase 4. Base-keyed; the reader resolves inflections. Translations need a native speaker's check before launch.",
        "entries": {}
    }
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(book, open(OUT, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(f"Wrote {OUT}: {len(nodes)} nodes, {sum(1 for n in nodes if n.get('ending'))} endings.")
