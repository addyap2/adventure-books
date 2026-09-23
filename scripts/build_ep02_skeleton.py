#!/usr/bin/env python3
"""Phase 2: build the graph skeleton for book 2, 'The Room' (episode 2).

The machine before the prose. Every node is id + choices + gotos + flags + ending
markers, with one-line stub text per level (identical across A2/B1/B2 for now — prose
phase replaces it). Emits content/episode-02.json. Run the validator on the output;
it must come back with 0 errors before any real prose is written.

Run: python3 scripts/build_ep02_skeleton.py
"""
import json, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "content", "episode-02.json")

# ---- flags -----------------------------------------------------------------
# carried in from book 1
STATE_IN = ["dodged_scam", "told_truth", "knows_name"]
# book 2's own eight, each set somewhere and read somewhere (see design §4)
OWN = ["kept_money", "dodged_letting_scam", "paid_letting_scam", "has_reference",
       "found_keepsake", "helped_neighbour", "rushed", "warm_welcome"]
STATE_OUT = OWN[:]
ARC_FLAGS = ["dodged_letting_scam", "warm_welcome", "found_keepsake"]

# ---- the graph -------------------------------------------------------------
# node: (id, stub, [ (choice_stub, goto, sets|None, requires|None), ... ])
# ending: (id, stub, valence)
N = []
def node(i, stub, choices): N.append({"id": i, "stub": stub, "choices": choices})
def end(i, stub, val): N.append({"id": i, "stub": stub, "ending": val})
def c(t, g, sets=None, req=None):
    d = {"t": t, "goto": g}
    if sets: d["sets"] = sets if isinstance(sets, list) else [sets]
    if req: d["requires"] = req if isinstance(req, list) else [req]
    return d

