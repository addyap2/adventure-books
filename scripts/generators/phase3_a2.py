#!/usr/bin/env python3
"""Phase 3 — the A2 pass: simplify each new node's B1 into A2.

A2 keeps the same events and voice but in short, plain sentences (mean ≤ 12 words,
sentences ≤ 18). Choices, which are already short imperatives, take the B1 label at A2.
B2 stays ⟨pending⟩ for the enrich pass.
"""
import json, os

EP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "episode-01.json")
book = json.load(open(EP, encoding="utf-8"))

A2 = {
 41: "The doors close. The platform is empty now. A few people walk fast to the exit. One of them is young, with a big bag. They read a small piece of paper, then read it again. They look lost, like you.",
 42: "Her name is Mara. She was on your train. She is here for work too. She does not know the city. For a few minutes, you are not alone. Her address is across the river. Yours is a street she does not know.",
 43: "The man at the newsstand is old. He reads your letter twice. \"Rosewater Street,\" he says. \"You are the third this month. Someone still writes the old address on the letters.\" He gives the paper back.",
 44: "\"They moved to the river years ago,\" he says. \"New offices, all glass. But the letters still say Rosewater Street. Not my problem.\" He shrugs. It is someone's problem, you think. Maybe soon it will be yours.",
 45: "Half of Rosewater Street is behind builders' fences. On one, an old notice still has the firm's name. Under it, someone wrote one word in black pen, with an arrow to the east: MOVED.",
 46: "You almost miss it. There is a small side door behind the fence. A thin line of light is under it. Someone is inside, this late. You stand and look at that small yellow line.",
 47: "The door opens. A woman comes out and puts on her coat. She is tired, but kind. \"Nobody works here now,\" she says. \"They are by the river. If you can't wait, ask at the café on the corner.\"",
 48: "On the next bench a man sits. No bag, no coat, just a paper cup. He does not ask for anything. He missed the last train, like you. But he has done this many more nights than you have.",
 49: "You take a wrong turn, then another. The same closed shop goes past twice. The map means nothing now. The streets are very quiet. At one in the morning, the city belongs to no one.",
 50: "The light is a launderette, open all night. One man is inside, folding towels. He is happy to talk. He knows these streets well. He draws the way in the air with his hand.",
 51: "On a glass door at the back, a painted name is half gone. You can still read ROWE under the marks. Someone left in a hurry, or someone wanted it gone. In the dark, you can't tell.",
 52: "A window upstairs at number 16 is lit. A girl, about ten, watches you through the glass. She is calm. She knows strangers come at strange hours. She does not wave. She just looks, and waits.",
 53: "A night bus comes round the corner. Its windows are warm and yellow. It goes the way of the river, you think. It will not wait. You have a few seconds. Your feet are tired of choosing.",
 54: "A bridge crosses the black water. On the far side, new offices stand dark and clean, all glass. One window is lit, high up. You watch it from the bridge. It does not go out.",
 55: "A night watchman leans out of a warm hut. \"Kessler and Rowe? Second floor. But nobody's in till nine.\" He is kind. He points to the hut. \"Go on. Get out of the cold.\"",
 56: "The café is shut. But there is a light in the back, and someone moving chairs. The card is still in the window. You put your hands to the glass and wait for someone to see you.",
 57: "The woman opens the door a little. \"Kessler and Rowe? Ada Rowe, you mean. She's by the river now.\" She almost smiles. \"She comes here for coffee every morning. You won't miss her.\"",
 58: "The cleaner is kind about waking you. She pours you half a cup from a flask. \"Where have you come from?\" she asks. She is not really curious. She has asked this many times before.",
 59: "At breakfast, Mara is there too. She leans over the table. \"There's an agency across the road,\" she says quietly. \"They wanted money from me last night. Don't. Whatever they say, don't.\"",
 60: "A queue is already outside WORK FOR EVERYONE. Tired faces in the early light. You can see their breath. Near the front, a woman counts her last money, twice, as if it might change.",
 61: "The man in the good suit passes a form across. \"Two hundred to register, then we find you work today. Everyone pays.\" The small print is grey and tiny. He is already reaching for your money.",
 62: "Outside, a man leans on the wall. He has a receipt like the one you nearly had. \"I paid them last week,\" he says. \"They never called.\" He looks at you. \"You didn't, did you?\"",
 63: "On the desk there is a tray of old post. Each letter has the Rosewater address crossed out by hand. You look again. One of them is yours — the letter that brought you here, to the wrong door.",
 65: "The driver tells the story as he drives. \"They all moved to the river. Glass offices, very smart.\" He looks at you in the mirror. \"And watch the work agencies near the station. They are not what they seem.\"",
 67: "First light is grey over Mill Quay. A coffee cart is opening. Vans go by along the water. You are early, and you are clean. For the first time, you know where you are, and where to go.",
 68: "You watch the doors along the quay. Then you see him: the man in the good suit from the agency. He goes into a building two doors down. No sign, no name. The way he looks around first tells you everything.",
 69: "In your bag: the letter, a little money, and a photo you do not take out. You read the letter again. You know every word. It is as if the words might change while you sleep.",
 72: "Your phone has one bar of battery. One. You could look up the firm now. Or you could save it for something worse. At night, in a strange city, a dying phone is a kind of clock.",
 73: "An old page loads, slowly. The firm's address is not Rosewater Street. It is somewhere by the river. Then the screen goes black and stays black. You are alone again with a paper letter.",
 75: "Mara has more sense than money. You have a little more money than sense. Together, it might be enough to do this well. If not, you will both walk the wrong way half the night.",
 77: "A guard walks the hall, turning off lights. \"We're closing. You can't sit here.\" He is not unkind, just tired. Behind him the big hall goes dark, piece by piece. The cold comes in.",
 79: "From the bus window the city goes by, dark and wet and strange. You could get off early and walk. Or you could stay on to the right stop, and trust the driver to know the way.",
 84: "Reception is warm. It smells of coffee. The woman at the desk is kind. She looks at you a little too long. Last night is all over you — the creased coat, the tired eyes. She says nothing.",
 85: "Ms Rowe's office looks over the water. On the desk is a folder. On top of it is a letter you know. It is yours — sent to the wrong street, and back again. She sees you see it.",
 86: "\"Someone here posted the old address for two years,\" she says. She turns the letter over. \"You are not the first it sent the wrong way. You are the first to come anyway.\"",
 88: "She reaches the step with a coffee and keys. She sees you waiting. She is not surprised. \"You look like you've been up all night,\" she says, and unlocks the door. \"Come in, before we freeze.\"",
 89: "The quay is waking up: gulls on grey water, a coffee cart, vans on the stone. You have time, for once. Your hands are clean, for once. After such a night, it is strange to be early.",
 90: "The man in the good suit sees you looking. For a second, neither of you moves. Then he goes into the building with no name, and is gone. Now you know what kind of place you left.",
 91: "\"They wanted money from me too,\" the other person says quietly. \"To register, they said. I nearly paid.\" She shakes her head. So you are not the only one. That helps, a little.",
 92: "Through the window you see the bridge you crossed in the dark. The black water under it is grey now. It does not look far by daylight. Most things do not, you are learning.",
 94: "She calls a younger worker in. He goes red. \"The old letterhead,\" she says, kindly. \"We'll fix it.\" Then she looks at you. \"And you can help us fix it. You know the way better than we do.\"",
 95: "The kiosk woman calls after you. \"There's a back way into number 14, through the yard. The front door hasn't opened in years.\" She points with her chin and turns for home.",
 96: "In the yard, a low window is lit. Inside, on a desk, is a tray of envelopes, stamped and ready. You look closer, and go cold. Every one has the Rosewater Street address. To here. To no one.",
 97: "The upstairs window opens. The girl leans out. \"They're by the river now,\" she says, as if you should know. \"Ada Rowe. My dad worked for her, before all this.\"",
 98: "\"Three Mill Quay,\" she says, as if everyone knows. \"Take the number four in the morning. It stops outside.\" Then her father calls her in. The window shuts. The street is yours again.",
 99: "By the water, you lose the streets completely. But a boathouse has its lights on. You hear long oars carried down to the river, and low voices — people with somewhere to be.",
 100: "\"Mill Quay? Straight on, past the second bridge. Ten minutes.\" The rower does not stop, an oar on his shoulder. \"You're nearly there,\" he says, seeing your face. \"Nearly there now.\"",
 101: "The new building has a glass hall, lit and empty. A guard's cap sits on an empty desk. Everything here is two years newer than your letter. You stand outside in last night's clothes.",
 102: "You wait for the café to open. The sky goes from black to grey. Your feet have stopped hurting, which may be worse. At last a light comes on inside. A chair scrapes.",
 103: "An early customer looks up from his tea. \"Kessler and Rowe? I did their books, years ago. Good people.\" He laughs. \"Bad with letters, though. Always were. Ask anyone.\"",
 104: "The hotel man leans on the desk. \"A word of advice,\" he says. \"That agency, the yellow sign? Don't. They took a boy's last money on Tuesday. He's still in my lobby, too ashamed to go home.\"",
 105: "The first bus of the day comes to the stop, warm and almost empty. It goes to Rosewater, or you can change for the river. Either way, it moves. That is more than you have done all night.",
 106: "The address the agency gave you is an empty lot behind a fence. Weeds, a burnt mattress, nothing else. There was never a job. There was only the two hundred, and it is gone.",
 107: "A woman in the queue reads the form, folds it, and gives it back. \"It's a swindle,\" she says, loud. \"Come on. All of you.\" And a few of you, barely believing it, follow her out.",
 108: "The taxi goes through empty streets. Closed shops, one all-night café throwing yellow light on the wet road, a fox on a corner. The driver hums to the radio. For a few minutes, it is almost restful.",
 109: "The man at the desk draws you a better map on a receipt. He marks the river with a small square. \"That's where the smart ones went,\" he says, and pushes it under the glass. \"Off you go.\"",
 110: "You walk to the quay in the growing light. People go to work, sure of the way. For the first time, so are you. It changes how you walk, knowing where you go. You had forgotten that.",
 111: "The young woman from number 16 goes the same way. \"Number four,\" she says, at the bus. \"I'll show you where to get off.\" She says it easily, as if helping a stranger were nothing. Maybe here it is.",
 112: "You go to the office to explain, late and out of breath. On the stairs you practise the words. None sound right. All start with sorry. And you feel that sorry will not be enough today.",
 113: "The woman at the coffee cart looks at you and adds an extra shot, free. \"Long night,\" she says. It is not a question. You hold the hot cup in both hands. You feel it in your fingers first, then everywhere.",
 114: "You sit with the cold coffee and decide, at last, to trust the letter. Or at least the person who wrote it. Someone meant you to come. That must count for something. You fold the letter away and stand.",
 115: "You cross an empty market square. The stalls are folded away. Wet stones shine under one lamp. A fox trots along the gutter, as if it owns the hour. It looks at you once, then decides you are nothing to fear.",
 116: "A taxi waits at the kerb, its light on, the driver reading. It would cost more than you want to spend. But it would end the walking. And the walking has begun to feel like your whole life.",
 117: "The cleaner sighs and holds the door with her foot. \"Leave a note if you must. I'll put it on Ada's desk in the morning. No promises.\" She holds out her hand, already looking past you.",
 118: "You take a photo of the half-gone name, twice, in case one is blurred. It is proof, of a kind, that you came and looked, and did not give up. Who is it for? Yourself, probably. It will do.",
 119: "You wait outside for the café to open. You stamp your feet in the cold. You watch the card in the window, as if it might change its mind. It does not. But it is something to watch.",
 120: "Ms Rowe sits back and looks at you. \"Tell me,\" she says. \"Why should I take on someone I've never met, who found us by accident?\" It is a fair question. She waits, and does not hurry you.",
 121: "You tell her about the bright office, and the man in the good suit, and the two hundred he wanted first. She listens, still. \"There's one of those on every corner now,\" she says quietly. \"You were right to walk away.\"",
 122: "The late worker is going your way and shares a cab. \"You'll never find it on foot in the dark,\" she says. \"And you look done in.\" You get in, glad. The heater is on. For ten minutes, someone else knows the way.",
 123: "The watchman waves you into his warm hut. He pours something from a flask into a tin cup. \"Nine o'clock,\" he says again. \"Not before. So you may as well be warm.\" You hold the cup and stay.",
 124: "In the queue you hear the name before you see anyone. \"...Ada Rowe wants the Thursday figures...\" Two people from the second floor, talking about work. You are close now. You can hear the place you have tried all night to reach.",
 125: "Mara is at breakfast with the same idea. \"The river,\" she says. \"We could go together. Safer, and I hate arriving alone.\" She says it quietly. You understand, because so do you. You finish your coffee and go.",
 126: "The cleaner has worked here twenty years. \"Kessler and Rowe,\" she says. \"They did right by my sister once, when no one else would.\" She looks at you. \"Go and find them. Don't sleep your chance away.\"",
 127: "You leave your name and number with the man at the counter, just in case. \"If they come in,\" you say. He writes it down and nods, as if he has heard it many times. He has. Everyone here looks for someone.",
 128: "Dawn on the bench. Your back hurts and your money is nearly gone. But you are not ready to give up. Not yet. You sit up. The morning is grey and full of buses. One of them is going your way.",
 129: "You cannot pay for the room. The man at the desk sees it, and something in him softens. \"Sit in the lobby till it's light,\" he says. \"There's a radiator by the window. I never saw you.\" You sit. You could cry, but you sit.",
 141: "You answer simply. You say what you can do, and what you can't. You do not pretend to be anyone else. It is enough. \"We can use someone like that,\" she says. \"Start on Monday.\" No story, no luck. Just work.",
 142: "You walk in rested and clear. You owe nothing to the people who tried to sell you hope. Somehow it shows. Ms Rowe looks at you and almost smiles. \"A good night, for a stranger,\" she says. \"Start on Monday.\"",
 143: "There is no job today. But she writes your name down by hand, on real paper, not a screen. \"We'll have something in the spring,\" she says. \"Come back then.\" It is not what you came for. But you are here now, and someone knows your name.",
 144: "Name, number, reference. It all goes smoothly. By lunchtime you have the job. Nobody asks how you got here, or what the night cost you. You do not say. You got what you came for. You wait to feel something. Nothing comes.",
 145: "You share what little you have. The job does not come. But the man from the bench has a room, a kettle, a spare key. He has a brother who needs hands. You are not hired. But for the first time since the train, you are not alone.",
 146: "You reach Mill Quay at twenty past nine. The book is closed. The chairs are full of other people. The woman at the desk is kind, and final. \"Try us in the spring,\" she says. You both know she means no.",
 147: "The morning is grey over the bench, and you let it come. You are too cold and too tired to move. Just a minute, you tell yourself. But by the time you can feel your feet, nine o'clock has gone. And so has the reason you came.",
}

nodes = choices = 0
for n in book["nodes"]:
    if n["id"] in A2 and isinstance(n.get("text"), dict):
        n["text"]["A2"] = A2[n["id"]]; nodes += 1
    for c in n.get("choices", []):
        t = c.get("text")
        if isinstance(t, dict) and str(t.get("A2", "")).startswith("⟨A2 pending"):
            t["A2"] = t.get("B1", ""); choices += 1

json.dump(book, open(EP, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(f"A2 pass: wrote A2 for {nodes} nodes and filled {choices} choice A2 slots.")
