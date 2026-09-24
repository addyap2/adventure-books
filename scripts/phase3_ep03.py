#!/usr/bin/env python3
"""Phase 3: pour leveled prose into the First Light skeleton.

Holds A2/B1/B2 prose for each node (and each choice, in skeleton order) in PROSE, then
writes it onto content/episode-03.json in place. Nodes absent from PROSE keep their stub, so
this grows batch by batch; re-run after each and validate to keep every level in band.

Run: python3 scripts/phase3_ep03.py
"""
import json, os, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BOOK = os.path.join(ROOT, "content", "episode-03.json")


def t(a2, b1, b2): return {"A2": a2, "B1": b1, "B2": b2}
PROSE = {}
def P(nid, text, choices): PROSE[nid] = {"text": text, "choices": choices}


# ============================ ACT I — THE LIGHTS GO OUT ====================

P(1,
  t("It is the coldest night of the winter. Just after dark, every light in the town goes out at once. The heating stops. The house begins to go cold. Then you think of Mrs Ada, up the hill. She was kind to you when you were small. She is old now, with a weak chest. And her heater needs electricity.",
    "It's the coldest night of the winter, and just after dark every light in the town goes out at once. The heating dies with a click, and the house begins to cool. Then you think of Mrs Ada, up the hill. She was kind to you when you were small. She's old now, with a weak chest — and her only heater runs on electricity.",
    "It is the coldest night of the whole winter, and just after dark every light in the town goes out at once, as if someone had pulled a single plug. The heating dies with a click, and the house begins, almost at once, to cool. Then you think of Mrs Ada, up the hill. She was kind to you when you were small, in a hundred quiet ways. She is old now, with a weak chest — and the only heater she has runs on electricity."),
  [t("Find a candle and your coat.", "Light a candle and find your coat.", "Light a candle and find your coat."),
   t("Try the phone for news.", "Try the phone for news.", "Try the phone for news."),
   t("Run straight out to Ada.", "Rush straight out to Ada.", "Rush straight out to Ada.")])

P(2,
  t("You find a candle and light it with shaking hands. You find a torch, your thick coat, your boots. The little flame makes the room gold and small. Outside the window, the whole street is black. The cold is already coming in under the doors. You must decide what to do, and do it soon.",
    "You find a candle and light it with hands that won't quite keep still. Then a torch, your thick coat, your boots. The little flame makes the room small and gold. Outside the window the whole street is black, and the cold is already creeping in under the doors. You have to decide what to do, and soon.",
    "You find a candle and light it with hands that won't quite keep still, then dig out a torch, your thickest coat, your boots. The little flame shrinks the room to something small and gold. Outside the window the whole street has gone black, and the cold is already creeping in under the doors like water. You have to decide what to do, and you have to decide it soon."),
  [t("Go out into the street.", "Step out into the street.", "Step out into the street."),
   t("Decide how to start.", "Decide how to start.", "Decide how to start."),
   t("The torch is dead.", "The torch batteries are dead.", "The torch batteries are dead.")])

P(3,
  t("You try the phone. The signal comes and goes. At last a message gets through from the town hall. The roads are blocked by snow. No help can come until first light. Everyone must stay in and keep warm. But Mrs Ada cannot keep warm. Not with no heat, not on a night like this.",
    "You try the phone. The signal comes and goes, but at last a message gets through from the town hall. The roads are blocked with snow; no help can come until first light. Everyone is to stay in and keep warm. But Mrs Ada can't keep warm — not with no heat, not on a night like this.",
    "You try the phone. The signal flickers in and out, but at last a message gets through from the town hall. The roads are blocked with snow, and no help can reach the town until first light. Everyone is asked to stay indoors and keep warm. But Mrs Ada can't keep warm — not with no heat at all, and not on a night as bitter as this one."),
  [t("Decide how to start.", "Decide how to start.", "Decide how to start."),
   t("But Ada can't wait.", "But Ada can't wait that long.", "But Ada can't wait that long.")])

P(4,
  t("You run straight out, with nothing in your hands. The cold hits you like a wall. It takes your breath away. Your fingers hurt at once. You stop in the dark street and understand. You cannot help Ada with empty hands. You need warm things. You need to think first.",
    "You rush straight out with nothing in your hands, and the cold hits you like a wall. It snatches your breath; your fingers ache at once. You stop in the black street and understand: you can't help Ada with empty hands. You need warm things, and you need to think before you run.",
    "You rush straight out with nothing in your hands, and the cold hits you like a wall, snatching the breath from your lungs. Your fingers ache almost at once. You stop in the black, silent street and understand, all at once, that you can't help Ada with empty hands. You need warm things. And, before you run anywhere, you need to think."),
  [t("Go back for supplies.", "Go back for supplies.", "Go back for supplies."),
   t("Feel how serious this is.", "Feel how serious this is.", "Feel how serious this is.")])

P(5,
  t("You step out. The street is dark and still. Snow covers everything. The houses are black shapes, but in one window a candle burns. Your breath is white in the air. It is very, very cold. Somewhere, a dog barks. The corner shop, you see, still has a small light inside.",
    "You step outside. The street is dark and utterly still, snow over everything, the houses just black shapes against the sky. In one window a single candle burns. Your breath hangs white in the air; the cold is fierce. Somewhere a dog barks. And the corner shop, you notice, still shows a small light inside.",
    "You step outside into a street gone dark and utterly still, snow lying over everything, the houses reduced to black shapes against a sky with no glow in it. In one window a single candle burns. Your breath hangs white in the air, and the cold is fierce enough to hurt. Somewhere a dog barks. And the corner shop, you notice, still shows a small, stubborn light inside."),
  [t("The corner shop is open.", "The corner shop is still open.", "The corner shop is still open."),
   t("Knock on a neighbour's door.", "Knock on a neighbour's door.", "Knock on a neighbour's door."),
   t("Decide how to start.", "Decide how to start.", "Decide how to start."),
   t("A kid is out searching.", "A kid is out in the dark, searching.", "A kid is out in the dark, searching.")])

P(6,
  t("You stand in the cold and think. You could go to the shop first, for a heater and blankets. You could run straight up the hill to Ada, and hope. Or you could knock on doors and find people to help. Each choice takes time. And tonight, time is cold.",
    "You stand in the cold and make yourself think. You could go to the shop first, for a heater and blankets. You could rush straight up the hill to Ada and hope for the best. Or you could knock on doors and gather people to help. Every choice costs time — and tonight, time is cold.",
    "You stand in the cold and make yourself think clearly. You could go to the shop first, for a heater and blankets. You could rush straight up the hill to Ada and simply hope for the best. Or you could knock on doors and gather people willing to help. Every choice costs time — and tonight, time is measured in how cold it's getting."),
  [t("The shop, for supplies.", "The shop, for supplies.", "The shop, for supplies."),
   t("Run up the hill.", "Rush up the hill.", "Rush up the hill."),
   t("Knock on doors for help.", "Knock on doors to gather help.", "Knock on doors to gather help.")])

P(8,
  t("You feel the cold in your bones. And you think of Ada, alone, in a house with no heat, her chest tight with every breath. A night like this could kill her. That is not a thought. It is a fact. No one else is going up that hill tonight. So it is you.",
    "You feel the cold settle into your bones. You think of Ada, alone in a house with no heat, her chest tightening with every breath. A night like this could kill her. That isn't a fear; it's a fact. No one else is going up that hill tonight. So it has to be you.",
    "You feel the cold settle deep into your bones, and you think of Ada, alone in a house with no heat, her weak chest tightening with every breath she takes. A night as cold as this could kill her. That isn't a fear any more; it's simply a fact. No one else is going up that hill tonight. So, whether you're ready or not, it has to be you."),
  [t("Decide how to start.", "Decide how to start.", "Decide how to start."),
   t("To the shop.", "To the shop.", "To the shop."),
   t("Panic at the shop.", "A rumour of panic at the shop.", "A rumour of panic at the shop.")])

P(9,
  t("Mr Okafor has opened his shop by candlelight. Shelves stand in the gold glow. He has a paraffin heater — real heat, not just light. He has blankets, a hot flask, batteries. \"Take what you need,\" he says. \"Pay me when the lights come back.\" He is a kind man, and tonight it shows.",
    "Mr Okafor has opened his shop by candlelight, the shelves glowing gold. He has a paraffin heater — real heat, not just light — and blankets, a hot flask, spare batteries. \"Take what you need,\" he says. \"Pay me when the lights come back.\" He's always been kind, and tonight it shows.",
    "Mr Okafor has opened his shop by candlelight, the shelves glowing gold in the dark. He has a paraffin heater — real heat, not merely light — along with blankets, a hot flask and spare batteries. \"Take what you need,\" he says. \"Pay me when the lights come back.\" He has always been a kind man, and tonight, in the dark, it shows."),
  [t("Take the paraffin heater.", "Take the paraffin heater.", "Take the paraffin heater."),
   t("Just candles and batteries.", "Just candles and batteries.", "Just candles and batteries."),
   t("Ask his advice.", "Ask Okafor's advice.", "Ask Okafor's advice."),
   t("He gives you his flask.", "He gives you the last flask.", "He gives you the last flask.")])

