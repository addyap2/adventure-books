#!/usr/bin/env python3
"""Phase 3: pour leveled prose into 'The Cool of Evening' skeleton.

Holds A2/B1/B2 prose for each node (and each choice, in skeleton order) in PROSE, then
writes it onto content/episode-04.json in place. Nodes absent from PROSE keep their stub, so
this grows batch by batch; re-run after each and validate to keep every level in band.

House voice: quiet, humane, a little uncertain — not frightening. The mercy here is water and
shade. Sami (the lone child) is referred to as they/them.

Run: python3 scripts/phase3_ep04.py
"""
import json, os, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BOOK = os.path.join(ROOT, "content", "episode-04.json")


def t(a2, b1, b2): return {"A2": a2, "B1": b1, "B2": b2}
PROSE = {}
def P(nid, text, choices): PROSE[nid] = {"text": text, "choices": choices}


# ============================ ACT I — THE ENGINE DIES ======================

P(1,
  t("It is the hottest hour of the day. The bus coughs, shakes, and stops. Steam comes up from the engine. You are far from any town. There is no phone signal here. On the bus is a child called Sami. Sami is about eight, and travels alone. The child is quiet now, and much too hot. There is not much water left.",
    "It is the hottest hour of the day when the bus coughs, shudders and dies. Steam curls from under the hood, and you are hours from the nearest town, with no signal on any phone. On the bus is Sami, a child of about eight, travelling all alone. The child has gone quiet and flushed in the heat, and there is not much water left.",
    "It is the hottest hour of the day when the bus coughs, shudders and dies on an empty road, steam curling from under the hood. You are hours from the nearest town in either direction, and there is no signal on any phone aboard. Among the passengers is Sami, a child of about eight, travelling entirely alone. The child has gone quiet and flushed in the heat, and one look tells you the plain truth: there is very little water left."),
  [t("Look after the water.", "Take charge of the water.", "Take charge of the water."),
   t("Try the radio.", "Try the radio for help.", "Try the radio for help."),
   t("Get Sami into shade.", "Get Sami into shade first.", "Get Sami into shade first.")])

P(2,
  t("You look for what the bus has. There are a few water bottles. There is a small first-aid box. There is a big canvas sheet for shade. You put it all together. The air inside the bus is getting hot. Sweat runs down your back. You must decide what to do, and soon.",
    "You gather what the bus has aboard: a few water bottles, a small first-aid box, and a big canvas tarp. It could be rigged for shade. The air inside is already thickening with heat, and sweat runs down your back. You have to decide what to do, and do it soon.",
    "You gather what the bus has to offer: a few water bottles, a small first-aid box, and a big canvas tarp that could, with some effort, be rigged into shade. The air inside is already thickening, and sweat gathers along your back before you have done anything at all. Whatever you decide, you understand, you had better decide it soon."),
  [t("Go out to the road.", "Step out onto the road.", "Step out onto the road."),
   t("Decide how to start.", "Decide how to start.", "Decide how to start."),
   t("The sheet is torn.", "The tarp is torn and short.", "The tarp is torn and short.")])

P(3,
  t("You try the radio. It is dead. There is no signal for the phones. Word comes back from the driver, Mr Bello. Nothing moves in this heat, he says. Help will come in the evening. Sit still and stay cool. But Sami is small, and getting worse. Evening is a long way off.",
    "You try the radio, but it is dead, and no phone has a signal. Word comes back from the driver, Mr Bello: nothing moves in heat like this, so help will only come at evening. Sit tight, he says, and stay cool. But Sami is small and fading, and evening is a long way off.",
    "You try the radio and find it dead; not a single phone has a signal either. Word filters back from the driver, Mr Bello: nothing moves in heat like this, so any help will only come once the sun drops toward evening. Sit tight, he tells everyone, and stay cool. But Sami is small and already fading, and evening, from here, feels a very long way off."),
  [t("Decide how to start.", "Decide how to start.", "Decide how to start."),
   t("Sami can't wait.", "But Sami can't wait that long.", "But Sami can't wait that long.")])

P(4,
  t("You move Sami into the thin shade of the bus. It helps a little. But shade is not enough on its own. The child needs water too. You need a plan. You stand for a moment and understand. You cannot do much with empty hands.",
    "You move Sami into the thin band of shade beside the bus. It helps a little, but shade alone won't be enough — the child needs water too, and you need a plan. You stand a moment and understand: with empty hands, you can't do much good here.",
    "You move Sami into the thin band of shade beside the bus, and it helps, a little. But shade alone will not be enough; the child needs water as much as shadow, and you need something like a plan. You stand for a moment in the glare and understand, clearly, that with empty hands you cannot do very much good for anyone here."),
  [t("Go and get supplies.", "Go back and organise supplies.", "Go back and organise supplies."),
   t("See how bad it is.", "Feel how serious this is.", "Feel how serious this is.")])

P(5,
  t("You step down onto the road. The glare is white and hard. Ochre flats run to the far ridge. The heat shakes the air. You can almost lean on it. The road is empty both ways. Far off, one shape moves. Someone is walking away down the road.",
    "You step down onto the road. The glare is white and hard, ochre flats running all the way to the shimmering ridge, the heat thick enough to lean on. The road is empty in both directions — except, far off, for one small shape, moving away.",
    "You step down onto the road, where the glare comes up white and hard off the tarmac, and ochre flats run to a far ridge that shivers in the heat. The air is thick enough, almost, to lean on. The road lies empty in both directions — save, far off, for a single small shape, moving slowly away from the bus."),
  [t("Mr Bello opens the stores.", "Mr Bello opens the bus's stores.", "Mr Bello opens the bus's stores."),
   t("Ask the others for water.", "Ask along the seats for water.", "Ask along the seats for water."),
   t("Decide how to start.", "Decide how to start.", "Decide how to start."),
   t("Someone walked off.", "A passenger has wandered off.", "A passenger has wandered off down the road.")])

P(6,
  t("You stand and think. You could sort out the water and shade first. You could go straight to Sami and stay with the child. Or you could ask the other people to help. Each choice takes time. And in this heat, time costs water.",
    "You make yourself think. You could sort out supplies first — water, shade, a plan. You could go straight to Sami and stay by the child. Or you could go seat to seat and get the passengers helping. Each choice costs time, and in this heat, time costs water.",
    "You make yourself stand still and think it through. You could sort out supplies first, and do the water and shade properly. You could go straight to Sami and simply not leave the child's side. Or you could work the aisle seat by seat and turn the passengers into help. Every choice costs time — and out here, time is measured in water."),
  [t("The bus's stores.", "The bus's stores.", "The bus's stores."),
   t("Straight to Sami.", "Straight to Sami.", "Straight to Sami."),
   t("Ask the others for help.", "Go seat to seat for help.", "Go seat to seat to gather help.")])

P(8,
  t("You feel the heat in your chest. And you think of Sami, small and quiet, with no water, in air like an oven. Heat like this can kill a child. That is not a fear. It is a fact. No one else is going to act. So it is you.",
    "You feel the heat sit heavy in your chest, and you think of Sami — small, gone quiet, with no water, in air like an oven. Heat like this can kill a child. That isn't a fear; it's a fact. No one else is going to move. So it has to be you.",
    "You feel the heat sit heavy in your chest, and you think of Sami: small, gone quiet, with next to no water, in air that has the weight of an oven. Heat like this can kill a child, and quickly. That is not a fear any more; it is simply a fact. No one else on this bus is going to move first. So, ready or not, it has to be you."),
  [t("Decide how to start.", "Decide how to start.", "Decide how to start."),
   t("To the stores.", "To the bus's stores.", "To the bus's stores."),
   t("A rush for the water.", "A rush on the water at the front.", "A rush on the water at the front.")])

P(9,
  t("Mr Bello opens the luggage bay. He looks ashamed. Inside there is a crate of water bottles. There is a first-aid box. There is a big canvas sheet, and some old rags. \"Take what you need,\" he says. He is a kind man, out of his depth.",
    "Mr Bello opens the luggage bay, shame all over his face. Inside is a crate of water bottles, a first-aid box, a big canvas tarp and some spare rags. \"Take what you need,\" he says quietly. He is a kind man, well out of his depth.",
    "Mr Bello swings open the luggage bay, shame written plainly across his face. Inside sit a crate of water bottles, a first-aid box, a big canvas tarp, and a bundle of spare rags. \"Take what you need,\" he says quietly, not quite meeting your eye. He is a kind man, you can see, and completely out of his depth."),
  [t("Take charge of the water.", "Take charge of the water crate.", "Take charge of the water crate."),
   t("Just the sheet and rags.", "Just the tarp and rags.", "Just the tarp and rags."),
   t("Ask Bello what he knows.", "Ask Bello what he knows.", "Ask Bello what he knows."),
   t("He gives you a cool bottle.", "He hands you the last cool bottle.", "He hands you the last cool bottle.")])

P(10,
  t("You go along the seats. Old Mr Danso sits there, confused. His mouth is dry. He pulls at his collar. He does not know where he is. He looks up at you with frightened eyes. You have a lot to do. But he is here, and he is scared.",
    "You move along the seats and find old Mr Danso, confused and dry-mouthed, plucking at his collar. He doesn't seem to know quite where he is, and he looks up at you with frightened eyes. You have a great deal to do — but he is here, and he is scared.",
    "You move along the aisle and come to old Mr Danso, confused and dry-mouthed, plucking weakly at his collar as though it were choking him. He does not seem to know quite where he is, and he turns frightened eyes up to you. You have a great deal to do and very little time — but the old man is here, in front of you, and he is scared."),
  [t("Stop and help him.", "Stop and help him.", "Stop and help him."),
   t("Go and see to Sami.", "Say you must see to Sami.", "Say you must see to Sami.")])

P(11,
  t("You get to Sami fast, with what little you have. A few sips, a wet cloth, some shade. The child steadies for a moment. But it will not last. You need real water, and more of it, soon. You cannot sit here and hope.",
    "You reach Sami fast with what little you have — a few sips, a wet cloth, a scrap of shade. It steadies the child for a moment. But it won't hold; you need real water, and more of it, and soon. You can't just sit and hope.",
    "You reach Sami fast with what little you have to give — a few careful sips, a wet cloth, a scrap of shade dragged over the seat. It steadies the child, for a moment. But it will not hold, and you know it; you need real water, and more of it, and soon. Sitting here and hoping is not a plan."),
  [t("Find more water.", "Decide how to reach more water.", "Decide how to reach more water."),
   t("The heat hits you too.", "The heat presses on you too.", "The heat presses on you too.")])

P(12,
  t("You go from seat to seat. You ask each person the same thing. Share your water. Share your shade. Let's watch the weak ones together. Some people look away. But some look up and nod. It only takes a few to start.",
    "You go seat to seat, asking each person the same thing: share your water, share your shade, and let's watch over the weak together. Some look away. But a few meet your eye and nod — and it only takes a few to begin.",
    "You work your way down the aisle, seat by seat, asking each person the same simple thing. Share what water you have, share what shade there is, and let us watch over the weakest between us. Some look pointedly away. But a few meet your eye and nod — and it only ever takes a few to begin the rest."),
  [t("The people help.", "The passengers turn out to help.", "The passengers turn out to help."),
   t("No one moves; go alone.", "No one moves; go on alone.", "No one moves; go on alone.")])

P(13,
  t("You take charge of the water crate. It is heavy in your arms. Every bottle matters now. If you share it well, and go slow, there is enough. If people grab and waste it, there is not. So you count it, and you keep it close.",
    "You take charge of the water crate. It's heavy, and every bottle in it matters now. Shared out slowly and fairly, there's enough to get through; grabbed at and wasted, there isn't. So you count it, and you keep it close.",
    "You take charge of the water crate, heavy and cool against your chest, and understand at once that every bottle in it matters now. Rationed slowly and shared out fairly, there is just enough to see the bus through; grabbed at and spilled, there is nothing like enough. So you count it, and you keep it close, and you do not let it out of your sight."),
  [t("Get it to Sami.", "Now, get it to Sami and the weak.", "Now, get it to Sami and the weak."),
   t("Thank Bello.", "Thank Bello.", "Thank Bello.")])