# === ACT I — MORNING ========================================================
node(1, "Dawn in the cheap hotel; a note under the door: the room is booked from tonight. In your pocket, one week's pay — a deposit and nothing spare.", [
    c("Ask the hotel man where a stranger looks for a room.", 2),
    c("Go to the corner kiosk for the local paper.", 3),
    c("Check the room listings on your phone.", 4),
])
node(2, "The hotel man, who let you sit by the radiator once, warns you off the flashy agents and says: the paper, or the canal side, is where the cheap real rooms are.", [
    c("Count exactly what you have before you spend a coin.", 10),
    c("Head to the kiosk for the paper he means.", 3),
    c("Look at your phone anyway.", 4),
])
node(3, "The kiosk woman from your first night is at her corner. She hands you the paper and circles two ads; over a third — 'KEYS TODAY' — she draws a line.", [
    c("Read the two rooms she circled.", 7),
    c("Dania from the firm is here too, also looking.", 5),
    c("Walk to the canal side to look before the crowds.", 6),
])
node(4, "Your phone: a bright, cheap room, photos too good for the price. 'Mr Vann — deposit today to hold it, keys today.'", [
    c("Go to Vann's office and see the room.", 8),
    c("Look Vann up before you go anywhere.", 9),
    c("You have met this trick before. Ignore it.", 11, req="dodged_scam"),
])
node(5, "Dania, a new hire at Kessler and Rowe, is as new to the city as you and just as roomless.", [
    c("Agree to look together — two sets of eyes.", 27),
    c("Wish her luck and look on your own.", 7),
    c("Check your phone listings first.", 4),
])
node(6, "The canal in grey morning light: an old rope-works, washing on a line, a smell of tar and cold water.", [
    c("Decide how to spend the day and the fare money.", 12),
    c("A delivery man here seems to know every door.", 13),
])
node(7, "The two ads: a room by the canal (a Mrs Halloran, viewing at noon) and a cheap bedsit you could see right now.", [
    c("The bedsit — see it now while it's going.", 14),
    c("Hold out for the canal room at noon.", 15),
    c("A third ad: a room to share, very cheap.", 36),
    c("Work out your money and route first.", 12),
])
node(8, "You stand at the door of Vann's office. A queue inside; a board of glossy rooms.", [
    c("Step inside and hear the pitch.", 40),
    c("Hesitate on the step.", 9),
])
node(9, "You look Vann up. A man leaving the office mutters that he never got his keys; the reviews are a wall of one stars.", [
    c("Ask around a little more.", 16),
    c("Decide it's a trap and walk away.", 17),
    c("The room looked so good — risk it anyway.", 8),
])
node(10, "On the bed you lay the money out. One week. A deposit is most of it. A wrong move today and you have neither room nor fare.", [
    c("Go out and look, carefully.", 6),
    c("Get the paper first.", 3),
])
node(11, "You know this game now. You put the phone away and trust the paper and your feet.", [
    c("Read the paper's real ads.", 7),
    c("Walk to the canal side.", 6),
])
node(12, "How you cross the city is how your money lasts.", [
    c("Walk everywhere and keep the fare.", 18, sets="kept_money"),
    c("Take the bus so you can see more rooms.", 19),
    c("Go back for the paper first.", 3),
])
node(13, "The delivery man leans on his trolley. 'Halloran's? Over the rope-works. Good stair. Ask for the room at the top.'", [
    c("Thank him and note the stair.", 20),
    c("Catch the bus into the centre first.", 19),
])
node(14, "The bedsit's address is close; you could be there in ten minutes.", [
    c("Go straight up to see it.", 30),
    c("Read the canal ad once more first.", 7),
])
node(15, "The canal viewing is at noon. Hours to fill, and a whole city between.", [
    c("Set off for the canal early.", 50),
    c("Kill the time in the market square.", 25),
])
node(16, "You ask the kiosk woman about Vann. Her face closes. 'That one. Keep your money in your pocket.'", [
    c("Take her word and leave it.", 17),
    c("Head into the square to think.", 25),
])
node(17, "You cross Vann off. It stings a little; the photos were lovely. But lovely and cheap and today is the whole trick.", [
    c("Back to the paper's real rooms.", 7),
    c("Into the square.", 25),
])
node(18, "Walking, you reach the market square by midday, feet already sore but the fare still in your pocket.", [
    c("Into the square to choose a direction.", 25),
    c("Straight on to the canal.", 50),
    c("The square clock says the morning's gone.", 26),
])
node(19, "The bus sets you down at the square. Faster, but the coins are fewer now.", [
    c("Into the square.", 25),
    c("On to the canal.", 50),
])
node(20, "The delivery man points you to Halloran's stair, then rattles off toward the centre.", [
    c("Go up to the canal building.", 50),
    c("Fill the time in the square first.", 25),
])
node(25, "The market square: Vann's office on one side, the canal lane on the other, and Dania waving from a stall.", [
    c("Vann's office.", 40),
    c("The canal room.", 50),
    c("Go with Dania.", 27),
    c("The bedsit first.", 21),
])
node(26, "The square clock strikes noon. Half your daylight is spent and you have seen nothing yet.", [
    c("Choose a direction and move.", 25),
    c("Vann's office, quickly.", 40),
])
node(27, "Dania is wary of Vann too. You compare your two ads on a bench.", [
    c("View the canal room together.", 28),
    c("Split up to cover more ground.", 29),
    c("Both try the agent, to be sure.", 40),
])
node(28, "With Dania beside you, the day feels less thin.", [
    c("Go to the canal room together.", 50),
    c("Try the bedsit together first.", 30),
    c("She wants to see one more first.", 90),
])
node(29, "Alone again, you keep your own counsel.", [
    c("The canal room.", 50),
    c("Vann's office.", 40),
    c("The bedsit.", 30),
])
node(36, "The 'room to share' ad is far out, but the price is barely half the rest.", [
    c("Make the trip to see it.", 37),
    c("Too far — back to the real ads.", 7),
])
node(37, "You get there. The share was taken this morning; the door is already someone else's.", [
    c("Nothing here. Move on.", 38),
    c("Ask if they know of anything else going.", 25),
])
node(38, "You are further out than you meant to be, and the daylight is shorter for it.", [
    c("Back toward the square.", 25),
    c("It's getting late — think about the evening.", 96),
])

