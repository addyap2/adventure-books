#!/usr/bin/env python3
"""Phase 2 (cont.): connective tissue across the night and the morning → ~125 nodes.

Runs on the 90-node skeleton. Adds real beats (not filler): the yard behind №14 and its
unsent letters, the number-16 daughter, the river boathouse, café-dawn waits, the scam's
empty-job payoff and a queue-mate who refuses, plus morning approaches to the quay. New
sources of knows_name / knows_river on the family and river paths. Stub text; validator
is the gate.
"""
import json, os

EP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "episode-01.json")
book = json.load(open(EP, encoding="utf-8"))
by_id = {n["id"]: n for n in book["nodes"]}

def stub(t): return "⟨STUB⟩ " + t
N = lambda t, g, rq=None, st=None: (t, g, rq, st)

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

NEW = [
 # Rosewater / letters night-side
 (95, "The kiosk woman calls after you: \"There's a back way into number 14 — through the yard. "
      "The front door hasn't opened in years.\"",
  [N("Go round the back, into the yard.", 96), N("Try the front of the building.", 7)]),
 (96, "In the yard a low window is lit. Inside, on a desk, there is a tray of envelopes, stamped "
      "and ready — all addressed, you see with a chill, to Rosewater Street.",
  [N("Look in the front window too.", 11), N("Come back at nine, when someone is here.", 17)]),
 (97, "Before you go, the upstairs window opens and the girl leans out. \"They're by the river "
      "now,\" she says, matter-of-fact. \"Ada Rowe. My dad used to work for her.\"",
  [N("Ask her more.", 98), N("Thank her, and wait for morning.", 17)]),
 (98, "\"Three Mill Quay,\" she says, as if everyone knows. \"Take the number four in the "
      "morning.\" Then her father calls her in, and the window shuts.",
  [N("Set off for the river.", 19, None, ["knows_name", "knows_river"]),
   N("Find the café she mentioned.", 15, None, ["knows_name", "knows_river"])]),
 # River / boathouse
 (99, "By the water you lose the thread of the streets entirely. But a boathouse has its lights "
      "on, early, and there is the knock of oars being carried down to the river.",
  [N("Ask the rowers the way.", 100), N("Push on along the dark bank.", 28)]),
 (100, "\"Mill Quay? Straight along, past the second bridge.\" The rower barely breaks step. "
       "\"Ten minutes. You're nearly there.\"",
  [N("Follow the bank to the quay.", 23, None, ["knows_river"]),
   N("Find the coffee cart and wait for nine.", 25, None, ["knows_river"])]),
 (101, "The new development has a glass lobby, lit and empty, a guard's cap on an untended desk. "
       "Everything here is two years newer than the letter in your bag.",
  [N("Try the gate and the night watchman.", 55), N("Wait for morning by the quay.", 23)]),
 # Café dawn
 (102, "You wait for the café to open. The sky goes from black to the colour of dishwater, and a "
       "light comes on inside at last.",
  [N("Ask the counter man when they open properly.", 29), N("Wait at the window.", 15)]),
 (103, "One of the early regulars looks up. \"Kessler and Rowe? I did their books, years back. "
       "Good people. Bad with letters.\" He laughs at his own joke.",
  [N("Head for the quay while there's time.", 23), N("Worry that it is already too late.", 34)]),
 # Hotel / bench dawn
 (104, "The hotel man leans on the desk. \"Word of advice — that agency across the way, the "
       "yellow sign? Don't. They took a lad's last money on Tuesday.\"",
  [N("Take the room and sleep.", 16), N("Too dear — try the station instead.", 13)]),
 (105, "The first bus of the day sighs up to the stop, warm and almost empty. It will go towards "
       "Rosewater, or you could change for the river.",
  [N("Take it to Rosewater Street.", 20), N("Change for the river.", 23)]),
 # Scam payoff / solidarity
 (106, "The address the agency gave you is an empty lot behind a fence. There was never any job. "
       "There was only the two hundred, and it is gone.",
  [N("Call the number again, uselessly.", 39), N("Give up on them and go to Rosewater.", 34)]),
 (107, "A woman near you in the queue reads the form, folds it, and hands it back. \"It's a "
       "swindle,\" she says, loud enough for the others. \"Come on.\" A few of you leave together.",
  [N("Leave the queue with her, for Rosewater.", 17), N("Stay in the queue anyway.", 24)]),
 # Act I extra
 (108, "The taxi carries you through streets with nobody on them, past shuttered shops and one "
       "all-night café throwing yellow light on the wet road.",
  [N("Rosewater Street, please.", 7), N("Somewhere cheap to sleep, by the water.", 10)]),
 (109, "The man at the desk draws you a better map on the back of a receipt, and marks the river "
       "with a small square. \"That's where the smart ones went,\" he says.",
  [N("Take the bus.", 4), N("Walk, with the new map.", 5)]),
 # Act III approaches
 (110, "You walk to the quay in the growing light, past people going to work who know exactly "
       "where they are going. For the first time, so do you.",
  [N("Arrive at the quay.", 23), N("Arrive early, by the water.", 25)]),
 (111, "The young woman from number 16 is going the same way. \"Number four,\" she says, nodding "
       "at the bus. \"I'll show you where to get off.\"",
  [N("Take the bus to the quay with her.", 23), N("Walk to Rosewater with her first.", 27)]),
 (112, "You go to the office to explain yourself, late and out of breath, rehearsing the words on "
       "the stairs.",
  [N("Reach reception and try.", 30), N("You are simply too late.", 146)]),
 (113, "The woman at the coffee cart takes one look at you and puts an extra shot in, no charge. "
       "\"Long night,\" she says. It is not a question.",
  [N("Take it, and go in to reception.", 30), N("Take it, and watch the door a while.", 31)]),
 (114, "You sit with the cold coffee and decide, finally, to trust the letter that brought you "
       "here — or at least the person who wrote it.",
  [N("Go back to Rosewater Street.", 17), N("Ask the café one more time.", 29)]),
 # Act II atmosphere / connective
 (115, "You cross an empty market square, the stalls folded away, a single fox trotting along the "
       "gutter as though it owns the hour.",
  [N("Follow the lit windows.", 49), N("Cut towards the corner shop.", 9)]),
 (116, "A taxi idles at the kerb, its light on, the driver reading a paper. It would cost you, but "
       "it would end the walking.",
  [N("Take it.", 6), N("Keep to the launderette light instead.", 50)]),
 (117, "The cleaner sighs and props the door. \"Leave a note if you must,\" she says. \"I'll put "
       "it on Ada's desk. No promises.\"",
  [N("Leave a note and come back at nine.", 17), N("Ask her one more question first.", 18)]),
 (118, "You take a photograph of the half-scraped name, twice, so you have it whatever happens. "
       "Proof, of a kind, that you were here and looked.",
  [N("Show it at the café.", 15), N("Keep it, and come back at nine.", 17)]),
 (119, "You wait outside the café for it to open, stamping your feet against the cold, watching "
       "the card in the window as if it might change its mind.",
  [N("Tap on the glass at the first sign of life.", 57), N("Give up waiting and go to the quay.", 23)]),
 (122, "The late worker is going your way and splits a cab. \"You'll never find it on foot in the "
       "dark,\" she says. \"And you look done in.\"",
  [N("Share the cab to the river.", 23), N("Thank her, but keep to your own way.", 17)]),
 (123, "The watchman waves you into the warm of his hut and pours something from a flask. \"Nine "
       "o'clock,\" he says again, kindly. \"Not a minute before.\"",
  [N("Wait in the warm until the light.", 25), N("Step out and watch the door.", 31)]),
 (124, "In the coffee-cart queue you hear the name before you see anyone: \"...Ada Rowe wants the "
       "Thursday figures...\" Two people from the second floor, talking shop.",
  [N("Follow them in to reception.", 30), N("Go up and wait your turn.", 84)]),
 (125, "Mara is at breakfast with the same idea as you. \"The river,\" she says. \"We could go "
       "together. Safer, and I hate arriving alone.\"",
  [N("Go to Rosewater first, then part.", 20), N("Go straight to the river together.", 23)]),
 (126, "The cleaner has worked the station twenty years. \"Kessler and Rowe,\" she says. \"They "
       "did right by my sister once. Go and find them. Don't sleep your chance away.\"",
  [N("Take her push, and go.", 20), N("Sit a moment longer, and think.", 21)]),
 (127, "You leave your name and number with the counter man, just in case. \"If they come in,\" "
       "you say. He nods as if he has heard it before, which he has.",
  [N("Go to the quay now.", 23), N("Go back to Rosewater first.", 34)]),
 (128, "Dawn on the bench. Your back is ruined and your money is nearly gone, but you are not, it "
       "turns out, ready to give up. Not quite yet.",
  [N("Get the first bus to Rosewater.", 20), N("Find the café and ask again.", 29)]),
 (129, "You cannot afford the room. The man behind the desk sees it, and something in him gives. "
       "\"Sit in the lobby till it's light,\" he says. \"I never saw you.\"",
  [N("Wait in the warm lobby till dawn.", 20), N("Thank him, but go to the station.", 13)]),
]

