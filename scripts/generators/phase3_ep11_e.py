#!/usr/bin/env python3
"""Phase 3 prose for Moving Day (episode-11), batch E: Act II core, nodes 60-80.
The Cass subplot (your estranged sister) + Bray's last try.
Run: python3 scripts/generators/phase3_ep11_e.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-11.json")

D = {
 60: {"t": {
  "A2": "A neighbour stops you. 'There's a lad round the back,' she says. 'On his own with a wardrobe, about to drop it. No one's helping.' Round the corner, a young man leans against the weight, going red. If no one lends a hand, it'll come down on him.",
  "B1": "A neighbour stops you. 'There's a lad round the back,' she says, 'struggling with a wardrobe on his own, about to drop it. No one's helping.' Round the corner, a young man leans against the weight, going red in the face. If no one lends a hand, it'll come down on him.",
  "B2": "A neighbour stops you. 'There's a lad round the back,' she says, 'struggling with a wardrobe all on his own, about to drop it. No one's helping.' Round the corner, a young man leans against the weight of it, going red in the face. If no one lends a hand now, it'll come down on top of him."},
  "c": ["Go and help.", "Send someone else."]},
 61: {"t": {
  "A2": "You get a shoulder under the wardrobe just in time. Together you lower it safe. He's shaking, out of breath, too winded to speak. 'Easy,' you say. 'I've got this end. Let's set it down.' And slowly the weight comes off you both.",
  "B1": "You get a shoulder under the wardrobe just in time. Together you lower it down safe. He's shaking, out of breath, too winded to speak. 'Easy,' you say. 'I've got this end. Let's set it down.' And slowly the weight comes off you both.",
  "B2": "You get a shoulder under the wardrobe just in time. Together, straining, you lower it down safe. He's shaking, out of breath, too winded to speak. 'Easy,' you say, steady. 'I've got this end. Let's set it down slow.' And slowly the weight comes off the two of you."},
  "c": ["See it to his door.", "Back to your own move."]},
 62: {"t": {
  "A2": "You can't do it all at once, and Mum's move needs you most. So you call over a couple of the others to take the weight, and press on. It sits badly with you. But today you have to choose, and keep on choosing.",
  "B1": "You can't do it all at once, and Mum's move needs you most of all. So you call over a couple of the others to take the weight, and press on. It sits badly with you. But today you have to choose, and keep on choosing.",
  "B2": "You can't do it all at once, and Mum's move needs you most of all today. So you call over a couple of the others to take the weight for him, and press on. It sits badly with you, and will for a while. But today you have to choose, and keep on choosing."},
  "c": ["On with the move.", "Get on with it."]},
 63: {"t": {
  "A2": "You help him walk the wardrobe to his door and set it down. His face fills with relief. His mates crowd round and clap you on the back. 'Thanks, pal,' they keep saying. But your own van's waiting, and you can't stay long.",
  "B1": "You help him walk the wardrobe to his door and set it down. His face fills with relief. His mates crowd round and clap you on the back. 'Thanks, pal,' they keep saying to you. But your own van's waiting, and you can't stay long today.",
  "B2": "You help him walk the wardrobe to his door and set it down at last. His face fills with relief at the sight. His mates crowd round and clap you on the back. 'Thanks, pal,' they keep saying to you, over and over. But your own van's waiting at the kerb, and you can't stay long today."},
  "c": ["Back out and on.", "To the new place at last."]},
 64: {"t": {
  "A2": "You stop a moment and look down the street. Movers and cars go by, everyone busy, everyone in their own day. The light is nearly gone. Only one person stands still at your gate, looking up. Something about them stops your breath.",
  "B1": "You stop a moment and look down the street. Movers and cars go by, everyone busy, everyone in their own day. The light is nearly gone now. Only one person stands still at your gate, looking up. Something about them stops your breath.",
  "B2": "You stop a moment and look down the street. Movers and cars go by, everyone busy, everyone wrapped up in their own day. The light is nearly gone now. Only one person stands quite still at your gate, looking up at the flat. And something about them, something you can't name, stops your breath."},
  "c": ["On with the move.", "That person at the gate."]},
 65: {"t": {
  "A2": "The work turns as hard as it gets now. Your arms are dead, your back aches, your legs won't lift. It's hard to think, hard to carry, hard to care. The last boxes feel like stone. This is the worst of it.",
  "B1": "The work turns as hard as it gets now. Your arms are dead, your back aches, your legs won't lift. It's hard to think, hard to carry, hard to care. The last boxes feel like stone in your hands. This is the worst of it — the hardest part of the whole day.",
  "B2": "The work turns as hard as it is going to get now. Your arms are dead, your back aches, your legs won't lift another step. It's hard to think, hard to carry, hard to care about any of it. The last boxes feel like stone in your hands. This is the worst of it — the hardest part of the whole long day."},
  "c": ["A neighbour with less.", "Keep going."]},
 67: {"t": {
  "A2": "Old Reg presses something on you — a proper sack trolley from the store cupboard. 'For the heavy stuff,' he says. 'Go on, take it. Saves your back the worst of it.' His face is kind in the stairwell light. It's what he has to give today, and he gives it gladly.",
  "B1": "Old Reg presses something on you — a proper sack trolley from the store cupboard. 'For the heavy stuff,' he says. 'Go on, take it. Saves your back the worst of it.' His face is kind in the stairwell light. It's what he has to give today, and he gives all of it gladly.",
  "B2": "Old Reg presses something on you — a proper sack trolley from the store cupboard. 'For the heavy stuff,' he says. 'Go on, take it. It'll save your back the worst of it.' His face is kind in the stairwell light. It's what he has to give today, and he gives every bit of it gladly."},
  "c": ["Thank him and on.", "Ask what else to watch for."]},
 68: {"t": {
  "A2": "At the van, people are grabbing for space — your boxes, the mum's, a neighbour's bags, all at once. Voices rise, arms reach, it's getting fraught. One more shove and something breaks. You can try to calm it and pack it fair. Or you can get your own in and go.",
  "B1": "At the van, people are grabbing for space — your boxes, the mum's, a neighbour's bags, all at once. Voices rise, arms reach, it's getting fraught. One more shove and something breaks. You can try to calm it down and pack it fair. Or you can get your own in and go.",
  "B2": "At the van, people are grabbing for space — your boxes, the young mum's, a neighbour's bags, all at once. Voices rise, arms reach across each other, it's getting fraught. One more shove and something breaks. You can try to calm it all down and pack it fair. Or you can get your own in and go."},
  "c": ["Calm it, pack it fair.", "Get yours in and go."]},
 69: {"t": {
  "A2": "A quiet spot by the back gate, where the noise falls away. You stop to breathe. Then you see her — by the wall, half-turned, achingly familiar. Someone you knew all your life, and lost. Your heart goes still.",
  "B1": "A quiet spot by the back gate, where the noise falls away. You stop to breathe for a moment. Then you see her — by the wall, half-turned, achingly familiar. Someone you knew all your life, and lost. Your heart goes still.",
  "B2": "A quiet spot by the back gate, where the noise falls away to almost nothing. You stop a moment just to breathe. Then you see her — standing by the wall, half-turned, achingly familiar. Someone you knew all your life, and grew up beside, and lost. And your heart goes quite still in your chest."},
  "c": ["Go to her.", "Slip past, head down."]},
 70: {"t": {
  "A2": "At the gate, a figure stands where the light is thin. They seem to be looking right at you — then away, then back. You can't place them, and yet you can. Something in you needs to know. And something in you is afraid to.",
  "B1": "At the gate, a figure stands where the light is thin. They seem to be looking right at you — then away, then back again. You can't place them, and yet you can. Something in you needs to know. And something in you is afraid to.",
  "B2": "At the gate, a figure stands where the light is thin. They seem to be looking right at you — then away, then back again, slowly. You can't quite place them, and yet somehow you can. Something in you needs to know who it is. And something in you, just as strong, is afraid to."},
  "c": ["Go and see.", "Leave it, carry on."]},
 71: {"t": {
  "A2": "You cross the yard toward them and lift a hand. They don't move, or don't let on. Then you catch their face in the last light — and the years fall away. You know that face. You've known it your whole life.",
  "B1": "You cross the yard toward them and lift a hand. They don't move, or don't let on. Then you catch their face in the last of the light — and the years fall away. You know that face. You've known it your whole life.",
  "B2": "You cross the yard toward them and lift a hand. They don't move, or don't choose to let on. Then you catch their face in the last of the light — and all the years fall away at once. You know that face. You've known it your whole life. And your feet carry you on toward it."},
  "c": ["Go to her.", "Say her name.", "Look again, be sure."]},
 72: {"t": {
  "A2": "You reach her, and your heart turns over. It's Cass — your sister, older now, the same tired eyes, a bag at her feet. She came. The one you fell out with, years ago, and never put right. No time to think. You have to speak now.",
  "B1": "You reach her, and your heart turns over. It's Cass — your sister, older now, the same tired eyes, a bag at her feet. She came. The one you fell out with, years ago, and never put right. There's no time to think. You have to say something now.",
  "B2": "You reach her, and your heart turns right over. It's Cass — your sister, older now, the same tired eyes, a packed bag at her feet. She came. The one you fell out with, years ago, and never once put right. There's no time to stop and think. You have to say something, and say it now."},
  "c": ["Face it with her.", "Lose your nerve."]},
 73: {"t": {
  "A2": "You say her name across the yard, and for a moment there's nothing. Then she turns, and her face changes — surprise, then something softer, harder to read. 'It's you,' she says. And you hear how much is in those two words.",
  "B1": "You say her name across the yard, and for a moment there's nothing at all. Then she turns, and her face changes — surprise, then something softer, harder to read. 'It's you,' she says. And you can hear how much is in those two words.",
  "B2": "You say her name across the yard, and for a long moment there's nothing at all. Then she turns, and her whole face changes — surprise first, then something softer, and much harder to read. 'It's you,' she says, quietly. And you can hear just how much is packed into those two small words."},
  "c": ["Go to her.", "Lose your nerve."]},
 74: {"t": {
  "A2": "You face Cass at last, and all the years come up between you. Slowly, the stiffness in her shoulders eases. She looks past you at the van. 'Mum's really going, then,' she says quietly. 'Let me help carry.' Even now, she's thinking of Mum, and the door home.",
  "B1": "You face Cass at last, and all the years come up between you. Slowly, the stiffness in her shoulders eases. She looks past you at the van. 'Mum's really going, then,' she says quietly. 'Let me help carry.' Even now, she's thinking of Mum, and the door home.",
  "B2": "You face Cass at last, and all the years come up between you at once. Slowly, the stiffness in her shoulders eases a little. She looks past you at the loaded van. 'Mum's really going, then,' she says quietly. 'Let me help carry.' Even now, standing here, she's thinking of Mum, and the door home. You keep your eyes on hers, and you don't look away."},
  "c": ["Ask what went wrong.", "Carry on together."]},
 75: {"t": {
  "A2": "You turn to carry on and say nothing — then stop short. There's no avoiding it, not now, not today. Not with Mum's things between you and her stood right there. It's face it or lose it, and she knows it too. Her eyes follow you across the yard.",
  "B1": "You turn to carry on and say nothing — then stop short. There's no avoiding it, not now, not today. Not with Mum's things between you and her standing right there. It's face it or lose it now, and she knows it too. Her eyes follow you across the yard.",
  "B2": "You turn to carry on and say nothing — then stop short. There's no avoiding it, not now, not today of all days. Not with Mum's whole life between you and her standing right there. It's face it or lose the chance now, and she knows it too. Her eyes follow you across the yard, steady and sad."},
  "c": ["Then face her. Go.", "Turn away, head down."]},
 76: {"t": {
  "A2": "Cass looks at you, her eyes clearer now. 'We stopped talking after Dad,' she says. 'Too much said, too much not said. My fault as much as yours. It's a long, sad story.' And you hear just how long it is.",
  "B1": "Cass looks at you, her eyes clearer now. 'We stopped talking after Dad,' she says. 'Too much said, and too much not said. My fault as much as yours. It's a long, sad story.' And you can hear just how long it is.",
  "B2": "Cass looks at you, her eyes a little clearer now. 'We stopped talking after Dad went,' she says. 'Too much said, and far too much left unsaid. My fault as much as yours. It's a long, sad story.' And you can hear, in her voice, just how long it is."},
  "c": ["Clear the air now.", "Just carry on first."]},
 77: {"t": {
  "A2": "You decide to clear the air before the light goes. You and Cass, after all these years apart. It's a small thing, next to the whole day's weight. But it's not nothing. Some shut doors can still be opened.",
  "B1": "You decide to clear the air before the light goes. You and Cass, after all these years apart. It's a small thing, next to the whole day's weight. But it's not nothing. Some shut doors can still be opened.",
  "B2": "You decide to clear the air before the light goes for good. You and Cass, after all these long years apart. It's a small thing, perhaps, next to the whole day's weight. But it is not nothing. Some shut doors can still be opened, if someone tries. And today, it seems, that someone is you."},
  "c": ["On together.", "Say it properly first."]},
 78: {"t": {
  "A2": "The figure stands still, and your nerve works at you, slow and cruel. And yet they came all this way, to your gate, on today of all days. You can't just carry on and pretend. You have to go closer and be sure who it is.",
  "B1": "The figure stands still, and your nerve works at you, slow and cruel. And yet they came all this way, to your gate, on today of all days. You can't just carry on and pretend. You have to go closer and be sure who it is.",
  "B2": "The figure stands quite still, and your nerve works away at you, slow and cruel. And yet they came all this way, right to your gate, on today of all days. You can't just carry on and pretend you didn't see. You have to go closer and be sure who it is."},
  "c": ["Go to her.", "Closer still."]},
 79: {"t": {
  "A2": "You go closer, and you know her at once. It's Cass — your own sister, not seen in years, not since the day it all fell apart. Then she looks up and sees you too. There's no hiding now.",
  "B1": "You go closer, and you know her at once. It's Cass — your own sister, not seen in years, not since the day it all fell apart. Then she looks up and sees you too. There's no hiding from it now.",
  "B2": "You go closer still, and you know her at once. It's Cass — your own sister, not seen in years, not since the day it all fell so badly apart. Then she looks up and sees you too, and her eyes widen. There's no hiding from it now, for either of you."},
  "c": ["Face it with her.", "Duck into the back."]},
 80: {"t": {
  "A2": "Bray swings by one last time, engine running. 'Still at it the hard way?' he says. 'Give it up. Let me finish it off — last chance, cash, done by dark.' The same easy smile. The same old con.",
  "B1": "Bray swings by one last time, engine running. 'Still at it the hard way?' he says. 'Give it up. Let me finish it off for you — last chance, cash, done by dark.' The same easy smile. The same old con.",
  "B2": "Bray swings by one last time, engine still running. 'Still at it the hard way?' he says. 'Give it up, love. Let me finish it off for you — last chance, cash, done by dark.' The same easy smile. The same old con underneath it. You've seen exactly where that road goes."},
  "c": ["Give in to Bray.", "Send him off."]},
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
    print(f"batch E: wrote prose for {len(D)} nodes")


if __name__ == "__main__":
    main()
