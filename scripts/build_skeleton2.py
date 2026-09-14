#!/usr/bin/env python3
"""Phase 2 (cont.): deepen Act II — the night — with more beat nodes.

Runs on the 57-node skeleton. Adds texture and micro-decisions across the night's
clusters (the lost walk, the Rosewater interior, number 16, the river/bridge, the café,
the station bench/hotel, and the agency scam given room to tempt), plus a second source
of `knows_name` on the café path and more `knows_river` reveals. Stub text; validator is
the gate. Idempotent only if run once.
"""
import json, os

EP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "episode-01.json")
book = json.load(open(EP, encoding="utf-8"))
by_id = {n["id"]: n for n in book["nodes"]}

def stub(t): return "⟨STUB⟩ " + t

def add_choice(nid, text, goto, requires=None, sets=None):
    c = {"text": stub(text), "goto": goto}
    if requires: c["requires"] = requires
    if sets: c["sets"] = sets
    by_id[nid]["choices"].append(c)

def node(nid, text, choices):
    n = {"id": nid, "text": stub(text),
         "choices": [dict(text=stub(t), goto=g,
                          **({"requires": rq} if rq else {}),
                          **({"sets": st} if st else {}))
                     for (t, g, rq, st) in choices]}
    book["nodes"].append(n); by_id[nid] = n

# --- new Act II beat nodes ---
node(49, "You take a wrong turn, and then another. The same shuttered shop goes past twice. The "
         "map in your hand has stopped meaning anything.",
     [("Head for an all-night light you can see two streets over.", 50, None, None),
      ("Press on towards number 14 on foot.", 7, None, None)])
node(50, "The light is a launderette, open all night, empty except for one attendant folding "
         "towels. He is glad of the company and knows the streets by heart.",
     [("Take his tip and go to the café on the corner.", 15, None, ["knows_river"]),
      ("Thank him and carry on to the street.", 7, None, ["knows_river"])])
node(51, "On the glass of an inner door at the back, a painted name is half scraped away: you can "
         "still read ROWE under the marks. Someone left in a hurry, or someone wanted it gone.",
     [("Note it, and come back at nine.", 17, None, None),
      ("Knock, and see who is cleaning in there.", 18, None, None)])
node(52, "An upstairs window at number 16 is lit. A girl of about ten watches you from behind the "
         "glass, quite calm, the way children watch when they are used to strangers at odd hours.",
     [("Give a small wave, and wait for morning.", 17, None, None),
      ("Set off for the river tonight instead.", 19, None, None)])
node(53, "A night bus swings around the far corner, its windows warm and yellow, heading the way "
         "you think the river lies. It will not wait.",
     [("Run, and catch it to the quay.", 23, None, None),
      ("Let it go, and keep walking.", 28, None, None)])
node(54, "A bridge crosses the black water. On the far side the new offices stand dark and clean, "
         "all glass — except one window, high up, where a single light is still on.",
     [("Try the gate of the new development.", 55, None, None),
      ("Wait for morning down by the quay.", 23, None, None)])
node(55, "A night watchman leans out of a lit hut at the gate. \"Kessler and Rowe? Second floor. "
         "But there's nobody in till nine, love. Go and get warm.\" He says it kindly.",
     [("Take his word, and wait for the light.", 25, None, ["knows_river"]),
      ("Wait by the water and watch the door.", 31, None, ["knows_river"])])
node(56, "The Blue Kettle is shut, but there is a light in the back and the shape of someone "
         "stacking chairs. The business card is still taped inside the window.",
     [("Tap on the glass.", 57, None, None),
      ("Just read the card, and head for the quay.", 23, None, None)])
node(57, "The woman inside lets you say your piece through a gap in the door. \"Kessler and Rowe? "
         "Ada Rowe, you mean. She's down at the river now. Comes in here for her coffee.\"",
     [("Go to the quay, knowing the name now.", 23, None, ["knows_name"]),
      ("Find a bed, and come back at nine.", 17, None, ["knows_name"])])