P(14,
  t("You take the sheet and the rags. They will make shade, and that helps. But you have no water set aside. Shade keeps the sun off. It does not fill a dry mouth. You will still need to find water, and find it soon.",
    "You take the tarp and the rags. They'll make shade, which helps — but you've secured no water. Shade keeps the sun off; it doesn't wet a cracked mouth. You'll still have to find water, and find it soon.",
    "You take the tarp and the bundle of rags. They will make shade, and shade is not nothing — but you have set no water aside, and that is the thing that matters most. Shadow keeps the sun off a body; it does nothing for a cracked mouth. You will still have to find water, somewhere, and you will have to find it soon."),
  [t("Find more water.", "Now the way to more water.", "Now the way to more water."),
   t("Ask Bello what he knows.", "Ask Bello what he knows.", "Ask Bello what he knows.")])

P(15,
  t("Auntie Rose knows this road. She has done it many times. \"Stay off the open flats,\" she says. \"They look near. They are not.\" She warns you about the pickup man too. \"Ration every drop. Wait out the sun. That is how you live out here.\"",
    "Auntie Rose knows this road; she's crossed it many times. \"Stay off the open flats,\" she says. \"They look close. They aren't.\" She warns you off the pickup man too. \"Ration every drop, wait the sun out. That's how people live out here.\"",
    "Auntie Rose knows this road better than anyone aboard; she has crossed it more times than she can count. \"Stay off the open flats,\" she tells you, low and certain. \"They look close. They never are.\" She warns you, too, about the man in the pickup. \"Ration every drop, and wait the sun right out. That is the only way people live out here.\""),
  [t("Take it to heart.", "Take it to heart.", "Take it to heart."),
   t("On with it.", "On with it.", "On with it.")])

P(16,
  t("You settle Mr Danso in the shade. You give him a mouthful of water. Slowly, his eyes come back to you. \"Thank you,\" he says. His hand shakes in yours. You promise to check on him again. Then you turn back to the day.",
    "You settle Mr Danso in the shade and give him a slow mouthful of water. Bit by bit his eyes clear and come back to you. \"Thank you,\" he says, his hand shaking in yours. You promise to look in on him again, and turn back to the day.",
    "You settle Mr Danso into the deepest shade you can find and coax a slow mouthful of water into him. Bit by bit his eyes clear and find your face. \"Thank you,\" he manages, his hand trembling in yours. You promise to look in on him again before long, and then you turn, reluctantly, back to the day and everything it still needs from you."),
  [t("On toward Sami.", "On toward Sami.", "On toward Sami."),
   t("Check the others too.", "He asks you to check the others.", "He asks you to check the others.")])

P(17,
  t("You press on to see to Sami. The child comes first. Everything else can wait a little. But you still have to decide how. Do you find real water first? Or go straight to the child's side?",
    "You press on to see to Sami; the child comes first, and everything else can wait a moment. But you still have to decide how — whether to secure real water first, or go straight to the child's side.",
    "You press on to see to Sami, because the child comes first and most of the rest can wait a little longer. Even so, you still have to decide the how of it: whether to secure real water first and bring it back, or simply go straight to the child's side and not leave it."),
  [t("Get supplies first.", "The bus's stores first.", "The bus's stores first."),
   t("Straight to the child.", "Straight to the child.", "Straight to the child.")])

P(18,
  t("The heat is in you now too. Your head is light. Your mouth is dry. Your legs feel far away. You are near your own limit, and you know it. If you go down, no one is left to help Sami. So be careful. Move slow.",
    "The heat is in you now as well — your head light, your mouth dry, your legs oddly far away. You're near your own limit, and you know it. If you go down, there's no one left for Sami. So move slowly, and be careful.",
    "The heat is inside you now, too: your head gone light, your mouth papery, your legs somehow further away than they should be. You are near your own limit, and you are clear-headed enough, still, to know it. If you go down out here, there is no one left to stand between Sami and the sun. So move slowly. Be careful."),
  [t("The pickup man is ahead.", "The pickup man's dust is ahead.", "The pickup man's dust is ahead."),
   t("Push on.", "Push on.", "Push on.")])

P(19,
  t("The bus wakes up to itself. People start to move and share. One woman has a big water carrier. A man rigs the sheet for shade. A plan takes shape, seat by seat. You are not alone in this now. That changes everything.",
    "The bus wakes up to itself. People begin to move and share. One woman produces a big water carrier; a man rigs the tarp for shade; and a plan takes shape seat by seat. You aren't doing this alone any more — and that changes everything.",
    "The bus seems to wake up to itself. People begin to move, and to share. One woman produces a big water carrier she'd kept quiet about; a man sets to rigging the tarp for shade; and a plan takes shape along the aisle, seat by seat. You are not doing this alone any more — and that, more than anything, changes what the afternoon can become."),
  [t("Lead the way to Sami.", "Lead the way to Sami.", "Lead the way to Sami."),
   t("Make one shaded spot.", "Set up one shaded spot first.", "Set up one shaded spot first.")])

P(20,
  t("No one moves. People look at their hands, or out at the glare. They are scared, and scared people go quiet. You cannot force them. So you turn away, and go on alone. It is harder this way. But Sami cannot wait.",
    "No one moves. People stare at their hands, or out at the glare — scared, and scared people go quiet. You can't force them. So you turn away and go on alone; it's harder this way, but Sami can't wait for them to be brave.",
    "No one moves. People look at their hands, or out through the windows at the white glare, saying nothing — because they are frightened, and frightened people go still and quiet. You cannot force courage into anyone. So you turn away and go on alone; it is harder this way, and slower, but Sami cannot wait for a busload of strangers to find their nerve."),
  [t("The bus's stores.", "The bus's stores.", "The bus's stores."),
   t("On to the water.", "On to the water.", "On to the water.")])

P(21,
  t("Supplies are sorted. Now you need real water. There are two ways to the ridge. You can keep to the road. It is long, but you can follow it. Or you can cut across the open flats. That is short, but there is no path, and no shade.",
    "Supplies are sorted; now you need real water. There are two ways to the ridge. Keep to the road, which is long but easy to follow. Or cut straight across the open flats — much shorter, but pathless, shadeless and unknown.",
    "Supplies are sorted, more or less, and now the thing you truly need is water. Two ways lead toward the ridge and its promise of it. You can keep to the road, which is long but at least follows itself and cannot lose you. Or you can cut straight across the open flats: far shorter on the map, and pathless, shadeless and treacherous in every other way."),
  [t("Keep to the road.", "Keep to the road.", "Keep to the road."),
   t("Cut across the flats.", "Cut across the flats.", "Cut across the flats."),
   t("The pickup man is ahead.", "The pickup man's dust ahead.", "The pickup man's dust ahead.")])

P(22,
  t("You take Rose's words to heart. Ration the water. Keep off the flats. Do not trust the man in the pickup. Wait out the worst of the sun. It is good advice, and simple. Now you just have to follow it.",
    "You take Rose's words to heart. Ration the water. Stay off the flats. Don't trust the man in the pickup, and wait the worst of the sun out. It's simple advice, and good. Now you just have to actually follow it.",
    "You take Rose's words to heart, one by one. Ration the water carefully. Stay well off the open flats. Put no trust in the man with the pickup, and wait the very worst of the sun out rather than fight it. It is simple advice, and good — the kind that is easy to nod at and hard, when the heat is on you, to actually keep."),
  [t("On the way.", "On the way.", "On the way."),
   t("Back to the stores.", "Back to the stores.", "Back to the stores.")])

P(23,
  t("You feel steadier for the good turn you did. Helping someone helps you too, somehow. Your head is clearer now. Your feet feel surer. There is more to do, and the sun is still high. But you can do it.",
    "You feel steadier for the good turn you did — helping someone seems, oddly, to help you too. Your head is clearer, your feet surer. There's more to do, and the sun's still high, but you feel able to do it.",
    "You feel steadier for the good turn you did; helping someone, it turns out, helps you too, in some quiet way you can't quite name. Your head is clearer than it was, your feet a little surer under you. There is a great deal still to do, and the sun is still murderously high — but, for the first time, you feel able to do it."),
  [t("On with the afternoon.", "On with the afternoon.", "On with the afternoon."),
   t("Gather more help.", "Gather more help.", "Gather more help.")])

P(24,
  t("A pickup truck is parked on the road's edge. The engine ticks in the heat. A man leans against it, smiling. He has bottled water, and a ride to town. Around him, a small crowd stands. They look scared, and thirsty, and ready to pay.",
    "A pickup truck sits on the shoulder, engine ticking in the heat. A man leans against it, all smiles, with bottled water and lifts to town on offer. A small crowd has gathered round him — scared, thirsty, and ready to pay.",
    "A pickup truck sits on the shoulder, its engine ticking as it cools, and a man leans against the door with an easy smile. He has bottled water, he says, and lifts to town for anyone who needs one. A small crowd has already gathered around him — scared, thirsty people, exactly the kind who are ready to pay whatever he asks."),
  [t("Hear what he sells.", "Hear what he's selling.", "Hear what he's selling."),
   t("Go round him.", "Go round him.", "Go round him.")])

P(25,
  t("You lead a small group toward Sami and the shade. Walking together, you feel stronger. People carry water, and rags, and hope. \"This way,\" you say. And they come. It is a good feeling, in a hard hour.",
    "You lead a small group toward Sami and the shade. Walking together, you all feel stronger; people carry water, rags, a little hope. \"This way,\" you say, and they come — a good feeling, in a hard hour.",
    "You lead a small group back toward Sami and the shade, and walking together, all of you seem to stand a little straighter. People carry water, and rags, and something like hope between them. \"This way,\" you tell them, and they come — which is a surprisingly good feeling, in an hour as hard as this one."),
  [t("The way.", "The way.", "The way."),
   t("Smoke at the siding.", "The smoke out at the siding.", "The smoke out at the siding.")])

P(29,
  t("The sheet is torn, and too short. It will not make much shade. You have only the rags now. It is not enough for everyone. You will have to make do, or go back for something better.",
    "The tarp is torn and too short to make much shade; you're left with just the rags, which won't cover everyone. You'll have to make do — or head back to the stores for something better.",
    "The tarp turns out to be torn and far too short to throw much shade at all, which leaves you with a handful of rags that won't begin to cover everyone who needs covering. You will have to make do with what you have — or go back to the stores and hope for something better."),
  [t("Out to the road.", "Out onto the road.", "Out onto the road."),
   t("Back for better.", "To the stores for better.", "To the stores for better.")])

P(36,
  t("The bus makes one shaded spot. You rig the sheet up high. You pool the water in the middle. You put the weak ones — the old, the small — where it is coolest. It is not much. But it is a plan, and it is shared.",
    "The bus builds one shaded spot. The tarp is rigged high, the water pooled in the middle, the weakest — the old, the small — settled where it's coolest. It isn't much. But it's a plan, and it belongs to everyone now.",
    "Together, the bus builds one proper shaded spot. The tarp is strung up high, the water pooled where all can see it, the weakest — the very old, the very small — settled into the coolest heart of it. It is not much against a sky like this. But it is a plan, and, better than that, it is a plan the whole bus now shares."),
  [t("Get Sami into it.", "Get Sami into it.", "Get Sami into it."),
   t("Fetch more people.", "Fetch more passengers.", "Fetch more passengers.")])

P(37,
  t("Seat by seat, the scared bus becomes a working one. People have jobs now. One watches the children. One shares the water. One keeps the shade up. Fear turns into doing. And doing is much better than waiting.",
    "Seat by seat, the frightened bus becomes a working one. People have jobs now — one watches the children, one shares the water, one holds up the shade. Fear turns into doing, and doing beats waiting every time.",
    "Seat by seat, the frightened bus turns into a working one. People have jobs now, small and clear ones: one keeps an eye on the children, one shares out the water a mouthful at a time, one holds the shade up against the wind. Fear becomes doing — and doing, you have always found, beats sitting and waiting every single time."),
  [t("To the water.", "To the water.", "To the water."),
   t("The last hard stretch.", "The last stretch of the heat.", "The last stretch of the heat.")])

P(60,
  t("Someone points down the road. A passenger has walked off, they say. Off toward the shimmer, dazed by the heat. Alone, in the open, in the sun. That way lies nothing but heat and distance. If no one goes, they will not come back.",
    "Someone points down the road: a passenger has wandered off, they say, out toward the shimmer, dazed by the heat. Alone, in the open sun, with nothing that way but heat and distance. If no one goes after them, they won't come back.",
    "Someone catches your arm and points down the road: a passenger has wandered off, they say, out toward the shimmering line of the horizon, plainly dazed by the heat. Alone, in the open, under a sun like this, with nothing in that direction but more heat and more distance. If no one goes after them, everyone seems to understand, they will not come back on their own."),
  [t("Go after them.", "Go after them.", "Go after them."),
   t("No time — Sami first.", "No time — Sami first.", "No time — Sami first.")])

