#!/usr/bin/env python3
"""Phase 3 prose for The Interview (episode-10), batch A: Act I opening, nodes 1-26.
Run: python3 scripts/generators/phase3_ep10_a.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-10.json")

D = {
 1: {"t": {
  "A2": "It is one o'clock. The interview that could change everything is at two. You have been out of work for months. The rent is late, and your dad is counting on you. But your bag is a mess, one paper is missing, and the trains are down. Getting there is all on you now.",
  "B1": "It is one o'clock, and the interview that could change everything is at two. You have been out of work for months now. The rent is late, and your dad is counting on you. But your bag is a mess, the one paper you need is missing, and the trains are down. For the first time, getting there is all on you.",
  "B2": "It is one o'clock, and the interview that could change everything is at two. You have been out of work for months now, and it shows. The rent is late, and your dad — who always said you'd land on your feet — is counting on you. But your bag is a mess, the one paper you really need is missing, and the trains are down across the city. For the first time, getting there, as yourself and on time, is all on you."},
  "c": ["Take stock of what you have.", "Call someone for advice.", "Call home first."]},
 2: {"t": {
  "A2": "You look at what you have to work with. Your one good suit, the job advert, a pen, your phone. But the paper with the address and the time is gone. It is already past one, and the clock is loud in your head. You must decide what to do, and move fast.",
  "B1": "You look at what you have to work with. Your one good suit, the job advert, a pen, your phone. But the paper with the address and the time on it is gone. It's already past one, and the clock is loud in your head. You have to decide what to do, and move fast.",
  "B2": "You look at what you have to work with. Your one good suit, the printed job advert, a pen that still works, your phone. But the paper with the address and the time on it — the one thing you can't do without — is gone. It's already past one, and the clock is loud in your head. You have to decide what to do, and you have to move fast."},
  "c": ["Get ready and go.", "Stop and think.", "Your phone is nearly dead."]},
 3: {"t": {
  "A2": "You call an old workmate to ask what to do. The phone rings and rings. Then she picks up. She can't meet you — she's miles away. But she talks you through it, calmly. 'Be yourself,' she says. 'You've done the work. You can do this.' And somehow you start to believe her.",
  "B1": "You call an old workmate to ask what to do. The phone rings and rings, and then at last she picks up. She can't meet you — she's miles away. But she talks you through it, calmly, step by step. 'Be yourself,' she says. 'You've done the work. You can do this.' And somehow you start to believe her.",
  "B2": "You call an old workmate to ask what on earth to do. The phone rings and rings, and then at last she picks up. She can't meet you today — she's miles away across the country. But she talks you through it anyway, calmly, step by step. 'Be yourself,' she says. 'You've done the work. You can do this.' And somehow, hearing her, you start to believe it."},
  "c": ["Think it through.", "It's on you now."]},
 4: {"t": {
  "A2": "You call home first. Your dad picks up, and his voice steadies you at once. 'You'll be grand,' he says. But the clock is still running, and you are still not ready. Sitting on the phone won't get you there. You need your papers, a plan, and a clear head before you go.",
  "B1": "You call home first. Your dad picks up, and his voice steadies you at once. 'You'll be grand,' he says. But the clock is still running, and you're still not ready. Sitting on the phone won't get you there. You need your papers, a plan, and a clear head before you go.",
  "B2": "You call home first, before anything else. Your dad picks up, and his voice steadies you at once. 'You'll be grand,' he says, the way he always does. But the clock is still running, and you're still not ready. Sitting on the phone to him won't get you across the city. You need your papers, a plan, and a clear head before you so much as leave the flat."},
  "c": ["Take stock and go.", "It's on you now."]},
 5: {"t": {
  "A2": "You pull yourself together and get ready. You press your shirt, check your shoes, and breathe. Outside, the street is grey and wet. Then your phone buzzes — a message from a number you don't know. 'I can help you get that job,' it says. You weren't expecting anything like that.",
  "B1": "You pull yourself together and get ready to go. You press your shirt, check your shoes, and breathe. Outside, the street is grey and wet. Then your phone buzzes — a message from a number you don't know. 'I can help you get that job,' it says. You weren't expecting anything like that, not today.",
  "B2": "You pull yourself together and get ready to go. You press your shirt, check your shoes, and try to breathe slowly. Outside, the street is grey and wet and unhelpful. Then your phone buzzes — a message from a number you don't recognise. 'I can help you get that job,' it says, and nothing more. You weren't expecting anything like that, not today of all days."},
  "c": ["To the print shop.", "A stranger needs help.", "Stop and think.", "A stranger, lost."]},
 6: {"t": {
  "A2": "You make yourself stop and think. You could set off right now and sort the rest on the way. You could get your papers in order first. Or you could call round for help and a lift. Each choice costs time you don't have. And the clock keeps moving toward two.",
  "B1": "You make yourself stop and think. You could set off right now and sort the rest on the way. You could get your papers in order first. Or you could call round for help and a lift. Each choice costs time you don't have — and the clock keeps moving toward two.",
  "B2": "You make yourself stop and think for a moment. You could set off right now and sort the rest out on the way. You could get all your papers in order first, properly. Or you could call round for help and maybe a lift across town. Each choice costs time you don't have — and the clock keeps moving, steadily, toward two."},
  "c": ["To the print shop.", "Just set off.", "Call round for help."]},
 8: {"t": {
  "A2": "The time presses on you like a weight. You think of the panel waiting at two, of the late rent, of your dad's quiet hope. A whole new life rests on this one hour. That isn't a worry; it's a plain fact. No one else can walk in there for you. It is you, today, or no one.",
  "B1": "The time presses on you like a weight. You think of the panel waiting at two, of the late rent, of your dad's quiet hope. A whole new life rests on this one hour now. That isn't a worry; it's a plain fact. No one else can walk in there for you. It's you, today, or no one.",
  "B2": "The time presses down on you like a weight. You think of the panel waiting at two o'clock, of the late rent, of your dad's quiet, stubborn hope. A whole new life rests on this one hour now. That isn't a worry; it's a plain fact. No one else can walk into that room for you. It's you, today, or it's no one."},
  "c": ["Stop and think.", "To the print shop.", "A crush at the station."]},
 11: {"t": {
  "A2": "You just set off, fast and half-ready. You grab your bag and go. But you've no real plan, and half your papers are loose in your hand. Rushing like this, it won't come together on its own. You can't just turn up and hope for the best.",
  "B1": "You just set off, fast and half-ready. You grab your bag and go. But you've no real plan, and half your papers are still loose in your hand. Rushing like this, it won't come together on its own. You can't just turn up and hope for the best.",
  "B2": "You just set off, fast and only half-ready. You grab your bag and go out the door. But you've no real plan, and half your papers are still loose in your hand, flapping in the wind. Rushing headlong like this, it won't come together on its own. You can't simply turn up at the door and hope for the best."},
  "c": ["On your way across town.", "The rush catches up."]},
 13: {"t": {
  "A2": "You take charge of yourself and your papers. You lay it all out: your CV, the advert, your notes, the address. Done well, this is a real shot at the job. Rushed or half-done, and you walk in with nothing. So you take a breath and get it right, carefully.",
  "B1": "You take charge of yourself and your papers. You lay it all out on the table: your CV, the advert, your notes, the address. Done well, this is a real shot at the job. Rushed or half-done, and you walk in with nothing. So you take a breath and get it right, carefully.",
  "B2": "You take charge of yourself and your papers. You lay it all out neatly on the table: your CV, the printed advert, your notes, the address. Done well, this gives you a real, honest shot at the job. Rushed or half-done, and you walk into that room with nothing to stand on. So you take a slow breath and get it right, carefully, one thing at a time."},
  "c": ["On your way.", "Ask an old hand first."]},
 14: {"t": {
  "A2": "You grab just the essentials — your CV and your phone — and go. It feels good to be moving at last. But it isn't a plan, and you've left things behind. You'll still need the rest, and soon. If not, you'll stand in that room with empty hands.",
  "B1": "You grab just the essentials — your CV and your phone — and go. It feels good to be moving at last. But it isn't a plan, and you've left things behind. You'll still need the rest, and soon. If not, you'll be standing in that room with empty hands.",
  "B2": "You grab just the bare essentials — your CV and your phone — and go. It feels good to be moving at last, after all the panic. But it isn't a plan, and you've left real things behind. You'll still need the rest, and soon. If you don't go back for them, you'll be standing in that room with empty hands and nothing to show."},
  "c": ["On your way.", "Ask an old hand first."]},
 15: {"t": {
  "A2": "Old Frank trained you years back, and he's seen it all. 'Don't cut the line to save time,' he says. 'It's not worth it — they always see.' He warns you about Reese too, the fixer. 'Walk in as yourself. Answer straight, stay calm. That's the whole job today.'",
  "B1": "Old Frank trained you years back, and he's seen it all in his time. 'Don't cut the line to save ten minutes,' he says. 'It's not worth it — they always see.' He warns you about Reese too, the fixer. 'Walk in as yourself. Answer straight, stay calm. That's the whole job today.'",
  "B2": "Old Frank trained you years back, and he's seen it all in his long time. 'Don't ever cut the line to save ten minutes,' he says. 'It's not worth it — they always see, in the end.' He warns you about Reese too, the fixer who works the station. 'Walk in as yourself. Answer straight, stay calm, and don't pretend. That's the whole job today.'"},
  "c": ["Take his words to heart.", "On your way."]},
 16: {"t": {
  "A2": "You stop and help the stranger. He's an older man who's dropped his bag and papers all over the wet path. You gather them up and walk him to a dry seat. Little by little he calms down. 'Thank you,' he says, gripping your hand. You point him on his way, then turn back to the clock.",
  "B1": "You stop and help the stranger — an older man who's dropped his bag and his papers all over the wet path. You gather them up and walk him to a dry seat. Little by little he calms down. 'Thank you,' he says, gripping your hand. You point him on his way, then turn back to your own morning and the clock.",
  "B2": "You stop and help the stranger — an older man who's dropped his bag and his papers all over the wet path, and can't quite manage them. You gather them up and walk him to a dry seat. Little by little he calms down and catches his breath. 'Thank you,' he says, gripping your hand hard. You point him on his way, then turn back to your own morning and the running clock."},
  "c": ["On, feeling steadier.", "Call round for help."]},
 17: {"t": {
  "A2": "Getting there comes first. The rest can wait a moment. But you still have to choose how. You could stop at the print shop for what you need first. Or you could set off now and sort the rest as you go.",
  "B1": "Getting there comes first. The rest can wait a moment. But you still have to choose how. You could stop at the print shop for what you need first. Or you could set off now and sort the rest out as you go.",
  "B2": "Getting there on time comes first. Everything else can wait a moment. But you still have to choose how to do it. You could stop at the print shop for what you need first, and go in prepared. Or you could set off right now and sort the rest out as you go along."},
  "c": ["To the print shop.", "Just set off."]},
 18: {"t": {
  "A2": "The rush catches up with you. Your hands shake, your heart races, and the clock won't stop. You're trying to do too much at once, and you know it. If you lose your head now, you'll lose the room. So slow down, breathe, one thing at a time.",
  "B1": "The rush catches up with you. Your hands shake, your heart races, and the clock won't stop. You're trying to do too much at once, and you know it. If you lose your head now, you'll lose the room. So slow down, breathe, and do one thing at a time.",
  "B2": "The rush finally catches up with you. Your hands shake, your heart races, and the clock will not stop for anyone. You're trying to do far too much at once, and you know it. If you lose your head now, out here, you'll lose the room later. So slow down, breathe, and do just one thing at a time."},
  "c": ["Reese steps in.", "On your way."]},
 19: {"t": {
  "A2": "You call round, and people come through. One texts you the address. One offers a lift. One sends a kind word to steady your nerves. Bit by bit, you're not so alone. You still walk in by yourself. But now the getting-there isn't all on you — and that changes things.",
  "B1": "You call round, and people come through for you. One texts you the address. One offers a lift across town. One sends a kind word to steady your nerves. Bit by bit, you're not so alone in this. You still walk in by yourself. But now the getting-there isn't all on you — and that changes everything.",
  "B2": "You call round, and people come through for you, one by one. One texts you the address. One offers a lift across town. One sends a kind word just to steady your nerves. Bit by bit, you're not nearly so alone in this. You'll still have to walk into that room by yourself. But now the getting-there isn't all on your shoulders — and that changes everything."},
  "c": ["In the waiting room.", "Steady the room."]},
 20: {"t": {
  "A2": "No one can help. One is at work, one is far away, one just doesn't pick up. You can't make them. So you square your shoulders and go on alone. It's harder this way. But the interview is at two, ready or not.",
  "B1": "No one can help. One is at work, one is far away, one just doesn't pick up the phone. You can't make them. So you square your shoulders and go on alone. It's harder this way. But the interview is at two, ready or not.",
  "B2": "No one can help you today. One is stuck at work, one is far away, one simply doesn't pick up the phone. You can't make them, and you don't try. So you square your shoulders and go on alone. It's a good deal harder this way. But the interview is at two o'clock, ready or not."},
  "c": ["To the print shop.", "Just set off."]},
 21: {"t": {
  "A2": "You're on your way across the city. To reach the office in time, you have to cross town. There are two ways. The long way round is safe but slow. Cutting through and jumping the queue is quick. But it's risky, and people are watching.",
  "B1": "You're on your way across the city. To reach the office in time, you have to cross town. There are two ways there. The long way round is safe but slow. Cutting through and jumping the queue is quick. But it's risky, and people are watching.",
  "B2": "You're on your way across the city at last. To reach the office in time now, you have to cross the whole of town. There are two ways to do it. The long way round is safe but slow. Cutting through and jumping the queue up front is quick. But it's risky, and there are always people watching."},
  "c": ["The long, safe way.", "The quick way — cut through.", "Reese is here."]},
 22: {"t": {
  "A2": "You take old Frank's words to heart. Walk in as yourself. Answer straight. Don't trust Reese. And don't cut any corners. It's simple advice, and good. Now you just have to follow it, with the clock running down.",
  "B1": "You take old Frank's words to heart. Walk in as yourself. Answer straight. Don't trust Reese. And don't cut any corners to save time. It's simple advice, and good. Now you just have to follow it, with the clock running down.",
  "B2": "You take old Frank's words right to heart. Walk in as yourself. Answer straight and honestly. Don't trust Reese for a second. And don't cut any corners to save time. It's simple advice, and good advice. Now you just have to follow it, with the clock running down on you."},
  "c": ["On your way.", "To the print shop."]},
 23: {"t": {
  "A2": "You feel better for the good turn you did. Helping someone, oddly, seems to steady you too. Your head is clearer, your hands are surer. There's still a lot to face before two. But now you feel able to meet it.",
  "B1": "You feel better for the good turn you did. Helping someone, oddly, seems to steady you too. Your head is clearer now, your hands are surer. There's still a lot to face before two. But now you feel able to meet it.",
  "B2": "You feel better for the good turn you did back there. Helping someone, oddly enough, seems to steady you as much as them. Your head is clearer now, and your hands are surer. There's still a great deal to face before two o'clock. But now, somehow, you feel able to meet it."},
  "c": ["On your way.", "Call round for help."]},
 24: {"t": {
  "A2": "Reese falls into step beside you, all smiles. He has a way to get you the job, and he's glad to sell it. 'Why sweat it, friend?' he says. 'I've got the questions, a reference, a name to drop.' No one will ever know, he says. You've heard this kind of offer before.",
  "B1": "Reese falls into step beside you, all smiles. He has a way to get you the job, and he's glad to sell it. 'Why sweat it, friend?' he says. 'I've got the questions, a reference, a name to drop — no one will ever know.' You've heard this kind of offer before.",
  "B2": "Reese falls into step beside you, all easy smiles. He has a way to get you the job, and he's more than glad to sell it to you. 'Why sweat it, friend?' he says. 'I've got the questions in advance, a glowing reference, a name to drop — and no one will ever know.' You've heard this exact kind of offer before."},
  "c": ["Hear him out.", "Say no and walk on."]},
 25: {"t": {
  "A2": "In the waiting room, the other candidates sit stiff and silent. You break the ice — a small joke, a shared nerve. Slowly the room loosens up. 'You go next,' someone says, and you help each other get ready. It's a good feeling, with the clock running down.",
  "B1": "In the waiting room, the other candidates sit stiff and silent. You break the ice — a small joke, a shared nerve. Slowly the room loosens up. 'You go next,' someone says, and you help each other get ready. It's a good feeling, with the clock running down.",
  "B2": "In the waiting room, the other candidates sit stiff and silent, each alone with their nerves. You break the ice — a small joke, an honest word about how shared the fear is. Slowly the whole room loosens up. 'You go next,' someone says, and you start to help each other get ready. It's a good feeling, with the clock running down."},
  "c": ["On your way.", "Someone you recognise."]},
 26: {"t": {
  "A2": "The long way is cold and wet, the rain on your face, no shelter at all. But it's safe, and it gets you there. So you keep walking, as fast as you dare, step after step. The clock ticks, but your feet keep moving.",
  "B1": "The long way is cold and wet, the rain on your face, no shelter at all. But it's safe under your feet, and it gets you there. So you keep walking, as fast as you dare, step after step. The clock ticks, but your feet keep moving.",
  "B2": "The long way round is cold and wet, the rain full in your face, no shelter at all along it. But it's safe under your feet, and it gets you there in the end. So you keep walking, as fast as you dare, step after step after step. The clock ticks on, but your feet keep moving."},
  "c": ["The street goes on.", "Someone has fallen.", "You stop and look up."]},
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
    print(f"batch A: wrote prose for {len(D)} nodes")


if __name__ == "__main__":
    main()
