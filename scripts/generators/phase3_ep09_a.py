#!/usr/bin/env python3
"""Phase 3 prose for The Dinner (episode-09), batch A: Act I, nodes 1-26.
Run: python3 scripts/generators/phase3_ep09_a.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-09.json")

D = {
 1: {"t": {
  "A2": "It is five o'clock. The family come for dinner at seven. But Gran Ivy is ill in bed upstairs, and tonight she can't cook. The chicken is still in the fridge. The cake is half made. The table is bare. Getting a good dinner on the table is on you now.",
  "B1": "It is five o'clock, and the family come for dinner at seven. But Gran Ivy, who cooks this dinner every year, is ill in bed upstairs. The chicken is still in the fridge, the cake is half made, and the table is bare. For the first time, getting dinner on the table is all on you.",
  "B2": "It is five o'clock, and the whole family come for dinner at seven. But Gran Ivy, who has cooked this dinner for thirty years, is ill in bed upstairs and can't come down. The chicken is still in the fridge, the cake is only half made, and the table is bare. For the first time, getting a good dinner on the table is all on you."},
  "c": ["Take charge of the cooking.", "Call someone for help.", "See to Gran first."]},
 2: {"t": {
  "A2": "You see what the kitchen holds. There is a chicken, potatoes, flour, and butter. There is a big pan and a good oven. The clock is already at five. You have to decide what to do, and start soon.",
  "B1": "You see what the kitchen holds: a chicken, potatoes, flour, butter, a big pan, a good oven. The clock is already past five, and the room smells of nothing cooking. You have to decide what to do, and start soon.",
  "B2": "You take stock of what the kitchen holds: a chicken, a bag of potatoes, flour and butter, a big roasting pan, a good oven. The clock is already past five, and there's that quiet, empty feeling of a kitchen where nothing is cooking yet. You have to decide what to do, and you have to start soon."},
  "c": ["Get started in the kitchen.", "Stop and plan it out.", "The oven won't come on."]},
 3: {"t": {
  "A2": "You call your mum to ask what to do. The phone rings and rings. At last she answers. She can't come over tonight, she says. She is too far away. But she talks you through Gran's recipe, step by step. 'You can do this,' she says.",
  "B1": "You call your mum to ask what to do. The phone rings and rings, then at last she answers. She can't come over tonight — she's too far away to help. But she talks you through Gran's recipe, step by step. 'You can do this,' she says, and somehow you start to believe her.",
  "B2": "You call your mum to ask what to do. The phone rings and rings, and then at last she answers. She can't come over tonight — she's an hour away, and the buses have stopped. But she talks you calmly through Gran's recipe, step by step, down the crackly line. 'You can do this,' she says, and somehow you start to believe her."},
  "c": ["Plan it out.", "But there's so little time."]},
 4: {"t": {
  "A2": "You go up to Gran first. You bring her tea and make her warm. But the kitchen is still cold and empty. Being kind to Gran is good. But the dinner still needs cooking. You need a plan, and a clear head, before seven.",
  "B1": "You go up to Gran first. You bring her tea and make her comfortable. But the kitchen is still cold and empty downstairs. Sitting with Gran won't cook the dinner. The family will be hungry at seven. You need the shopping, a plan, and a clear head before you start.",
  "B2": "You go up to Gran first, bringing her tea and making her comfortable in bed. But the kitchen is still cold and empty downstairs, and sitting with Gran won't get the dinner cooked. The family will be at the door at seven, hungry and happy. You need the shopping, a plan, and a clear head before you can give them that."},
  "c": ["Go down and start cooking.", "Feel how little time there is."]},
 5: {"t": {
  "A2": "You roll up your sleeves in the kitchen. The oven hums as it warms. Outside, the street is dark and wet. Then there is a knock at the gate — soft, once, then nothing. Someone is out there in the dark. But you weren't expecting anyone yet.",
  "B1": "You roll up your sleeves and get into the kitchen. The oven hums as it warms, and the window begins to steam. Outside, the street is dark and wet. Then you hear it: a knock at the gate — soft, once, then nothing. Someone is out there in the dark, and you weren't expecting anyone this early.",
  "B2": "You roll up your sleeves and get into the kitchen. The oven hums as it warms, and the window begins to steam up against the cold. Outside, the street is dark and wet and empty. Then you hear it: a knock at the gate — soft, just once, then nothing. Someone is out there in the dark tonight, and you weren't expecting a soul this early."},
  "c": ["Pop to the corner shop.", "Knock next door for help.", "Plan it out.", "The knock at the gate."]},
 6: {"t": {
  "A2": "You stop and think. You could start cooking right now. You could go up to Gran and the family first. Or you could call friends to come and help. Each choice costs time you do not have. And the clock keeps moving toward seven.",
  "B1": "You make yourself stop and think. You could start the cooking right now and sort the rest later. You could go to Gran and get things straight first. Or you could call a few friends to come and help. Each choice costs time you don't have — and the clock keeps moving toward seven.",
  "B2": "You make yourself stop and think it through. You could start the cooking right now and worry about everything else after. You could go up to Gran and the family and get things straight first. Or you could call a few friends and get more hands in the kitchen. Each choice costs time you don't have — and the clock keeps ticking, steadily, toward seven."},
  "c": ["The corner shop.", "Straight into the cooking.", "Call friends to help."]},
 8: {"t": {
  "A2": "The time presses on you like a weight. You think of the family at seven: the kids, the aunts, Gran's friends from the street. A whole evening, and it rests on you. That is not a worry; it is a plain fact. No one else is going to cook it. It is you, tonight, or no one.",
  "B1": "The time presses on you like a weight. You think of the family coming at seven — the kids, the aunts, Gran's old friends from the street — all of them hungry and happy. A whole evening rests on you now. That isn't a worry; it's a plain fact. No one else is going to cook it. It is you, tonight, or no one.",
  "B2": "The time presses on you like a weight. You think of the family coming at seven — the kids, the aunts, Gran's old friends from down the street — all of them hungry and happy and expecting her roast. A whole evening rests on you now. That isn't a worry; it's a plain fact. No one else is going to step in and cook it. It is you, tonight, or it is no one."},
  "c": ["Plan it out.", "To the corner shop.", "A rush at the shop."]},
 11: {"t": {
  "A2": "You get straight into the cooking. You turn on the hob, put a pan on, cut a few things. But you have no proper plan. Half the food is still in the bags. This will not come together on its own. You can't just throw things in a pan and hope.",
  "B1": "You get straight into the cooking. You turn on the hob, put a pan on, start cutting. But you've no proper plan, and half the food is still in the bags. Rushing like this, it won't come together on its own. You can't just throw things in a pan and hope for the best.",
  "B2": "You get straight into the cooking. You turn on the hob, slap a pan down, start cutting whatever's to hand. But you've no proper plan, and half the food is still sitting in the shopping bags. Rushed like this, it won't come together on its own. You can't just throw things in a pan and hope the evening turns out well."},
  "c": ["Sort out a proper plan.", "The rush tires you out."]},
 13: {"t": {
  "A2": "You take charge of the food and the recipe. You lay it all out on the table: chicken, potatoes, butter, the cake things. Done well, this makes a real dinner for seven. Rushed and wasted, and there's nothing on the table. So you start, carefully.",
  "B1": "You take charge of the food and Gran's recipe. You lay it all out on the table — chicken, potatoes, butter, the things for the cake. Done well, this makes a real dinner for seven. Rushed or wasted, and the table stays bare. So you take a breath and start, carefully.",
  "B2": "You take charge of the food and Gran's recipe. You lay it all out along the table — the chicken, the bag of potatoes, the butter, the things for the cake. Done properly, this is a real dinner for the whole family at seven. Rushed or wasted, and the table stays bare. So you take a breath, and you start, carefully."},
  "c": ["Now, into the cooking.", "Ask Joan next door for tips."]},
 14: {"t": {
  "A2": "You grab just a pan and a knife and start. They let you begin, and that feels good. But it is not a plan, and you've bought nothing extra. You'll still need the shopping, and soon. If not, there won't be enough for seven.",
  "B1": "You grab just a pan and a knife and make a start. They let you begin, and that feels like something. But it isn't a plan, and you've bought nothing extra. You'll still need the shopping, and soon. If not, there won't be enough for everyone at seven.",
  "B2": "You grab just a pan and a knife and make a start. They let you begin, and that feels like something, at least. But it isn't a plan, and you've bought nothing extra for the table. You'll still need to get the shopping, and soon. Without it, there simply won't be enough to go round at seven."},
  "c": ["Now, get the shopping.", "Ask Joan next door for tips."]},
 15: {"t": {
  "A2": "Old Joan next door has cooked a thousand dinners. 'Don't run across the main road,' she says. 'It saves ten minutes. It's not worth it in the dark.' She warns you about Dale too, from the takeaway. 'Cook your own food. Watch the oven. That's the whole job tonight.'",
  "B1": "Old Joan next door has cooked a thousand dinners in her time. 'Don't run across the main road,' she says. 'It saves ten minutes — and it's not worth it in the dark and the rain.' She warns you about Dale too, from the takeaway. 'Cook your own food, keep an eye on the oven. That's the whole job tonight.'",
  "B2": "Old Joan next door has cooked a thousand dinners in her time, and she knows a panic when she sees one. 'Don't run across the main road,' she says. 'It saves you ten minutes — and it's not worth it, not in the dark and the rain.' She warns you about Dale as well, the fellow from the takeaway. 'Cook your own food, and keep one eye on the oven. That's the whole job tonight.'"},
  "c": ["Take it to heart.", "On with it."]},
 16: {"t": {
  "A2": "You help your neighbour, Mr Doyle, who is locked out in the cold. You get him inside and sit him down with tea. Little by little, he warms up. 'Bless you,' he says, holding your hand. You promise to pop back later. Then you go back to your kitchen and the clock.",
  "B1": "You help your neighbour, Mr Doyle, who's locked out of his flat in the cold. You get him inside and sit him down with a cup of tea. Little by little, he warms up and stops shivering. 'Bless you,' he says, gripping your hand. You promise to look in on him later, then go back to your own kitchen and the clock.",
  "B2": "You help your neighbour, Mr Doyle, who's locked out of his flat and shivering on the step. You get him inside, sit him down, and put the kettle on. Little by little he warms up and the colour comes back to his face. 'Bless you,' he says, gripping your hand. You promise to look in on him later, then turn back to your own kitchen and the ticking clock."},
  "c": ["On with the cooking.", "He asks you to check the others."]},
 17: {"t": {
  "A2": "The cooking comes first. The rest can wait a moment. But you still have to choose how. You could go to the shop for what you need first. Or you could start with what you've got and sort it as you go.",
  "B1": "The cooking comes first. The rest can wait a moment. But you still have to choose how. You could go to the shop for what you need first. Or you could start with what you've got and sort the rest as you go.",
  "B2": "Getting the cooking going comes first; the rest can wait a moment. But you still have to choose how to do it. You could go to the shop for what you need and set yourself up properly. Or you could start with what you've already got, and sort the rest out as you go along."},
  "c": ["Get the shopping first.", "Start with what you've got."]},
 18: {"t": {
  "A2": "The rush catches up with you. Your back aches, your hands shake, and the clock keeps moving. You are doing too much at once, and you know it. If you tire yourself out now, nothing gets finished. So slow down, and do one thing at a time.",
  "B1": "The rush catches up with you. Your back aches, your hands are shaking, and the clock won't stop. You're trying to do too much at once, and you know it. If you tire yourself out now, nothing gets finished. So slow down, and do one thing at a time.",
  "B2": "The rush catches up with you all at once. Your back aches, your hands are shaking, and the clock on the wall will not stop moving. You're trying to do far too much at once, and you know it. If you burn yourself out now, nothing gets finished at all. So slow down, breathe, and do one thing at a time."},
  "c": ["Dale knocks at the door.", "Push on."]},
 19: {"t": {
  "A2": "You call round, and friends start to come. One brings a dish. One brings chairs. Another just rolls up their sleeves. Bit by bit, a plan takes shape. You are not doing this alone any more. And that changes everything.",
  "B1": "You call round, and friends start to arrive. One brings a dish of their own. One brings extra chairs. Another just rolls up their sleeves and asks what to chop. Bit by bit, a plan takes shape. You're not doing this alone any more — and that changes everything.",
  "B2": "You call round, and friends start to arrive at the door. One brings a dish of their own to add to the table. One brings extra chairs under both arms. Another just rolls up their sleeves and asks what needs chopping. Bit by bit, hand by hand, a plan takes shape in the warm kitchen. You're not doing this alone any more — and that, more than anything, changes the evening."},
  "c": ["Get everyone cooking.", "Lay the big table first."]},
 20: {"t": {
  "A2": "No one can come. One is working, one is out, one just doesn't pick up. You can't make them. So you turn back to the kitchen and go on alone. It is harder this way. But the family still come at seven.",
  "B1": "No one can come. One is working late, one is already out, one just doesn't pick up the phone. You can't make them. So you turn back to the kitchen and go on alone. It's harder this way. But the family still come at seven, ready or not.",
  "B2": "No one can come, in the end. One is working late, one is already out for the evening, one simply doesn't pick up. You can't make anyone help you. So you turn back to the kitchen and go on alone; it's harder this way, dish by dish — but the family still come at seven, ready or not."},
  "c": ["The corner shop.", "On with the cooking."]},
 21: {"t": {
  "A2": "The first dishes are on. Now you need a few things from the shop. There are two ways there. The long way round the block is safe but slow. Straight across the main road is quick. But it's dark and wet, and cars come fast.",
  "B1": "The first dishes are on. Now you need a few things from the shop to finish. There are two ways there. The long way round the block is safe but slow. Straight across the main road is quick. But it's dark and wet, and the cars come fast.",
  "B2": "The first dishes are on and ticking over. Now you need a few last things from the shop to finish the meal. There are two ways to get there: the long way round the block, safe but slow, or straight across the main road, quick and tempting. But it's dark and wet out, and the cars come fast along that road."},
  "c": ["Go the long way round.", "Cross the main road.", "Dale's offer ahead."]},
 22: {"t": {
  "A2": "You take old Joan's words to heart. Cook your own food. Watch the oven. Don't trust Dale. And stay off that main road. It is simple advice, and good. Now you just have to follow it.",
  "B1": "You take old Joan's words to heart. Cook your own food. Keep an eye on the oven. Don't trust Dale. And stay well off that main road. It's simple advice, and good. Now you just have to follow it, with the clock running.",
  "B2": "You take old Joan's words to heart, one by one. Cook your own food. Keep one eye on the oven. Don't trust a word Dale says. And stay well off that main road in the dark. It's simple advice, and good — the hard part is following it when you're tired and the clock is running down."},
  "c": ["On with it.", "Back to the shop."]},
 23: {"t": {
  "A2": "You feel better for helping someone. Oddly, it steadies you too. Your head is clearer, and your hands are surer. There's still a lot to do before seven. But now you feel able to do it.",
  "B1": "You feel better for the good turn you did. Helping someone, oddly, seems to steady you too. Your head is clearer, and your hands are surer. There's still a lot to do before seven. But now you feel able to meet it.",
  "B2": "You feel better for the good turn you did. Helping someone out, oddly enough, seems to steady you as well. Your head is clearer now, and your hands are surer on the work. There's still a great deal to do before seven — but you feel, for the first time since Gran called down, able to meet it."},
  "c": ["On with the cooking.", "Call more people in."]},
 24: {"t": {
  "A2": "Dale from the takeaway is at the door, all smiles. He has hot food in bags and an easy way out. 'Why cook, love?' he says. 'Buy mine, tip it in your dishes. No one will ever know.' You've heard that kind of thing before.",
  "B1": "Dale from the takeaway is at the door, all smiles. He has hot food in bags and an easy way out to sell you. 'Why go to all that trouble, love?' he says. 'Buy mine, tip it into your own dishes — no one will ever know.' You've heard that kind of offer before.",
  "B2": "Dale from the takeaway on the corner is at your door, all smiles, steam rising off the bags in his hands. He has hot food to sell and an easy way out to go with it. 'Why go to all that trouble, love?' he says. 'Buy mine, tip it into your own dishes — no one will ever know the difference.' You've heard that kind of offer before, and you know a hook when it's dangled."},
  "c": ["Hear him out.", "Say no and get on."]},
 25: {"t": {
  "A2": "You get everyone busy in the kitchen. Working together, it all feels lighter. One peels, one stirs, one lays the table. 'This bit next,' you say, and they follow. It's a good feeling, with the clock running.",
  "B1": "You get everyone busy in the kitchen. Working together, the whole thing feels lighter. One peels the potatoes, one stirs a pot, one lays the table. 'This bit next,' you say, and they follow your lead. It's a good feeling, with the clock running down.",
  "B2": "You get everyone busy in the warm kitchen. Working together, the whole evening suddenly feels lighter than it did. One peels the potatoes, one stirs a pot, one lays the table under your eye. 'This bit next,' you say, and they follow your lead. It's a good feeling to have, with the clock running down toward seven."},
  "c": ["This way.", "The knock at the gate again."]},
 26: {"t": {
  "A2": "The long way round is dark and cold. The rain is on your face, and there is no shelter. But it is safe under your feet, and it gets you to the shop. So you keep walking, as fast as you dare.",
  "B1": "The long way round is dark and cold, the rain on your face, no shelter at all. But it's safe under your feet, and it gets you to the shop and back. So you keep walking, as fast as you dare, step after step.",
  "B2": "The long way round the block is dark and cold, the rain stinging your face, with no shelter at all along the way. But it's safe under your feet, and it gets you to the shop and back in one piece. So you keep walking into it, as fast as you dare, step after step after step."},
  "c": ["Press on.", "Someone needs a hand.", "The quiet street, all lit windows."]},
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
