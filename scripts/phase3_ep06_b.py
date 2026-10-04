#!/usr/bin/env python3
"""Phase 3 prose for The Orchard — batch 2 (nodes 17-40). Same method as batch 1.
Run: python3 scripts/phase3_ep06_b.py ; then validate (these nodes must be band-clean)."""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
EP = os.path.join(ROOT, "content", "episode-06.json")
book = json.load(open(EP, encoding="utf-8"))
nodes = {n["id"]: n for n in book["nodes"]}

P = {
 17: (
  "The fires come first. The rest can wait a moment. But how do you start? You could get proper oil first. Or you could go straight out to the rows.",
  "Keeping the fires comes first. The rest can wait a moment. But you still have to choose how. You could get proper oil from the store first. Or you could go straight out to the rows and begin.",
  "Keeping the fires lit comes first. Everything else can wait a moment. But you still have to decide how to do it. You could make sure of proper oil at the store before anything else. Or you could go straight out to the rows now and start lighting what you can."),
 18: (
  "The work takes it out of you. Your legs burn and your chest heaves. The cold fights you at every row. You are near your limit. If you fall now, no one is left. So go slow and careful.",
  "The work takes it out of you. Your legs burn, your chest heaves, and the cold fights you at every step. You are near your own limit, and you know it. If you drop here, there is no one left to keep the fires. So go slowly, and go carefully.",
  "The work takes it out of you. Your legs burn, your chest heaves, and the cold fights you at every step. You are near your own limit, and you know it well. If you drop out here, there is no one left to keep the fires alive. So you go slowly. You go carefully. You cannot afford to fall."),
 19: (
  "The village wakes up. People start to move. One man rolls out a barrel of oil. A woman drags out dry wood. A plan grows, door by door. You are not alone now. That changes everything.",
  "The village wakes to itself, and people begin to move. One man rolls out a barrel of oil. A woman drags out dry wood. Door by door, a plan takes shape. You are not doing this alone any more. And that changes everything.",
  "The village wakes to itself, and people begin to move in the dark. One man rolls out a barrel of oil. A woman drags out an armful of dry wood. Door by door, a plan takes shape between you. You are not doing this alone any more. And on a night like this, that changes everything."),
 20: (
  "No one comes out. Doors stay shut. Faces turn from the windows. They are afraid, and afraid people go quiet. You cannot force them. So you go on alone. It is harder this way. But the blossom can't wait.",
  "No one stirs. Doors stay shut, and faces turn from the windows. They are afraid, and afraid people go quiet. You can't force them to help. So you turn away and go on alone. It's harder this way. But the blossom can't wait for them.",
  "No one stirs. Doors stay shut, and faces turn away from the dark windows. They are afraid, and frightened people go quiet. You can't force them, and you don't try. So you turn away and go on alone. It is much harder this way. But the blossom out there cannot wait for anyone to find their courage."),
 21: (
  "The fires are going. Now for the far rows. There are two ways down. The lane is safe but slow. The frozen pond is quick. But in this cold, it could kill.",
  "The near fires are going. Now for the far rows. There are two ways to get down there. The long lane round is safe but slow. The frozen pond is quick, straight across. But in a frost like this, the ice could kill.",
  "The near fires are lit and holding. Now for the far rows, where the cold pools worst. There are two ways to reach them. The long lane round the edge is safe, but slow. Straight across the frozen pond is quick — and a killer in a frost like this one."),
 22: (
  "You take Jack Hale's words to heart. Mind the oil. Keep off the frozen pond. Don't trust the buyer. Hold the fires above all. It is simple, good advice. Now you just have to follow it.",
  "You take Jack Hale's words to heart. Mind the oil carefully. Keep well off the frozen pond. Don't trust the buyer. And hold the fires above everything else. It's simple advice, and good. Now you just have to follow it.",
  "You take old Jack Hale's words to heart. Mind the oil carefully. Keep well off the frozen pond. Don't let the buyer talk you round. And above all else, hold the fires. It is simple advice, and good advice. Now you only have to actually follow it, all night long."),
 23: (
  "The good turn steadies you. Helping someone helps you too. Your head is clearer now. Your hands are surer. There is a hard night still to come. But you feel able to meet it.",
  "You feel steadier for the good turn you did. Helping someone seems, oddly, to steady you too. Your head is clearer, and your hands are surer. There is a hard night still to go. But now you feel able to meet it.",
  "You feel steadier for the good turn you did. Oddly, helping someone else seems to steady you too. Your head is clearer now, and your hands are surer. There is a long, hard night still ahead of you. But you feel able, now, to go out and meet it. The orchard is still out there, waiting for you."),
 24: (
  "A man waits in the lane, a lantern in his hand. It is the buyer. He has oil to sell and a strong back to offer. He smiles too easily. \"The orchard's not your job tonight, friend,\" he says. You have met his kind before.",
  "A man stands in the lane, a lantern swinging in his fist — the buyer. He has oil to sell and a strong back to offer, and he smiles too easily. \"The orchard's not really your job tonight, friend,\" he says. You've met his kind before.",
  "A man stands in the lane, a lantern swinging in his fist. It is the buyer, Rourke. He has oil to sell and a strong back to lend, and he smiles far too easily. \"The orchard's not really your job tonight, friend,\" he says. You have met this kind before, and you know the smile."),
 25: (
  "You lead a small band out to the rows. Together, you all feel stronger. They carry oil and wood. \"This way!\" you call over the cold. And they come. It is a good feeling in a hard hour.",
  "You lead a small band out toward the fires. Walking together, you all feel stronger. They carry oil, wood, and straw. \"This way!\" you call into the cold, and they come. It's a good feeling, in a hard hour.",
  "You lead a small band out toward the fires. Walking together, all of you feel stronger for it. They carry oil, dry wood, and armfuls of straw. \"This way!\" you call into the cold, and they come after you. It is a good feeling to have, in such a hard hour."),
 26: (
  "The lane is black and hard. The cold streams down it. There is no shelter here. But the ground is firm under your feet. And it runs where you need to go. So you keep walking.",
  "The lane is black and hard, the cold pressing down it, no shelter anywhere. But it's solid under your feet, and it runs where you need to go. So you keep walking, step after step.",
  "The lane is black and hard, the cold pressing down the length of it, and there is no shelter anywhere along it. But it is solid under your feet, and it runs exactly where you need to go. So you keep walking, step after cold step, toward the far rows."),
 27: (
  "The frozen pond would halve the way. The far rows are close beyond it. But the ice is thin and black. The cold wants to pull you under. Jack Hale told you to keep off it. He was not joking.",
  "The frozen pond would halve the way, and the far rows lie close beyond it. But the ice is thin, black, and treacherous over deep water. Jack Hale told you to keep off it — and he wasn't joking.",
  "The frozen pond would halve the walking, and the far rows lie close beyond it. But the ice is thin and black over deep, freezing water, and it groans when the cold shifts. Jack Hale told you plainly to keep off it. And he was not joking. You will have to choose, and choose quickly."),
 28: (
  "You step out onto the ice. At once it feels wrong. Deep water waits below, black and cold. Every step is a gamble now. And you are out on it, alone.",
  "You step out onto the ice, and at once it feels wrong. The water waits below, black and deep and freezing. Every step is a gamble now — and you're out on it, alone. There is no going back once you start across.",
  "You step out onto the ice, and at once it feels wrong under you. The water waits below, black and deep and killing cold. Every single step is a gamble now. And you are out on it already, alone, with no one to pull you back. There is no turning back once you are this far out."),
 29: (
  "The straw is damp and won't take. You get only a low, weak flame. It is little use in this cold. You must make do. Or go back to the store for dry straw.",
  "The straw is damp and won't catch. It gives only a low, guttering flame. That's little use in a frost like this. You'll have to make do with it. Or go back to the store for dry straw.",
  "The straw is damp and won't catch properly. It gives only a low, guttering flame that throws no real heat. That is little use against a frost like this one. You will have to make do with what you have. Or you can go back to the store for dry straw and start again."),
 30: (
  "The lane runs on. The frost gets harder by the hour. Below, a cottage has no fire at all. Ahead, the cold nearly knocks you flat. And there is a row-marker, half down in the ground.",
  "The lane runs on along the rows, the cold deepening by the hour. Below, a cottage sits dark, with no fire in it. Ahead, the still, hard air seems to push back at you. And there's a row-marker, half fallen in the frost.",
  "The lane runs on along the rows, and the cold deepens by the hour. Below you, a low cottage sits dark and silent, with no fire lit in it. Ahead, the still and bitter air seems almost to push back against you. And there is an old row-marker, half fallen and stiff with frost."),
 31: (
  "An old man has slipped on the frozen lane. He can't get back up. The cold is taking him fast. Stop, and you lose time. Don't, and the cold may take him for good.",
  "An old man has gone down on the frozen lane and can't get up. The cold is already taking hold of him. Stop, and you lose time you don't have. Don't, and he may not last the hour.",
  "An old man has gone down on the frozen lane and cannot get himself up. The cold has hold of him already, and he is shaking badly. Stop for him, and you lose time you do not have. Don't, and he may not last out the hour on the frozen ground."),
 32: (
  "A family is trapped in a cold house. No fire, no lamp, a child crying in the dark. The parents look at you, tired and without hope. You have a lamp and a coat. It is not much. But it is more than they have.",
  "A family is shut in a freezing house — no fire, no lamp, a child crying in the dark. The parents look at you with tired, hopeless eyes. You have a lamp and a coat of your own. Not much, but more than they've got.",
  "A family is shut in a freezing house, the cold seeping under the door, with no fire and no lamp and a child crying in the dark. The parents look up at you with tired, hopeless eyes. You have a lamp and a warm coat of your own. It is not much. But it is a great deal more than they have."),
 33: (
  "You push on through the worst of it. Each step is a fight now. The cold stings your face. Ahead lie choices. The buyer may be near. Or that light in the far trees. Or you drive straight on for the fires.",
  "You push on through the worst of the cold, each step a fight now, the frost stinging your face. Choices lie ahead. The buyer may be near. There is that strange light out in the far trees. Or you can just drive on for the rows.",
  "You push on through the worst of the cold, and each step is a fight now, the frost stinging your face raw. Several choices lie ahead of you. The buyer may be waiting near. There is still that strange light out among the far trees. Or you can set all of it aside and drive straight on for the rows."),
 34: (
  "You get the old man up and warm him as you can. His eyes fill. He presses a dry sack on you. \"Take it,\" he says, \"for your trouble.\" A small thing. But freely given. You take it and move on.",
  "You get the old man up onto his feet and warm him as best you can. His eyes fill, and he presses a dry sack into your hands. \"Take it,\" he says, \"for your trouble.\" A small thing — but freely given, and you take it and move on.",
  "You get the old man up onto his feet and warm his hands as best you can. His eyes fill, and he presses a dry sack into your arms. \"Take it,\" he says, \"for your trouble.\" It is a small thing. But it is freely given, with nothing asked back. So you take it, thank him, and move on."),
 35: (
  "You can't stop now. But you can't just leave them. So you promise to send help back. \"Hold on!\" you call. \"Stay warm, stay together. I won't forget you.\" And you mean it. Then you turn and go.",
  "You can't stop now — but you can't just leave them, either. So you promise to send help back soon. \"Hold on!\" you shout. \"Stay warm, stay together — I won't forget you.\" You mean it, too. And then you turn and go.",
  "You can't stop now. But you can't simply leave them, either. So you promise to send help back as soon as you can. \"Hold on!\" you shout over the cold. \"Stay warm, stay together — I won't forget you.\" You mean every word of it. And then you make yourself turn and go."),
 36: (
  "The village lights one big fire among the rows. A barrel blazes, throwing heat into the cold. People crowd near it. The old and weak get the best of it. It is not the full rows. But it is a start, and it is warm.",
  "The village lights one big fire among the rows — a barrel ablaze, throwing light and heat into the frost. People crowd near it, the old and the weak given the best of it. It isn't the whole orchard saved. But it's a real warmth, and a beginning.",
  "The village gets one big fire going among the rows — a barrel ablaze, throwing light and heat out into the hard frost. People crowd in near it, and the old and the weak are given the best of the warmth. It is not the whole orchard saved, not yet. But it is a real light, and a real beginning, and you can feel the mood turn."),
 37: (
  "Cottage by cottage, the frightened village becomes a working one. Now people have jobs. One tends the fire. One fetches straw. One watches the rows. Fear turns into doing. And doing beats waiting every time.",
  "Cottage by cottage, the frightened village turns into a working one. People have jobs now: one tends the fire, one carries straw, one watches the rows. Fear turns into doing. And doing beats waiting, every single time.",
  "Cottage by cottage, the frightened, sleepy village turns into a working one. People have real jobs now: one tends the big fire, one carries straw down the rows, one keeps an eye on the thermometer. Fear turns into doing, almost without anyone noticing. And doing beats waiting, every single time."),
 38: (
  "The cold gnaws at your will. A small voice says: stop, go inside, rest. No one would blame you. It would be so easy. But you think of the blossom out there. And you push the voice away. Not yet.",
  "The long cold gnaws at your will. A small voice says: stop, go inside, rest — no one would blame you, and it would be so easy. But you think of the blossom out there on the trees. And you push the voice away. Not yet. Not while it can still be saved.",
  "The long cold gnaws slowly at your will. A small, reasonable voice says: stop now, go inside, rest — no one would blame you, and it would be so easy to do. But then you think of the blossom out there, brittle on every branch. And you push the voice firmly away. Not yet. Not while there is still a chance to save it."),
 39: (
  "You reach the row-marker. The frost has split it, and you can barely read it. One arm points along the rows. The other points out to the far trees. Which way? You will have to guess, and guess right.",
  "You reach the old row-marker, but the frost has cracked and half-toppled it. You can barely read it now. One arm points along the rows. The other points out toward the far trees. Which way? You'll have to guess, and guess right.",
  "You reach the old row-marker, but the cold has cracked and half-toppled it, and you can barely make it out now. One weathered arm points on along the rows. The other points away, out toward the far trees. Which way should you go? You will have to guess — and you will have to guess right."),
 40: (
  "The buyer turns his wide, easy smile on you. \"Cold work, this,\" he says. \"I have oil to sell and a strong back to lend. And the orchard's not really your job tonight, friend.\" His smile never reaches his eyes. You've seen his kind before.",
  "The buyer turns his wide, easy smile on you. \"Cold work, this,\" he says. \"I've oil to sell, and a strong back to lend — and the orchard's not really your job tonight, friend.\" His lantern swings. His smile never reaches his eyes.",
  "The buyer turns his wide, easy smile on you. \"Cold work, this,\" he says. \"I've oil to sell, and a strong back to lend — and the orchard's not really your job tonight, friend.\" His lantern swings gently in his hand. His smile never quite reaches his eyes. You have seen exactly this kind before."),
}