P(61,
  t("You find them in a dry gully. They stumble, and blink, and do not know your face. The sun has struck them hard. Their skin is dry, not wet. That is a bad sign. You take their arm. \"Come with me,\" you say. \"This way. Slowly.\"",
    "You find them in a dry gully, stumbling, blinking, not knowing your face. The sun has struck them hard; their skin is dry, not damp, which is a bad sign. You take their arm. \"Come with me,\" you say. \"This way. Slowly now.\"",
    "You find them at last in a dry gully, stumbling and blinking, no recognition at all in their face when they look at you. The sun has struck them hard: their skin is dry rather than damp, which is exactly the sign you did not want to see. You take their arm, gently. \"Come with me,\" you say, keeping your voice level. \"This way. Slowly does it.\""),
  [t("Walk them back.", "Walk them back.", "Walk them back."),
   t("On to Sami.", "On to Sami.", "On to Sami.")])

P(62,
  t("You cannot do everything. Sami needs you most. So you send word for someone else to go after the lost passenger. Then you press on. It sits badly with you. But you have to choose, and you choose the child.",
    "You can't do everything at once, and Sami needs you most. So you send word for someone else to go after the lost passenger, and press on. It sits badly with you — but you have to choose, and you choose the child.",
    "You cannot do everything at once, and Sami, of everyone, needs you most. So you send word back for someone else to go after the lost passenger, and you press on. It sits badly with you, this choosing — but choosing is exactly what the afternoon keeps demanding, and this time you choose the child."),
  [t("Decide how to start.", "Decide how to start.", "Decide how to start."),
   t("On toward the water.", "On toward the water.", "On toward the water.")])

P(63,
  t("You walk them back to the bus. Their family is there, and cries out with relief. They give you a bottle to share, and a place in the shade. \"Thank you,\" they say, over and over. A kindness never stays still. It moves.",
    "You walk them safely back to the bus, where their family cries out with relief. They press a bottle on you to share and make you a place in the shade. \"Thank you,\" they keep saying — because a kindness never stays still; it moves.",
    "You walk them all the way back to the bus, where their family cries out with relief and half-falls on the two of you. They press a bottle into your hands to share and make you a place in the best of the shade. \"Thank you,\" they keep saying, over and over — and you think, not for the first time, that a kindness never really stays still. It moves."),
  [t("On toward the water.", "On toward the water.", "On toward the water."),
   t("The last hard stretch.", "The last stretch of the heat.", "The last stretch of the heat.")])

P(67,
  t("Bello presses the last cool bottle on you. \"For the child,\" he says. \"Go on. I'll stay with the engine.\" His hands are black with oil, and shaking a little. He wants to help, and this is how he can. You take it, and thank him.",
    "Bello presses the last cool bottle on you. \"For the child,\" he says. \"Go on — I'll stay with the engine.\" His hands are black with oil, and shaking a little. This is the help he has to give, and he gives it. You take it, and thank him.",
    "Bello presses the last genuinely cool bottle into your hands. \"For the child,\" he says. \"Go on — I'll stay here with the engine.\" His hands are black with oil and shaking, just slightly. And you understand that this small thing is the help he has to give, so he is giving it. You take the bottle, and you thank him, and you mean it."),
  [t("On the way.", "On the way.", "On the way."),
   t("His warning first.", "His warning first.", "His warning first.")])

P(68,
  t("At the front of the bus, people rush the water. Voices rise. Hands grab. Fear has caught, and it spreads fast. One more push and it will be a fight. You have a choice. Calm them, and share it out. Or fight your own way in.",
    "At the front of the bus, people are rushing the water — voices rising, hands grabbing, fear catching and spreading fast. One more shove and it's a fight. You can try to calm them and share it out fairly, or fight your own way through to the crate.",
    "At the front of the bus, people have begun to rush the water: voices climbing, hands grabbing, fear catching like dry grass and spreading down the aisle. One more shove and it becomes an outright fight over bottles. You have a choice to make, and quickly — try to calm them and share the water out fairly, or simply fight your own way through to the crate."),
  [t("Calm them, share it.", "Calm it, and get them sharing.", "Calm it, and get them sharing."),
   t("Get to the crate.", "Get to the crate.", "Get to the crate.")])


# ============================ ACT II — THE LONG AFTERNOON ==================

P(26,
  t("The road is long and hard. The tarmac is soft with heat. Far off, false pools of water shine on it, then vanish. There is no shade at all. But the road is clear, and it goes where you need to go. You keep walking.",
    "The road is long and punishing. The tarmac is soft underfoot; mirage pools shine ahead and vanish as you reach them; and there's not a scrap of shade anywhere. But it's clear, and it runs where you need to go. So you keep walking.",
    "The road is long and quietly punishing: the tarmac gone soft underfoot, false pools of water shining just ahead and dissolving the moment you reach them, and not one scrap of shade the whole way. But it is clear, at least, and it runs where you need it to run. So you put your head down and keep walking."),
  [t("Press on.", "Press on.", "Press on."),
   t("Someone's stuck ahead.", "Someone's stuck ahead.", "Someone's stuck ahead."),
   t("The empty plain.", "The whole plain, empty and shimmering.", "The whole plain, empty and shimmering.")])

P(27,
  t("The flats would cut the way in half. The ridge looks so close from here. But the ground is open and flat. There is no path. There is no shade. And the heat sits on it like a heavy hand. Rose said to stay off it. She was not joking.",
    "The flats would halve the way, and the ridge looks so close from here. But the ground is open and trackless, with no path and no shade, and the heat sits on it like a heavy hand. Rose told you to stay off it — and she wasn't joking.",
    "The flats would halve the way, and from here the ridge looks close enough to touch. But the ground out there is open and trackless, with no path to follow and no shade to break for, and the heat sits on all of it like a heavy, pressing hand. Rose told you plainly to stay off the flats — and Rose, you already know, was not joking."),
  [t("Risk the flats.", "Risk the flats.", "Risk the flats."),
   t("Too risky — back to the road.", "Too dangerous — back to the road.", "Too dangerous — back to the road.")])

P(28,
  t("You step out onto the open flats. At once, it feels wrong. The ridge does not come any closer. Behind you, the road blurs and fades in the shimmer. There is nothing out here but heat and light. And you are in the middle of it, alone.",
    "You step out onto the open flats, and at once it feels wrong. The ridge comes no closer; behind you the road blurs and fades into the shimmer. There's nothing out here but heat and hard light — and you're in the middle of it, alone.",
    "You step off the road onto the open flats, and almost at once it feels wrong. The ridge, however long you walk toward it, comes no closer; behind you the road smears and dissolves into the shimmer until you can't be sure it's there. There is nothing out here at all but heat and hard, flat light — and you are in the very middle of it, entirely alone."),
  [t("Push on across.", "Push on across.", "Push on across."),
   t("The horizon bends.", "The horizon warps and slides.", "The horizon warps and slides.")])

P(30,
  t("The road runs on under the white sun. The heat grows worse by the hour. Your shadow is small and hard beneath you. Ahead, a car is stopped at the roadside. The sun beats down on your neck. There is a signpost too, its paint gone.",
    "The road runs on under the white sun, the heat worsening by the hour, your shadow shrunk hard beneath your feet. Ahead, a car sits stalled at the roadside; the sun hammers your neck; and there's a signpost, its paint long blistered away.",
    "The road runs on under a white, pitiless sun, the heat deepening by the hour until your own shadow has shrunk to a hard little pool beneath your feet. Ahead of you a car sits stalled at the roadside, and the sun hammers down on the back of your neck like a weight. Off to one side stands a signpost, its paint long since blistered clean away."),
  [t("A stalled family.", "A family stalled at the roadside.", "A family stalled at the roadside."),
   t("Press on.", "Press on.", "Press on."),
   t("The sun on your neck.", "The sun sits on your neck.", "The sun sits on your neck like a weight."),
   t("A blank signpost.", "A signpost, paint blistered off.", "A signpost, paint blistered off.")])

P(31,
  t("A car sits stuck in the sand. An old man is slumped at the wheel. His window is down. His head hangs low. He is too hot, and too tired to move. If you stop, you lose time. If you don't, he may not last the afternoon.",
    "A car sits stuck in the sand, an old man slumped over the wheel, his window down, his head hanging. He's overheated and too spent to move. Stop, and you lose time; don't, and he may not last the afternoon.",
    "A car sits mired in the soft sand at the road's edge, an old man slumped over the wheel with his window down and his head hanging low. He is badly overheated and far too spent to help himself. If you stop, you lose time you can't spare; if you don't, there's a real chance he won't last the afternoon out here alone."),
  [t("Help push it clear.", "Help get it moving.", "Help get it moving."),
   t("Can't stop — Sami.", "You can't stop — Sami.", "You can't stop — Sami.")])

P(32,
  t("A family stands by a stopped car. They have run out of water. A small child cries, red in the face from the heat. The parents look at you with tired eyes. You have water of your own. Not much. But more than they have.",
    "A family stands by a stalled car, out of water, a small child crying and red-faced in the heat. The parents look at you with tired, hopeless eyes. You have water of your own — not much, but more than they've got.",
    "A family stands helpless by a stalled car, out of water entirely, a small child crying and gone alarmingly red in the heat. The parents turn to you with tired, half-hopeless eyes, not quite asking. You have water of your own — not much of it, and every drop already spoken for, but more, all the same, than they have."),
  [t("Give them water.", "Give them your own water.", "Give them your own water."),
   t("Promise to send help.", "Promise to send help.", "Promise to send help."),
   t("Try to make shade.", "Try to make them shade.", "Try to make them shade.")])

P(33,
  t("You go on through the worst of the heat. Each step is hard now. The air burns your throat. Ahead, you have choices to make. The pickup man may be near. So may the strange smoke at the siding. Or you can just push for the bus.",
    "You push on through the worst of the heat, each step harder than the last, the air burning your throat. Ahead lie choices: the pickup man may be near, or the strange smoke at the siding — or you can just drive for the bus.",
    "You push on through the very worst of the heat, each step costing more than the last, the air scorching the back of your throat. Ahead of you, the afternoon fans out into choices again. The pickup man is somewhere near, and so is that strange thread of smoke at the siding. Or you can put your head down and simply push for the bus."),
  [t("The pickup man again.", "The pickup man again.", "The pickup man again."),
   t("The smoke at the siding.", "The smoke at the siding.", "The smoke at the siding."),
   t("The last hard stretch.", "The last stretch of the heat.", "The last stretch of the heat."),
   t("The heat makes you doubt.", "The heat makes you doubt.", "The heat makes you doubt.")])

P(34,
  t("You help push, and the car comes free. The old man's eyes fill. He presses a warm bottle on you. \"Take it,\" he says. \"For your trouble.\" It is not cold. But it is water, and it is given with a full heart. You take it, and go on.",
    "You put your shoulder to it, and the car comes free. The old man's eyes fill; he presses a warm bottle on you. \"Take it,\" he says, \"for your trouble.\" It isn't cold — but it's water, freely given, and you take it and move on.",
    "You put your shoulder to the back of the car and heave, and at last it comes free of the sand. The old man's eyes fill with tears he's too proud to spill; he presses a warm bottle into your hands. \"Take it,\" he insists. \"For your trouble.\" It is far from cold — but it is water, given with a full heart, and you take it, and thank him, and go on."),
  [t("On your way.", "On your way.", "On your way."),
   t("He tells you of the siding.", "He tells you of the siding.", "He tells you of the siding.")])

P(35,
  t("You cannot stop, not now. But you cannot just leave them either. So you promise to send help back for them. \"Hold on,\" you say. \"Stay in the shade. I will not forget you.\" You mean it. Then you turn, and go.",
    "You can't stop now — but you can't just leave them, either. So you promise to send help back. \"Hold on,\" you tell them. \"Stay in the shade. I won't forget you.\" You mean it, too — and then you turn and go.",
    "You can't stop now, not with Sami waiting — but neither can you simply walk past them. So you promise to send help back the moment you can. \"Hold on,\" you tell them, meeting the parents' eyes. \"Stay in the shade, keep the child still. I won't forget you.\" You mean every word of it. And then you make yourself turn, and go."),
  [t("Rally the bus.", "Rally the bus.", "Rally the bus."),
   t("On through the heat.", "On through the heat.", "On through the heat.")])