# === ACT II — VIEWINGS: THE AGENT (the scam) ================================
node(40, "Vann's office. A queue of tired hopefuls. Vann himself is all warmth and hurry.", [
    c("Listen to the pitch.", 41),
    c("Talk to the people in the queue.", 42),
])
node(41, "The pitch is perfect: the very room from the photos, cheap, yours — if you leave a deposit today to hold it.", [
    c("Ask to see the room before you pay.", 43),
    c("Pay the deposit now, before it's gone.", 44),
    c("Say you'll think about it, and leave.", 45),
])
node(42, "In the queue, a woman whispers she's been 'holding' a room for a week. A man says Vann found his cousin a flat, no trouble.", [
    c("Ask to see the room first.", 43),
    c("Leave; you've heard enough.", 45),
    c("Hear the woman's story out.", 65),
])
node(43, "You ask to see it first. Vann's smile holds but his eyes flick to the clock. 'It'll be gone by five. The deposit only holds it.'", [
    c("Better safe — pay to hold it.", 44),
    c("Refuse the 'hold' and insist on seeing it.", 46, sets="dodged_letting_scam"),
    c("Walk. He never once said the address.", 47, sets="dodged_letting_scam", req="dodged_scam"),
])
node(44, "You hand over the deposit. A receipt, a firm handshake, 'keys tomorrow, come at nine.'", [
    c("Pocket the receipt and go.", 48, sets="paid_letting_scam"),
    c("Head out, already uneasy.", 96, sets="paid_letting_scam"),
])
node(45, "You leave without paying. Behind you the queue shuffles up one place.", [
    c("On to a real room.", 49),
    c("Back to the square.", 25),
])
node(46, "You refuse the hold and ask, plainly, for the address so you can see it. Vann's warmth cools. He hasn't got one to give.", [
    c("Out the door, money intact.", 49),
    c("Straight to the canal instead.", 50),
])
node(47, "You just walk. On the step you realise: in ten minutes of talk, he never once named a street.", [
    c("Note it and move on.", 49),
    c("On to the canal.", 50),
])
node(48, "Out on the street with a receipt and no keys, the morning gone, a small cold doubt starting.", [
    c("On to see a real room too.", 50),
    c("Read the receipt again.", 117),
    c("Think about the evening.", 96),
])
node(117, "You read Vann's receipt again: a company you can't find online, a number that rings and rings. The cold doubt hardens into something like knowledge.", [
    c("Try to salvage the day.", 50),
    c("Face the evening with it.", 96),
])
node(49, "Out of Vann's, purse still full, but the clock is unkind. Canal or bedsit left.", [
    c("The canal room.", 50),
    c("The bedsit.", 21),
    c("Leaving, the queue is longer than before.", 68),
])
node(65, "The woman's story: a deposit paid, a date given, then another, then Vann 'so sorry, it fell through' — and no money back.", [
    c("Thank her and refuse to pay.", 45),
    c("Vann leans in with one last push.", 66),
])
node(66, "'Last one at this price,' Vann says, hand out. 'People like you don't get second chances in this city.'", [
    c("Pay, against your better sense.", 44),
    c("That line is the tell. Leave.", 45),
])
node(68, "Behind you the queue has doubled; the same warmth, the same clock, the same hand out.", [
    c("On to a real room.", 50),
    c("Think about the evening.", 96),
])

