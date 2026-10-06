#!/usr/bin/env python3
"""Phase 2: expand episode-01's graph to the flagship skeleton.

Preserves the existing 40 passages and their prose. Adds the eight-flag state model,
wires each flag onto the choice where it is earned, deepens the three acts with new
beat nodes (stub text, marked ⟨STUB⟩, to be written in the prose phase), and adds the
seven new endings so the full 12-ending fan exists. Idempotent-ish: run once on the
40-node file. The validator is the gate — this must leave the graph clean.
"""
import json, os

EP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "episode-01.json")
book = json.load(open(EP, encoding="utf-8"))

FLAGS = ["has_card", "knows_name", "knows_river", "dodged_scam", "paid_scam",
         "rested", "rough_night", "told_truth"]
book["state_out"] = FLAGS

by_id = {n["id"]: n for n in book["nodes"]}

def choice(nid, goto):
    for c in by_id[nid]["choices"]:
        if c.get("goto") == goto:
            return c
    raise KeyError(f"no choice §{nid}→{goto}")

def add_set(nid, goto, flag):
    c = choice(nid, goto)
    s = c.get("sets") or []
    if isinstance(s, str):
        s = [s]
    if flag not in s:
        s.append(flag)
    c["sets"] = s

# --- wire flags onto existing choices where they are earned ---
add_set(10, 16, "rested")                       # take the hotel room
for a, b in [(7, 13), (8, 13), (8, 14), (10, 13), (14, 22)]:
    add_set(a, b, "rough_night")                # sleep rough / walk the night
add_set(24, 33, "dodged_scam")                  # refuse the agency
add_set(24, 32, "paid_scam")                    # pay the agency
add_set(35, 36, "told_truth")                   # tell Rowe the whole night
for a, b in [(6, 7), (6, 10), (12, 17), (12, 19), (29, 23), (29, 34)]:
    add_set(a, b, "knows_river")                # someone tells you they moved to the river

def stub(text):
    return "⟨STUB⟩ " + text

def add_choice(nid, text, goto, requires=None, sets=None):
    c = {"text": stub(text), "goto": goto}
    if requires:
        c["requires"] = requires
    if sets:
        c["sets"] = sets
    by_id[nid]["choices"].append(c)

def node(nid, text, choices):
    n = {"id": nid, "text": stub(text),
         "choices": [dict(text=stub(t), goto=g,
                          **({"requires": rq} if rq else {}),
                          **({"sets": st} if st else {}))
                     for (t, g, rq, st) in choices]}
    book["nodes"].append(n)
    by_id[nid] = n

def ending(nid, text, kind):
    n = {"id": nid, "text": stub(text), "ending": kind}
    book["nodes"].append(n)
    by_id[nid] = n

# --- new beat nodes (stub text -> prose phase) ---
# Act I: the arrival, deepened; the night-shift man seeds the letters mystery
node(41, "The platform empties. You watch who else got off the late train — among them a "
         "young traveller reading an address on a scrap of paper, the way you are.",
     [("Fall into step with the young traveller.", 42, None, None),
      ("Keep to yourself and go to the information desk.", 2, None, None)])
node(42, "The young traveller is Mara, also here for work, also new. For a few minutes in a "
         "cold station you are not quite alone.",
     [("Ask the newsstand man about your address.", 43, None, None),
      ("Head out into the night, each your own way.", 3, None, None)])
node(43, "The night-shift man at the newsstand reads your letter. \"Rosewater Street? Third "
         "one this month I've sent that way. Somebody up there still posts the old address.\"",
     [("Ask what he means — 'third one this month'.", 44, None, None),
      ("Just take the bus he points you to.", 4, None, ["knows_river"])])
node(44, "He shrugs. \"They moved to the river years back. But the letters still go out with "
         "the old street on them. Not my business.\" It is, you think, somebody's business.",
     [("Take the bus to Rosewater Street anyway.", 4, None, ["knows_river"]),
      ("Walk, to save the fare.", 5, None, ["knows_river"])])
