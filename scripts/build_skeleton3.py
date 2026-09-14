#!/usr/bin/env python3
"""Phase 2 (cont.): deepen Act I (arrival) and Act III (the morning/interview).

Runs on the 75-node skeleton. Act I gets grounding and stakes (what you carry, the
dying phone that reveals the river, sharing the cost with Mara, the guard moving you on).
Act III gets the payoff room it deserves: the waking quay, the reception, and the
interview as a real scene where the misdirected-letters mystery resolves. Stub text;
validator is the gate.
"""
import json, os

EP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "episode-01.json")
book = json.load(open(EP, encoding="utf-8"))
by_id = {n["id"]: n for n in book["nodes"]}

def stub(t): return "⟨STUB⟩ " + t

def node(nid, text, choices):
    book["nodes"].append({"id": nid, "text": stub(text),
        "choices": [dict(text=stub(t), goto=g,
                         **({"requires": rq} if rq else {}),
                         **({"sets": st} if st else {}))
                    for (t, g, rq, st) in choices]})

def add_choice(nid, text, goto, requires=None, sets=None):
    c = {"text": stub(text), "goto": goto}
    if requires: c["requires"] = requires
    if sets: c["sets"] = sets
    by_id[nid]["choices"].append(c)

N = lambda t, g, rq=None, st=None: (t, g, rq, st)

# ---- Act I depth ----
node(69, "In your bag there is the letter, a little money that will not last long, and a "
         "photograph you do not take out. You read the letter again, though you know every word.",
     [N("Go and ask at the information desk.", 2),
      N("Go out into the night.", 3)])
node(72, "Your phone has one bar of battery left. You could use it now to look up the firm, or "
         "save it for something worse.",
     [N("Use the last of it to search the firm.", 73),
      N("Save it, and ask people instead.", 4)])
node(73, "An old page loads, slowly: the firm's address is not Rosewater Street at all, but "
         "somewhere on the river. Then the screen goes black and stays black.",
     [N("Take the bus — you know it is the river now.", 4, None, ["knows_river"]),
      N("Walk, now that you know where.", 5, None, ["knows_river"])])
node(75, "Mara has more sense than money, and you have more money than sense. Between you there "
         "might be enough to do this properly.",
     [N("Share a taxi, and drop Mara off first.", 6),
      N("Take the bus together.", 4)])
node(77, "A guard walks the concourse, turning off lights. \"Station's closing, love. You can't "
         "sit here.\" He is not unkind, only tired, and he means it.",
     [N("Move on, out into the night.", 3),
      N("Ask him the way before you go.", 2)])
node(79, "From the bus window the city slides past, dark and wet and unfamiliar. You could get "
         "off early and find your own feet, or stay on to the proper stop.",
     [N("Get off early and walk the last part.", 5),
      N("Stay on to the Rosewater stop.", 7)])

# ---- Act III depth ----
node(84, "Reception is warm and smells of coffee. The woman behind the desk is kind, and looks at "
         "you a moment longer than she needs to — last night is written all over you.",
     [N("She squeezes you in to see Ms Rowe.", 35),
      N("No room today — but she takes your details.", 37),
      N("A waiting candidate warns you about the agency too.", 91)])
node(85, "Ms Rowe's office looks out over the water. On the desk is a folder, and on top of the "
         "folder is a letter you recognise: your own, sent to the wrong street, come back again.",
     [N("She slides it across: 'this came back to us twice'.", 86),
      N("She sets it aside and asks about you.", 120),
      N("You recognise the bridge you crossed in the dark.", 92)])
node(86, "\"Someone here has been posting the old address for two years,\" she says, turning the "
         "returned letter over. \"You are not the first it sent the wrong way. You are the first to "
         "arrive anyway.\"",
     [N("Offer to be the one who fixes the letters.", 141),
      N("Just say you found them, anyway.", 37),
      N("She calls in the colleague who kept sending them.", 94)])
node(88, "She reaches the step with a coffee in one hand and keys in the other, and sees you "
         "waiting. \"You look like someone who has been up all night,\" she says. \"Come in.\"",
     [N("Help her with the door, and walk in together.", 35),
      N("Hang back, suddenly unsure.", 34)])
node(89, "The quay is waking: gulls on the grey water, a coffee cart, delivery vans humming along "
         "the stone. You have time, for once, and clean hands, for once.",
     [N("Walk the quay a while to steady your nerves.", 67),
      N("Go straight in to reception.", 30)])
node(90, "The man in the good suit from the agency sees you seeing him. For a second neither of "
         "you moves. Then he lets himself into the unmarked building and is gone.",
     [N("Go in to reception before he can.", 30),
      N("Look away, and keep to the water.", 25)])
node(91, "\"They wanted money off me too,\" the other candidate says quietly. \"For 'registration'. "
         "I nearly paid it.\" You are not the only one, then, who nearly did.",
     [N("Take the warning to heart.", 35),
      N("Keep to yourself, and wait.", 37)])
node(92, "Through the window you can see the bridge you crossed in the dark, and the black water "
         "under it, ordinary and grey now. It does not look far at all by daylight.",
     [N("Look closer at the folder and the letter.", 86),
      N("Keep your eyes on Ms Rowe.", 120)])
node(94, "She calls in a younger colleague, who goes red to the ears. \"The old letterhead,\" she "
         "says, not unkindly. \"We will sort it. And you\" — to you — \"can help us sort it.\"",
     [N("Your first job will be the letters.", 141),
      N("She lets it go, for now.", 37)])

# ---- connectors from existing nodes ----
add_choice(1, "Take stock of what you are actually carrying.", 69)
add_choice(3, "Check your phone before you decide.", 72)
add_choice(42, "Work out whether you can share the cost.", 75)
add_choice(41, "A guard is turning the lights off — you cannot linger.", 77)
add_choice(4, "Watch the city from the bus window.", 79)
add_choice(67, "Go up to reception and wait.", 84)
add_choice(35, "She shows you into her office.", 85)
add_choice(27, "Wait for her on the step as the office opens.", 88)
add_choice(23, "Walk the waking quay first.", 89)
add_choice(68, "The agency man notices you watching.", 90)

json.dump(book, open(EP, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(f"Acts I & III deepened: now {len(book['nodes'])} nodes, "
      f"{sum(1 for n in book['nodes'] if n.get('ending'))} endings.")