P(38,
  t("The heat gnaws at your will. A small voice in you says stop. Sit down. Rest. No one would blame you. It would be so easy. But you think of Sami, waiting, and you push the voice away. Not yet. Not while the child needs you.",
    "The heat gnaws at your will. A small voice says: stop, sit down, rest — no one would blame you, and it would be so easy. But you think of Sami waiting, and you push the voice away. Not yet. Not while the child still needs you.",
    "The heat gnaws steadily at your will, and a small, reasonable voice inside you says: stop now, sit down, rest a while — no one on earth would blame you, and, God, it would be easy. But you make yourself think of Sami, waiting, and you push the voice back down where it came from. Not yet. Not while the child still needs you upright."),
  [t("The last hard stretch.", "The last stretch of the heat.", "The last stretch of the heat."),
   t("The pickup man.", "The pickup man's dust.", "The pickup man's dust.")])

P(39,
  t("You reach the signpost. The sun has eaten the paint clean off. You cannot read a word of it. One arm points to the road. One arm points out toward the smoke. Which way? You have to guess, and guess well.",
    "You reach the signpost, but the sun has eaten the paint clean off; not a word is left to read. One arm points down the road, the other out toward the smoke. Which way? You'll have to guess, and guess right.",
    "You reach the signpost at last, and find the sun has stripped the paint clean off it — not one letter of it is left to read. One weathered arm points on down the road; the other points out, unmistakably, toward that thread of smoke. Which way? There is no one to ask, so you will have to guess, and you had better guess right."),
  [t("The road.", "The road.", "The road."),
   t("The smoke.", "The smoke at the siding.", "The smoke at the siding.")])

P(50,
  t("Far out on the flats, the ridge looks nearer at last. Or does it? You cannot tell any more. The heat bends the air. It bends what you see. It may bend what you think, too. You are so tired. So dry. But you go on.",
    "Far out on the flats, the ridge seems nearer at last — or does it? You can't be sure any more; the heat bends the air, bends what you see, maybe bends what you think. You're so tired, so dry. But you go on.",
    "Far out on the flats, the ridge seems, at last, to be nearer — or does it? You honestly can't tell any more, because the heat bends the air, and bends what you see through it, and may by now be bending what you think as well. You are so tired, and so dry it hurts. But you make yourself go on, because stopping out here is the one thing you can't do."),
  [t("Nearly there.", "Nearly there.", "Nearly there."),
   t("The ground lies.", "The ground shimmers and lies.", "The ground shimmers and lies.")])

P(51,
  t("The flats go on and on. The ridge never grows. Your head swims. The horizon breaks into pieces and floats. Your legs are not yours any more. This is the moment. Go down here, in the open. Or turn back, now, while you still can.",
    "The flats go on and on, the ridge never growing, your head swimming as the horizon breaks apart and floats. Your legs aren't yours any more. This is the moment: go down here in the open — or turn back now, while you still can.",
    "The flats go on and on and on, and the ridge, mockingly, never grows any nearer. Your head swims; the horizon breaks into floating, shivering pieces; your legs stop feeling like they belong to you. This is the moment, then, the one Rose warned you about. Go down here, in the open, with no one to see — or turn back for the road now, while some small part of you still can."),
  [t("You go down.", "You go down in the open.", "You go down in the open."),
   t("Turn back now.", "Turn back for the road while you can.", "Turn back for the road while you still can.")])

P(52,
  t("You reach the foot of the ridge at last. You are staggering. Your tongue is thick. But you are there. Somehow, you crossed it. Now you must decide. Push on, spent as you are. Or face what you lost on the way.",
    "You reach the foot of the ridge at last, staggering, your tongue thick and dry — but there. Somehow, you crossed it. Now you have to decide: push on, spent as you are, or face what you lost on the way.",
    "You reach the foot of the ridge at last, staggering, your tongue thick and useless in your mouth — but there, all the same. Somehow, against everything, you crossed it. Now you have to decide what comes next: push on, spent as you are and running on nothing, or turn and face whatever it was you lost somewhere out on those flats."),
  [t("Push on, spent.", "Push on, spent.", "Push on, spent."),
   t("You lost the water.", "You dropped the water back there.", "You dropped the water somewhere back there.")])

P(53,
  t("You turn back for the road while you still can. It is the hard, right choice. You crawl the last part on your knees. When you reach the tarmac, you are shaken, and slow. The afternoon is burning away. But you are alive, and still able to help.",
    "You turn back for the road while you still can — the hard, right choice. You crawl the last stretch on your knees, and reach the tarmac shaken and slow. The afternoon is burning away. But you're alive, and still able to help.",
    "You turn back for the road while some part of you still can, and it is the hard, right choice, though it costs you the last of everything. You crawl the final stretch on your knees. When you reach the tarmac you are shaken and slow and hollowed out — and the afternoon is burning away behind you. But you are alive, and still, just, able to help."),
  [t("The long road after all.", "The long road after all.", "The long road after all."),
   t("Too spent to go on.", "Too spent to go on.", "Too spent to go on.")])

P(54,
  t("You try to make the family some shade. You prop up a door, hang a cloth, do what you can. It keeps the sun off, a little. But there is no water to give them. Shade without water only buys a little time. You have to choose.",
    "You try to rig the family some shade — a propped door, a hung cloth, whatever you can manage. It keeps the sun off a little. But there's no water to give, and shade without water only buys time. You have to choose.",
    "You try to rig the family some shade: a propped car door, a cloth hung across it, whatever your tired hands can manage from what's there. It keeps the worst of the sun off them, a little. But there is no water to give, and shade without water only ever buys a little time. So the choice comes round again, as it keeps doing."),
  [t("Give them water.", "Give them your own water.", "Give them your own water."),
   t("Promise to send help.", "Promise to send help.", "Promise to send help.")])

P(55,
  t("You hand over your own bottle. The family drink, slow and careful. Relief moves across their faces. The small child stops crying at last. \"Thank you,\" the mother says, again and again. You have less water now. But you did the right thing.",
    "You hand over your own bottle, and the family drink, slow and careful, relief spreading across their faces. The small child stops crying at last. \"Thank you,\" the mother says, over and over. You have less water now — but you did right.",
    "You hand over your own bottle without letting yourself think too hard about it, and the family drink, slow and careful, relief moving visibly across their faces. The small child stops crying at last. \"Thank you,\" the mother keeps saying, over and over, as if the words might run out. You have a good deal less water now than you did — but you know, cleanly, that you did the right thing."),
  [t("On, drier now.", "On, drier now.", "On, drier now."),
   t("They point to the siding.", "They point you to the siding.", "They point you to the siding.")])

P(56,
  t("Without your water, the heat finds you fast. Your mouth dries. Your head aches. You gave to help, and you would do it again. But the sun does not care about that. It just presses down. You have to keep your head, and keep moving.",
    "Without your water, the heat finds you fast — mouth drying, head aching. You gave to help, and you'd do it again; but the sun doesn't care about that. It just presses down. You have to keep your head, and keep moving.",
    "Without your water, the heat finds you fast now: your mouth drying to paper, a dull ache setting up behind your eyes. You gave the bottle away to help someone, and you would do it again in a heartbeat — but the sun does not care in the least about that, and only goes on pressing down. So you keep your head, because it's all you have left to keep, and you keep moving."),
  [t("Keep moving.", "Keep moving, keep your head.", "Keep moving, keep your head."),
   t("A minute of shade.", "A strip of shade offers a minute's rest.", "A strip of shade offers a minute's rest.")])

P(57,
  t("A stranger waves you into a strip of shade. \"Just a minute,\" they say. \"Sit. Breathe.\" It is cool there, out of the sun. Your body begs you to stay. But a minute can turn into an hour. And Sami is waiting.",
    "A stranger waves you into a strip of shade. \"Just a minute,\" they say. \"Sit. Breathe.\" Out of the sun it's blessedly cool, and your body begs you to stay. But a minute can slide into an hour — and Sami is waiting.",
    "A stranger waves you in under a thin strip of shade at the road's edge. \"Just a minute,\" they say kindly. \"Sit down. Breathe.\" Out of the direct sun it is blessedly, dangerously cool, and every muscle in your body begs you to stay exactly where you are. But you know how a minute slides into an hour out here — and Sami is still waiting."),
  [t("Rest, then on.", "Rest, then on.", "Rest, then on."),
   t("Refuse, press on.", "Refuse, press on.", "Refuse, press on.")])

P(58,
  t("You press on into the glare. Your mouth feels like paper. The light is so bright it hurts. Every step is a small fight. But you keep them coming, one after the next. Slow is fine. Stopping is not.",
    "You press on into the glare, your mouth like paper, the light bright enough to hurt. Every step is a small fight — but you keep them coming, one after another. Slow is fine out here. Stopping is what kills you.",
    "You press on into the glare, mouth gone to paper, the light bright enough now that it actually hurts to keep your eyes open. Every single step is its own small fight against the wish to stop. But you keep them coming, one after another after another, because slow is survivable out here — and stopping, you understand perfectly well, is what kills you."),
  [t("The last hard stretch.", "The last stretch of the heat.", "The last stretch of the heat."),
   t("On toward the water.", "On toward the water.", "On toward the water.")])

P(64,
  t("You look out over the plain. It is huge, and empty, and it shimmers in the heat. Nothing moves out there. Nothing at all. The whole world seems to be holding still. Waiting. Everything is waiting for the sun to drop. So are you.",
    "You look out over the plain — huge, empty, shimmering in the heat, nothing moving anywhere. The whole world seems to be holding still, waiting for the sun to drop at last. And so, you realise, are you.",
    "You look out over the plain, and it is vast, and empty, and shimmering silver-white in the heat, with nothing moving anywhere across the whole enormous stretch of it. The world seems to be holding its breath, waiting — waiting only for the sun to drop and let it live again. And so, you realise, standing there, are you."),
  [t("On down the road.", "Press on down the road.", "Press on down the road."),
   t("The smoke.", "The smoke at the siding.", "The smoke at the siding.")])

P(65,
  t("The sun climbs to its worst point. This is the peak of the heat. The tarmac goes soft under your feet. The air itself seems to burn. It is hard to think. Hard to breathe. This is the hour to get through. If you can, you win the day.",
    "The sun climbs to its worst; this is the peak of the heat. The tarmac is soft underfoot, the air itself seems to burn, and thinking has gone slow and hard. This is the hour to survive. Get through it, and you've all but won the day.",
    "The sun climbs to its very worst, and this, you understand, is the peak of it. The tarmac softens under your feet, the air itself seems to catch and burn, and every thought comes slow and thick. It is hard to think, hard even to breathe. This is the hour that has to be got through — and if you can get through it, you have all but won the day."),
  [t("The stalled family.", "The stalled family.", "The stalled family."),
   t("Press on.", "Press on.", "Press on.")])


# ============================ THE PICKUP MAN (the trap) ====================

P(40,
  t("The pickup man smiles at you. It is a wide, easy smile. \"Water?\" he says. \"A ride to town? I can help. Today only. Cash only.\" His bottles sit in the sun, warm and cheap. His smile does not reach his eyes. You have seen this before.",
    "The pickup man turns his easy smile on you. \"Water? A ride to town? I can help,\" he says. \"Today only. Cash only.\" His bottles sit warm in the sun, and his smile never quite reaches his eyes. You've seen this kind of help before.",
    "The pickup man turns a wide, easy smile on you as you come up. \"Water? A ride into town? I can help you out,\" he says smoothly. \"Today only, mind. Cash only.\" His bottles sit stacked and warm in the full sun, and his smile, you notice, never once reaches his eyes. You have seen this exact kind of help before, and you know what it costs."),
  [t("Hear the price.", "Hear the price.", "Hear the price."),
   t("Refuse and go round.", "Refuse and go round.", "Refuse and go round.")])

P(41,
  t("The price is robbery, plain and simple. He sees your face, and leans in close. \"That kid won't last, friend,\" he says, soft. \"What's a child worth to you?\" It is a cruel thing to say. And it is meant to work. That line is the whole trick.",
    "The price is robbery, plain and simple. He watches your face fall and leans in. \"That kid won't last, friend,\" he says softly. \"What's a child worth to you?\" It's a cruel thing to say — and it's meant to work. That line is the whole trick.",
    "The price he names is robbery, plain and simple, and he watches your face take it in before he leans in, close and soft. \"That kid won't last long, friend,\" he murmurs. \"What's a child worth to you, when it comes to it?\" It is a deliberately cruel thing to say. And it is meant, precisely, to work — because that line, you realise, is the whole of the trick."),
  [t("Pay him.", "Pay him.", "Pay him."),
   t("That's the tell — refuse.", "That line is the tell — refuse.", "That line is the tell — refuse."),
   t("Ask if it's even cold.", "Ask if the water's even cold.", "Ask if the water's even cold."),
   t("The crowd's fear.", "The crowd's fear presses in.", "The crowd's fear presses in.")])