# Act II: Rosewater texture, the side door, a kindness beat
node(45, "On the builders' hoarding a torn notice still carries the firm's name. Under it, in "
         "marker, someone has written a single word and an arrow: MOVED →, pointing east, "
         "toward the water.",
     [("Follow the arrow toward the river.", 19, None, ["knows_river"]),
      ("Try number 16 first.", 12, None, None)])
node(46, "There is a narrow side door you had not seen, and a thread of light under it.",
     [("A cleaner opens it and waves you off.", 18, None, None),
      ("Wait quietly on the side step.", 47, None, None)])
node(47, "A woman comes out pulling on her coat — a late worker, not a stranger to the place. "
         "\"Nobody here now,\" she says, not unkindly. \"They're by the river. Or ask at the café.\"",
     [("Head for the river at first light.", 17, None, ["knows_river"]),
      ("Go to the café on the corner.", 15, None, None)])
node(48, "By the bench you find someone worse off than you — cold, no ticket, no plan. You have "
         "almost nothing yourself. Almost.",
     [("Share what little you have.", 145, None, None),
      ("Keep it, and keep moving.", 21, None, None)])
# Act III: the interview as a real scene
node(120, "Ms Rowe sits back. \"Tell me why I should take on someone I have never met, who found "
          "us by accident.\"",
     [("Answer plainly, about the work you can do.", 141, None, None),
      ("Tell her about the agency you almost paid.", 121, None, None)])
node(121, "You tell her how close you came to handing two hundred to a man in a good suit for a "
          "receipt with no address on it. She listens without a flicker.",
     [("Tell her the whole night, too.", 36, None, ["told_truth"]),
      ("Leave it there, and keep it professional.", 37, None, None)])
# --- new choices into the new depth from existing nodes ---
add_choice(1, "Wait a moment and watch who else gets off the train.", 41)
add_choice(2, "Ask the man if others have come looking for this firm.", 43)
add_choice(3, "Check what you are carrying before you decide.", 42)
add_choice(7, "Read the notices on the builders' hoarding.", 45)
add_choice(11, "Try the side door you can just make out.", 46)
add_choice(13, "Notice someone worse off than you nearby.", 48)
add_choice(35, "Wait — she has a question for you first.", 120)
add_choice(20, "Leave your name at the empty office and go.", 143)
add_choice(30, "Give only your name and the reference number.", 144)
add_choice(34, "Reach Mill Quay at last — twenty past nine.", 146)
add_choice(22, "Stay on the bench and let the morning pass.", 147)
add_choice(23, "Walk straight in — rested, clear-headed, nothing owed.", 142,
           requires=["rested", "dodged_scam"])
# --- the seven new endings ---
ending(141, "You answer plainly, and it is enough. \"We can use someone like that,\" she says. "
            "\"Start Monday.\" Not a story — just work, honestly won.", "good")
ending(142, "You walk in rested, having owed nothing to anyone who tried to sell you hope, and it "
            "shows. \"You had a good night, for a stranger,\" she says. \"Start Monday.\"", "good")
ending(143, "There is no job today. But your name is written down, by a real hand, and kept. You "
            "are in the city now, and someone in it knows you came.", "neutral")
ending(144, "Name, number, reference. It all goes smoothly and you are hired by lunchtime. Nobody "
            "asked how you got here. You got what you came for, and it feels like nothing.", "neutral")
ending(145, "You share what you have. The job does not come — but the person you helped has a floor, "
            "a kettle, a spare key. You are not hired. You are also not alone.", "neutral")
ending(146, "Twenty past nine. The diary is closed, the chairs are full, and the woman at reception "
            "is kind and final. \"Try us in the spring,\" she says, meaning no.", "bad")
ending(147, "The morning comes up grey over the bench and you let it. By the time you can feel your "
            "feet again, nine o'clock has been and gone, and so has the reason you came.", "bad")

json.dump(book, open(EP, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(f"Skeleton built: {len(book['nodes'])} nodes, "
      f"{sum(1 for n in book['nodes'] if n.get('ending'))} endings, flags={len(FLAGS)}.")
