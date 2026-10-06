#!/usr/bin/env python3
"""Phase 3: pour leveled prose into 'The Keeper' skeleton.

Holds A2/B1/B2 prose for each node (and each choice, in skeleton order) in PROSE, then writes it
onto content/episode-05.json in place. Nodes absent from PROSE keep their stub, so this grows batch
by batch; re-run after each and validate to keep every level in band.

House voice: quiet, humane, a little uncertain — not frightening. The mercy here is a light kept
burning. Nan Bright (the old keeper) is she/her; Ash (the one on the water) is they/them.

Run: python3 scripts/phase3_ep05.py
"""
import json, os, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BOOK = os.path.join(ROOT, "content", "episode-05.json")


def t(a2, b1, b2): return {"A2": a2, "B1": b1, "B2": b2}
PROSE = {}
def P(nid, text, choices): PROSE[nid] = {"text": text, "choices": choices}


# ============================ ACT I — THE LIGHT GOES OUT ===================

P(1,
  t("The worst storm of the year hits after dark. The power fails. The lighthouse beacon dies with it. On the wet stairs, the old keeper Nan Bright falls. She cannot get up. Out past the point, a small boat's lights lift and fall in the waves. The great lamp can be worked by hand. But it is dark now, and that is on you.",
    "The worst storm of the year hits after dark, and the power fails — and the lighthouse beacon dies with it. On the wet iron stairs, the old keeper Nan Bright falls and can't get up. Out past the point, a small boat's lights lift and fall in the swell. The great lamp can still be worked by hand. But it's dark now, and keeping it lit is on you.",
    "The worst storm of the year comes in after dark, and the power fails along the coast — and the lighthouse beacon dies with it. At that exact moment, coming down the wet iron stairs, the old keeper Nan Bright falls and cannot get up, her breath short and a leg gone under her. Out past the point, a small boat's lights lift and fall in the swell, hunting for the harbour mouth. The great lamp is old enough to be worked by hand. But it is dark now, and keeping it lit has become, entirely, your job."),
  [t("Take charge of the light.", "Take charge of the light.", "Take charge of the light."),
   t("Try the radio for help.", "Try the radio for help.", "Try the radio for help."),
   t("See to Nan first.", "See to Nan first.", "See to Nan first.")])

P(2,
  t("You look for what the tower has. There is a can of oil. There are spare wicks and matches. There is a storm-lamp. Outside, the wind screams in the rail. The rain hits the glass like stones. You must decide what to do, and fast.",
    "You gather what the tower has: a can of oil, spare wicks, a box of matches, a good storm-lamp. Outside, the wind screams in the gallery rail and the rain hits the glass like thrown stones. You have to decide what to do, and quickly.",
    "You gather what the tower has to hand: a can of oil, spare wicks, a box of matches, a good storm-lamp. Outside, the wind screams in the gallery rail and the rain hits the glass like handfuls of thrown gravel. Whatever you decide, you understand, you had better decide it fast."),
  [t("Go out into the storm.", "Step out into the storm.", "Step out into the storm."),
   t("Decide how to start.", "Decide how to start.", "Decide how to start."),
   t("The hand-lamp's wick is spoiled.", "The hand-lamp's wick is spoiled.", "The hand-lamp's wick is spoiled.")])

P(3,
  t("You try the radio. It crackles and spits. At last a voice gets through. It is Tam, at the coast station. No lifeboat can go out in a sea like this, he says. Not until it eases, or dawn comes. Keep the light burning if you can.",
    "You try the radio. It crackles and spits, but at last Tam's voice gets through from the coast station. No lifeboat can launch into a sea like this, he says — not until it eases or dawn comes. Keep the light burning, if you can.",
    "You try the radio. It crackles and spits, but at last Tam's voice fights through from the coast station. No lifeboat can launch into a sea like this one, he tells you — not until the storm eases or dawn finally comes. Keep the light burning, if you possibly can. It's all anyone out there has."),
  [t("Decide how to start.", "Decide how to start.", "Decide how to start."),
   t("But that boat can't wait.", "But that boat can't wait.", "But that boat can't wait.")])

P(4,
  t("You go to Nan at the foot of the stairs. You make her as easy as you can. But the light is still dark. Warmth alone will not do. That boat needs the beam. You need oil, and a plan, and to think before you climb.",
    "You get to Nan at the foot of the stairs and make her as easy as you can. But the light is still dark, and shelter alone won't do — that boat out there needs the beam. You need oil, a plan, and a clear head before you climb.",
    "You get to Nan at the foot of the stairs and make her as easy as you can. But the light overhead is still dark, and shelter alone will not do — the boat out past the point needs the beam, not your good intentions. You need oil, and a plan, and a clear head, before you go climbing anywhere."),
  [t("Go back and get the light going.", "Go back and get the light going.", "Go back and get the light going."),
   t("See how serious this is.", "Feel how serious this is.", "Feel how serious this is.")])

P(5,
  t("You step out onto the gallery. The sea is black and huge. The rain is driven flat by the wind. Far off past the point, the boat's lights are small and struggling. Below you, the cove is a well of dark. The whole coast is roaring.",
    "You step out onto the gallery. The sea is black and huge, the rain driven flat by the wind. Far off past the point, the boat's lights show small and struggling. Below you the cove is a well of dark, and the whole coast is roaring.",
    "You step out onto the gallery, and the storm takes you full in the face. The sea is black and vast, the rain driven flat by a wind that shoulders you against the rail, and far off past the point the boat's lights show small and struggling. Below you the cove is a well of pure dark, and the whole coast, end to end, is roaring."),
  [t("Tam opens the oil store.", "Tam opens the oil store.", "Tam opens the oil store."),
   t("Knock on the cottages for help.", "Knock along the cottages for help.", "Knock along the cottages for help."),
   t("Decide how to start.", "Decide how to start.", "Decide how to start."),
   t("Someone's out on the head.", "Someone's out on the head.", "Someone's out on the head.")])

P(6,
  t("You stand and think. You could get the light going first. You could see to Nan and the rest. Or you could knock on doors and find people to help. Each choice takes time. And tonight, time is a boat on the rocks.",
    "You make yourself think. You could get the light going first, and worry about the rest after. You could go straight to Nan and the cottages. Or you could rouse the coast to help. Each choice costs time — and tonight, time is a boat closing on the rocks.",
    "You make yourself stand still and think it through. You could get the light going first and worry about everything else after. You could go straight to Nan and the frightened cottages below. Or you could rouse the whole coast to help. Every choice costs time — and out here tonight, time is measured in how far a boat has drifted toward the rocks."),
  [t("The oil store.", "The oil store.", "The oil store."),
   t("Straight up to the lamp.", "Straight up to the lamp.", "Straight up to the lamp."),
   t("Rouse the coast for help.", "Rouse the coast for help.", "Rouse the coast for help.")])

P(8,
  t("You feel the storm in your chest. And you think of that boat, out past the point. It is closing on the rocks with no light to steer by. A night like this can drown a whole crew. That is not a fear. It is a fact. No one else will climb that tower. So it is you.",
    "You feel the storm settle into your chest. You think of that boat out past the point, closing on the rocks with no light to steer by. A night like this can drown a whole crew. That isn't a fear; it's a fact. No one else is going to climb that tower. So it has to be you.",
    "You feel the storm settle heavy in your chest, and you think of the boat out past the point, closing on the rocks with no light at all to steer by. A night like this one can drown a whole crew and leave nothing by morning. That is not a fear any more; it is simply a fact. No one else is going to climb that tower. So, ready or not, it has to be you."),
  [t("Decide how to start.", "Decide how to start.", "Decide how to start."),
   t("To the oil store.", "To the oil store.", "To the oil store."),
   t("A scramble at the store.", "A scramble at the store.", "A scramble at the store.")])

P(9,
  t("Tam heaves open the oil store. Inside there is a barrel of oil. There are spare wicks and a box of matches. There is a good storm-lamp and dry rope. \"Take what you need,\" he says. \"I'll work the radio.\" He is a steady man, and tonight it shows.",
    "Tam heaves open the oil store: a barrel of oil, spare wicks, a box of matches, a good storm-lamp, dry rope. \"Take what you need,\" he says. \"I'll stay on the radio.\" He's a steady man, and on a night like this it shows.",
    "Tam heaves open the heavy door of the oil store: a barrel of oil, spare wicks, a box of matches, a good storm-lamp, a coil of dry rope. \"Take whatever you need,\" he says over the wind. \"I'll stay on the radio and raise who I can.\" He has always been a steady man, and on a night like this one it shows."),
  [t("Take charge of the oil and wick.", "Take charge of the oil and wick.", "Take charge of the oil and wick."),
   t("Just a storm-lamp and rope.", "Just a storm-lamp and rope.", "Just a storm-lamp and rope."),
   t("Ask Tam what he knows.", "Ask Tam what he knows.", "Ask Tam what he knows."),
   t("He gives you the last dry lamp.", "He presses the last dry lamp on you.", "He presses the last dry lamp on you.")])

P(10,
  t("You knock along the cottages. Old Da Finch opens up, pale in the dark. His lamp is dead. He has no matches. His hands shake. \"I can't get it lit,\" he says. You have a long night ahead. But he is here, and he is scared, and he is asking.",
    "You knock along the cottages, and old Da Finch opens up, pale in the dark — his lamp dead, no matches, his hands shaking. \"I can't get it lit,\" he says. You've a long night ahead of you. But he's here, and he's scared, and he's asking you.",
    "You knock along the cottages, and old Da Finch opens up, pale and small in the dark — his lamp dead, no matches to hand, his fingers shaking too hard to strike one anyway. \"I can't get it lit,\" he says, and there's real fear in it. You have a long, hard night ahead of you. But Da Finch is here, in front of you, and he is frightened, and he is asking."),
  [t("Stop and help him.", "Stop and help him.", "Stop and help him."),
   t("Go and keep the light.", "Say you must keep the light.", "Say you must keep the light.")])

P(11,
  t("You climb up to the lamp fast, with what little you have. A match, a spark, a small flicker of flame. It catches — but it is weak. It will not hold without proper oil. You cannot leave it like this and hope.",
    "You climb up to the lamp fast with what little you have. A match, a spark, a flicker of flame — it catches, but it's weak, and it won't hold without proper oil. You can't just leave it like this and hope.",
    "You climb up to the lamp fast with what little you have to hand. A match, a spark, a thin flicker of flame — it catches, just, but it's weak and hungry, and it will not hold through the night without proper oil to feed it. Leaving it like this and hoping is not a plan, and you know it."),
  [t("Find more oil.", "Decide how to get real oil.", "Decide how to get real oil."),
   t("The climb tires you.", "The climb takes it out of you.", "The climb takes it out of you.")])

P(12,
  t("You go from cottage to cottage. You ask each door the same thing. Bring wood for a fire. Lend a hand on the rope. Help me hold the light. Some faces turn away. But some turn out into the storm. It only takes a few to start.",
    "You go cottage to cottage, asking each door the same thing. Bring wood for a signal fire, lend a hand on the rope, help me hold the light. Some turn away. But a few pull on their coats and come out into the storm — and it only takes a few to begin.",
    "You go cottage to cottage, hammering on each door and asking the same thing: bring wood for a signal fire, lend a hand on the rope, help me hold the light. Some faces turn away from the cold and the risk. But a few pull on their coats and step out into the storm with you — and it only ever takes a few to begin the rest."),
  [t("The coast turns out.", "The coast turns out.", "The coast turns out."),
   t("No one stirs; go alone.", "No one stirs; go on alone.", "No one stirs; go on alone.")])

P(13,
  t("You take charge of the oil and wick. The can is heavy in your arms. Every drop matters now. Tend it well, and the lamp will burn all night. Waste it, and the light goes dark. So you hold it close, and you climb.",
    "You take charge of the oil and wick. The can is heavy, and every drop of it matters now. Tended well, it'll keep the lamp burning all night; wasted, and the light goes dark. So you hold it close and start to climb.",
    "You take charge of the oil and the wick, and the can hangs heavy and precious from your fist. Every drop of it matters now. Tended carefully, it will keep the lamp burning right through the night; spilled or squandered, and the light goes dark and a boat dies for it. So you hold it close, and you start to climb."),
  [t("Now, up to the lamp.", "Now, up to the lamp.", "Now, up to the lamp."),
   t("Thank Tam.", "Thank Tam.", "Thank Tam.")])

