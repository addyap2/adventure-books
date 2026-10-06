#!/usr/bin/env python3
"""Phase 3 prose for The Orchard — batch 4 (nodes 70-96). Run then validate."""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
EP = os.path.join(ROOT, "content", "episode-06.json")
book = json.load(open(EP, encoding="utf-8"))
nodes = {n["id"]: n for n in book["nodes"]}

P = {
 70: (
  "Far out among the far trees, a small light shows and hides. It is out where no one should be tonight. It appears, then is gone, then appears again. No one can say what it is. Something in you wants to go and see.",
  "Far out among the far trees, a small light lifts and fades. It's out where no one should be tonight — showing, then gone, then showing again. No one can explain it. And something in you wants to go and answer it.",
  "Far out among the far trees, a small light lifts and fades and lifts again. It is out where no one should be on a night like this — showing, then hidden, then showing once more in the dark. No one can explain it to you. And something in you, against all sense, wants to go and answer it."),
 71: (
  "You get out to the far trees and call into the dark. Only the cold answers. Then you see it: a small shape, down among the roots, half-hidden by frost. Someone is out here. And they are not moving much.",
  "You get out to the far trees and call into the dark. No answer comes but the cold. Then you see it: a small shape, down among the trees, half-hidden in the white frost. Someone is out here after all. And they are barely moving.",
  "You get out to the far trees and call into the dark. No answer comes back but the cold and the dark. Then you see it, low among the roots: a small, still shape, half-hidden under the white frost. Someone is out here after all, on the worst night of the year. And they are barely moving at all."),
 72: (
  "You go to them, and your heart turns over. It is a child — Wren — curled in the frost, half-frozen, barely awake. The cold has them. There is no time to wait. You have to act now.",
  "You reach them, and your heart turns over. It's a child — Wren — curled in the frost, half-frozen and barely awake. The cold has them in its grip. There's no time to wait and think. You have to do something now.",
  "You reach them, and your heart turns right over. It is a child — Wren — curled small in the frost, half-frozen and barely awake. The cold has them fully in its grip now. There is no time to wait, no time to think it through. You have to do something, and you have to do it now."),
 73: (
  "You call again into the dark. For a moment, nothing. Then a thin voice comes back: \"Here. Out here.\" Someone is out among the trees, and they need you. And they do not sound strong.",
  "You call again into the dark, and for a moment there's nothing. Then a thin voice comes back, torn by the cold: \"Here! Out here!\" Someone is out among the trees, and they need help. And they don't sound strong at all.",
  "You call again into the dark, and for a long moment there is nothing at all. Then a thin voice comes back, small and torn by the cold: \"Here! Out here!\" Someone is out among the trees, and they need help badly. And from the sound of them, they do not have long."),
 74: (
  "You get Wren up out of the frost and wrap them in your coat. Slowly they come round, gripping your arm. \"The fires,\" they say. \"Keep the fires going.\" Even now, half-frozen, they are thinking of the trees.",
  "You get Wren up out of the frost and wrap them tight in your coat. Slowly they come round, gripping your arm. \"The fires,\" they whisper. \"Keep the fires going. The blossom...\" Even now, half-frozen, they are thinking of the orchard.",
  "You get Wren up out of the frost and wrap them tight in your own coat. Slowly, slowly, they come round, gripping your arm with cold fingers. \"The fires,\" they whisper. \"Keep the fires going. The blossom...\" Even now, half-frozen in the dark, this child is thinking of the orchard and its trees."),
 75: (
  "You turn to run for help — then stop. There is no help out here. Not till morning. No crew, no one coming. It is you or no one, and Wren knows it too. Their eyes follow you in the dark.",
  "You turn to run for help — then stop short. There is no help out here, not till morning. No crew, no neighbours, no one coming. It's you or no one, and Wren knows it too. Their frightened eyes follow you in the dark.",
  "You turn to run for help — and then you stop short. There is no help to be had out here, not till morning comes. No crew, no neighbours, no one coming at all. It is you or it is no one, and Wren knows it too. Their frightened eyes follow you in the dark, and you cannot leave them."),
 76: (
  "Wren looks up, their eyes clearer now. \"The grower — Edith,\" they say. \"That's my gran. We don't speak. Not since Dad and her fell out. It's a long story.\" You hear the sadness in it.",
  "Wren looks up at you, their eyes clearer now. \"The grower, Edith — that's my gran,\" they say. \"We haven't spoken in years. Not since my dad and her fell out. It's a long, sad story.\" And you can hear just how long it is.",
  "Wren looks up at you, their eyes clearer now. \"The grower, Edith — that's my gran,\" they say. \"We haven't spoken in years, none of us. Not since my dad and her fell out, back when I was small. It's a long story, and a sad one.\" And in the way they say it, you can hear just how long and how sad."),
 77: (
  "You decide to get them face to face before dawn. Wren and old Edith, after all these years. It is a small thing, next to the fires and the frost. But it is not nothing. Some doors can still open.",
  "You decide to get them face to face before the night is out — Wren and old Edith, after all these years. It's a small thing, next to the fires and the frost. But it isn't nothing. Some shut doors can still be opened.",
  "You decide, there and then, to get them face to face before the night is out — Wren and old Edith, after all these silent years. It is a small thing, you know, set beside the fires and the killing frost. But it is not nothing. Some doors, even long-shut ones, can still be opened if someone tries."),
 78: (
  "The small shape isn't moving. The frost is working on it, cold and slow. And yet someone came out here, into the dark, alone. You can't just leave them. You have to know who it is.",
  "The small shape isn't moving, and the frost is working on it, cold and patient. And yet someone came all the way out here, into the dark, alone. You can't just leave them lying there. You have to go closer and know who it is.",
  "The small shape isn't moving at all, and the frost is working on it, cold and slow and patient. And yet someone came all the way out here, into the dark and the deep cold, alone. You cannot just leave them lying there in the frost. You have to go closer, now, and know who it is."),
 79: (
  "You go closer, and you know them. It is Wren — Edith's grandchild. No one has seen them here in years, not since the family fell out. Then a weak sound comes from the frost. You move fast.",
  "You go closer, and you know them at once. It's Wren — old Edith's grandchild, not seen here in years, not since the family fell out. Then a weak sound comes from the frost at your feet. You move fast now.",
  "You go closer, and you know them at once. It is Wren — old Edith's own grandchild, not seen anywhere near here in years, not since the whole family fell out and went silent. Then a weak sound comes from the frost at your feet. You stop thinking, and you move fast."),
 80: (
  "The buyer comes up one last time, his lantern swinging. \"Still fighting it?\" he says. \"Let it go dark. Last chance to be on the winning side, friend.\" The same smile. The same lie.",
  "The buyer comes up one last time, his lantern swinging. \"Still fighting it?\" he says. \"Let the frost have it. Last chance to be on the winning side, friend.\" The same easy smile. The same old lie.",
  "The buyer comes up one last time, his lantern swinging gently in his hand. \"Still fighting it?\" he says. \"Let the frost have the lot. Last chance to be on the winning side, friend.\" It is the same easy smile as before. And it is the same old lie underneath."),
 90: (
  "You are back at the orchard, frozen through. The hardest cold of the night sits on everything. By the back steps, Edith lies grey and still. Out in the rows, the fires burn low. This is the hour it all turns on.",
  "You're back at the orchard, frozen through, the hardest cold of the night pressing down on everything. By the back steps, Edith lies grey and still. Out in the rows, the fires are burning low. This is the hour the whole night turns on.",
  "You're back at the orchard at last, frozen through, with the hardest cold of the whole night pressing down on everything. By the back steps, old Edith lies grey and far too still. Out in the rows, the fires are burning low and hungry. This is the hour, you understand, that the whole night turns on."),
 91: (
  "You reach the fires. The flames are low, the far pots cold. Out there, the worst frost is close to taking the far rows. You have to get the fires full and burning again. And you have to do it now.",
  "You reach the fires: the flames low, the far pots gone cold. Out among the far rows, the frost is close to taking the blossom for good. You have to get the fires full and burning again — and you have to do it now, fast.",
  "You reach the fires at last: the flames low, the far pots gone cold and dark. Out among the far rows, the hard frost is close to taking the blossom for good. You have to get the fires full and burning again, all down the line. And you have to do it now, before the cold finishes what it started."),
 92: (
  "Then help reaches you — hands, oil, steady people who know the work. You are not alone with it now. Others are here to share the weight. It is like setting down something you have carried too long.",
  "Then help reaches you at last — more hands, more oil, steady people who know the work. You aren't alone with this now; others are here to share the weight. It's like setting down something heavy you've carried far too long.",
  "Then help reaches you at last — more hands, more oil, steady people who know this work in their sleep. You are not alone with it any more; others are here now to share the weight of it. It is like setting down something heavy that you have been carrying, alone, for far too long."),
 93: (
  "Now you keep the fires. What you can do depends on what you brought. With proper oil, you have plenty to work with. Without it, you must coax every last flicker of flame. Either way, the night is not over.",
  "Now you keep the fires going — and what you can do depends on what you carried out here. With proper oil, you've plenty to work with. Without it, you must coax every last flicker of flame. Either way, the night is far from over.",
  "Now comes the real work: keeping the fires going until dawn. What you can do depends entirely on what you carried out here with you. With proper oil, you have plenty to work with down the rows. Without it, you must coax every last flicker of flame by hand. Either way, the night is still far from over."),
 94: (
  "You go to check on Edith. Her eyes open just a little. There is fear in them — then, seeing you, a little less. \"You kept it going,\" she whispers. \"That I did,\" you say. \"Now rest.\"",
  "You go down to check on Edith, and her eyes open just a little. There's fear in them — then, seeing your face, a little less fear. \"You kept it going,\" she whispers. \"That I did,\" you tell her softly. \"Now rest.\"",
  "You go down to check on Edith, and her eyes open just a little at your step. There is fear in them at first — and then, seeing your face above her, a little less of it. \"You kept it going,\" she whispers, barely a sound. \"That I did,\" you tell her softly. \"Now rest. Leave the rest to me.\""),
 95: (
  "The oil does it. You feed the pots and bank them well. One by one, the fires come up full and gold down the rows. Warm light in all that cold. This is what the whole night was for.",
  "The oil does it. You feed the pots and bank them, and one by one the fires come up full and gold all down the rows. Warm light pushing back all that cold. This, you think, is what the whole hard night was for.",
  "The oil does it, in the end. You feed the pots and bank them carefully, and one by one the fires come up full and gold the whole length of the rows. Warm light and warm air, pushing back against all that killing cold. This, you think, standing among the glow, is what the whole long night was for."),
 96: (
  "You have no proper oil, so you coax what flame there is. You shield it from the cold with your own body. You feed it scraps, breath, will. It burns low and thin. It may not be enough. But you will not let it die.",
  "You've no proper oil to pour, so you coax what little flame there is. You shield it from the draught with your own body, feeding it scraps, breath, sheer will. It burns low and thin. It may not be enough. But you won't let it die without a fight.",
  "You have no proper oil to pour, so you coax along what little flame there is. You shield it from the cold with your own body, feeding it scraps and straw and breath and sheer will. It burns low and thin and uncertain. It may not be enough to save the blossom. But you will not let it die without a fight."),
}

