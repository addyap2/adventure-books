#!/usr/bin/env python3
"""Phase 3 prose for The Interview (episode-10), batch B: rest of Act I, nodes 28-39.
Run: python3 scripts/generators/phase3_ep10_b.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-10.json")

D = {
 28: {"t": {
  "A2": "You push into the front of the queue, past everyone waiting. At once it feels wrong. People glare and mutter, and a guard turns his head. Every step forward is a gamble now. And there's no going back once you've jumped the line.",
  "B1": "You push into the front of the queue, past everyone waiting. At once it feels wrong. People glare and mutter, and a guard turns his head your way. Every step forward is a gamble now — and there's no going back once you've jumped the line.",
  "B2": "You push your way into the front of the queue, past everyone patiently waiting. At once it feels wrong, deep down. People glare and mutter, and a guard turns his head slowly your way. Every step forward is a gamble now — and there's no going back once you've jumped the line in front of them all."},
  "c": ["Almost through.", "A guard steps out."]},
 29: {"t": {
  "A2": "Your phone blinks red and dies in your hand — no map, no address, no tickets. You can still ask people the way, but it's slow, and the clock is loud. You'll have to manage without it. Or dash to the print shop and sort it out there.",
  "B1": "Your phone blinks red and dies in your hand — no map, no address, no tickets. You can still ask people the way, but it's slow, and the clock is loud. You'll have to manage without it. Or dash to the print shop and sort it all out there.",
  "B2": "Your phone blinks red and dies right in your hand — no map, no address, no tickets, nothing. You can still ask people the way, but it's slow going, and the clock is loud in your ears. You'll have to manage without it somehow. Or dash to the print shop and sort it all out there, properly."},
  "c": ["Push on regardless.", "To the print shop."]},
 30: {"t": {
  "A2": "The street goes on, cold and wet, the rain coming harder. One shop sits dark and shut. Ahead, the wind pushes back at you. And there's a café on the corner, warm and bright through the glass.",
  "B1": "The street goes on, cold and wet, the rain coming harder by the minute. One shop sits dark and shut. Ahead, the wind pushes back at you. And there's a café on the corner, warm and bright through the fogged glass.",
  "B2": "The street goes on and on, cold and wet, the rain coming harder by the minute now. One shop sits dark and shut up for the day. Ahead of you, the wind pushes back with every step. And there's a café on the corner, warm and bright through the fogged-up glass, pulling at you."},
  "c": ["Someone in real trouble.", "Press on.", "The rain nearly beats you.", "The café's warm glow."]},
 31: {"t": {
  "A2": "A young woman has slipped on the wet steps and spilled her things everywhere. She's shaken and near tears. Stop, and you lose time you don't have. Don't, and she's left there alone in the rain.",
  "B1": "A young woman has slipped on the wet steps and spilled her things everywhere. She's shaken and near tears. Stop, and you lose time you don't have. Don't, and she's left there alone in the cold rain.",
  "B2": "A young woman has slipped on the wet steps and spilled her things everywhere across the pavement. She's shaken, and near tears with it. Stop, and you lose time you simply don't have. Don't, and she's left there alone in the cold rain, with no one else about to help."},
  "c": ["Help her up.", "You can't stop — the time."]},
 33: {"t": {
  "A2": "You hurry on through the cold and the rain, head down. Choices lie ahead. Reese may be near. There's that strange message still to think about. Or you can just keep moving toward the office.",
  "B1": "You hurry on through the cold and the rain, head down against it. Choices lie ahead. Reese may be near. There's that strange message still to think about. Or you can just keep moving toward the office.",
  "B2": "You hurry on through the cold and the rain, head down against the worst of it. Choices lie ahead of you. Reese may be near with his offer. There's that strange message still to think about, nagging at you. Or you can simply keep moving toward the office and the clock."},
  "c": ["Reese again.", "A face you know.", "The last stretch.", "The nerves get to you."]},
 34: {"t": {
  "A2": "You help the young woman up and gather her things. Her eyes fill. She presses a card into your hand — a name at the very firm you're headed to. 'Ask for her,' she says. 'Tell her I sent you.' A small thing, freely given. You take it and go on.",
  "B1": "You help the young woman up and gather her things. Her eyes fill. She presses a card into your hand — a name at the very firm you're headed to. 'Ask for her,' she says. 'Tell her I sent you.' A small thing — but freely given, and you take it and go on.",
  "B2": "You help the young woman up and gather her scattered things. Her eyes fill with relief. She presses a small card into your hand — a name at the very firm you're headed to. 'Ask for her,' she says. 'Tell her I sent you.' A small thing — but freely given, in the rain, and you take it and go on your way."},
  "c": ["On your way.", "She knows the panel."]},
 35: {"t": {
  "A2": "You can't stop now — but you can't just leave her, either. So you promise to send help soon. 'Hang on,' you say. 'Stay here, stay dry — someone will come.' You mean it, too. And then you turn and go.",
  "B1": "You can't stop now — but you can't just leave her, either. So you promise to send help soon. 'Hang on,' you say. 'Stay here, stay dry — someone will come for you.' You mean it, too. And then you turn and go.",
  "B2": "You can't stop now — but you can't simply leave her there, either. So you promise to send help soon. 'Hang on,' you say, over the rain. 'Stay here, stay dry — someone will come for you.' You mean it, too; and then you turn and go, carrying the weight of it with you."},
  "c": ["Call someone for her.", "On through the rain."]},
 36: {"t": {
  "A2": "You get one good thing going — you help calm the whole waiting room at once. People breathe easier. Someone shares water, someone shares a laugh. It isn't the interview itself. But it's real, and it's a start.",
  "B1": "You get one good thing going — you help calm the whole waiting room at once. People breathe easier around you. Someone shares water, someone shares a laugh. It isn't the interview itself. But it's real, and it's a good start.",
  "B2": "You get one good thing going — you help calm the whole tense waiting room at once. People breathe easier around you now. Someone shares a bottle of water, someone shares a nervous laugh. It isn't the interview itself, not by a long way. But it's real, and it's a good start, and the room feels warmer for it."},
  "c": ["Help each one get ready.", "Turn nerves into doing."]},
 37: {"t": {
  "A2": "Person by person, the panic turns into a calm room. People have focus now: one reads notes, one breathes slow, one cheers the next in. Worry turns into doing. And doing beats worrying, every time. The room fills with a quiet, steady warmth.",
  "B1": "Person by person, the panic turns into a calm room. People have focus now: one reads notes, one breathes slow, one cheers the next one in. Worry turns into doing. And doing beats worrying, every single time. The room fills with a quiet, steady warmth.",
  "B2": "Person by person, nerve by nerve, the panic turns into a calm room. People have focus now: one reads over notes, one breathes slow, one quietly cheers the next one in. Worry turns into doing — and doing beats worrying, in a waiting room, every single time. The room fills with a quiet, steady warmth, and the worst of the fear lifts."},
  "c": ["Back out and on.", "Your turn soon."]},
 38: {"t": {
  "A2": "The long morning wears at you. A voice says: give up, go home, tell them you were ill. No one would blame you, and it would be easy. But you think of your dad's face, and the room at two. And you push the voice away. Not yet.",
  "B1": "The long morning wears at you. A small voice says: give up, go home, tell them you were ill — no one would blame you, and it would be so easy. But you think of your dad's face, and the room at two. And you push the voice away. Not yet. Not while it can still go right.",
  "B2": "The long morning wears at you. A small voice says: give up, go home, tell them you were ill — no one would blame you, and it would be so easy to do. But you think of your dad's face, and the room waiting at two. And you push the voice away. Not yet. Not while this can still go right."},
  "c": ["The last stretch.", "Reese, one more time."]},
 39: {"t": {
  "A2": "You duck under a café awning to read your notes again. Half the ink has run in the rain. You could push on and trust what you remember. Or something makes you look up — and across the street, a face you half know.",
  "B1": "You duck under a café awning to read your notes again. Half the ink has run in the rain. You could push on and trust what you remember. Or something makes you look up — and there, across the street, a face you half know.",
  "B2": "You duck under a café awning to read your notes one more time. Half the ink has run and smudged in the rain. You could push on and trust what you remember. Or something makes you look up — and there, across the wet street, a face you half know, half dread."},
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