P(14,
  t("You take a storm-lamp and a coil of rope. They give you some light, and a way to tie on. But it is not the beam. And you have no proper oil set by. You will still need real oil, and soon, or the tower stays dark.",
    "You take a storm-lamp and a coil of rope. They give you some light and a way to tie yourself on — but not the beam, and you've no proper oil set by. You'll still need real oil, and soon, or the tower stays dark.",
    "You take a storm-lamp and a coil of rope. They give you a little light and a way to tie yourself on against the wind — but they are not the beam, and you have no proper oil set by for the great lamp. You will still have to find real oil, somewhere, and soon, or the whole tower stays dark over the rocks."),
  [t("Find more oil.", "Now, find real oil.", "Now, find real oil."),
   t("Ask Tam what he knows.", "Ask Tam what he knows.", "Ask Tam what he knows.")])

P(15,
  t("Bosun Carrick knows this coast. He has kept it many years. \"Stay off the cliff path,\" he says. \"It looks quick. It kills.\" He warns you about the wrecker too. \"Mind your oil. Hold the light. That's the whole of the job tonight.\"",
    "Bosun Carrick knows this coast; he's watched it for years. \"Stay off the cliff path,\" he says. \"It looks quick. It kills.\" He warns you off the wrecker too. \"Mind your oil, hold the light — that's the whole of the job tonight.\"",
    "Bosun Carrick has watched this coast in the dark for more years than he'll admit. \"Stay off the cliff path,\" he tells you, low and certain. \"It looks quick. It kills.\" He warns you, too, about the man working the cove. \"Mind your oil, and hold the light. That is the whole of the job tonight, and it's enough.\""),
  [t("Take it to heart.", "Take it to heart.", "Take it to heart."),
   t("On with it.", "On with it.", "On with it.")])

P(16,
  t("You settle Da Finch with a lit lamp and a blanket. Slowly, his shaking eases. \"Bless you,\" he says. His hand grips yours. You promise to look in again. Then you turn back to the storm.",
    "You settle Da Finch with a lit lamp and a blanket, and slowly his shaking eases. \"Bless you,\" he says, gripping your hand. You promise to look in on him again, and turn back to the storm.",
    "You settle Da Finch with a lit lamp and a blanket, and little by little the worst of his shaking eases off. \"Bless you,\" he says, gripping your hand with a strength that surprises you. You promise to look in on him again before the night's out, and then you turn, reluctantly, back into the storm."),
  [t("On up to the lamp.", "On up to the lamp.", "On up to the lamp."),
   t("Check the others too.", "He asks you to check the others.", "He asks you to check the others.")])

P(17,
  t("You press on to keep the light. That comes first. Everything else can wait a while. But you still have to choose how. Do you get proper oil first? Or climb straight to the lamp?",
    "You press on to keep the light; that comes first, and the rest can wait a moment. But you still have to decide how — secure proper oil first, or climb straight up to the lamp.",
    "You press on to keep the light, because that comes before everything else and most of the rest can wait a little longer. Even so, you still have to decide the how of it: whether to secure proper oil first and carry it up, or climb straight to the lamp and coax what flame you can."),
  [t("Get oil first.", "The oil store first.", "The oil store first."),
   t("Straight up to the lamp.", "Straight up to the lamp.", "Straight up to the lamp.")])

P(18,
  t("The climb takes it out of you. Your legs burn. Your chest heaves. The wind fights you on every stair. You are near your limit, and you know it. If you fall, no one is left to keep the light. So go slow. Hold the rail.",
    "The climb takes it out of you — legs burning, chest heaving, the wind fighting you on every stair. You're near your own limit, and you know it. If you fall here, there's no one left to keep the light. So go slow, and hold the rail.",
    "The climb takes it out of you: legs burning, chest heaving, the wind clawing at you through the gaps on every iron stair. You are near your own limit, and you are clear-headed enough, still, to know it. If you fall here, there is no one left to keep the light for that boat. So you go slow. You hold the rail."),
  [t("The wrecker's lantern is ahead.", "The wrecker's lantern is ahead.", "The wrecker's lantern is ahead."),
   t("Push on.", "Push on.", "Push on.")])

P(19,
  t("The coast wakes to itself. People start to move. One man rolls up a barrel of oil. A woman brings dry wood. A plan takes shape, door by door. You are not alone in this now. That changes everything.",
    "The coast wakes to itself. People begin to move. One man rolls up a barrel of oil, a woman drags out dry wood, and a plan takes shape door by door. You aren't doing this alone any more — and that changes everything.",
    "The coast seems to wake up to itself. People begin to move, and to help. One man rolls a barrel of oil up from a shed he'd kept quiet about. A woman drags out an armful of dry wood for the fire. A plan takes shape along the shore, door by door. You are not doing this alone any more — and that, more than anything, changes what the night can become."),
  [t("Lead them up to the light.", "Lead them up to the light.", "Lead them up to the light."),
   t("Light the signal fire first.", "Light the signal fire first.", "Light the signal fire first.")])

P(20,
  t("No one stirs. Doors stay shut. Faces turn from the window. They are afraid, and afraid people go quiet. You cannot force them. So you turn away, and go on alone. It is harder this way. But that boat cannot wait.",
    "No one stirs. Doors stay shut, faces turn from the windows — they're afraid, and afraid people go quiet. You can't force them. So you turn away and go on alone; it's harder this way, but that boat can't wait for them to be brave.",
    "No one stirs. Doors stay shut against the weather; faces turn away from the black windows, saying nothing — because they are frightened, and frightened people go still and quiet. You cannot force courage into anyone. So you turn away and go on alone; it is harder this way, and slower, but that boat out past the point cannot wait for a coast to find its nerve."),
  [t("The oil store.", "The oil store.", "The oil store."),
   t("On up to the lamp.", "On up to the lamp.", "On up to the lamp.")])

P(21,
  t("The light is sorted. Now for the cove and that boat. There are two ways down. You can keep to the long path round the head. It is safe, but slow. Or you can take the cliff path straight down. It is quick — and it is a killer.",
    "The light's sorted; now for the cove and that boat. There are two ways down. The long path round the head is safe but slow. The cliff path straight down is quick — and a killer in a wind like this.",
    "The light is sorted, more or less, and now there's the cove and that boat to reach. Two ways lead down to the water. You can keep to the long path round the head, which is safe enough but slow. Or you can take the cliff path straight down: far quicker, and, in a wind like tonight's, an outright killer."),
  [t("Keep to the path.", "Keep to the path.", "Keep to the path."),
   t("Take the cliff path.", "Take the cliff path.", "Take the cliff path."),
   t("The wrecker's lantern ahead.", "The wrecker's lantern ahead.", "The wrecker's lantern ahead.")])

P(22,
  t("You take Carrick's words to heart. Mind the oil. Keep off the cliff. Don't trust the wrecker. Hold the light. It is good advice, and simple. Now you just have to follow it.",
    "You take Carrick's words to heart. Mind the oil carefully, keep well off the cliff, don't trust the wrecker, and hold the light above all else. It's simple advice, and good. Now you just have to actually follow it, out here in the dark and the wind.",
    "You take Carrick's words to heart, one by one: mind the oil carefully, keep well off the cliff path, put no trust in the wrecker, and hold the light whatever it costs. It is simple advice, and good — the kind that is easy to nod at and hard, when the wind is screaming, to actually keep."),
  [t("On the way.", "On the way.", "On the way."),
   t("Back to the store.", "Back to the store.", "Back to the store.")])

P(23,
  t("You feel steadier for the good turn you did. Helping someone helps you too, somehow. Your head is clearer now. Your hands feel surer. There is a hard night still to go. But you can do it.",
    "You feel steadier for the good turn you did — helping someone seems, oddly, to steady you too. Your head is clearer, your hands surer. There's a hard night still to go, but you feel able to meet it.",
    "You feel steadier for the good turn you did; helping someone, it turns out, steadies you as well, in some quiet way you couldn't name. Your head is clearer than it was, your hands surer on the rope. There is a long, hard night still ahead — but, for the first time, you feel able to meet it."),
  [t("On with the watch.", "On with the watch.", "On with the watch."),
   t("Rouse more hands.", "Rouse more hands.", "Rouse more hands.")])

P(24,
  t("A man stands in the surf, a lantern swinging in his fist. It is the wrecker. He has oil to sell, and a strong back to lend. He smiles too easily. \"The light's not your job tonight, friend,\" he says. You have heard men like him before.",
    "A man stands in the surf, a lantern swinging in his fist — the wrecker. He has oil to sell and a strong back to offer, and he smiles too easily. \"The light's not your job tonight, friend,\" he says. You've met his kind before.",
    "A man stands braced in the surf, a lantern swinging in his fist — the wrecker. He has oil to sell, he says, and a strong back to lend, and he smiles far too easily for a night like this. \"The light's not really your job tonight, friend,\" he says. You have met his kind before, and you know what their help costs."),
  [t("Hear him out.", "Hear him out.", "Hear him out."),
   t("Go round him.", "Go round him.", "Go round him.")])

P(25,
  t("You lead a small band up toward the light. Walking together, you feel stronger. They carry oil, and wood, and rope. \"This way,\" you call, over the wind. And they come. It is a good feeling, in a hard hour.",
    "You lead a small band up toward the light. Walking together, you all feel stronger; they carry oil, wood, rope. \"This way!\" you call over the wind, and they come — a good feeling, in a hard hour.",
    "You lead a small band up toward the light, and walking together, into the teeth of it, all of you seem to stand a little straighter. They carry oil, and wood, and coils of rope between them. \"This way!\" you call over the wind, and they come — which is a surprisingly good feeling, in an hour as hard as this one."),
  [t("The way.", "The way.", "The way."),
   t("The light on the water.", "The light out on the water.", "The light out on the water.")])

P(29,
  t("The hand-lamp's wick is spoiled. It gives only a low, guttering flame. It will not throw far. It is not much use in a storm like this. You will have to make do, or go back for a better one.",
    "The hand-lamp's wick is spoiled; it gives only a low, guttering flame that won't throw far. It's little use in a storm like this. You'll have to make do — or go back to the store for a better one.",
    "The hand-lamp's wick turns out to be spoiled, giving only a low, guttering flame that won't throw any distance at all. It is next to no use in a storm like this one. You will have to make do with it as it is — or go back to the store and hope for something better."),
  [t("Out into the storm.", "Out into the storm.", "Out into the storm."),
   t("Back for a better one.", "To the store for better.", "To the store for better.")])

P(36,
  t("The coast lights one signal fire on the head. A barrel of oil goes up in flame. It throws light and heat into the storm. People crowd near it. The weak and the old get the best of it. It is not the beam. But it is a light, and it is shared.",
    "The coast lights one signal fire on the head — a barrel ablaze, throwing light and heat into the storm. People crowd near it, the old and the weak given the best of it. It isn't the beam. But it's a light, and it belongs to everyone now.",
    "Together, the coast gets one signal fire lit on the head: a barrel of oil ablaze, throwing light and heat out into the storm. People crowd near it, the old and the weak settled into the best of the warmth. It is not the beam that turns over the rocks. But it is a light, and, better than that, it is a light the whole shore now shares."),
  [t("Light the beam above it.", "Get the beam lit above it.", "Get the beam lit above it."),
   t("Fetch more hands.", "Fetch more hands.", "Fetch more hands.")])

P(37,
  t("Cottage by cottage, the scared shore becomes a working one. People have jobs now. One tends the fire. One coils the rope. One watches the sea. Fear turns into doing. And doing is far better than waiting.",
    "Cottage by cottage, the frightened shore becomes a working one. People have jobs now — one tends the fire, one coils the rope, one watches the sea. Fear turns into doing, and doing beats waiting every time.",
    "Cottage by cottage, the frightened shore turns into a working one. People have jobs now, small and clear ones: one tends the signal fire, one coils and checks the rope, one keeps their eyes on the black water. Fear becomes doing — and doing, you have always found, beats sitting and waiting every single time."),
  [t("To the cove.", "To the cove.", "To the cove."),
   t("The last of the watch.", "The last of the watch.", "The last of the watch.")])

P(60,
  t("Someone points to the head. A figure has gone out that way, into the storm. Out toward the point, alone. That way lies only rock and wind and the black drop. If no one goes after them, they will not come back.",
    "Someone points to the head: a figure has gone out that way, into the storm, out toward the point and alone. That way lies nothing but rock, wind and the black drop. If no one goes after them, they won't come back.",
    "Someone catches your arm and points to the head: a figure has gone out that way, into the storm, out toward the point and quite alone. That way lies nothing at all but wet rock, screaming wind, and the black drop to the sea. If no one goes after them now, everyone seems to understand, they will not come back on their own."),
  [t("Go after them.", "Go after them.", "Go after them."),
   t("No time — the light first.", "No time — the light first.", "No time — the light first.")])