P(10,
  t("You knock on a neighbour's door. Mrs Pratt opens it, pale in the candlelight. She is old, and alone, and frightened. \"I can't get warm,\" she says. \"And I can't see.\" You have a long way to go tonight. But she is here, and she is scared, and she is asking.",
    "You knock on a neighbour's door, and Mrs Pratt opens it, pale in the candlelight — old, alone, and plainly frightened. \"I can't get warm,\" she says. \"And I can't see a thing.\" You have a long way to go tonight. But she's here, and she's scared, and she's asking you.",
    "You knock on a neighbour's door, and Mrs Pratt opens it, pale and small in the candlelight — old, alone, and plainly frightened. \"I can't get warm,\" she says. \"And I can't see a thing.\" You have a long way to go tonight, and Ada is waiting. But Mrs Pratt is here, and she is scared, and she is asking you."),
  [t("Stop and help her.", "Stop and help her.", "Stop and help her."),
   t("Say you must reach Ada.", "Say you must reach Ada.", "Say you must reach Ada.")])

P(11,
  t("You set off up the hill with what you have. It is steep, and the snow is deep. Your legs burn. The cold gets into your chest, and each breath hurts. You are not sure you can carry anything useful this way. But you keep climbing, because Ada is at the top.",
    "You set off up the hill with what you have. It's steep and the snow is deep, and your legs soon burn. The cold gets into your chest until every breath hurts. You're not sure you're carrying anything useful at all. But you keep climbing, because Ada is at the top.",
    "You set off up the hill with whatever you have. It is steep, and the snow is deep, and your legs are burning before you're halfway. The cold works its way into your chest until every breath is a small ache. You aren't sure you're carrying anything that will help. But you keep on climbing, because Ada is at the top."),
  [t("The way splits: road or river.", "The way splits: road or river.", "The way splits: road or river."),
   t("You're cold and out of breath.", "You're cold and short of breath.", "You're cold and short of breath.")])

P(12,
  t("You go from door to door, knocking. At first, nobody comes. Then a door opens, and another. Tired faces, candles, coats over pyjamas. You tell them about Ada, and about the cold, and about the long night. Some people will help. Some won't. You have to ask anyway.",
    "You go from door to door, knocking. At first nobody comes. Then a door opens, and another — tired faces, candles, coats thrown over pyjamas. You tell them about Ada, and the cold, and the long night ahead. Some will help and some won't. You have to ask anyway.",
    "You go from door to door along the street, knocking. At first nobody comes at all. Then a door opens, and then another — tired faces, guttering candles, coats thrown over pyjamas. You tell them about Ada, and about the cold, and about the long night still ahead. Some of them will help and some of them won't. You have to ask anyway."),
  [t("Neighbours come out to help.", "Neighbours turn out to help.", "Neighbours turn out to help."),
   t("No one answers. Go alone.", "No one answers; go alone.", "No one answers; go alone.")])

P(13,
  t("You take the paraffin heater. It is heavy, and awkward to carry. But it is real heat — the one thing Ada needs most. You thank Mr Okafor, and he nods. \"Mind how you carry it,\" he says. \"And mind the ice.\" With the heater in your arms, you feel you have a chance.",
    "You take the paraffin heater. It's heavy and awkward to carry, but it's real heat — the one thing Ada needs most. You thank Mr Okafor and he nods. \"Mind how you carry it,\" he says. \"And mind the ice.\" With the heater in your arms, you feel, for the first time, that you have a chance.",
    "You take the paraffin heater. It is heavy, and awkward to carry, but it is real heat — the one thing Ada needs above everything else. You thank Mr Okafor, and he nods. \"Mind how you carry it,\" he says. \"And mind the ice.\" With the heater held against your chest, you feel, for the first time tonight, that you might actually have a chance."),
  [t("Now the way to her.", "Now the way to her.", "Now the way to her."),
   t("Thank Mr Okafor.", "Thank Okafor.", "Thank Okafor.")])

P(14,
  t("You take candles and batteries. They will give Ada light, and light helps. But light is not heat. The cold will still come in, and her chest will still be tight. You feel you have chosen something, but maybe not enough. You look back at the heater on the shelf.",
    "You take candles and batteries. They'll give Ada light, and light helps — but light isn't heat. The cold will still creep in, and her chest will still tighten. You've chosen something, but maybe not enough. You glance back at the heater on the shelf.",
    "You take candles and batteries. They will give Ada light, and light, in the dark, helps more than you'd think — but light is not heat. The cold will still creep in, and her chest will still tighten through the night. You've chosen something, certainly, but perhaps not enough. You glance back at the heater on the shelf."),
  [t("Now the way to her.", "Now the way to her.", "Now the way to her."),
   t("Ask his advice.", "Ask Okafor's advice.", "Ask Okafor's advice.")])

P(15,
  t("\"Listen,\" Mr Okafor says. \"Three things.\" He counts on his fingers. \"Stay away from the man with the van. He sells fear. Don't cross the river ice — it looks strong, but it isn't. And take the road, even though it's longer.\" Good advice is rare tonight. You keep it close.",
    "\"Listen,\" Mr Okafor says. \"Three things.\" He counts them off. \"Keep away from the man with the van — he sells fear. Don't cross the river ice; it looks strong, but it isn't. And take the road, even though it's longer.\" Good advice is rare tonight. You hold on to it.",
    "\"Listen,\" Mr Okafor says. \"Three things.\" He counts them off on his fingers. \"Keep away from the man with the van — he sells fear, nothing else. Don't cross the river ice; it looks strong, but it isn't. And take the road, even though it's longer.\" Good advice is a rare thing on a night like this. You hold on to it tightly."),
  [t("Take it to heart.", "Take it to heart.", "Take it to heart."),
   t("On with it.", "On with it.", "On with it.")])

P(16,
  t("You light Mrs Pratt's candles and wrap her in a blanket. You show her how to close the doors to keep the warmth in. Her hands stop shaking. \"You're a good one,\" she says. \"Go on. Someone else needs you more.\" You promise to come back. It costs you minutes. It was worth them.",
    "You light Mrs Pratt's candles, wrap her in a blanket, and show her how to shut the doors to keep what warmth there is. Her hands stop shaking. \"You're a good one,\" she says. \"Go on — someone else needs you more.\" You promise to come back. It cost you minutes, and it was worth them.",
    "You light Mrs Pratt's candles, wrap her in a blanket, and show her how to shut the inner doors to hold what warmth there is. Slowly, her hands stop shaking. \"You're a good one,\" she says. \"Go on now — someone else needs you more than I do.\" You promise to come back later. It cost you precious minutes, and it was worth every one."),
  [t("On toward Ada.", "On toward Ada.", "On toward Ada."),
   t("She asks you to check on others.", "She asks you to check on others.", "She asks you to check on others.")])

P(17,
  t("You tell Mrs Pratt you must reach Ada, and you are sorry. She nods, and closes her door. You feel bad as you walk away. But Ada's need is greater, and the night is getting colder. You go on, faster now, into the dark.",
    "You tell Mrs Pratt you have to reach Ada, and that you're sorry. She nods and closes her door. You feel bad walking away. But Ada's need is greater, and the night is only getting colder. You go on, faster now, into the dark.",
    "You tell Mrs Pratt that you have to reach Ada first, and that you're sorry. She nods, and quietly closes her door. You feel bad walking away from it. But Ada's need is greater, and the night is only getting colder by the minute. You go on, faster now, into the dark."),
  [t("The shop first.", "The shop first.", "The shop first."),
   t("Straight up the hill.", "Straight up the hill.", "Straight up the hill.")])

P(18,
  t("You are near the bottom of the hill, but you are cold and not ready. Your hands are empty and numb. You have no heat to give Ada. Ahead, through the snow, you see bright headlights. A van. A small crowd. Something is being sold.",
    "You're near the foot of the hill, but you're cold and not ready — hands empty and numb, nothing warm to give Ada. Ahead, through the falling snow, you see bright headlights: a van, a small crowd around it. Something is being sold.",
    "You're near the foot of the hill now, but you're cold and utterly unready — hands empty and numb, nothing warm at all to give Ada. Ahead, through the falling snow, you see bright headlights: a van, with a small, restless crowd gathered around it. Something, clearly, is being sold. You slow down, uneasy."),
  [t("The van man's lights are ahead.", "The van man's lights are ahead.", "The van man's lights are ahead."),
   t("Push on.", "Push on.", "Push on.")])

