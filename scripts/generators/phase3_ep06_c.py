#!/usr/bin/env python3
"""Phase 3 prose for The Orchard — batch 3 (nodes 41-69). Run then validate."""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
EP = os.path.join(ROOT, "content", "episode-06.json")
book = json.load(open(EP, encoding="utf-8"))
nodes = {n["id"]: n for n in book["nodes"]}

P = {
 41: (
  "The offer is a hook, and you feel it set. He leans in close. \"That orchard's lost already,\" he says, low. \"Let the frost take it. There's money in it for you.\" It is a cruel thing to say. And it is meant to work.",
  "The offer is a hook, and you feel it set. He leans in close. \"That orchard's lost already,\" he says, low. \"Let the frost take it — and there's a share in it for you.\" It's a cruel thing to say. And it is meant to work on your fear.",
  "The offer is a hook, and you feel it set in you. He leans in close. \"That orchard's lost already,\" he says, low and easy. \"Let the frost do its work — and there's a good share in it for you.\" It is a cruel thing to say to you tonight. And every word of it is meant to work on your fear."),
 42: (
  "You turn your back and leave him to his cold trade. It feels good to walk away. He calls after you. You don't turn round. His kind always finds someone. But it won't be you tonight.",
  "You turn your back on him and leave him to his cold trade. It feels good to walk away. He calls after you, but you don't turn round. His kind always finds someone, in the end. But it won't be you, not tonight.",
  "You turn your back on him and leave him to the dark and his cold trade. It feels good to walk away from it. He calls after you, but you don't turn round. His kind always finds someone, in the end — a frightened person, a bad night. But it won't be you, and it won't be tonight."),
 43: (
  "You take his oil and his money. Your hands close on them. And something in you already knows. His smile widens. \"Wise,\" he says. But it does not feel wise. It feels like a door shutting.",
  "You take his oil and his money. Your hands close on them, and something in you already knows. His smile widens. \"Wise,\" he says. But it doesn't feel wise at all. It feels like a door quietly shutting.",
  "You take his oil and his money, and your hands close on them before your head can argue. Something in you already knows. His smile widens. \"Wise,\" he says. But it doesn't feel wise at all. It feels, if anything, like a door shutting somewhere behind you. You cannot take it back now."),
 44: (
  "You ask him straight. What does he really want? Why should the orchard fail? He smiles and looks away. \"Land comes cheap after a bad year,\" he says. \"The frost is kind — to a buyer.\"",
  "You ask him straight: what does he really want, and why should the orchard fail? He smiles and looks off down the lane. \"Land comes cheap after a bad year,\" he says. \"A frost like this is a kindness — to a buyer like me.\"",
  "You ask him straight out: what is it he really wants, and why should the orchard be left to fail? He smiles and looks off down the dark lane. \"Land comes cheap after a bad year,\" he says, unhurried. \"A frost like this one is a real kindness — to a buyer like me.\""),
 45: (
  "You carry his oil out to the pots. But when you pour it, the flame chokes and spits. The oil is cut with water. It won't feed the fire. The flames sink low and brown.",
  "You carry his oil out to the pots. But when you pour it in, the flame chokes and spits. The oil is thin, cut with water — it won't feed the fire. The flames sink low and brown and useless.",
  "You carry his oil out to the pots and tip it in. But the moment it reaches the flame, the fire chokes and spits. The oil is thin and watered, cut to make it stretch — it will not feed a flame at all. Down the rows, the fires sink low and brown and useless."),
 46: (
  "You open the can, and the smell hits you. Thin, cut with water. This oil will never feed a flame. You paid for it, and it is worthless. The doubt in your gut was right.",
  "You open the can, and the smell hits you — thin, sour, cut with water. This oil will never feed a flame. You paid good money for it, and it's worthless. The doubt in your gut was right all along.",
  "You open the can, and the smell hits you at once — thin and sour, cut down with water to stretch it. This oil will never feed a flame; not one pot will light on it. You paid good money for it, and it is worthless. The doubt in your gut, it turns out, was right all along."),
 47: (
  "You look for him, but he is already gone. His lantern is far down the lane. He was never helping you. He was waiting for the frost, and the failed year, and the cheap land. You were fooled.",
  "You look for him, but the buyer's lantern is already gone, off down the lane. He was never helping you at all. He was waiting for the frost, the failed harvest, the cheap land after. You were fooled, plain and simple.",
  "You look for him, but the buyer's lantern is already gone, bobbing away down the lane. He was never helping you at all, not for a moment. He was only waiting for the frost, the failed harvest, and the cheap land that comes after a ruined year. You were fooled, plain and simple."),
 48: (
  "He is gone, the lane empty. There is only the cold now, and the dark, and what you gave him for nothing. You learned a hard lesson. And you paid far too much for it. Now you go on with less.",
  "He's gone, and the lane is empty — only the cold now, the dark, and what you handed him for nothing. You learned a hard lesson tonight. And you paid far too much for it. Now you go on with less than you started.",
  "He is gone, and the lane is empty — only the cold now, the dark, and the thought of what you handed him for nothing at all. You learned a hard lesson tonight, about who smiles and why. And you paid far too much for the learning. Now you have to go on with less than you started with."),
 49: (
  "The frightened people press their money on him. Hands full of coins, voices begging for oil. And he takes it, slow, with that smile. He chooses who to help by who pays most.",
  "The frightened folk press their coins on him. Hands full of money, voices begging for oil. He takes it slow, with that same smile. He chooses who to help by who can pay the most.",
  "The frightened folk press their coins on him. Hands full of money, voices begging for oil, for warmth, for any way through the night. He takes it slow and easy, with that same smile. He chooses who to help and who to pass by. And he chooses by who can pay the most."),
 50: (
  "Far out on the ice, the far rows seem nearer at last. Or do they? You can't be sure now. The dark plays tricks. Your tired eyes play tricks. And you are a long way from either side.",
  "Far out on the ice, the far rows seem nearer at last — or do they? You can't be sure any more. The dark plays tricks, and so do your tired eyes. And you're a long way now from either bank.",
  "Far out on the ice, the far rows seem a little nearer at last — or do they? You can't be sure of anything any more. The dark plays tricks on you, and so do your cold, tired eyes. And you are a long way out now, a long way from either bank."),
 51: (
  "The ice, the dark, the deep water below — and your foot breaks through. This is the moment. Go down into the black water. Or throw yourself back from the crack, while you still can.",
  "The ice, the dark, the deep water below — and a crack runs out from under your foot. This is the moment. You can go down into the freezing water. Or you can throw yourself back from the crack, while you still can.",
  "The ice, the dark, the deep black water below — and a long crack runs out from under your foot with a sound like a shot. This is the moment, and there is no other. You can go down into the freezing water. Or you can throw yourself back from the crack, right now, while you still can."),
 52: (
  "You reach the far rows at last. You are soaked, shaking, your hands torn. But you made it across. Now you must decide. Push on, spent as you are. Or face what you dropped on the ice.",
  "You reach the far rows at last, soaked and shaking, your hands torn raw — but across. Somehow, you made it. Now you have to decide: push on, spent as you are, or face what you lost out on the ice.",
  "You reach the far rows at last, soaked and shaking, your hands torn raw on the ice — but down, and across. Somehow, against the odds, you made it. Now you have to decide what comes next: push on, spent as you are, or face what you dropped out on the ice in the scramble."),
 53: (
  "You throw yourself back from the crack, while you still can. It is the hard, right choice. You crawl the last stretch on hands and knees. You reach the bank shaken and slow. The night is not lost. But you lost time.",
  "You throw yourself back from the crack while you still can — the hard, right choice. You crawl the last stretch on hands and knees, and reach the bank shaken and slow. The night isn't lost. But it cost you time you'll miss.",
  "You throw yourself back from the crack while you still can — the hard choice, and the right one. You crawl the last stretch on your hands and knees, and reach the bank at last, shaken and slow and soaked through. The night is not lost. But it has cost you time you are going to miss before dawn."),
 54: (
  "You try to get their stove going. You block the worst of the draughts with sacks. It holds back a little of the cold. But there is no lamp to leave them. And the night is far from over.",
  "You try to get their stove going, and block the worst of the draughts with sacks and an old chest. It holds back a little of the cold. But there's still no lamp to leave them, and the night is far from over.",
  "You try to get their stove going again, and pile sacks and an old chest against the worst of the draughts. It holds a little of the cold back, enough to matter. But there is still no lamp to leave them, and the long night is far from over for any of you."),
 55: (
  "You hand over your own coat and lamp. The family huddle round the small flame. Relief spreads across their faces. The child stops crying at last. \"Thank you,\" the mother says. Then she points you to a light out in the trees.",
  "You hand over your own coat and lamp, and the family huddle round the small flame, relief spreading across their faces. The child stops crying at last. \"Thank you,\" the mother says — and then she points you toward a light, out among the far trees.",
  "You hand over your own coat and your own lamp, and the family huddle close round the small flame, relief spreading slowly across their faces. The child stops crying at last. \"Thank you,\" the mother says, over and over — and then she points you toward something: a light, out among the far trees, where no one should be."),
 56: (
  "Without your coat, the cold finds you fast. Your teeth chatter. Your fingers go stiff. You gave it to help, and you would do it again. But the frost does not care about that. It just bites.",
  "Without your coat, the cold and damp find you fast — teeth chattering, fingers going stiff. You gave it away to help, and you'd do it again. But the frost doesn't care about any of that. It just bites harder.",
  "Without your coat, the cold finds you fast and deep — teeth chattering, fingers going stiff and clumsy. You gave it away to help someone with less, and you would do it again tomorrow. But the frost doesn't care about any of that. It simply bites, and goes on biting. You will feel this choice for hours yet."),
 57: (
  "A stranger waves you into a warm doorway. \"Just a minute,\" they say. \"Get out of the cold. Catch your breath.\" It is warm and dry, and your body begs you to stay. But a minute can turn into an hour.",
  "A stranger waves you into a lit doorway. \"Just a minute,\" they say. \"Out of the cold — catch your breath.\" It's warm and dry, and your whole body begs you to stay. But a minute like this can quietly slide into an hour.",
  "A stranger waves you into a lit, warm doorway. \"Just a minute,\" they say kindly. \"Get out of the cold, catch your breath.\" It is warm and dry inside, and your whole exhausted body begs you to stay. But a minute like this one can quietly slide into an hour, and an hour is more than the blossom has."),
 58: (
  "You press on into the frost, chilled to the bone. The cold fights every step. Your eyes water and sting. Each step is a small battle. But you keep them coming, one after another.",
  "You press on into the frost, chilled to the bone, the cold fighting every step, your eyes watering and stinging. Each step is a small battle on its own. But you keep them coming, one after another, toward the rows.",
  "You press on into the frost, chilled to the bone now, the cold fighting you for every single step, your eyes watering and stinging in the still air. Each step is a small battle fought and won on its own. But you keep them coming, one after another after another, toward the waiting rows."),
 60: (
  "Someone points out toward the far trees. A figure went that way, alone, into the dark. Out there lies only cold and the deep frost. If no one goes after them, they may not come back.",
  "Someone points out toward the far trees: a figure has gone out that way, alone, into the cold and the dark. Out there lies nothing but frost and the low, killing ground. If no one goes after them, they may not come back.",
  "Someone points out toward the far trees: a small figure has gone out that way, alone, into the cold and the dark. Out there lies nothing but hard frost and the low ground where the cold pools deepest. If no one goes after them tonight, they may simply not come back at all."),
 61: (
  "You find them among the far trees, half-frozen and lost. The cold has them, and they don't seem to know your face. You take a firm hold of their arm. \"Come with me,\" you say. \"You're all right now.\"",
  "You find them among the far trees, half-frozen and lost, the cold tearing at them. They don't seem to know your face at all. You take a firm hold of their arm. \"Come with me,\" you say. \"You're all right now. I've got you.\"",
  "You find them out among the far trees, half-frozen and badly lost, the cold tearing at their thin coat. They don't seem to know your face, or quite where they are. You take a firm, steady hold of their arm. \"Come with me,\" you say, as gently as you can. \"You're all right now. I've got you.\""),
 62: (
  "You can't do everything at once. And the fires need you most. So you send word for someone else to go after them. Then you press on. It sits badly with you. But you have to choose.",
  "You can't do everything at once, and the fires need you most of all. So you send word for someone else to go after them, and press on. It sits badly with you — but tonight, you have to choose, and keep choosing.",
  "You can't do everything at once, and the fires are the thing that needs you most of all. So you send word back for someone else to go after them, and you press on into the dark. It sits badly with you, and it will go on sitting badly. But tonight you have to choose, and keep choosing, and live with it."),
 63: (
  "You walk them safely back to the cottages. Their family cries out with relief. They wrap you in a dry coat and give you a place by the fire. \"Thank you,\" they keep saying. But you can't stay long.",
  "You walk them safely back to the cottages, where their family cries out with relief. They wrap you in a dry coat and make you a place by the fire. \"Thank you,\" they keep saying. But the rows are waiting, and you can't stay long.",
  "You walk them safely back to the lit cottages, where their family cries out with relief and pulls them inside. They wrap you in a dry coat and make you a place by the fire. \"Thank you,\" they keep saying, again and again. But the rows are still waiting out there in the cold, and you can't stay long."),
 64: (
  "You look out over the orchard. It is all white and still. The blossom shines pale in the dark. No light shows but the far trees. The whole orchard seems to hold its breath, and wait.",
  "You look out over the whole orchard — all white, all still. The blossom shines pale and brittle in the dark. No light shows anywhere but out among the far trees. The whole orchard seems to hold its breath and wait for dawn.",
  "You look out over the whole orchard — all white, all still, under a hard and starry sky. The blossom shines pale and brittle on every tree, waiting on a few degrees of warmth. No light shows anywhere but out among the far trees. The whole orchard seems to hold its breath, and wait to see what you will do."),
 65: (
  "The cold deepens to its worst. The thermometer drops as low as it will go. Your breath hangs white and still. It is hard to think, hard to move. This is the hardest hour of the night.",
  "The cold deepens to its very worst now. The thermometer drops as low as it will go, and your breath hangs white in the still air. It's hard to think, hard to move, hard to care. This is the hardest hour of the whole night.",
  "The cold deepens now to its very worst. The thermometer slides as low as it will go, and your breath hangs white and unmoving in the dead-still air. It is hard to think, hard to move, hard even to care. This is the hardest hour of the whole long night — the hour when the frost does its real damage."),
 67: (
  "Tom presses the last dry lantern on you. \"For the rows,\" he says. \"Go on. I'll stay by the phone.\" His face is grey with worry. This is the help he has to give. And he gives it gladly.",
  "Tom presses the last dry lantern on you. \"For the rows,\" he says. \"Go on — I'll stay here by the phone.\" His face is grey with worry. This is the help he has to give tonight, and he gives all of it gladly.",
  "Tom presses the last dry lantern into your hands. \"For the rows,\" he says. \"Go on — I'll stay here by the phone and raise what hands I can.\" His face is grey with worry under the lamplight. This is the help he has to give tonight, and he gives every bit of it gladly."),
 68: (
  "At the fuel store, people are rushing the cans. Voices rise, hands grab, fear spreads fast. One more shove and it turns into a fight. You can try to calm them and share it out. Or you can just grab your oil and go.",
  "At the fuel store, people are rushing the cans — voices rising, hands grabbing, fear catching and spreading fast. One more shove and it's a fight. You can try to calm them and share the oil out fairly. Or you can just grab yours and go.",
  "At the fuel store, people are rushing the cans — voices rising, hands grabbing, fear catching and spreading fast through the crowd. One more hard shove and the whole thing turns into a fight. You can try to calm them down and share the oil out fairly. Or you can just grab what you came for and go."),
 69: (
  "Years of a shut-up house press in. Dust, silence, old cold — a place where nothing seems alive. Then you hear it. Breathing, weak and close, from the back room. Someone is alive in here after all.",
  "A shut-up house presses in around you — dust, silence, old cold, a place where nothing seems left alive. Then you hear it: breathing, weak and close, from the back room. Someone is alive in here after all.",
  "A long-shut house presses in around you — dust, deep silence, old cold, a place where nothing seems left alive at all. Then you hear it, and you go still: breathing, weak and close, coming from the back room. Someone is alive in here after all, right now, needing you."),
}