P(61,
  t("You find them clinging in the rocks. They are half-drowned, and lost, and shaking. The wind tears at their coat. They do not seem to know your face. You take a firm hold of their arm. \"Come with me,\" you shout. \"This way. Slowly.\"",
    "You find them clinging in the rocks, half-drowned and lost, the wind tearing at their coat. They don't seem to know your face. You take a firm hold of their arm. \"Come with me!\" you shout over the storm. \"This way. Slowly now.\"",
    "You find them at last, clinging in the rocks, half-drowned and lost, the wind tearing at their coat and no recognition in their face when they turn it up to you. You take a firm hold of their arm, the way Carrick would. \"Come with me!\" you shout over the storm, keeping your grip sure. \"This way. Slowly does it.\""),
  [t("Walk them back.", "Walk them back.", "Walk them back."),
   t("On to the light.", "On to the light.", "On to the light.")])

P(62,
  t("You cannot do everything. The light needs you most. So you send word for someone else to go. Then you press on. It sits badly with you. But you have to choose, and you choose the light.",
    "You can't do everything at once, and the light needs you most. So you send word for someone else to go after them, and press on. It sits badly with you — but you have to choose, and you choose the light.",
    "You cannot do everything at once, and the light, of everything, needs you most. So you send word back for someone else to go after the lost figure, and you press on. It sits badly with you, this choosing — but choosing is exactly what the night keeps demanding, and this time you choose the light."),
  [t("Decide how to start.", "Decide how to start.", "Decide how to start."),
   t("On toward the cove.", "On toward the cove.", "On toward the cove.")])

P(63,
  t("You walk them back to the cottages. Their family cries out with relief. They wrap you in a dry coat and give you a place by the fire. \"Thank you,\" they say, again and again. A kindness never stays still. It moves.",
    "You walk them safely back to the cottages, where their family cries out with relief. They wrap you in a dry coat and make you a place by the fire. \"Thank you,\" they keep saying — because a kindness never stays still; it moves.",
    "You walk them all the way back to the cottages, where their family cries out with relief and half-falls on the two of you. They wrap you in a dry coat and press you toward the best place by the fire. \"Thank you,\" they keep saying, over and over — and you think, not for the first time, that a kindness never really stays where you leave it. It moves."),
  [t("On toward the cove.", "On toward the cove.", "On toward the cove."),
   t("The last of the watch.", "The last of the watch.", "The last of the watch.")])

P(67,
  t("Tam presses the last dry lamp on you. \"For the climb,\" he says. \"Go on. I'll stay on the radio.\" His face is grey with worry. He wants to help, and this is how he can. You take it, and you thank him.",
    "Tam presses the last dry lamp on you. \"For the climb,\" he says. \"Go on — I'll stay on the radio.\" His face is grey with worry. This is the help he has to give, and he gives it. You take it, and thank him.",
    "Tam presses the last genuinely dry lamp into your hands. \"For the climb,\" he says. \"Go on — I'll stay here on the radio and raise who I can.\" His face is grey with worry. And you understand that this small thing is the help he has to give, so he is giving it. You take the lamp, and you thank him, and you mean it."),
  [t("On the way.", "On the way.", "On the way."),
   t("His warning first.", "His warning first.", "His warning first.")])

P(68,
  t("At the oil store, people rush the cans. Voices rise. Hands grab. Fear has caught, and it spreads fast. One more shove and it will be a fight. You have a choice. Calm them, and share it out. Or push your own way in.",
    "At the oil store, people are rushing the cans — voices rising, hands grabbing, fear catching and spreading fast. One more shove and it's a fight. You can try to calm them and share it out fairly, or push your own way through to the oil.",
    "At the oil store, people have begun to rush the cans: voices climbing, hands grabbing, fear catching like a spark in dry grass and spreading down the line. One more shove and it becomes an outright fight over the oil. You have a choice to make, and quickly — try to calm them and share it out fairly, or simply push your own way through to what you need."),
  [t("Calm them, share it.", "Calm it, and share it out.", "Calm it, and share it out."),
   t("Get to the oil.", "Get to the oil.", "Get to the oil.")])


# ============================ ACT II — THE LONG WATCH =====================

P(26,
  t("The head path is black and hard. The rain runs down it in streams. The wind pushes at your back. There is no shelter at all. But the path is solid, and it goes where you need to go. You keep walking.",
    "The head path is black and hard, rain streaming down it, the wind shoving at your back, no shelter anywhere. But it's solid underfoot, and it runs where you need to go. So you keep walking.",
    "The head path is black and hard going, rain streaming down it in ropes, the wind shoving at your back and then, without warning, in your face. There is no shelter anywhere along it. But it is solid underfoot, at least, and it runs where you need it to run. So you put your head down and keep walking."),
  [t("Press on.", "Press on.", "Press on."),
   t("Someone's in trouble ahead.", "Someone's in trouble ahead.", "Someone's in trouble ahead."),
   t("The whole coast, dark and roaring.", "The whole coast, dark and roaring.", "The whole coast, dark and roaring.")])

P(27,
  t("The cliff path would cut the way in half. The cove is close below. But the path is a narrow ledge. The rock is wet. The drop is black. And the wind wants to throw you off it. Carrick said to stay off it. He was not joking.",
    "The cliff path would halve the way, and the cove is close below. But it's a narrow ledge of wet rock over a black drop, and the wind wants to throw you off it. Carrick told you to stay off it — and he wasn't joking.",
    "The cliff path would halve the way, and from here the cove looks close enough below to reach in minutes. But the path is a narrow ledge of streaming wet rock over a black drop, and the wind, gusting hard, plainly wants to peel you off it. Carrick told you flatly to stay off the cliff — and Carrick, you already know, was not joking."),
  [t("Risk the cliff path.", "Risk the cliff path.", "Risk the cliff path."),
   t("Too risky — back to the path.", "Too dangerous — back to the path.", "Too dangerous — back to the path.")])

P(28,
  t("You step out onto the ledge. At once, it feels wrong. The drop yawns below you, black and deep. The wind slams the cliff and pulls at your coat. Every step is a gamble. And you are out on it now, alone.",
    "You step out onto the ledge, and at once it feels wrong. The drop yawns below, black and deep; the wind slams the cliff and drags at your coat. Every step is a gamble — and you're out on it now, alone.",
    "You step out onto the ledge, and almost at once it feels wrong. The drop yawns below you, black and deep and hungry; the wind slams into the cliff and drags at your coat with both hands. Every single step is a gamble against the gust. And you are out on it now, committed, entirely alone."),
  [t("Edge on.", "Edge on.", "Edge on."),
   t("The wind slams the cliff.", "The wind slams the cliff.", "The wind slams the cliff.")])

P(30,
  t("The path runs on along the head. The storm gets worse by the hour. Below you, a low cottage has the sea coming in. Ahead, the wind nearly knocks you flat. There is a marker post too, half torn away by the gale.",
    "The path runs on along the head, the storm worsening by the hour. Below, a low cottage has the sea coming in. Ahead, the wind nearly knocks you flat. And there's a marker post, half torn away by the gale.",
    "The path runs on along the head, the storm deepening by the hour until each gust seems to want something from you. Below the path, a low cottage has the sea coming in under its door. Ahead, a gust nearly knocks you flat against the rock. And off to one side stands a marker post, half torn away by the wind."),
  [t("A flooding cottage.", "A family in a flooding cottage.", "A family in a flooding cottage."),
   t("Press on.", "Press on.", "Press on."),
   t("The wind nearly floors you.", "The wind nearly has you off your feet.", "The wind nearly has you off your feet."),
   t("A half-gone marker post.", "A marker post, half torn away.", "A marker post, half torn away.")])

P(31,
  t("A small boat is swamped on the slip. An old man is caught in the lines. The sea drags at him. He cannot pull free. If you stop, you lose time. If you don't, the next big wave may take him.",
    "A small boat is swamped on the slip, an old man caught in the lines, the sea dragging at him — he can't pull free. Stop, and you lose time; don't, and the next big wave may take him.",
    "A small boat lies swamped on the slip, an old man caught fast in the lines, the sea dragging at him with every surge and hauling him toward the deep water. He cannot pull himself free. If you stop, you lose time you can't spare; if you don't, there's a real chance the next big wave takes him for good."),
  [t("Help cut him free.", "Help cut him free.", "Help cut him free."),
   t("Can't stop — the light.", "You can't stop — the light.", "You can't stop — the light.")])

P(32,
  t("A family is in a low cottage. The sea is coming in under the door. They have no lamp. A child is crying in the dark. The parents look at you with tired eyes. You have a lamp and a coat. Not much. But more than they have.",
    "A family is trapped in a low cottage, the sea coming under the door, no lamp, a child crying in the dark. The parents look at you with tired, hopeless eyes. You've a lamp and a coat of your own — not much, but more than they've got.",
    "A family is trapped in a low cottage with the sea already coming in under the door, no lamp lit, a small child crying somewhere in the dark. The parents turn to you with tired, half-hopeless eyes, not quite asking. You have a lamp and a coat of your own — not much, and every bit of it already spoken for, but more, all the same, than they have."),
  [t("Give them your lamp and coat.", "Give them your own lamp and coat.", "Give them your own lamp and coat."),
   t("Promise to send help.", "Promise to send help.", "Promise to send help."),
   t("Bank the door against the water.", "Try to bank the door against the water.", "Try to bank the door against the water.")])

P(33,
  t("You go on through the worst of the storm. Each step is a fight now. The rain stings your face. Ahead, you have choices to make. The wrecker may be near. So may the strange light on the water. Or you can push for the tower.",
    "You push on through the worst of the storm, each step a fight now, the rain stinging your face. Ahead lie choices: the wrecker may be near, or the strange light on the water — or you can just drive for the tower.",
    "You push on through the very worst of the storm, each step a fight against the wind, the rain stinging your face like grit. Ahead of you, the night fans out into choices again. The wrecker is somewhere near, and so is that strange second light on the water. Or you can put your head down and simply push for the tower and the lamp."),
  [t("The wrecker again.", "The wrecker again.", "The wrecker again."),
   t("The light on the water.", "The light out on the water.", "The light out on the water."),
   t("The last of the watch.", "The last of the watch.", "The last of the watch."),
   t("The storm makes you doubt.", "The storm makes you doubt.", "The storm makes you doubt.")])

P(34,
  t("You cut the old man free, and the boat lets him go. His eyes fill. He presses a dry oilskin on you. \"Take it,\" he says. \"For your trouble.\" It is a small thing. But it is given with a full heart. You take it, and go on.",
    "You cut the old man free, and the boat lets him go. His eyes fill; he presses a dry oilskin on you. \"Take it,\" he says, \"for your trouble.\" A small thing — but freely given, and you take it and move on.",
    "You saw through the lines at last, and the swamped boat lets the old man go. His eyes fill with tears the wind whips away; he presses a dry oilskin into your hands. \"Take it,\" he insists. \"For your trouble.\" It is a small thing against the night — but it is given with a full heart, and you take it, and thank him, and go on."),
  [t("On your way.", "On your way.", "On your way."),
   t("He tells you of the light on the water.", "He tells you of the light on the water.", "He tells you of the light on the water.")])

P(35,
  t("You cannot stop, not now. But you cannot just leave them either. So you promise to send help back. \"Hold on,\" you shout. \"Stay high. I will not forget you.\" You mean it. Then you turn, and go.",
    "You can't stop now — but you can't just leave them, either. So you promise to send help back. \"Hold on!\" you shout. \"Stay high, stay together — I won't forget you.\" You mean it, too — and then you turn and go.",
    "You can't stop now, not with the light waiting — but neither can you simply pass them by. So you promise to send help back the moment you can. \"Hold on!\" you shout over the wind, meeting the parents' eyes. \"Stay high, keep the child close. I won't forget you.\" You mean every word of it. And then you make yourself turn, and go."),
  [t("Rouse the coast.", "Rouse the coast.", "Rouse the coast."),
   t("On through the storm.", "On through the storm.", "On through the storm.")])