for nid, text, choices in NEW:
    node(nid, text, choices)

for nid, text, goto, *rest in [
    (9, "There's a back way into number 14, through the yard.", 95),
    (12, "The girl at the window is leaning out to speak.", 97),
    (19, "By the water, a boathouse has its lights on.", 99),
    (28, "The new development's glass lobby is lit and empty.", 101),
    (21, "Wait for the café to open at first light.", 102),
    (29, "One of the early regulars is looking your way.", 103),
    (10, "Ask the hotel man about the agency across the road.", 104),
    (14, "Wait at the stop for the first bus of the day.", 105),
    (62, "Go to the job address the agency gave you.", 106),
    (60, "A woman in the queue reads the form and stops.", 107),
    (6, "Just take the taxi and end the walking.", 108),
    (2, "Ask him to draw you a proper map.", 109),
    (17, "Walk to the quay in the morning light.", 110),
    (26, "Let her show you the way to the quay.", 111),
    (34, "Go to the office anyway and explain.", 112),
    (25, "Buy a coffee from the woman at the cart.", 113),
    (21, "Decide, finally, to trust the letter.", 114),
    (5, "Cross the empty market square.", 115),
    (49, "A taxi is idling at the kerb.", 116),
    (46, "Ask to leave a note for Ada.", 117),
    (51, "Photograph the half-scraped name.", 118),
    (56, "Wait outside for the café to open.", 119),
    (47, "Share the late worker's cab.", 122),
    (55, "Wait in the watchman's warm hut.", 123),
    (67, "Overhear the coffee-cart queue.", 124),
    (59, "Go to the river with Mara.", 125),
    (58, "Let the cleaner tell you about the old firm.", 126),
    (29, "Leave your name and number with the counter man.", 127),
    (22, "Dawn: decide you are not ready to give up.", 128),
    (10, "You cannot afford the room.", 129),
]:
    add_choice(nid, text, goto)

json.dump(book, open(EP, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(f"Connective pass: now {len(book['nodes'])} nodes, "
      f"{sum(1 for n in book['nodes'] if n.get('ending'))} endings.")