C = {
 70: ["Go and answer it.", "Leave it — the fires first."],
 71: ["Go to them.", "Call again and wait.", "The small shape isn't moving."],
 72: ["Get them up and warm.", "Run for help."],
 73: ["Go to them.", "Fetch help."],
 74: ["Wren speaks of Edith.", "Get you both back."],
 75: ["Go back for them.", "To the fires, torn."],
 76: ["Resolve to bring them together.", "Up with the news."],
 77: ["Back to the orchard.", "Get Wren steady first."],
 78: ["Go closer.", "You know this child."],
 79: ["Follow the sound, and find them.", "The years in it."],
 80: ["Take his deal.", "Refuse for good."],
 90: ["See to the fires.", "The buyer's last offer.", "Help arrives behind you."],
 91: ["Get the fires full.", "Check on Edith below.", "The sky greys over the ridge."],
 92: ["To the fires together.", "Hold the watch.", "A light out among the trees."],
 93: ["The oil and straw.", "Coax the guttering flame."],
 94: ["Get the fires full.", "Break out the oil."],
 95: ["Hold the watch.", "Help arrives."],
 96: ["Hold the watch.", "It may not be enough."],
}

LV = ("A2", "B1", "B2")
for nid, (a2, b1, b2) in P.items():
    n = nodes[nid]
    n["text"] = {"A2": a2, "B1": b1, "B2": b2}
    if nid in C:
        for j, ct in enumerate(C[nid]):
            n["choices"][j]["text"] = {lv: ct for lv in LV}
json.dump(book, open(EP, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("Patched %d nodes (batch 4)" % len(P))
