#!/usr/bin/env python3
"""Phase 2+3 for book 7, 'High Water' (standalone).

The branching ENGINE is the proven, validator-clean topology shared by every book
(same ids, edges and flag positions). We clone book 6's graph exactly, remap three
flag names role-for-role, stamp this book's identity, and install this book's own
three-level prose. Flag re-map: has_fires->has_wall, dodged_buyer->dodged_dealer,
paid_buyer->paid_dealer (found_child, rallied_village, helped_stranger, gave_shelter,
took_shortcut keep their names). The validator must return 0 errors on the output.

Run: python3 scripts/build_ep07.py
"""
import json, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SRC = os.path.join(ROOT, "content", "episode-06.json")
OUT = os.path.join(ROOT, "content", "episode-07.json")

FLAG = {"has_fires": "has_wall", "dodged_buyer": "dodged_dealer", "paid_buyer": "paid_dealer"}
def rf(lst): return [FLAG.get(f, f) for f in (lst or [])]

# --- node prose: id -> {A2,B1,B2} ---
P = {
1: {
"A2": "It is the wettest night in years. The river has climbed all day and will not stop. Along the low street the water is already at the doorsteps. Then old Nora Kettle falls on the wet back step and cannot get up. The sandbag wall along the lane is not built, and the river is still rising. Keeping the water out of the houses is on you now.",
"B1": "It is the wettest night in years, and the river has climbed all day under hard, steady rain. Along the low street the water stands dark at the doorsteps. A whole row of homes is held on a few inches of bank. Then old Nora Kettle goes over on the wet back step and cannot get up. The sandbag wall along the lane is unbuilt, and the water is already over the kerb. No crew will come before morning. Keeping the river out of the houses is on you now.",
"B2": "It is the wettest night in years, and the river has climbed all day under a hard, unbroken rain. The water slides past the old flood mark, and along the low street it stands black at the doorsteps. A whole row of homes now hangs on a few inches of soaked bank. Then old Nora Kettle, coming down the back step to start the work, goes over on her bad hip and cannot rise. The sandbag wall along the lane is unbuilt, the water is already over the kerb, and no crew will come before morning. Keeping the river out of the houses — and the home that is all Nora has — is suddenly, entirely on you.",
},
2: {
"A2": "You gather what the shed holds: a stack of sacks, a spade, a small pump, a good torch. Outside the rain beats down and the river keeps rising. The water is already across the lane. You must decide what to do, and do it fast.",
"B1": "You gather what the shed holds: a stack of empty sacks, a spade, a small petrol pump, a good torch. Outside, the rain comes straight down and the river keeps on rising. The water is already creeping across the lane. You have to decide what to do, and do it quickly.",
"B2": "You gather what the shed will give you: a stack of empty sacks, a spade, a small petrol pump, a good torch for the dark. Outside the rain comes straight down out of a low sky, and the river has real weight to it now. You can watch the water creep across the lane as you stand there. Whatever you choose, you must choose it fast — every minute you spend thinking is a minute the river is climbing the bank.",
},
3: {
"A2": "You try the phone. At last Tom's voice comes through from the yard. No one can come out before morning, he says — not in a flood like this. Build the wall and keep it holding, he tells you, if you can.",
"B1": "You try the phone. It rings and rings, then at last Tom's voice gets through from the boatyard. No crew can come out before morning, he says — not with the river up like this. Build the wall down the lane, he tells you, and hold it however you can until the water turns.",
"B2": "You try the phone with wet fingers. It rings and rings into the dark, and then, at last, Tom's steady voice gets through from the boatyard. No crew can come out before morning, he tells you plainly; not with a river that climbs this fast and this hard. The only thing that beats a flood is a wall built by hand — so stack the bags down the lane, he says, and hold it, whatever it takes, until first light.",
},
4: {
"A2": "You go to Nora at the foot of the step. You make her as warm and dry as you can. But the water is still rising, and shelter is not enough. The houses out there need the wall. You need bags, a plan, and a clear head before you start.",
"B1": "You get to Nora at the foot of the back step. You make her as easy and warm as you can. But the river is still climbing, and shelter alone won't do. The houses along the lane need the wall built and held. You need sandbags, a plan, and a clear head before you go out into the water.",
"B2": "You get to Nora at the foot of the back step. You make her as easy and as dry as you can, a coat under her head, a blanket over her. But keeping her warm is not the same as keeping the river out. Shelter alone won't save a single home. The houses out there need the wall. The wall means bags, a spade, and a clear head. Before you can do any good tonight, you have to decide how to begin.",
},
5: {
"A2": "You step out along the lane. The night is huge and loud with rain, and the black water shines all around you. The river pushes at the bank like a hand. Far off, down at the water's edge, a small light moves where no light should be.",
"B1": "You step out along the lane. The night is huge and full of rain, and the dark water seems to shine under your torch. The river presses at the whole low street like a hand. Then, far off, down at the water's edge, you catch it: a small light moving, out where no one should be tonight.",
"B2": "You step out along the lane, and the wet night takes your breath. It is huge and loud, and the black water seems to hold its own faint shine under the torch. Over everything the river presses, slow and heavy, finding the low ground first. Then, far off, down at the water's edge, you catch something that stops you: a small light, moving, out where no one in their right mind should be on a night like this.",
},
6: {
"A2": "You make yourself think. You could build the wall first, and worry about the rest after. You could see to Nora and the neighbours. Or you could wake the street to help. Each choice costs time — and the river is rising now.",
"B1": "You make yourself stop and think. You could get the wall going first, and worry about everything else after. You could go to Nora and the neighbours instead. Or you could rouse the whole street and bring more hands. Each choice costs time you don't have — and out in the dark, the river is already climbing the bank.",
"B2": "You make yourself stop and think, though every part of you wants to run. You could get the wall built first and leave the rest for later. You could put people before the houses, and go to Nora and the frightened neighbours. Or you could wake the whole street and turn one pair of hands into twenty. Each path costs time, and time is the one thing the river will not give you — out there, with every minute, the water is climbing higher.",
},
8: {
"A2": "The cold water seems to rise in your chest too. You think of the houses on the low street. They are everything these people have. If the wall stays unbuilt, the river is inside by dawn. No one else will do this. It is you, tonight, or no one.",
"B1": "The cold settles into your chest like a weight. You think of the houses out there: a whole row of homes, the little street that is all Nora has. If the wall stays unbuilt much longer, the river is through the doors by dawn. That isn't a fear; it's a plain fact. No one else is coming to do this. It is you, tonight, or no one.",
"B2": "The cold settles into your chest like a weight. The size of the night opens up in front of you. You think of the row of homes along the low street. It is a lifetime of living, for Nora and for every family here. The street is the last thing keeping any of them in place. If the wall stays unbuilt much longer, the river will be through every door by first light. No one will be able to undo that. This is not a fear you can talk yourself out of. It is a fact. And no one else is coming to do it. It is you, tonight, or no one at all.",
},
9: {
"A2": "Tom heaves open the yard store. Inside there are pallets of sandbags, a petrol pump, coils of rope, and a good torch. \"Take what you need,\" he says. \"I'll stay by the phone.\" He is a steady man. Tonight it shows.",
"B1": "Tom heaves open the yard store and holds up the torch. Inside are pallets of sandbags, a petrol pump, coils of rope, and dry sacking. \"Take what you need,\" he says. \"I'll stay here by the phone and raise who I can.\" He's a steady man, and on a night like this it shows.",
"B2": "Tom heaves open the door of the yard store and swings the torch inside. There are pallets of sandbags, a petrol pump, coils of good rope, and a roll of dry sacking. \"Take whatever you need,\" he says, no fuss about it. \"I'll stay here by the phone and raise what hands I can.\" He's a steady, unshowy man. He is the kind you only really notice on a night like this. And tonight it shows.",
},
10: {
"A2": "You knock along the row. Old Mr Hollis opens up, pale in the dark. His power is out and his torch is dead. His hands are shaking too hard to lift a bag. \"I can't hold it back,\" he says. You have a long night ahead. But he is here, and he is scared, and he is asking you.",
"B1": "You knock along the row of houses, and old Mr Hollis opens up, pale in the wet. His power is out, his torch is dead, and his hands are shaking too hard to lift a single bag. \"I can't hold it back,\" he says. You have a long, hard night ahead of you. But he's here, and he's frightened, and he's asking you.",
"B2": "You knock along the row of houses until a door opens: old Mr Hollis, pale and blinking in the dark, a coat pulled over his nightclothes. His power is out, his torch is dead, and his hands are shaking far too hard to lift a sandbag even if he could reach them. \"I can't hold it back,\" he says, and the fear is plain in his voice. You have a long, hard night ahead and a street to save. But he is here, now, and he is frightened, and it is you he is asking.",
},
11: {
"A2": "You go straight to the lane and stack what you can. A bag here, a bag there, a low line against the water. But the wall is thin and short. Without proper bags it won't hold an hour. You cannot just build a little and hope.",
"B1": "You go straight out to the lane and stack what you can. A bag, a spadeful of sand, a low line going up here and there. But the wall is thin and low. Without proper sandbags it won't hold an hour. You can't just build a little and walk away and hope.",
"B2": "You go straight out to the lane and start building what you can. You work as fast as your cold hands will move. A bag, a spadeful of sand, a low line rising here and there along the kerb. But the wall comes up thin and low. Without proper sandbags, you can see it will be over within the hour. You can't simply set a few bags down and turn your back and hope the river is kind. A half-built wall is no safer than none.",
},
12: {
"A2": "You go from door to door with the same words. Bring sand. Lend a hand at the bags. Help me hold the wall. Some turn away. But a few pull on their coats and come out. A few is enough to begin.",
"B1": "You go door to door, asking each one the same thing. Bring sand for the bags. Lend a hand at the wall. Help me hold the line down the lane. Some turn away and shut the door. But a few pull on their coats and step out into the rain. Tonight, a few is enough to begin.",
"B2": "You go from house to house, knocking, asking each sleepy face the same three things. Bring what sand or sacks you have. Lend a pair of hands at the wall. Help me hold the line down the lane till the river turns. Some look at the rain and the hour and quietly shut the door. You can't even blame them. But a few reach for their coats and boots and step out with you. On a night like this, a few is all it takes to begin.",
},
13: {
"A2": "You take charge of the bags and the pump yourself. The pallet is heavy, and every bag matters now. Stacked well, the wall holds the river back all night. Done badly, and the water is in by dawn. You hold them close and head for the lane.",
"B1": "You take charge of the bags and the pump yourself. The pallet is heavy, and every bag of them matters now. Stacked with care, they will hold the river back all night; wasted, and the water is through the doors before dawn. So you hold them close and head out for the lane.",
"B2": "You take charge of the bags and the pump yourself. This, above everything, is the thing the night turns on. The pallet is heavy to shift, and every bag of it counts now. There is no more until the roads clear. Stacked with care, this wall will hold the river back until dawn. Dropped in the water or built badly, and the homes are lost long before the sun. So you take hold, square your shoulders, and head out into the rain.",
},
14: {
"A2": "You take just a torch and a spade. They give you light and a way to dig. But not the wall itself. And you have set no proper bags aside. You will still need real sandbags, and soon. If not, the lane floods and the river wins.",
"B1": "You take just a torch and a spade. They give you light to work by and a way to move sand. But not the wall itself. And you've set no proper bags aside. You'll still need real sandbags, and soon. If not, the lane floods and the river wins.",
"B2": "You take just a torch and a spade. It is enough to see by, enough to move a little sand. It is nothing like enough to carry the night. You have light and a start, and that is all. You've set no proper bags aside. A spade and good will won't hold a river off a whole street. You'll still need real sandbags, and you'll need them soon. If not, the lane floods and the water does as it likes.",
},
15: {
"A2": "Old Jack Reed knows this river. He has watched it rise for years. \"Stay off the weir bridge,\" he says. \"It looks quick. It drowns.\" He warns you about the dealer too. \"Mind your bags. Hold the wall. That's the whole job tonight.\"",
"B1": "Old Jack Reed knows this river in the dark better than anyone. \"Stay off the weir bridge,\" he says. \"It looks like a short cut. It isn't — it's a drowning.\" He warns you about the dealer too, that smiling man with the van. \"Mind your bags, hold the wall — that's the whole of the job tonight.\"",
"B2": "Old Jack Reed has watched this river come up for more years than you've been alive, and he finds you in the dark to say his piece. \"Stay off the weir bridge,\" he tells you, gripping your arm. \"It looks like it'll save you half the walking. It won't — the planks are rotten, and it's a drowning, not a short cut.\" He warns you about the dealer too, that smiling man with the van who has been circling the street. \"Mind your bags, hold the wall, and don't let anyone talk you off the job. That's the whole of it tonight.\"",
},
16: {
"A2": "You stack bags at Mr Hollis's door and settle him with a blanket. Slowly his shaking stops. \"Bless you,\" he says, holding your hand. You promise to look in on him again. Then you turn back out into the rain.",
"B1": "You get a line of bags across Mr Hollis's door and settle him back with a blanket. Little by little, his shaking eases. \"Bless you,\" he says, gripping your hand hard. You promise to look in on him again before morning. Then you turn back out into the rain and the waiting lane.",
"B2": "You get a line of bags across his doorway and settle Mr Hollis in a chair with a blanket round his shoulders. You wait until, little by little, the shaking goes out of him. \"Bless you,\" he says, and grips your hand with surprising strength. You promise you'll look in on him again before the night is out. Then you turn back to the door, and the rain, and the long dark lane still waiting for its wall.",
},
17: {
"A2": "The wall comes first. The rest can wait a moment. But how do you start? You could get proper bags first. Or you could go straight out to the lane.",
"B1": "Holding the wall comes first. The rest can wait a moment. But you still have to choose how. You could get proper sandbags from the yard first. Or you could go straight out to the lane and begin.",
"B2": "Keeping the wall up comes first. Everything else can wait a moment. But you still have to decide how to do it. You could make sure of proper sandbags at the yard before anything else. Or you could go straight out to the lane now and start building what you can.",
},
18: {
"A2": "The work takes it out of you. Your back burns and your arms shake. The rain fights you at every bag. You are near your limit. If you fall now, no one is left. So go slow and careful.",
"B1": "The work takes it out of you. Your legs burn, your chest heaves, and the rain fights you at every step. You are near your own limit, and you know it. If you drop here, there is no one left to hold the wall. So go slowly, and go carefully.",
"B2": "The work takes it out of you. Your back burns, your chest heaves, and the rain fights you at every bag. You are near your own limit, and you know it well. If you drop out here, there is no one left to hold the wall. So you go slowly. You go carefully. You cannot afford to fall.",
},
19: {
"A2": "The street wakes up. People start to move. One man wheels out a barrow of sand. A woman drags out sacks. A plan grows, door by door. You are not alone now. That changes everything.",
"B1": "The street wakes to itself, and people begin to move. One man wheels out a barrow of sand. A woman drags out a roll of sacks. Door by door, a plan takes shape. You are not doing this alone any more. And that changes everything.",
"B2": "The street wakes to itself, and people begin to move in the dark. One man wheels out a barrow of sand. A woman drags out an armful of empty sacks. Door by door, a plan takes shape between you. You are not doing this alone any more. And on a night like this, that changes everything.",
},
20: {
"A2": "No one comes out. Doors stay shut. Faces turn from the windows. They are afraid, and afraid people go quiet. You cannot force them. So you go on alone. It is harder this way. But the water can't wait.",
"B1": "No one stirs. Doors stay shut, and faces turn from the windows. They are afraid, and afraid people go quiet. You can't force them to help. So you turn away and go on alone. It's harder this way. But the river can't wait for them.",
"B2": "No one stirs. Doors stay shut, and faces turn away from the dark windows. They are afraid, and frightened people go quiet. You can't force them, and you don't try. So you turn away and go on alone. It is much harder this way. But the river out there cannot wait for anyone to find their courage.",
},
21: {
"A2": "The near wall is up. Now for the far houses. There are two ways down. The long lane is safe but slow. The weir bridge is quick, straight across. But in a flood like this, it could kill.",
"B1": "The near wall is holding. Now for the far houses. There are two ways to get down there. The long lane round is safe but slow. The weir bridge is quick, straight across. But in a flood like this, the water could kill.",
"B2": "The near wall is built and holding. Now for the far houses, where the water pools worst. There are two ways to reach them. The long lane round the edge is safe, but slow. Straight across the weir bridge is quick — and a killer with the river up like this.",
},
22: {
"A2": "You take Jack Reed's words to heart. Mind the bags. Keep off the weir bridge. Don't trust the dealer. Hold the wall above all. It is simple, good advice. Now you just have to follow it.",
"B1": "You take Jack Reed's words to heart. Mind the bags carefully. Keep well off the weir bridge. Don't trust the dealer. And hold the wall above everything else. It's simple advice, and good. Now you just have to follow it.",
"B2": "You take old Jack Reed's words to heart. Mind the bags carefully. Keep well off the weir bridge. Don't let the dealer talk you round. And above all else, hold the wall. It is simple advice, and good advice. Now you only have to actually follow it, all night long.",
},
23: {
"A2": "The good turn steadies you. Helping someone helps you too. Your head is clearer now. Your hands are surer. There is a hard night still to come. But you feel able to meet it.",
"B1": "You feel steadier for the good turn you did. Helping someone seems, oddly, to steady you too. Your head is clearer, and your hands are surer. There is a hard night still to go. But now you feel able to meet it.",
"B2": "You feel steadier for the good turn you did. Oddly, helping someone else seems to steady you too. Your head is clearer now, and your hands are surer. There is a long, hard night still ahead of you. But you feel able, now, to go out and meet it. The street is still out there, waiting for you.",
},
24: {
"A2": "A man waits in the lane, a torch in his hand. It is the dealer. He has pumps to sell and a strong back to offer. He smiles too easily. \"The street's not your job tonight, friend,\" he says. You have met his kind before.",
"B1": "A man stands in the lane, a torch swinging in his fist — the dealer. He has pumps to sell and a strong back to offer, and he smiles too easily. \"The street's not really your job tonight, friend,\" he says. You've met his kind before.",
"B2": "A man stands in the lane, a torch swinging in his fist. It is the dealer, Rourke. He has pumps to sell and a strong back to lend, and he smiles far too easily. \"The street's not really your job tonight, friend,\" he says. You have met this kind before, and you know the smile.",
},
25: {
"A2": "You lead a small band out to the lane. Together, you all feel stronger. They carry sand and sacks. \"This way!\" you call through the rain. And they come. It is a good feeling in a hard hour.",
"B1": "You lead a small band out toward the wall. Walking together, you all feel stronger. They carry sand, sacks, and the pump. \"This way!\" you call into the rain, and they come. It's a good feeling, in a hard hour.",
"B2": "You lead a small band out toward the wall. Walking together, all of you feel stronger for it. They carry sand, sacks, and the heavy pump between them. \"This way!\" you call into the rain, and they come after you. It is a good feeling to have, in such a hard hour.",
},
26: {
"A2": "The lane is black and running with water. The rain streams down it. There is no shelter here. But the ground is firm under your feet. And it runs where you need to go. So you keep walking.",
"B1": "The lane is black and awash, the rain pressing down it, no shelter anywhere. But it's solid under your feet, and it runs where you need to go. So you keep walking, step after step.",
"B2": "The lane is black and running ankle-deep, the rain pressing down the length of it, and there is no shelter anywhere along it. But it is solid under your feet, and it runs exactly where you need to go. So you keep walking, step after cold step, toward the far houses.",
},
27: {
"A2": "The weir bridge would halve the way. The far houses are close beyond it. But the planks are old and slick. The race below runs fast and deep. Jack Reed told you to keep off it. He was not joking.",
"B1": "The weir bridge would halve the way, and the far houses lie close beyond it. But the planks are old and slick above a fast, deep race. Jack Reed told you to keep off it — and he wasn't joking.",
"B2": "The weir bridge would halve the walking, and the far houses lie close beyond it. But the planks are rotten and slick above a deep, fast race, and the whole thing shakes when the water hits it. Jack Reed told you plainly to keep off it. And he was not joking. You will have to choose, and choose quickly.",
},
28: {
"A2": "You step out onto the planks. At once it feels wrong. The race runs below, black and fast. Every step is a gamble now. And you are out on it, alone.",
"B1": "You step out onto the planks, and at once it feels wrong. The race waits below, black and deep and fast. Every step is a gamble now — and you're out on it, alone. There is no going back once you start across.",
"B2": "You step out onto the planks, and at once it feels wrong under you. The race waits below, black and deep and killing fast. Every single step is a gamble now. And you are out on it already, alone, with no one to pull you back. There is no turning back once you are this far out.",
},
29: {
"A2": "The pump won't prime. It coughs and dies. In a flood like this, that is a hard loss. You must fill and stack bags by hand now. Or go back to the yard for another one.",
"B1": "The pump won't prime. It coughs, catches for a second, and dies. That's a hard loss in a flood like this. You'll have to fill and stack bags by hand. Or go back to the yard for another pump.",
"B2": "The pump won't prime. It coughs, catches for a single second, and dies in your hands. In a flood like this one, that is a real loss. You will have to fill and stack every bag by hand now, slow and heavy work. Or you can go back to the yard for another pump and start again.",
},
30: {
"A2": "The lane runs on. The water gets deeper by the hour. Below, a house sits dark, with the river at its door. Ahead, the rain nearly knocks you flat. And there is a signpost, half down in the water.",
"B1": "The lane runs on along the row, the water deepening by the hour. Below, a house sits dark, the river already at its door. Ahead, the driving rain seems to push back at you. And there's a signpost, half fallen in the flood.",
"B2": "The lane runs on along the row, and the water deepens by the hour. Below you, a low house sits dark and silent, the river already lapping at its door. Ahead, the driving rain seems almost to push back against you. And there is an old signpost, half fallen and leaning in the flood.",
},
31: {
"A2": "An old man has gone down in the flooded lane and can't get up. The cold water is taking hold of him. Stop, and you lose time. Don't, and he may not last the hour.",
"B1": "An old man has gone down in the flooded lane and can't get up. The cold is already taking hold of him. Stop, and you lose time you don't have. Don't, and he may not last the hour.",
"B2": "An old man has gone down in the flooded lane and cannot get himself up. The cold water has hold of him already, and he is shaking badly. Stop for him, and you lose time you do not have. Don't, and he may not last out the hour in the rising water.",
},
32: {
"A2": "A family is trapped in a flooding house. No power, no light, a child crying in the dark. The water is at their feet. The parents look at you, tired and afraid. You have a lamp and a coat. It is not much. But it is more than they have.",
"B1": "A family is shut in a flooding house — no power, no light, a child crying in the dark. The water is rising at their feet. The parents look at you with tired, hopeless eyes. You have a lamp and a coat of your own. Not much, but more than they've got.",
"B2": "A family is shut in a flooding house, the water seeping under the door, with no power and no light and a child crying in the dark. The parents look up at you with tired, hopeless eyes. You have a lamp and a dry coat of your own. It is not much. But it is a great deal more than they have.",
},
33: {
"A2": "You push on through the worst of it. Each step is a fight now. The rain stings your face. Ahead lie choices. The dealer may be near. Or that light at the water's edge. Or you drive straight on for the wall.",
"B1": "You push on through the worst of the rain, each step a fight now, the water dragging at your legs. Choices lie ahead. The dealer may be near. There is that strange light out at the water's edge. Or you can just drive on for the wall.",
"B2": "You push on through the worst of it, and each step is a fight now, the rain stinging your face raw. Several choices lie ahead of you. The dealer may be waiting near. There is still that strange light out at the water's edge. Or you can set all of it aside and drive straight on for the wall.",
},
34: {
"A2": "You get the old man up and warm him as you can. His eyes fill. He presses a coil of rope on you. \"Take it,\" he says, \"for your trouble.\" A small thing. But freely given. You take it and move on.",
"B1": "You get the old man up onto his feet. You warm him as best you can. His eyes fill, and he presses a coil of rope into your hands. \"Take it,\" he says, \"for your trouble.\" A small thing — but freely given, and you take it and move on.",
"B2": "You get the old man up onto his feet and warm his hands as best you can. His eyes fill, and he presses a coil of good rope into your arms. \"Take it,\" he says, \"for your trouble.\" It is a small thing. But it is freely given, with nothing asked back. So you take it, thank him, and move on.",
},
35: {
"A2": "You can't stop now. But you can't just leave them. So you promise to send help back. \"Hold on!\" you call. \"Get upstairs, stay together. I won't forget you.\" And you mean it. Then you turn and go.",
"B1": "You can't stop now — but you can't just leave them, either. So you promise to send help back soon. \"Hold on!\" you shout. \"Get upstairs, stay together — I won't forget you.\" You mean it, too. And then you turn and go.",
"B2": "You can't stop now. But you can't simply leave them, either. So you promise to send help back as soon as you can. \"Hold on!\" you shout over the rain. \"Get upstairs, stay together — I won't forget you.\" You mean every word of it. And then you make yourself turn and go.",
},
36: {
"A2": "The street builds one strong length of wall first — a solid bank of bags across the worst gap. People crowd to it, passing bags hand to hand. It is not the whole lane saved. But it is a real start, and it holds.",
"B1": "The street builds one strong length of wall first — a solid bank of bags across the worst gap, throwing the water back. People crowd to it, passing bags hand to hand. It isn't the whole lane saved. But it's real, and it holds, and it's a beginning.",
"B2": "The street gets one strong length of wall up first — a solid bank of bags across the worst of the gap, throwing the water back on itself. People crowd in to pass the bags hand to hand down the line. It is not the whole lane saved, not yet. But it is a real wall, and a real beginning, and you can feel the mood turn.",
},
37: {
"A2": "Door by door, the frightened street becomes a working one. Now people have jobs. One fills bags. One carries them. One watches the water. Fear turns into doing. And doing beats waiting every time.",
"B1": "House by house, the frightened street turns into a working one. People have jobs now: one fills bags, one carries them, one watches the water mark. Fear turns into doing. And doing beats waiting, every single time.",
"B2": "House by house, the frightened, sleepy street turns into a working one. People have real jobs now: one fills bags, one carries them down the line, one keeps an eye on the rising water. Fear turns into doing, almost without anyone noticing it happen. And doing beats waiting, every single time, on a night as hard as this one.",
},
38: {
"A2": "The long wet gnaws at your will. A small voice says: stop, go inside, rest. No one would blame you. It would be so easy. But you think of the houses out there. And you push the voice away. Not yet.",
"B1": "The long night gnaws at your will. A small voice says: stop, go inside, rest — no one would blame you, and it would be so easy. But you think of the houses out there, the water at their doors. And you push the voice away. Not yet. Not while they can still be saved.",
"B2": "The long wet gnaws slowly at your will. A small, reasonable voice says: stop now, go inside, rest — no one would blame you, and it would be so easy to do. But then you think of the houses out there, the river already at their doors. And you push the voice firmly away. Not yet. Not while there is still a chance to save them.",
},
39: {
"A2": "You reach the signpost. The flood has knocked it down, and you can barely read it. One arm points along the lane. The other points out to the water's edge. Which way? You will have to guess, and guess right.",
"B1": "You reach the old signpost, but the flood has cracked and half-toppled it. You can barely read it now. One arm points along the lane. The other points out toward the water's edge. Which way? You'll have to guess, and guess right.",
"B2": "You reach the old signpost, but the water has knocked it half down, and you can barely make it out now. One weathered arm points on along the lane. The other points away, out toward the dark water's edge. Which way should you go? You will have to guess — and you will have to guess right.",
},
40: {
"A2": "The dealer turns his wide, easy smile on you. \"Wet work, this,\" he says. \"I have pumps to sell and a strong back to lend. And the street's not really your job tonight, friend.\" His smile never reaches his eyes. You've seen his kind before.",
"B1": "The dealer turns his wide, easy smile on you. \"Wet work, this,\" he says. \"I've pumps to sell, and a strong back to lend — and the street's not really your job tonight, friend.\" His torch swings. His smile never reaches his eyes.",
"B2": "The dealer turns his wide, easy smile on you. \"Wet work, this,\" he says. \"I've pumps to sell, and a strong back to lend — and the street's not really your job tonight, friend.\" His torch swings gently in his hand. His smile never quite reaches his eyes. You have seen exactly this kind before.",
},
41: {
"A2": "The offer is a hook, and you feel it set. He leans in close. \"That street's lost already,\" he says, low. \"Let the river take it. There's money in it for you.\" It is a cruel thing to say. And it is meant to work.",
"B1": "The offer is a hook, and you feel it set. He leans in close. \"That street's lost already,\" he says, low. \"Let the river take it — and there's a share in it for you.\" It's a cruel thing to say. And it is meant to work on your fear.",
"B2": "The offer is a hook, and you feel it set in you. He leans in close. \"That street's lost already,\" he says, low and easy. \"Let the river do its work — and there's a good share in it for you.\" It is a cruel thing to say to you tonight. And every word of it is meant to work on your fear.",
},
42: {
"A2": "You turn your back and leave him to his cold trade. It feels good to walk away. He calls after you. You don't turn round. His kind always finds someone. But it won't be you tonight.",
"B1": "You turn your back on him and leave him to his cold trade. It feels good to walk away. He calls after you, but you don't turn round. His kind always finds someone, in the end. But it won't be you, not tonight.",
"B2": "You turn your back on him and leave him to the dark and his cold trade. It feels good to walk away from it. He calls after you, but you don't turn round. His kind always finds someone, in the end — a frightened person, a bad night. But it won't be you, and it won't be tonight.",
},
43: {
"A2": "You take his pump and his deal. Your hands close on them. And something in you already knows. His smile widens. \"Wise,\" he says. But it does not feel wise. It feels like a door shutting.",
"B1": "You take his pump and his deal. Your hands close on them, and something in you already knows. His smile widens. \"Wise,\" he says. But it doesn't feel wise at all. It feels like a door quietly shutting.",
"B2": "You take his pump and his money, and your hands close on them before your head can argue. Something in you already knows. His smile widens. \"Wise,\" he says. But it doesn't feel wise at all. It feels, if anything, like a door shutting somewhere behind you. You cannot take it back now.",
},
44: {
"A2": "You ask him straight. What does he really want? Why should the street flood? He smiles and looks away. \"Houses come cheap after a flood,\" he says. \"A night like this is a kindness — to a buyer.\"",
"B1": "You ask him straight: what does he really want, and why should the street go under? He smiles and looks off down the lane. \"Houses come cheap after a flood,\" he says. \"A night like this is a kindness — to a buyer like me.\"",
"B2": "You ask him straight out: what is it he really wants, and why should the street be left to flood? He smiles and looks off down the dark lane. \"Houses come cheap after a flood,\" he says, unhurried. \"A night like this one is a real kindness — to a buyer like me.\"",
},
45: {
"A2": "You carry his bags out to the wall. But when you stack them, the sand runs straight out. The sacks are split and rotten. They won't hold water at all. The line sags low and useless.",
"B1": "You carry his bags out to the wall. But as you stack them, the sand runs straight out. The sacks are split and rotten — they won't hold the water at all. The line sags low and useless.",
"B2": "You carry his bags out to the wall and start to stack them. But the moment you set them down, the sand runs straight out through the sacking. The bags are split and rotten, sold to make a quick pound — they will not hold the water at all. Down the lane, the line sags low and useless.",
},
46: {
"A2": "You open a bag, and your heart sinks. The sacking is split and rotten. These bags will never hold water. You paid good money for them, and they are worthless. The doubt in your gut was right.",
"B1": "You open one of the bags, and your heart sinks. The sacking is split and rotten through. These bags will never hold the water. You paid good money for them, and they're worthless. The doubt in your gut was right all along.",
"B2": "You open one of the bags, and the truth of it hits you — the sacking is split and rotten, half the sand gone already. These bags will never hold the water; not one of them will stand in the wall. You paid good money for them, and they are worthless. The doubt in your gut, it turns out, was right all along.",
},
47: {
"A2": "You look for him, but the dealer's van is already gone, off down the lane. He was never helping you. He was waiting for the flood, the ruined homes, the cheap land after. You were fooled.",
"B1": "You look for him, but the dealer's van is already gone, off down the lane. He was never helping you at all. He was waiting for the flood, the ruined homes, the cheap land after. You were fooled, plain and simple.",
"B2": "You look for him, but the dealer's van is already gone, its lights bobbing away down the lane. He was never helping you at all, not for a moment. He was only waiting for the flood, the ruined street, and the cheap land that comes after a bad night. You were fooled, plain and simple.",
},
48: {
"A2": "He is gone, the lane empty. There is only the rain now, and the dark, and what you gave him for nothing. You learned a hard lesson. And you paid far too much for it. Now you go on with less.",
"B1": "He's gone, and the lane is empty — only the rain now, the dark, and what you handed him for nothing. You learned a hard lesson tonight. And you paid far too much for it. Now you go on with less than you started.",
"B2": "He is gone, and the lane is empty — only the rain now, the dark, and the thought of what you handed him for nothing at all. You learned a hard lesson tonight, about who smiles and why. And you paid far too much for the learning. Now you have to go on with less than you started with.",
},
49: {
"A2": "The frightened people press their money on him. Hands full of coins, voices begging for a pump. And he takes it, slow, with that smile. He chooses who to help by who pays most.",
"B1": "The frightened folk press their money on him. Hands full of coins, voices begging for a pump. He takes it slow, with that same smile. He chooses who to help by who can pay the most.",
"B2": "The frightened folk press their coins on him. Hands full of money, voices begging for a pump, for any way through the night. He takes it slow and easy, with that same smile. He chooses who to help and who to pass by. And he chooses by who can pay the most.",
},
50: {
"A2": "Far out on the planks, the far houses seem nearer at last. Or do they? You can't be sure now. The dark plays tricks. Your tired eyes play tricks. And you are a long way from either side.",
"B1": "Far out on the bridge, the far houses seem nearer at last — or do they? You can't be sure any more. The dark plays tricks, and so do your tired eyes. And you're a long way now from either bank.",
"B2": "Far out on the bridge, the far houses seem a little nearer at last — or do they? You can't be sure of anything any more. The dark plays tricks on you, and so do your cold, tired eyes. And you are a long way out now, a long way from either bank.",
},
51: {
"A2": "The planks, the dark, the race below — and a board breaks under your foot. This is the moment. Go down into the fast water. Or throw yourself back from the gap, while you still can.",
"B1": "The planks, the dark, the deep race below — and a board cracks under your foot. This is the moment. You can go down into the fast water. Or you can throw yourself back from the gap, while you still can.",
"B2": "The planks, the dark, the deep black race below — and a board cracks out from under your foot with a sound like a shot. This is the moment, and there is no other. You can go down into the fast water. Or you can throw yourself back from the gap, right now, while you still can.",
},
52: {
"A2": "You reach the far houses at last, soaked and shaking, your hands torn — but across. Somehow, you made it. Now you must decide. Push on, spent as you are. Or face what you lost in the water.",
"B1": "You reach the far houses at last, soaked and shaking, your hands torn raw — but across. Somehow, you made it. Now you have to decide: push on, spent as you are, or face what you lost out in the water.",
"B2": "You reach the far houses at last, soaked and shaking, your hands torn raw on the planks — but down, and across. Somehow, against the odds, you made it. Now you have to decide what comes next: push on, spent as you are, or face what you dropped in the water in the scramble.",
},
53: {
"A2": "You throw yourself back from the gap, while you still can. It is the hard, right choice. You crawl the last stretch on hands and knees. You reach the bank shaken and slow. The night is not lost. But you lost time.",
"B1": "You throw yourself back from the gap while you still can — the hard, right choice. You crawl the last stretch on hands and knees, and reach the bank shaken and slow. The night isn't lost. But it cost you time you'll miss.",
"B2": "You throw yourself back from the gap while you still can — the hard choice, and the right one. You crawl the last stretch on your hands and knees, and reach the bank at last, shaken and slow and soaked through. The night is not lost. But it has cost you time you are going to miss before dawn.",
},
54: {
"A2": "You stack a few bags at their door and start to bail the water with a bucket. It holds back a little. But there is still no lamp to leave them. And the night is far from over.",
"B1": "You stack a low line of bags at their door and bail out the worst of the water with a bucket. It holds back a little of the river. But there's still no lamp to leave them, and the night is far from over.",
"B2": "You stack a low line of bags across their doorway and bail the worst of the water back out with a bucket. It holds a little of the river off, enough to matter. But there is still no lamp to leave them, and the long night is far from over for any of you.",
},
55: {
"A2": "You hand over your own coat and lamp. The family huddle upstairs by the small light. Relief spreads across their faces. The child stops crying at last. \"Thank you,\" the mother says. Then she points you to a light out on the water.",
"B1": "You hand over your own coat and lamp, and the family huddle upstairs round the small flame, relief spreading across their faces. The child stops crying at last. \"Thank you,\" the mother says — and then she points you toward a light, out at the water's edge.",
"B2": "You hand over your own coat and your own lamp, and the family huddle upstairs round the small light, relief spreading slowly across their faces. The child stops crying at last. \"Thank you,\" the mother says, over and over — and then she points you toward something: a light, out at the water's edge, where no one should be.",
},
56: {
"A2": "Without your coat, the cold and wet find you fast. Your teeth chatter. Your fingers go stiff. You gave it away to help, and you would do it again. But the river does not care about that. It just keeps rising.",
"B1": "Without your coat, the cold and wet find you fast — teeth chattering, fingers going stiff. You gave it away to help, and you'd do it again. But the river doesn't care about any of that. It just keeps rising.",
"B2": "Without your coat, the cold and the wet find you fast and deep — teeth chattering, fingers going stiff and clumsy. You gave it away to help someone with less, and you would do it again tomorrow. But the river doesn't care about any of that. It simply keeps rising. You will feel this choice for hours yet.",
},
57: {
"A2": "A stranger waves you into a dry doorway. \"Just a minute,\" they say. \"Get out of the rain. Catch your breath.\" It is warm and dry, and your body begs you to stay. But a minute can turn into an hour.",
"B1": "A stranger waves you into a lit doorway. \"Just a minute,\" they say. \"Out of the rain — catch your breath.\" It's warm and dry, and your whole body begs you to stay. But a minute like this can quietly slide into an hour.",
"B2": "A stranger waves you into a lit, dry doorway. \"Just a minute,\" they say kindly. \"Get out of the rain, catch your breath.\" It is warm and dry inside, and your whole exhausted body begs you to stay. But a minute like this one can quietly slide into an hour, and an hour is more than the houses have.",
},
58: {
"A2": "You press on into the rain, soaked to the bone, the wind fighting every step. Your eyes sting with water. Each step is a small battle. But you keep them coming, one after another.",
"B1": "You press on into the rain, chilled to the bone, the wind fighting every step, your eyes stinging with water. Each step is a small battle on its own. But you keep them coming, one after another, toward the houses.",
"B2": "You press on into the rain, chilled to the bone now, the wind fighting you for every single step, your eyes watering and stinging. Each step is a small battle fought and won on its own. But you keep them coming, one after another after another, toward the waiting houses.",
},
60: {
"A2": "Someone points out toward the water. A figure went that way, alone, into the dark. Out there lies only the flood and the fast, deep race. If no one goes after them, they may not come back.",
"B1": "Someone points out toward the water's edge: a figure has gone out that way, alone, into the dark. Out there lies nothing but the flood and the deep, fast race. If no one goes after them, they may not come back.",
"B2": "Someone points out toward the water's edge: a small figure has gone out that way, alone, into the dark. Out there lies nothing but the rising flood and the deep race where the water runs fastest. If no one goes after them tonight, they may simply not come back at all.",
},
61: {
"A2": "You find them at the water's edge, soaked and lost, the cold tearing at them. They don't seem to know your face. You take a firm hold of their arm. \"Come with me,\" you say. \"You're all right now.\"",
"B1": "You find them out at the water's edge, half-frozen and lost, the cold tearing at them. They don't seem to know your face at all. You take a firm hold of their arm. \"Come with me,\" you say. \"You're all right now. I've got you.\"",
"B2": "You find them out at the water's edge, half-frozen and badly lost, the river tearing at their thin coat. They don't seem to know your face, or quite where they are. You take a firm, steady hold of their arm. \"Come with me,\" you say, as gently as you can. \"You're all right now. I've got you.\"",
},
62: {
"A2": "You can't do everything at once. And the wall needs you most. So you send word for someone else to go after them. Then you press on. It sits badly with you. But you have to choose.",
"B1": "You can't do everything at once, and the wall needs you most of all. So you send word for someone else to go after them, and press on. It sits badly with you — but tonight, you have to choose, and keep choosing.",
"B2": "You can't do everything at once, and the wall is the thing that needs you most of all. So you send word back for someone else to go after them, and you press on into the dark. It sits badly with you, and it will go on sitting badly. But tonight you have to choose, and keep choosing, and live with it.",
},
63: {
"A2": "You walk them safely back to the houses, where their family cries with relief. They wrap you in a dry coat and give you a place by the fire. \"Thank you,\" they keep saying. But you can't stay long.",
"B1": "You walk them safely back to the houses, where their family cries out with relief. They wrap you in a dry coat and make you a place by the fire. \"Thank you,\" they keep saying. But the lane is waiting, and you can't stay long.",
"B2": "You walk them safely back to the lit houses, where their family cries out with relief and pulls them inside. They wrap you in a dry coat and make you a place by the fire. \"Thank you,\" they keep saying, again and again. But the lane is still waiting out there in the rain, and you can't stay long.",
},
64: {
"A2": "You look out over the whole low street — all dark, all rising. The water shines black between the houses. No light shows but the one out on the water. The whole street seems to hold its breath and wait.",
"B1": "You look out over the whole low street — all dark, all rising. The flood shines black between the houses. No light shows anywhere but out at the water's edge. The whole street seems to hold its breath and wait for dawn.",
"B2": "You look out over the whole low street — all dark, all rising, under a sky that will not stop. The flood shines black between the houses, climbing the walls inch by inch. No light shows anywhere but out at the water's edge. The whole street seems to hold its breath, and wait to see what you will do.",
},
65: {
"A2": "The flood rises now to its worst. The water climbs as high as it will go, and your breath comes short in the cold. It is hard to think, hard to move, hard to care. This is the hardest hour of the night.",
"B1": "The flood deepens to its very worst now. The water climbs as high as it will go, and your breath hangs white in the cold, wet air. It's hard to think, hard to move, hard to care. This is the hardest hour of the whole night.",
"B2": "The flood deepens now to its very worst. The water climbs as high as it will go, and your breath hangs white in the cold, wet air. It is hard to think, hard to move, hard even to care. This is the hardest hour of the whole long night — the hour when the river does its real damage.",
},
67: {
"A2": "Tom presses the last good torch on you. \"For the lane,\" he says. \"Go on. I'll stay by the phone.\" His face is grey with worry. This is the help he has to give. And he gives it gladly.",
"B1": "Tom presses the last good torch on you. \"For the lane,\" he says. \"Go on — I'll stay here by the phone.\" His face is grey with worry. This is the help he has to give tonight, and he gives all of it gladly.",
"B2": "Tom presses the last good torch into your hands. \"For the lane,\" he says. \"Go on — I'll stay here by the phone and raise what hands I can.\" His face is grey with worry under the lamplight. This is the help he has to give tonight, and he gives every bit of it gladly.",
},
68: {
"A2": "At the yard, people are rushing the bags. Voices rise, hands grab, fear spreads fast. One more shove and it turns into a fight. You can try to calm them and share the bags out. Or you can grab yours and go.",
"B1": "At the yard store, people are rushing the bags — voices rising, hands grabbing, fear catching and spreading fast. One more shove and it's a fight. You can try to calm them and share the bags out fairly. Or you can just grab yours and go.",
"B2": "At the yard store, people are rushing the pallets — voices rising, hands grabbing, fear catching and spreading fast through the crowd. One more hard shove and the whole thing turns into a fight. You can try to calm them down and share the bags out fairly. Or you can just grab what you came for and go.",
},
69: {
"A2": "A dark, shut-up house presses in around you. There is damp, silence, old cold. Nothing seems alive in here. Then you hear it. Breathing, weak and close, from the back room. Someone is alive after all.",
"B1": "A shut-up house presses in around you — damp, silence, old cold, a place where nothing seems left alive. Then you hear it: breathing, weak and close, from the back room. Someone is alive in here after all.",
"B2": "A long-shut house presses in around you — damp, deep silence, old cold, a place where nothing seems left alive at all. Then you hear it, and you go still: breathing, weak and close, coming from the back room. Someone is alive in here after all, right now, needing you.",
},
70: {
"A2": "Far out at the water's edge, a small light shows and hides. It is out where no one should be tonight. It appears, then is gone, then appears again. No one can say what it is. Something in you wants to go and see.",
"B1": "Far out at the water's edge, a small light lifts and fades. It's out where no one should be tonight — showing, then gone, then showing again. No one can explain it. And something in you wants to go and answer it.",
"B2": "Far out at the water's edge, a small light lifts and fades and lifts again. It is out where no one should be on a night like this — showing, then hidden, then showing once more in the dark. No one can explain it to you. And something in you, against all sense, wants to go and answer it.",
},
71: {
"A2": "You get out to the water's edge and call into the dark. Only the rain answers. Then you see it: a small shape, down by the flood, half in the water. Someone is out here. And they are not moving much.",
"B1": "You get out to the water's edge and call into the dark. No answer comes but the rain. Then you see it: a small shape, down by the flood, half-hidden in the dark water. Someone is out here after all. And they are barely moving.",
"B2": "You get out to the water's edge and call into the dark. No answer comes back but the rain and the river. Then you see it, low by the flood: a small, still shape, half in the black water. Someone is out here after all, on the worst night of the year. And they are barely moving at all.",
},
72: {
"A2": "You reach them, and your heart turns over. It is a child — Wren — curled by the water, soaked and barely awake. The cold has them. There is no time to wait. You have to act now.",
"B1": "You reach them, and your heart turns over. It's a child — Wren — curled by the flood, soaked and half-frozen and barely awake. The cold has them in its grip. There's no time to wait and think. You have to do something now.",
"B2": "You reach them, and your heart turns right over. It is a child — Wren — curled small by the flood, soaked through and barely awake. The cold has them fully in its grip now. There is no time to wait, no time to think it through. You have to do something, and you have to do it now.",
},
73: {
"A2": "You call again into the dark. For a moment, nothing. Then a thin voice comes back: \"Here. Out here.\" Someone is out by the water, and they need you. And they do not sound strong.",
"B1": "You call again into the dark, and for a moment there's nothing. Then a thin voice comes back, torn by the cold: \"Here! Out here!\" Someone is out by the water, and they need help. And they don't sound strong at all.",
"B2": "You call again into the dark, and for a long moment there is nothing at all. Then a thin voice comes back, small and torn by the cold: \"Here! Out here!\" Someone is out by the water, and they need help badly. And from the sound of them, they do not have long.",
},
74: {
"A2": "You get Wren up out of the water and wrap them in your coat. Slowly they come round, gripping your arm. \"The wall,\" they say. \"Keep the wall up. The houses...\" Even now, soaked through, they are thinking of the street.",
"B1": "You get Wren up out of the water and wrap them tight in your coat. Slowly they come round, gripping your arm. \"The wall,\" they whisper. \"Keep the wall up. The houses...\" Even now, half-frozen, they are thinking of the street.",
"B2": "You get Wren up out of the water and wrap them tight in your own coat. Slowly, slowly, they come round, gripping your arm with cold fingers. \"The wall,\" they whisper. \"Keep the wall up. The houses...\" Even now, half-frozen in the dark, this child is thinking of the street and its homes.",
},
75: {
"A2": "You turn to run for help — then stop. There is no help out here. Not till morning. No crew, no one coming. It is you or no one, and Wren knows it too. Their eyes follow you in the dark.",
"B1": "You turn to run for help — then stop short. There is no help out here, not till morning. No crew, no neighbours, no one coming. It's you or no one, and Wren knows it too. Their frightened eyes follow you in the dark.",
"B2": "You turn to run for help — and then you stop short. There is no help to be had out here, not till morning comes. No crew, no neighbours, no one coming at all. It is you or it is no one, and Wren knows it too. Their frightened eyes follow you in the dark, and you cannot leave them.",
},
76: {
"A2": "Wren looks up, their eyes clearer now. \"The old lady — Nora,\" they say. \"That's my gran. We don't speak. Not since Dad and her fell out. It's a long story.\" You hear the sadness in it.",
"B1": "Wren looks up at you, their eyes clearer now. \"The old lady, Nora — that's my gran,\" they say. \"We haven't spoken in years. Not since my dad and her fell out. It's a long, sad story.\" And you can hear just how long it is.",
"B2": "Wren looks up at you, their eyes clearer now. \"The old lady, Nora — that's my gran,\" they say. \"We haven't spoken in years, none of us. Not since my dad and her fell out, back when I was small. It's a long story, and a sad one.\" And in the way they say it, you can hear just how long and how sad.",
},
77: {
"A2": "You decide to get them face to face before dawn. Wren and old Nora, after all these years. It is a small thing, next to the wall and the flood. But it is not nothing. Some doors can still open.",
"B1": "You decide to get them face to face before the night is out — Wren and old Nora, after all these years. It's a small thing, next to the wall and the flood. But it isn't nothing. Some shut doors can still be opened.",
"B2": "You decide, there and then, to get them face to face before the night is out — Wren and old Nora, after all these silent years. It is a small thing, you know, set beside the wall and the rising flood. But it is not nothing. Some doors, even long-shut ones, can still be opened if someone tries.",
},
78: {
"A2": "The small shape isn't moving, and the water is creeping toward it, cold and slow. And yet someone came out here, into the dark, alone. You can't just leave them. You have to know who it is.",
"B1": "The small shape isn't moving, and the flood is creeping toward it, cold and patient. And yet someone came all the way out here, into the dark, alone. You can't just leave them lying there. You have to go closer and know who it is.",
"B2": "The small shape isn't moving at all, and the flood is creeping toward it, cold and slow and patient. And yet someone came all the way out here, into the dark and the deep water, alone. You cannot just leave them lying there by the river. You have to go closer, now, and know who it is.",
},
79: {
"A2": "You go closer, and you know them. It is Wren — old Nora's grandchild, not seen here in years, not since the family fell out. Then a weak sound comes from the water. You move fast.",
"B1": "You go closer, and you know them at once. It's Wren — old Nora's grandchild, not seen here in years, not since the family fell out. Then a weak sound comes from the water at your feet. You move fast now.",
"B2": "You go closer, and you know them at once. It is Wren — old Nora's own grandchild, not seen anywhere near here in years, not since the whole family fell out and went silent. Then a weak sound comes from the water at your feet. You stop thinking, and you move fast.",
},
80: {
"A2": "The dealer comes up one last time, his torch swinging. \"Still fighting it?\" he says. \"Let the river have it. Last chance to be on the winning side, friend.\" The same smile. The same old lie.",
"B1": "The dealer comes up one last time, his torch swinging. \"Still fighting it?\" he says. \"Let the river have it. Last chance to be on the winning side, friend.\" The same easy smile. The same old lie.",
"B2": "The dealer comes up one last time, his torch swinging gently in his hand. \"Still fighting it?\" he says. \"Let the river have the lot. Last chance to be on the winning side, friend.\" It is the same easy smile as before. And it is the same old lie underneath.",
},
90: {
"A2": "You are back at the lane, soaked through, the worst of the flood pressing on everything. By the back step, Nora lies grey and still. Along the lane, the wall is low and leaking. This is the hour it all turns on.",
"B1": "You're back at the lane, soaked through, the hardest hour of the flood pressing down on everything. By the back step, Nora lies grey and still. Along the lane, the wall is low and starting to leak. This is the hour the whole night turns on.",
"B2": "You're back at the lane at last, soaked through, with the worst of the flood pressing down on everything. By the back step, old Nora lies grey and far too still. Along the lane, the wall is low and beginning to leak at its weakest points. This is the hour, you understand, that the whole night turns on.",
},
91: {
"A2": "You reach the wall: the line low, the far end leaking badly. Out by the far houses, the river is close to coming over. You have to get the wall solid and high again. And you have to do it now.",
"B1": "You reach the wall: the line low, the far end leaking badly. Out by the far houses, the river is close to coming over for good. You have to get the wall solid and high again — and you have to do it now, fast.",
"B2": "You reach the wall at last: the line low, the far end leaking badly where the sand has washed through. Out by the far houses, the river is close to coming over the top for good. You have to get the wall solid and high again, all down the line. And you have to do it now, before the water finishes what it started.",
},
92: {
"A2": "Then help reaches you — more hands, more bags, steady people who know the work. You are not alone now. Others are here to share the weight. It is like setting down something heavy you carried too long.",
"B1": "Then help reaches you at last — more hands, more bags, steady people who know the work. You aren't alone with this now; others are here to share the weight. It's like setting down something heavy you've carried far too long.",
"B2": "Then help reaches you at last — more hands, more bags, steady people who know this work in their sleep. You are not alone with it any more; others are here now to share the weight of it. It is like setting down something heavy that you have been carrying, alone, for far too long.",
},
93: {
"A2": "Now you hold the wall — and what you can do depends on what you carried out here. With proper bags, you have plenty to work with. Without them, you must fight for every inch by hand. Either way, the night is far from over.",
"B1": "Now you keep the wall holding — and what you can do depends on what you carried out here. With proper bags, you've plenty to work with. Without them, you must fight for every inch by hand. Either way, the night is far from over.",
"B2": "Now comes the real work: holding the wall until the river turns. What you can do depends entirely on what you carried out here with you. With proper bags, you have plenty to work with down the lane. Without them, you must fight for every inch by hand. Either way, the night is still far from over.",
},
94: {
"A2": "You go down to check on Nora. Her eyes open a little. There is fear in them — then, seeing you, a little less. \"You held it,\" she whispers. \"That I did,\" you say. \"Now rest.\"",
"B1": "You go down to check on Nora, and her eyes open just a little. There's fear in them — then, seeing your face, a little less fear. \"You held it,\" she whispers. \"That I did,\" you tell her softly. \"Now rest.\"",
"B2": "You go down to check on Nora, and her eyes open just a little at your step. There is fear in them at first — and then, seeing your face above her, a little less of it. \"You held it,\" she whispers, barely a sound. \"That I did,\" you tell her softly. \"Now rest. Leave the rest to me.\"",
},
95: {
"A2": "The good bags do it. You build the line up and pack it tight. Down the lane the wall rises solid and strong. The river throws itself at it and is held. This, you think, is what the whole night was for.",
"B1": "The good bags do it. You build the line up and pack it tight, and one by one the gaps close down the lane. The river throws itself at the wall and is held. This, you think, is what the whole hard night was for.",
"B2": "The good bags do it, in the end. You build the line up and pack it tight, and one by one the weak points close the whole length of the lane. The river throws its weight at the wall and is held back. This, you think, standing in the rain, is what the whole long night was for.",
},
96: {
"A2": "You have no proper bags, so you fight for every inch by hand. You pack mud and sand into the gaps with your own arms. You hold the line with your body, your breath, your will. It may not be enough. But you will not let it go.",
"B1": "You've no proper bags to build with, so you fight for every inch by hand. You pack mud and sand into the gaps, holding the line with your own body, breath, and will. It may not be enough. But you won't let it go without a fight.",
"B2": "You have no proper bags to build with, so you fight for every inch of the line by hand. You pack mud and sand into the gaps, shoring up the weak points with your own body, your breath, your sheer will. It holds low and uncertain. It may not be enough to save the houses. But you will not let it go without a fight.",
},
97: {
"A2": "The wall is low and leaking, and you are afraid that holding it alone won't be enough. You have done all you can with what you have. But it may not hold. You need more now — more bags, more hands, or both.",
"B1": "The wall is low and leaking, and you're afraid that holding it alone won't be enough. You've done all you can with what you have. But it may still not hold. You need more now — more bags, more hands, or both.",
"B2": "The wall is low and leaking, and you are afraid that holding it with your own two hands alone will not be enough. You have done everything you can with what little you have. But it may still not hold until the river turns. You need more now — more bags, more hands, or both, and quickly.",
},
98: {
"A2": "You glance out and see it. Far out at the water's edge, a light flares and falls. It is out where no one should be. It shows, hides, and shows again. It pulls at your eye. And at something deeper.",
"B1": "You glance out and see it. Far out at the water's edge, a light flares and falls — out where no one should be, showing and hiding and showing again. It pulls at your eye. And it pulls at something deeper than that.",
"B2": "You glance out across the lane and see it. Far out at the water's edge, a light flares and falls and flares again — out where no one should be on a night like this, showing and hiding in the dark. It pulls at your eye. And it pulls at something deeper and harder to name.",
},
99: {
"A2": "The light out on the water shows again. It is where everyone says no one would be. But a light means a hand to make it. And a hand means a person. A person out there, alone, in this flood.",
"B1": "The light out on the water shows again — out where everyone swears no one would be. But a light means a hand to light it, and a hand means a person. A person out there, alone, in a flood like this one.",
"B2": "The light out on the water shows again — out where everyone swears no one would be tonight. But a light means a hand to make it, and a hand means a person. A person out there, alone, in a rising flood like this one. You can't quite let it go.",
},
100: {
"A2": "Now comes the long hold. You keep the wall packed. You keep Nora warm. You watch the water, hour by hour. It is not exciting. It is just steady, hard, careful work. And it is the whole job tonight.",
"B1": "Now comes the long hold: you keep the wall packed, keep Nora warm, and watch the water hour by hour. It isn't exciting — just steady, hard, careful work. But it is the whole job tonight, and it is yours.",
"B2": "Now comes the long hold: you keep the wall packed and solid, keep Nora warm and breathing, and watch the water climb and ease hour by hour. It isn't exciting work — just steady, hard, careful work, done over and over. But it is the whole job tonight. And tonight it is yours alone.",
},
101: {
"A2": "And then, at last, it turns. The river stops climbing. It holds, then drops an inch, then another. The first thin light comes up over the roofs. The flood is losing. You have nearly held the whole night.",
"B1": "And then, at last, it turns. The river stops climbing. It holds, then drops an inch, then another. The sky greys over the roofs, and the first thin light comes. The flood is losing. You have nearly held the whole night.",
"B2": "And then, at last, it turns. The river stops its climbing. It holds for a long moment, then drops an inch, then another. The sky greys at the edge of the roofs, and the first thin light of the day comes creeping up. The flood is losing its hold at last. You have very nearly held the whole long night.",
},
102: {
"A2": "This is the worst hour — the one just before the break. The river has not dropped yet. Your arms ache. Your eyes burn. But you can feel the night starting to turn. Hold on a little longer.",
"B1": "This is the worst hour, the one just before the break. The river hasn't dropped yet; your arms ache, your eyes burn. But you can feel the night beginning to turn, somewhere underneath it all. Hold on a little longer.",
"B2": "This is the worst hour of all, the one just before the break. The river has not dropped yet; your arms ache from the bags, your eyes burn in the dark. But you can feel the night beginning to turn, somewhere underneath the water. Just hold on a little longer now.",
},
103: {
"A2": "Along the lane you see them — torches, dark figures moving, walls of bags holding the water. Other people, out in the flood with you. The street got through this night as well. You were never quite as alone as you felt.",
"B1": "Along the lane you see them — torches, dark figures moving, walls of bags holding against the flood. Other people, out in the rain with you. The street got through this night as well. You were never quite as alone as you felt.",
"B2": "Along the lane you see them now — torches, dark figures moving slowly, walls of bags holding the water back. Other people, out in the flood all night, same as you. The whole street got through this night as well. And you were never quite as alone in it as you felt.",
},
104: {
"A2": "At last, help comes up the lane — a truck, more hands, more bags, real help at real speed. You lean on a wall and watch it come. Your legs shake under you now. But the worst of the night is behind you.",
"B1": "At last, help comes up the lane — a truck, more hands, more bags, real help at real speed. You lean on the wall and watch it come, your legs shaking under you now. But the worst of the night is behind you.",
"B2": "At last, help comes up the lane — a truck, more hands, more bags, real help arriving at real speed. You lean on the wall and watch it come on, your legs shaking under you now that you can let them. But the worst of the night is well behind you now.",
},
105: {
"A2": "Dawn comes up over the street, the light turning grey, then pale and clean. The rain eases at last, and the river drops back. The houses are still there, still dry inside. The worst has passed at last.",
"B1": "Dawn comes up over the street, the light turning grey, then pale and clean. The rain eases at last, and the river slides back down the bank. The houses are still standing, still dry inside. The worst has passed at last.",
"B2": "Dawn comes up over the street, the light turning grey, then pale, then clean. The rain eases off at last, and the river slides back down the bank inch by inch. The houses are still standing, still dry inside their doors. The worst of it has passed at last. You can hardly believe you made it through.",
},
106: {
"A2": "Then it comes — the first bird of the morning. It sings over the wet roofs as if there had been no flood at all. After the night you have had, it seems almost absurd. And it is beautiful.",
"B1": "Then it comes — the first bird of the morning, singing over the wet roofs as if there'd been no flood at all. After the night you've had, it seems almost absurd. And it is beautiful, and you stop to listen.",
"B2": "Then it comes — the first bird of the morning, singing out over the wet roofs as if there had been no flood, no fear, no long dark night at all. After the night you have had, it seems almost absurd. And it is beautiful, and you stop a moment just to listen.",
},
107: {
"A2": "From the lane you watch the water, where a light lifts and falls and slowly grows. Something is coming at last, too far yet to make out. But a light means someone. And someone is better than no one tonight.",
"B1": "From the lane you watch the water's edge, where a light lifts and falls and slowly grows. Something's coming at last, still too far off to make out. But a light means someone out there — and someone is far better than no one tonight.",
"B2": "From the lane you watch the water's edge, where a light lifts and falls in the dark and slowly, slowly grows. Something is coming at last, still too far off to make out clearly. But a light means a hand, and a hand means someone — and someone is far better than no one, on a night like this.",
},
110: {
"A2": "First light comes at last. Now the night adds up to what it is. Whatever you did out there, in the rain, comes home now. Some of it to be proud of. Some of it not. Let's see what it came to.",
"B1": "First light comes at last, and the night adds up to what it is. Whatever you did out there in the rain comes home to you now — some of it to be proud of, some of it not. Let's see, then, what it all came to.",
"B2": "First light comes at last, and the night adds up to exactly what it is. Whatever you did out there in the rain and the dark comes home to you now — some of it to be proud of, some of it not so much. Let's see, then, what the whole long night finally came to.",
},
111: {
"A2": "The night adds up — not with one big act, but with many small ones. What you held. What you refused. Who you went out for. It all counts in the end. It all made the night what it was.",
"B1": "The night adds up — not always with one big act, but with many small ones. What you held, what you refused, who you went out into the rain for. It all counts in the end. It all made the night what it was.",
"B2": "The night adds up — not with one single grand act, but with many small ones laid end to end. What you held, what you refused, who you went out into the rain for. It all counts in the end, every last piece of it. And it all made the night exactly what it was.",
},
112: {
"A2": "There is more to weigh. The night held other things too. A stranger you stopped for. A coat and a lamp you gave away with an open hand. Small choices, made in the rain, when it was easier to pass by.",
"B1": "There's more to weigh; the night held other things too. A stranger you stopped for. A coat and a lamp you gave away with an open hand. Small choices, made in the rain, when it would have been easier to pass by.",
"B2": "There is more to weigh; the night held other things too. A stranger you stopped for when you had no time. A coat and a lamp you gave away with an open hand. Small choices, made out in the rain, when it would have been far easier to pass them by.",
},
113: {
"A2": "And what does the night leave you? Maybe not a clean win. Maybe just this: that you went out, that you tried. When it was dark and wet and easy to stay in, you didn't. That counts for something.",
"B1": "And what does the night leave you with? Maybe not a clean win. Maybe just the fact that you went out, that you tried. When it was dark and wet and easy to bar the door, you didn't. That counts for something.",
"B2": "And what does the night leave you with, in the end? Maybe not a clean win at all. Maybe just the plain fact that you went out, that you tried. When it was dark and wet and so easy to bar the door and stay in, you didn't. And that counts for something.",
},
114: {
"A2": "But not every night ends well. Some choices cost more than you knew. Some doors, once opened, can't be shut again. This is the hard end of the night. This is where the worst comes home.",
"B1": "But not every night ends well. Some choices cost more than you knew at the time; some doors, once opened, can't be shut again. This is the hard end of the night — the place where the worst of it comes home.",
"B2": "But not every night ends well. Some choices cost far more than you knew at the time; some doors, once opened, cannot be shut again. This is the hard end of the night — the place where the worst of what you did, or didn't do, comes home to you. Some of it cannot be undone now.",
},
120: {
"A2": "You held the wall down the lane all night. At first light the river drops back and the rain stops. Every house is still dry inside. A whole row of homes is safe. And it is safe because you stayed out in the rain.",
"B1": "You held the wall down the lane all night. At first light the river drops back, the rain stops, and the houses — a whole row of homes — come through dry. It all came through because you stayed out in the rain and would not let the wall fail. That's the whole of it.",
"B2": "You held the wall down the lane all night long. At first light the river drops back down the bank, the rain stops, and the houses — and with them a whole row of homes — come through dry and whole. It all came through because you stayed out in the rain and would not let the wall fail. That is the whole of it, and it is enough.",
},
121: {
"A2": "You answered the light no one could explain. You found Wren, lost and cold by the water, and got them warm in time. And there was more. Wren is Nora's grandchild. A door shut for years opens again, at dawn.",
"B1": "You answered the light no one could explain. You found Wren lost and cold by the water, and got them warm just in time. And there was more than one life saved. Wren is Nora's grandchild. A door shut for years is opening again, there in the grey dawn.",
"B2": "You answered the light no one could explain, out at the water's edge. You found Wren lost and cold by the flood, and got them warm just in time. And there was more than one life saved out there. Wren is Nora's own grandchild, estranged for years. And a door that both sides thought shut for good is quietly opening again, there in the grey light of dawn.",
},
122: {
"A2": "There was no single brave act. There was something better. You turned a sleeping street into people with bags down every door. Together, they brought the night through. No one was left alone in it. That is what a street can be.",
"B1": "There was no single brave act — there was something better than that. You turned a sleeping street into people with bags down every door, and together they brought the whole night through. No one was left alone in it. That, in the end, is what a street can be.",
"B2": "There was no single brave act to point to — there was something better than that. You turned a sleeping, frightened street into people with bags down every door, and together, all of you brought the whole night through. No one was left alone in it. That, in the end, is what a street can be for.",
},
123: {
"A2": "You refused the con. You saw the dealer's trick and turned your back on it. You kept your head, and saved what you could by decent means. It was not perfect. But it was clean, and honest, and enough.",
"B1": "You refused the con — saw the dealer's trick for what it was and turned your back on it. You kept your head, and saved what you could by decent, honest means. It wasn't a perfect night; you didn't save everyone. But you did it clean, and clean is enough.",
"B2": "You refused the con — you saw the dealer's trick for exactly what it was and turned your back on it. You kept your head through the worst of it, and saved what you could by decent, honest means. It was not a perfect night, and you did not save everyone. But you did it clean. And clean, in the end, is enough.",
},
124: {
"A2": "You fell short of the whole street. But the neighbour you stopped for comes back now. They help you save the near houses and get Nora warm. It is not the full win. But a kindness, it turns out, comes back around.",
"B1": "You fell short of the whole street. But the neighbour you stopped for earlier comes back now. They help you save the near houses and get Nora warm. It isn't the full win. But a kindness, it turns out, doesn't stay where you leave it. It comes back around.",
"B2": "You fell short of saving the whole street — but the neighbour you stopped for earlier comes back now, when it matters, and helps you save the near houses and get Nora warm. It is not the full win you wanted. But a kindness, it turns out, does not stay where you leave it. It comes back around.",
},
125: {
"A2": "You gave your own coat and lamp away to those with less. Now you end the night cold yourself. You did not save everything. But you are not alone, and nor is anyone you met. Something in the street has shifted. It is a start, not a save.",
"B1": "You gave your own coat and lamp away to those with less, and you end the night cold yourself. You didn't save everything. But you're not alone, and neither is anyone you met out there. Something in the street has quietly shifted. It's a start, not a save.",
"B2": "You gave your own coat and lamp away to people who had less, and you end the night cold and worn through yourself. You did not save everything. But you are not alone, and neither is anyone you met out there in the dark. Something in the street has quietly shifted tonight. It is a start, not a save — and starts matter.",
},
126: {
"A2": "You scrape through the worst of it. The river turns at last, and a thin dawn saves most of the street. It is no triumph, and no one will sing about it. But you got through the night. And that is a relief all its own.",
"B1": "You scrape through the worst of it. The river turns at last, and a thin dawn finds most of the street still dry. It's no triumph, and no one will sing about it. But you got through the night — and in the end, that is a relief all of its own.",
"B2": "You scrape through the worst of it, only just. The river turns at last, and a thin, grudging dawn finds most of the street still dry. It is no triumph, and no one will sing about it. But you got through the night — and in the end, that is a relief all of its own.",
},
127: {
"A2": "You didn't save it all. But the street saw you out by the water when others stayed in bed. They saw you try, on the worst night of the year. From tonight, you are someone this place knows. That is not nothing.",
"B1": "You didn't save it all. But the street saw you out by the water when others stayed in bed — saw you try, on the worst night of the year. From tonight, you're someone this place knows. And that is not nothing.",
"B2": "You didn't manage to save it all, far from it. But the whole street saw you out by the water when others stayed warm in bed — saw you try, on the worst night of the year. From tonight, you are someone this place knows and nods to. And that, in the end, is not nothing at all.",
},
128: {
"A2": "You took the dealer's deal. By morning the street is no longer Nora's to save. The river did the rest. The cheque in your hand is cold. So is the water at the door. You will not forget how you earned it.",
"B1": "You took the dealer's deal, and by morning the street is no longer Nora's to save. The river did the rest. The cheque in your pocket is cold, and so is the water at the door by morning. You won't soon forget how you came to earn it.",
"B2": "You took the dealer's deal, and by morning the street is no longer Nora's to save — it is his, in all but the signing. The river did the rest. The cheque in your pocket is cold, and so is the water standing in the houses by morning. You will not soon forget how you came to earn it.",
},
129: {
"A2": "The weir bridge was a trap, just as Jack Reed warned. You went through it in the dark, and it took the night. You drag yourself out, soaked and shaking, and reach the far houses far too late. The race cost you everything the short cut promised.",
"B1": "The weir bridge was a trap, just as Jack Reed warned. You went through it in the dark, and it took the whole night. You drag yourself out, soaked and shaking, and reach the far houses far too late. The race cost you everything the short cut promised to save.",
"B2": "The weir bridge was a trap, exactly as Jack Reed warned you it would be. You went through it in the dark, and it took the whole night with it. You drag yourself out, soaked and shaking and broken, and reach the far houses far too late to matter. The race cost you everything the short cut ever promised to save.",
},
130: {
"A2": "You spent the night on the wrong things. The wall stayed low too long. By dawn, the river is through every door, and the street is ruined. You did go out into the rain. But you didn't hold the wall when it counted.",
"B1": "You spent the night on the wrong things, and the wall stayed low too long. By dawn, the river is through every door, and the street is ruined. You did go out into the rain. But you didn't hold the wall when it truly counted.",
"B2": "You spent the night on the wrong things, and the wall stayed low too long to matter. By dawn, the river is through every door, and the whole street is ruined with it. You did go out into the rain, and you did try. But you did not hold the wall when it truly counted.",
},
131: {
"A2": "In the end, you stayed inside, where it was warm and dry. You told yourself it wasn't your job. That help would come at dawn. All of it was true. And all night, the wall stayed unbuilt. Nothing bad happened to you. You will think about that for a long time.",
"B1": "In the end, you stayed inside, where it was warm and safe. You told yourself the river was too high, that it wasn't your job, that help would come at dawn. All of that was true. And all night, out in the lane, the wall stayed unbuilt. Nothing bad happened to you. You'll think about that for a long, long time.",
"B2": "In the end, you stayed inside, where it was warm and dry and safe. You told yourself the river was too high, that it wasn't really your job, that help would surely come at dawn. All of that was true. And all night, out in the dark lane, the wall stayed unbuilt. Nothing bad happened to you at all. You will think about that for a long, long time.",
},
}