P(42,
  t("You turn your back on him. You leave him to the frightened crowd and their cash. It feels good to walk away. He calls after you, but you do not turn round. His kind always finds someone. But not you. Not today.",
    "You turn your back on him and leave him to the frightened crowd and their cash. It feels good to walk away. He calls after you, but you don't turn round. His kind always finds someone — but not you, and not today.",
    "You turn your back on him and leave him to the frightened crowd and their fistfuls of cash. It feels surprisingly good to walk away. He calls something after you, oily and knowing, but you don't give him the satisfaction of turning round. His kind always finds someone, out here — but it won't be you, and it won't be today."),
  [t("On the way.", "On the way.", "On the way."),
   t("To the stores instead.", "To the bus's stores instead.", "To the bus's stores instead.")])

P(43,
  t("You count out the cash. It hurts to hand it over. He gives you warm bottles, and a wide smile. \"The lift will come,\" he says. \"Wait here.\" Something in you does not believe him. But it is done now. The money is gone.",
    "You count out the cash — it hurts to hand it over — and he gives you warm bottles and that wide smile. \"The lift will come,\" he says. \"Just wait here.\" Something in you doesn't believe him. But it's done now, and the money's gone.",
    "You count out the cash, and it physically hurts to press it into his hand, but you do it. He gives you warm bottles and that same wide, empty smile. \"The lift will come along, don't you worry,\" he says. \"Just wait right here.\" Something low in your stomach doesn't believe a word of it. But it is done now, whatever happens; the money is gone."),
  [t("Carry them back.", "Carry them back.", "Carry them back."),
   t("A doubt already.", "A doubt already.", "A doubt already.")])

P(44,
  t("You ask him straight. Is the water even cold? Is it clean? He smiles, and looks away. \"It's wet, isn't it?\" he says. He will not promise a thing. And that, right there, is your answer. A man who won't promise is a man with something to hide.",
    "You ask him straight: is the water even cold? Is it clean? He smiles and looks away. \"It's wet, isn't it?\" he says, and won't promise a thing. That's your answer, right there — a man who won't promise has something to hide.",
    "You ask him straight out: is the water even cold? Is it clean? He smiles and lets his eyes slide away from yours. \"It's wet, isn't it?\" he says, and that's as far as he'll go — he won't promise you a single thing. And that, right there, is your whole answer. A man who won't promise, out here, is a man with something to hide."),
  [t("That's my answer — refuse.", "That's your answer — refuse.", "That's your answer — refuse."),
   t("Buy it anyway.", "Buy it anyway.", "Buy it anyway.")])

P(45,
  t("You carry the bottles back. In your hands, they are hot. Hot as bathwater. No good to a child at all. And the lift he promised? It never comes. You wait, and watch the road. Nothing. He took your money and gave you almost nothing.",
    "You carry the bottles back, and in your hands they're hot — hot as bathwater, no good to a child at all. And the lift he promised? It never comes. You wait, you watch the road: nothing. He took your money and gave you next to nothing.",
    "You carry the bottles back, and by the time you reach the bus they're hot in your hands — hot as bathwater, no earthly use to a child in this state. And the lift he swore was coming? It never comes at all. You wait, and watch the empty road, and wait: nothing, and more nothing. He took your money and gave you, in the end, next to nothing for it."),
  [t("Flag him back.", "Try to flag him back.", "Try to flag him back."),
   t("On to Sami with nothing.", "On to Sami with nothing.", "On to Sami with nothing.")])

P(46,
  t("You open a bottle. The water tastes wrong. It is warm, and thin, and a little foul. Something is off about it. You would not give this to a child. You paid good money, and got bad water. The doubt in your gut was right all along.",
    "You crack a bottle open, and the water tastes wrong — warm, thin, faintly foul. Something's off about it; you wouldn't give this to a child. You paid good money for bad water, and the doubt in your gut was right all along.",
    "You crack a bottle open and drink, and the water tastes plainly wrong: warm, thin, and faintly, unmistakably foul, as though it came from somewhere it shouldn't have. You wouldn't give this to a child in a hundred years. You paid good money for bad water — and the small cold doubt in your gut, it turns out, was right about him all along."),
  [t("On to Sami.", "On to Sami.", "On to Sami."),
   t("Back to argue.", "Back to argue.", "Back to argue.")])

P(47,
  t("You look for him. The pickup is already gone. Only its dust hangs on the far road, thinning in the heat. The lift was never real. It was never coming. You stand there, cheated, in the middle of the empty road, with your bad, warm water.",
    "You look for him, but the pickup's already gone — only its dust hangs on the far road, thinning in the heat. The lift was never real, never coming. You stand there cheated, in the middle of the empty road, with your bad warm water.",
    "You turn to look for him, and the pickup is already gone; only its dust still hangs on the far road, thinning as you watch it. The lift was never real, of course — never once coming. You stand there in the middle of the empty road, plainly and completely cheated, holding your bad, warm, useless water, and there is no one left even to be angry at."),
  [t("On to Sami, fleeced.", "On to Sami, fleeced.", "On to Sami, fleeced."),
   t("Leave the bottles.", "Leave the hot bottles in the sand.", "Leave the hot bottles in the sand.")])

P(48,
  t("The pickup is gone. The crowd has scattered. There is only the heat now, and the empty road, and your empty pockets. You learned a hard lesson, and paid too much for it. Now you must go on with what little is left. Which is not much.",
    "The pickup's gone, the crowd scattered — only the heat now, the empty road, your empty pockets. You learned a hard lesson and paid far too much for it. Now you go on with what little is left, and it isn't much.",
    "The pickup is gone, and the crowd with it, scattered back into the glare — leaving only the heat, and the empty road, and your emptied pockets. You have learned a hard lesson this afternoon, and paid far too much for the privilege. Now you go on with whatever little is left to you, which, when you take honest stock, is not much at all."),
  [t("On to Sami.", "On to Sami.", "On to Sami."),
   t("Stand in the glare.", "Stand a moment in the glare.", "Stand a moment in the glare.")])

P(49,
  t("The crowd shoves cash at him. Hands reach out, full of money. Faces beg him to take it. And he takes it, slow, with that smile. He picks who to help by who can pay. Now you see the whole trick, plain and clear. It is ugly.",
    "The crowd shoves cash at him — hands full of money, faces begging him to take it. And he takes it, slow, with that smile, choosing who to help by who can pay. Now you see the whole trick, plain and clear. It's ugly.",
    "The crowd presses in and shoves cash at him, hands full of crumpled money, faces openly begging him to take theirs first. And he takes it, unhurried, with that same smile, choosing who to save by who can pay him most. Now you see the whole trick laid out plain and clear in front of you, and it is an ugly, ugly thing to watch."),
  [t("Hear the price anyway.", "Hear the price anyway.", "Hear the price anyway."),
   t("Refuse and go round.", "Refuse and go round.", "Refuse and go round.")])


# ============================ THE SMOKE AT THE SIDING (mystery) ============

P(70,
  t("Out on the low siding stands an old rail-stop. It has been shut for years. Everyone says so. But today a thin thread of smoke rises from it. And an old windmill turns, slow, beside it. No one can explain it. Something is there.",
    "Out on the low siding stands an old rail-stop, shut for years — everyone says so. Yet today a thin thread of smoke rises from it, and an old windmill turns slowly beside it. No one can explain it. Something, or someone, is there.",
    "Out on the low siding stands an old rail-stop, shuttered and dead for years — everyone on the bus will tell you so. And yet today a thin thread of smoke rises from its chimney, and an old windmill turns, slow and patient, beside it. No one can explain it, and no one wants to try. But something is out there, or someone — and you find you can't quite look away."),
  [t("Go and see.", "Go and see.", "Go and see."),
   t("Leave it — Sami first.", "Leave it — Sami first.", "Leave it — Sami first.")])

P(71,
  t("You reach the old siding. Up close, it looks less dead. You knock. No one answers. You knock again. Still nothing. But the door is not shut. It stands open, just a crack. Warm air, and the smell of smoke, drift out through the gap.",
    "You reach the old siding, which looks less dead up close. You knock — no answer. You knock again — nothing. But the door isn't shut; it stands ajar, and warm air and the smell of smoke drift out through the gap.",
    "You reach the old siding, and up close it looks a good deal less dead than the bus swore it was. You knock. No answer. You knock again, harder. Still nothing. But the door, you notice, is not shut at all: it stands ajar, just a crack, and warm air and the unmistakable smell of woodsmoke drift out to you through the gap."),
  [t("Go in.", "Go in.", "Go in."),
   t("Call out and wait.", "Call out and wait.", "Call out and wait."),
   t("Dust and heat inside.", "Years of dust and heat-crack inside.", "Years of dust and heat-crack inside.")])

P(72,
  t("You step inside. It is dim, and stifling hot. And there, on the floor, is an old man. He lies by a dead radio set. He barely moves. His breath is shallow. His skin is dry and grey. He has been down here a while, alone. There is no time to lose.",
    "You step inside, into a dim, stifling room — and there on the floor lies an old man, beside a dead radio set, barely moving. His breath is shallow, his skin dry and grey. He's been down here a while, alone. There's no time to lose.",
    "You step inside, into a room that's dim and stifling and thick with old heat — and there, on the floor, lies an old man, fallen beside a dead radio set, barely moving at all. His breath comes shallow; his skin is dry and greyish, the way skin should never look. He has plainly been down here a good while, alone, with no one in the world to know. There is no time at all to lose."),
  [t("Get him cool and watered.", "Get him cool and watered.", "Get him cool and watered."),
   t("Run for help.", "Run for help.", "Run for help.")])

P(73,
  t("You call out at the door. For a moment, nothing. Then a voice comes back. It is weak, and dry, and old. \"Here,\" it says. \"In here.\" Someone is inside, and they need help. You cannot walk away from that now.",
    "You call out at the door, and for a moment there's nothing. Then a voice comes back — weak, dry, old. \"Here,\" it says. \"In here.\" Someone's inside, and they need help. You can't walk away from that now.",
    "You call out into the gap of the door, and for a long moment there is nothing at all but the creak of the windmill. Then a voice comes back to you — weak, dry, old, and unmistakably real. \"Here,\" it says. \"In here.\" Someone is inside, then, and they need help; and you find, standing there, that you couldn't walk away from that now if you tried."),
  [t("Go in.", "Go in.", "Go in."),
   t("Fetch help.", "Fetch help.", "Fetch help.")])

P(74,
  t("You get to work. Water to his lips, slow and steady. A wet cloth on his neck. You fan the hot air off his face. Little by little, the old man comes back. His eyes open. \"The well,\" he says. \"Out back. Deep and cold. And the radio, if you can get it going.\"",
    "You get to work — water to his lips, slow and steady, a wet cloth on his neck, the hot air fanned off his face. Little by little the old man comes back. His eyes open. \"The well,\" he rasps. \"Out back. Deep and cold. And the radio, if you can raise it.\"",
    "You get straight to work: water to his lips, slow and patient, a wet cloth pressed to his neck, the thick hot air fanned off his face. Little by little, against the odds, the old man comes back to himself. His eyes open and find you. \"The well,\" he rasps, lifting one hand toward the back of the room. \"Out back. It's deep, and cold, and it never went dry. And the radio — the radio still works, if you can only get it to raise someone.\""),
  [t("He speaks of the road.", "He speaks of the road.", "He speaks of the road."),
   t("Get you both back.", "Get you both back to the bus.", "Get you both back to the bus.")])

P(75,
  t("You turn to run for help. Then you stop. There is no help. Not out here. Not till evening. No crews, no phones, no one coming. It is you, or it is no one. The old man on the floor knows it too. His eyes follow you to the door.",
    "You turn to run for help — then stop. There is no help out here; not till evening. No crews, no phones, no one coming. It's you or no one, and the old man on the floor knows it too. His eyes follow you to the door.",
    "You turn to run for help — and then you stop, because you already know the truth of it. There is no help out here. Not till evening, not for hours. No crews, no phones, no one coming down that dead road for either of you. It is you, or it is no one at all. And the old man on the floor knows it as well as you do; his eyes follow you, quietly, all the way to the door."),
  [t("Go back in.", "Go back in.", "Go back in."),
   t("On to Sami, torn.", "On to Sami, torn.", "On to Sami, torn.")])