C = {
 41: ["Take his deal.", "That's the tell — refuse.", "Ask what he really wants.", "The frightened folk press in."],
 42: ["On the way.", "To the fuel store instead."],
 43: ["Carry it out to the pots.", "A doubt already."],
 44: ["That's your answer — refuse.", "Take it anyway."],
 45: ["Try to work it.", "Out to the rows with nothing."],
 46: ["Out to the rows.", "Back to have it out with him."],
 47: ["Out to the rows, fooled.", "Fling the fouled can down."],
 48: ["Out to the rows.", "Stand a moment in the dark."],
 49: ["Hear the price anyway.", "Refuse and go round."],
 50: ["Nearly across.", "The ice cracks under you."],
 51: ["You go through the ice.", "Throw yourself back while you can."],
 52: ["Push on, spent.", "You dropped the oil on the ice."],
 53: ["The long lane after all.", "Too spent to go on."],
 54: ["Give them your own lamp and coat.", "Promise to send help."],
 55: ["On, colder now.", "Ask about the light in the trees."],
 56: ["Keep moving, keep your head.", "A lit doorway offers a minute."],
 57: ["Warm up, then on.", "Refuse, press on."],
 58: ["The last of the watch.", "On toward the far rows."],
 60: ["Go after them.", "No time — the fires first."],
 61: ["Walk them back.", "On to the fires."],
 62: ["Decide how to start.", "On toward the far rows."],
 63: ["On toward the far rows.", "The last of the watch."],
 64: ["On along the rows.", "The light in the trees."],
 65: ["The family with no fire.", "Press on."],
 67: ["On the way.", "His warning first."],
 68: ["Calm it, and share it out.", "Get to the oil."],
 69: ["Follow the breathing, and find them.", "It's too much — back to the fires."],
}

LV = ("A2", "B1", "B2")
for nid, (a2, b1, b2) in P.items():
    n = nodes[nid]
    n["text"] = {"A2": a2, "B1": b1, "B2": b2}
    if nid in C:
        for j, ct in enumerate(C[nid]):
            n["choices"][j]["text"] = {lv: ct for lv in LV}
json.dump(book, open(EP, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("Patched %d nodes (batch 3)" % len(P))
