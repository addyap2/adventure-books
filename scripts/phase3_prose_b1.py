#!/usr/bin/env python3
"""Phase 3 — the B1 prose pass across every new flagship node.

The existing 40 passages already carry all three levels. Every node added in Phase 2 has
placeholder text that was written as real B1-voice prose (present tense, second person,
spare, humane); this pass promotes it to the B1 slot, applies the richer explicit versions
drafted for the original 17 beats/endings, and levelises every new choice. A2 and B2 are
set to explicit ⟨pending⟩ markers so the validator still sees text at every level and it is
obvious what the A2 (simplify) and B2 (enrich) passes must still write. Branch only.

Idempotent: only touches text that is still a bare string (new content); the existing 40
nodes and their choices are per-level dicts already and are left untouched.
"""
import json, os, re

EP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "episode-01.json")
book = json.load(open(EP, encoding="utf-8"))

def pend(level):
    return f"⟨{level} pending⟩"

def strip(s):
    return re.sub(r"^⟨STUB⟩\s*", "", s).strip()

# Richer explicit B1 for the original 17 Phase-2 nodes (fuller than their one-line stubs).
PROSE = {
 41: "The last doors close and the platform empties around you. A few travellers hurry towards "
     "the exit with their collars up. One of them, a young traveller with a heavy rucksack, stops "
     "under a light and reads a scrap of paper, then reads it again — the way you keep reading your "
     "own letter. They look as lost as you feel.",
 42: "Her name is Mara, and she came in on the same train. She is here for work too, and knows the "
     "city no better than you do. For a few minutes, in the cold light of the station, neither of "
     "you is quite alone. Her address is somewhere across the river; yours is a street she has "
     "never heard of.",
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

nodes_done = choices_done = 0
for n in book["nodes"]:
    if isinstance(n.get("text"), str):                       # a new node (bare string)
        b1 = PROSE.get(n["id"]) or strip(n["text"])
        n["text"] = {"A2": pend("A2"), "B1": b1, "B2": pend("B2")}
        nodes_done += 1
    for c in n.get("choices", []):
        if isinstance(c.get("text"), str):                   # a new/added choice
            b1 = strip(c["text"])
            c["text"] = {"A2": pend("A2"), "B1": b1, "B2": pend("B2")}
            choices_done += 1

json.dump(book, open(EP, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(f"B1 pass: wrote B1 for {nodes_done} nodes and {choices_done} choices; A2/B2 ⟨pending⟩.")
