#!/usr/bin/env python3
"""Phase 3 prose for book 6, The Orchard — batch 1 (opening / Act I, nodes 1-16).

Replaces the placeholder stubs with original, in-band three-level prose (A2/B1/B2) and levelised
choice text, keeping the graph (ids, gotos, flags) untouched. Run the validator after; these
nodes must be band-clean (A2 mean<=12 / longest<=18 / 25-90w; B1 <=16/<=25/35-130; B2 <=22/<=35/
50-190). Further batches (Acts II-III) patch the remaining nodes the same way.

Run: python3 scripts/phase3_ep06.py
"""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
EP = os.path.join(ROOT, "content", "episode-06.json")
book = json.load(open(EP, encoding="utf-8"))
nodes = {n["id"]: n for n in book["nodes"]}

# text per node: (A2, B1, B2)
P = {
 1: (
  "It is the coldest night of spring. The cold comes down fast from a clear sky. On every tree the blossom is white and still. Then old Edith Marsh falls on the back steps and cannot get up. The fires along the rows are not lit, and the frost is already here. Keeping the blossom alive is on you now.",
  "It is the coldest night of spring, and the cold comes down fast from a clear, still sky. On every tree the blossom stands white and brittle, a whole year's fruit held on a few degrees. Then old Edith Marsh goes over on the back steps and cannot get up. The fires along the rows are unlit, the frost is already down, and no crew will come before morning. Keeping the blossom alive is on you now.",
  "It is the coldest night of spring, and the cold settles fast out of a clear, still sky. The thermometer slides past freezing, and on every tree the blossom stands white and brittle. A whole year's fruit now hangs on a few degrees of warmth. Then old Edith Marsh, coming down the back steps to start the work, goes over on her bad hip and cannot rise. The smudge-fires along the rows are unlit, the frost is already down, and no crew will come before morning. Keeping the blossom alive — and the orchard that is all Edith has — is suddenly, entirely on you."),
 2: (
  "You gather what the shed holds: oil, matches, a lantern, and dry straw. Outside the air is still and very cold. The frost is already on the grass. You must decide what to do, and do it fast.",
  "You gather what the shed holds: a can of oil, matches, a good lantern, an armful of dry straw. Outside, the air is dead still and bitterly cold. The frost is already creeping white across the grass. You have to decide what to do, and do it quickly.",
  "You gather what the shed will give you: a can of oil, a box of matches, a good lantern, an armful of dry straw for kindling. Outside the air is dead still under a hard, clear sky, and the cold has real teeth now. You can watch the frost creep white across the grass as you stand there. Whatever you choose, you must choose it fast — every minute you spend thinking is a minute the cold is working on the trees."),
 3: (
  "You try the phone. At last Tom's voice comes through from the co-op. No one can come out before morning, he says — not in a frost like this. Light the fires and keep them going, if you can.",
  "You try the phone. It rings and rings, then at last Tom's voice gets through from the co-op. No crew can come out before morning, he says — not in a frost like this one. Light the fires down the rows, he tells you, and keep them going if you possibly can.",
  "You try the phone with cold fingers. It rings and rings into the dark, and then, at last, Tom's steady voice gets through from the co-op. No crew can come out before morning, he tells you plainly; not for a frost that drops this hard and this fast. The only thing that beats a frost is fire by hand — so light the pots down the rows, he says, and keep them going, whatever it takes, until the sun comes up."),
 4: (
  "You go to Edith at the foot of the steps and make her as warm as you can. But the fires are still unlit, and shelter is not enough. The blossom out there needs heat. You need oil, a plan, and a clear head before you start.",
  "You get to Edith at the foot of the steps. You make her as easy and warm as you can. But the rows are still dark and cold. Shelter alone won't do. The blossom out there needs the fires lit. You need oil, a plan, and a clear head before you go out among the trees.",
  "You get to Edith at the foot of the back steps. You make her as easy and as warm as you can, a coat under her head, a blanket over her. But keeping her warm is not the same as keeping the orchard alive. Shelter alone won't save a single tree. The blossom out there needs heat. Heat means fire, and fire means oil, straw, and a clear head. Before you can do any good tonight, you have to decide how to begin."),
 5: (
  "You step out among the rows. The night is huge and still, and the blossom is pale all around you. The cold presses down on everything. Far off, among the end trees, a small light moves where no light should be.",
  "You step out among the rows. The night is huge and dead still, and the pale blossom seems to glow in the dark. The cold presses down on the whole orchard like a hand. Then, far off among the end trees, you catch it: a small light moving, out where no one should be tonight.",
  "You step out among the rows, and the cold takes your breath. The night is huge and dead still, and the pale blossom seems to hold its own faint light in the dark. Over everything the frost presses down like a slow, heavy hand, settling first in the low ground. Then, far off among the trees at the orchard's end, you catch something that stops you: a small light, moving, out where no one in their right mind should be on a night like this."),
 6: (
  "You make yourself think. You could light the fires first, and worry about the rest after. You could see to Edith and the neighbours. Or you could wake the village to help. Each choice costs time — and the frost is working now.",
  "You make yourself stop and think. You could get the fires going first, and worry about everything else after. You could go to Edith and the neighbours instead. Or you could rouse the village and bring more hands. Each choice costs time you don't have — and out in the dark, the frost is already working on the trees.",
  "You make yourself stop and think, though every part of you wants to run. You could get the fires going first and leave the rest for later. You could put people before the trees, and go to Edith and the frightened neighbours. Or you could wake the whole village and turn one pair of hands into twenty. Each path costs time, and time is the one thing the frost will not give you — out there, with every still minute, the cold is sinking deeper into the blossom."),
 8: (
  "The cold settles in your chest like a weight. You think of the blossom — a whole year's fruit, the orchard that is all Edith has. If the fires stay dark, it is lost by dawn. No one else will do this. It is you, tonight, or no one.",
  "The cold settles into your chest like a weight. You think of the blossom out there: a whole year's fruit, the orchard that is all Edith has left. If the fires stay dark much longer, the frost takes every bit of it by dawn. That isn't a fear; it's a plain fact. No one else is coming to climb into this and do it. It is you, tonight, or no one.",
  "The cold settles into your chest like a weight. The size of the night opens up in front of you. You think of the blossom on every branch. It is a whole year's fruit, a whole year's living. The orchard is the last thing keeping Edith on her land. If the fires stay dark much longer, the frost will have all of it by first light. No one will be able to undo that. This is not a fear you can talk yourself out of. It is a fact. And no one else is coming to do it. It is you, tonight, or no one at all."),
 9: (
  "Tom heaves open the fuel store. Inside there is a drum of oil, matches, spare straw, a lantern, and dry sacking. \"Take what you need,\" he says. \"I'll stay by the phone.\" He is a steady man. Tonight it shows.",
  "Tom heaves open the fuel store and holds up the lantern. Inside are a drum of oil, a box of matches, bundles of spare straw, and dry sacking. \"Take what you need,\" he says. \"I'll stay here by the phone and raise who I can.\" He's a steady man, and on a night like this it shows.",
  "Tom heaves open the door of the fuel store and swings the lantern inside. There is a drum of oil, a box of matches, bundles of spare straw, a good storm-lantern, and a roll of dry sacking. \"Take whatever you need,\" he says, no fuss about it. \"I'll stay here by the phone and raise what hands I can.\" He's a steady, unshowy man. He is the kind you only really notice on a night like this. And tonight it shows."),
 10: (
  "You knock along the cottages. Old Mr Hollis opens up, pale in the dark. His stove is dead, his matches gone, his hands shaking. \"I can't get it lit,\" he says. You have a long night ahead. But he is here, and he is scared, and he is asking you.",
  "You knock along the row of cottages, and old Mr Hollis opens up, pale in the cold. His stove has gone out, his matches are finished, and his hands are shaking too hard to strike one. \"I can't get it lit,\" he says. You have a long, hard night ahead of you. But he's here, and he's frightened, and he's asking you.",
  "You knock along the row of cottages until a door opens: old Mr Hollis, pale and blinking in the dark, a coat pulled over his nightclothes. His little stove has gone out, his matches are finished, and his hands are shaking far too hard to strike a light even if he had one. \"I can't get it lit,\" he says, and the fear is plain in his voice. You have a long, hard night ahead and an orchard to save. But he is here, now, and he is frightened, and it is you he is asking."),
 11: (
  "You go straight to the rows and light what you can. A match, a flare of straw, a pot catching — but the flames are weak. Without proper oil they will not last. You cannot just leave them and hope.",
  "You go straight out to the rows and light what you can. A match, a flare of straw, a pot catching here and there. But the flames are thin and low. Without proper oil they won't last an hour. You can't just light them and walk away and hope.",
  "You go straight out to the rows and start lighting what you can. You work as fast as your cold hands will move. A match, a flare of straw, a smudge-pot catching here and there along the line. But the flames come up thin and low. Without proper oil, you can see they will gutter out within the hour. You can't simply set them going and turn your back and hope the cold is kind. A half-lit orchard is no safer than a dark one."),
 12: (
  "You go from door to door with the same words. Bring straw. Lend a hand at the pots. Help me hold the fires. Some turn away. But a few pull on their coats and come out. A few is enough to begin.",
  "You go cottage to cottage, asking each door the same thing. Bring straw for the fires. Lend a hand at the pots. Help me hold the light down the rows. Some turn away and shut the door. But a few pull on their coats and step out into the cold. Tonight, a few is enough to begin.",
  "You go from cottage to cottage, knocking, asking each sleepy face the same three things. Bring what straw you have. Lend a pair of hands at the pots. Help me hold the fires down the rows till dawn. Some look at the cold and the hour and quietly shut the door. You can't even blame them. But a few reach for their coats and boots and step out with you. On a night like this, a few is all it takes to begin."),
 13: (
  "You take charge of the oil and straw. The drum is heavy, and every drop of it counts now. Used well, it keeps the fires going all night. Wasted, and the blossom freezes. You hold it close and head for the rows.",
  "You take charge of the oil and the straw yourself. The drum is heavy, and every drop of it matters now. Tended carefully, it will keep the fires burning down the rows all night; wasted, and the blossom freezes before dawn. So you hold it close and head out for the trees.",
  "You take charge of the oil and the straw yourself. This, above everything, is the thing the night turns on. The drum is heavy in your arms, and every drop of it counts now. There is no more until the roads clear. Tended with care, it will keep the fires burning down every row until dawn. Spilled or wasted, and the blossom is lost long before the sun. So you hold it close, square your shoulders, and head out into the trees."),
 14: (
  "You take just a lantern and some kindling. They give you light and a start. But not the fires. And you have no proper oil set by. You will still need real oil, and soon. If not, the rows stay dark and cold.",
  "You take just a lantern and a bundle of kindling. They give you light to work by and a way to start a flame. But not the fires themselves. And you've set no proper oil aside. You'll still need real oil, and soon. If not, the rows stay dark and the frost wins.",
  "You take just a lantern and a bundle of kindling. It is enough to see by, enough to coax a first flame. It is nothing like enough to carry the night. You have light and a start, and that is all. You've set no proper oil aside. A few handfuls of straw won't hold the cold off a whole orchard. You'll still need real oil, and you'll need it soon. If not, every row stays dark and the frost does as it likes."),
 15: (
  "Old Jack Hale knows this orchard. He has watched it for years. \"Stay off the frozen pond,\" he says. \"It looks quick. It kills.\" He warns you about the buyer too. \"Mind your oil. Hold the fires. That's the whole job tonight.\"",
  "Old Jack Hale knows this orchard in the dark better than anyone. \"Stay off the frozen pond,\" he says. \"It looks like a short cut. It isn't — it's a drowning.\" He warns you about the buyer too, that smiling man from the company. \"Mind your oil, hold the fires — that's the whole of the job tonight.\"",
  "Old Jack Hale has worked and watched this orchard for more years than you've been alive, and he finds you in the dark to say his piece. \"Stay off the frozen pond,\" he tells you, gripping your arm. \"It looks like it'll save you half the walking. It won't — the ice is rotten, and it's a drowning, not a short cut.\" He warns you about the buyer too, that smiling man from the company who has been circling Edith's land. \"Mind your oil, hold the fires, and don't let anyone talk you off the job,\" he says. \"That's the whole of it tonight.\""),
 16: (
  "You settle Mr Hollis by a lit stove with a blanket. Slowly his shaking stops. \"Bless you,\" he says, holding your hand. You promise to look in on him again. Then you turn back out into the cold.",
  "You get Mr Hollis's stove lit and settle him by it with a blanket. Little by little, his shaking eases. \"Bless you,\" he says, gripping your hand hard. You promise to look in on him again before morning. Then you turn back out into the frost and the waiting rows.",
  "You coax his little stove back to life. You settle Mr Hollis in a chair beside it, a blanket round his shoulders. You wait until, little by little, the shaking goes out of him. \"Bless you,\" he says, and grips your hand with surprising strength. You promise you'll look in on him again before the night is out. Then you turn back to the door, and the frost, and the long dark rows still waiting for their fires."),
}