P(38,
  t("The storm gnaws at your will. A small voice in you says stop. Get inside. Rest. No one would blame you. It would be so easy. But you think of that boat, and you push the voice away. Not yet. Not while the light is dark.",
    "The storm gnaws at your will. A small voice says: stop, get inside, rest — no one would blame you, and it would be so easy. But you think of that boat on the rocks, and you push the voice away. Not yet. Not while the light is dark.",
    "The storm gnaws steadily at your will, and a small, reasonable voice inside you says: stop now, get inside, rest a while. No one on earth would blame you, and, God, it would be easy. But you make yourself think of that boat closing on the rocks, and you push the voice back down where it came from. Not yet. Not while the light is still dark."),
  [t("The last of the watch.", "The last of the watch.", "The last of the watch."),
   t("The wrecker's lantern.", "The wrecker's lantern.", "The wrecker's lantern.")])

P(39,
  t("You reach the marker post. The gale has torn half of it away. You can barely read it. One arm points along the path. One arm points out toward the water. Which way? You have to guess, and guess well.",
    "You reach the marker post, but the gale has torn half of it away; you can barely read it. One arm points along the path, the other out toward the water. Which way? You'll have to guess, and guess right.",
    "You reach the marker post at last, and find the gale has torn half of it clean away — you can barely make out what's left. One weathered arm points on along the path; the other points out, unmistakably, toward the water. Which way? There is no one to ask, so you will have to guess, and you had better guess right."),
  [t("The path.", "The path.", "The path."),
   t("The light on the water.", "The light on the water.", "The light on the water.")])

P(50,
  t("Far out on the ledge, the cove looks nearer at last. Or does it? You cannot tell any more. The dark plays tricks. The wind plays tricks. Your tired eyes play tricks. You are soaked and shaking. But you edge on.",
    "Far out on the ledge, the cove seems nearer at last — or does it? You can't be sure any more; the dark plays tricks, the wind plays tricks, your tired eyes play tricks. You're soaked and shaking. But you edge on.",
    "Far out on the ledge, the cove seems, at last, to be nearer — or does it? You honestly can't tell any more, because the dark plays tricks, and the wind plays tricks, and your soaked, exhausted eyes play the worst tricks of all. You are shaking with cold and effort. But you make yourself edge on, because stopping out here is the one thing you can't do."),
  [t("Nearly down.", "Nearly down.", "Nearly down."),
   t("The rock crumbles.", "The rock crumbles under you.", "The rock crumbles under you.")])

P(51,
  t("The ledge, the wind, the black drop below. Your foot slips on the wet rock. Your heart slams. This is the moment. Go off the edge into the dark. Or throw yourself back, now, while you still can.",
    "The ledge, the wind, the black drop below — and your foot slips on the wet rock. This is the moment: go off the edge into the dark, or throw yourself back from it now, while you still can.",
    "The ledge, the wind, the black drop yawning below — and then your foot slips on the streaming wet rock and your heart slams up into your throat. This is the moment, then, the one Carrick warned you about. Go off the edge into the dark, with no one to see — or throw yourself back from it now, hard, while some small part of you still can."),
  [t("You go off the edge.", "You go off the edge.", "You go off the edge."),
   t("Throw yourself back.", "Throw yourself back from the edge while you can.", "Throw yourself back from the edge while you can.")])

P(52,
  t("You reach the cove at last. You are soaked and shaking. Your hands are torn. But you are down. Somehow, you made it. Now you must decide. Push on, spent as you are. Or face what you lost on the way.",
    "You reach the cove at last, soaked and shaking, your hands torn — but down. Somehow, you made it. Now you have to decide: push on, spent as you are, or face what you lost on the way.",
    "You reach the cove at last, soaked and shaking and with your hands torn raw on the rock — but down, all the same. Somehow, against everything, you made it. Now you have to decide what comes next: push on, spent as you are and running on nothing, or turn and face whatever it was you lost somewhere back on that ledge."),
  [t("Push on, spent.", "Push on, spent.", "Push on, spent."),
   t("You lost the oil.", "You dropped the oil in the scramble.", "You lost the oil in the scramble.")])

P(53,
  t("You throw yourself back from the edge while you still can. It is the hard, right choice. You crawl the last part on your hands and knees. When you reach the path, you are shaken and slow. The night is burning away. But you are alive, and still able to help.",
    "You throw yourself back from the edge while you still can — the hard, right choice. You crawl the last stretch on hands and knees, and reach the path shaken and slow. The night's burning away. But you're alive, and still able to help.",
    "You throw yourself back from the edge while some part of you still can, and it is the hard, right choice, though it costs you the last of everything. You crawl the final stretch on your hands and knees. When you reach the path you are shaken and slow and hollowed out — and the night is burning away behind you. But you are alive, and still, just, able to help."),
  [t("The long path after all.", "The long path after all.", "The long path after all."),
   t("Too spent to go on.", "Too spent to go on.", "Too spent to go on.")])

P(54,
  t("You try to bank the door against the water. You drag a chest, pile up sacks, do what you can. It holds the worst of the sea back, a little. But you have no lamp to leave them. And a dark, wet room is a hard place to wait. You have to choose.",
    "You try to bank the door against the water — a dragged chest, piled sacks, whatever you can manage. It holds the worst of the sea back a little. But there's no lamp to leave them, and a dark, flooding room is a hard place to wait. You have to choose.",
    "You try to bank the door against the water: a dragged chest, a pile of sacks, whatever your cold hands can manage from what's there. It holds the worst of the sea back, a little. But there is no lamp to leave them, and a dark, flooding room is a hard place to wait out a night like this. So the choice comes round again, as it keeps doing."),
  [t("Give them your lamp and coat.", "Give them your own lamp and coat.", "Give them your own lamp and coat."),
   t("Promise to send help.", "Promise to send help.", "Promise to send help.")])

P(55,
  t("You hand over your own coat and lamp. The family huddle round the small flame. Relief moves across their faces. The child stops crying at last. \"Thank you,\" the mother says, again and again. You have less now. But you did the right thing.",
    "You hand over your own coat and lamp, and the family huddle round the small flame, relief spreading across their faces. The child stops crying at last. \"Thank you,\" the mother says, over and over. You've less to keep you now — but you did right.",
    "You hand over your own coat and lamp without letting yourself think too hard about it, and the family huddle round the small flame, relief moving visibly across their faces. The child stops crying at last. \"Thank you,\" the mother keeps saying, over and over, as if the words might run out. You have a good deal less to keep the cold off you now — but you know, cleanly, that you did the right thing."),
  [t("On, colder now.", "On, colder now.", "On, colder now."),
   t("They point you to the water.", "They point you to the light on the water.", "They point you to the light on the water.")])

P(56,
  t("Without your coat, the cold and wet find you fast. Your teeth chatter. Your fingers go stiff. You gave it to help, and you would do it again. But the storm does not care about that. It just batters on. You have to keep your head, and keep moving.",
    "Without your coat, the cold and wet find you fast — teeth chattering, fingers going stiff. You gave it to help, and you'd do it again; but the storm doesn't care about that. It just batters on. You have to keep your head, and keep moving.",
    "Without your coat, the cold and the wet find you fast now: your teeth chattering, your fingers going stiff and stupid. You gave it away to help someone, and you would do it again in a heartbeat — but the storm does not care in the least about that, and only goes on battering the coast. So you keep your head, because it's all you have left to keep, and you keep moving."),
  [t("Keep moving.", "Keep moving, keep your head.", "Keep moving, keep your head."),
   t("A minute out of the rain.", "A lit doorway offers a minute.", "A lit doorway offers a minute.")])

P(57,
  t("A stranger waves you into a doorway. \"Just a minute,\" they say. \"Out of the rain. Catch your breath.\" It is warm and dry in there. Your body begs you to stay. But a minute can turn into an hour. And the light is still dark.",
    "A stranger waves you into a doorway. \"Just a minute,\" they say. \"Out of the rain — catch your breath.\" It's warm and dry, and your body begs you to stay. But a minute can slide into an hour — and the light is still dark.",
    "A stranger waves you in under a low doorway, out of the worst of the rain. \"Just a minute,\" they say kindly. \"Get out of it. Catch your breath.\" Out of the wind it is warm and dry and dangerously welcoming, and every muscle in your body begs you to stay exactly where you are. But you know how a minute slides into an hour on a night like this — and the light up the tower is still dark."),
  [t("Rest, then on.", "Warm up, then on.", "Warm up, then on."),
   t("Refuse, press on.", "Refuse, press on.", "Refuse, press on.")])

P(58,
  t("You press on into the storm, soaked to the bone. The wind fights every step. The rain blinds you. Each step is a small battle. But you keep them coming, one after the next. Slow is fine. Stopping is not.",
    "You press on into the storm, soaked to the bone, the wind fighting every step, the rain blinding you. Each step is a small battle — but you keep them coming, one after another. Slow is fine tonight. Stopping is what kills.",
    "You press on into the storm, soaked to the bone, the wind fighting you for every single step and the rain driving so hard you can barely see the path. Every step is its own small battle against the wish to stop. But you keep them coming, one after another after another, because slow is survivable tonight — and stopping, you understand perfectly well, is what kills you and the light both."),
  [t("The last of the watch.", "The last of the watch.", "The last of the watch."),
   t("On toward the cove.", "On toward the cove.", "On toward the cove.")])

P(64,
  t("You look out over the coast. It is all dark, and it is roaring. Great waves break white on the rocks. Nothing shows a light but the far, struggling boat. The whole shore seems to hold its breath. Everything waits for the storm to break. So do you.",
    "You look out over the coast — all dark, all roaring. Great waves break white on the rocks, and no light shows but the far, struggling boat. The whole shore seems to hold its breath, waiting for the storm to break. And so, you realise, are you.",
    "You look out over the coast, and it is all dark, and all roaring, great waves breaking white on the rocks below and the wind tearing the tops off them. Nothing shows a light anywhere but the far, struggling boat past the point. The whole shore seems to be holding its breath, waiting — waiting only for the storm to break and let it live again. And so, you realise, standing there, are you."),
  [t("Press on along the head.", "Press on along the head.", "Press on along the head."),
   t("The light on the water.", "The light on the water.", "The light on the water.")])

P(65,
  t("The wind climbs to its worst. It nearly takes you off your feet. You have to crouch and hold on. The air is full of spray and torn spume. It is hard to see. Hard to breathe. This is the hour to get through. Hold on, and the boat has a chance.",
    "The wind climbs to its worst and nearly takes you off your feet. You crouch and hold on, the air full of spray and torn spume. It's hard to see, hard to breathe. This is the hour to survive — get through it, and that boat still has a chance.",
    "The wind climbs to its absolute worst, and this, you understand, is the hour of it. A gust nearly takes you off your feet, and you crouch and cling to the rock, the air full of stinging spray and torn spume. It is hard to see, hard even to breathe. This is the hour that simply has to be got through — and if you can get through it, that boat out there still has a chance."),
  [t("The flooding cottage.", "The flooding cottage.", "The flooding cottage."),
   t("Press on.", "Press on.", "Press on.")])


# ============================ THE WRECKER (the trap) ======================

P(40,
  t("The wrecker smiles at you. It is a wide, easy smile. \"Cold work, this,\" he says. \"I've oil to sell. A strong back to lend. The light's not really your job tonight, friend.\" His lantern swings. His eyes are cold. You have seen this before.",
    "The wrecker turns his wide, easy smile on you. \"Cold work, this,\" he says. \"I've oil to sell, a strong back to lend — and the light's not really your job tonight, friend.\" His lantern swings. His smile never reaches his eyes. You've seen this kind before.",
    "The wrecker turns a wide, easy smile on you as you come up. \"Cold work, this,\" he says smoothly, over the wind. \"I've oil to sell you, and a strong back to lend — and the light's not really your job tonight, friend.\" His lantern swings in his fist. And his smile, you notice, never once reaches his eyes. You have seen this exact kind of help before, and you know what it costs."),
  [t("Hear the price.", "Hear the price.", "Hear the price."),
   t("Refuse and go round.", "Refuse and go round.", "Refuse and go round.")])

P(41,
  t("The offer is a hook, and you feel it. He leans in close. \"That boat's lost already,\" he says, low. \"Let the dark do its work. There's a share in it for you.\" It is a cruel thing to say. And it is meant to work. That line is the whole trick.",
    "The offer is a hook, and you feel it set. He leans in close. \"That boat's lost already,\" he says, low. \"Let the dark do its work — and there's a share in it for you.\" It's a cruel thing to say. And it's meant to work. That line is the whole trick.",
    "The offer is a hook, and you feel it set the moment he leans in, close and low over the wind. \"That boat's lost already, friend,\" he murmurs. \"Let the dark do its work tonight, and there's a fair share in it for you by morning.\" It is a deliberately cruel thing to say. And it is meant, precisely, to work — because that line, you realise, is the whole of the trick."),
  [t("Take his deal.", "Take his deal.", "Take his deal."),
   t("That's the tell — refuse.", "That line is the tell — refuse.", "That line is the tell — refuse."),
   t("Ask what he really wants.", "Ask what he really wants.", "Ask what he really wants."),
   t("The frightened folk press in.", "The frightened folk press in.", "The frightened folk press in.")])