P(19,
  t("The street begins to wake. Doors open. People come out with candles and torches. Someone has a camping stove. Someone has soup. A plan starts to form, all by itself. Suddenly you are not alone in the dark. You are part of something, and it feels warm.",
    "The street begins to wake up. Doors open; people come out with candles and torches. Someone has a camping stove, someone has a pot of soup, and a plan starts to form almost by itself. Suddenly you're not alone in the dark. You're part of something — and it feels warm.",
    "The street begins, slowly, to wake up. Doors open; people come out with candles and torches. Someone has a camping stove, someone else a pot of soup, and a plan starts to form almost by itself. Suddenly you're no longer alone in the dark. You're part of something larger — and, for the first time all night, it feels warm."),
  [t("Lead the way to Ada.", "Lead the way to Ada.", "Lead the way to Ada."),
   t("Share one warm room first.", "Share one warm room first.", "Share one warm room first.")])

P(20,
  t("You knock and knock, but no one answers. Maybe they are asleep. Maybe they are too cold and scared to open. The street stays dark and silent. You feel very alone. But being alone does not change what Ada needs. You will have to go by yourself.",
    "You knock and knock, but no one answers. Maybe they're asleep; maybe they're too cold and scared to open up. The street stays dark and silent, and you feel very alone. But being alone doesn't change what Ada needs. You'll have to go by yourself.",
    "You knock and knock, but no one answers. Perhaps they're asleep; perhaps they're simply too cold and frightened to open their doors. The street stays dark and silent around you, and you feel very alone in it. But being alone doesn't change what Ada needs tonight. You'll just have to go by yourself."),
  [t("The shop.", "The shop.", "The shop."),
   t("Up the hill.", "Up the hill.", "Up the hill.")])

P(22,
  t("You decide to be careful tonight. No shortcuts. No deals in the dark. You will take the long road and trust the people you know. It will be slower. But slower and safe is better than fast and foolish, on the coldest night of the year.",
    "You decide to be careful tonight: no shortcuts, no deals in the dark. You'll take the long road and trust the people you know. It'll be slower. But slower and safe beats fast and foolish, on the coldest night of the year.",
    "You decide to be careful tonight: no shortcuts, and no deals struck in the dark. You'll take the long road and trust the people you actually know. It will be slower, certainly. But slower and safe beats fast and foolish, on the coldest night of the year. Ada needs you to arrive, not to arrive quickly."),
  [t("On the way.", "On the way.", "On the way."),
   t("Back to the shop.", "Back to the shop.", "Back to the shop.")])

P(23,
  t("You walk on, a little warmer inside for the good turn. It is funny: the night is just as cold, but you feel stronger. Helping someone does that. Now, though, you must think of Ada again. The hill is still ahead of you, and it is still dark.",
    "You walk on, a little warmer inside for the good turn. It's strange: the night is every bit as cold, but you feel stronger. Helping someone does that. Now, though, you have to think of Ada again. The hill is still ahead, and it's still dark.",
    "You walk on, a little warmer inside for the good turn you've done. It's strange: the night is every bit as cold as before, and yet you feel stronger. Helping someone seems to do that. Now, though, your thoughts have to turn back to Ada. The hill still lies ahead of you, and it is still very dark."),
  [t("On with the night.", "On with the night.", "On with the night."),
   t("Gather more help.", "Gather more help.", "Gather more help.")])

P(24,
  t("The van is parked in the snow, its lights blazing. A man stands by it, calling out. A crowd of cold, scared people is pushing close. On the van are heaters, generators, cans of fuel. \"Tonight only!\" the man shouts. \"Cash only!\" Everyone here is frightened. He seems to know it.",
    "The van is parked in the snow, headlights blazing, a man beside it calling out. A crowd of cold, scared people pushes close. On the van are heaters, generators, cans of fuel. \"Tonight only!\" he shouts. \"Cash only!\" Everyone here is frightened, and he seems to know it.",
    "The van is parked in the snow with its headlights blazing, and a man stands beside it calling out. A crowd of cold, frightened people pushes close around him. On the van are heaters, generators, cans of fuel. \"Tonight only!\" he shouts. \"Cash only!\" Everyone here is afraid — and he seems to understand that perfectly."),
  [t("Hear what he's selling.", "Hear what he's selling.", "Hear what he's selling."),
   t("Go round him.", "Go round him.", "Go round him.")])

P(25,
  t("You lead a small group up toward the hill. Candles bob in the dark behind you. Someone carries the stove, someone the soup. You feel like the front of something good. Then you see it: a warm light, high on the hill, in the old Harrow house. But that house has been empty for years.",
    "You lead a small group up toward the hill, candles bobbing in the dark behind you — someone carrying the stove, someone the soup. You feel like the front of something good. Then you see it: a warm light high on the hill, in the old Harrow house. But that house has stood empty for years.",
    "You lead a small group up toward the hill, candles bobbing in the dark behind you — someone carrying the stove, someone else the soup. You feel, for once, like the front of something good. Then you see it: a warm light high on the hill, in the old Harrow house. But that house, everyone knows, has stood empty for years."),
  [t("The way.", "The way.", "The way."),
   t("The strange light on the hill.", "The strange light on the hill.", "The strange light on the hill.")])

P(29,
  t("You click the torch. Nothing. The batteries are dead. You have only the one candle now, and a candle blows out in the wind. You will need more light before you go far. The corner shop may still have batteries. Or you can manage, carefully, with what you have.",
    "You click the torch — nothing. The batteries are dead. You have only the one candle now, and a candle won't survive the wind outside. You'll need more light before you go far. The corner shop might still have batteries, or you could manage, carefully, with what you've got.",
    "You click the torch, and nothing happens: the batteries are dead. You have only the one candle now, and a candle won't last a minute in the wind outside. You'll need more light before you go very far. The corner shop might still have batteries — or you could try to manage, carefully, with what you've got."),
  [t("Out into the street.", "Out into the street.", "Out into the street."),
   t("To the shop for more.", "To the shop for more.", "To the shop for more.")])

P(36,
  t("The neighbours bring everything into one house with a stove. One warm room, full of candles and soup and people. Children sleep on coats. Old people sit close to the heat. It is crowded and noisy and warm. For the first time tonight, the cold feels far away.",
    "The neighbours bring everything into one house with a stove: one warm room, full of candles and soup and people. Children sleep on piled coats; the old sit closest to the heat. It's crowded, noisy and warm. For the first time tonight, the cold feels far away.",
    "The neighbours bring everything into the one house that has a stove: one warm room, crammed with candles and soup and people. Children sleep on piled coats; the elderly sit closest to the heat. It is crowded, and noisy, and wonderfully warm. For the first time all night, the cold feels a long way off."),
  [t("Bring Ada down to it.", "Get Ada down to it.", "Get Ada down to it."),
   t("Fetch more neighbours.", "Fetch more neighbours.", "Fetch more neighbours.")])

P(37,
  t("You go back out and knock on more doors. One by one, more candles appear in more windows. The dark street slowly becomes a lit one. People are helping people now, without being asked. You started this. Now it is bigger than you.",
    "You go back out and knock on more doors. One by one, candles appear in more windows, and the dark street slowly becomes a lit one. People are helping people now, without being asked. You started this — and now it's bigger than you.",
    "You go back out into the cold and knock on still more doors. One by one, candles appear in more and more windows, and the dark street slowly becomes a lit one. People are helping people now, without needing to be asked. You started this — and now it has grown far bigger than you."),
  [t("To the hill.", "To the hill.", "To the hill."),
   t("The last stretch.", "The last stretch.", "The last stretch.")])

P(60,
  t("A small figure runs past in the dark — a kid, Bex, from down the road. \"Have you seen my brother?\" Bex asks, crying. \"He went out to find the cat. He isn't back.\" A little child, lost in the snow, on a night like this. You look up at the hill. Then back at Bex.",
    "A small figure runs past in the dark: a kid, Bex, from down the road. \"Have you seen my brother?\" Bex asks, crying. \"He went out after the cat, and he isn't back.\" A little child, lost in the snow on a night like this. You look up at the hill, then back at Bex.",
    "A small figure comes running past in the dark: a kid, Bex, from further down the road. \"Have you seen my brother?\" Bex asks, crying hard. \"He went out after the cat, and he isn't back.\" A little child, lost somewhere in the snow on a night like this. You look up at the hill, and then back down at Bex."),
  [t("Help Bex look.", "Help Bex look.", "Help Bex look."),
   t("No time. Ada first.", "No time — Ada first.", "No time — Ada first.")])

