#!/usr/bin/env python3
"""Phase 3 (B1 pass): write real B1 prose into the new flagship nodes and their choices.

The existing 40 passages already carry all three levels. This fills the new beat nodes
and the seven new endings at B1, in the established voice (present tense, second person,
spare, humane). A2 and B2 are left as explicit ⟨pending⟩ markers so the validator still
sees text at every level and it is obvious what the next passes must write. Branch only.
"""
import json, os

EP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "episode-01.json")
book = json.load(open(EP, encoding="utf-8"))

def pend(level, hint):
    return f"⟨{level} pending — derive from B1⟩ {hint}"

# ---- B1 prose for the new nodes ----
PROSE = {
 41: "The last doors close and the platform empties around you. A few travellers hurry towards "
     "the exit with their collars up. One of them, a young traveller with a heavy rucksack, stops "
     "under a light and reads a scrap of paper, then reads it again — the way you keep reading your "
     "own letter. They look as lost as you feel.",
 42: "Her name is Mara, and she came in on the same train. She is here for work too, and knows the "
     "city no better than you do. For a few minutes, in the cold light of the station, neither of "
     "you is quite alone. Her address is somewhere across the river; yours is a street she has never "
     "heard of.",
 43: "The man at the newsstand is old and slow, and reads your letter twice. \"Rosewater Street,\" "
     "he says. \"You are the third one this month I have sent that way. Somebody up there still puts "
     "the old address on the letters.\" He hands the paper back as if that settles it.",
 44: "\"They moved to the river years ago,\" he says. \"New offices, all glass. But the letters "
     "still go out with Rosewater Street on them. Not my business.\" He shrugs. It is somebody's "
     "business, you think — and tomorrow, perhaps, it might even be yours.",
 45: "Half of Rosewater Street is hidden behind builders' hoarding. On it, a torn notice still "
     "carries the firm's name in faded print. Underneath, someone has written one word in thick "
     "marker, with an arrow pointing east, towards the water: MOVED.",
 46: "You almost miss it: a narrow side door, half behind the hoarding, with a thin line of light "
     "along the bottom. Someone is inside after all.",
 47: "After a while the door opens and a woman comes out, pulling on her coat. She is tired, but "
     "not unfriendly. \"Nobody works here now,\" she says. \"They are down by the river. If you "
     "cannot wait until morning, ask at the café on the corner — they know everyone.\"",
 48: "On the next bench a man sits with no bag and no coat, only a paper cup. He is not asking for "
     "anything. He has missed the last train and has nowhere to be until morning — the same as you, "
     "except that he has done this on many more nights than you have.",
 120: "Ms Rowe sits back in her chair and looks at you for a moment. \"Tell me,\" she says, \"why I "
      "should take on someone I have never met, who found us more or less by accident.\" It is a "
      "fair question, and she waits for your answer without hurrying you.",
 121: "You tell her about the bright office and the man in the good suit, and the two hundred he "
      "wanted before he would find you any work at all. She listens without a flicker. \"There is "
      "one of those on every corner now,\" she says quietly. \"You were right to walk away.\"",
 141: "You answer plainly. You tell her what you can do, and what you cannot, and you do not pretend "
      "to be anyone but yourself. It is enough. \"We can use someone like that,\" she says. \"Start "
      "on Monday.\" No story, no luck — just work, honestly won.",
 142: "You walk in rested and clear-headed, owing nothing to anyone who tried to sell you hope in "
      "the night. Somehow it shows. Ms Rowe studies you for a moment and almost smiles. \"You had a "
      "good night, for a stranger in a strange city,\" she says. \"Start on Monday.\"",
 143: "There is no job today. But she takes your name and writes it down herself, by hand, on a "
      "real sheet of paper rather than into a screen. \"We will have something in the spring,\" she "
      "says. \"Come back then.\" It is not what you came for. But you are in the city now, and "
      "someone in it knows your name.",
 144: "Name, number, reference. Everything goes smoothly, and by lunchtime you have the job. Nobody "
      "asks how you got here, or what the night cost you, and you do not say. You got exactly what "
      "you came for. Standing on the new carpet, you wait to feel something, and nothing comes.",
 145: "You share what little you have. The job does not come — the diary is full, the timing wrong. "
      "But the man from the bench, it turns out, has a room, a kettle and a spare key, and a brother "
      "who is always looking for hands. You are not hired. You are also, for the first time since "
      "the train, not alone.",
 146: "You reach Mill Quay at twenty past nine. The diary is closed, the chairs in reception are "
      "full of other people, and the woman behind the desk is kind and completely final. \"Try us "
      "in the spring,\" she says, and you both know she means no. Outside, the river goes on exactly "
      "as before.",
 147: "The morning comes up grey over the station bench, and you let it. You are too cold and too "
      "tired to move, and you tell yourself it is only for a minute. By the time you can feel your "
      "feet again, nine o'clock has come and gone — and so has the only reason you came to this city.",
}