C = {
 17: ["Get proper oil first.", "Straight out to the fires."],
 18: ["The buyer's lantern is ahead.", "Push on."],
 19: ["Lead them out to the fires.", "Light the big fire first."],
 20: ["The fuel store.", "On out to the fires."],
 21: ["Keep to the lane.", "Take the frozen pond.", "The buyer's lantern ahead."],
 22: ["On the way.", "Back to the store."],
 23: ["On with the watch.", "Rouse more hands."],
 24: ["Hear him out.", "Go round him."],
 25: ["This way.", "A light out among the far trees."],
 26: ["Press on.", "Someone's in trouble ahead.", "The whole orchard, white and still."],
 27: ["Risk the frozen pond.", "Too dangerous — back to the lane."],
 28: ["Edge on.", "The ice groans under you."],
 29: ["Out among the rows.", "Back to the store for dry straw."],
 30: ["A family with no fire.", "Press on.", "The cold nearly has you.", "A row-marker, half down."],
 31: ["Help him up.", "You can't stop — the fires."],
 32: ["Give them your own lamp and coat.", "Promise to send help.", "Try to get their stove going."],
 33: ["The buyer again.", "A light out among the far trees.", "The last of the watch.", "The cold makes you doubt."],
 34: ["On your way.", "He tells you of the light in the trees."],
 35: ["Rouse the village.", "On through the cold."],
 36: ["Get the fires lit as well.", "Fetch more hands."],
 37: ["To the far rows.", "The last of the watch."],
 38: ["The last of the watch.", "The buyer's lantern."],
 39: ["The rows.", "The light in the trees."],
 40: ["Hear the price.", "Refuse and go round."],
}

LV = ("A2", "B1", "B2")
for nid, (a2, b1, b2) in P.items():
    n = nodes[nid]
    n["text"] = {"A2": a2, "B1": b1, "B2": b2}
    if nid in C:
        for j, ct in enumerate(C[nid]):
            n["choices"][j]["text"] = {lv: ct for lv in LV}
json.dump(book, open(EP, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("Patched %d nodes (batch 2)" % len(P))