P(61,
  t("You and Bex search the dark gardens, calling his name. At last you hear a small sound from a shed. Inside, cold and frightened, is Bex's little brother, holding the cat. You wrap him in your scarf. He is safe. Bex holds him and won't let go.",
    "You and Bex search the dark gardens, calling his name. At last you hear a small sound from a shed. Inside, cold and frightened, is Bex's little brother, clutching the cat. You wrap him in your scarf. He's safe, and Bex holds him and won't let go.",
    "You and Bex search the dark gardens, calling his name into the wind. At last you hear a small sound from a garden shed. Inside, cold and frightened, is Bex's little brother, clutching the cat to his chest. You wrap him in your scarf. He's safe — and Bex holds on to him and won't let go."),
  [t("Get them home.", "Get them home.", "Get them home."),
   t("On to Ada.", "On to Ada.", "On to Ada.")])

P(62,
  t("You tell Bex to run home and tell a grown-up. It is the fastest help you can give, and Ada is waiting. Bex runs off into the dark. You hope the brother is found. You go on, but the worry comes with you, a small weight in the cold.",
    "You tell Bex to run home and fetch a grown-up — it's the fastest help you can give, and Ada is waiting. Bex runs off into the dark. You hope the brother is found soon. You go on, but the worry comes with you, a small weight in the cold.",
    "You tell Bex to run home and fetch a grown-up — it's the quickest help you can give, and Ada is still waiting. Bex runs off into the dark. You hope, hard, that the little brother is found soon. You go on, but the worry comes along with you, a small cold weight in your chest."),
  [t("Decide how to start.", "Decide how to start.", "Decide how to start."),
   t("On toward the hill.", "On toward the hill.", "On toward the hill.")])

P(63,
  t("You walk the two children home. Their mother opens the door and cries with relief. She pulls you inside, just for a moment, and gives you a hot drink by a candle. \"Thank you,\" she says, again and again. Warmth for warmth. Then you must go on.",
    "You walk the two children home. Their mother opens the door and cries with relief. She pulls you inside for a moment and presses a hot drink into your hands by candlelight. \"Thank you,\" she keeps saying. Warmth for warmth. Then you have to go on.",
    "You walk the two children home through the snow. Their mother opens the door and cries with relief, then pulls you inside for a moment and presses a hot drink into your frozen hands by candlelight. \"Thank you,\" she keeps saying, over and over. Warmth given, warmth returned. Then you have to go on."),
  [t("On toward the hill.", "On toward the hill.", "On toward the hill."),
   t("The last stretch.", "The last stretch.", "The last stretch.")])

P(67,
  t("Mr Okafor puts his own flask of hot tea into your hands. \"The last one,\" he says. \"For Ada.\" Then he begins to close up, blowing out his candles one by one. He is going home to his own cold house. You feel the warm flask through your gloves. It is a small, good gift.",
    "Mr Okafor presses his own flask of hot tea into your hands. \"The last one,\" he says. \"For Ada.\" Then he starts to close up, blowing out his candles one by one, heading home to his own cold house. You feel the warm flask through your gloves — a small, good gift.",
    "Mr Okafor presses his own flask of hot tea into your hands. \"The last one,\" he says quietly. \"For Ada.\" Then he begins to close up, blowing out his candles one by one, heading home to a cold house of his own. You feel the warmth of the flask right through your gloves — a small gift, and a good one."),
  [t("On the way.", "On the way.", "On the way."),
   t("His advice first.", "His advice first.", "His advice first.")])

P(68,
  t("At the shop, a rumour runs through the queue. \"There's no more heaters!\" someone shouts. \"It's every man for himself!\" People start to push. Fear spreads faster than cold. You could step in and calm them. Or you could just push into the shop and get what you can.",
    "At the shop, a rumour ripples down the queue. \"There's no more heaters!\" someone shouts. \"It's every man for himself!\" People start to push. Fear spreads faster than the cold. You could step in and calm them, or just push into the shop and grab what you can.",
    "At the shop, a rumour ripples down the waiting queue. \"There's no more heaters!\" someone shouts. \"It's every man for himself!\" People begin to push and shove. Fear, you realise, spreads faster than the cold ever could. You could step in and calm them down — or you could simply push into the shop and grab whatever you can."),
  [t("Calm them and rally them.", "Calm it, and rally them.", "Calm it, and rally them."),
   t("Go into the shop.", "Into the shop.", "Into the shop.")])


# ============================ ACT II — INTO THE DARK TOWN ==================

P(21,
  t("Now the way to Ada. Two ways lead up the hill. The road is long, but it is solid under the snow. The river is frozen, and crossing the ice would be much shorter. But ice can lie. Down by the river you also see the van man's lights, and a crowd around them.",
    "Now for the way to Ada. Two ways lead up the hill: the long road, solid under the snow, or the frozen river, which would cut the journey in half. But ice can lie. Down by the water you also see the van man's headlights, and a crowd gathered round them.",
    "Now for the way up to Ada. Two ways climb the hill: the long road, solid enough under the snow, or the frozen river, which would cut the journey clean in half. But ice can lie, and lie well. Down by the water you can also see the van man's headlights, and a restless crowd gathered around them."),
  [t("Take the road.", "Take the road.", "Take the road."),
   t("Cross the river ice.", "Cross the river ice.", "Cross the river ice."),
   t("The van man's lights.", "The van man's lights ahead.", "The van man's lights ahead.")])

P(26,
  t("You take the road. It is long, and it winds up the hill in the dark. But the ground is solid under the snow, and that matters tonight. Your feet crunch. Your breath smokes. The town is silent all around you, holding its cold breath, waiting for the light.",
    "You take the road. It's long, winding up the hill in the dark, but the ground is solid under the snow, and tonight that matters more than speed. Your feet crunch; your breath smokes. The whole town is silent around you, holding its cold breath, waiting for the light to return.",
    "You take the road. It's long, and it winds up the hill in the dark, but the ground is solid under the snow, and tonight that matters far more than speed. Your feet crunch; your breath smokes in the torchlight. The whole town lies silent around you, holding its cold breath, waiting for the light to return at dawn."),
  [t("Press on.", "Press on.", "Press on."),
   t("Someone is stuck ahead.", "Someone's stuck ahead.", "Someone's stuck ahead."),
   t("The town, dark and still.", "The whole town, dark and quiet.", "The whole town, dark and quiet.")])

P(27,
  t("The frozen river runs at the foot of the hill. Cross it, and you save a lot of time. The ice looks thick and white. But Mr Okafor warned you: it looks strong, but it isn't. Under the ice is black, cold water. Time, or safety. You cannot have both.",
    "The frozen river lies at the foot of the hill. Cross it, and you'd save a great deal of time. The ice looks thick and white and solid. But Okafor warned you: it looks strong, and it isn't. Under it runs black, freezing water. Time or safety — you can't have both tonight.",
    "The frozen river lies at the foot of the hill. Cross it, and you'd save a great deal of precious time. The ice looks thick, and white, and solid enough to trust. But Okafor warned you plainly: it looks strong, and it isn't. Under it runs black, freezing water. Time, or safety — you can't have both of them tonight."),
  [t("Risk the ice.", "Risk the ice.", "Risk the ice."),
   t("Too dangerous. The road.", "Too dangerous — back to the road.", "Too dangerous — back to the road.")])

P(28,
  t("You step out onto the ice. It holds. You take another step, and another. The black water waits below you. Every step is a small bet with your life. The far bank is not far now. But the ice makes small sounds under your boots, and you do not like them.",
    "You step out onto the ice, and it holds. Another step, and another. The black water waits somewhere below you. Every step is a small bet with your own life. The far bank isn't far now — but the ice makes small sounds under your boots, and you don't like them at all.",
    "You step out onto the ice, and it holds your weight. Another step, and another. The black water waits somewhere below you, patient. Every single step is a small bet made with your own life. The far bank isn't far now — but the ice keeps making small sounds under your boots, and you don't like a single one of them."),
  [t("Edge across.", "Edge across.", "Edge across."),
   t("The ice groans.", "The ice groans.", "The ice groans.")])

P(30,
  t("You climb the road in the deep dark. The cold gets harder every hour. Your face hurts with it. Ahead, at a black window, a family stands shivering, wrapped in every coat they own. And still the hill goes up, and up, toward Ada.",
    "You climb the road through the deep dark, and the cold grows harder every hour, until your face aches with it. Ahead, at a black window, a family stands shivering, wrapped in every coat they own. And still the hill climbs on, up and up, toward Ada.",
    "You climb the road through the deep dark, and the cold grows harder with every hour that passes, until your face aches with it. Ahead, at a black window, a whole family stands shivering, wrapped in every coat they own. And still the hill climbs on, up and up and up, toward Ada at the top."),
  [t("A shivering family.", "A family shivering at a dark window.", "A family shivering at a dark window."),
   t("Press on.", "Press on.", "Press on."),
   t("You can see your breath.", "You can see your breath.", "You can see your breath."),
   t("A buried signpost.", "A signpost, half-buried in snow.", "A signpost, half-buried in snow.")])