P(76,
  t("The old man looks up at you. His eyes are clearer now. \"You came off the noon bus?\" he says. \"Then there's an old friend of mine on it, I'd bet. Rose. We knew each other, long ago, on this road. Tell her Faro is still here.\"",
    "The old man looks up at you, his eyes clearer now. \"You came off the noon bus?\" he says. \"Then there's an old friend of mine aboard, I'd bet — Rose. We knew each other once, long ago, on this road. Tell her Faro's still here.\"",
    "The old man looks up at you, his eyes clearer now than they were, and something like wonder crossing his face. \"You came off the noon bus?\" he says slowly. \"Then there's an old friend of mine aboard it, I'd put money on it — Rose. We knew each other once, a long time ago now, on this very road. Tell her, would you. Tell her Faro is still here.\""),
  [t("Bring them together.", "Resolve to bring them together.", "Resolve to bring them together."),
   t("On to Sami with the news.", "On to Sami with the news.", "On to Sami with the news.")])

P(77,
  t("You decide to get them face to face today. Rose and old Faro, after all these years. It is a small thing, next to water and shade. But it is not nothing. Some doors stay shut for years because no one thinks to knock. You will knock.",
    "You decide to get them face to face before the day's out — Rose and old Faro, after all these years. It's a small thing, next to water and shade. But it isn't nothing; some doors stay shut for years only because no one thinks to knock. You will.",
    "You decide, there and then, to get the two of them face to face before the day is out — Rose and old Faro, after all these long years apart. It's a small thing, you know, set beside water and shade and a child's life. But it is not nothing, either; some doors stay shut for years for no better reason than that no one ever thinks to knock. You mean to knock."),
  [t("Back to the bus.", "Back to the bus.", "Back to the bus."),
   t("Get Faro steady first.", "Get Faro steady first.", "Get Faro steady first.")])

P(78,
  t("Inside, the place holds years of dust. The air is dry and old and still. Heat has cracked the wood. Nothing has moved here in a long time. And yet, somewhere, something did move. Someone lit that fire. Someone turned that windmill on.",
    "Inside, the place holds years of dust — the air dry and old and still, the wood cracked with heat, nothing moved in a long time. And yet something did move here: someone lit that fire; someone set that windmill turning.",
    "Inside, the place holds years of undisturbed dust: the air dry and old and utterly still, the wood cracked and greyed with heat, nothing shifted in a very long time. And yet — and this is what keeps you moving forward — something did move here, and recently. Someone lit that fire. Someone set that old windmill turning again. Someone is here."),
  [t("Deeper in.", "Deeper in.", "Deeper in."),
   t("An old photo.", "An old photo, curled on the wall.", "An old photo, curled on the wall.")])

P(79,
  t("On the wall hangs an old photo. It is curled and yellow now. In it, a young man stands by this same windmill. Beside him is a young woman. Both of them are laughing. You know that face. It is Rose, from the bus, long ago. Then, from the back room, a weak sound.",
    "On the wall hangs an old photo, curled and yellowed. In it, a young man stands by this same windmill, a young woman beside him, both laughing. You know that face — it's Rose, from the bus, long ago. Then, from the back room, a weak sound.",
    "On the wall hangs an old photograph, curled and yellowed at the edges with age. In it, a young man stands proudly by this very windmill, a young woman at his side, and both of them are laughing at something outside the frame. You know that laughing face at once: it's Rose, from the bus, forty years younger. And then, from the back room, comes a weak, unmistakable sound."),
  [t("Follow the sound.", "Follow the sound, and find him.", "Follow the sound, and find him."),
   t("The years in the dust.", "The years in the dust.", "The years in the dust.")])

P(69,
  t("Years of a shut-up house press in around you. Dust, and silence, and old heat. It feels like a place where nothing lives. Then you hear it. Breathing. Slow, and shallow, and close. It comes from the back room. Someone is alive in here.",
    "Years of a shut-up house press in — dust, silence, old heat, a place where nothing seems to live. Then you hear it: breathing, slow and shallow, close by, from the back room. Someone is alive in here after all.",
    "Years of a shut-up house press in around you: dust, and silence, and the old trapped heat, everything about it saying that nothing has lived here in a very long time. And then you hear it, and your whole body goes still — breathing, slow and shallow and close, coming from the back room. Someone is alive in here, after all. Someone is barely hanging on."),
  [t("Follow the breathing.", "Follow the breathing, and find him.", "Follow the breathing, and find him."),
   t("Too much — back to Sami.", "It's too much — back to Sami.", "It's too much — back to Sami.")])


# ============================ ACT III — TOWARD THE COOL OF EVENING =========

P(90,
  t("You are back at the bus, in the last of the worst heat. Your breath is dry. Your head pounds. And there is Sami, pale in the shade, too still. This is the hour that counts. Whatever you do now, do it well. The child's life is close.",
    "You're back at the bus, in the last of the worst heat, your breath dry, your head pounding. And there's Sami — pale in the shade, too still. This is the hour that counts; whatever you do now, do it well. The child's life is close.",
    "You're back at the bus at last, in the very last of the worst heat, your breath dry and your head pounding with every step. And there is Sami, pale in the shade, gone too still for a child. This is the hour that counts, above all the others; whatever you do now, you had better do it well, because the child's life has come down close, and you can feel it."),
  [t("See to the child.", "See to the child.", "See to the child."),
   t("The pickup man's last offer.", "The pickup man's last offer.", "The pickup man's last offer."),
   t("Help arrives behind you.", "Help arrives behind you.", "Help arrives behind you.")])

P(80,
  t("The pickup rolls back one last time. The window comes down. \"Still stuck?\" he says. \"Still thirsty? This is your last chance, friend.\" The same smile. The same lie. He knows you are tired. He is counting on it. Now you choose, for good.",
    "The pickup rolls back one last time, the window sliding down. \"Still stuck? Still thirsty?\" he says. \"Last chance, friend.\" The same smile, the same lie. He knows you're tired, and he's counting on it. Now you choose, for good.",
    "The pickup rolls back one last time, and the window slides down on that same smile. \"Still stuck?\" he says, easy as ever. \"Still thirsty? This is your very last chance, friend.\" The same smile, the same lie underneath it. He knows exactly how tired you are by now, and he is counting on it to do his work for him. So now you choose, and this time for good."),
  [t("Pay him.", "Pay him.", "Pay him."),
   t("Refuse for good.", "Refuse for good.", "Refuse for good.")])

P(91,
  t("You kneel at Sami's side. The child is hot to the touch. The breathing is fast and shallow. The lips are cracked and dry. It is bad, and getting worse. You have to cool the child, and cool them now. Everything you did today comes down to this.",
    "You kneel at Sami's side. The child is hot to the touch, breathing fast and shallow, lips cracked and dry — bad, and getting worse. You have to cool them, and cool them now. Everything you did today comes down to this moment.",
    "You kneel at Sami's side and your stomach drops. The child is hot to the touch, breathing fast and shallow, lips cracked and split with dryness — bad, and plainly getting worse by the minute. You have to cool the child down, and you have to do it now, this minute. Everything you did or failed to do across the whole long afternoon comes down, in the end, to this."),
  [t("Set up real cooling.", "Set up real cooling.", "Set up real cooling."),
   t("Check the child over.", "Check the child over.", "Check the child over."),
   t("A glint far off.", "A glint far off catches your eye.", "A glint far off catches your eye.")])

P(92,
  t("Then help reaches the bus behind you. Hands, and water, and calm heads. People who know what to do. You are not alone with this now. Others are here to share the weight. It is like setting down a heavy load. You breathe out at last.",
    "Then help reaches the bus behind you — hands, water, calm heads, people who know what to do. You aren't alone with this now; others are here to share the weight. It's like setting down a heavy load, and you breathe out at last.",
    "And then, behind you, help reaches the bus at last: hands, and water, and calm heads, people who actually know what to do with a child in this state. You are not alone with it any more. Others are here now to take up their share of the weight — and it is like setting down a load you'd forgotten you were carrying. You breathe out, properly, for the first time in hours."),
  [t("To Sami together.", "To Sami together.", "To Sami together."),
   t("Hold through the worst.", "Hold through the worst.", "Hold through the worst."),
   t("Dust on the road.", "Dust on the road, far off.", "Dust on the road, far off.")])

P(93,
  t("Now you cool the child. What you can do depends on what you carried. If you kept a good store of water, you have plenty to work with. If not, you must make the very most of what little is left. Either way, you begin.",
    "Now you cool the child — and what you can do depends on what you carried. If you kept a good store of water, you've plenty to work with; if not, you must make the very most of what little remains. Either way, you begin.",
    "Now, at last, you cool the child — and exactly what you can do depends entirely on what you had the sense to carry back here. If you kept charge of a real store of water, you have plenty to work with, and a fighting chance. If you didn't, you'll have to make the very most of whatever little remains. Either way, there's no more time to weigh it; you begin."),
  [t("The water crate.", "The water crate.", "The water crate."),
   t("Wet rags and sips.", "Wet rags, shade, sips.", "Wet rags, shade, sips.")])

P(94,
  t("You check the child over, gentle and careful. Sami's eyes open, just a little. There is fear in them, and then, seeing you, less fear. \"You came back,\" the child says, so quiet. \"I said I would,\" you tell them. \"Now let's get you cool.\"",
    "You check the child over, gentle and careful, and Sami's eyes open just a little — fear in them, then, seeing you, a little less fear. \"You came back,\" the child whispers. \"I said I would,\" you tell them. \"Now let's get you cool.\"",
    "You check the child over, gentle and careful, and Sami's eyes flicker open just a little — there's fear in them at first, and then, focusing on your face, a little less of it. \"You came back,\" the child whispers, barely a sound at all. \"I said I would,\" you tell them, keeping your voice steady and light. \"Now come on. Let's get you cool.\""),
  [t("Get the child cool.", "Get the child cool.", "Get the child cool."),
   t("Break out the water.", "Break out the water.", "Break out the water.")])

P(95,
  t("You open the water crate, and it makes all the difference. Steady sips, one after the next. Wet cloths, changed often, on the neck and wrists. Slowly, the fever-heat starts to ease. Sami's breathing slows and calms. Water, shared right, is life. You knew that. Now you see it.",
    "You open the water crate, and it makes all the difference. Steady sips, wet cloths changed often at neck and wrists, the fever-heat slowly easing. Sami's breathing slows and calms. Water, shared right, is life; you knew that, and now you see it.",
    "You open the water crate, and it makes all the difference in the world. Steady, careful sips, one after another; wet cloths changed often at the neck and wrists; and, slowly, wonderfully, the fever-heat beginning to ease its grip. Sami's breathing slows and steadies and calms. Water, shared out right and kept for the ones who need it, is simply life — you always knew that in the abstract, and now, kneeling here, you see it happen."),
  [t("Hold through the worst.", "Hold through the worst.", "Hold through the worst."),
   t("Help arrives.", "Help arrives.", "Help arrives.")])

P(96,
  t("You have no crate to open. So you use what you have. You wet rags in your own last water. You drag every scrap of shade over the child. You keep Sami talking, keep those eyes open. It may be enough. It may not. But you will not stop trying.",
    "You've no crate to open, so you use what you have. Rags wet in your own last water. Every scrap of shade dragged over the child, Sami kept talking and those eyes kept open. It may be enough. It may not. But you won't stop trying.",
    "You've no crate to open, so you make do with what little you have and refuse to think about the difference. You wet rags in your own last mouthfuls of water; you drag every scrap of shade there is over the child; you keep Sami talking, and keep those eyes open by main force of will. It may be enough. It may, honestly, not. But you will not, whatever happens, stop trying."),
  [t("Hold through the worst.", "Hold through the worst.", "Hold through the worst."),
   t("It may not be enough.", "It may not be enough.", "It may not be enough.")])

P(97,
  t("The heat is deep in the child now. And you are afraid that rags and shade will not hold it back. You have done all you can with what you have. But it may not be enough. You need more. You need help, or water, or both, and soon.",
    "The heat is deep in the child now, and you're afraid rags and shade won't hold it back. You've done all you can with what you have — but it may not be enough. You need more: help, or water, or both, and soon.",
    "The heat is deep in the child now, deeper than you like, and you're honestly afraid that rags and shade alone won't be enough to hold it back. You have done everything you can with what little you have, and you know it — but everything you can may still not be enough. You need more than this. You need help, or water, or both, and you need it soon."),
  [t("Hold on to evening.", "Hold on to evening.", "Hold on to evening."),
   t("Send for the help.", "Send for the rallied help.", "Send for the rallied help.")])

