#!/usr/bin/env python3
"""Phase 3 prose for The Dinner (episode-09), batch D: Act I gap nodes 9,10,12,27,32.
Run: python3 scripts/generators/phase3_ep09_d.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-09.json")

D = {
 9: {"t": {
  "A2": "The shop is still open. Old Sam waves you in out of the rain. 'Take what you need,' he says. 'Pay me later.' He points to the shelves. Flour, eggs, a bit of meat, some veg. Everything for a proper dinner. He's a good sort, Sam.",
  "B1": "The shop is still open, and old Sam waves you in out of the rain. 'Take what you need,' he says. 'Pay me when you can.' He points to the shelves. Flour, eggs, a bit of meat, some veg. Everything you need for a proper dinner is here. He's a good sort, Sam.",
  "B2": "The shop is still open, and old Sam waves you in out of the rain. 'Take what you need,' he says. 'Pay me when you're able.' He points to the shelves. Flour, eggs, a bit of meat, some veg. Everything you'd want for a proper dinner is here, under one roof. He's a good sort, Sam, and always has been."},
  "c": ["Load the basket.", "Grab the basics and run.", "Ask Joan's advice first.", "Ask Sam what he'd cook."]},
 10: {"t": {
  "A2": "Next door, you hear knocking. Mr Doyle is locked out, shivering on his step in the rain. He can't get in, and his hands are too cold to work the key. 'Can you help?' he asks. You've a dinner to cook. But he's here, cold and asking you.",
  "B1": "Next door, you hear knocking. Mr Doyle is locked out, shivering on his step in the rain. He can't get in, and his hands are too cold to work the key. 'Can you give me a hand?' he asks. You've a dinner to cook and no time. But he's right here, cold and asking you.",
  "B2": "Next door, you hear a knocking. Mr Doyle is locked out, shivering on his own step in the rain. He can't get in, and his hands are far too cold to work the key. 'Can you give me a hand?' he asks. You've a dinner to cook and precious little time. But he's right here in front of you, cold and asking you for help."},
  "c": ["Help him in.", "The dinner comes first."]},
 12: {"t": {
  "A2": "You go round the doors and make your calls, asking the same thing each time. Come and help with the dinner. Bring a dish, bring a chair, bring yourself. Some say no, too busy, too tired. But a few say yes, and start pulling on their coats. Tonight, a few is enough.",
  "B1": "You go round the doors and make your calls, asking the same thing each time. Come and help with the dinner. Bring a dish, bring a chair, bring yourself. Some say no — too busy, too tired, another night. But a few say yes, and start pulling on their coats. Tonight, a few is more than enough.",
  "B2": "You go round the doors and make your phone calls, asking the same thing each time. Come and help with the dinner tonight. Bring a dish, bring a chair, bring yourself and an appetite. Some say no — too busy, too tired, another night maybe. But a few say yes, and start pulling on their coats at once. Tonight, a few willing hands is more than enough to begin."},
  "c": ["See who turns up.", "No one can come."]},
 27: {"t": {
  "A2": "Cutting across the main road would halve your walk, and home lies just beyond it. But the traffic is fast, the rain is hard, and the cars won't see you well. Joan told you to keep off that road. And she wasn't joking.",
  "B1": "Cutting straight across the main road would halve your walk, and home lies just beyond it. But the traffic is fast, the rain is hard, and the cars won't see you well in the dark. Joan told you to keep off that road. And she wasn't joking about it.",
  "B2": "Cutting straight across the main road would halve your walk, and home lies just beyond it now. But the traffic is fast, the rain is coming hard, and the cars won't see you at all well in the dark. Joan told you, plainly, to keep off that road. And she wasn't joking when she said it."},
  "c": ["Chance the road.", "Go the long way."]},
 32: {"t": {
  "A2": "At one house the lights are low and a child is crying. A family here has no dinner tonight — bare cupboards, no money till Friday, and hungry kids. The two parents look at you, tired and ashamed. You've bags of food of your own. Not a lot, but more than they have.",
  "B1": "At one house the lights are low and a child is crying inside. A family here has no dinner tonight — bare cupboards, no money till Friday, and hungry kids. The two parents look at you, tired and ashamed. You've bags of food of your own in your hands. Not a lot, but a good deal more than they have.",
  "B2": "At one house the lights are low and a child is crying somewhere inside. A family here has no dinner tonight — bare cupboards, no money until Friday, and two hungry kids. The two parents look at you, tired and ashamed to be seen like this. You've bags of food of your own in your hands. Not a lot, maybe, but a good deal more than they have got."},
  "c": ["Give them your food.", "Promise help, then go.", "Help them cook what's there."]},
}


def main():
    d = json.load(open(P, encoding="utf-8"))
    by = {n["id"]: n for n in d["nodes"]}
    for nid, spec in D.items():
        n = by[nid]; n["text"] = spec["t"]
        for j, c in enumerate(n.get("choices") or []):
            if j < len(spec["c"]):
                t = spec["c"][j]; c["text"] = {"A2": t, "B1": t, "B2": t}
    json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"batch D: wrote prose for {len(D)} nodes")


if __name__ == "__main__":
    main()
