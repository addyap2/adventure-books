#!/usr/bin/env python3
"""Phase 3 prose for The Interview (episode-10), batch E: Act II core, nodes 60-80.
The Maya subplot (the panellist you fell out with) + Reese's last try.
Run: python3 scripts/generators/phase3_ep10_e.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-10.json")

D = {
 60: {"t": {
  "A2": "An usher stops you. 'There's someone over there,' she says, 'having a bad turn, gone to pieces. No one is helping.' Across the busy hall, a person stands shaking, eyes shut. If no one goes to them, they'll be stuck like that a long while.",
  "B1": "An usher stops you. 'There's someone over there,' she says, 'having a bad turn, gone to pieces. No one's helping.' Across the busy hall, a person stands shaking, eyes shut tight. If no one goes to them, they'll be stuck like that a long while.",
  "B2": "An usher stops you in the hall. 'There's someone over there,' she says, 'having a bad turn, gone quite to pieces. No one's helping.' Across the busy concourse, a person stands shaking, eyes shut tight against it all. If no one goes to them now, they'll be stuck like that a long while."},
  "c": ["Go to them.", "Send someone else."]},
 61: {"t": {
  "A2": "You find them by the wall, shaking and lost, too far gone to speak. The panic has them tight. They don't seem to know where they are. You take a firm hold of their arm. 'Breathe with me,' you say. 'You're all right now. I've got you.'",
  "B1": "You find them by the wall, shaking and lost, too far gone to speak. The panic has them tight. They don't seem to know quite where they are. You take a firm hold of their arm. 'Breathe with me,' you say. 'You're all right now. I've got you.'",
  "B2": "You find them by the wall, shaking and lost, too far gone to speak. The panic has them tight in its grip. They don't seem to know quite where they are, or who you are. You take a firm hold of their arm. 'Breathe with me,' you say, low and steady. 'You're all right now. I've got you.'"},
  "c": ["Walk them to help.", "Back to your own morning."]},
 62: {"t": {
  "A2": "You can't do it all at once, and the room needs you most. So you find a guard and send help their way, and press on. It sits badly with you. But today you have to choose, and keep on choosing.",
  "B1": "You can't do it all at once, and the room needs you most of all. So you find a guard and send help their way, and press on. It sits badly with you. But today you have to choose, and keep on choosing.",
  "B2": "You can't do it all at once, and the room needs you most of all today. So you find a guard and send help their way, and press on through the hall. It sits badly with you, and will for a while. But today you have to choose, and keep on choosing."},
  "c": ["On to the office.", "Get on with it."]},
 63: {"t": {
  "A2": "You walk them safely to the first-aid desk, where staff take over. Their face fills with relief. Someone brings water and a chair. 'Thank you,' they keep saying to you. But your own room is waiting, and you can't stay long today.",
  "B1": "You walk them safely to the first-aid desk, where the staff take over. Their face fills with relief. Someone brings water and a chair. 'Thank you,' they keep saying to you. But your own room is waiting, and you can't stay long today.",
  "B2": "You walk them safely across to the first-aid desk, where the staff take over at once. Their face fills with relief at the sight. Someone brings water and a chair and a kind word. 'Thank you,' they keep saying to you, over and over. But your own room is waiting across the hall, and you can't stay long."},
  "c": ["Back out and on.", "To the office at last."]},
 64: {"t": {
  "A2": "You stop and look across the great hall. People stream past under the high glass roof, all in a hurry, all alone. Everyone is going somewhere. Only one figure stands still, far off, watching. Something about them stops your breath.",
  "B1": "You stop and look across the great hall. People stream past under the high glass roof, all in a hurry, all alone. Everyone is going somewhere today. Only one figure stands still, far off, watching. Something about them stops your breath.",
  "B2": "You stop and look out across the great hall. People stream past under the high glass roof, all in a hurry, all alone with their day. Everyone is going somewhere, fast. Only one figure stands quite still, far off, watching the crowd. And something about them, something you can't name, stops your breath."},
  "c": ["On through the hall.", "That figure, far off."]},
 65: {"t": {
  "A2": "The nerves turn as hard as they get now. Your chest is tight, your mouth is dry, your hands won't settle. It's hard to think, hard to breathe, hard to care. Your bag feels like lead. This is the worst of it.",
  "B1": "The nerves turn as hard as they get now. Your chest is tight, your mouth is dry, your hands won't settle. It's hard to think, hard to breathe, hard to care. Your bag feels like lead in your hand. This is the worst of it — the hardest part of the whole day.",
  "B2": "The nerves turn as hard as they are going to get now. Your chest is tight, your mouth is dry, your hands won't settle at all. It's hard to think, hard to breathe, hard to care about any of it. Your bag feels like lead in your hand. This is the worst of it — the hardest part of the whole long day."},
  "c": ["A rival in real trouble.", "Keep going."]},
 67: {"t": {
  "A2": "Old Sam presses something into your hands — a good pen and a clean folder for your papers. 'For the room,' he says. 'Go on, take it. Walk in looking like you mean it.' His face is kind under the shop light. It's what he has to give today, and he gives it gladly.",
  "B1": "Old Sam presses something into your hands — a good pen and a clean folder for your papers. 'For the room,' he says. 'Go on, take it. Walk in looking like you mean it.' His face is kind under the shop light. It's what he has to give today, and he gives all of it gladly.",
  "B2": "Old Sam presses something into your hands — a good pen and a clean folder for your papers. 'For the room,' he says. 'Go on, take it. Walk in looking like you mean it.' His face is kind under the shop light. It's what he has to give today, and he gives every bit of it gladly."},
  "c": ["Thank him and go.", "Ask what else you'll need."]},
 68: {"t": {
  "A2": "At the sign-in desk, people are pushing for the last forms and slots. Voices rise, elbows go, panic spreading fast down the line. One more shove and it's a row. You can try to calm them and sort it fairly. Or you can grab your slot and go.",
  "B1": "At the sign-in desk, people are pushing for the last forms and slots. Voices rise, elbows go, panic spreading fast down the line. One more shove and it's a row. You can try to calm them and sort it out fairly. Or you can grab your slot and go.",
  "B2": "At the sign-in desk, people are pushing and grabbing for the last forms and slots. Voices rise, elbows go, panic spreading fast down the whole line. One more shove and it tips into a row. You can try to calm them down and sort it out fairly. Or you can grab your own slot and go."},
  "c": ["Calm them, sort it fairly.", "Grab your slot and go."]},
 69: {"t": {
  "A2": "A quiet corner off the main hall, where the noise falls away. You stop to breathe. Then you see her — by the lifts, half-turned, achingly familiar. Someone you knew once, and lost. Your heart goes still.",
  "B1": "A quiet corner off the main hall, where the noise falls away. You stop to breathe for a moment. Then you see her — by the lifts, half-turned, achingly familiar. Someone you knew once, and lost. Your heart goes still.",
  "B2": "A quiet corner off the main hall, where the noise falls away to almost nothing. You stop a moment just to breathe. Then you see her — standing by the lifts, half-turned, achingly familiar. Someone you knew once, and worked beside, and lost. And your heart goes quite still in your chest."},
  "c": ["Go to her.", "Slip past, head down."]},
 70: {"t": {
  "A2": "Far across the hall, a figure stands where the crowd thins. They seem to be looking right at you — then away, then back. You can't place them, and yet you can. Something in you needs to know. And something in you is afraid to.",
  "B1": "Far across the hall, a figure stands where the crowd thins out. They seem to be looking right at you — then away, then back again. You can't place them, and yet you can. Something in you needs to know. And something in you is afraid to.",
  "B2": "Far across the hall, a figure stands where the crowd thins out. They seem to be looking right at you — then away, then back again, slowly. You can't quite place them, and yet somehow you can. Something in you needs to know who it is. And something in you, just as strong, is afraid to."},
  "c": ["Go and see.", "Leave it, head up."]},
 71: {"t": {
  "A2": "You cross the hall toward them and lift a hand. They don't see you, or don't show it. Then you catch their face in the light — and the years fall away. You know that face. You know it far too well.",
  "B1": "You cross the hall toward them and lift a hand. They don't see you, or don't show it. Then you catch their face in the light — and the years fall away at once. You know that face. You know it far too well.",
  "B2": "You cross the hall toward them and lift a hand. They don't see you, or don't choose to show it. Then you catch their face in the light — and all the years fall away at once. You know that face. You know it far, far too well. And your legs carry you on toward it anyway."},
  "c": ["Go to her.", "Call her name.", "Look again, be sure."]},
 72: {"t": {
  "A2": "You reach her, and your heart turns over. It's Maya — older now, the same steady eyes, a lanyard round her neck. She's on the panel. The one you fell out with, years ago, and never put right. No time to think. You have to speak now.",
  "B1": "You reach her, and your heart turns over. It's Maya — older now, the same steady eyes, a lanyard round her neck. She's on the panel. The one you fell out with, years ago, and never put right. There's no time to think. You have to say something now.",
  "B2": "You reach her, and your heart turns right over. It's Maya — older now, the same steady eyes, a staff lanyard round her neck. She's on the panel. The one you fell out with, years ago, and never once put right. There's no time to stop and think. You have to say something, and say it now."},
  "c": ["Face it with her.", "Lose your nerve."]},
 73: {"t": {
  "A2": "You call her name across the hall, and for a moment there's nothing. Then she turns, and her face changes — surprise, then something softer, harder to read. 'It's you,' she says. And you hear how much is in those two words.",
  "B1": "You call her name across the hall, and for a moment there's nothing at all. Then she turns, and her face changes — surprise, then something softer, harder to read. 'It's you,' she says. And you can hear how much is in those two words.",
  "B2": "You call her name across the hall, and for a long moment there's nothing at all. Then she turns, and her whole face changes — surprise first, then something softer, and much harder to read. 'It's you,' she says, quietly. And you can hear just how much is packed into those two small words."},
  "c": ["Go to her.", "Lose your nerve."]},
 74: {"t": {
  "A2": "You face Maya at last, and the years come up between you. Slowly, the hard set of her shoulders eases. She grips your arm. 'So it's you, in there,' she says quietly. 'After all this time.' Even now, she's thinking of the door you both closed.",
  "B1": "You face Maya at last, and all the years come up between you. Slowly, the hard set of her shoulders eases. She grips your arm. 'So it's you, in there,' she says quietly. 'After all this time.' Even now, she's thinking of the door you both closed.",
  "B2": "You face Maya at last, and all the years come up between you at once. Slowly, the hard set of her shoulders eases a little. She grips your arm. 'So it's you, in there,' she says quietly. 'After all this time.' Even now, standing here, she's thinking of the door the two of you closed. You keep your eyes on hers, and you don't look away."},
  "c": ["Ask what went wrong.", "Get to the room first."]},
 75: {"t": {
  "A2": "You turn to slip away — then stop short. There's no avoiding it, not now, not today. Not her on the panel and you at the door. It's face it or lose it, and she knows it too. Her eyes follow you across the hall.",
  "B1": "You turn to slip away — then stop short. There's no avoiding it, not now, not today. Not with her on the panel and you at the door. It's face it or lose it now, and she knows it too. Her eyes follow you across the hall.",
  "B2": "You turn to slip away — then stop short. There's no avoiding it, not now, not today of all days. Not with her on the panel and you about to walk in. It's face it or lose the whole thing now, and she knows it too. Her eyes follow you across the hall, steady and sad."},
  "c": ["Then face her. Go.", "Run from it, head down."]},
 76: {"t": {
  "A2": "Maya looks at you, her eyes clearer now. 'We were a team once,' she says. 'Then it all went wrong, and neither of us called. My fault as much as yours. It's a long, sad story.' And you hear just how long it is.",
  "B1": "Maya looks at you, her eyes clearer now. 'We were a team once,' she says. 'Then it all went wrong, and neither of us called. My fault as much as yours. It's a long, sad story.' And you can hear just how long it is.",
  "B2": "Maya looks at you, her eyes a little clearer now. 'We were a team once, you and me,' she says. 'Then it all went wrong, and neither of us ever called. My fault as much as yours. It's a long, sad story.' And you can hear, in her voice, just how long it is."},
  "c": ["Clear the air before two.", "Just get to the room first."]},
 77: {"t": {
  "A2": "You decide to clear the air before you walk in. You and Maya, after all these years apart. It's a small thing, next to everything else today. But it's not nothing. Some shut doors can still be opened.",
  "B1": "You decide to clear the air before you walk in. You and Maya, after all these years apart. It's a small thing, next to everything else today. But it's not nothing. Some shut doors can still be opened.",
  "B2": "You decide to clear the air before you walk in there. You and Maya, after all these long years apart. It's a small thing, perhaps, next to everything else today. But it is not nothing. Some shut doors can still be opened, if someone tries. And tonight, it seems, that someone is you."},
  "c": ["To the room, with that said.", "Say it properly first."]},
 78: {"t": {
  "A2": "The figure stands still, and your nerve works at you, slow and cruel. And yet you came all this way, through all of it, to this. You can't just walk past and pretend. You have to go closer and be sure who it is.",
  "B1": "The figure stands still, and your nerve works at you, slow and cruel. And yet you came all this way, through all of it, to this moment. You can't just walk past and pretend. You have to go closer and be sure who it is.",
  "B2": "The figure stands quite still, and your nerve works away at you, slow and cruel. And yet you came all this way, through all of it, to this very moment. You can't just walk past and pretend you didn't see. You have to go closer and be sure who it is."},
  "c": ["Go to her.", "Closer still."]},
 79: {"t": {
  "A2": "You go closer, and you know her at once. It's Maya — your old partner, not seen in years, not since the day it all fell apart. Then she turns and sees you too. There's no hiding now.",
  "B1": "You go closer, and you know her at once. It's Maya — your old partner, not seen in years, not since the day it all fell apart. Then she turns and sees you too. There's no hiding from it now.",
  "B2": "You go closer still, and you know her at once. It's Maya — your old partner, not seen in years, not since the day it all fell so badly apart. Then she turns and sees you too, and her eyes widen. There's no hiding from it now, for either of you."},
  "c": ["Face it with her.", "Duck into a quiet corner."]},
 80: {"t": {
  "A2": "Reese turns up one last time, folder in hand. 'Still doing it the hard way?' he says. 'Give it up. Let me sort you out — last chance to take the easy road, friend.' The same easy smile. The same old lie.",
  "B1": "Reese turns up one last time, folder in hand. 'Still doing it the hard way?' he says. 'Give it up. Let me sort you out — last chance to take the easy road, friend.' The same easy smile. The same old lie.",
  "B2": "Reese turns up one last time, a folder in his hand. 'Still doing it the hard way?' he says. 'Give it up, friend. Let me sort you out — last chance to take the easy road.' The same easy smile. The same old lie underneath it. You've seen exactly where that road goes."},
  "c": ["Give in to Reese.", "Send him packing."]},
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