# === ACT II — VIEWINGS: THE BEDSIT ==========================================
node(21, "The bedsit building: a damp stair, a smell of old cooking, a landlord jingling keys.", [
    c("Go up to the room.", 30),
    c("Back to the square; something's off.", 25),
])
node(30, "The room is small and grey and cheap. The landlord wants cash now, asks nothing, offers nothing.", [
    c("Take it on the spot — a room is a room.", 31, sets="rushed"),
    c("Say you'll think about it.", 32),
    c("Ask to look at it properly first.", 34),
    c("Ask why it's empty; his face hardens.", 35),
])
node(31, "You give him a cash 'hold' and it is, in a way, yours. You didn't really look. You were just tired of looking.", [
    c("It's done. Move on.", 33),
    c("A second thought, too late.", 32),
])
node(32, "You tell him you'll think. He shrugs; there's always someone.", [
    c("Out to look properly.", 34),
    c("On to the canal room.", 50),
])
node(33, "You have a room, of sorts. Grey walls, a shared bathroom, a key that's yours.", [
    c("Carry on with the day anyway.", 96),
    c("Wonder if you rushed it.", 34),
])
node(34, "You back out to keep looking. The bedsit will keep; grim rooms always do.", [
    c("On to the canal room.", 50),
    c("Weigh it against the evening.", 96),
    c("The shared bathroom decides it — no.", 39),
])
node(35, "You ask why it's stood empty. The landlord bristles: 'You want it or not?' No lease, no questions, no answers.", [
    c("Say you'll think about it.", 32),
    c("Back out.", 34),
])
node(39, "One cold shared bathroom off the stair, a queue of doors. A room, but never a home.", [
    c("On to the canal room.", 50),
    c("Think about the evening.", 96),
])