P(31,
  t("A car sits stuck in the snow, its wheels spinning. An old man is at the wheel, alone, his face grey. He cannot go forward or back. If you stop to push, you lose time you may not have. If you don't, he may sit here in the cold all night.",
    "A car sits stuck in the snow, wheels spinning uselessly. An old man is at the wheel, alone, his face grey with cold. He can't go forward or back. Stop to push, and you lose time you may not have; leave him, and he could sit out here in the cold all night.",
    "A car sits stuck fast in the snow, its wheels spinning uselessly. An old man is at the wheel, alone, his face grey with the cold. He can't go forward and he can't go back. Stop to push, and you lose time you may not have to spare; leave him, and he could sit out here in the freezing dark all night long."),
  [t("Help push it clear.", "Help push it clear.", "Help push it clear."),
   t("You can't stop. Ada.", "You can't stop — Ada.", "You can't stop — Ada.")])

P(32,
  t("Inside a cold, dark house, a family sits close together. A baby cries and cries. There is no heat here, and no light but one candle. The mother looks at you with wide, tired eyes. You have a blanket for Ada. You have only the one.",
    "Inside a cold, dark house, a family sits huddled together. A baby cries and cries. There's no heat here, and no light but a single candle. The mother looks at you with wide, tired eyes. You have a blanket meant for Ada — and you have only the one.",
    "Inside a cold, dark house, a whole family sits huddled together for warmth. A baby cries, and cries, and won't stop. There's no heat in the place, and no light but a single guttering candle. The mother looks up at you with wide, exhausted eyes. You have a blanket, meant for Ada — and you have only the one."),
  [t("Give them your blanket.", "Give them your blanket.", "Give them your blanket."),
   t("Promise to send help.", "Promise to send help.", "Promise to send help."),
   t("Try to warm the room.", "Try to warm the room.", "Try to warm the room.")])

P(33,
  t("You go on, up toward the hill. The dark is thick. Your torch throws one small circle of light on the snow. There is the van man's van, off to one side. There is the strange light in the old house, high up. And there is the last hard climb to Ada's door.",
    "You go on, up toward the hill. The dark is thick, and your torch throws one small circle of light onto the snow. Off to one side sits the van man's van. High up burns that strange light in the old house. And ahead lies the last hard climb to Ada's door.",
    "You press on, up toward the hill. The dark is thick and close, and your torch throws one small circle of light onto the snow ahead. Off to one side sits the van man's van; high up on the hill burns that strange, unexplained light in the old house; and ahead of you lies the last hard climb to Ada's door."),
  [t("The van man again.", "The van man again.", "The van man again."),
   t("The Harrow light.", "The Harrow light.", "The Harrow light."),
   t("The last stretch.", "The last stretch.", "The last stretch."),
   t("The cold makes you doubt.", "The cold makes you doubt.", "The cold makes you doubt.")])

P(34,
  t("You put your shoulder to the car and push. Your boots slip. Then, slowly, the wheels grip, and the car pulls free. The old man winds down his window. \"Bless you,\" he says, and pushes a warm flask into your hands. \"Now get where you're going, quick.\"",
    "You put your shoulder to the car and push. Your boots slip on the ice; then, slowly, the wheels grip and the car pulls free. The old man winds down his window. \"Bless you,\" he says, pressing a warm flask into your hands. \"Now get where you're going, and quick.\"",
    "You put your shoulder to the back of the car and push with everything you have. Your boots slip on the ice; then, slowly, the wheels find their grip and the car pulls free. The old man winds down his window. \"Bless you,\" he says, pressing a warm flask into your hands. \"Now get where you're going, and be quick about it.\""),
  [t("On your way.", "On your way.", "On your way."),
   t("He tells you of the hill.", "He tells you of the hill.", "He tells you of the hill.")])

P(35,
  t("You promise the family you will send help, and you mean it. But a promise is not heat, and the baby is still crying as you close the door. You feel the weight of it as you walk on. You can only be in one place at a time, tonight of all nights.",
    "You promise the family you'll send help, and you mean it. But a promise isn't heat, and the baby is still crying as you close the door behind you. You feel the weight of that as you walk on. You can only be in one place at a time, tonight of all nights.",
    "You promise the family you'll send help, and you mean every word of it — but a promise isn't heat, and the baby is still crying as you close the door softly behind you. You feel the whole weight of that as you walk on into the dark. You can only be in one place at a time, tonight of all nights."),
  [t("Rally the street.", "Rally the street.", "Rally the street."),
   t("On toward the hill.", "On toward the hill.", "On toward the hill.")])

P(38,
  t("The cold gets into your head as well as your bones. A small voice says: go home. Sit by a candle. Nobody would blame you. It would be so easy. Then you think of Ada's face, and the voice goes quiet. You are not going home. Not tonight.",
    "The cold works into your head as well as your bones. A small voice says: go home, sit by a candle, nobody would blame you. It would be so easy. Then you think of Ada's face, and the voice goes quiet. You are not going home tonight.",
    "The cold works its way into your head as well as your bones. A small, reasonable voice says: go home, sit by a candle, nobody on earth would blame you. It would be so easy to listen to it. Then you think of Ada's face, and the small voice goes quiet. You are not going home tonight, and that's the end of it."),
  [t("The last stretch.", "The last stretch.", "The last stretch."),
   t("The van man's lights.", "The van man's lights.", "The van man's lights.")])

P(39,
  t("A signpost stands half-buried in snow. You brush the snow away to read it. One arrow points along the road. One points up a path toward the hill. It leads to the old Harrow house, where the light still burns. Which way, in the dark?",
    "A signpost stands half-buried in snow. You brush it clear to read it. One arrow points along the road; the other up a path toward the hill, and the old Harrow house, where that light still burns. Which way, in the dark?",
    "A signpost stands half-buried in the snow. You brush it clear enough to read. One arrow points along the winding road; the other up a steeper path toward the hill, and the old Harrow house, where that unexplained light is still burning. Two ways up, and no one to tell you which. Which way, then, in the dark?"),
  [t("The road.", "The road.", "The road."),
   t("The light on the hill.", "The light on the hill.", "The light on the hill.")])

P(50,
  t("You are halfway across the ice now. The far bank is close — you can almost touch it. Just a few more steps. The black water is under your feet, but you try not to think of it. Slow and steady. Nearly there. Nearly—",
    "You're halfway across the ice now, and the far bank is close — you could almost touch it. Just a few more careful steps. The black water is right under your feet, but you try not to think about that. Slow and steady. Nearly there. Nearly—",
    "You're halfway across the ice now, and the far bank is close enough that you could almost reach out and touch it. Just a few more careful steps. The black water waits right under your feet, but you try very hard not to think about that. Slow and steady. Nearly there now. Nearly—"),
  [t("Nearly there.", "Nearly there.", "Nearly there."),
   t("The ice cracks.", "The ice cracks.", "The ice cracks.")])

P(51,
  t("A sound like a gunshot cracks the night. The ice splits open under your feet. In one cold second, everything could go wrong — everything. Your heart stops dead. There is no time to think now, only to move, right now, one way or the other.",
    "A sound like a gunshot cracks the night. The ice splits open under your feet. In one freezing second, everything could go wrong. Your heart stops dead. There's no time to think now — only to move, this instant, one way or the other.",
    "A sound like a gunshot cracks the night in half. The ice splits open under your feet. In one freezing second, you understand that everything could go wrong, all at once. Your heart stops dead in your chest. There's no time left to think now — only to move, this very instant, one way or the other."),
  [t("The ice gives way.", "The ice gives way.", "The ice gives way."),
   t("Scramble back to the bank.", "Scramble back to the bank.", "Scramble back to the bank.")])

P(52,
  t("You throw yourself at the far bank and grab it. You are safe — but soaked to the knee, and shaking hard. The cold water freezes on your legs at once. You saved time. But now you are wet and freezing, high on a hill, on the coldest night of the year.",
    "You throw yourself at the far bank and cling to it. You're safe — but soaked to the knee and shaking hard, the river water already freezing on your legs. You saved time, yes. But now you're wet and freezing, high on a cold hill, on the coldest night of the year.",
    "You throw yourself at the far bank and cling to it with numb hands. You're safe — but soaked to the knee and shaking hard, the river water already freezing solid on your legs. You saved yourself some time, yes. But now you're wet and freezing, high on a cold hill, on the coldest night of the whole year."),
  [t("Push on, freezing.", "Push on, freezing.", "Push on, freezing."),
   t("You dropped the heater.", "You lost the heater in the scramble.", "You lost the heater in the scramble.")])