# --- choice labels per node, in the SAME order as episode-06's choices ---
C = {
1: ["Take charge of the wall.", "Try the phone for help.", "See to Nora first."],
2: ["Step out along the lane.", "Decide how to start.", "The pump won't start."],
3: ["Decide how to start.", "But the water can't wait."],
4: ["Go back and get the wall up.", "Feel how serious this is."],
5: ["Tom opens the yard store.", "Knock along the row for help.", "Decide how to start.", "A light out at the water's edge."],
6: ["The yard store.", "Straight out to the wall.", "Rouse the street for help."],
8: ["Decide how to start.", "To the yard store.", "A scramble at the store."],
9: ["Take charge of the bags and pump.", "Just a torch and a spade.", "Ask Tom what he knows.", "He presses a good torch on you."],
10: ["Stop and help him.", "Say you must hold the wall."],
11: ["Decide how to get real bags.", "The wet takes it out of you."],
12: ["The street turns out.", "No one stirs; go on alone."],
13: ["Now, out to the wall.", "Thank Tom."],
14: ["Now, find real bags.", "Ask Tom what he knows."],
15: ["Take it to heart.", "On with it."],
16: ["On out to the wall.", "He asks you to check the others."],
17: ["Get proper bags first.", "Straight out to the wall."],
18: ["The dealer's van is ahead.", "Push on."],
19: ["Lead them out to the wall.", "Build one strong length first."],
20: ["The yard store.", "On out to the wall."],
21: ["Keep to the lane.", "Take the weir bridge.", "The dealer's van ahead."],
22: ["On the way.", "Back to the store."],
23: ["On with the watch.", "Rouse more hands."],
24: ["Hear him out.", "Go round him."],
25: ["This way.", "A light out at the water's edge."],
26: ["Press on.", "Someone's in trouble ahead.", "The whole low street, dark and rising."],
27: ["Risk the weir bridge.", "Too dangerous — back to the lane."],
28: ["Edge on.", "The planks shift under you."],
29: ["Out along the lane.", "Back to the yard for another pump."],
30: ["A family with water coming in.", "Press on.", "The wet nearly has you.", "A signpost, half down."],
31: ["Help him up.", "You can't stop — the wall."],
32: ["Give them your own lamp and coat.", "Promise to send help.", "Try to block their doorway."],
33: ["The dealer again.", "A light out at the water's edge.", "The last of the watch.", "The wet makes you doubt."],
34: ["On your way.", "He tells you of the light on the water."],
35: ["Rouse the street.", "On through the rain."],
36: ["Get the wall up as well.", "Fetch more hands."],
37: ["To the far houses.", "The last of the watch."],
38: ["The last of the watch.", "The dealer's van."],
39: ["The lane.", "The light on the water."],
40: ["Hear the price.", "Refuse and go round."],
41: ["Take his deal.", "That's the tell — refuse.", "Ask what he really wants.", "The frightened folk press in."],
42: ["On the way.", "To the yard store instead."],
43: ["Carry the bags to the wall.", "A doubt already."],
44: ["That's your answer — refuse.", "Take it anyway."],
45: ["Try to stack them anyway.", "Out to the wall with nothing."],
46: ["Out to the wall.", "Back to have it out with him."],
47: ["Out to the wall, fooled.", "Fling the split bags down."],
48: ["Out to the wall.", "Stand a moment in the dark."],
49: ["Hear the price anyway.", "Refuse and go round."],
50: ["Nearly across.", "The planks crack under you."],
51: ["You go through into the race.", "Throw yourself back while you can."],
52: ["Push on, spent.", "You dropped the bags in the water."],
53: ["The long lane after all.", "Too spent to go on."],
54: ["Give them your own lamp and coat.", "Promise to send help."],
55: ["On, wetter now.", "Ask about the light on the water."],
56: ["Keep moving, keep your head.", "A lit doorway offers a minute."],
57: ["Warm up, then on.", "Refuse, press on."],
58: ["The last of the watch.", "On toward the far houses."],
60: ["Go after them.", "No time — the wall first."],
61: ["Walk them back.", "On to the wall."],
62: ["Decide how to start.", "On toward the far houses."],
63: ["On toward the far houses.", "The last of the watch."],
64: ["On along the lane.", "The light on the water."],
65: ["The family with water coming in.", "Press on."],
67: ["On the way.", "His warning first."],
68: ["Calm it, and share it out.", "Get to the bags."],
69: ["Follow the breathing, and find them.", "It's too much — back to the wall."],
70: ["Go and answer it.", "Leave it — the wall first."],
71: ["Go to them.", "Call again and wait.", "The small shape isn't moving."],
72: ["Get them up and warm.", "Run for help."],
73: ["Go to them.", "Fetch help."],
74: ["Wren speaks of Nora.", "Get you both back."],
75: ["Go back for them.", "To the wall, torn."],
76: ["Resolve to bring them together.", "Up with the news."],
77: ["Back to the lane.", "Get Wren steady first."],
78: ["Go closer.", "You know this child."],
79: ["Follow the sound, and find them.", "The years in it."],
80: ["Take his deal.", "Refuse for good."],
90: ["See to the wall.", "The dealer's last offer.", "Help arrives behind you."],
91: ["Get the wall solid.", "Check on Nora below.", "The sky greys over the roofs."],
92: ["To the wall together.", "Hold the watch.", "A light out on the water."],
93: ["The bags and pump.", "Work with what little you have."],
94: ["Get the wall solid.", "Break out the bags."],
95: ["Hold the watch.", "Help arrives."],
96: ["Hold the watch.", "It may not be enough."],
97: ["Hold on to first light.", "Send for the rallied help."],
98: ["See to the wall first.", "The light nags at you."],
99: ["The wall first.", "Hold the watch."],
100: ["Watch for first light.", "The light on the water still nags.", "The night's worst hour."],
101: ["First light, and what it finds.", "Dawn over the lane."],
102: ["Watch for first light.", "Other lights along the lane."],
103: ["First light.", "Help coming up the lane."],
104: ["First light.", "What the night came to."],
105: ["First light.", "Help reaches you.", "The first bird of the morning."],
106: ["First light.", "Help reaches you."],
107: ["To the wall.", "Hold the watch."],
110: ["The homes held; the wall stood.", "You answered the light, and found Wren.", "Weigh the rest."],
111: ["The whole street came through together.", "You did it clean — no con.", "Weigh the rest."],
112: ["A stranger you helped sees you home.", "You gave your own lamp away.", "Weigh the rest."],
113: ["The water falls at last, late.", "The street saw you out there.", "The worst of it."],
114: ["You took the dealer's deal.", "You were simply too late.", "The water fell before real harm."],
}