P(42,
  t("You turn your back on him. You leave him to the surf and his cold trade. It feels good to walk away. He calls after you, but you do not turn round. His kind always finds someone. But not you. Not tonight.",
    "You turn your back on him and leave him to the surf and his cold trade. It feels good to walk away. He calls after you, but you don't turn round. His kind always finds someone — but not you, and not tonight.",
    "You turn your back on him and leave him to the surf and his cold trade. It feels surprisingly good to walk away. He calls something after you, oily and knowing, but you don't give him the satisfaction of turning round. His kind always finds someone, on a coast like this — but it won't be you, and it won't be tonight."),
  [t("On the way.", "On the way.", "On the way."),
   t("To the oil store instead.", "To the oil store instead.", "To the oil store instead.")])

P(43,
  t("You take his oil, his coin. Your hands close on it. And something in you already knows. His smile widens. \"Wise,\" he says. But it does not feel wise. It feels like a door shutting somewhere in the dark.",
    "You take his oil, his coin; your hands close on them, and something in you already knows. His smile widens. \"Wise,\" he says. But it doesn't feel wise. It feels like a door shutting somewhere out in the dark.",
    "You take his oil, and his coin, and your hands close on them — and something low in your stomach already knows. His smile widens in the lantern-light. \"Wise,\" he says. But it doesn't feel wise at all. It feels, standing there in the surf, like a door shutting quietly somewhere out in the dark."),
  [t("Carry it up.", "Carry it up.", "Carry it up."),
   t("A doubt already.", "A doubt already.", "A doubt already.")])

P(44,
  t("You ask him straight. What does he really want? Why should the light stay dark? He smiles, and looks out to sea. \"Ships come in on the rocks,\" he says. \"The sea's generous, after.\" He will not say more. And that, right there, is your answer.",
    "You ask him straight: what does he really want? Why should the light stay dark? He smiles and looks out to sea. \"Ships come in on the rocks,\" he says. \"The sea's generous, after.\" He won't say more — and that, right there, is your answer.",
    "You ask him straight out: what does he really want, and why should the light stay dark? He smiles and lets his eyes slide out to the black sea. \"Ships come in on the rocks, on a night like this,\" he says. \"And the sea's generous, after.\" He won't say a word more — and that, right there, is your whole answer. A man who wants the dark wants it for the wreck."),
  [t("That's my answer — refuse.", "That's your answer — refuse.", "That's your answer — refuse."),
   t("Take it anyway.", "Take it anyway.", "Take it anyway.")])

P(45,
  t("You carry his oil up to the lamp. But when you pour it, the flame chokes and spits. The oil is fouled with seawater. It will not feed the wick. The beam gutters low and brown. He gave you ruin, not help.",
    "You carry his oil up to the lamp. But when you pour it, the flame chokes and spits — the oil's fouled with seawater, and it won't feed the wick. The beam gutters low and brown. He gave you ruin, not help.",
    "You carry his oil all the way up to the lamp. But the moment you pour it in, the flame chokes and spits and shrinks — the oil is fouled through with seawater, and it will not feed the wick at all. The beam gutters low and brown over the rocks. He gave you ruin dressed up as help, and you took it."),
  [t("Try to work it.", "Try to work it.", "Try to work it."),
   t("Up to Nan with nothing.", "Up to Nan with nothing.", "Up to Nan with nothing.")])

P(46,
  t("You open the can and the smell hits you. Salt. Thin. Cut with water. This oil will never feed a flame. You paid for it, and it is worthless. The doubt in your gut was right all along.",
    "You open the can and the smell hits you — salt, thin, cut with water. This oil will never feed a flame; you paid for it, and it's worthless. The doubt in your gut was right about him all along.",
    "You open the can and the smell hits you at once: salt, thin, plainly cut with seawater. This oil will never feed a flame in a hundred years, whatever he promised. You paid for it, and it is worthless — and the small cold doubt in your gut, it turns out, was right about him from the start."),
  [t("Up to the lamp.", "Up to the lamp.", "Up to the lamp."),
   t("Back to have it out with him.", "Back to have it out with him.", "Back to have it out with him.")])

P(47,
  t("You look for him. The wrecker's lantern is already gone, down toward the cove. He was never helping you. He was waiting for the dark, and the wreck, and the sea's cold gift. You stand there, fooled, with his worthless oil in your hands.",
    "You look for him, but the wrecker's lantern is already gone, down toward the cove. He was never helping you — he was waiting for the dark, the wreck, the sea's cold gift. You stand there, fooled, his worthless oil in your hands.",
    "You turn to look for him, and the wrecker's lantern is already gone, swinging away down toward the cove. He was never helping you, of course — he was only ever waiting for the dark, and the wreck, and the sea's cold gift after. You stand there in the surf, plainly and completely fooled, holding his worthless, salt-cut oil."),
  [t("Up to the lamp, fooled.", "Up to the lamp, fooled.", "Up to the lamp, fooled."),
   t("Fling the can into the surf.", "Fling the fouled can into the surf.", "Fling the fouled can into the surf.")])

P(48,
  t("The wrecker is gone. The cove is empty. There is only the storm now, and the dark, and what you gave him for nothing. You learned a hard lesson, and paid too much for it. Now you must go on with what little is left.",
    "The wrecker's gone, the cove empty — only the storm now, the dark, and what you handed him for nothing. You learned a hard lesson and paid far too much for it. Now you go on with what little is left.",
    "The wrecker is gone, and the cove with him, empty — leaving only the storm, and the dark, and what you handed over to him for nothing at all. You have learned a hard lesson tonight, and paid far too much for the privilege. Now you go on with whatever little is left to you, which, when you take honest stock, is not much."),
  [t("Up to the lamp.", "Up to the lamp.", "Up to the lamp."),
   t("Stand in the dark.", "Stand a moment in the dark.", "Stand a moment in the dark.")])

P(49,
  t("The frightened folk press their coins on him. Hands reach out, full of money. Voices beg him for oil, for a way out. And he takes it, slow, with that smile. He picks who to help by who can pay. Now you see the whole trick, plain and ugly.",
    "The frightened folk press their coins on him — hands full of money, voices begging for oil, for a way out. And he takes it, slow, with that smile, choosing who to help by who can pay. Now you see the whole trick, plain and ugly.",
    "The frightened folk press in and shove their coins at him — hands full of money, voices begging him for oil, for a boat, for any way out of the dark. And he takes it, unhurried, with that same smile, choosing who to help by who can pay him most. Now you see the whole trick laid out plain in front of you, and it is an ugly, ugly thing to watch."),
  [t("Hear the price anyway.", "Hear the price anyway.", "Hear the price anyway."),
   t("Refuse and go round.", "Refuse and go round.", "Refuse and go round.")])


# ============================ THE LIGHT ON THE WATER (mystery) ============

P(70,
  t("Far out past the point, a second light lifts and falls. It is out where no boat should be tonight. It shows, and hides, and shows again in the swell. No one can explain it. Something is out there. Or someone.",
    "Far out past the point, a second light lifts and falls. It's out where no boat should be tonight, showing and hiding and showing again in the swell. No one can explain it. Something is out there, or someone.",
    "Far out past the point, a second light lifts and falls, out where no harbour boat should be on a night like this. It shows, then hides in the swell, then shows again, low and stubborn. No one on the coast can explain it, and no one wants to try. But something is out there, or someone — and you find you can't quite look away from it."),
  [t("Go and answer it.", "Go and answer it.", "Go and answer it."),
   t("Leave it — the light first.", "Leave it — the light first.", "Leave it — the light first.")])

P(71,
  t("You get down to the cove. You call out into the dark. No answer comes but the sea. Then you see it. A boat's shape, low on the rocks, half swallowed by the waves. Someone rigged that light. Someone is out there.",
    "You get down to the cove and call out into the dark. No answer comes but the sea — then you see it: a boat's shape, low on the rocks, half swallowed by the waves. Someone rigged that light. Someone's out there.",
    "You get down to the cove and call out into the dark, once, twice. No answer comes back but the sea working the rocks. And then you see it, low against the white water: a boat's shape, half swallowed by the waves, hard on the rocks. Someone rigged that light to be seen. Someone, against all sense, is out there."),
  [t("Wade out to it.", "Wade out to it.", "Wade out to it."),
   t("Call again and wait.", "Call again and wait.", "Call again and wait."),
   t("The boat's stove in.", "The boat's stove in, half under.", "The boat's stove in, half under.")])

P(72,
  t("You wade out onto the rocks. And there, in the swamped boat, is an old fisher — Ash. They are tangled in the lines, barely holding on. The sea drags at them with every wave. There is no time to lose.",
    "You wade out onto the rocks. There in the swamped boat is an old fisher — Ash — tangled in the lines and barely holding on. The sea drags at them with every wave. There's no time to lose.",
    "You wade out onto the rocks, the swell surging round your legs. There in the swamped boat is an old fisher — Ash — tangled fast in the lines and barely holding on, the sea hauling at them with every wave that comes through. They've been out here a long time, alone. There is no time at all to lose."),
  [t("Get them off and warm.", "Get them off and warm.", "Get them off and warm."),
   t("Run for help.", "Run for help.", "Run for help.")])

P(73,
  t("You call out again into the dark. For a moment, nothing. Then a voice comes back, weak and torn by the wind. \"Here,\" it cries. \"Out here.\" Someone is on the rocks, and they need help. You cannot walk away from that now.",
    "You call out again into the dark, and for a moment there's nothing. Then a voice comes back, weak and torn by the wind: \"Here! Out here!\" Someone's on the rocks, and they need help. You can't walk away from that now.",
    "You call out again into the dark, once, twice, and for a long moment there is nothing but the sea. Then a voice comes back to you, weak and torn ragged by the wind: \"Here! Out here!\" Someone is on the rocks, then, and they need help; and you find, standing there in the surf, that you couldn't walk away from that now if you tried."),
  [t("Wade out.", "Wade out.", "Wade out."),
   t("Fetch help.", "Fetch help.", "Fetch help.")])

P(74,
  t("You drag Ash clear of the lines. You get them up the rocks and wrap them in your coat. Slowly, they come round. They grip your arm. \"The light,\" they gasp. \"Keep the light. There may be others out there.\"",
    "You drag Ash clear of the lines, get them up the rocks and wrap them in your coat. Slowly they come round, gripping your arm. \"The light,\" they gasp. \"Keep the light. There may be others out there.\"",
    "You drag Ash clear of the lines, haul them up off the rocks and wrap them in your coat, and little by little, against the odds, they come round. Their hand finds your arm and grips it hard. \"The light,\" they gasp out, over the wind. \"Keep the light burning. There may be others out there tonight — you can't let it go dark.\""),
  [t("Ash speaks of Nan.", "Ash speaks of Nan.", "Ash speaks of Nan."),
   t("Get you both back.", "Get you both back to the tower.", "Get you both back to the tower.")])

P(75,
  t("You turn to run for help. Then you stop. There is no help. Not out here. Not till dawn. No lifeboat, no crew, no one coming. It is you, or it is no one. Ash knows it too. Their eyes follow you across the rocks.",
    "You turn to run for help — then stop. There is no help out here; not till dawn. No lifeboat, no crew, no one coming. It's you or no one, and Ash knows it too. Their eyes follow you across the rocks.",
    "You turn to run for help — and then you stop, because you already know the truth of it. There is no help out here. Not till dawn, not for hours yet. No lifeboat, no crew, no one at all coming down to this cove in a sea like this. It is you, or it is no one. And Ash knows it as well as you do; their eyes follow you, quietly, across the wet rocks."),
  [t("Go back for them.", "Go back for them.", "Go back for them."),
   t("Up to the lamp, torn.", "Up to the lamp, torn.", "Up to the lamp, torn.")])

P(76,
  t("Ash looks up at you. Their eyes are clearer now. \"The keeper, up in the tower,\" they say. \"Nan? That's my mother. We haven't spoken in years. Not since — well. It's a long tale, and a cold night for it.\"",
    "Ash looks up at you, their eyes clearer now. \"The keeper, up in the tower — Nan?\" they say. \"That's my mother. We haven't spoken in years. Not since — well. It's a long tale, and a cold night for it.\"",
    "Ash looks up at you, their eyes clearer now than they were, and something like grief crossing their face. \"The keeper up in the tower,\" they say slowly. \"Nan? That's my mother. We haven't spoken in years — not since, well. It's a long tale, and this is a cold night for the telling of it.\""),
  [t("Bring them together.", "Resolve to bring them together.", "Resolve to bring them together."),
   t("Up with the news.", "Up with the news.", "Up with the news.")])