P(53,
  t("You throw yourself back the way you came. The ice holds — just. You crawl onto the bank, safe but shaking, your heart going wild. The river almost had you. You lost time, and you lost your nerve. But you are alive, and you have learned something. The ice lies.",
    "You throw yourself back the way you came, and the ice holds — just. You crawl onto the bank, safe but shaking, your heart going wild. The river nearly had you. You've lost time, and lost your nerve with it — but you're alive, and you've learned one thing tonight: the ice lies.",
    "You throw yourself back the way you came, and the ice holds — just barely. You crawl up onto the solid bank, safe but shaking, your heart going wild in your chest. The river very nearly had you. You've lost time, and lost your nerve along with it — but you're alive, and you've learned one hard thing tonight: the ice lies."),
  [t("The long road after all.", "The long road after all.", "The long road after all."),
   t("Too shaken to go on.", "Too shaken to go on.", "Too shaken to go on.")])

P(54,
  t("You try to warm the family's room. You close the doors. You block the gaps under them with coats. It helps a little, but not enough. Without heat, a room this cold cannot be saved. The baby still cries. There is really only one thing left you can give.",
    "You try to warm the family's room — closing doors, blocking the gaps beneath them with rolled-up coats. It helps a little, but not nearly enough. Without heat, a room this cold can't really be saved. The baby still cries. There's really only one thing left that you can give.",
    "You try to warm the family's room as best you can — closing the inner doors, blocking the gaps beneath them with rolled-up coats. It helps a little, but nowhere near enough. Without any heat at all, a room this cold simply can't be saved. The baby is still crying. There's really only one thing left that you can give them."),
  [t("Give them your blanket.", "Give them your blanket.", "Give them your blanket."),
   t("Promise to send help.", "Promise to send help.", "Promise to send help.")])

P(55,
  t("You take out Ada's blanket and wrap it around the baby. The crying softens. The mother holds your arm and cannot speak. You go back out into the cold with less than you came with. But the baby is warm now. Some things you give away, and you feel richer, not poorer.",
    "You take out Ada's blanket and wrap it snugly around the baby. The crying softens, then stops. The mother grips your arm and can't speak. You step back out into the cold with less than you came with — but the baby is warm now. Some things you give away and feel richer for, not poorer.",
    "You take out the blanket meant for Ada and wrap it snugly around the crying baby. The crying softens, and then stops altogether. The mother grips your arm and can't find the words. You step back out into the cold with less than you came in with — but the baby is warm now. Some things you give away and feel richer for, not poorer."),
  [t("On, colder now.", "On, colder now.", "On, colder now."),
   t("They point you to the hill.", "They point you to the hill.", "They point you to the hill.")])

P(56,
  t("Without the blanket, the cold finds you fast. It gets in at your collar and your wrists. You walk faster to stay warm. You gave away your warmth, and now you feel it. But you would do it again. Ahead, a doorway glows with candlelight, warm and open.",
    "Without the blanket, the cold finds you fast — in at your collar, your wrists, the small of your back. You walk faster to stay warm. You gave your warmth away, and now you feel the cost of it. But you'd do it again. Ahead, a doorway glows with candlelight, warm and open.",
    "Without the blanket, the cold finds you fast — in at your collar, your wrists, the small of your back. You walk faster just to stay warm. You gave your warmth away, and now you feel the exact cost of it. But you'd do it again in a heartbeat. Ahead, a doorway glows with candlelight, warm and open, spilling gold onto the snow."),
  [t("Keep moving to stay warm.", "Keep moving to stay warm.", "Keep moving to stay warm."),
   t("A lit doorway, open.", "A lit doorway offers shelter.", "A lit doorway offers shelter.")])

P(57,
  t("A stranger stands in the lit doorway. \"You look frozen,\" she says. \"Come in, just for a minute. Warm your hands.\" It is so tempting. One warm minute. But Ada is waiting, and one minute has a way of becoming ten. You have to choose.",
    "A stranger stands in the lit doorway. \"You look half frozen,\" she says. \"Come in, just a minute — warm your hands.\" It's so tempting: one warm minute. But Ada is waiting, and one minute has a way of becoming ten. You have to choose.",
    "A stranger stands framed in the lit doorway. \"You look half frozen,\" she says kindly. \"Come in, just for a minute — warm your hands at least.\" It's so tempting: one warm minute out of the cold. But Ada is waiting up the hill, and one minute has a way of quietly becoming ten. You have to choose."),
  [t("Warm up, then on.", "Warm up, then on.", "Warm up, then on."),
   t("Refuse, and press on.", "Refuse, press on.", "Refuse, press on.")])

P(58,
  t("You thank her, but you do not stop. You press on into the dark, your teeth going like a drum. The cold is a hand around your chest now. But every step is a step closer to Ada, and that thought is its own small fire. You keep walking.",
    "You thank her, but you don't stop. You press on into the dark, teeth chattering like a drum. The cold is a hand closed around your chest now. But every step is a step closer to Ada, and that thought is its own small fire. You keep walking.",
    "You thank her warmly, but you don't stop. You press on into the dark, your teeth chattering like a drum. The cold is a hand closed tight around your chest now. But every single step is a step closer to Ada, and that thought is its own small fire inside you. You keep walking."),
  [t("The last stretch.", "The last stretch.", "The last stretch."),
   t("On toward the hill.", "On toward the hill.", "On toward the hill.")])

P(64,
  t("You stop for a moment and look at the town below. It is all dark. No street lights, no lit windows, only here and there the small gold of a candle. It is strange and beautiful and a little frightening. A whole town, holding its breath in the cold, waiting.",
    "You stop a moment and look back at the town below. It's all dark — no street lights, no lit windows, only here and there the small gold of a candle. It's strange, and beautiful, and a little frightening: a whole town holding its breath in the cold, waiting for the dawn.",
    "You stop a moment and look back down at the town below you. It's all dark — no street lights, no lit windows, only here and there the small, stubborn gold of a single candle. It's strange, and beautiful, and more than a little frightening: a whole town holding its breath in the cold, waiting for the dawn to come."),
  [t("Press on down the road.", "Press on down the road.", "Press on down the road."),
   t("The light in the Harrow house.", "The light in the Harrow house.", "The light in the Harrow house.")])

P(65,
  t("The cold is deeper now than before. There is frost on your coat, white on the wool. Your feet feel far away. This is the kind of cold that kills, slowly and quietly, if you let it. You cannot stop moving. You cannot let it win. You keep going.",
    "The cold drops deeper still. Frost forms on your coat, white on the dark wool; your feet feel far away and strange. This is the kind of cold that kills, slowly and quietly, if you let it. You can't stop moving. You can't let it win. You keep going.",
    "The cold drops deeper still, past anything you're used to. Frost forms on your coat, white against the dark wool; your feet feel far away and strangely disconnected. This is the kind of cold that kills, slowly and quietly, if you once let it. You can't stop moving. You can't afford to let it win. You keep going."),
  [t("The shivering family.", "The shivering family.", "The shivering family."),
   t("Press on.", "Press on.", "Press on.")])

# --- the van man (the trap) ---
P(40,
  t("The van man turns his smile on you. \"Cold night, friend,\" he says. \"Somebody up that hill you're worried about? I can help. Heaters, fuel, a generator — I've got it all, right here. But it's going fast. What do you say?\" His voice is warm. His prices, you are sure, are not.",
    "The van man turns his smile on you. \"Cold night, friend,\" he says. \"Somebody up that hill you're worried about? I can help. Heaters, fuel, a generator — got it all, right here, right now. Going fast, though. What do you say?\" His voice is warm. His prices, you're sure, are not.",
    "The van man turns the full beam of his smile on you. \"Cold night, friend,\" he says. \"Somebody up that hill you're worried about? I can help with that. Heaters, fuel, a generator — got it all right here, right now. Going fast, mind. What do you say?\" His voice is warm as a fire. His prices, you're quite sure, are not."),
  [t("Hear the price.", "Hear the price.", "Hear the price."),
   t("Refuse, and go round.", "Refuse and go round.", "Refuse and go round.")])

P(41,
  t("He names his price. It is robbery — five times what these things should cost. When you step back, he leans in close. \"Your Ada won't last the night, friend,\" he says softly. \"How much is she worth to you?\" He is using your fear. It is a cruel, clever trick.",
    "He names his price, and it's robbery — five times what any of it should cost. When you step back, he leans in close. \"Your Ada won't last the night, friend,\" he says softly. \"How much is she worth to you?\" He's using your fear against you. It's a cruel, clever trick.",
    "He names his price, and it's plain robbery — five times what any of it should cost, and he knows it. When you step back, he leans in close and drops his voice. \"Your Ada won't last the night, friend,\" he says softly. \"How much is she worth to you?\" He's using your fear against you, coldly. It's a cruel, clever trick, and it's working on the crowd."),
  [t("Pay him.", "Pay him.", "Pay him."),
   t("That line is the tell. Refuse.", "That line is the tell — refuse.", "That line is the tell — refuse."),
   t("Ask if it even works.", "Ask if it even works.", "Ask if it even works."),
   t("The crowd's fear.", "The crowd's fear presses in.", "The crowd's fear presses in.")])