def main():
    book = json.load(open(SRC, encoding="utf-8"))
    book["episode"] = 7
    book["series"] = "high-water"
    book["slug"] = "high-water"
    book["title"] = "High Water"
    book["blurb"] = ("The river has been rising for two days, and tonight it comes over the bank "
        "into the low street by the water — just as old Nora Kettle falls at her back step and "
        "cannot get up. Building the sandbag wall down the lane, and holding it, is on you now. "
        "You have until first light to keep the river out of the homes, against a flood that will not stop.")
    book["state_out"] = rf(book["state_out"])
    book["arc_flags"] = []
    book["state_in"] = []

    # rebuild nodes: keep ids/gotos/endings; install our prose; remap flag sets/requires; re-skin choice labels
    for n in book["nodes"]:
        nid = n["id"]
        if nid in P:
            n["text"] = {lvl: P[nid][lvl] for lvl in ("A2", "B1", "B2")}
        labels = C.get(nid, [])
        for i, ch in enumerate(n.get("choices", [])):
            if "sets" in ch: ch["sets"] = rf(ch["sets"])
            if "requires" in ch: ch["requires"] = rf(ch["requires"])
            if i < len(labels):
                lab = labels[i]
                ch["text"] = {"A2": lab, "B1": lab, "B2": lab}

    book["identity"] = {
        "name": "High Water",
        "mood": "A dark town as the river climbs its banks; the only thing between the water and the homes is the wall you build and hold.",
        "palette": {
            "ground": "#0B1A24", "surface": "#12242E", "ink": "#EAF1F4",
            "muted": "#7F93A0", "line": "#203541",
            "accent": "#E8B24A", "accentHot": "#F6C96B", "secondary": "#5FA8C4"
        },
        "cover": {"kind": "highwater", "glow": True},
        "type": {"display": "Fraunces", "ui": "Hanken Grotesk", "mono": "JetBrains Mono"},
        "hero": {
            "line": {
                "en": "The river comes for the houses tonight. Build the wall along the lane and hold it till first light.",
                "fr": "Cette nuit, la rivière vient pour les maisons. Monte le mur le long de la ruelle et tiens-le jusqu'à l'aube.",
                "es": "Esta noche el río viene por las casas. Levanta el muro a lo largo del callejón y manténlo hasta el amanecer.",
                "it": "Stanotte il fiume viene per le case. Costruisci il muro lungo il vicolo e tienilo fino alle prime luci.",
                "de": "Heute Nacht kommt der Fluss für die Häuser. Bau die Mauer entlang der Gasse und halte sie bis zum ersten Licht.",
                "pt": "Esta noite o rio vem pelas casas. Levanta o muro ao longo da viela e segura-o até ao amanhecer.",
                "ru": "Этой ночью река идёт за домами. Выстрой стену вдоль переулка и удержи её до первого света.",
                "zh": "今夜河水要来淹没房屋。沿着巷子垒起沙袋墙，守着它撑到天明。",
                "ar": "الليلة يأتي النهر على البيوت. ابنِ الجدار على امتداد الزقاق وأبقِه صامدًا حتى أول ضوء."
            },
            "sub": "A story where you are the hero — and every choice turns you to a new page. Written for people learning English, at your level, with meaning in your language whenever you need it."
        }
    }
    book["language_focus"] = {
        "A2": ["imperatives and going to", "the rain, the river and the home"],
        "B1": ["the first conditional and modals of advice", "warning, helping and planning"],
        "B2": ["inference, obligation and conditionals", "care, risk and responsibility"]
    }
    book["lexicon"] = {
        "_comment": "High Water's chosen lexicon. Grown in phase 4. Base-keyed; the reader resolves inflections. Translations need a native speaker's check before launch.",
        "entries": {}
    }

    json.dump(book, open(OUT, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    missing = [n["id"] for n in book["nodes"] if n["id"] not in P]
    print("Wrote %s: %d nodes, %d endings. Nodes missing prose: %s" % (
        OUT, len(book["nodes"]), sum(1 for n in book["nodes"] if n.get("ending")),
        missing or "none"))

if __name__ == "__main__":
    main()