P(77,
  t("You decide to get them face to face tonight. Ash and old Nan, after all these years. It is a small thing, next to the light and the storm. But it is not nothing. Some doors stay shut for years because no one dares to knock. You will knock.",
    "You decide to get them face to face before the night's out — Ash and old Nan, after all these years. It's a small thing, next to the light and the storm. But it isn't nothing; some doors stay shut for years only because no one dares to knock. You will.",
    "You decide, there and then, to get the two of them face to face before the night is out — Ash and old Nan Bright, after all these years apart. It's a small thing, you know, set beside the light and the storm and a boat on the rocks. But it is not nothing, either; some doors stay shut for years for no better reason than that no one ever dares to knock. You mean to knock."),
  [t("Back to the tower.", "Back to the tower.", "Back to the tower."),
   t("Get Ash steady first.", "Get Ash steady first.", "Get Ash steady first.")])

P(78,
  t("The boat is stove in, half under the water. The sea works at it with every wave. It will not last long. And yet someone got a light going on it. Someone climbed out onto these rocks in the dark. Someone is here.",
    "The boat's stove in, half under, the sea working at it with every wave — it won't last long. And yet someone got a light going on it, someone climbed out onto these rocks in the dark. Someone is here.",
    "The boat is stove in, half under the black water, the sea working at the broken hull with every wave that comes through; it will not last much longer. And yet — and this is what keeps you moving forward over the rocks — someone got a light going on it, and recently. Someone climbed out onto these rocks in the dark. Someone is still here."),
  [t("Wade closer.", "Wade closer.", "Wade closer."),
   t("A name on the bow.", "A name painted on the bow.", "A name painted on the bow.")])

P(79,
  t("You wade closer, and see the name on the bow. You know it. It is Nan's own boat — the one lost years ago, or so they always said. Then, from under the broken hull, a weak sound. A cough. Someone is alive in there.",
    "You wade closer and see the name on the bow, and you know it. It's Nan's own boat — the one lost years ago, or so they always said. Then, from under the broken hull, a weak sound: a cough. Someone's alive in there.",
    "You wade closer, and the swell lifts for a moment and shows you the name painted on the bow — and you know it at once. It's Nan's own boat, the one lost years ago, or so the coast always said. And then, from under the broken hull, comes a weak, unmistakable sound: a cough, and after it, breathing. Someone is alive in there."),
  [t("Follow the sound.", "Follow the sound, and find them.", "Follow the sound, and find them."),
   t("The years in it.", "The years in it.", "The years in it.")])

P(69,
  t("Years of a shut door press in on you. All the words no one said. All the silence between them. It feels like a place where nothing is left alive. Then you hear it. Breathing. Weak, and close, from under the hull. Someone is alive in there.",
    "Years of a shut door press in. All the words no one said, all the silence between them — a place where nothing seems left alive. Then you hear it: breathing, weak and close, from under the hull. Someone's alive in there after all.",
    "Years of a shut door seem to press in around you on the rocks. All the words no one ever said, all the long silence between a mother and a child — everything about it saying that nothing is left alive out here. And then you hear it, and your whole body goes still — breathing, weak and close, from under the broken hull. Someone is alive in there, after all. Someone is barely hanging on."),
  [t("Follow the breathing.", "Follow the breathing, and find them.", "Follow the breathing, and find them."),
   t("Too much — back to the light.", "It's too much — back to the light.", "It's too much — back to the light.")])


# ============================ ACT III — TOWARD FIRST LIGHT ================

P(90,
  t("You are back at the tower, soaked to the bone. The last of the worst storm batters the glass. Below, Nan lies grey at the foot of the stairs. Above, the lamp burns low. This is the hour that counts. Whatever you do now, do it well. That boat is close to the rocks.",
    "You're back at the tower, soaked through, the last of the worst storm battering the glass. Below, Nan lies grey at the foot of the stairs; above, the lamp burns low. This is the hour that counts; whatever you do now, do it well. That boat is close to the rocks.",
    "You're back at the tower at last, soaked to the bone, the last of the worst storm still battering the glass overhead. Below you, Nan lies grey and still at the foot of the stairs; above you, the great lamp burns low and hungry. This is the hour that counts, above all the others; whatever you do now, you had better do it well, because that boat has come down close to the rocks, and you can feel it."),
  [t("See to the light.", "See to the light.", "See to the light."),
   t("The wrecker's last offer.", "The wrecker's last offer.", "The wrecker's last offer."),
   t("Help arrives behind you.", "Help arrives behind you.", "Help arrives behind you.")])

P(80,
  t("The wrecker comes up one last time. His lantern swings in the dark. \"Still fighting it?\" he says. \"Let it go dark. Last chance to be on the winning side, friend.\" The same smile. The same lie. He knows you are spent. Now you choose, for good.",
    "The wrecker comes up one last time, his lantern swinging. \"Still fighting it?\" he says. \"Let it go dark. Last chance to be on the winning side, friend.\" The same smile, the same lie. He knows you're spent, and he's counting on it. Now you choose, for good.",
    "The wrecker climbs up to you one last time, his lantern swinging in the dark. \"Still fighting it?\" he says, easy as ever. \"Let it go dark. Last chance to be on the winning side, friend.\" The same smile, the same lie underneath it. He knows exactly how spent you are by now, and he is counting on it to do his work for him. So now you choose, and this time for good."),
  [t("Take his deal.", "Take his deal.", "Take his deal."),
   t("Refuse for good.", "Refuse for good.", "Refuse for good.")])

P(91,
  t("You reach the lamp. The flame is low. The great lens sits still. Out past the glass, the boat's lights are close to the rocks now, far too close. You have to get the beam full and turning, and get it now. Everything you did tonight comes down to this.",
    "You reach the lamp: the flame low, the great lens still. Out past the glass, the boat's lights are close to the rocks now — far too close. You have to get the beam full and turning, and now. Everything you did tonight comes down to this.",
    "You reach the lamp, and your stomach drops. The flame is low, the great lens sitting dead still, and out past the streaming glass the boat's lights have come in close to the rocks now — far too close. You have to get the beam full and turning, and you have to do it now, this minute. Everything you did or failed to do across the whole long night comes down, in the end, to this."),
  [t("Get the beam turning.", "Get the beam full and turning.", "Get the beam full and turning."),
   t("Check on Nan below.", "Check on Nan below.", "Check on Nan below."),
   t("A light flares far out.", "A light flares far out to sea.", "A light flares far out to sea.")])

P(92,
  t("Then help reaches the tower behind you. Hands, and oil, and steady heads. People who know the light. You are not alone with this now. Others are here to share the weight. It is like setting down a heavy load. You breathe out at last.",
    "Then help reaches the tower behind you — hands, oil, steady heads, people who know the light. You aren't alone with this now; others are here to share the weight. It's like setting down a heavy load, and you breathe out at last.",
    "And then, behind you on the stairs, help reaches the tower at last: hands, and oil, and steady heads, people who know this light and how to keep it. You are not alone with it any more. Others are here now to take up their share of the weight — and it is like setting down a load you'd forgotten you were carrying. You breathe out, properly, for the first time in hours."),
  [t("To the lamp together.", "To the lamp together.", "To the lamp together."),
   t("Hold the watch.", "Hold the watch.", "Hold the watch."),
   t("A lamp on the water, far off.", "A lamp on the water, far off.", "A lamp on the water, far off.")])

P(93,
  t("Now you keep the beam. What you can do depends on what you carried. If you have proper oil, you have plenty to work with. If not, you must coax every last flicker of the flame. Either way, you begin.",
    "Now you keep the beam — and what you can do depends on what you carried. With proper oil, you've plenty to work with; without it, you must coax every last flicker of the flame. Either way, you begin.",
    "Now, at last, you keep the beam — and exactly what you can do depends entirely on what you had the sense to carry up here. If you brought proper oil, you have plenty to work with, and a real chance. If you didn't, you'll have to coax every last flicker out of a starving flame. Either way, there's no more time to weigh it; you begin."),
  [t("The oil and wick.", "The oil and wick.", "The oil and wick."),
   t("Coax the guttering flame.", "Coax the guttering flame.", "Coax the guttering flame.")])

P(94,
  t("You go down to check on Nan. Her eyes open, just a little. There is fear in them, and then, seeing you, less fear. \"You kept it going,\" she says, so quiet. \"That I did,\" you tell her. \"Now rest. I've got the light.\"",
    "You go down to check on Nan, and her eyes open just a little — fear in them, then, seeing you, a little less fear. \"You kept it going,\" she whispers. \"That I did,\" you tell her. \"Now rest. I've got the light.\"",
    "You go down to check on Nan, gentle and careful, and her eyes flicker open just a little. There's fear in them at first, and then, focusing on your face, a little less of it. \"You kept it going,\" she whispers, barely a sound at all. \"That I did,\" you tell her, keeping your voice steady and light. \"Now rest. I've got the light. You just rest.\""),
  [t("Get the light full.", "Get the light full.", "Get the light full."),
   t("Break out the oil.", "Break out the oil.", "Break out the oil.")])

P(95,
  t("The oil does it. You trim the wick true. You wind the great lens round like a clock. And the beam swings out full and gold, far across the black water. A light in all that dark. This is what the tower is for. You knew that. Now you see it.",
    "The oil does it. You trim the wick true, wind the great lens round like a clock, and the beam swings out full and gold across the black water. A light in all that dark. This is what the tower is for; you knew that, and now you see it.",
    "The oil does it, and it makes all the difference in the world. You trim the wick true, wind the great lens round like a clock, and the beam swings out full and gold, reaching far across the black water toward the rocks. A single light in all that roaring dark. This is what the tower is for, what it has always been for — you knew that in the abstract, and now, standing at the lamp, you see it happen."),
  [t("Hold the watch.", "Hold the watch.", "Hold the watch."),
   t("Help arrives.", "Help arrives.", "Help arrives.")])

P(96,
  t("You have no proper oil to pour. So you coax what flame there is. You shield it from the draught with your own body. You feed it scraps, and breath, and will. It burns low, and thin. It may be enough. It may not. But you will not let it go out.",
    "You've no proper oil to pour, so you coax what flame there is. You shield it from the draught with your own body, feeding it scraps, breath, will. It burns low and thin. It may be enough. It may not. But you won't let it go out.",
    "You've no proper oil to pour, so you make do with what little flame there is and refuse to think about the difference. You shield it from the draught with your own body; you feed it scraps, and breath, and sheer will. It burns low, and thin, and desperate. It may be enough. It may, honestly, not. But you will not, whatever happens, let it go out."),
  [t("Hold the watch.", "Hold the watch.", "Hold the watch."),
   t("It may not be enough.", "It may not be enough.", "It may not be enough.")])

P(97,
  t("The flame is low, and failing. And you are afraid that shielding it will not be enough. You have done all you can with what you have. But it may not hold. You need more. You need oil, or hands, or both, and soon.",
    "The flame is low and failing, and you're afraid shielding it won't be enough. You've done all you can with what you have — but it may not hold. You need more: oil, or hands, or both, and soon.",
    "The flame is low, and failing, and you are honestly afraid that shielding it with your body won't be enough to hold it through what's left of the night. You have done everything you can with what little you have, and you know it — but everything you can may still not be enough. You need more than this. You need oil, or hands, or both, and you need it soon."),
  [t("Hold on to first light.", "Hold on to first light.", "Hold on to first light."),
   t("Send for the help.", "Send for the rallied help.", "Send for the rallied help.")])

P(98,
  t("You glance out, and see it. Far out to sea, a light flares and falls. It is out where no boat should be. It shows, and hides, and shows again. It pulls at your eye. It pulls at something in you. Someone is out there.",
    "You glance out and see it. Far out to sea, a light flares and falls, out where no boat should be, showing and hiding and showing again. It pulls at your eye, and at something in you. Someone's out there.",
    "You glance out through the streaming glass, and there it is. Far out to sea, a light flares and falls, out where no boat should be on a night like this, showing and hiding and showing again in the swell. It pulls at your eye, that light, and at something deeper in you that has never learned to leave a wrong thing alone. Someone is out there."),
  [t("See to the light first.", "See to the light first.", "See to the light first."),
   t("The light nags at you.", "The light nags at you.", "The light nags at you.")])

