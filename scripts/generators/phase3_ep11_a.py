#!/usr/bin/env python3
"""Phase 3 prose for Moving Day (episode-11), batch A: Act I opening, nodes 1-26.
Run: python3 scripts/generators/phase3_ep11_a.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-11.json")

D = {
 1: {"t": {
  "A2": "It's gone two, and the light will fade by five. Today you move your mum, Edie, into her new flat. She can't do the stairs here any more. She sits among the boxes, waiting, her hands in her lap. The van is late, the new key is stiff, and one box has gone missing. Getting her home is all on you now.",
  "B1": "It's gone two, and the light will fade by five. Today you move your mum, Edie, into her new flat. She can't do the stairs in this place any more. She sits among the boxes, waiting, her hands in her lap. The van is late, the new key is stiff, and one box has gone missing. For the first time, getting her home is all on you.",
  "B2": "It's gone two o'clock, and the light will fade by five. Today you move your mum, Edie, into her new ground-floor flat. She can't manage the stairs in this old place any more. She sits among the half-packed boxes, waiting, her hands folded in her lap. The van is late, the new key is stiff in the lock, and one box has already gone missing. For the first time, getting her home before dark is all on you."},
  "c": ["See what's left to shift.", "Call for help.", "See to Mum first."]},
 2: {"t": {
  "A2": "You look at what's left to move. Mum's bed and her big chair, the last of the boxes, a few bags. But the box with your dad's things isn't where you left it. It's gone three now, and the light is turning. You have to decide what to do, and move fast.",
  "B1": "You look at what's left to move. Mum's bed and her big chair, the last of the boxes, a few bags. But the box with your dad's things isn't where you left it. It's gone three now, and the light is already turning. You have to decide what to do, and move fast.",
  "B2": "You look at what's left to move. Mum's bed and her big armchair, the last of the boxes, a few loose bags. But the box with your late dad's things — the photos, his watch — isn't where you left it. It's gone three now, and the light is already turning grey. You have to decide what to do, and you have to move fast."},
  "c": ["Start loading.", "Stop and think.", "The new key won't turn."]},
 3: {"t": {
  "A2": "You call an old mate to ask for a hand. The phone rings and rings. Then he picks up. He can't come — he's away for the day. But he talks you through it, calm. 'Load the heavy stuff low,' he says. 'Little and often. You'll get there.' And somehow you start to believe him.",
  "B1": "You call an old mate to ask for a hand. The phone rings and rings, and then at last he picks up. He can't come — he's away for the day. But he talks you through it, calm and clear. 'Load the heavy stuff low,' he says. 'Little and often. You'll get there.' And somehow you start to believe him.",
  "B2": "You call an old mate to ask for a hand. The phone rings and rings, and then at last he picks up. He can't come over — he's away for the whole day. But he talks you through it anyway, calm and clear. 'Load the heavy stuff low,' he says. 'Little and often, and mind your back. You'll get there.' And somehow, hearing him, you start to believe it."},
  "c": ["Think it through.", "It's on you now."]},
 4: {"t": {
  "A2": "You go to Mum first. You make her tea and settle her in her chair. 'Don't fuss over me,' she says, but her hand holds yours. The rooms are still full, though, and the light is going. Sitting with her won't shift the boxes. You need a plan, and a clear head, before you start.",
  "B1": "You go to Mum first. You make her tea and settle her in her chair. 'Don't fuss over me,' she says, but her hand holds on to yours. The rooms are still full, though, and the light is going. Sitting with her won't shift the boxes. You need a plan, and a clear head, before you start.",
  "B2": "You go to Mum first, before anything else. You make her a cup of tea and settle her into her chair. 'Don't fuss over me,' she says, but her hand holds on to yours a moment too long. The rooms are still full, though, and the light is going. Sitting here with her won't shift a single box. You need a plan, and a clear head, before you so much as start."},
  "c": ["See what's left to shift.", "It's on you now."]},
 5: {"t": {
  "A2": "You roll up your sleeves and start to load. You lift one box, then another, and find a rhythm. Outside, the light is going grey. Then a van pulls up and a man leans out. 'Need a hand with that lot?' he calls. 'Cheap, cash, done by dark.' You weren't expecting anyone.",
  "B1": "You roll up your sleeves and start to load. You lift one box, then another, and find a rhythm. Outside, the light is going grey. Then a van pulls up and a man leans out. 'Need a hand shifting that lot?' he calls. 'Cheap, cash, done by dark.' You weren't expecting anyone, not yet.",
  "B2": "You roll up your sleeves and start to load. You lift one box, then another, and slowly find a rhythm. Outside, the afternoon light is going grey. Then a van pulls up at the kerb and a man leans out of the window. 'Need a hand shifting that lot?' he calls. 'Cheap, cash, done by dark.' You weren't expecting anyone, not yet, and something about him puts you on your guard."},
  "c": ["Down to the van.", "A neighbour needs a hand.", "Stop and think.", "Someone at the door."]},
 6: {"t": {
  "A2": "You make yourself stop and think. You could start carrying down right now and sort the rest later. You could load the heavy things first. Or you could knock on doors and ask for a hand. Each choice costs time you don't have. And the light keeps going.",
  "B1": "You make yourself stop and think. You could start carrying down right now and sort the rest later. You could load the heavy things first, while you're fresh. Or you could knock on doors and ask for a hand. Each choice costs time you don't have — and the light keeps going.",
  "B2": "You make yourself stop and think for a moment. You could start carrying down right now and sort the rest out later. You could load the heavy things first, while your arms are still fresh. Or you could knock on a few doors and ask for a hand. Each choice costs time you don't have — and the light keeps going, steadily, toward dusk."},
  "c": ["Start carrying down.", "Just start lifting.", "Knock for help."]},
 8: {"t": {
  "A2": "The weight of it presses down on you. You think of Mum in her chair, of the dark coming, of the key you can't yet turn. A whole new start rests on this one afternoon. That isn't a worry; it's a plain fact. No one else will carry it in for you. It's you, today, or it waits.",
  "B1": "The weight of it presses down on you. You think of Mum in her chair, of the dark coming on, of the key you can't yet turn. A whole new start rests on this one afternoon. That isn't a worry; it's a plain fact. No one else will carry it in for you. It's you, today, or it waits.",
  "B2": "The weight of it presses down on you like a hand. You think of Mum sitting in her chair, of the dark coming on, of the key you can't yet turn in the new lock. A whole new start rests on this one short afternoon. That isn't a worry; it's a plain fact. No one else is going to carry it all in for you. It's you, today, or it waits."},
  "c": ["Stop and think.", "Down to the van.", "A scramble at the van."]},
 11: {"t": {
  "A2": "You just start lifting, fast and in no order. You grab the nearest box and go. But you've no real plan, and the heavy things are left for last, when you'll be tired. Rushing like this, your back will pay for it. You can't just pile it up and hope.",
  "B1": "You just start lifting, fast and in no order. You grab the nearest box and go. But you've no real plan, and the heavy things get left for last, when you'll be tired. Rushing like this, your back will pay for it. You can't just pile it up and hope for the best.",
  "B2": "You just start lifting, fast and in no order at all. You grab the nearest box and go. But you've no real plan, and the heavy things get left for last, for when you'll be tired and sloppy. Rushing headlong like this, your back will pay for it. You can't simply pile it all up and hope for the best."},
  "c": ["Out to the van.", "The rush catches up."]},
 13: {"t": {
  "A2": "You take charge of the move. You sort it all out: heavy and low, light on top, Mum's things kept safe and apart. Done well, this gets her home in one trip. Rushed or jumbled, and something breaks on the stairs. So you take a breath and load it right, with care.",
  "B1": "You take charge of the move. You sort it all out: heavy and low, light on top, Mum's things kept safe and apart. Done well, this gets her home in one or two trips. Rushed or jumbled, and something breaks on the stairs. So you take a breath and load it right, with care.",
  "B2": "You take charge of the whole move. You sort it all out properly: heavy things low, light things on top, Mum's own things kept safe and apart. Done well, this gets her home in one or two careful trips. Rushed or jumbled, and something gets dropped and broken on the stairs. So you take a breath and load it right, with care, piece by piece."},
  "c": ["Out to the van.", "Ask an old hand first."]},
 14: {"t": {
  "A2": "You grab just the first few boxes and go. It feels good to be moving at last. But it isn't a plan, and the hard things are still up there. You'll have to come back for the rest, and soon. If not, it'll still be here when the light's gone.",
  "B1": "You grab just the first few boxes and go. It feels good to be moving at last. But it isn't a plan, and the hard things are still up there. You'll have to come back for the rest, and soon. If not, it'll still be here when the light has gone.",
  "B2": "You grab just the first few boxes and go. It feels good to be moving at last, after all the standing around. But it isn't a plan, and the hard, heavy things are still up there. You'll have to come back for the rest, and soon. If you don't, it'll still be sitting here when the light has gone."},
  "c": ["Out to the van.", "Ask an old hand first."]},
 15: {"t": {
  "A2": "Old Tom from the ground floor has moved more homes than he can count. 'Don't carry too much to save trips,' he says. 'That's how backs go, and boxes.' He warns you about Bray too, the man with the van. 'Do it yourself, slow and steady. That's the whole job today.'",
  "B1": "Old Tom from the ground floor has moved more homes than he can count. 'Don't carry too much at once to save trips,' he says. 'That's how backs go, and boxes.' He warns you about Bray too, the man with the van. 'Do it yourself, slow and steady. That's the whole job today.'",
  "B2": "Old Tom from the ground floor has moved more homes in his time than he can count. 'Don't carry too much at once just to save trips,' he says. 'That's how backs go, and boxes.' He warns you about Bray too, the man with the van. 'Do it yourself, slow and steady, and mind the stairs. That's the whole job today.'"},
  "c": ["Take his words to heart.", "Out to the van."]},
 16: {"t": {
  "A2": "You stop and help the neighbour. She's an old woman who can't lift her shopping up the step. You carry it in and set it down in her kitchen. Little by little she stops fretting. 'Bless you,' she says, holding your arm. You tell her you'll look in later, then turn back to your own boxes.",
  "B1": "You stop and help the neighbour. She's an old woman who can't lift her shopping up the step. You carry it in and set it down in her kitchen. Little by little she stops fretting. 'Bless you,' she says, holding on to your arm. You tell her you'll look in later, then turn back to your own boxes and the light.",
  "B2": "You stop and help the neighbour. She's an old woman who can't lift her heavy shopping up the step. You carry it in for her and set it down in her kitchen. Little by little she stops fretting and catches her breath. 'Bless you,' she says, holding on to your arm. You tell her you'll look in later, then turn back to your own boxes and the fading light."},
  "c": ["On, feeling steadier.", "Knock for more help."]},
 17: {"t": {
  "A2": "Getting Mum home comes first. The rest can wait a moment. But you still have to choose how. You could start carrying the boxes down to the van first. Or you could just start lifting and sort the order as you go.",
  "B1": "Getting Mum home comes first. The rest can wait a moment. But you still have to choose how. You could start carrying the boxes down to the van first. Or you could just start lifting and sort out the order as you go.",
  "B2": "Getting Mum home before dark comes first. Everything else can wait a moment. But you still have to choose how to do it. You could start carrying the boxes down to the van first, and load it properly. Or you could just start lifting and sort out the order as you go along."},
  "c": ["Down to the van.", "Just start lifting."]},
 18: {"t": {
  "A2": "The rush catches up with you. Your arms ache, your back twinges, and the light won't wait. You're trying to carry too much at once, and you know it. If you hurt yourself now, the move stops dead. So slow down, breathe, one box at a time.",
  "B1": "The rush catches up with you. Your arms ache, your back twinges, and the light won't wait. You're trying to carry too much at once, and you know it. If you hurt yourself now, the whole move stops dead. So slow down, breathe, and take one box at a time.",
  "B2": "The rush finally catches up with you. Your arms ache, your back twinges, and the light will not wait for anyone. You're trying to carry far too much at once, and you know it. If you hurt yourself now, on these stairs, the whole move stops dead. So slow down, breathe, and take just one box at a time."},
  "c": ["Bray steps in.", "Out to the van."]},
 19: {"t": {
  "A2": "You knock round, and the block comes through. One brings a trolley. One takes an end of the sofa. One just rolls up their sleeves and asks what's next. Bit by bit, it stops being a job for one. You're not carrying it alone now — and that changes everything.",
  "B1": "You knock round, and the block comes through for you. One brings a trolley. One takes an end of the sofa. One just rolls up their sleeves and asks what's next. Bit by bit, it stops being a job for one. You're not carrying it alone now — and that changes everything.",
  "B2": "You knock round the doors, and the block comes through for you, one by one. One brings down a trolley. One takes the other end of the sofa. One just rolls up their sleeves and asks what's next. Bit by bit, it stops being a job for one pair of hands. You're not carrying it alone any more — and that changes everything."},
  "c": ["Everyone pitches in.", "Get a system going."]},
 20: {"t": {
  "A2": "No one can help. One is out, one is at work, one just doesn't answer the door. You can't make them. So you set your shoulders and carry on alone. It's harder this way. But the light goes at five, ready or not.",
  "B1": "No one can help. One is out, one is at work, one just doesn't answer the door. You can't make them. So you set your shoulders and carry on alone. It's harder this way. But the light goes at five, ready or not.",
  "B2": "No one can help you today. One is out, one is stuck at work, one simply doesn't answer the door. You can't make them, and you don't try. So you set your shoulders and carry on alone. It's a good deal harder this way. But the light goes at five o'clock, ready or not."},
  "c": ["Down to the van.", "Just start lifting."]},
 21: {"t": {
  "A2": "You're down at the van with the first load. To get it all in before dark, you have to choose how to carry. The safe way is one box at a time, up and down the stairs. Piling it high saves trips and time. But it's risky, and the stairs are steep.",
  "B1": "You're down at the van with the first load. To get it all in before dark, you have to choose how to carry. The safe way is one box at a time, up and down the stairs. Piling it high saves trips and time. But it's risky, and the stairs are steep.",
  "B2": "You're down at the van at last with the first load. To get it all in before dark now, you have to choose how to carry it. The safe way is one box at a time, up and down the stairs. Piling it high in your arms saves trips and time. But it's risky, and the stairs are steep and worn."},
  "c": ["One at a time, the safe way.", "Pile it high.", "Bray is here."]},
 22: {"t": {
  "A2": "You take old Tom's words to heart. Do it yourself. Load it right. Don't trust Bray. And don't carry too much to save a trip. It's simple advice, and good. Now you just have to follow it, with the light going down.",
  "B1": "You take old Tom's words to heart. Do it yourself. Load it right. Don't trust Bray. And don't carry too much just to save a trip. It's simple advice, and good. Now you just have to follow it, with the light going down.",
  "B2": "You take old Tom's words right to heart. Do it yourself. Load it right, heavy things low. Don't trust Bray for a second. And don't carry too much just to save a trip. It's simple advice, and good advice. Now you just have to follow it, with the light going down fast."},
  "c": ["Back to loading.", "Carry the next one down."]},
 23: {"t": {
  "A2": "You feel better for the good turn you did. Helping someone, oddly, seems to steady you too. Your arms feel stronger, your head is clearer. There's still a lot to shift before dark. But now you feel able to meet it.",
  "B1": "You feel better for the good turn you did. Helping someone, oddly, seems to steady you too. Your arms feel stronger now, your head is clearer. There's still a lot to shift before dark. But now you feel able to meet it.",
  "B2": "You feel better for the good turn you did back there. Helping someone, oddly enough, seems to steady you as much as them. Your arms feel stronger now, and your head is clearer. There's still a great deal to shift before dark. But now, somehow, you feel able to meet it."},
  "c": ["Back to the van.", "Knock for more help."]},
 24: {"t": {
  "A2": "Bray hops down from the van, all smiles. He can shift the whole lot in twenty minutes, he says, and he's happy to. 'Why break your back, love?' he says. 'Fixed price, cash, done by dark. No stairs, no sweat.' You've heard this kind of offer before.",
  "B1": "Bray hops down from the van, all smiles. He can shift the whole lot in twenty minutes, he says, and he's happy to. 'Why break your back, love?' he says. 'Fixed price, cash, done by dark. No stairs, no sweat.' You've heard this kind of offer before.",
  "B2": "Bray hops down from the van, all easy smiles. He can shift the whole lot in twenty minutes, he says, and he's more than happy to. 'Why break your back, love?' he says. 'Fixed price, cash in hand, done by dark. No stairs, no sweat.' You've heard this exact kind of offer before."},
  "c": ["Hear his price.", "Say no and carry on."]},
 25: {"t": {
  "A2": "With the block pitching in, the work turns light. One carries, one packs the van, one keeps Mum company. 'This one next,' you say, and they follow your lead. It's a good feeling, a chain of hands on the stairs, with the light going down.",
  "B1": "With the block pitching in, the work turns light. One carries, one packs the van, one keeps Mum company. 'This one next,' you say, and they follow your lead. It's a good feeling, a chain of hands on the stairs, with the light going down.",
  "B2": "With the whole block pitching in, the work turns light. One carries, one packs the van, one keeps Mum company by the window. 'This one next,' you say, and they follow your lead. It's a good feeling, a chain of willing hands on the stairs, with the light going down."},
  "c": ["Keep the chain going.", "A face at the gate."]},
 26: {"t": {
  "A2": "One box at a time is slow and hard, up and down the long stairs. Your legs burn and the light fades. But nothing breaks, and nothing falls. So you keep going, trip after trip, as fast as you safely can. The light drops, but the van fills.",
  "B1": "One box at a time is slow and hard, up and down the long stairs. Your legs burn and the light fades. But nothing breaks, and nothing falls. So you keep going, trip after trip, as fast as you safely can. The light drops, but the van fills up.",
  "B2": "One box at a time is slow and hard going, up and down the long worn stairs. Your legs burn and the light fades. But nothing breaks, and nothing falls, and nobody gets hurt. So you keep going, trip after trip after trip, as fast as you safely can. The light drops, but the van slowly fills."},
  "c": ["The afternoon wears on.", "Someone has fallen.", "You stop for breath."]},
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
