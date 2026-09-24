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
