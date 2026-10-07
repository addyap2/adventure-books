#!/usr/bin/env python3
"""Phase 3 prose for The Refuge (episode-07), batch B: rest of Act I, nodes 28-39.
Run: python3 scripts/generators/phase3_ep07_b.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-07.json")

D = {
 28: {"t": {
  "A2": "You step out onto the cornice, and at once it feels wrong. The drop waits below, black and far. Every step is a gamble now. You are out on it, alone. There is no going back once you start across.",
  "B1": "You step out onto the cornice, and at once it feels wrong. The drop waits below, black and far and freezing. Every step is a gamble now — and you're out on it, alone. There is no going back once you start across.",
  "B2": "You step out onto the cornice, and at once it feels wrong. The drop waits somewhere below, black and far and freezing in the dark. Every single step is a gamble now — and you are out on it, alone, with the wind trying to take you. There is no going back once you have started across."},
  "c": ["Edge on.", "The snow gives under you."]},
 29: {"t": {
  "A2": "The wood is damp and will not catch. It gives only a low, smoky flame. That is little use on a night like this. You will have to make do. Or go back to the store for dry wood.",
  "B1": "The wood is damp and won't catch. It gives only a low, smoky flame. That's little use in a cold like this. You'll have to make do with it. Or go back to the store for dry wood.",
  "B2": "The wood is damp and won't catch properly. It gives only a low, smoky flame that throws no real heat. That's little use on a night like this one. You'll have to make do with it — or go back to the store for dry wood and a better start. Either way, you'll lose a little time you can't spare."},
  "c": ["Out and look down the slope.", "Back to the store for dry wood."]},
 30: {"t": {
  "A2": "The path runs on along the slope, the cold deeper by the hour. Below, a bothy sits dark, with no fire in it. Ahead, the hard air seems to push back at you. And there is a marker post, half-buried in the snow.",
  "B1": "The path runs on along the slope, the cold deepening by the hour. Below, a bothy sits dark, with no fire in it. Ahead, the still, hard air seems to push back at you. And there's a marker post, half-buried in the frozen snow.",
  "B2": "The path runs on along the slope, the cold deepening by the hour until it aches in your teeth. Below, a bothy sits dark, with no fire lit in it. Ahead, the still, hard air of the storm seems to push back at you with every step. And there's a marker post, half-buried and leaning in the frozen snow."},
  "c": ["A party with no fire.", "Press on.", "The cold nearly has you.", "A marker post, half down."]},
 31: {"t": {
  "A2": "A walker has gone down in the snow and can't get up. The cold is already taking hold of them. Stop, and you lose time you do not have. Don't, and they may not last the hour.",
  "B1": "A walker has gone down in the snow and can't get up. The cold is already taking hold of them. Stop, and you lose time you don't have. Don't, and they may not last the hour.",
  "B2": "A walker has gone down in the deep snow and can't get up again. The cold is already taking hold of them, slow and quiet. Stop, and you lose time you don't have; don't, and they may not last the hour out here. And there's no one else on this path tonight to find them if you don't."},
  "c": ["Get them up.", "You can't stop — the refuge."]},
 33: {"t": {
  "A2": "You push on through the worst of the cold. Each step is a fight now, the snow stinging your face. Choices lie ahead. Vane may be near. There is that strange light down the slope. Or you can drive on for the hut.",
  "B1": "You push on through the worst of the cold, each step a fight now, the snow stinging your face. Choices lie ahead. Vane may be near. There is that strange light out on the slope. Or you can just drive on for the hut.",
  "B2": "You push on through the worst of the cold, each step a fight now, the driven snow stinging your face raw. Choices lie ahead of you in the dark. Vane may be near. There is that strange light out on the slope. Or you can simply drive on for the hut and the window."},
  "c": ["Vane again.", "A light out on the slope.", "The last of the watch.", "The cold makes you doubt."]},
 34: {"t": {
  "A2": "You get the walker up onto their feet. You warm them as best you can. Their eyes fill. They press a dry pair of mitts into your hands. 'Take them,' they say, 'for your trouble.' A small thing, freely given. You take it and move on.",
  "B1": "You get the walker up onto their feet and warm them as best you can. Their eyes fill. They press a dry pair of mitts into your hands. 'Take them,' they say, 'for your trouble.' A small thing — but freely given, and you take it and move on.",
  "B2": "You get the walker up onto their feet and warm them as best you can with your own body and a steady word. Their eyes fill, and they press a dry pair of mitts into your hands. 'Take them,' they say, 'for your trouble.' A small thing — but freely given, out here, and you take it and move on."},
  "c": ["On your way.", "They tell you of the light on the slope."]},
 35: {"t": {
  "A2": "You can't stop now. But you can't just leave them, either. So you promise to send help back soon. 'Hold on!' you shout. 'Stay warm, stay together — I won't forget you.' You mean it, too. And then you turn and go.",
  "B1": "You can't stop now — but you can't just leave them, either. So you promise to send help back soon. 'Hold on!' you shout. 'Stay warm, stay together — I won't forget you.' You mean it, too. And then you turn and go.",
  "B2": "You can't stop now — but you can't simply leave them, either. So you promise to send help back soon. 'Hold on!' you shout over the wind. 'Stay warm, stay together — I won't forget you.' You mean it, too; and then you turn and go, carrying the weight of it with you."},
  "c": ["Raise the valley.", "On through the cold."]},
 36: {"t": {
  "A2": "The valley lights one big signal fire out on the hill. A drum of wood ablaze, throwing light and heat into the storm. People crowd near it, the old and the weak given the best of it. It is not the whole night saved. But it is real warmth, and a start.",
  "B1": "The valley lights one big signal fire out on the hill — a drum of wood ablaze, throwing light and heat into the storm. People crowd near it, the old and the weak given the best of it. It isn't the whole night won. But it's a real warmth, and a beginning.",
  "B2": "The valley lights one big signal fire out on the hill — a drum of dry wood ablaze, throwing light and heat up into the driving storm. People crowd near it, the old and the weak given the best of the warmth. It isn't the whole night saved, not by a long way. But it's a real warmth, and a beginning, and a light that can be seen for miles."},
  "c": ["Get the hut going as well.", "Fetch more hands."]},
 37: {"t": {
  "A2": "Hut by hut, the frightened valley turns into a working one. People have jobs now: one feeds the fire, one carries wood, one watches the slope. Fear turns into doing. And doing beats waiting, every single time.",
  "B1": "Hut by hut, the frightened valley turns into a working one. People have jobs now: one tends the fire, one carries wood, one watches the slope. Fear turns into doing. And doing beats waiting, every single time.",
  "B2": "Hut by hut, door by door, the frightened valley turns into a working one. People have jobs now: one tends the signal fire, one carries wood up the track, one watches the slope for lights. Fear turns into doing — and doing beats waiting, out here, every single time. One by one, more lights come on along the dark hill."},
  "c": ["To the far store.", "The last of the watch."]},
 38: {"t": {
  "A2": "The long cold gnaws at your will. A small voice says: stop, go inside, rest. No one would blame you, and it would be so easy. But you think of the people out on the slope. And you push the voice away. Not yet. Not while they can still be reached.",
  "B1": "The long cold gnaws at your will. A small voice says: stop, go inside, rest — no one would blame you, and it would be so easy. But you think of the people out on the slope. And you push the voice away. Not yet. Not while they can still be reached.",
  "B2": "The long cold gnaws at your will. A small voice says: stop, go inside, rest — no one would blame you, and it would be so easy to do. But you think of whoever is still out on the slope in this. And you push the voice away. Not yet. Not while they can still be reached in time."},
  "c": ["The last of the watch.", "Vane's lantern."]},
 39: {"t": {
  "A2": "You reach the old marker post, but the snow has buried and half-toppled it. You can barely read it now. One arm points along the path. The other points out across the slope. Which way? You will have to guess, and guess right.",
  "B1": "You reach the old marker post, but the snow has buried and half-toppled it. You can barely read it now. One arm points along the path. The other points out across the slope. Which way? You'll have to guess, and guess right.",
  "B2": "You reach the old marker post, but the snow has buried its base and half-toppled it in the wind. You can barely read it now. One arm points on along the path; the other points out across the open slope. Which way? You'll have to guess, out here in the white dark — and guess right."},
  "c": ["The path.", "The light on the slope."]},
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
    print(f"batch B: wrote prose for {len(D)} nodes")


if __name__ == "__main__":
    main()