# === ACT II — VIEWINGS: THE CANAL ROOM & THE MYSTERY ========================
node(50, "Halloran's building over the rope-works. A steep clean stair; at the top, an open door and a woman waiting.", [
    c("Go up for the viewing.", 51),
    c("You're early — wait in the square.", 25),
])
node(51, "Mrs Halloran is brisk and grey-eyed. The room has good light — and someone's things, half-packed: a coat, a tin of buttons, a box by the wall.", [
    c("Ask about the last tenant.", 52),
    c("Look at the room itself first.", 53),
])
node(52, "'He's gone. That's all,' she says, and busies herself with the window catch.", [
    c("Let it go; ask about terms.", 54),
    c("Look more closely at what he left.", 55),
])
node(53, "Good light off the water; a coat still on the hook; the tin of buttons on the sill. Someone lived here, and lately.", [
    c("Notice the things he left.", 55),
    c("Ask Halloran what happened here.", 80),
    c("Picture yourself living here.", 84),
])
node(54, "Terms: the rent is fair, the deposit steep, and references — 'people who'll say you're sound' — required.", [
    c("Face the references problem.", 56),
    c("Look around once more as she talks.", 53),
])
node(55, "Among his things, a notebook lies open on the sill — pages of names and addresses in a careful hand.", [
    c("Pick it up to return to him.", 57, sets="found_keepsake"),
    c("Leave it; not your business.", 58),
    c("Ask Halloran about it.", 80),
])
node(56, "References. You know no one in this city who could vouch that you're sound. You've been here three days.", [
    c("She names her condition — unless.", 59),
    c("She softens a little as you take it in.", 60),
])
node(57, "You slip the notebook into your bag to give back. It feels less like taking and more like keeping safe.", [
    c("Turn back to Halloran.", 60),
    c("Ask her about it, holding it.", 80),
])
node(58, "You put the notebook down where it lay. Whatever it is, it isn't yours.", [
    c("Turn back to Halloran.", 60),
    c("Ask about him instead.", 52),
])
node(59, "'No references, no room,' she says. 'Unless you give me a reason to trust my own eyes.'", [
    c("Mention Kessler and Rowe.", 61),
    c("Just be honest about who you are.", 62),
])
node(60, "She watches how you move through the room — carefully, as if it were already someone's home. Something in her eases.", [
    c("Mention your job at the firm.", 61),
    c("Be honest: new here, no one, need a chance.", 62),
])
node(61, "You mention Kessler and Rowe. Her eyebrows lift. 'Rowe. I know that name. If she'd say a word for you...'", [
    c("A reference from the firm — how?", 70),
    c("Say you'll be honest instead.", 62),
])
node(62, "You tell her the plain truth: three days in the city, no one to vouch for you, a week's pay, and today to find a home.", [
    c("She says: come back at dusk.", 63),
    c("She studies you a moment longer.", 60),
])
node(63, "'Come back when the light goes,' she says. 'I'll have thought.' On the stair, a neighbour is wrestling shopping and a child.", [
    c("Fill the hours till dusk.", 64),
    c("Help the neighbour on the stair.", 76),
])
node(64, "Hours to kill before dusk, and a whole city that still doesn't know you.", [
    c("Back to the square.", 25),
    c("Think ahead to the evening.", 96),
    c("Count what the day has cost.", 99),
])
node(80, "You ask Halloran outright what happened here. She stiffens, straightens the coat on its hook, and changes the subject.", [
    c("Press gently.", 81),
    c("Let it drop.", 60),
])
node(81, "On the stair a neighbour murmurs: 'The lad up top? Went to sea. Sudden. She won't speak of it.'", [
    c("Ask the neighbour more.", 82),
    c("Leave it and help the neighbour instead.", 76),
    c("Back to Halloran and the room.", 60),
])
node(82, "'Owed nothing, harmed no one,' the neighbour says. 'Just gone one morning. It's her boy, see. She won't say.'", [
    c("Her boy. You understand the packed box now.", 83),
    c("Enough — help with the shopping.", 76),
])
node(83, "Her son. The half-packed room, the coat she won't move, the notebook of addresses he meant to write to.", [
    c("Take the notebook to return it.", 57, sets="found_keepsake"),
    c("Say nothing; go back down.", 60),
])
node(84, "At the window you can see yourself here: the water, the light, a kettle, a life. It's the first room that felt like one.", [
    c("Look at what he left behind.", 85),
    c("Turn back before you hope too hard.", 55),
])
node(85, "In the coat pocket, a photograph: the same window, a young man, and Halloran, younger, laughing.", [
    c("You understand who lived here.", 86),
    c("Put it back exactly as it was.", 55),
])
node(86, "Someone lived here and left fast, and the woman letting the room is not a stranger to him at all.", [
    c("Take the notebook to give back.", 57, sets="found_keepsake"),
    c("Say nothing yet.", 60),
])

# === ACT II — THE GUARANTOR FLAT & THE REFERENCE ============================
node(70, "There is a better flat across town — but it needs a guarantor, someone to stand behind your rent. You have none. Unless the firm will.", [
    c("Think how to get the firm's word.", 71),
    c("Give up on the good flat.", 74),
])
node(71, "You could ask. It's your first week; it's a lot to ask. But you did tell Ms Rowe everything, once.", [
    c("Call Ms Rowe, who trusts you.", 72, sets="has_reference", req="told_truth"),
    c("Ask a colleague at the firm instead.", 73, sets="has_reference"),
    c("It's too much to ask. Let it go.", 74),
])
node(72, "Ms Rowe listens, then: 'Of course. Put them onto me.' Because you were straight with her once, she is straight with you now.", [
    c("A reference — you have one.", 75),
    c("Thank her and get on with the day.", 96),
])
node(73, "A colleague hesitates — you're new — then agrees to say you're sound. Not warm, but enough.", [
    c("A reference, of a kind.", 75),
    c("On with the day.", 96),
])
node(74, "You let the good flat go. You can't ask the firm for your name in your first week.", [
    c("Back to the day's real chances.", 96),
    c("Into the square to think.", 25),
])
node(75, "You have a reference now — a name that will answer for you. It changes what doors will open.", [
    c("Carry it to the evening.", 96),
    c("Into the square first.", 25),
])