# choice text per node, in the SAME order as the existing choices (levelised: one text, all levels)
C = {
 1: ["Take charge of the fires.", "Try the phone for help.", "See to Edith first."],
 2: ["Step out among the rows.", "Decide how to start.", "The straw is damp and won't take."],
 3: ["Decide how to start.", "But the blossom can't wait."],
 4: ["Go back and get the fires going.", "Feel how serious this is."],
 5: ["Tom opens the fuel store.", "Knock along the cottages for help.", "Decide how to start.", "A light out among the far trees."],
 6: ["The fuel store.", "Straight out to the fires.", "Rouse the village for help."],
 8: ["Decide how to start.", "To the fuel store.", "A scramble at the store."],
 9: ["Take charge of the oil and straw.", "Just a lantern and kindling.", "Ask Tom what he knows.", "He presses the last dry lantern on you."],
 10: ["Stop and help him.", "Say you must keep the fires."],
 11: ["Decide how to get real oil.", "The cold takes it out of you."],
 12: ["The village turns out.", "No one stirs; go on alone."],
 13: ["Now, out to the fires.", "Thank Tom."],
 14: ["Now, find real oil.", "Ask Tom what he knows."],
 15: ["Take it to heart.", "On with it."],
 16: ["On out to the fires.", "He asks you to check the others."],
}

LV = ("A2", "B1", "B2")
for nid, (a2, b1, b2) in P.items():
    n = nodes[nid]
    n["text"] = {"A2": a2, "B1": b1, "B2": b2}
    if nid in C:
        for j, ct in enumerate(C[nid]):
            n["choices"][j]["text"] = {lv: ct for lv in LV}

json.dump(book, open(EP, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("Patched %d nodes (batch 1) in %s" % (len(P), EP))
