#!/usr/bin/env python3
"""Phase 3 prose for The Dinner (episode-09), batch B: rest of Act I, nodes 28-39.
Run: python3 scripts/generators/phase3_ep09_b.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-09.json")

D = {
 28: {"t": {
  "A2": "You step out into the main road, and at once it feels wrong. The cars come fast out of the dark and rain. Every step is a gamble now. And there is no going back once you are out in the traffic.",
  "B1": "You step out into the main road, and at once it feels wrong. The cars come fast out of the dark and the rain, their lights in your eyes. Every step is a gamble now — and there's no going back once you're out in the traffic.",
  "B2": "You step out into the main road, and at once it feels wrong. The cars come fast out of the dark and the rain, headlights swinging straight into your eyes. Every single step is a gamble now — and there's no going back once you're out in the middle of the traffic."},
  "c": ["Keep going.", "A car comes out of nowhere."]},
 29: {"t": {
  "A2": "The oven clicks and clicks but won't light. The gas must be low. You can cook on the hob, but it is slow, and there is a lot to do. You'll have to make do. Or nip to the shop and sort it there.",
  "B1": "The oven clicks and clicks but won't light — the gas must be low. You can still cook on the hob, but it's slow, and there's a lot to get through. You'll have to make do with it. Or nip down to the shop and sort it out there.",
  "B2": "The oven clicks and clicks but won't light — the gas must be running low. You can still cook on the hob, but it's slow going, and there's a great deal to get through before seven. You'll have to make do with it — or nip down to the corner shop and sort it out there."},
  "c": ["Make do on the hob.", "To the shop — sort it there."]},
 30: {"t": {
  "A2": "The street runs on, cold and wet, the rain coming harder. One house sits dark, with no one home. Ahead, the wind pushes at you. And there is a shop sign at the corner, half torn down in the rain.",
  "B1": "The street runs on, cold and wet, the rain coming harder by the minute. One house sits dark, with no one home. Ahead, the wind pushes back at you. And there's a shop sign at the corner, half torn down in the rain.",
  "B2": "The street runs on, cold and wet, the rain coming harder by the minute now. One house sits dark along it, with no lights and no one home. Ahead, the wind pushes back at you with every step. And there's a shop sign at the corner, half torn down and swinging in the rain."},
  "c": ["A neighbour with no dinner.", "Press on.", "The rain nearly beats you.", "The half-torn sign."]},
 31: {"t": {
  "A2": "An old man has slipped on the wet pavement and can't get up. The cold is getting into him. Stop, and you lose time you don't have. Don't, and he could be there a while.",
  "B1": "An old man has slipped on the wet pavement and can't get up. The cold is getting into him fast. Stop, and you lose time you don't have. Don't, and he could be stuck there a long while in the rain.",
  "B2": "An old man has slipped on the wet pavement and can't get himself up. The cold is getting into him fast, there on the ground. Stop, and you lose time you don't have; don't, and he could be stuck there a long while in the rain, with no one else about."},
  "c": ["Help him up.", "You can't stop — the dinner."]},
 33: {"t": {
  "A2": "You hurry on through the cold and the rain, head down. Choices lie ahead. Dale may be near. There is that knock at the gate. Or you can just get on with the dinner.",
  "B1": "You hurry on through the cold and the rain, head down against it. Choices lie ahead. Dale may be near. There's that soft knock at the gate to think about. Or you can just get on with the dinner.",
  "B2": "You hurry on through the cold and the rain, head down against the worst of it. Choices lie ahead of you in the dark. Dale may be near with his bags. There's that soft knock at the gate still to think about. Or you can simply get on with the dinner and the clock."},
  "c": ["Dale again.", "The knock at the gate.", "The last stretch.", "The tiredness gets to you."]},
 34: {"t": {
  "A2": "You help the old man up and walk him to his door. His eyes fill. He presses a bag into your hands — fresh herbs from his window box. 'Take them,' he says, 'for the dinner.' A small thing, freely given. You take it and go on.",
  "B1": "You help the old man up and walk him to his door. His eyes fill. He presses a small bag into your hands — fresh herbs from his window box. 'Take them,' he says, 'for your dinner.' A small thing — but freely given, and you take it and go on.",
  "B2": "You help the old man up and walk him safely to his door. His eyes fill, and he presses a small paper bag into your hands — fresh herbs from his window box. 'Take them,' he says, 'for your dinner.' A small thing — but freely given, in the rain, and you take it and go on your way."},
  "c": ["On your way.", "He tells you about the knock at your gate."]},
 35: {"t": {
  "A2": "You can't stop now. But you can't just leave them, either. So you promise to send help round soon. 'Hang on,' you say. 'Stay warm, stay put — I won't forget you.' You mean it, too. And then you go.",
  "B1": "You can't stop now — but you can't just leave them, either. So you promise to send help round soon. 'Hang on,' you say. 'Stay warm, stay put — I won't forget you.' You mean it, too. And then you turn and go.",
  "B2": "You can't stop now — but you can't simply leave them, either. So you promise to send help round soon. 'Hang on,' you say, over the rain. 'Stay warm, stay put — I won't forget you.' You mean it, too; and then you turn and go, carrying the weight of it with you."},
  "c": ["Call the neighbours.", "On through the rain."]},
 36: {"t": {
  "A2": "You and the friends get one big pot going — a warm stew that will feed everyone. People gather round the warm hob. It is not the whole dinner. But it is real food, and a start.",
  "B1": "You and the friends get one big pot going — a warm stew that will feed everyone, whatever else happens. People gather round the warm hob. It isn't the whole dinner. But it's real food, and a good beginning.",
  "B2": "You and the friends get one big pot going — a warm, simple stew that will feed everyone, whatever else happens with the clock. People gather round the warm hob, glad of it. It isn't the whole dinner, not by a long way. But it's real food, and a good beginning, and the kitchen smells of it."},
  "c": ["Get the rest cooking too.", "Fetch more hands."]},
 37: {"t": {
  "A2": "Friend by friend, the panic turns into a working kitchen. People have jobs now: one peels, one stirs, one lays the table. Worry turns into doing. And doing beats worrying, every single time. The kitchen fills up with noise and warmth.",
  "B1": "Friend by friend, the panic turns into a working kitchen. People have jobs now: one peels, one stirs, one lays the table. Worry turns into doing. And doing beats worrying, every single time. The kitchen fills up with noise and warmth.",
  "B2": "Friend by friend, task by task, the panic turns into a working kitchen. People have jobs now: one peels the potatoes, one stirs a pot, one lays the table under your eye. Worry turns into doing — and doing beats worrying, in a kitchen, every single time. The kitchen fills up with noise and warmth, and the worst of the panic lifts."},
  "c": ["To the shop for the rest.", "The last stretch."]},
 38: {"t": {
  "A2": "The long evening wears at you. A voice says: give up, order a takeaway, put your feet up. No one would blame you, and it would be easy. But you think of Gran's face at a full table. And you push the voice away. Not yet.",
  "B1": "The long evening wears at you. A small voice says: give up, order a takeaway, put your feet up — no one would blame you, and it would be so easy. But you think of Gran's face at a full table. And you push the voice away. Not yet. Not while it can still be good.",
  "B2": "The long evening wears at you. A small voice says: give up, order a takeaway, put your feet up — no one would blame you, and it would be so easy to do. But you think of Gran's face coming down to a full, warm table. And you push the voice away. Not yet. Not while the evening can still be good."},
  "c": ["The last stretch.", "Dale at the door."]},
 39: {"t": {
  "A2": "You stop under a lamp to read the rest of Gran's list. Half of it is smudged by the rain. You could push on to the shop for the rest. Or something makes you look back at the gate, and that soft knock.",
  "B1": "You stop under a street lamp to read the rest of Gran's list. Half of it is smudged by the rain. You could push on to the shop and get the rest. Or something makes you look back at the gate, and that soft knock you heard.",
  "B2": "You stop under a street lamp to read the rest of Gran's list, but half of it is smudged and run by the rain. You could push on to the shop and get the last few things. Or something makes you look back, down the dark street, toward the gate and that soft knock you heard earlier."},
  "c": ["On to the shop.", "Back to the gate."]},
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