# === ACT II — THE NEIGHBOUR =================================================
node(76, "The neighbour: bags splitting, a small child on the step, three floors to climb.", [
    c("Take the bags and help up.", 77, sets="helped_neighbour"),
    c("You're in a hurry — pass by.", 78),
    c("Mind the child while she manages the bags.", 92),
])
node(77, "You carry the shopping up. She's breathless with thanks and insists you'll be repaid one day.", [
    c("Wave it off; back to the day.", 79),
    c("She points you back toward Halloran.", 63),
])
node(78, "You pass by with a nod. Not unkind, just busy. The stair swallows the sound of her struggling on.", [
    c("Back to the day.", 79),
    c("Into the square.", 25),
])
node(79, "Back to the day, the small warmth or small guilt of it going with you.", [
    c("Think toward the evening.", 96),
    c("Back to Halloran's block at dusk.", 64),
])
node(92, "The child holds your hand solemnly while the mother hauls the bags. A tiny trust, freely given.", [
    c("See them both safely up.", 77, sets="helped_neighbour"),
    c("Hand the child back and hurry on.", 78),
])
node(90, "Dania wants to see a place round the corner first. You go with her.", [
    c("On to the canal room after.", 50),
    c("She's found something; you're still looking.", 91),
])
node(91, "Dania takes a small room she likes and hugs you goodbye. You're glad for her, and more alone.", [
    c("Back to the square.", 25),
    c("On to the evening.", 96),
    c("She texts you a listing to try.", 118),
])
node(118, "Dania's text: a room near hers, going tonight. Kind of her. Probably gone already.", [
    c("Think toward the evening.", 96),
    c("Back to the square to chase it.", 25),
])