node(58, "The cleaner who woke you is not unkind about it. She pours you half a cup from a flask "
         "before you can say no, and asks, without much curiosity, where you have come from.",
     [("Sit a while, and tell her.", 21, None, None),
      ("Thank her, and go.", 20, None, None)])
node(59, "At breakfast, Mara is there too — she took a room here as well. \"There is an agency "
         "across the road,\" she says, low. \"They wanted money off me last night. Don't.\"",
     [("Go and see the agency for yourself anyway.", 24, None, None),
      ("Take her warning, and go straight to Rosewater.", 20, None, None)])
node(60, "A queue has formed outside WORK FOR EVERYONE before it is even open. Tired faces, early "
         "light. A woman near the front counts out the last of her notes, twice.",
     [("Join the queue.", 24, None, None),
      ("Think twice, and turn towards Rosewater.", 17, None, None)])
node(61, "The man in the good suit slides a form across. \"Two hundred for registration, then we "
         "place you today.\" The small print underneath is grey and very small.",
     [("Read the small print, and refuse.", 33, None, ["dodged_scam"]),
      ("Sign it — you are almost out of choices.", 32, None, ["paid_scam"])])
node(62, "Outside, a man leans on the wall with a receipt like the one you would have had. \"Paid "
         "them last week,\" he says. \"They never called. You didn't, did you?\"",
     [("Panic, and call the number now.", 39, None, None),
      ("Cut your losses, and head for Rosewater.", 34, None, None)])
node(63, "On the reception desk there is a tray of returned post — old letters, each with the "
         "Rosewater Street address crossed out by hand. Your own letter, you realise, is one of these.",
     [("Mention the letters to the receptionist.", 35, None, None),
      ("Say nothing about it.", 37, None, None)])
node(65, "The driver settles into the story as he drives. \"They all moved to the river — glass "
         "offices, very smart. And watch the work agencies near the station. They are not what they "
         "look like.\"",
     [("Ask him to take you to Rosewater Street.", 7, None, ["knows_river"]),
      ("Ask for a cheap hotel near the water.", 10, None, ["knows_river"])])
node(67, "First light comes up grey over Mill Quay. A coffee cart is opening; delivery vans hum "
         "along the water. You are early, and for once you know exactly where you are.",
     [("Buy a coffee, and go in to reception.", 30, None, None),
      ("Wait by the water, and watch the door.", 31, None, None)])
node(68, "Watching the other doors along the quay, you see the man in the good suit from the agency "
         "let himself into a building two doors down — no sign, no name on it at all.",
     [("Go in to reception now, certain of things.", 30, None, None),
      ("Keep to the water until nine.", 25, None, None)])

# --- connect the new depth from existing nodes ---
add_choice(5, "Admit you are lost, and look for help.", 49)
add_choice(11, "Read the half-scraped name on the inner door.", 51)
add_choice(12, "Notice the lit upstairs window.", 52)
add_choice(19, "Take the shortest way you can guess toward the water.", 53)
add_choice(28, "Cross the bridge towards the one lit window.", 54)
add_choice(15, "There is a light in the back of the café — look closer.", 56)
add_choice(13, "Let the cleaner pour you a coffee.", 58)
add_choice(16, "Go down to breakfast.", 59)
add_choice(16, "Look at the queue outside the agency first.", 60)
add_choice(20, "Look at the queue outside the agency first.", 60)
add_choice(24, "Ask exactly what the two hundred is for.", 61)
add_choice(32, "Outside, someone with a receipt like yours stops you.", 62)
add_choice(30, "Notice the tray of returned letters on the desk.", 63)
add_choice(6, "Ask him why the offices moved.", 65)
add_choice(25, "Buy a coffee from the cart to steady yourself.", 67)
add_choice(31, "Watch the other doors along the quay.", 68)

json.dump(book, open(EP, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(f"Act II deepened: now {len(book['nodes'])} nodes, "
      f"{sum(1 for n in book['nodes'] if n.get('ending'))} endings.")
