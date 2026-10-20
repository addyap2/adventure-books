#!/usr/bin/env python3
"""Phase 3 prose for The Interview (episode-10), batch D: Act II part 1, nodes 40-58.
Run: python3 scripts/generators/phase3_ep10_d.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-10.json")

D = {
 40: {"t": {
  "A2": "Reese leans in close, all friendly. 'Rough day,' he says. 'I've got it all — the questions, a reference, a name on the panel. Learn the lines and walk in, no one any the wiser. Why put yourself through this?' His smile is wide. But his eyes don't smile with it.",
  "B1": "Reese leans in close, all friendly. 'Rough day,' he says. 'I've got it all — the questions, a reference, a name on the panel. Learn the lines and walk in, and no one's any the wiser. Why put yourself through this?' His smile is wide. But his eyes don't smile with it.",
  "B2": "Reese leans in close, all friendly. 'Rough day,' he says. 'I've got it all — the questions in advance, a glowing reference, a friendly name on the panel. Learn the lines and walk in, and no one's ever any the wiser. Why put yourself through all this?' His smile is wide and easy. But his eyes don't smile along with it, and you notice that."},
  "c": ["Hear his price.", "Say no and walk on."]},
 41: {"t": {
  "A2": "'Fair price,' Reese says, and names a sum that makes you blink. It's a lot. But he's quick, he's sure, and he's right here. No sweat, no nerves, no risk of a blank. So: pay him, turn him down, or ask him straight what his game is?",
  "B1": "'Fair price,' Reese says, and names a sum that makes you blink. It's a lot of money. But he's quick, he's sure, and he's right here in front of you. No sweat, no nerves, no risk of a blank. So what's it to be — pay him, turn him down, or ask what his game is?",
  "B2": "'Fair price,' Reese says, and names a sum that makes you blink in the rain. It's a lot of money, more than you've got spare. But he's quick, he's sure of himself, and he's right here in front of you now. No sweat, no nerves, no risk of a blank in the room. So what's it to be — pay him, turn him down flat, or ask him straight out what his game really is?"},
  "c": ["Pay him.", "Turn him down.", "Ask him straight.", "Watch who else pays."]},
 42: {"t": {
  "A2": "You say no thanks and walk on. It feels good to turn him down. He calls after you, but you don't look back. His sort always find someone. But it won't be you, not today.",
  "B1": "You say no thanks and walk on past him. It feels good to turn him down. He calls something after you, but you don't look back. His sort always find someone, in the end. But it won't be you, not today.",
  "B2": "You say no thanks and walk on past him into the rain. It feels good to turn him down flat. He calls something after you, but you don't look back. His sort always find someone, in the end — someone tired and frightened enough. But it won't be you, not today."},
  "c": ["On the way.", "To the print shop instead."]},
 43: {"t": {
  "A2": "You take his papers and hand over the money. Your hand closes on the envelope, and part of you already knows. His smile grows. 'Smart move,' he says. But it doesn't feel smart. It feels like a small lie starting.",
  "B1": "You take his papers and hand over the money. Your hand closes on the envelope, and part of you already knows. His smile grows. 'Smart move,' he says. But it doesn't feel smart at all. It feels like a small lie, just starting.",
  "B2": "You take his papers and hand over the money. Your hand closes on the envelope, and part of you already knows the truth of it. His smile grows. 'Smart move,' he says. But it doesn't feel smart at all. It feels, in the cold, like a small lie being told — one you'll have to keep telling in that room."},
  "c": ["Learn the lines.", "A bad feeling already."]},
 44: {"t": {
  "A2": "You ask him straight: why so keen to help? He laughs. 'Easy money, friend,' he says. 'Flop today, and you'll be back to me next time.' He's honest, at least. That tells you all you need to know.",
  "B1": "You ask him straight: why is he so keen to help? He laughs. 'Easy money, friend,' he says. 'Flop today, and you'll be back to me next time.' He laughs again. At least he's honest — and that tells you all you need to know.",
  "B2": "You ask him straight out: why is he so keen to help? He laughs, quite openly. 'Easy money, friend,' he says. 'Flop today, and you'll be back to me next time, won't you.' He laughs again. At least he's honest — and that, right there, tells you everything you need to know."},
  "c": ["That's your answer — no.", "Take it anyway."]},
 45: {"t": {
  "A2": "You try to learn his lines on the way. But up close they're all wrong — stiff, false, nothing like you. They won't hold up for a second across that table. The whole thing already feels like a mistake.",
  "B1": "You try to learn his lines on the way. But up close they're all wrong — stiff, false, nothing like the way you talk. They won't hold up for a second across that table. The whole thing already feels like a mistake.",
  "B2": "You try to learn his lines on the way there. But up close they're all wrong — stiff, false, nothing at all like the way you actually talk. They won't hold up for a second across that table, under real questions. And the whole thing already feels, in your stomach, like a mistake."},
  "c": ["Try to make it fit.", "Into the room with it."]},
 46: {"t": {
  "A2": "You open the envelope, and your heart sinks. A half-real reference, a name spelled wrong, answers to the wrong job. This won't pass in the room for a minute. You paid good money, and it's worthless. The bad feeling in your gut was right.",
  "B1": "You open the envelope, and your heart sinks — a half-real reference, a name spelled wrong, answers to the wrong job. This won't pass in the room for a minute. You paid good money for it, and it's worthless. The bad feeling in your gut was right all along.",
  "B2": "You open the envelope, and your heart sinks right through the floor — a half-real reference, a name spelled wrong, answers to the wrong job entirely. This won't pass in that room for a single minute. You paid good money for it, out here in the rain, and it's worthless. The bad feeling in your gut was right about him all along."},
  "c": ["Into the room anyway.", "Go back and have words."]},
 47: {"t": {
  "A2": "You turn to find Reese, but he's already gone, off into the crowd. He was never really helping. He just wanted the sale, and you flustered so you'd come back. You've been had, plain and simple.",
  "B1": "You turn to find Reese, but he's already gone, off into the crowd. He was never really helping you. He just wanted the sale — and you flustered, so you'd come back to him. You've been had, plain and simple.",
  "B2": "You turn to find Reese, but he's already gone, melted off into the crowd. He was never really helping you at all. He just wanted the sale — and you flustered and shaken, so you'd be back to him next time. You've been had, out here, plain and simple. The rain keeps on, and the money's gone with him."},
  "c": ["Into the room, fooled.", "Bin the lot."]},
 48: {"t": {
  "A2": "He's gone, and the street is empty. Just the rain now, and the money you gave him for nothing. You learned something today. And you paid too much for it. Now you go on with less than you had.",
  "B1": "He's gone, and the street is empty — just the rain now, and the money you handed him for nothing. You learned something today. And you paid far too much for it. Now you go on with less than you started with.",
  "B2": "He's gone, and the street is empty — just the rain now, the cold, and the money you handed him for nothing at all. You learned something today, out here. And you paid far too much for it. Now you go on with less than you started with, and the clock no kinder."},
  "c": ["On to the office.", "Stand a moment in the rain."]},
 49: {"t": {
  "A2": "Other nervous people are paying Reese too, cash in hand, glad of the easy way. He takes it slow, with that same smile. He only helps the ones who pay the most.",
  "B1": "Other nervous people are paying Reese too — cash in hand, glad of the easy way out. He takes it slow, with that same smile. He only ever helps the ones who can pay the most.",
  "B2": "Other nervous people are paying Reese too — cash in hand, glad of any easy way out today. He takes it slow, unhurried, with that same wide smile. He only ever helps the ones who can pay him the most — and you see the whole of him in it. And you want no part of it."},
  "c": ["Hear his price anyway.", "Say no and walk on."]},
 50: {"t": {
  "A2": "You're halfway through the crush now, past most of the queue. The gate looks close — or does it? The crowd and the noise play tricks. And you're a long way from where you should be.",
  "B1": "You're halfway through the crush now, past most of the queue. The gate looks close — or does it? The crowd and the noise play tricks on you. And you're a long way from where you should be.",
  "B2": "You're halfway through the crush now, shoved past most of the queue. The gate looks close — or does it? The crowd and the noise and the shouting play tricks on your nerves. And you're a long way from where you should be, out of line, exposed. You keep your eyes down and your feet moving."},
  "c": ["Almost through.", "A guard steps out."]},
 51: {"t": {
  "A2": "A guard steps out of the crowd, straight at you, his hand up. This is the moment. You can push on and hope he lets it go. Or you can step back into the line, while you still can.",
  "B1": "A guard steps out of the crowd, straight at you, his hand up. This is the moment. You can push on and hope he lets it go. Or you can step back into the line, while you still can.",
  "B2": "A guard steps out of the crowd, straight at you, his hand raised. This is the moment, and it's a short one. You can push on and hope he lets it go. Or you can step back into the line, right now, while you still can. There is no third way out of this one."},
  "c": ["You don't make it.", "Step back while you can."]},
 52: {"t": {
  "A2": "You get through at last, heart going hard — but through. Somehow you made it. Now you must choose. Push on, rattled as you are? Or go back for the bag you dropped in the crush?",
  "B1": "You get through at last, heart going hard — but through. Somehow you made it. Now you have to decide: push on, rattled as you are, or go back for the bag you dropped in the crush.",
  "B2": "You get through at last, your heart going hard against your ribs — but through. Somehow, against the odds, you made it. Now you have to decide: push on, rattled as you are, or go back for the bag you dropped in the crush behind you. Either way, the clock will not wait for you."},
  "c": ["Push on, rattled.", "You dropped your papers."]},
 53: {"t": {
  "A2": "You step back into the line just in time — the hard, right choice. The guard's eyes move on past you. You stand there, heart racing, but safe. The day isn't lost. But you've lost time you'll miss, and you'll go the long way now.",
  "B1": "You step back into the line just in time — the hard, right choice. The guard's eyes move on past you. You stand there, heart racing, but safe. The day isn't lost. But you've lost time you'll miss — and you'll go the long way now.",
  "B2": "You step back into the line just in time — the hard choice, and the right one. The guard's eyes move on past you, and away. You stand there, heart racing, but safe. The day isn't lost. But you've lost time you'll badly miss — and you'll go the long way round now, like you should have."},
  "c": ["The long way after all.", "Too rattled to go on."]},
 54: {"t": {
  "A2": "You try to help the lad calm down — slow his breathing, run through a question, find his feet. It helps a little. But he's got next to nothing ready, and you can't stay long. There's really only one thing you can do for him.",
  "B1": "You try to help the lad calm down — slow his breathing, run through a question, find his feet. It helps a little. But he's got next to nothing ready, and you can't stay long. There's really only one thing you can do for him.",
  "B2": "You try to help the lad calm down — slow his breathing, run through a question or two, help him find his feet again. It helps a little. But he's got next to nothing ready, and you can't stay long today. There's really only one thing left that you can do for him."},
  "c": ["Give him your notes.", "Promise to help, then go."]},
 55: {"t": {
  "A2": "You hand him your own notes, and his face changes. He grips them like a lifeline. The grey goes out of his cheeks. 'Thank you,' he says — then he tells you someone's been asking for you, up ahead.",
  "B1": "You hand him your own notes, and his face changes. He grips them like a lifeline. The grey goes out of his cheeks. 'Thank you,' he says — and then he tells you that someone's been asking for you, up ahead.",
  "B2": "You hand him your own notes, and his tired face changes all at once. He grips them like a lifeline. The grey goes out of his cheeks. 'Thank you,' he says, over and over — and then he tells you that someone's been asking for you, up ahead, by name."},
  "c": ["On, with less now.", "Ask who's asking."]},
 56: {"t": {
  "A2": "With your notes given away, your heart sinks a little. Now there's less in your own hand for the room. You gave it to help, and you'd do it again. But the clock doesn't care about that. It just keeps ticking.",
  "B1": "With your notes given away, your heart sinks a little. Now there's less in your own hand for the room. You gave it to help, and you'd do it again. But the clock doesn't care about any of that. It just keeps ticking on.",
  "B2": "With your notes given away, your heart sinks a little in your chest. Now there's that much less in your own hand for the room at two. You gave it away to help, and you'd do it again in a heartbeat. But the clock doesn't care about any of that. It just keeps ticking on toward the hour."},
  "c": ["Keep going, keep your head.", "A café offers a sit-down."]},
 57: {"t": {
  "A2": "Someone waves you into a warm café. 'Just five minutes,' they say. 'Sit down, dry off, have a cuppa.' It's warm in there. Your nerves beg you to stop. But five minutes can turn into twenty.",
  "B1": "Someone waves you into a warm café. 'Just five minutes,' they say. 'Sit down, dry off, have a cuppa.' It's warm and dry inside, and your frayed nerves beg you to stop. But five minutes like this can quietly turn into twenty.",
  "B2": "Someone waves you into a warm, bright café out of the rain. 'Just five minutes,' they say. 'Sit down, dry off, have a cuppa.' It's warm and dry in there, and your frayed nerves beg you to stop a while. But five minutes like this one can quietly turn into twenty, with the clock running."},
  "c": ["Warm up, then on.", "Say no, press on."]},
 58: {"t": {
  "A2": "You press on through the rain, cold and wet. Your bag is heavy, the clock in your head. Each step is a small effort now. But you keep them coming, one after another, toward the office and the room.",
  "B1": "You press on through the rain, cold and wet, your bag heavy, the clock ticking in your head. Each step is a small effort now. But you keep them coming, one after another, toward the office and the room.",
  "B2": "You press on through the rain, cold and wet to the skin, your bag heavy in your hand and the clock ticking loud in your head. Each step is a small effort on its own now. But you keep them coming, one after another after another, toward the office and the waiting room."},
  "c": ["The last stretch.", "On toward the office."]},
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