P(99,
  t("The light on the water shows again. Out where everyone swears no boat would be. But a light means a hand to light it. A hand means a person. And a person, out there, on a night like this, is in real trouble. You can feel it.",
    "The light on the water shows again — out where everyone swears no boat would be. But a light means a hand to light it, and a hand means a person, and a person out there tonight is in real trouble. You can feel it.",
    "The light on the water shows again, out where everyone on the coast swears no boat would ever be tonight. But a light means a hand to light it, and a hand means a person, and a person out there, on a night as wild as this one, is in real and mortal trouble. You can feel the truth of it, pulling at you like a hook set deep."),
  [t("The lamp first.", "The lamp first.", "The lamp first."),
   t("Hold the watch.", "Hold the watch.", "Hold the watch.")])

P(100,
  t("Now comes the long hold. You keep the beam turning. You keep Nan warm and breathing. You watch the black water, hour by hour. It is not exciting. It is just steady, hard, careful work. But steady work is what saves people. So you do it, and you do not stop.",
    "Now comes the long hold: you keep the beam turning, keep Nan warm and breathing, watch the black water hour by hour. It isn't exciting — just steady, hard, careful work. But steady work is what saves people, so you do it, and you don't stop.",
    "Now comes the long hold, the hardest and least dramatic part of all. You keep the beam turning, you keep Nan warm and breathing at the foot of the stairs, and you watch the black water, hour by grinding hour. It is not exciting, none of it; it is just steady, patient, careful work. But steady, patient work, you have learned tonight, is exactly what saves people out here. So you do it, and you don't stop doing it."),
  [t("Watch for first light.", "Watch for first light.", "Watch for first light."),
   t("The light on the water nags.", "The light on the water still nags.", "The light on the water still nags."),
   t("The night's worst hour.", "The night's worst hour.", "The night's worst hour.")])

P(101,
  t("And then, at last, it turns. The wind drops a note. The rain eases. The sky greys at the edge of the sea. And a lamp swings round the point — the lifeboat, come out at last. You held the light to first light. You did it.",
    "And then, at last, it turns. The wind drops a note, the rain eases, the sky greys at the edge of the sea. And a lamp swings round the point — the lifeboat, out at last. You held the light to first light. You did it.",
    "And then, at long last, it turns. The wind drops a note; the rain eases from a roar to a hiss; the sky greys, just faintly, at the far edge of the sea. And a lamp swings round the point at last — the lifeboat, out and searching. You held the light all the way to first light. Somehow, against everything the night threw, you did it."),
  [t("What it finds.", "First light, and what it finds.", "First light, and what it finds."),
   t("Dawn over the sea.", "Dawn over the wild sea.", "Dawn over the wild sea.")])

P(102,
  t("This is the worst hour, the one just before the break. The storm has not eased yet. Your arms ache from the lens. Your eyes burn. But you can feel the night starting to turn. Hold on. Hold on a little longer. The end of it is close now.",
    "This is the worst hour, the one just before the break. The storm's not eased yet; your arms ache from the lens; your eyes burn. But you can feel the night beginning to turn. Hold on. Hold on a little longer. The end is close now.",
    "This is the worst hour of all, the one that comes just before the break. The storm has not eased in the least; your arms ache from winding the lens; your eyes burn with salt and tiredness. But you can feel it now, under everything — the night beginning, at last, to turn. So you hold on. You hold on a little longer. The end of it is genuinely close now, and you know it."),
  [t("Watch for first light.", "Watch for first light.", "Watch for first light."),
   t("Other lamps along the head.", "Other lamps along the head.", "Other lamps along the head.")])

P(103,
  t("Along the head, you see them. Lamps, and dark figures moving. Signal fires burning low against the rain. Other people, out in it too. The coast got through this night as well. You were not the only one keeping watch. That warms you, somehow.",
    "Along the head you see them — lamps, dark figures moving, signal fires burning low against the rain. Other people, out in it too. The coast got through this night as well, and you weren't the only one keeping watch. That warms you, somehow.",
    "Along the head, you see them at last: lamps, and dark figures moving, and signal fires burning low and stubborn against the rain. Other people, out in it too, all night. The coast got through this night as well, then — you were never the only one out here, keeping watch, holding the same small line against the dark. And that thought, somehow, warms you more than you'd expect."),
  [t("First light.", "First light.", "First light."),
   t("The lifeboat coming round.", "The lifeboat's lamp coming round.", "The lifeboat's lamp coming round.")])

P(104,
  t("At last, the lifeboat. Its lamp and a plume of spray come round the point, hard into the sea. Real help, coming at real speed. You grip the rail and watch it, and your legs shake under you. It is nearly over now. Nearly. You can let yourself believe it.",
    "At last, the lifeboat — its lamp and a plume of spray coming round the point, hard into the sea. Real help, at real speed. You grip the rail and watch, your legs shaking under you. It's nearly over now. Nearly. You let yourself believe it.",
    "At last, the lifeboat — its lamp and a great plume of spray come round the point, driving hard into the sea toward the rocks. Real help, coming at real speed, coming for that boat and for all of you. You grip the rail and watch it come, your legs shaking under you with more than cold. It is nearly over now. Nearly. And for the first time all night, you let yourself actually believe it."),
  [t("First light.", "First light.", "First light."),
   t("What it came to.", "What the night came to.", "What the night came to.")])

P(105,
  t("Dawn comes up over the wild sea. The light turns grey, and then pale, and clean. The storm blows itself out, wave by wave. The great swells still run, but the worst has passed. The coast, so cruel all night, is almost gentle now. You stand and watch it, and you breathe.",
    "Dawn comes up over the wild sea, the light turning grey, then pale and clean, the storm blowing itself out wave by wave. The great swells still run, but the worst has passed. The coast, so cruel all night, is almost gentle now. You stand and watch, and breathe.",
    "Dawn comes up over the wild sea at last, and the light turns grey, and then pale, and clean, and the storm blows itself out wave by wave by wave. The great swells still run in and break white on the rocks, but the worst of it has passed and gone. The coast that was so purely cruel all night is almost gentle now, almost kind. You just stand there at the rail and watch it happen, and you breathe, and breathe."),
  [t("First light.", "First light.", "First light."),
   t("Help reaches the tower.", "Help reaches the tower.", "Help reaches the tower."),
   t("The first gull over the water.", "The first gull over the water.", "The first gull over the water.")])

P(106,
  t("Then it comes. The first gull, out over the grey water. It rides the wind, easy, as if there had been no storm at all. After the night you have had, it seems absurd, and beautiful. You watch it go. You made it. You all made it.",
    "Then it comes — the first gull, out over the grey water, riding the wind easy, as if there'd been no storm at all. After the night you've had, it seems absurd, and beautiful. You watch it go. You made it. You all made it.",
    "Then it comes, the thing you'd half stopped believing in: the first gull, out over the grey water, riding the easing wind as though there had been no storm at all, ever. After the night you've all had, it seems absurd, and quietly beautiful. You watch it go. You made it. Against everything, all of you made it through to the light."),
  [t("First light.", "First light.", "First light."),
   t("Help reaches the tower.", "Help reaches the tower.", "Help reaches the tower.")])

P(107,
  t("From the tower, you watch the water. Far off, a lamp lifts and falls in the swell. It grows, a little. Something is coming, at last. It is too far yet to see what. But a lamp, out there, means a hand. And a hand, right now, means hope. You keep your eyes on it, and you wait.",
    "From the tower, you watch the water, where far off a lamp lifts and falls in the swell and slowly grows. Something's coming at last, too far yet to make out. But a lamp out there means a hand — and a hand, right now, means hope. You keep your eyes on it, and wait.",
    "From the tower, you keep your eyes fixed on the water, where far off a lamp lifts and falls in the swell and slowly, steadily grows. Something is coming at last, too far away yet to make out what. But a lamp out there means a hand on it — and a hand, right now, at the end of a night like this, means hope. So you keep your eyes on it, and you wait, and you let yourself hope."),
  [t("To the lamp.", "To the lamp.", "To the lamp."),
   t("Hold the watch.", "Hold the watch.", "Hold the watch.")])


# ============================ CLOSING HUBS ================================

P(110,
  t("First light comes at last. Now the night adds up to what it is. Whatever you did up in that tower, in the storm, comes home now. Some of it you can be proud of. Some of it you cannot. This is where it all comes clear.",
    "First light comes at last, and the night adds up to what it is. Whatever you did up in that tower, in the storm, comes home now — some of it to be proud of, some of it not. This is where it all comes clear.",
    "First light comes at last, and now the whole long night adds up, quietly, to exactly what it was. Whatever you did up in that tower, in the teeth of the storm — every choice, every drop of oil kept or spilled — comes home now to be counted. Some of it you can be proud of. Some of it, if you're honest, you can't. This is the hour where all of it comes clear."),
  [t("The boat's safe; the light held.", "The boat made harbour; the light held.", "The boat made harbour; the light held."),
   t("You saved Ash on the water.", "You answered the light, and saved Ash.", "You answered the light, and saved Ash."),
   t("Weigh the rest.", "Weigh the rest.", "Weigh the rest.")])

P(111,
  t("The night adds up. Not with one big act, maybe. But with many small ones. What you kept. What you refused. Who you climbed for. It all counts, in the end. It all made the night what it was. So, what did the night come to?",
    "The night adds up — not always with one big act, but with many small ones. What you kept, what you refused, who you climbed for. It all counts in the end; it all made the night what it was. So what did the night come to?",
    "The night adds up, and not always in the way you'd expect. Not with one grand act, usually, but with a great many small ones: what you kept, what you had the sense to refuse, who you climbed for when climbing cost you. All of it counts, in the end. All of it, together, made the night exactly what it was. So: what did it come to?"),
  [t("The whole coast, together.", "The whole coast came through together.", "The whole coast came through together."),
   t("Clean — no con.", "You did it clean — no con.", "You did it clean — no con."),
   t("Weigh the rest.", "Weigh the rest.", "Weigh the rest.")])

P(112,
  t("There is more to weigh. The night held other things too. A stranger you helped. A coat and lamp you gave away with an open hand. Small choices, made in the storm, when it would have been easy to pass by. Those choices have their own weight. What did they come to?",
    "There's more to weigh; the night held other things too. A stranger you helped. A coat and lamp you gave away with an open hand. Small choices made in the storm, when passing by would've been easy. Those have their own weight. What did they come to?",
    "There is still more to weigh, because the night held other things as well. A stranger you stopped for. A coat and lamp you gave away with an open hand, when nobody would have known if you hadn't. Small, hard choices made in the full storm, when passing by would have been the easiest thing in the world. Those choices carry their own quiet weight. What, in the end, did they come to?"),
  [t("A stranger sees you home.", "A stranger you helped sees you home.", "A stranger you helped sees you home."),
   t("You gave your lamp away.", "You gave your own lamp away.", "You gave your own lamp away."),
   t("Weigh the rest.", "Weigh the rest.", "Weigh the rest.")])

P(113,
  t("And what does the night leave you with? Maybe not a clean win. Maybe just the fact that you climbed. That you tried. That when it was dark, and wild, and easy to bar the door, you did not. That counts for something. It always did.",
    "And what does the night leave you with? Maybe not a clean win. Maybe just the fact that you climbed, that you tried. When it was dark and wild and easy to bar the door, you didn't. That counts for something. It always did.",
    "And what, when all is counted, does the night leave you with? Maybe not a clean win, no. Maybe just the plain fact that you climbed to the lamp, that you tried — that when it was dark and wild and so very easy to bar your own door and wait, you didn't. That counts for something, whatever else it does or doesn't. It always did count for something."),
  [t("The storm eases, late.", "The storm eases at last, late.", "The storm eases at last, late."),
   t("The coast saw you climb.", "The coast saw you climb to the lamp.", "The coast saw you climb to the lamp."),
   t("The worst of it.", "The worst of it.", "The worst of it.")])

P(114,
  t("But not every night ends well. Some choices cost more than you knew. Some doors, once opened, cannot be shut again. This is the hard end of the night, where the worst comes home. It is not easy to look at. But it is true. So look.",
    "But not every night ends well. Some choices cost more than you knew; some doors, once opened, can't be shut again. This is the hard end of the night, where the worst comes home. It isn't easy to look at — but it's true. So look.",
    "But not every night ends well, and it would be a lie to pretend otherwise. Some choices cost more than you could have known at the time; some doors, once opened onto the dark, cannot be shut again. This is the hard end of the night, then, the place where the worst of it comes home to be counted. It is not easy to look at directly. But it is true, all the same. So you look."),
  [t("You took the deal — a ship struck.", "You took the wrecker's deal — a ship struck.", "You took the wrecker's deal — a ship struck."),
   t("You were too late.", "You were simply too late.", "You were simply too late."),
   t("The storm broke in time.", "The storm broke before real harm.", "The storm broke before real harm.")])