# ---- B1 labels for every new/added choice, keyed by (node id, goto) ----
CHOICE = {
 (1, 41): "Wait a moment, and watch who else gets off the train.",
 (2, 43): "Ask the man if others have come looking for this firm.",
 (3, 42): "See who else is leaving the station on foot.",
 (7, 45): "Read the notices on the builders' hoarding.",
 (11, 46): "Try the side door you can just make out.",
 (13, 48): "Notice the man on the next bench.",
 (35, 120): "Wait — she has a question for you first.",
 (20, 143): "Leave your name at the empty office, and go.",
 (30, 144): "Give only your name and the reference number.",
 (34, 146): "Push on to Mill Quay anyway — it is twenty past nine.",
 (22, 147): "Stay on the bench, and let the morning come.",
 (23, 142): "Walk straight in — rested, clear-headed, owing nothing.",
 (41, 42): "Fall into step with the young traveller.",
 (41, 2): "Keep to yourself, and go to the information desk.",
 (42, 43): "Ask the newsstand man about your street.",
 (42, 3): "Wish her luck, and go your separate ways.",
 (43, 44): "Ask what he means — 'the third one this month'.",
 (43, 4): "Just ask him the quickest way there.",
 (44, 4): "Take the bus towards Rosewater Street anyway.",
 (44, 5): "Walk, and save the fare.",
 (45, 19): "Follow the arrow towards the river.",
 (45, 12): "Try number 16 first.",
 (46, 18): "Knock, and let the cleaner wave you away.",
 (46, 47): "Wait quietly on the step instead.",
 (47, 17): "Decide to head for the river at first light.",
 (47, 15): "Go and find the café on the corner.",
 (48, 145): "Share what little you have with him.",
 (48, 21): "Keep what you have, and move on.",
 (120, 141): "Answer plainly, about the work you can do.",
 (120, 121): "Tell her about the agency you almost paid.",
 (121, 36): "Tell her the whole night, as well.",
 (121, 37): "Leave it there, and keep things professional.",
}

def levelise_node(nid, prose):
    n = next(x for x in book["nodes"] if x["id"] == nid)
    beat = n["text"] if isinstance(n["text"], str) else n["text"].get("B1", "")
    n["text"] = {"A2": pend("A2", "(" + prose[:60] + "…)"),
                 "B1": prose,
                 "B2": pend("B2", "(" + prose[:60] + "…)")}

def levelise_choice(nid, goto, label):
    n = next(x for x in book["nodes"] if x["id"] == nid)
    for c in n["choices"]:
        if c.get("goto") == goto:
            c["text"] = {"A2": pend("A2", label), "B1": label, "B2": pend("B2", label)}
            return
    raise KeyError(f"no choice §{nid}→{goto}")

for nid, prose in PROSE.items():
    levelise_node(nid, prose)
for (nid, goto), label in CHOICE.items():
    levelise_choice(nid, goto, label)

json.dump(book, open(EP, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
done = len(PROSE)
print(f"Wrote B1 prose for {done} new nodes and {len(CHOICE)} choices. "
      f"A2/B2 left as ⟨pending⟩.")