P(98,
  t("You glance up, and see it. Far off across the flats, a thread of smoke. And beside it, a windmill, turning slow. Out where nothing should be. Out where the old rail-stop stands shut. It pulls at your eye. It pulls at something in you.",
    "You glance up and see it: far off across the flats, a thread of smoke, and beside it a windmill turning slowly. It's out where nothing should be, where the old rail-stop stands shut. It pulls at your eye, and at something in you.",
    "You glance up, and there it is again. Far off across the shimmering flats, a thin thread of smoke, and beside it a windmill turning slow and patient. Out where nothing at all should be, out where the old rail-stop is supposed to stand dead and shut. It pulls at your eye, that smoke, and at something deeper in you that has never learned to leave a wrong thing alone."),
  [t("See to Sami first.", "See to Sami first.", "See to Sami first."),
   t("The smoke nags.", "The smoke nags at you.", "The smoke nags at you.")])

P(99,
  t("The smoke rises where no one lives. Everyone swears the place is dead. But smoke means a fire. A fire means a hand to light it. A hand means a person. And a person, out here, alone, on a day like this, may be in real trouble. You can feel it.",
    "The smoke rises where no one lives — everyone swears the place is dead. But smoke means a fire, and a fire means a hand to light it, and a hand means a person. And a person out here alone, on a day like this, may be in real trouble. You can feel it.",
    "The smoke rises steadily from a place where everyone swears no one lives, where the whole bus insists nothing has stirred in years. But smoke means a fire, and a fire means a hand to light it, and a hand means a person. And a person out here alone, on a day as murderous as this one, may very well be in real trouble. You can feel the truth of it, pulling at you like a hook."),
  [t("Sami first.", "Sami first.", "Sami first."),
   t("Hold through the worst.", "Hold through the worst.", "Hold through the worst.")])

P(100,
  t("Now comes the long hold. You keep the child cool. You keep the water going round. You wait out the sun, hour by slow hour. It is not exciting. It is just steady, hard, careful work. But steady work is what saves people. So you do it, and you do not stop.",
    "Now comes the long hold: you keep the child cool, keep the water going round, wait the sun out hour by slow hour. It isn't exciting — just steady, hard, careful work. But steady work is what saves people, so you do it, and you don't stop.",
    "Now comes the long hold, the hardest and least dramatic part of all. You keep the child cool, you keep the water going round the shade in careful measures, and you wait the sun out, hour by grinding hour. It is not exciting, none of it; it is just steady, patient, careful work. But steady, patient work, you have learned today, is exactly what saves people out here. So you do it, and you don't stop doing it."),
  [t("Watch for the sun to drop.", "Watch for the sun to drop.", "Watch for the sun to drop."),
   t("The smoke still nags.", "The smoke still nags.", "The smoke still nags."),
   t("The worst hour.", "The afternoon's worst hour.", "The afternoon's worst hour.")])

P(101,
  t("And then, at last, it turns. The glare goes soft. The white sun slides down toward the ridge. The air, just a touch, begins to cool. And far off on the road, dust rises. A truck. A real one, coming this way. You made it to the cool of evening.",
    "And then, at last, it turns. The glare softens; the white sun slides down toward the ridge; the air begins, just faintly, to cool. And far off on the road, dust rises — a truck, a real one, coming this way. You made it to the cool of evening.",
    "And then, at long last, it turns. The glare goes soft around the edges; the white sun slides down at last toward the ridge; the air, ever so faintly, begins to cool against your skin. And far off down the road, dust rises — a truck, a real one, unmistakably coming this way. You made it. Somehow, against everything the day threw, you made it to the cool of evening."),
  [t("What it finds.", "The cool of evening, and what it finds.", "The cool of evening, and what it finds."),
   t("Evening over the flats.", "Evening over the flats.", "Evening over the flats.")])

P(102,
  t("This is the worst hour, the one just before the break. The heat has not eased yet. Your body is spent. Your will is thin. But you can feel the day starting to tip. Hold on. Hold on a little longer. The end of it is close now.",
    "This is the worst hour, the one just before the break — the heat not eased yet, your body spent, your will worn thin. But you can feel the day beginning to tip. Hold on. Hold on a little longer. The end is close now.",
    "This is the worst hour of all, the one that comes just before the break. The heat has not eased in the least, your body is spent, and your will is worn down to almost nothing. But you can feel it now, under everything — the day beginning, at last, to tip over. So you hold on. You hold on a little longer. The end of it is genuinely close now, and you know it."),
  [t("Watch for the sun to drop.", "Watch for the sun to drop.", "Watch for the sun to drop."),
   t("Vehicles far off.", "Others' vehicles far down the road.", "Others' vehicles far down the road.")])

P(103,
  t("Down the long road, you see them. Dust, and glints of glass in the low sun. Other people, other vehicles. Others got through this day too. You were not the only one out here, fighting the heat. That thought warms you, somehow, in the fading light.",
    "Down the long road you see them — dust, glints of glass in the low sun, other people, other vehicles. Others got through this day too. You weren't the only one out here fighting the heat, and that thought warms you in the fading light.",
    "Down the long road, you see them at last: dust, and bright glints of glass catching the low sun, other people and other vehicles moving again. Others got through this day too, then — you were never the only one out here, fighting the same heat, holding the same small line. And that thought, somehow, warms you more than you'd expect, there in the fading, golden light."),
  [t("The cool of evening.", "The cool of evening.", "The cool of evening."),
   t("The coming truck.", "The lights of the coming truck.", "The lights of the coming truck.")])

P(104,
  t("At last, headlights. And a long plume of dust behind them, climbing the road toward you. A truck. Real help, coming at real speed. You stand, and you wave, and your legs shake under you. It is nearly over now. Nearly. You can let yourself believe it.",
    "At last, headlights — and a long plume of dust behind them, climbing the road toward you. A truck. Real help, coming at real speed. You stand and wave, your legs shaking under you. It's nearly over now. Nearly. You let yourself believe it.",
    "At last, headlights — and behind them a long plume of dust, climbing the road toward you in the failing light. A truck. Real help, coming at real speed, coming for all of you. You get to your feet and wave both arms, your legs shaking under you with more than tiredness. It is nearly over now. Nearly. And for the first time all day, you let yourself actually believe it."),
  [t("The cool of evening.", "The cool of evening.", "The cool of evening."),
   t("What it came to.", "What the afternoon came to.", "What the afternoon came to.")])

P(105,
  t("Evening comes down over the flats. The light turns long and gold and clean. The killing heat lifts, breath by breath. Shadows stretch out from every stone. The land, so cruel an hour ago, is almost kind now. You stand and watch it, and you breathe.",
    "Evening comes down over the flats. The light turns long and gold and clean, the killing heat lifting breath by breath, shadows stretching from every stone. The land, so cruel an hour ago, is almost kind now. You stand and watch it, and breathe.",
    "Evening comes down over the flats at last, and the light turns long and gold and clean, and the killing heat lifts off the land breath by breath by breath. Shadows stretch out, blue and cool, from every stone and every scrubby bush. The land that was so purely cruel an hour ago is almost kind now, almost gentle. You just stand there and watch it happen, and you breathe, and breathe."),
  [t("The cool of evening.", "The cool of evening.", "The cool of evening."),
   t("Help reaches the bus.", "Help reaches the bus.", "Help reaches the bus."),
   t("The first cool wind.", "The first cool breath of wind.", "The first cool breath of wind.")])

P(106,
  t("Then it comes. The first cool breath of wind. It moves across the flats and touches your face. After the day you have had, it feels like a gift you did not earn. You close your eyes. You let it cool the sweat on your skin. You made it. You all made it.",
    "Then it comes — the first cool breath of wind, moving across the flats to touch your face. After the day you've had, it feels like a gift you didn't earn. You close your eyes and let it cool the sweat on your skin. You made it. You all made it.",
    "Then it comes, the thing you'd half stopped believing in: the first cool breath of wind, moving low across the flats to touch your face. After the day you've all had, it feels less like weather than like a gift you never quite earned. You close your eyes and let it move over the dried sweat on your skin. You made it. Against everything, all of you made it."),
  [t("The cool of evening.", "The cool of evening.", "The cool of evening."),
   t("Help reaches the bus.", "Help reaches the bus.", "Help reaches the bus.")])

P(107,
  t("From the bus, you watch the road. Far off, a plume of dust rises. It grows. Something is coming, at last. It is too far yet to see what. But dust, out here, means wheels. And wheels, right now, mean hope. You keep your eyes on it, and you wait.",
    "From the bus, you watch the road, where a plume of dust rises far off and grows. Something is coming at last — too far yet to make out, but dust out here means wheels, and wheels, right now, mean hope. You keep your eyes on it, and wait.",
    "From the bus, you keep your eyes fixed on the road, where far off a plume of dust has risen and is slowly, steadily growing. Something is coming at last — too far away yet to make out what — but dust, out here, means wheels, and wheels, right now, at the end of a day like this one, mean hope. So you keep your eyes on it, and you wait, and you let yourself hope."),
  [t("To Sami.", "To Sami.", "To Sami."),
   t("Hold through the worst.", "Hold through the worst.", "Hold through the worst.")])


# ============================ CLOSING HUBS =================================

P(110,
  t("The cool of evening comes at last. Now the day adds up to what it is. Whatever you did out here, in the heat, comes home now. Some of it you can be proud of. Some of it you cannot. This is where it all comes clear.",
    "The cool of evening comes at last, and the day adds up to what it is. Whatever you did out here in the heat comes home now — some of it to be proud of, some of it not. This is where it all comes clear.",
    "The cool of evening comes at last, and now the whole long day adds up, quietly, to exactly what it was. Whatever you did out here in the heat — every choice, every drop shared or kept — comes home now to be counted. Some of it you can be proud of. Some of it, if you're honest, you can't. This is the hour where all of it comes clear."),
  [t("Sami safe; you kept the water.", "Sami is safe; you kept the water going.", "Sami is safe; you kept the water going."),
   t("You found the smoke, saved Faro.", "You found the smoke, and saved Faro.", "You found the smoke, and saved Faro."),
   t("Weigh the rest.", "Weigh the rest.", "Weigh the rest.")])

P(111,
  t("The afternoon adds up. Not with one big act, maybe. But with many small ones. What you shared. What you refused. Who you stopped for. It all counts, in the end. It all made the day what it was. So, what did the day come to?",
    "The afternoon adds up — not always with one big act, but with many small ones: what you shared, what you refused, who you stopped for. It all counts in the end; it all made the day what it was. So what did the day come to?",
    "The afternoon adds up, and not always in the way you'd expect. Not with one grand act, usually, but with a great many small ones: what you chose to share, what you had the sense to refuse, who you stopped for when stopping cost you. All of it counts, in the end. All of it, together, made the day exactly what it was. So: what did it come to?"),
  [t("The whole bus, together.", "The whole bus came through together.", "The whole bus came through together."),
   t("Clean — no con.", "You did it clean — no con.", "You did it clean — no con."),
   t("Weigh the rest.", "Weigh the rest.", "Weigh the rest.")])

P(112,
  t("There is more to weigh. The day held other things too. A stranger you helped. Water you gave away with an open hand. Small choices, made in the heat, when it would have been easy to look away. Those choices have their own weight. What did they come to?",
    "There's more to weigh; the day held other things too. A stranger you helped. Water you gave away with an open hand. Small choices made in the heat, when looking away would have been easy. Those have their own weight. What did they come to?",
    "There is still more to weigh, because the day held other things as well. A stranger you stopped for. Water you gave away with an open hand, when nobody would have known if you hadn't. Small, hard choices made in the full heat, when looking the other way would have been the easiest thing in the world. Those choices carry their own quiet weight. What, in the end, did they come to?"),
  [t("A stranger carries you on.", "A stranger you helped carries you on.", "A stranger you helped carries you on."),
   t("You gave your water away.", "You gave your own water away.", "You gave your own water away."),
   t("Weigh the rest.", "Weigh the rest.", "Weigh the rest.")])

