#!/usr/bin/env python3
"""Phase 3 prose for The Interview (episode-10), batch C: Act I gaps 9,10,12,27,32.
Run: python3 scripts/generators/phase3_ep10_c.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-10.json")

D = {
 9: {"t": {
  "A2": "The print shop is still open. Old Sam waves you in out of the rain. 'Use the machine,' he says. 'Pay me when you can.' He points you to it. Print your CV, your letter, the address, the map. Everything you need to walk in ready. He's a good sort, Sam.",
  "B1": "The print shop is still open, and old Sam waves you in out of the rain. 'Use the machine,' he says. 'Pay me when you can.' He points you to it. Print your CV, your letter, the address, the map. Everything you need to walk in ready is here. He's a good sort, Sam.",
  "B2": "The print shop is still open, and old Sam waves you in out of the rain. 'Use the machine,' he says. 'Pay me when you're able.' He points you to it in the corner. Print your CV, your covering letter, the address, the map — everything you need to walk in ready is right here. He's a good sort, Sam, and always has been."},
  "c": ["Print it all, properly.", "Grab the basics and go.", "Ask an old hand first.", "Ask Sam what he'd do."]},
 10: {"t": {
  "A2": "Near the station, you see her. A young woman stands frozen at the barrier, her ticket jammed, the crowd pushing past. She can't get through, and no one stops. 'Can you help?' she asks. You've an interview to reach and no time. But she's right here, stuck, and asking you.",
  "B1": "Near the station, you see her. A young woman stands frozen at the barrier, her ticket jammed, the crowd pushing past. She can't get through, and no one stops for her. 'Can you help?' she asks. You've an interview to reach and no time. But she's right here, stuck, and asking you.",
  "B2": "Near the station, you see her. A young woman stands frozen at the ticket barrier, her ticket jammed, the crowd pushing past on both sides. She can't get through, and no one stops for her. 'Can you help me?' she asks. You've an interview to reach and precious little time. But she's right here in front of you, stuck, and asking you for help."},
  "c": ["Help her through.", "The interview comes first."]},
 12: {"t": {
  "A2": "You make your calls, asking the same thing each time. Can you help me get there? Send me the address. Give me a lift. Steady my nerves. Some say no — too busy, too far, bad timing. But a few say yes, and come through. Today, a few is enough.",
  "B1": "You make your calls, asking the same thing each time. Can you help me get there? Send me the address. Give me a lift. Steady my nerves. Some say no — too busy, too far, bad timing. But a few say yes, and come through for you. Today, a few is more than enough.",
  "B2": "You make your calls, asking the same thing each time. Can you help me get there? Send me the address. Give me a lift across town. Steady my nerves. Some say no — too busy, too far, bad timing all round. But a few say yes, and come through for you at once. Today, a few willing people is more than enough."},
  "c": ["See who comes through.", "No one can help."]},
 27: {"t": {
  "A2": "Jumping the queue up front would save you twenty minutes, and the platform is right there. But the guards are watching, the crowd is tight, and getting caught means losing it all. Frank told you not to cut the line. And he wasn't joking.",
  "B1": "Jumping the queue up front would save you twenty minutes, and the platform is right there. But the guards are watching, the crowd is tight, and getting caught means losing it all. Frank told you not to cut the line. And he wasn't joking about it.",
  "B2": "Jumping the queue right up front would save you a good twenty minutes, and the platform is right there. But the guards are watching closely, the crowd is tight, and getting caught means losing the whole thing. Frank told you, plainly, not to cut the line. And he wasn't joking when he said it."},
  "c": ["Chance the queue.", "Go the long, right way."]},
 32: {"t": {
  "A2": "At the barrier, a lad about your age looks lost and grey. He's up for the same job, he says, and he's frozen — forgot his notes, forgot everything. He looks at you, tired and ashamed. You've your own notes in your hand. Not much, but more than he has.",
  "B1": "At the barrier, a lad about your age looks lost and grey. He's up for the same job, he says, and he's frozen — forgot his notes, forgot everything. He looks at you, tired and ashamed. You've your own notes in your hand. Not much, but a good deal more than he has.",
  "B2": "At the barrier, a lad about your own age looks lost and grey. He's up for the very same job, he says, and he's frozen solid — forgot his notes, forgot everything. He looks at you, tired and ashamed of himself. You've your own notes right there in your hand. Not much, maybe, but a good deal more than he has got."},
  "c": ["Share your notes.", "Wish him luck and go.", "Help him calm down."]},
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
    print(f"batch C: wrote prose for {len(D)} nodes")


if __name__ == "__main__":
    main()