# ============================ ENDINGS (12: 4 good / 4 neutral / 4 bad) ====

P(120,
  t("You kept the beam burning all night. Trimmed wick. Wound lens. Oil fed drop by careful drop. Then, at first light, the storm breaks. The lifeboat comes round the point. And the boat you were lighting slips at last into the harbour mouth, safe. It is safe because you climbed to the lamp, and stayed. That is the whole of it.",
    "You kept the beam burning all night — trimmed wick, wound lens, oil fed drop by careful drop. Then, at first light, the storm breaks. The lifeboat comes round the point, and the boat you were lighting slips at last into the harbour mouth, safe. It is safe because you climbed to the lamp and stayed. That's the whole of it.",
    "You kept the beam burning all night long: the wick trimmed true, the lens wound round and round, the oil fed drop by careful drop through the worst of it. Then, at first light, the storm breaks, and the lifeboat comes round the point, and the boat you were lighting slips at last into the harbour mouth, safe and whole. It is safe for one reason and one only — because you climbed to the lamp, and you stayed. That is the whole of it, and it is enough."),
  [])

P(121,
  t("You answered the light no one could explain. You went down to the cove and waded out onto the rocks. You found old Ash there, swamped and half-drowned. You got them off in time. And there was more: Ash is Nan's own child, gone from her for years. Two lives, joined again at the end of a hard night. A door both had thought shut for good, reopened.",
    "You answered the light no one could explain: down to the cove, out onto the rocks, and old Ash swamped and half-drowned. You got them off in time. And there was more — Ash is Nan's own child, gone from her for years. Two lives joined again at the end of a hard night, a door reopened that both had thought shut for good.",
    "You answered the light that no one could explain, the one out where no boat should be. Down to the cove, out onto the black rocks — and there was old Ash, swamped and half-drowned and nearly gone. You got them off in time. And there was more, unlooked for: Ash is Nan Bright's own child, gone from her for years over words neither could take back. Two lives joined again at the end of a hard night, and a door reopened that both had long thought shut for good. The mystery paid off in a life, and then in another kind of one."),
  [])

P(122,
  t("There was no one big, brave act. There was something better. You turned a frightened, dark coast into people who worked together. Hands on the rope. Wood on the signal fire. Eyes on the black water. And so, together, the whole shore came through the night. No one was left alone in it. That is what a coast can be.",
    "There was no single brave act — there was something better. You turned a frightened, dark coast into people who worked together: hands on the rope, wood on the signal fire, eyes on the black water. And so, together, the whole shore came through the night. No one was left alone in it. That's what a coast can be.",
    "There was no single, shining act of bravery here, no one heroic moment — and there was something better than that. You turned a frightened, dark coast into people who worked together: hands on the rope, wood on the signal fire, eyes fixed on the black water all night long. And so, together, in the end, the whole shore came through the night intact. No one was left alone in it. That, it turns out, is what a coast can be, when just one person climbs to the lamp first."),
  [])

P(123,
  t("You refused the con. You saw the wrecker's trick for what it was, and you turned your back on it. You kept your head. You kept the light by decent means, the hard, honest way. It was not a perfect night. You did not save everyone. But you did it clean. And clean, in the end, is enough.",
    "You refused the con — saw the wrecker's trick for what it was and turned your back on it. You kept your head, and kept the light by decent means, the hard honest way. It wasn't a perfect night; you didn't save everyone. But you did it clean, and clean, in the end, is enough.",
    "You refused the con. You saw the wrecker's trick for exactly what it was — a man who wanted the dark for the wreck in it — and you turned your back on it and walked. You kept your head, and you kept the light by decent means, the hard and honest way, the way that lets you sleep. It was not a perfect night; you didn't save everyone, and you know it. But you did it clean, start to finish. And clean, at the end of a night like this, is more than enough to carry home."),
  [])

P(124,
  t("You did not manage the whole night. But you stopped, once, for a stranger in trouble. You gave them your time when time was short. And now, at first light, that same stranger stands with you at the lamp. They hold the watch, and see you and Nan safe. A kindness, it turns out, does not stay where you leave it. It comes back around.",
    "You didn't manage the whole night — but you stopped, once, for a stranger in trouble, and gave them your time when time was short. Now, at first light, that same stranger stands with you at the lamp, holding the watch, and sees you and Nan safe. A kindness, it turns out, doesn't stay where you leave it. It comes back around.",
    "You didn't manage the whole of the night, not everything you'd hoped. But you stopped, once, for a stranger in trouble, and gave them your time and your care when both were in desperately short supply. And now, at first light, that same stranger stands beside you at the lamp, holding the watch with you, and sees you and old Nan safe through to the dawn. A kindness, it seems, never really stays where you set it down. Given away freely, it has a way of coming back around."),
  [])

P(125,
  t("You gave your own coat and lamp away. To a family with the sea at their door. To someone with nothing. And now, at first light, you are cold to the bone and worn thin. But you are not alone. The people you helped are near you. Something on this coast has changed, quietly. It is not a full win. But it is a start. And starts matter.",
    "You gave your own coat and lamp away — to a family with the sea at their door, to someone with nothing. And now, at first light, you're cold to the bone and worn thin. But you aren't alone: the people you helped are near you. Something on this coast has quietly changed. It's not a full win. But it's a start, and starts matter.",
    "You gave your own coat and lamp away, again and again — to a family with the sea already at their door, to someone who had nothing left. And now, at first light, you are cold to the bone and worn thin as rope. But you are not alone in it, and that turns out to matter more than you'd have guessed: the people you helped are close around you now. Something on this coast has shifted, quietly, over the course of the night. It is not a full win, and you won't pretend it is. But it is a start. And starts, you've come to believe, matter as much as anything."),
  [])

P(126,
  t("You scraped through the worst of it. Just. There was no clean win, and no clever plan. There was only holding on, hour by hour, until the storm eased. Then, late and grudging, the boat limped in on its own. It is not a triumph. No one will sing about it. But you are through. And, in the end, that is a kind of relief all its own.",
    "You scraped through the worst of it — just. No clean win, no clever plan. Only holding on, hour by hour, until the storm eased and the boat limped in on its own, late and grudging. It's no triumph, and no one will sing about it. But you're through — and in the end, that is a relief all its own.",
    "You scraped through the worst of it, in the end — just barely. There was no clean win to be had, and no clever plan that saved the night. There was only holding on, hour by grinding hour, until the storm finally eased and the boat limped in on its own, late and grudging, out of the greying dark. It is no triumph, and no one will ever sing about it. But you are through it, all of you, and still here. And that, at the end of a night like this, turns out to be a kind of relief entirely its own."),
  [])

P(127,
  t("You did not manage everything. Far from it. But the whole coast saw you do one thing. When it was dark, and wild, and easy to bar the door, you climbed to the lamp. You kept the watch. Others stayed inside. You did not. And people remember that. From tonight, you are someone this coast knows. That is not nothing.",
    "You didn't manage everything — far from it. But the whole coast saw you do one thing. When it was dark and wild and easy to bar the door, you climbed to the lamp and kept the watch. Others stayed inside; you didn't. And people remember that. From tonight, you're someone this coast knows. That's not nothing.",
    "You didn't manage everything — not by a long way, and you know it. But the whole coast saw you do the one thing that counted most. When it was dark, and wild, and so very easy to bar your own door and wait it out, you climbed to the lamp and kept the watch. The others stayed inside; you didn't. And people remember that kind of thing far longer than they remember who won. From tonight, whatever else is true, you are someone this coast knows by name. And that, in the end, is not nothing at all."),
  [])

P(128,
  t("You took the wrecker's deal. You let the light go dark, or fed it his fouled oil. You told yourself the boat was lost anyway. And in the dark, a ship struck the rocks. By morning there is wreckage on the shore, and the sea has taken what it wanted. The money in your pocket is cold. So is the shore. You will not forget how you earned it.",
    "You took the wrecker's deal — let the light go dark, or fed it his fouled oil, and told yourself the boat was lost anyway. And in the dark, a ship struck the rocks. By morning there's wreckage on the shore, and the sea has taken what it wanted. The money in your pocket is cold. So is the shore. You won't forget how you earned it.",
    "You took the wrecker's deal in the end — let the light go dark, or fed it his fouled, salt-cut oil, and told yourself the whole time that the boat was lost anyway. And in the dark it made, a ship struck the rocks. By morning there is wreckage strung along the shore, and a search of the tideline, and the sea has taken exactly what it wanted. The money in your pocket is cold. So is the shore, and so is everything you'll think about when you remember how you earned it."),
  [])

P(129,
  t("The cliff path was a trap, just as Carrick warned. The ledge was wet. The wind was cruel. And halfway down, the rock gave under your foot. You saved yourself — barely, somehow — but the fall took the night. You reach the cove at last soaked, broken, and far too late. The light stayed dark while you clung to the rock.",
    "The cliff path was a trap, exactly as Carrick warned. The ledge was wet, the wind cruel, and halfway down the rock gave under your foot. You saved yourself — barely — but the fall took the night. You reach the cove at last soaked, broken, and far too late. The light stayed dark while you clung to the rock.",
    "The cliff path was a trap, exactly as Carrick warned you it would be. The ledge was streaming wet, the wind cruel and gusting, and halfway down the rock simply gave way under your foot. You saved yourself — barely, somehow, clawing back to a handhold — but the fall took the night from you. You reach the cove at last soaked, broken, and far, far too late to do any good. And all the while you clung there to the rock, the light stayed dark over the sea."),
  [])

P(130,
  t("You spent the night on the wrong things. A bad deal, a wrong turn, a warm doorway you should not have stayed in. And the light went dark too long. When dawn finally comes, there is wreckage on the shore, and a slow search along the tideline. You went out into the storm. But the beam was not there when it was needed.",
    "You spent the night on the wrong things — a bad deal, a wrong turn, a warm doorway you shouldn't have stayed in. And the light went dark too long. When dawn finally comes, there's wreckage on the shore and a slow search along the tideline. You went out into the storm. But the beam wasn't there when it was needed.",
    "You spent the night, in the end, on the wrong things: a bad deal, a wrong turn, a warm doorway you should never have stayed in. And the light went dark too long, at the worst possible hour. When dawn finally comes up grey over the sea, there is wreckage strung along the shore, and a slow, quiet search along the tideline. You went out into the storm, and that was real, and it mattered. But the beam was not there when it was needed, and that, in the end, matters more."),
  [])

P(131,
  t("In the end, you stayed inside, where it was dry and safe. You told yourself the sea was too wild. The light was not your job. Someone else would climb. All of that was true. And all night, at the top of the dark tower, the great lamp stayed cold. Nothing bad happened to you. You will think about that for a long, long time.",
    "In the end, you stayed inside, where it was dry and safe. You told yourself the sea was too wild, that the light wasn't your job, that someone else would climb. All of that was true. And all night, at the top of the dark tower, the great lamp stayed cold. Nothing bad happened to you. You'll think about that for a long, long time.",
    "In the end, you stayed inside, where it was dry and safe and warm. You told yourself the sea was too wild to fight, that the light wasn't really your job, that someone else, surely, would climb the tower. And all of that was perfectly, comfortably true. And all night long, at the top of the dark tower, the great lamp stayed cold, and out past the point a boat looked for a beam that never came. Nothing bad happened to you at all. You came through the night dry and untouched. You will think about that, quietly, for a long, long time."),
  [])


# ============================ apply =======================================
def main():
    book = json.load(open(BOOK, encoding="utf-8"))
    by_id = {n["id"]: n for n in book["nodes"]}
    applied, mism = 0, []
    for nid, p in PROSE.items():
        n = by_id.get(nid)
        if not n:
            print(f"!! node {nid} not in book", file=sys.stderr); continue
        n["text"] = p["text"]
        chs, pcs = n.get("choices") or [], p.get("choices") or []
        if len(chs) != len(pcs):
            mism.append((nid, len(chs), len(pcs))); continue
        for c, pc in zip(chs, pcs):
            c["text"] = pc
        applied += 1
    json.dump(book, open(BOOK, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"Applied prose to {applied} node(s).")
    for nid, a, b in mism:
        print(f"CHOICE MISMATCH §{nid}: book {a} vs prose {b}")


if __name__ == "__main__":
    main()