P(113,
  t("And what does the day leave you with? Maybe not a clean win. Maybe just the fact that you got up. That you tried. That when it was hard, and hot, and easy to sit still, you did not. That counts for something. It always did.",
    "And what does the day leave you with? Maybe not a clean win. Maybe just the fact that you got up, that you tried — that when it was hard and hot and easy to sit still, you didn't. That counts for something. It always did.",
    "And what, when all is counted, does the day leave you with? Maybe not a clean win, no. Maybe just the plain fact that you got up out of your seat, that you tried — that when it was hard and hot and so very easy to simply sit still and wait, you didn't. That counts for something, whatever else it does or doesn't. It always did count for something."),
  [t("A truck comes, late.", "A truck comes at last, late.", "A truck comes at last, late."),
   t("The bus saw you act.", "The bus saw you get up and act.", "The bus saw you get up and act."),
   t("The worst of it.", "The worst of it.", "The worst of it.")])

P(114,
  t("But not every day ends well. Some choices cost more than you knew. Some roads, once taken, cannot be walked back. This is the hard end of the day, where the worst comes home. It is not easy to look at. But it is true. So look.",
    "But not every day ends well. Some choices cost more than you knew; some roads, once taken, can't be walked back. This is the hard end of the day, where the worst comes home. It isn't easy to look at — but it's true. So look.",
    "But not every day ends well, and it would be a lie to pretend otherwise. Some choices cost more than you could have known at the time; some roads, once taken, simply cannot be walked back up. This is the hard end of the day, then, the place where the worst of it comes home to be counted. It is not easy to look at directly. But it is true, all the same. So you look."),
  [t("You paid — fleeced.", "You paid the pickup man — fleeced.", "You paid the pickup man — fleeced."),
   t("You were too late.", "You were simply too late.", "You were simply too late."),
   t("A truck came in time.", "A truck came before real harm.", "A truck came before real harm.")])


# ============================ ENDINGS (12: 4 good / 4 neutral / 4 bad) =====

P(120,
  t("You kept the water going, all through the worst of the heat. Steady sips. Shade held high. Every drop shared and counted. Then the sun drops, and a truck finds you on the road. Sami reaches the city safe, and well. The child is alive because you got up out of your seat. That is the whole of it.",
    "You kept the water going all through the worst of the heat — steady sips, shade held high, every drop shared and counted. Then the sun drops, and a truck finds you on the road. Sami reaches the city safe and well. The child is alive because you got up out of your seat. That's the whole of it.",
    "You kept the water going all through the very worst of the heat: steady sips, the shade held high, every last drop shared out and counted like it mattered, because it did. Then the sun drops at last, and a truck finds you on the road, and Sami reaches the city safe, and well, and blinking in the cool. The child is alive for one reason and one only — because you got up out of your seat. That is the whole of it, and it is enough."),
  [])

P(121,
  t("You crossed to the smoke no one could explain. And you found old Mr Faro, down and failing in the heat, alone. You got him cool in time. His deep well gave water to the whole bus. His old radio raised help at last. And there was one more gift: Rose, from the bus, knew his face. Two old friends, found again, after all these years.",
    "You crossed to the smoke no one could explain, and found old Mr Faro down and failing in the heat, alone. You got him cool in time. His deep well watered the whole bus; his old radio raised help at last. And there was one gift more: Rose, from the bus, knew his face — two old friends, found again after all these years.",
    "You crossed to the smoke that no one could explain, the light that shouldn't have been there. And you found old Mr Faro, down and failing in the heat, with no one in the world to know. You got him cool in time. His deep well, which had never once run dry, gave water to the whole bus; his old radio, coaxed back to life, raised help at last. And there was one gift more, unlooked for: Rose, from the bus, knew his face across all the years. Two old friends, found again, at the end of a hard day. The mystery paid off in a life, and then in another kind of one."),
  [])

P(122,
  t("There was no one big, brave act. There was something better. You turned a busload of scared strangers into people who helped each other. Water shared. Shade held. The weak watched over by the strong. And so, together, the whole bus came through the day. No one was left alone in it. That is what a busful of people can be.",
    "There was no single brave act — there was something better. You turned a busload of frightened strangers into people who helped one another: water shared, shade held, the weak watched over by the strong. And so, together, the whole bus came through the day. No one was left alone in it. That's what a busful of people can be.",
    "There was no single, shining act of bravery here, no one heroic moment — and there was something better than that. You turned a busload of frightened strangers into people who looked after one another: water shared out fairly, shade held up against the sun, the weakest among them watched over by the strongest. And so, together, in the end, the whole bus came through the day intact. No one was left alone in it. That, it turns out, is what a busful of ordinary people can be, when just one of them stands up first."),
  [])

P(123,
  t("You refused the con. You saw the trick for what it was, and you turned your back on it. You kept your head. You kept your money. And you found water by decent means, the hard, honest way. It was not a perfect day. You did not save everyone. But you did it clean. And clean, in the end, is enough.",
    "You refused the con — saw the trick for what it was and turned your back on it. You kept your head, kept your money, and found water by decent means, the hard honest way. It wasn't a perfect day; you didn't save everyone. But you did it clean, and clean, in the end, is enough.",
    "You refused the con. You saw the man's trick for exactly what it was — cruelty dressed up as help — and you turned your back on it and walked. You kept your head, and you kept your money, and you found water by decent means, the hard and honest way, the way that lets you sleep. It was not a perfect day; you didn't save everyone, and you know it. But you did it clean, start to finish. And clean, at the end of a day like this, is more than enough to carry home."),
  [])

P(124,
  t("You did not manage the whole day. But you stopped, once, for a stranger in trouble. You gave them your time when time was short. And now, in the cool of evening, that same stranger comes back with a vehicle. They take you and Sami on toward town. A kindness, it turns out, does not stay where you leave it. It comes back around.",
    "You didn't manage the whole day — but you stopped, once, for a stranger in trouble, and gave them your time when time was short. Now, in the cool of evening, that same stranger comes back with a vehicle and takes you and Sami on toward town. A kindness, it turns out, doesn't stay where you leave it. It comes back around.",
    "You didn't manage the whole of the day, not everything you'd hoped. But you stopped, once, for a stranger in trouble, and gave them your time and your care when both were in desperately short supply. And now, in the cool of the evening, that same stranger comes back, with a vehicle and a place in it for two. They take you and Sami on toward town through the failing light. A kindness, it seems, never really stays where you set it down. Given away freely, it has a way of coming back around."),
  [])

P(125,
  t("You gave your own water away. To a crying child. To a family with nothing. And now, in the cool of evening, you are parched yourself, and worn thin. But you are not alone. The people you helped are near you. Something on that bus has changed, quietly. It is not a full win. But it is a start. And starts matter.",
    "You gave your own water away — to a crying child, to a family with nothing. And now, in the cool of evening, you're parched and worn thin yourself. But you aren't alone: the people you helped are near you. Something on that bus has quietly changed. It's not a full win. But it's a start, and starts matter.",
    "You gave your own water away, again and again — to a crying child, to a family that had nothing left. And now, in the cool of the evening, you are parched yourself, and worn thin as paper. But you are not alone in it, and that turns out to matter more than you'd have guessed: the people you helped are close around you now. Something on that bus has shifted, quietly, over the course of the day. It is not a full win, and you won't pretend it is. But it is a start. And starts, you've come to believe, matter as much as anything."),
  [])

P(126,
  t("You scraped through the worst of it. Just. There was no clean win, and no clever plan. There was only holding on, hour by hour, until the heat broke. Then a truck came at last, late and slow and grudging. It is not a triumph. No one will sing about it. But you are through. And, in the end, that is a kind of relief all its own.",
    "You scraped through the worst of it — just. No clean win, no clever plan; only holding on, hour by hour, until the heat broke and a truck came at last, late and grudging. It's no triumph, and no one will sing about it. But you're through — and in the end, that is a relief all its own.",
    "You scraped through the worst of it, in the end — just barely. There was no clean win to be had, and no clever plan that saved the day. There was only holding on, hour by grinding hour, until the heat finally broke and a truck came at last, late and slow and grudging down the road. It is no triumph, and no one will ever sing about it. But you are through it, all of you, and still here. And that, at the end of a day like this, turns out to be a kind of relief entirely its own."),
  [])

P(127,
  t("You did not manage everything. Far from it. But the whole bus saw you do one thing. When it was hard, and hot, and easy to sit still, you got up. You acted. Others stayed in their seats. You did not. And people remember that. From today, you are someone this road knows. That is not nothing.",
    "You didn't manage everything — far from it. But the whole bus saw you do one thing: when it was hard and hot and easy to sit still, you got up and acted. Others stayed in their seats; you didn't. And people remember that. From today, you're someone this road knows. That's not nothing.",
    "You didn't manage everything — not by a long way, and you know it. But the whole bus saw you do the one thing that counted most. When it was hard, and hot, and so very easy to stay in your seat and let it be someone else's problem, you got up. You acted. The others stayed put; you didn't. And people remember that kind of thing far longer than they remember who won. From today, whatever else is true, you are someone this road knows by name. And that, in the end, is not nothing at all."),
  [])

P(128,
  t("You paid the pickup man. You handed over your cash, in the heat, when you were scared. And what did you get? Water hot as bathwater, half of it already gone. A lift to town that never once came. The money is gone for good. And the thirst is exactly, cruelly, where it was before. He knew you would pay. That was the whole game.",
    "You paid the pickup man — handed over your cash, in the heat, when you were scared. And what did you get? Water hot as bathwater, half of it gone; a lift that never came. The money's gone for good, and the thirst is exactly where it was. He knew you'd pay. That was the whole game.",
    "You paid the pickup man in the end — handed over your cash, out there in the heat, at the exact moment you were most scared and least able to think. And what did it buy you? Water hot as bathwater, half of it already gone; a lift to town that was never, not for one second, actually coming. The money is gone now, and gone for good. And the thirst is exactly, cruelly, where it was before you started. He knew you would pay, because frightened people do. That was the whole of his game, and you played it."),
  [])

P(129,
  t("The open flats were a trap, just as Rose warned. The ridge never came closer. The road behind you faded to nothing. And the heat, out there with no shade, nearly took you for good. You got back — somehow, barely — but far too late. The flats took the whole afternoon. And the afternoon was all you had.",
    "The open flats were a trap, exactly as Rose warned. The ridge never came closer; the road behind you faded to nothing; and the heat, out there with no shade, nearly took you for good. You got back — barely — but far too late. The flats took the whole afternoon, and the afternoon was all you had.",
    "The open flats were a trap, exactly as Rose warned you they would be. The ridge never once came closer, however long you walked. The road behind you smeared and faded into the shimmer until it was gone. And the heat, out there with no scrap of shade to break for, nearly took you for good. You got back — somehow, barely, on your hands and knees at the end — but far, far too late to do any good. The flats took the whole of the afternoon from you. And the afternoon, it turned out, was all you ever had."),
  [])

P(130,
  t("You spent the day on the wrong things. A bad deal here. A wrong turn there. Time lost that you could not get back. And when at last you knelt by Sami, the heat had been in the child too long. By evening they carry the child to a truck, limp and grey. You got up. You went out. But you did not get there in time.",
    "You spent the day on the wrong things — a bad deal here, a wrong turn there, time lost that you couldn't get back. And when at last you knelt by Sami, the heat had been in the child too long. By evening they carry the child to a truck, limp and grey. You got up, you went out — but you didn't get there in time.",
    "You spent the day, in the end, on the wrong things: a bad deal here, a wrong turn there, hour after hour lost that you could never get back. And when at last you knelt down by Sami in the last of the light, the heat had already been in the child far too long. By evening they are carrying the child to a truck, limp and grey and terribly quiet. You got up. You went out into it. That mattered, and it was real. But you did not get there in time, and that, in the end, matters more."),
  [])

P(131,
  t("In the end, you stayed in your seat. You kept your own bottle capped. You told yourself it was not your job. That help would come at evening. That someone else would surely act. And all of that was true. And a small child, three seats away, went quiet in the heat. Nothing bad happened to you. You will think about that for a long, long time.",
    "In the end, you stayed in your seat and kept your own bottle capped. You told yourself it wasn't your job, that help would come at evening, that someone else would surely act. All of that was true. And a small child, three seats away, went quiet in the heat. Nothing bad happened to you. You'll think about that for a long, long time.",
    "In the end, you stayed in your seat, and you kept your own bottle capped and cool beside you. You told yourself it wasn't really your job; that help would come at evening; that someone else, surely, would get up and act. And all of that was perfectly, comfortably true. And a small child, three seats away from you, went quiet in the heat while you sat there. Nothing bad happened to you at all. You came through the day untouched. You will think about that, quietly, for a long, long time."),
  [])


# ============================ apply ========================================
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