P(42,
  t("You turn your back on him and walk away. Behind you, the frightened crowd keeps pushing money at him. You feel the pull of it — the fear, the hope of an easy answer. But there are no easy answers tonight, only cold work and good people. You go on, your money safe.",
    "You turn your back on him and walk away. Behind you, the frightened crowd keeps pushing money into his hands. You feel the pull of it — the fear, the hope of an easy answer. But there are no easy answers tonight, only cold work and good people. You go on, your money still your own.",
    "You turn your back on him and walk away into the dark. Behind you, the frightened crowd keeps pushing money into his open hands. You feel the pull of it, honestly — the fear, the hope of one easy answer. But there are no easy answers tonight, only cold work and good people. You go on, your money still your own."),
  [t("On the way.", "On the way.", "On the way."),
   t("To the shop instead.", "To the shop instead.", "To the shop instead.")])

P(43,
  t("Fear wins. You count out the money — most of what you have — and hand it over. He gives you a generator and a can of fuel, and a wide, quick smile. \"Good choice, friend,\" he says. The money is gone from your hands. Somehow, you feel colder than before.",
    "Fear wins. You count out the money — most of what you have — and hand it over. He gives you a generator and a can of fuel, and a wide, quick smile. \"Good choice, friend,\" he says. The money's gone from your pocket now. Somehow, you feel colder than you did before.",
    "Fear wins the argument. You count out the money — most of what you have on you — and hand it across. He gives you a heavy generator and a can of fuel, and a wide, quick, professional smile. \"Good choice, friend,\" he says. The money is gone from your pocket now. And somehow, you feel colder than you did before."),
  [t("Haul it up the hill.", "Haul it up the hill.", "Haul it up the hill."),
   t("A doubt already.", "A doubt already.", "A doubt already.")])

P(44,
  t("\"Does it work?\" you ask. \"In this cold? For sure?\" His smile flickers, just for a second. \"They all work,\" he says, too fast. \"No promises, mind. No refunds.\" No promises. There is your answer, if you want to hear it. A good thing does not need 'no promises.'",
    "\"Does it work?\" you ask. \"In this cold? For certain?\" His smile flickers, just for a second. \"They all work,\" he says, too fast. \"No promises, mind. No refunds.\" No promises. There's your answer, if you want to hear it — a good thing doesn't need 'no promises.'",
    "\"Does it actually work?\" you ask. \"In this cold? For certain?\" His smile flickers, just for a second, before it locks back into place. \"They all work,\" he says, too fast. \"No promises, mind. No refunds.\" No promises. There's your answer, if you're willing to hear it — a good thing has never once needed the words 'no promises.'"),
  [t("That's your answer. Refuse.", "That's your answer — refuse.", "That's your answer — refuse."),
   t("Buy it anyway.", "Buy it anyway.", "Buy it anyway.")])

P(45,
  t("The generator is heavy — a dead weight in your arms. You haul it up the hill, breathing hard. At the top, you set it down and try to start it. It coughs. It sputters. In this cold, it will not catch. You begin to understand what you have really bought.",
    "The generator is heavy — a dead weight in your aching arms. You haul it up the hill, breathing hard. At the top you set it down and try to start it. It coughs. It sputters. In this cold, it simply won't catch. You're beginning to understand what you've really bought.",
    "The generator is heavy — a dead weight in your aching arms. You haul it all the way up the hill, breathing hard, telling yourself it'll be worth it. At the top you set it down and try to start it. It coughs. It sputters. In this cold, it simply will not catch. You're beginning to understand exactly what you've really bought."),
  [t("Try and try.", "Try and try.", "Try and try."),
   t("On to Ada with nothing.", "On to Ada with nothing.", "On to Ada with nothing.")])

P(46,
  t("You open the can of fuel and smell it. It is wrong — thin and watery, more water than fuel. He sold you a can of almost nothing, for almost all your money. The doubt in you turns hard and cold. You have been cheated, and the night is only half over.",
    "You open the fuel can and smell it. It's wrong — thin and watery, more water than fuel. He sold you a can of almost nothing for almost all your money. The doubt in you turns hard and cold. You've been cheated, and the night is only half over.",
    "You open the fuel can and smell it, and your heart sinks. It's wrong — thin and watery, more water than fuel by the smell of it. He sold you a can of almost nothing for almost all the money you had. The doubt in you turns hard and cold. You've been cheated, plainly, and the night is only half over."),
  [t("On to Ada.", "On to Ada.", "On to Ada."),
   t("Back to argue.", "Back to argue.", "Back to argue.")])

P(47,
  t("You pull the cord again and again. The generator coughs, catches for one second, and dies. The fuel is bad. The machine is junk. You paid nearly everything for a heavy, useless lump of metal in the snow. There is nothing to do but leave it, and go to Ada with empty hands.",
    "You pull the cord again and again. The generator coughs, catches for a single second, and dies. The fuel is bad, the machine is junk. You paid nearly everything you had for a heavy, useless lump of metal in the snow. Nothing to do now but leave it and go to Ada with empty hands.",
    "You pull the cord again, and again, and again. The generator coughs, catches for a single hopeful second, and dies. The fuel is bad, and the machine is junk. You paid nearly everything you had for a heavy, useless lump of cold metal in the snow. There's nothing to do now but leave it where it lies and go to Ada with empty hands."),
  [t("On to Ada, fleeced.", "On to Ada, fleeced.", "On to Ada, fleeced."),
   t("Leave it in the snow.", "Leave it in the snow.", "Leave it in the snow.")])

P(48,
  t("You turn to find the van. It is gone. The lights, the man, the crowd — all gone, melted back into the dark. Only the cold is left, and your empty pockets, and the useless thing in the snow. He knew. He always knew. And now he is somewhere else, selling fear to someone else.",
    "You turn to find the van, but it's gone — the lights, the man, the crowd, all melted back into the dark. Only the cold is left, and your empty pockets, and the useless thing in the snow. He knew. He always knew. And now he's somewhere else, selling fear to someone new.",
    "You turn to find the van, but it's gone — the lights, the man, the whole frightened crowd, all melted back into the dark as if they'd never been. Only the cold is left, and your empty pockets, and the useless machine in the snow. He knew. He always knew. And now he's somewhere else in the dark, selling the same fear to someone new."),
  [t("On to Ada.", "On to Ada.", "On to Ada."),
   t("Stand a moment in the dark.", "Stand a moment in the dark.", "Stand a moment in the dark.")])

P(49,
  t("You look at the crowd around the van. They are not fools. They are just afraid — for their children, their parents, themselves. Fear makes good people do foolish things. You see the whole trick now, laid out clear. The man sells fear, and tonight, fear sells itself.",
    "You look at the crowd around the van. They're not fools — they're just afraid, for their children, their parents, themselves. Fear makes good people do foolish things. You can see the whole trick now, laid out clear: the man sells fear, and on a night like this, fear sells itself.",
    "You look properly at the crowd pressing around the van. They're not fools, any of them — they're just afraid, for their children, their parents, themselves. Fear makes good people do foolish things. You can see the whole trick now, laid out perfectly clear: the man sells fear, and on a night like this one, fear sells itself."),
  [t("Hear the price anyway.", "Hear the price anyway.", "Hear the price anyway."),
   t("Refuse, and go round.", "Refuse and go round.", "Refuse and go round.")])

# --- the light in the Harrow house (the mystery) ---
P(70,
  t("The old Harrow house stands on the hill. It has been empty for years — dark, cold, forgotten. But tonight, one window glows with a warm, steady light. No one lives there. No one should be there. And yet the light burns, gold in the dark, as if someone is home.",
    "The old Harrow house stands high on the hill. It's been empty for years — dark, cold, forgotten by everyone. But tonight, one window glows with a warm, steady light. No one lives there. No one should be there. And yet the light burns on, gold in the dark, as if someone were home.",
    "The old Harrow house stands high on the hill. It's been empty for years — dark, cold, and quietly forgotten by the whole town. But tonight, one single window glows with a warm, steady light. No one lives there. No one should be there at all. And yet the light burns on, gold in the dark, exactly as if someone were home."),
  [t("Go and see.", "Go and see.", "Go and see."),
   t("Leave it. Ada first.", "Leave it — Ada first.", "Leave it — Ada first.")])