# === ACT III — THE DECISION (dusk) ==========================================
node(99, "You add the day up on a bench: the fare, the wasted trip, the rooms seen, the one that felt like a home.", [
    c("Decide where to go as the light goes.", 96),
    c("None of it's enough — think harder.", 98),
    c("The stalls are closing around you.", 115),
])
node(96, "Dusk. The hotel wants its room tonight. You have one evening and whatever the day has left you.", [
    c("Back to Mrs Halloran's.", 100),
    c("Claim the good flat.", 101, req="has_reference"),
    c("Weigh the other options.", 97),
])
node(97, "The light is nearly gone. What's actually within your reach tonight?", [
    c("Go for the agent's keys.", 102, req="paid_letting_scam"),
    c("Sign for the bedsit.", 103, req="rushed"),
    c("One last phone check.", 114),
    c("None of these — think again.", 98),
])
node(98, "Nothing has quite worked. The hotel closes to you at ten.", [
    c("Ask the neighbour you helped.", 113, req="helped_neighbour"),
    c("Try the landlady who remembered your name.", 126, req="knows_name"),
    c("Accept the rooms are gone for today.", 130),
    c("Wonder if this city will ever have you.", 131),
])
node(114, "A last scroll: the good listings are all marked LET now. Only Vann's kind are still bright and still lying.", [
    c("Back to thinking it through.", 98),
    c("It really is too late.", 130),
])
node(115, "The market folds up around you — shutters, crates, the smell of the day ending.", [
    c("Go where the evening leads.", 96),
    c("Sit, and let the city win a moment.", 131),
    c("One last idea.", 119),
])
node(119, "The last of the light on the wet square. Somewhere a door is warm; the question is whether one is warm for you.", [
    c("Try the last real chance.", 98),
    c("Give the day up.", 131),
])
node(100, "Halloran's stair again, the light in her window just come on. You climb.", [
    c("She opens the door.", 104),
    c("Give back his notebook first.", 111, req="found_keepsake"),
    c("The walk up feels longer at dusk.", 110),
])
node(110, "The canal is black glass; the rope-works quiet; her window the one warm square in the dark.", [
    c("Go up and knock.", 104),
    c("Her stair light comes on above.", 116),
    c("Lose your nerve; think again.", 96),
])
node(116, "A light climbs the stair to meet you. She heard you coming.", [
    c("Meet her at the door.", 104),
    c("Back down a step, and up again.", 100),
])
node(104, "Mrs Halloran in the doorway, the warm room behind her, the deposit money warm in your hand.", [
    c("Talk terms.", 105),
    c("Step back onto the stair a moment.", 100),
])
node(105, "She waits. This is the moment the whole day was walking toward.", [
    c("Tell her the truth of your circumstances.", 106),
    c("Keep it businesslike; just the rent.", 107),
])
node(106, "You tell her plainly: new, alone, a week's pay, no one to vouch — but honest, and you'll mind the place. Her grey eyes hold yours.", [
    c("She decides.", 108, sets="warm_welcome"),
    c("On second thought, retreat to business.", 107),
])
node(107, "You keep it to rent and dates and deposits. Correct. Cool. She nods along, and something doesn't quite open.", [
    c("She weighs it.", 109),
    c("Change tack; be honest after all.", 106),
])
node(108, "She looks at you a long moment, then at the packed box she cannot bring herself to move.", [
    c("She gives you the room.", 120, req="warm_welcome"),
    c("It doesn't quite land; back to the hotel.", 127),
])
node(109, "She weighs you like a form to be processed: money present, references absent.", [
    c("You cover it cleanly, by your own careful means.", 122, req=["kept_money", "dodged_letting_scam"]),
    c("No money kept, no one to vouch — a polite no.", 129),
])
node(111, "On the step you hold out the notebook. 'This was up there. I think it's his.' The colour leaves her face.", [
    c("She takes it, and everything changes.", 121, req="found_keepsake"),
    c("Then talk about the room.", 104),
])
node(101, "The good flat, clean and bright, and a letting man who only wants your reference to be real.", [
    c("Take it; you're vouched for.", 123),
    c("Hesitate — it's more than you can hold.", 127),
])
node(102, "Vann's 'address' at last — a slip of paper, a street you don't know, a key that's cold in your hand.", [
    c("Go and let yourself in.", 112),
    c("Hesitate on the dark street.", 130),
])
node(112, "The street is a car park behind a hoarding. The key fits no door because there is no door. There never was a room.", [
    c("The deposit is gone.", 128),
    c("Back to argue — but the office is dark.", 130),
])
node(103, "The bedsit landlord counts your cash again and pushes a scrap of paper across for your name.", [
    c("Sign; it's yours tonight.", 124),
    c("Back out at the last second.", 127),
])
node(113, "The neighbour you helped opens her door, the child behind her knees. 'You carried my bags. There's a box room. It's yours till you're sorted.'", [
    c("Take the box room, gratefully.", 125, req="helped_neighbour"),
    c("Thank her, but keep looking.", 127),
])

