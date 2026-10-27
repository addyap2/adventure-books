#!/usr/bin/env python3
"""Phase 3 prose for Moving Day (episode-11), batch B: rest of Act I, nodes 28-39.
Run: python3 scripts/generators/phase3_ep11_b.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-11.json")

D = {
 28: {"t": {
  "A2": "You stack the boxes high in your arms, more than you should. At once it feels wrong. You can't see your feet, and the top box wobbles. Every step up the stairs is a gamble now. And there's no setting it down safely once you've started to climb.",
  "B1": "You stack the boxes high in your arms, more than you should. At once it feels wrong. You can't see your feet, and the top box wobbles with each step. Every step up the stairs is a gamble now — and there's no setting it down safely once you've started to climb.",
  "B2": "You stack the boxes high in your arms, far more than you should. At once it feels wrong, deep down. You can't see your feet at all, and the top box wobbles with each step. Every step up the stairs is a gamble now — and there's no setting the whole lot down safely once you've started to climb."},
  "c": ["Almost up.", "The pile tips."]},
 29: {"t": {
  "A2": "You try the new key, and it won't turn. It sticks halfway, then jams. You can't get Mum's things in until the door opens. You can work at it slowly and hope. Or run down and find the caretaker to sort it.",
  "B1": "You try the new key, and it won't turn. It sticks halfway, then jams. You can't get Mum's things in until the door opens. You can work at it slowly and hope it gives. Or run down and find the caretaker to sort it out.",
  "B2": "You try the new key in the new lock, and it won't turn. It sticks halfway, then jams solid. You can't get a single one of Mum's things in until that door opens. You can work at it slowly and hope it gives. Or run down and find the caretaker to sort it out properly."},
  "c": ["Keep working the lock.", "Find the caretaker."]},
 30: {"t": {
  "A2": "The afternoon wears on, grey and cooling, the light dropping by the hour. One flat on the landing is dark and shut. On the stairs, your legs begin to shake. And there's a door propped open at the end, with a trolley just inside.",
  "B1": "The afternoon wears on, grey and cooling, the light dropping by the hour. One flat on the landing is dark and shut up. On the stairs, your legs begin to shake. And there's a door propped open at the end, with a trolley just inside it.",
  "B2": "The afternoon wears on, grey and cooling, the light dropping by the hour now. One flat on the landing is dark and shut up for good. On the stairs, your legs begin to shake under the weight. And there's a door propped open at the end of the landing, with a handy trolley just inside it."},
  "c": ["A neighbour with less.", "Press on.", "The stairs nearly beat you.", "The open door."]},
 31: {"t": {
  "A2": "A man on the landing has dropped a heavy box and can't lift it back. He's winded, holding his side. Stop, and you lose time you don't have. Don't, and he's stuck there with it, alone in the cold stairwell.",
  "B1": "A man on the landing has dropped a heavy box and can't lift it back. He's winded, holding his side. Stop, and you lose time you don't have. Don't, and he's stuck there with it, alone in the cold stairwell.",
  "B2": "A man on the landing has dropped a heavy box and can't lift it back up. He's winded, holding his side and wincing. Stop, and you lose time you simply don't have. Don't, and he's stuck there with it, alone in the cold stairwell, with no one else about. You have to decide, and fast."},
  "c": ["Help him up.", "You can't stop — the light."]},
 33: {"t": {
  "A2": "You carry on up and down, head down, breathing hard. Choices lie ahead. Bray may be near with his van. There's that knock at the door still to answer. Or you can just keep shifting the boxes.",
  "B1": "You carry on up and down the stairs, head down, breathing hard. Choices lie ahead. Bray may be near with his van. There's that knock at the door still to answer. Or you can just keep shifting the boxes.",
  "B2": "You carry on up and down the stairs, head down, breathing hard through it. Choices lie ahead of you. Bray may be near with his van and his offer. There's that knock at the door still to answer, nagging at you. Or you can simply keep shifting the boxes, one by one."},
  "c": ["Bray again.", "A face you know.", "The last of it.", "The ache gets to you."]},
 34: {"t": {
  "A2": "You help the man lift the box and carry it to his door. He catches his breath. 'Here,' he says, and presses a key into your hand. It opens the back gate, so you can bring the van close. 'Saves your legs,' he says. A small thing, freely given, and you take it and go on.",
  "B1": "You help the man lift the box and carry it to his door. He catches his breath. 'Here,' he says, and presses a key into your hand. It opens the back gate, so you can bring the van right up close. 'Saves your legs,' he says. A small thing — but freely given, and you take it and go on.",
  "B2": "You help the man lift the box and carry it the last few feet to his door. He catches his breath, leaning on the frame. 'Here,' he says, and presses a key into your hand. It opens the back gate, so you can bring the van right up to the stairs. 'Saves your legs,' he says, with a tired nod. A small thing — but freely given, and you take it and go on your way."},
  "c": ["On your way.", "He knows your sister."]},
 35: {"t": {
  "A2": "You can't stop now — but you can't just leave him, either. So you promise to send help soon. 'Hang on,' you say. 'Catch your breath — I'll send someone down.' You mean it, too. And then you turn and carry on.",
  "B1": "You can't stop now — but you can't just leave him, either. So you promise to send help soon. 'Hang on,' you say. 'Catch your breath — I'll send someone down to you.' You mean it, too. And then you turn and carry on.",
  "B2": "You can't stop now — but you can't simply leave him, either. So you promise to send help soon. 'Hang on,' you say, over your shoulder. 'Catch your breath — I'll send someone down to you.' You mean it, too; and then you turn and carry on up the stairs, carrying the weight of it."},
  "c": ["Knock up help for him.", "On up the stairs."]},
 36: {"t": {
  "A2": "You get one good thing going — you set up a chain on the stairs. One hands a box down, the next takes it, the next stacks it in the van. People breathe easier. It isn't the whole move. But it's real, and it's a good start.",
  "B1": "You get one good thing going — you set up a steady chain on the stairs. One hands a box down, the next takes it, the next stacks it in the van. People breathe easier. It isn't the whole move. But it's real, and it's a good start.",
  "B2": "You get one good thing going — you set up a steady chain on the stairs. One hands a box down, the next takes it, the next stacks it tight in the van. People breathe easier with a system. It isn't the whole move, not by a long way. But it's real, and it's a good start, and the stairwell hums with it."},
  "c": ["Get everyone a job.", "Turn worry into work."]},
 37: {"t": {
  "A2": "Hand by hand, the panic turns into a working chain. Everyone has a job now: one lifts, one carries, one packs the van tight. Worry turns into doing. And doing beats worrying, every time. The stairwell fills with footsteps and quiet, steady work.",
  "B1": "Hand by hand, the panic turns into a working chain. Everyone has a job now: one lifts, one carries, one packs the van tight. Worry turns into doing. And doing beats worrying, every single time. The stairwell fills with footsteps and quiet, steady work.",
  "B2": "Hand by hand, box by box, the panic turns into a working chain. Everyone has a job now: one lifts, one carries down, one packs the van tight. Worry turns into doing — and doing beats worrying, on a moving day, every single time. The stairwell fills with footsteps and quiet, steady work, and the worst of the panic lifts."},
  "c": ["Back to the stairs.", "The last load soon."]},
 38: {"t": {
  "A2": "The long afternoon wears at you. A voice says: give up, leave the rest, finish tomorrow. No one would blame you, and it would be easy. But you think of Mum, home before dark. And you push the voice away. Not yet. Not while there's light.",
  "B1": "The long afternoon wears at you. A small voice says: give up, leave the rest, finish tomorrow — no one would blame you, and it would be so easy. But you think of Mum, home before dark. And you push the voice away. Not yet. Not while there's still light.",
  "B2": "The long afternoon wears at you. A small voice says: give up, leave the rest, finish it tomorrow — no one would blame you, and it would be so easy to do. But you think of Mum, home and settled before dark. And you push the voice away. Not yet. Not while there's still light in the sky."},
  "c": ["The last of it.", "Bray, one more time."]},
 39: {"t": {
  "A2": "You sit on a step a moment. You check the list of what's left. Half of it is done; the hard half isn't. You could push on and clear the rest. Or something makes you look down the stairs — and there, at the door, a face you half know.",
  "B1": "You sit on a step a moment and check the list of what's left. Half of it is done; the hard half isn't. You could push on and clear the rest. Or something makes you look down the stairs — and there, at the door below, a face you half know.",
  "B2": "You sit on a step a moment and check the list of what's left to shift. Half of it is done; the hard, heavy half isn't. You could push on and clear the rest before dark. Or something makes you look down the stairs — and there, at the door below, a face you half know, half dread."},
  "c": ["Push on.", "That face again."]},
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
    print(f"batch B: wrote prose for {len(D)} nodes")


if __name__ == "__main__":
    main()