P(71,
  t("You knock on the old door. No answer. You knock again, and call out. Still nothing. But when you push, the door swings open — it was never locked. Inside is cold and dark, and it smells of dust and years. But somewhere further in, that warm light is still burning.",
    "You knock on the old door. No answer. You knock again and call out; still nothing. But when you push, the door swings open — never locked. Inside it's cold and dark, and it smells of dust and years. But somewhere further in, that warm light is still burning.",
    "You knock on the old door. No answer. You knock again, harder, and call out; still nothing at all. But when you push, the door swings quietly open — it was never locked. Inside it's cold and dark, and it smells of dust and long-shut years. But somewhere further in, that warm light is still burning."),
  [t("Go in.", "Go in.", "Go in."),
   t("Call out and wait.", "Call out and wait.", "Call out and wait."),
   t("Dust and cold inside.", "Years of dust and cold inside.", "Years of dust and cold inside.")])

P(72,
  t("You go in, following the light. In a back room, by a candle almost burned down, an old man lies on the floor. He is thin, and grey, and very cold. He fell hours ago, and could not get up. His eyes find yours. \"You came,\" he whispers. \"Nobody comes.\"",
    "You go in, following the light. In a back room, by a candle burned almost to nothing, an old man lies on the floor. He's thin, grey, and dangerously cold. He fell hours ago and couldn't get up again. His eyes find yours. \"You came,\" he whispers. \"Nobody comes.\"",
    "You go in, following the warm light. In a back room, by a candle burned almost down to nothing, an old man lies on the floor. He's thin, and grey, and dangerously cold to the touch. He fell hours ago, it's clear, and hasn't been able to get up again. His eyes find yours in the dark. \"You came,\" he whispers. \"Nobody ever comes.\""),
  [t("Get him warm.", "Get him warm.", "Get him warm."),
   t("Run for help.", "Run for help.", "Run for help.")])

P(73,
  t("You call out into the dark house. For a long moment, nothing. Then, from a back room, a weak voice answers — thin, cracked, afraid. Someone is here. Someone needs help. You cannot walk away from that, not tonight, not ever.",
    "You call out into the dark house. For a long moment, nothing at all. Then, from a back room, a weak voice answers — thin, cracked, and afraid. Someone is here. Someone needs help. You can't walk away from that, not tonight, not ever.",
    "You call out into the dark, silent house. For a long moment there's nothing at all. Then, from a back room, a weak voice answers — thin, cracked, and clearly afraid. Someone is here after all, in the cold and the dark. Someone needs help. You can't just walk away from that, not tonight, and not ever."),
  [t("Go in.", "Go in.", "Go in."),
   t("Fetch help.", "Fetch help.", "Fetch help.")])

P(74,
  t("You wrap the old man in your coat. You build up the little fire and hold his cold hands in yours. Slowly, slowly, the colour comes back to his face. He drinks a little from your flask. \"Thank you,\" he says, and his eyes fill. You got here in time. Just in time.",
    "You wrap the old man in your coat, build up the little fire, and hold his cold hands in yours. Slowly, slowly, the colour comes back into his face. He drinks a little from your flask. \"Thank you,\" he says, and his eyes fill. You got here in time — only just, but in time.",
    "You wrap the old man in your own coat, build up the little fire, and hold his cold hands between yours. Slowly, slowly, the colour comes back into his grey face. He drinks a little from your flask. \"Thank you,\" he says, and his tired eyes fill. You got here in time — only just, but in time. A few hours more and it would have been another story."),
  [t("He speaks of Ada.", "He speaks of Ada.", "He speaks of Ada."),
   t("Get you both to Ada.", "Get you both to Ada.", "Get you both to Ada.")])

P(75,
  t("You turn to run for help — then stop. There is no help coming. The roads are blocked. The phones are down. It is you, or it is no one, for this man too. You cannot save everyone tonight. But you cannot leave him on the floor to freeze, either.",
    "You turn to run for help — then stop cold. There is no help coming. The roads are blocked, the phones are down. It's you or no one, for this man as well. You can't save everyone tonight. But you can't leave him on the floor to freeze, either.",
    "You turn to run for help — and then stop cold, understanding. There is no help coming. The roads are blocked, the phones are down, and dawn is hours away. It's you or it's no one, for this man too. You can't save everyone tonight, you know that. But you can't leave him on the floor to freeze, either."),
  [t("Go back in.", "Go back in.", "Go back in."),
   t("On to Ada, torn.", "On to Ada, torn.", "On to Ada, torn.")])

P(76,
  t("Warm now, the old man talks. \"My name is Harrow,\" he says. \"I came back months ago. I told no one.\" He looks at the fire. \"Ada. She is my sister. We had a fight, long ago. Forty years, we haven't spoken. Forty years. And she is just down the hill.\"",
    "Warm now, the old man talks. \"My name is Harrow,\" he says. \"I came back months ago. I told no one.\" He looks into the fire. \"Ada is my sister. We fought, long ago — a stupid thing. Forty years, we haven't spoken. Forty years. And she's just down the hill.\"",
    "Warm now, and steadier, the old man talks. \"My name is Harrow,\" he says. \"I came back months ago. I told no one — I was ashamed to.\" He looks into the fire. \"Ada is my sister. We fought, long ago, over something stupid. Forty years, we haven't spoken a word. Forty years. And she's been just down the hill the whole time.\""),
  [t("Bring them together.", "Resolve to bring them together.", "Resolve to bring them together."),
   t("On to Ada with the news.", "On to Ada with the news.", "On to Ada with the news.")])

P(77,
  t("Forty years is a long time to be angry. And a cold night is a strange, hard gift: it does not care about old fights. Two old people, a brother and a sister, both alone in the dark, both cold. You are going to bring them together tonight. You have decided.",
    "Forty years is a long time to stay angry. And a cold night is a strange, hard gift: it doesn't care about old fights. Two old people — a brother and a sister — both alone in the dark, both cold, both a short walk apart. You're going to bring them together tonight. You've decided.",
    "Forty years is a long time to stay angry at anyone. And a cold night is a strange, hard sort of gift: it doesn't care in the slightest about old fights. Two old people — a brother and a sister — both alone in the dark, both cold, both only a short walk apart. You're going to bring them together tonight. You've decided, and that's that."),
  [t("Down to Ada.", "Down to Ada.", "Down to Ada."),
   t("Warm Harrow first.", "Warm Harrow first.", "Warm Harrow first.")])

P(78,
  t("Inside, the house is a museum of cold. Dust lies thick on everything. Chairs sit under white sheets. It is like walking into a stopped clock. But the warm light pulls you on, room by room, deeper in. Someone made that light. Someone is here.",
    "Inside, the house is a museum of cold. Dust lies thick on everything; chairs sit under white sheets like ghosts. It's like walking into a stopped clock. But the warm light draws you on, room by room, deeper in. Someone made that light. Someone is here.",
    "Inside, the house is a kind of museum of cold. Dust lies thick over everything; chairs sit shrouded under white sheets like patient ghosts. It's like walking into a clock that stopped years ago. But the warm light draws you on, room by room, deeper into the dark. Someone made that light. Someone, against all sense, is here."),
  [t("Deeper in.", "Deeper in.", "Deeper in."),
   t("An old photograph.", "An old photograph on the wall.", "An old photograph on the wall.")])

P(79,
  t("On the wall hangs an old photograph. Two young people, a boy and a girl, laugh together in summer light. You look closer. The girl is Ada — young, but her, without a doubt. Then, from the next room, you hear a small sound. Slow, weak breathing.",
    "On the wall hangs an old photograph: two young people, a boy and a girl, laughing together in summer light. You look closer — the girl is Ada, young, but unmistakably her. Then, from the next room, comes a small sound: slow, weak breathing.",
    "On the wall hangs an old, faded photograph: two young people, a boy and a girl, laughing together in some long-ago summer light. You look closer, and your breath catches — the girl is Ada, young, but unmistakably her. Then, from the next room, comes a small sound: slow, weak, laboured breathing."),
  [t("Follow the sound. Find him.", "Follow the sound, and find him.", "Follow the sound, and find him."),
   t("The years between them.", "The years between them.", "The years between them.")])

P(69,
  t("Forty years of silence hang in this cold house. A brother and a sister who stopped speaking, and never started again. It is a sad, heavy thing. Then, from the next room, comes the breathing again. Slow. Weak. Someone real, someone alive, right now, needing you.",
    "Forty years of silence hang in this cold house — a brother and a sister who stopped speaking and never started again. It's a sad, heavy thing to stand inside. Then, from the next room, the breathing comes again: slow, weak. Someone real, someone alive, right now, needing you.",
    "Forty years of silence hang in the cold air of this house — a brother and a sister who stopped speaking one day and never started again. It's a sad, heavy thing to stand inside of. Then, from the next room, the breathing comes again: slow, and weak, and labouring. Someone real, someone alive, right now, needing you."),
  [t("Follow the breathing. Find him.", "Follow the breathing, and find him.", "Follow the breathing, and find him."),
   t("It's too much. Go to Ada.", "It's too much — go to Ada.", "It's too much — go to Ada.")])


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