# === ENDINGS (12: 4 good / 4 neutral / 4 bad) ===============================
end(120, "GOOD — A home, honestly. She gives you the room on trust, because you were straight about having no one. The first job at the firm was fixing the letters; the first thing you fix here is the window catch. It is a home.", "good")
end(121, "GOOD — The room returned (secret). She takes the notebook, sits down hard on the packed box, and tells you about her son gone to sea. You gave her back a piece of him. The room is yours; so, now, is a place at her table.", "good")
end(122, "GOOD — On your own terms. No favours, no con, no one vouching — just a modest real room secured by your own careful means. Bare walls, a borrowed chair, a key you earned. Yours, and only yours.", "good")
end(123, "GOOD — Vouched for. Ms Rowe's word unlocks the good flat. You are new here, but you are known — and being known, you are beginning to learn, is how a stranger becomes a resident.", "good")
end(124, "NEUTRAL — A room, not a home. You took the first thing, sight barely seen. It is yours, it is fine, it is grey and empty and quiet. A technical win. You lie on the bed and feel, exactly, nothing.", "neutral")
end(125, "NEUTRAL — The kindness returned. No room of your own tonight, but the neighbour's box room and the child's shy hello. Warmth without the win — and warmth, tonight, is not nothing.", "neutral")
end(126, "NEUTRAL — Remembered. No room today, but a landlady who kept your name says, come back Monday. You are becoming someone the city recognises. That is a kind of address.", "neutral")
end(127, "NEUTRAL — Back to the hotel, one more week. Nothing signed, but you have the city's map now and its prices in your head. You buy one more week and set the alarm. Not a loss — just not yet.", "neutral")
end(128, "BAD — The deposit gone. The room was never his to let. Your deposit — most of a week's pay — is gone, and the hotel wants its key by ten. You knew the tune and danced anyway.", "bad")
end(129, "BAD — No one to vouch. No money kept, no reference, nothing to set against a stranger's face. Every good door was a polite no, and the day has simply run out.", "bad")
end(130, "BAD — Too late to look. You spent the daylight on the wrong lead, and by dark the real rooms are all taken. The city didn't cheat you; you just ran out of light.", "bad")
end(131, "BAD — You think about leaving. No room, no welcome, and the old thought again: a two-o'clock train, a way back to where they know you. You don't buy the ticket. But tonight, you think about it.", "bad")

# ---- assemble --------------------------------------------------------------
def leveled(s):
    return {"A2": s, "B1": s, "B2": s}

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
    "series": "new-city",
    "episode": 2,
    "title": "The Room",
    "slug": "the-room",
    "blurb": "You have the job. Now you have one grey Saturday, and a week's pay you can't afford to lose, to find somewhere to live in a city that still doesn't know you.",
    "identity": {
        "name": "Rope-Works Winter",
        "mood": "A cold bright city by day; one lit doorway with a warm room behind it.",
        "palette": {
            "ground": "#0C1118", "surface": "#141b26", "ink": "#F3EFE7",
            "muted": "#8992A1", "line": "#242f40",
            "accent": "#E8955A", "accentHot": "#F4B978", "secondary": "#7FC3A6"
        },
        "cover": {"kind": "daybreak", "glow": True},
        "type": {"display": "Fraunces", "ui": "Hanken Grotesk", "mono": "JetBrains Mono"},
        "hero": {
            "line": {
                "en": "You have the job. Now you need a room.",
                "fr": "Vous avez le travail. Il vous faut maintenant une chambre.",
                "es": "Ya tienes el trabajo. Ahora necesitas una habitación.",
                "it": "Hai il lavoro. Adesso ti serve una stanza.",
                "de": "Du hast die Stelle. Jetzt brauchst du ein Zimmer.",
                "pt": "Já tens o emprego. Agora precisas de um quarto.",
                "ru": "Работа есть. Теперь нужна комната.",
                "zh": "工作有了。现在你需要一个房间。",
                "ar": "حصلت على العمل. الآن تحتاج إلى غرفة."
            },
            "sub": "A story where you are the hero — and every choice turns you to a new page. Written for people learning English, at your level, with meaning in your language whenever you need it."
        }
    },
    "levels": ["A2", "B1", "B2"],
    "start": 1,
    "language_focus": {
        "A2": ["present simple, have/have got", "money, prices, rooms and furniture"],
        "B1": ["future forms and the first conditional", "renting, agreements, comparisons"],
        "B2": ["inference, conditionals and hedging", "trust, obligation and the housing market"]
    },
    "state_in": STATE_IN,
    "state_out": STATE_OUT,
    "arc_flags": ARC_FLAGS,
    "nodes": nodes,
    "lexicon": {
        "_comment": "Book 2's chosen lexicon. Grown in phase 4. Any word here is tappable wherever it appears (base form; the reader resolves inflections). Translations need a native speaker's check before launch.",
        "entries": {}
    }
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(book, open(OUT, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(f"Wrote {OUT}: {len(nodes)} nodes, "
      f"{sum(1 for n in nodes if n.get('ending'))} endings.")
