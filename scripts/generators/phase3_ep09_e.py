#!/usr/bin/env python3
"""Phase 3 prose for The Dinner (episode-09), batch E: Act II core, nodes 60-80.
The Nora subplot (estranged granddaughter out in the rain) + Dale's last try.
Run: python3 scripts/generators/phase3_ep09_e.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-09.json")

D = {
 60: {"t": {
  "A2": "A neighbour stops you. 'There's someone down the road,' they say, 'out in the rain, lost. Been there an hour. No coat, no umbrella.' Out there is just the dark and the cold. If no one goes to them, they'll be there all night.",
  "B1": "A neighbour stops you. 'There's someone down the road,' they say, 'standing out in the rain, lost. Been there an hour. No coat, no umbrella.' Out there is just the dark and the cold. If no one goes to them, they'll be there all night.",
  "B2": "A neighbour stops you in the street. 'There's someone down the road,' they say, 'standing out in the rain, quite lost. Been there the best part of an hour. No coat, no umbrella, nothing.' Out there is just the dark and the cold. If no one goes to them tonight, they'll be there until morning."},
  "c": ["Go to them.", "Send someone else."]},
 61: {"t": {
  "A2": "You find them down the road, soaked through and shaking, lost. The cold has got right into them. They don't seem to know where they are. You take a firm hold of their arm. 'Come with me,' you say. 'You're all right now. I've got you.'",
  "B1": "You find them down the road, soaked through and shaking, lost. The cold has got right into them. They don't seem to know quite where they are. You take a firm hold of their arm. 'Come with me,' you say. 'You're all right now. I've got you.'",
  "B2": "You find them down the road, soaked through and shaking, utterly lost. The cold has got right into them. They don't seem to know quite where they are, or who you are. You take a firm hold of their arm. 'Come with me,' you say, over the rain. 'You're all right now. I've got you.'"},
  "c": ["Walk them in.", "Back to the dinner."]},
 62: {"t": {
  "A2": "You can't do it all at once, and the dinner needs you most. So you send word for someone else to go to them, and press on home. It sits badly with you. But tonight you have to choose, and keep choosing.",
  "B1": "You can't do it all at once, and the dinner needs you most of all. So you send word for someone else to go to them, and press on home. It sits badly with you. But tonight you have to choose, and keep on choosing.",
  "B2": "You can't do it all at once, and the dinner needs you most of all tonight. So you send word for someone else to go to them, and press on home through the rain. It sits badly with you, and will for a while. But tonight you have to choose, and keep on choosing."},
  "c": ["On home.", "Get on with it."]},
 63: {"t": {
  "A2": "You walk them safely to a warm doorway, where friends take them in. Their faces fill with relief. They wrap the stranger in a dry coat and sit them down by the fire. 'Thank you,' they keep saying to you. But your own kitchen is waiting, and you can't stay long.",
  "B1": "You walk them safely to a warm doorway, where friends take them in. Their faces fill with relief. They wrap the stranger in a dry coat and sit them down by the fire. 'Thank you,' they keep saying to you. But your own kitchen is waiting, and you can't stay long tonight.",
  "B2": "You walk them safely to a warm doorway, where friends take them in at once. Their faces fill with relief at the sight. They wrap the stranger in a dry coat and sit them down by the fire. 'Thank you,' they keep saying to you, over and over. But your own kitchen is waiting across the dark, and you can't stay long."},
  "c": ["Back out into it.", "Home at last."]},
 64: {"t": {
  "A2": "You stop and look down the long wet street. The rain falls through the lamplight, soft and steady. The houses are dark, the curtains drawn, everyone in for the night. Only one small light moves, far off. The whole street seems to hold its breath.",
  "B1": "You stop and look down the long wet street. The rain falls through the lamplight, soft and steady. The houses are dark, the curtains drawn, everyone in for the night. Only one small light moves, far off down the road. The whole street seems to hold its breath.",
  "B2": "You stop and look down the long, wet street. The rain falls through the lamplight, soft and steady and endless. The houses are dark, the curtains drawn, everyone in for the night. Only one small light moves, far off down the road, where it has no business being. The whole street seems to hold its breath and wait."},
  "c": ["On down the street.", "That light, far off."]},
 65: {"t": {
  "A2": "The night turns as hard as it gets. The rain comes down in sheets now, and the cold bites through your coat. It's hard to think, hard to move, hard to care. Your bags feel like lead. This is the worst of it.",
  "B1": "The night turns as hard as it gets now. The rain comes down in sheets, and the cold bites through your coat. It's hard to think, hard to move, hard to care. Your bags feel like lead in your hands. This is the worst of it — the hardest part of the whole evening.",
  "B2": "The night turns as hard as it is going to get. The rain comes down in sheets now, and the cold bites straight through your coat. It's hard to think, hard to move, hard to care about any of it. Your bags feel like lead in your hands. This is the worst of it — the hardest part of the whole long evening."},
  "c": ["A house with no dinner.", "Keep going."]},
 67: {"t": {
  "A2": "Old Sam presses a parcel into your hands — the last good cut of meat in the shop. 'For the table,' he says. 'Go on, take it. I'll put it on the tab.' His face is kind under the shop light. It's what he has to give tonight, and he gives it gladly.",
  "B1": "Old Sam presses a parcel into your hands — the last good cut of meat in the shop. 'For the table,' he says. 'Go on, take it. I'll put it on your tab.' His face is kind under the shop light. It's what he has to give tonight, and he gives all of it gladly.",
  "B2": "Old Sam presses a wrapped parcel into your hands — the last good cut of meat left in the shop. 'For the table,' he says. 'Go on, take it. I'll put it on your tab.' His face is kind under the shop light. It's what he has to give tonight, and he gives every bit of it gladly."},
  "c": ["Thank him and go.", "Ask what else you'll need."]},
 68: {"t": {
  "A2": "At the shop door, people are grabbing the last of the food. Voices rise, hands push, fear spreading fast. One more shove and it's a fight. You can try to calm them and share it out fairly. Or you can grab what's yours and go.",
  "B1": "At the shop door, people are grabbing the last of the food. Voices rise, hands push, fear spreading fast through the queue. One more shove and it's a fight. You can try to calm them and share it out fairly. Or you can grab what's yours and go.",
  "B2": "At the shop door, people are grabbing the last of the food off the shelves. Voices rise, hands push, fear spreading fast through the queue. One more shove and it tips into a fight. You can try to calm them down and share it out fairly. Or you can grab what's yours and go."},
  "c": ["Calm them, share it out.", "Grab yours and go."]},
 69: {"t": {
  "A2": "A dark, quiet corner by the gate, where nothing seems to move. The rain drips. The cold creeps in. Then you hear it — breathing, weak and close, out of the dark. Someone is here after all, huddled down against the wall.",
  "B1": "A dark, quiet corner by the gate, where nothing seems to move at all. The rain drips. The cold creeps in. Then you hear it — breathing, weak and close, out of the dark. Someone is here after all, huddled down against the wall.",
  "B2": "A dark, quiet corner by the gate, where nothing seems to move at all. The rain drips from the eaves. The cold creeps in around you. Then you hear it — breathing, weak and close, somewhere out of the dark. Someone is here after all, huddled down against the cold wall."},
  "c": ["Reach them.", "Hurry inside."]},
 70: {"t": {
  "A2": "Far down the dark street, a small light lifts and fades. It's out where no one should be, this late, in this rain. Showing, then gone, then showing again. You can't explain it. And something in you wants to go and answer it.",
  "B1": "Far down the dark street, a small light lifts and fades. It's out where no one should be, this late, in this rain. Showing, then gone, then showing again. No one could explain it. And something in you wants to go and answer it.",
  "B2": "Far down the dark street, a small light lifts and fades, lifts and fades. It's out where no one should be, this late, in this kind of rain. Showing, then gone, then showing again, patient as anything. No one could explain it. And something in you wants to go and answer it."},
  "c": ["Go and see.", "Leave it, get home."]},
 71: {"t": {
  "A2": "You go down toward the light and call into the dark. No answer comes but the rain. Then you see it — a small shape, down low against a wall, half-hidden in the dark. Someone is out here after all. And they are barely moving.",
  "B1": "You go down toward the light and call into the dark. No answer comes back but the rain. Then you see it — a small shape, down low against a wall, half-hidden in the dark. Someone is out here after all. And they are barely moving.",
  "B2": "You go on down toward the light and call into the dark. No answer comes back but the rain and the wind. Then you see it — a small shape, down low against a wall, half-hidden in the dark. Someone is out here after all, alone. And they are barely moving now."},
  "c": ["Go to them.", "Call again.", "Look closer first."]},
 72: {"t": {
  "A2": "You reach them, and your heart turns over. It's a young woman — Nora — huddled against the wall, soaked and shaking, barely awake. The cold has got right into her. There's no time to stop and think. You have to do something now.",
  "B1": "You reach them, and your heart turns over. It's a young woman — Nora — huddled against the wall, soaked and shaking, barely awake. The cold has got right into her. There's no time to stop and think about it. You have to do something now.",
  "B2": "You reach them, and your heart turns right over. It's a young woman — Nora — huddled against the wall, soaked and shaking, barely awake at all. The cold has got right into her now. There's no time to stop and think it through. You have to do something, and do it now."},
  "c": ["Get her up.", "Run for help."]},
 73: {"t": {
  "A2": "You call again into the dark, and for a moment there's nothing. Then a thin voice comes back, shaking with cold: 'Here! Over here!' Someone is out in the rain, and they need help. And they don't sound strong at all.",
  "B1": "You call again into the dark, and for a moment there's nothing at all. Then a thin voice comes back, shaking with cold: 'Here! Over here!' Someone is out in the rain, and they need help. And they don't sound strong at all.",
  "B2": "You call again into the dark, and for a long moment there's nothing at all. Then a thin voice comes back, torn and shaking with cold: 'Here! Over here!' Someone is out in the rain, and they need help badly. And they don't sound strong at all. You cup your hands and shout back into the rain."},
  "c": ["Go to the voice.", "Run for help."]},
 74: {"t": {
  "A2": "You get Nora up out of the wet and wrap her tight in your coat. Slowly she comes round, gripping your arm. 'The door,' she whispers. 'Is the door still open...?' Even now, half-frozen, she's thinking of someone's door.",
  "B1": "You get Nora up out of the wet and wrap her tight in your own coat. Slowly she comes round, gripping your arm. 'The door,' she whispers. 'Is the door still open...?' Even now, half-frozen, she's thinking of someone's door.",
  "B2": "You get Nora up out of the wet and wrap her tight in your own coat. Slowly she comes round, gripping your arm hard. 'The door,' she whispers. 'Is the door still open...?' Even now, half-frozen in the rain, she's thinking of someone's door. You keep your arm around her, and hold on."},
  "c": ["Ask what she means.", "Get her home and warm."]},
 75: {"t": {
  "A2": "You turn to run for help — then stop short. There's no one out here to call, not at this hour. No neighbours up, no one coming. It's you or no one, and she knows it too. Her frightened eyes follow you in the dark.",
  "B1": "You turn to run for help — then stop short. There's no one out here to call, not at this hour. No neighbours up, no one coming for you. It's you or no one now, and she knows it too. Her frightened eyes follow you in the dark.",
  "B2": "You turn to run for help — then stop short. There's no one out here to call on, not at this hour of the night. No neighbours up, no one coming for either of you. It's you or no one now, and she knows it too. Her frightened eyes follow you in the dark."},
  "c": ["Then it's you. Go to her.", "Panic and run home."]},
 76: {"t": {
  "A2": "Nora looks up at you, her eyes clearer now. 'Ivy's my gran,' she says. 'We haven't spoken in years. Not since my mum and her fell out. It's a long, sad story.' And you hear just how long it is.",
  "B1": "Nora looks up at you, her eyes clearer now. 'Ivy's my gran,' she says. 'We haven't spoken in years. Not since my mum and her fell out. It's a long, sad story.' And you can hear just how long it is.",
  "B2": "Nora looks up at you, her eyes a little clearer now. 'Ivy's my gran,' she says. 'We haven't spoken in years. Not since my mum and her fell out, back then. It's a long, sad story.' And you can hear, in her voice, just how long it is."},
  "c": ["Bring them together tonight.", "Just get her warm first."]},
 77: {"t": {
  "A2": "You decide to get them face to face before the night is out. Nora and old Gran Ivy, after all these years. It's a small thing, next to everything else tonight. But it's not nothing. Some shut doors can still be opened.",
  "B1": "You decide to get them face to face before the night is out. Nora and old Gran Ivy, after all these years apart. It's a small thing, next to everything else tonight. But it's not nothing. Some shut doors can still be opened.",
  "B2": "You decide to get them face to face before the night is out. Nora and old Gran Ivy, after all these long years apart. It's a small thing, perhaps, next to everything else tonight. But it is not nothing. Some shut doors can still be opened, if someone tries. And tonight, it seems, that someone is you."},
  "c": ["Home, with Nora.", "Get her warm first."]},
 78: {"t": {
  "A2": "The small shape isn't moving, and the cold is working on it, slow and patient. And yet someone came all this way out here, in the rain, alone. You can't just leave them lying in the wet. You have to go closer and see who it is.",
  "B1": "The small shape isn't moving, and the cold is working on it, slow and patient. And yet someone came all this way out here, in the rain, alone. You can't just leave them lying there in the wet. You have to go closer and see who it is.",
  "B2": "The small shape isn't moving at all, and the cold is working on it, slow and patient. And yet someone came all this way out here, in the rain, quite alone. You can't just leave them lying there in the wet. You have to go closer and see who it is."},
  "c": ["Go to them.", "Closer still."]},
 79: {"t": {
  "A2": "You go closer, and you know her at once. It's Nora — Gran Ivy's own granddaughter, not seen round here in years, not since the family fell out. Then a weak sound comes from the dark at your feet. You move fast now.",
  "B1": "You go closer, and you know her at once. It's Nora — Gran Ivy's own granddaughter, not seen round here in years, not since the family fell out. Then a weak sound comes from the dark at your feet. You move fast now.",
  "B2": "You go closer still, and you know her at once. It's Nora — Gran Ivy's own granddaughter, not seen round here in years, not since the family fell out so badly. Then a weak sound comes from the dark at your feet. You move fast now. There is no time left to lose, none at all."},
  "c": ["Get her up.", "Down into the dark."]},
 80: {"t": {
  "A2": "Dale turns up one last time, his bags swinging. 'Still at it?' he says. 'Give it up. Let me sort your dinner — last chance to take the easy road, friend.' The same easy smile. The same old lie.",
  "B1": "Dale turns up one last time, his bags swinging. 'Still at it?' he says. 'Give it up. Let me sort your dinner out — last chance to take the easy road, friend.' The same easy smile. The same old lie.",
  "B2": "Dale turns up one last time, his bags swinging in the rain. 'Still at it?' he says. 'Give it up, love. Let me sort your dinner out — last chance to take the easy road, friend.' The same easy smile. The same old lie underneath it. You've seen exactly where that road goes."},
  "c": ["Give in to Dale.", "Send him packing."]},
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
