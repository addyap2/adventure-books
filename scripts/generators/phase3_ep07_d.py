#!/usr/bin/env python3
"""Phase 3 prose for The Refuge (episode-07), batch D: Act II part 2, nodes 60-80.
Run: python3 scripts/generators/phase3_ep07_d.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-07.json")

D = {
 60: {"t": {
  "A2": "Someone points out across the slope. A walker has gone out that way, alone, into the cold and dark. Out there is nothing but snow and the long drop. If no one goes after them, they may not come back.",
  "B1": "Someone points out across the slope: a walker has gone out that way, alone, into the cold and the dark. Out there lies nothing but snow and the long, killing drop. If no one goes after them, they may not come back.",
  "B2": "Someone points out across the dark slope: a walker has gone out that way, alone, into the cold and the storm. Out there lies nothing but deep snow and the long, killing drop below the cornice. If no one goes out after them tonight, they may not come back at all."},
  "c": ["Go after them.", "No time — the refuge first."]},
 61: {"t": {
  "A2": "You find them out on the slope, half-frozen and lost. The cold is tearing at them. They do not seem to know your face. You take a firm hold of their arm. 'Come with me,' you say. 'You're all right now. I've got you.'",
  "B1": "You find them out on the slope, half-frozen and lost, the cold tearing at them. They don't seem to know your face at all. You take a firm hold of their arm. 'Come with me,' you say. 'You're all right now. I've got you.'",
  "B2": "You find them out on the slope, half-frozen and lost, the cold tearing at them through their clothes. They don't seem to know your face at all. You take a firm hold of their arm. 'Come with me,' you say, as steady as you can. 'You're all right now. I've got you.'"},
  "c": ["Walk them back.", "On to the hut."]},
 62: {"t": {
  "A2": "You can't do everything at once, and the refuge needs you most. So you send word for someone else to go after them, and press on. It sits badly with you. But tonight you have to choose, and keep choosing.",
  "B1": "You can't do everything at once, and the refuge needs you most of all. So you send word for someone else to go after them, and press on. It sits badly with you — but tonight, you have to choose, and keep choosing.",
  "B2": "You can't do everything at once, and the refuge needs you most of all tonight. So you send word for someone else to go after them, and press on alone. It sits badly with you, and it stays with you — but tonight, you have to choose, and keep choosing. It is that kind of night, from here to the dawn."},
  "c": ["Decide how to start.", "On toward the far store."]},
 63: {"t": {
  "A2": "You walk them safely back to the bothy. Their friends cry out with relief. They wrap you in a dry coat and make you a place by the stove. 'Thank you,' they keep saying. But the hut is waiting, and you can't stay long.",
  "B1": "You walk them safely back to the bothy, where their friends cry out with relief. They wrap you in a dry coat and make you a place by the stove. 'Thank you,' they keep saying. But the hut is waiting, and you can't stay long.",
  "B2": "You walk them safely back to the bothy, where their friends cry out with relief at the door. They wrap you in a dry coat and make you a place by the stove. 'Thank you,' they keep saying, again and again. But the hut is waiting up the hill, and you can't stay long."},
  "c": ["On toward the far store.", "The last of the watch."]},
 64: {"t": {
  "A2": "You look out over the whole mountain — all white, all still. The snow lies pale and deep in the dark. No light shows anywhere but out on the slope. The whole mountain seems to hold its breath and wait for dawn.",
  "B1": "You look out over the whole mountain — all white, all still. The snow lies pale and deep in the dark. No light shows anywhere but out on the slope. The whole mountain seems to hold its breath and wait for dawn.",
  "B2": "You look out over the whole mountain — all white, all still between the gusts. The snow lies pale and deep and trackless in the dark. No light shows anywhere now but that one out on the slope. The whole mountain seems to hold its breath and wait for the dawn."},
  "c": ["On along the path.", "The light on the slope."]},
 65: {"t": {
  "A2": "The cold deepens to its very worst now. The glass drops as low as it will go. Your breath hangs white in the still air. It is hard to think, hard to move, hard to care. This is the hardest hour of the whole night.",
  "B1": "The cold deepens to its very worst now. The glass drops as low as it will go, and your breath hangs white in the still air. It's hard to think, hard to move, hard to care. This is the hardest hour of the whole night.",
  "B2": "The cold deepens now to its very worst. The glass drops as low as it will go, and your breath hangs white and still in the frozen air. It's hard to think, hard to move, hard even to care. This is the hardest hour of the whole long night. You make yourself keep moving, and keep the watch."},
  "c": ["The party with no fire.", "Press on."]},
 67: {"t": {
  "A2": "Old Doune presses the last dry lamp on you. 'For the window,' he says. 'Go on — I'll stay with Marta and the radio.' His face is grey with worry. This is the help he has to give tonight, and he gives all of it gladly.",
  "B1": "Old Doune presses the last dry lamp on you. 'For the window,' he says. 'Go on — I'll stay here with Marta and the radio.' His face is grey with worry. This is the help he has to give tonight, and he gives all of it gladly.",
  "B2": "Old Doune presses the last dry lamp on you. 'For the window,' he says. 'Go on — I'll stay here with Marta and the radio set.' His face is grey with worry under the lamplight. This is the help he has to give tonight, and he gives all of it, gladly."},
  "c": ["On the way.", "His warning first."]},
 68: {"t": {
  "A2": "At the fuel store, people are rushing the cans. Voices rising, hands grabbing, fear spreading fast. One more shove and it is a fight. You can try to calm them and share the fuel out fairly. Or you can grab yours and go.",
  "B1": "At the fuel store, people are rushing the cans — voices rising, hands grabbing, fear catching and spreading fast. One more shove and it's a fight. You can try to calm them and share the fuel out fairly. Or you can just grab yours and go.",
  "B2": "At the fuel store, people are rushing the cans — voices rising, hands grabbing, fear catching and spreading fast through the crowd. One more shove and it's a fight in the dark. You can try to calm them and share the fuel out fairly. Or you can just grab yours and go."},
  "c": ["Calm it, and share it out.", "Get to the fuel."]},
 70: {"t": {
  "A2": "Far out on the slope, a small light lifts and fades. It is out where no one should be tonight. Showing, then gone, then showing again. No one can explain it. And something in you wants to go and answer it.",
  "B1": "Far out on the slope, a small light lifts and fades. It's out where no one should be tonight — showing, then gone, then showing again. No one can explain it. And something in you wants to go and answer it.",
  "B2": "Far out on the dark slope, a small light lifts and fades. It's out where no one on earth should be tonight — showing, then gone, then showing again through the snow. No one can explain it. And something in you wants, badly, to go and answer it. A light out there, on a night like this, is a question you can't quite leave."},
  "c": ["Go and answer it.", "Leave it — the refuge first."]},
 71: {"t": {
  "A2": "You get out onto the slope and call into the dark. No answer comes but the wind. Then you see it: a small shape, down in the snow, half-hidden in the white. Someone is out here after all. And they are barely moving.",
  "B1": "You get out onto the slope and call into the dark. No answer comes but the wind. Then you see it: a small shape, down in the snow, half-hidden in the white. Someone is out here after all. And they are barely moving.",
  "B2": "You get out onto the open slope and call into the dark. No answer comes back but the wind. Then you see it: a small shape, down in the deep snow, half-hidden in the white. Someone is out here after all, below the cornice. And they are barely moving."},
  "c": ["Go to them.", "Call again and wait.", "The small shape isn't moving."]},
 72: {"t": {
  "A2": "You reach them, and your heart turns over. It is a young walker — Rowan — curled in the snow, half-frozen and barely awake. The cold has them in its grip. There is no time to wait and think. You have to do something now.",
  "B1": "You reach them, and your heart turns over. It's a young walker — Rowan — curled in the snow, half-frozen and barely awake. The cold has them in its grip. There's no time to wait and think. You have to do something now.",
  "B2": "You reach them, and your heart turns over. It's a young walker — Rowan — curled in the snow, half-frozen and barely awake. The cold has them fully in its grip now. There's no time to wait and think about it. You have to do something, and do it now. You drop to your knees in the snow beside them."},
  "c": ["Get them up and warm.", "Run for help."]},
 73: {"t": {
  "A2": "You call again into the dark, and for a moment there is nothing. Then a thin voice comes back, torn by the cold: 'Here! Out here!' Someone is out on the slope, and they need help. And they do not sound strong at all.",
  "B1": "You call again into the dark, and for a moment there's nothing. Then a thin voice comes back, torn by the cold: 'Here! Out here!' Someone is out on the slope, and they need help. And they don't sound strong at all.",
  "B2": "You call again into the dark, and for a long moment there's nothing at all. Then a thin voice comes back, torn ragged by the cold: 'Here! Out here!' Someone is out on the slope, and they need help. And they don't sound strong at all. You shout back into the wind and start toward the voice."},
  "c": ["Go to them.", "Fetch help."]},
 74: {"t": {
  "A2": "You get Rowan up out of the snow and wrap them tight in your coat. Slowly they come round, gripping your arm. 'The lamp,' they whisper. 'Keep the lamp in the window...' Even now, half-frozen, they think of the hut.",
  "B1": "You get Rowan up out of the snow and wrap them tight in your coat. Slowly they come round, gripping your arm. 'The lamp,' they whisper. 'Keep the lamp in the window...' Even now, half-frozen, they are thinking of the hut.",
  "B2": "You get Rowan up out of the deep snow and wrap them tight in your coat. Slowly they come round, gripping your arm hard. 'The lamp,' they whisper. 'Keep the lamp in the window...' Even now, half-frozen on the hill, they are thinking of the refuge. You hold them tighter, and start the long way back."},
  "c": ["Rowan speaks of Marta.", "Get you both back."]},
 75: {"t": {
  "A2": "You turn to run for help — then stop short. There is no help out here, not till morning. No team, no valley, no one coming. It is you or no one, and Rowan knows it too. Their frightened eyes follow you in the dark.",
  "B1": "You turn to run for help — then stop short. There is no help out here, not till morning. No team, no valley, no one coming. It's you or no one, and Rowan knows it too. Their frightened eyes follow you in the dark.",
  "B2": "You turn to run for help — then stop short. There is no help out here, not till morning, not in this. No team, no valley, no one coming up the hill. It's you or no one, and Rowan knows it too. Their frightened eyes follow you in the dark. So you turn back, and make the only choice there is."},
  "c": ["Go back for them.", "To the hut, torn."]},
 76: {"t": {
  "A2": "Rowan looks up at you, their eyes clearer now. 'The warden, Marta — that's my gran,' they say. 'We haven't spoken in years. Not since my dad and her fell out. It's a long, sad story.' And you hear how long it is.",
  "B1": "Rowan looks up at you, their eyes clearer now. 'The warden, Marta — that's my gran,' they say. 'We haven't spoken in years. Not since my dad and her fell out. It's a long, sad story.' And you can hear just how long it is.",
  "B2": "Rowan looks up at you, their eyes clearer now in the lamplight. 'The warden, Marta — that's my gran,' they say. 'We haven't spoken in years. Not since my dad and her fell out. It's a long, sad story.' And you can hear, in the few words, just how long it is."},
  "c": ["Resolve to bring them together.", "Up with the news."]},
 77: {"t": {
  "A2": "You decide to get them face to face before the night is out. Rowan and old Marta, after all these years. It is a small thing, next to the storm and the cold. But it is not nothing. Some shut doors can still be opened.",
  "B1": "You decide to get them face to face before the night is out — Rowan and old Marta, after all these years. It's a small thing, next to the storm and the cold. But it isn't nothing. Some shut doors can still be opened.",
  "B2": "You decide to get them face to face before the night is out — Rowan and old Marta, after all these years apart. It's a small thing, next to the storm and the cold and the lamp. But it isn't nothing. Some shut doors, you think, can still be opened — even on a night like this one."},
  "c": ["Back to the refuge.", "Get Rowan steady first."]},
 78: {"t": {
  "A2": "The small shape isn't moving, and the cold is working on it, slow and patient. And yet someone came all the way out here, into the dark, alone. You can't just leave them lying there. You must go closer and know who it is.",
  "B1": "The small shape isn't moving, and the cold is working on it, slow and patient. And yet someone came all the way out here, into the dark, alone. You can't just leave them lying there. You have to go closer and know who it is.",
  "B2": "The small shape isn't moving, and the cold is working on it, slow and patient and sure. And yet someone came all the way out here, into the dark, alone. You can't just leave them lying there in the snow. You have to go closer, and know who it is."},
  "c": ["Go closer.", "You know this walker."]},
 79: {"t": {
  "A2": "You go closer, and you know them at once. It is Rowan — old Marta's grandchild, not seen here in years, not since the family fell out. Then a weak sound comes from the snow at your feet. You move fast now.",
  "B1": "You go closer, and you know them at once. It's Rowan — old Marta's grandchild, not seen here in years, not since the family fell out. Then a weak sound comes from the snow at your feet. You move fast now.",
  "B2": "You go closer, and you know them at once. It's Rowan — old Marta's grandchild, not seen on this hill in years, not since the family fell out. Then a weak sound comes from the snow at your feet. You move fast now, all thought gone, dropping into the snow to reach them."},
  "c": ["Follow the sound, and find them.", "The years in it."]},
 80: {"t": {
  "A2": "Vane comes up one last time, his lantern swinging. 'Still fighting it?' he says. 'Let the cold have it. Last chance to be on the winning side, friend.' The same easy smile. The same old lie.",
  "B1": "Vane comes up one last time, his lantern swinging. 'Still fighting it?' he says. 'Let the cold have it. Last chance to be on the winning side, friend.' The same easy smile. The same old lie.",
  "B2": "Vane comes up out of the snow one last time, his lantern swinging. 'Still fighting it?' he says. 'Let the cold have it. Last chance to be on the winning side, friend.' The same easy smile. The same old lie, worn thin now. You have heard it before tonight, and you have heard enough of it."},
  "c": ["Take his deal.", "Refuse for good."]},
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
    print(f"batch D: wrote prose for {len(D)} nodes")


if __name__ == "__main__":
    main()
