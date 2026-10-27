#!/usr/bin/env python3
"""Phase 3 prose for Moving Day (episode-11), batch C: Act I gaps 9,10,12,27,32.
Run: python3 scripts/generators/phase3_ep11_c.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-11.json")

D = {
 9: {"t": {
  "A2": "The caretaker, old Reg, meets you at the new flat with a smile. 'Let me get that,' he says, and props the stiff door wide. He waves you in. Mum's bed here, the chair by the window, boxes down the hall. Everything can go straight in now. He's a good sort, Reg.",
  "B1": "The caretaker, old Reg, meets you at the new flat with a smile. 'Let me get that,' he says, and props the stiff door wide. He waves you in. Mum's bed here, the chair by the window, boxes down the hall. Everything can go straight in now. He's a good sort, Reg.",
  "B2": "The caretaker, old Reg, meets you at the new flat with a smile. 'Let me get that for you,' he says, and props the stiff door wide open. He waves you in. Mum's bed here, the big chair by the window, boxes down the hall. Everything can go straight in now, no waiting. He's a good sort, Reg, and always has been."},
  "c": ["Carry it all in.", "Just the basics first.", "Ask an old hand first.", "Ask Reg where things go."]},
 10: {"t": {
  "A2": "On the stairs, you hear a call. An old woman is stuck with her shopping — two heavy bags, no lift, bad knees. She can't get them up, and no one stops. 'Could you?' she asks. You've a flat to fill before dark. But she's right here, stuck, and asking you.",
  "B1": "On the stairs, you hear a call. An old woman is stuck with her shopping — two heavy bags, no lift, and bad knees. She can't get them up, and no one stops for her. 'Could you?' she asks. You've a flat to fill before dark. But she's right here, stuck, and asking you.",
  "B2": "On the stairs, you hear a call. An old woman is stuck with her shopping — two heavy bags, no lift in the building, and bad knees. She can't get them up, and no one stops for her. 'Could you?' she asks. You've a whole flat to fill before dark. But she's right here in front of you, stuck, and asking you."},
  "c": ["Help her up.", "The move comes first."]},
 12: {"t": {
  "A2": "You knock round the doors, asking the same thing each time. Can you lend a hand? Take an end of the sofa. Carry a box. Mind Mum for ten minutes. Some say no — busy, tired, bad back. But a few say yes, and come down. Today, a few is enough.",
  "B1": "You knock round the doors, asking the same thing each time. Can you lend a hand? Take an end of the sofa. Carry a box or two. Mind Mum for ten minutes. Some say no — busy, tired, bad back. But a few say yes, and come down. Today, a few is more than enough.",
  "B2": "You knock round the doors, asking the same thing each time. Can you lend a hand? Take an end of the sofa. Carry a box or two down. Mind Mum for ten minutes. Some say no — too busy, too tired, a bad back. But a few say yes, and come down at once. Today, a few willing neighbours is more than enough."},
  "c": ["See who comes down.", "No one can help."]},
 27: {"t": {
  "A2": "Piling the boxes high would halve your trips, and the van's nearly full. But the stairs are steep and worn, your arms are tired, and you won't see your feet. Tom told you not to carry too much at once. And he wasn't joking.",
  "B1": "Piling the boxes high would halve your trips, and the van's nearly full. But the stairs are steep and worn, your arms are tired, and you won't see your feet. Tom told you not to carry too much at once. And he wasn't joking about it.",
  "B2": "Piling the boxes high in your arms would halve your trips, and the van's nearly full now. But the stairs are steep and worn, your arms are tired, and you won't see your feet at all. Tom told you, plainly, not to carry too much at once. And he wasn't joking when he said it."},
  "c": ["Pile it high.", "One at a time, the safe way."]},
 32: {"t": {
  "A2": "At the next door, a young mum is packing to move too. But she's on her own, with a baby and no help at all. She looks at you, tired and near tears. You've a van, a strong pair of hands, and a little time. Not much, but more than she has.",
  "B1": "At the next door, a young mum is packing to move too. But she's on her own, with a baby and no help at all. She looks at you, tired and near tears. You've a van, a strong pair of hands, and a little time. Not much, but more than she has.",
  "B2": "At the next door, a young mum is packing up to move too. But she's on her own, with a baby on her hip and no help at all. She looks at you, tired and near tears with it. You've a van outside, a strong pair of hands, and a little time left. Not much, maybe, but a good deal more than she has got."},
  "c": ["Lend her your van and hands.", "Wish her luck and go.", "Help her get started."]},
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
