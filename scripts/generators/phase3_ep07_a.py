#!/usr/bin/env python3
"""Phase 3 prose for The Refuge (episode-07), batch A: Act I opening, nodes 1-26.
Writes A2/B1/B2 per node and the choice text. Run: python3 scripts/generators/phase3_ep07_a.py"""
import json, os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "content", "episode-07.json")
# normalise: build path relative to repo root
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-07.json")

D = {
 1: {"t": {
  "A2": "It is the worst night of the winter. The whiteout comes down fast with the dark. Snow drives past the one window. The mountain is lost in white. Then old Marta falls on the loft ladder. She keeps this refuge, but now she cannot get up. The stove is low and the lamp is out. No help can come before morning. Holding the refuge is on you now.",
  "B1": "It is the worst night of the winter, and the whiteout comes down fast with the dark. Snow drives past the one window, and the mountain is lost in white. Then old Marta, who has kept this refuge for thirty winters, goes over on the loft ladder and cannot get up. The stove is low, the lamp is out, and no rescue team can climb before morning. Holding the refuge is on you now.",
  "B2": "It is the worst night of the winter, and the whiteout comes down fast with the falling dark. Snow drives flat past the hut's one window, and the whole mountain is lost somewhere in the white. Then old Marta, who has kept this refuge through thirty winters, goes over on the loft ladder and cannot get up again. The stove has burned low, the storm-lamp is out, and no rescue team will climb this slope before morning. Holding the refuge, and its one light in the window, has come down to you alone."},
  "c": ["Take charge of the stove.", "Try the radio for help.", "See to Marta first."]},
 2: {"t": {
  "A2": "You gather what the hut holds. There is a can of lamp-oil and some matches. There is a good storm-lamp and dry wood. Outside, the wind screams. The cold cuts under the door. Snow is creeping in. You must decide what to do, and do it fast.",
  "B1": "You gather what the hut holds: a can of lamp-oil, matches, a good storm-lamp, an armful of dry wood. Outside, the wind screams and the cold cuts straight through the door. Snow is already creeping in white under it. You have to decide what to do, and do it quickly.",
  "B2": "You gather what the hut holds: a can of lamp-oil, a box of matches, a good storm-lamp, an armful of dry wood from the bunk. Outside, the wind screams across the stone and the cold comes straight through the gap under the door. Snow is already creeping in, white along the floor. You have to decide what to do, and you have to do it quickly."},
  "c": ["Step out and look down the slope.", "Stop and decide how to start.", "The wood is damp and won't take."]},
 3: {"t": {
  "A2": "You try the radio. It hisses and crackles. Then at last Kerr answers from the glen post. No team can climb before morning, he says. Not in a storm like this. Keep the stove in, he tells you. Keep the lamp in the window. Hold on if you can.",
  "B1": "You try the radio. It hisses and crackles, then at last Kerr's voice gets through from the glen post. No team can climb before morning, he says — not into a whiteout like this. Keep the stove in and the lamp in the window, he tells you, and hold on if you possibly can.",
  "B2": "You try the radio. It hisses and spits static, and then at last Kerr's voice breaks through from the glen post far below. No team can climb before morning, he says — not into a whiteout like this one. Keep the stove drawing and the lamp bright in the window, he tells you, and hold on as long as you possibly can."},
  "c": ["Decide how to start.", "But people out there can't wait."]},
 4: {"t": {
  "A2": "You get to Marta at the foot of the ladder. You make her warm and easy. But the hut is still cold. The window is dark. Shelter alone is not enough. People out there need the lamp and the stove. You need fuel, a plan, and a clear head first.",
  "B1": "You get to Marta at the foot of the ladder. You make her as warm and easy as you can. But the hut is still cold and the window is dark. Shelter alone won't do. Anyone caught out there needs the lamp lit and the stove in. You need fuel, a plan, and a clear head first.",
  "B2": "You reach Marta at the foot of the loft ladder and make her as warm and easy as you can. But the hut is still cold and the window is still dark. Shelter alone will not do: anyone caught out on the mountain tonight needs the stove drawing and the lamp bright in the glass. You need fuel, a plan, and a clear head before you can give them that."},
  "c": ["Go and get the stove going.", "Feel how serious this is."]},
 5: {"t": {
  "A2": "You step out into the storm. The wind nearly knocks you down. The snow drives flat and white. The cold presses down on the mountain. Then, far down the slope, you see it. A small light is moving. It is out where no one should be tonight.",
  "B1": "You step out into the storm. The wind nearly takes you off your feet, and the snow drives flat and white. The cold presses down on the whole mountain like a hand. Then, far down the slope, you catch it: a small light moving, out where no one should be tonight.",
  "B2": "You step out into the storm, and the wind nearly takes you off your feet; the snow drives flat and white past the one lit window. The cold presses down on the whole mountain like a hand laid over it. Then, far down the slope, you catch it — a small light, moving, out where no one on earth should be on a night like this."},
  "c": ["Open the fuel store.", "Knock along the bunks for help.", "Decide how to start.", "A light down the slope."]},
 6: {"t": {
  "A2": "You stop and think. You could get the stove and the lamp going first. You could go to Marta and the walkers in the bunkroom. Or you could raise the valley for more hands. Each choice costs time you do not have. And out there, the cold is already working on people.",
  "B1": "You make yourself stop and think. You could get the stove and the lamp going first, and worry about the rest after. You could go to Marta and the walkers in the bunkroom instead. Or you could raise the valley and bring more hands. Each choice costs time you don't have — and out there, the cold is already working on anyone caught in it.",
  "B2": "You make yourself stop and think it through. You could get the stove drawing and the lamp in the window first, and worry about everything else after. You could go to Marta and the walkers in the bunkroom instead. Or you could raise the valley below and bring more hands up the hill. Each choice costs time you do not have — and out in the dark, the cold is already working on whoever is caught in it."},
  "c": ["The fuel store.", "Straight to the stove.", "Raise the valley for help."]},
 8: {"t": {
  "A2": "The cold settles into your chest like a weight. You think of the people out there. Someone is lost on the slope. The hut is the only warmth for miles. If the window stays dark, the cold wins by dawn. That is not a fear. It is a plain fact. No one else will do this. It is you, tonight, or no one.",
  "B1": "The cold settles into your chest like a weight. You think of the people out there: a lost walker on the slope, and the hut the only warmth for miles. If the window stays dark much longer, the cold takes them by dawn. That isn't a fear; it's a plain fact. No one else is coming to do this. It is you, tonight, or no one.",
  "B2": "The cold settles into your chest like a weight. You think of whoever is out there tonight — a lost walker somewhere on the slope — and of this hut, the only warmth and the only light for miles in any direction. If the window stays dark much longer, the cold takes them before dawn. That is not a fear; it is a plain fact. No one else is coming to climb into this and do it. It is you, tonight, or it is no one."},
  "c": ["Decide how to start.", "To the fuel store.", "A scramble at the store."]},
 11: {"t": {
  "A2": "You go straight to the stove and light what you can. A match, a flare of kindling, a small flame in the grate. But the fire is thin. The lamp gutters low. Without proper fuel they will not last an hour. You cannot just light them and hope.",
  "B1": "You go straight to the stove and light what you can. A match, a flare of kindling, a low flame catching in the grate. But the fire is thin and the lamp gutters. Without proper fuel they won't last an hour. You can't just light them and hope the night is kind.",
  "B2": "You go straight to the stove and light what you can — a match, a flare of kindling, a low flame catching at last in the cold grate. But the fire is thin and the storm-lamp gutters in the draught. Without proper fuel neither will last the hour. You cannot simply light them, turn your back, and hope the night turns out kind."},
  "c": ["Decide how to get real fuel.", "The cold takes it out of you."]},
 13: {"t": {
  "A2": "You take charge of the fuel and the dry wood. The drum is heavy. Every drop of oil matters now. Used well, it keeps the stove and lamp going all night. Wasted, the hut goes cold before dawn. So you hold it close and get to work.",
  "B1": "You take charge of the fuel and the dry wood yourself. The drum is heavy, and every drop of oil matters now. Used well, it will keep the stove and the lamp going all night; wasted, and the hut goes cold and dark before dawn. So you hold it close and get to work.",
  "B2": "You take charge of the fuel and the dry wood yourself. The drum is heavy against your chest, and every drop of oil in it matters now. Tended carefully, it will keep the stove drawing and the lamp bright all night; grabbed at and wasted, and the hut goes cold and dark long before dawn. So you hold it close and get to work."},
  "c": ["Now, back to the stove and lamp.", "Ask old Doune about the hill."]},
 14: {"t": {
  "A2": "You take just a storm-lamp and some kindling. They give you light and a way to start a flame. But not the stove itself. You have set no proper fuel aside. You will still need real fuel, and soon. If not, the window stays dark and the cold wins.",
  "B1": "You take just a storm-lamp and a bundle of kindling. They give you light to work by and a way to start a flame. But not the stove itself, and you've set no proper fuel aside. You'll still need real fuel, and soon. If not, the window stays dark and the cold wins.",
  "B2": "You take just a storm-lamp and a bundle of kindling. They give you light to work by and a way to start a flame — but not the stove itself, and you have set no proper fuel aside. You will still need real fuel, and soon. Without it the window stays dark, the hut cools, and the cold wins the night."},
  "c": ["Now, find real fuel.", "Ask old Doune about the hill."]},
 15: {"t": {
  "A2": "Old Doune knows this mountain in the dark. 'Keep off the cornice above the corrie,' he says. 'It looks quick. It is not. It is a long fall.' He warns you about Vane too, the smiling man from the company. 'Mind your fuel. Hold the lamp. That is the whole job tonight.'",
  "B1": "Old Doune has walked this mountain in the dark more than anyone alive. 'Keep off the cornice above the corrie,' he says. 'It looks like a quick way down. It isn't — it's a long fall.' He warns you about Vane too, that smiling man from the company. 'Mind your fuel, hold the lamp — that's the whole of the job tonight.'",
  "B2": "Old Doune has walked this mountain in the dark more than anyone alive. 'Keep well off the cornice above the corrie,' he says. 'It looks like a quick way across. It isn't — it's a long fall onto rock.' He warns you about Vane as well, that smiling man from the company. 'Mind your fuel, hold the lamp in the window — that's the whole of the job tonight, and don't let him tell you different.'"},
  "c": ["Take it to heart.", "On with it."]},
 16: {"t": {
  "A2": "You get the stove going and settle Breck beside it with a blanket. Little by little, his shaking eases. 'Bless you,' he says, holding your hand hard. You promise to check on him again before morning. Then you turn back to the cold and the dark window.",
  "B1": "You get the stove drawing and settle Breck beside it with a blanket. Little by little, his shaking eases. 'Bless you,' he says, gripping your hand hard. You promise to look in on him again before morning. Then you turn back out to the cold and the dark window.",
  "B2": "You get the stove drawing and settle Breck beside it with a blanket round his shoulders. Little by little his shaking eases, and the grey goes out of his face. 'Bless you,' he says, gripping your hand hard. You promise to look in on him again before morning, then turn back out into the cold and the waiting, dark window."},
  "c": ["On, to the stove and lamp.", "He asks you to check the others."]},
 17: {"t": {
  "A2": "Keeping the hut warm and lit comes first. The rest can wait a moment. But you must choose how. You could get proper fuel from the store first. Or you could go straight to the stove and lamp and begin.",
  "B1": "Keeping the hut warm and lit comes first. The rest can wait a moment. But you still have to choose how. You could get proper fuel from the store first. Or you could go straight to the stove and the lamp and begin.",
  "B2": "Keeping the hut warm and the window lit comes first; the rest can wait a moment. But you still have to choose how to do it. You could fetch proper fuel from the store first and do it right. Or you could go straight to the stove and the lamp and begin with what's already to hand."},
  "c": ["Get proper fuel first.", "Straight to the stove."]},
 18: {"t": {
  "A2": "The work takes it out of you. Your legs burn. Your chest heaves. The wind fights you at every step. You are near your limit, and you know it. If you go down here, no one is left to keep the hut. So go slowly, and go carefully.",
  "B1": "The work takes it out of you. Your legs burn, your chest heaves, and the wind fights you at every step. You are near your own limit, and you know it. If you go down out here, there is no one left to keep the hut. So go slowly, and go carefully.",
  "B2": "The work takes it out of you. Your legs burn, your chest heaves, and the wind fights you for every single step. You are near your own limit, and you know it. If you go down out here in the dark, there is no one left to keep the hut and the lamp. So go slowly, and go carefully, and do not spend what you cannot get back."},
  "c": ["Vane's lantern is ahead.", "Push on."]},
 19: {"t": {
  "A2": "The valley wakes, and people start to move. One man carries up a drum of fuel. A woman brings dry wood and torches. Door by door, a plan takes shape. You are not doing this alone any more. And that changes everything.",
  "B1": "The valley wakes to itself, and people begin to move. One man shoulders a drum of fuel. A woman drags out dry wood and head-torches. Door by door, a plan takes shape. You are not doing this alone any more. And that changes everything.",
  "B2": "The valley wakes to itself, and people begin to move. One man shoulders a drum of fuel up the track; a woman drags out dry wood and a box of head-torches. Door by door, hand by hand, a plan takes shape in the dark. You are not doing this alone any more — and that, more than anything, changes the whole shape of the night."},
  "c": ["Lead them up to the hut.", "Light a signal fire first."]},
 20: {"t": {
  "A2": "No one stirs. Doors stay shut. Faces turn from the windows. They are afraid, and afraid people go quiet. You cannot force them out into this. So you turn away and go on alone. It is harder this way. But people out there cannot wait.",
  "B1": "No one stirs. Doors stay shut, and faces turn from the windows. They are afraid, and afraid people go quiet. You can't force them to climb out into this. So you turn away and go on alone. It's harder this way. But the people out there can't wait for them.",
  "B2": "No one stirs. Doors stay shut, and faces turn away from the windows. They are afraid, and afraid people go quiet. You cannot force them out into a night like this. So you turn away and go on alone; it is harder this way, step for step, but whoever is out there on the mountain cannot wait for them to find their courage."},
  "c": ["The fuel store.", "On to the stove."]},
 21: {"t": {
  "A2": "The stove is going and the lamp is in the window. Now for the far store and the fuel. There are two ways to reach it. The long path round the corrie is safe but slow. The cornice straight across is quick. But tonight, the cornice could give way.",
  "B1": "The stove is drawing and the lamp is in the window. Now for the far store and the fuel cache. There are two ways to reach it. The long path round the corrie is safe but slow. The cornice straight across is quick. But on a night like this, the cornice could give way.",
  "B2": "The stove is drawing and the lamp burns in the window at last. Now for the far store and the fuel cache beyond the corrie. There are two ways down to it: the long path round the head of the corrie, safe but slow, or the cornice straight across, quick and tempting. But on a night like this one, the cornice could give way under you."},
  "c": ["Keep to the long path.", "Take the cornice.", "Vane's lantern ahead."]},
 22: {"t": {
  "A2": "You take old Doune's words to heart. Mind the fuel. Keep off the cornice. Do not trust Vane. Hold the lamp in the window above all else. It is simple advice, and good. Now you just have to follow it.",
  "B1": "You take old Doune's words to heart. Mind the fuel carefully. Keep well off the cornice. Don't trust Vane. And hold the lamp in the window above everything else. It's simple advice, and good. Now you just have to follow it.",
  "B2": "You take old Doune's words to heart, one by one. Mind the fuel carefully. Keep well off the cornice above the corrie. Put no trust in Vane. And hold the lamp in the window above everything else. It is simple advice, and good — the hard part is following it when the wind is screaming and the easy way looks so close."},
  "c": ["On the way.", "Back to the store."]},
 23: {"t": {
  "A2": "You feel steadier for the good turn you did. Helping someone steadies you too. Your head is clearer. Your hands are surer. There is a hard night still ahead. But now you feel able to meet it.",
  "B1": "You feel steadier for the good turn you did. Helping someone seems, oddly, to steady you too. Your head is clearer, and your hands are surer. There is a hard night still to go. But now you feel able to meet it.",
  "B2": "You feel steadier for the good turn you did. Helping someone through the cold seems, oddly, to steady you as well. Your head is clearer now, and your hands are surer on the work. There is a long, hard night still to go — but you feel, for the first time since Marta went down, able to meet it."},
  "c": ["On with the watch.", "Raise more hands."]},
 24: {"t": {
  "A2": "A man stands out of the snow, a lantern in his fist — Vane. He has fuel to sell and a strong back to offer. He smiles too easily. 'The refuge isn't really your job tonight, friend,' he says. You have met his kind before.",
  "B1": "A man stands out of the snow, a lantern swinging in his fist — Vane. He has fuel to sell and a strong back to offer, and he smiles too easily. 'The refuge isn't really your job tonight, friend,' he says. You've met his kind before.",
  "B2": "A man stands out of the driving snow, a lantern swinging in his fist — Vane. He has fuel to sell and a strong back to lend, and he smiles far too easily for a night like this. 'The refuge isn't really your job tonight, friend,' he says. You have met his kind before, and you know a hook when it's dangled."},
  "c": ["Hear him out.", "Go round him."]},
 25: {"t": {
  "A2": "You lead a small band up toward the hut. Walking together, you all feel stronger. They carry fuel, wood, and torches. 'This way!' you call into the wind, and they come. It is a good feeling, in a hard hour.",
  "B1": "You lead a small band up toward the hut. Walking together, you all feel stronger. They carry fuel, wood, and torches. 'This way!' you call into the wind, and they come. It's a good feeling, in a hard hour.",
  "B2": "You lead a small band up the track toward the hut. Walking together into the wind, you all feel stronger than any of you would alone; they carry fuel, dry wood, torches. 'This way!' you call into the storm, and they come on behind your light. It is a good feeling to have, in a hard hour."},
  "c": ["This way.", "A light down the slope."]},
 26: {"t": {
  "A2": "The path is black and hard. The wind presses down it. There is no shelter anywhere. But it is solid under your feet. It runs where you need to go. So you keep walking, step after step.",
  "B1": "The path is black and hard, the wind pressing down it, no shelter anywhere. But it's solid under your feet, and it runs where you need to go. So you keep walking, step after step.",
  "B2": "The path is black and hard, the wind pressing straight down it, and there is no shelter anywhere along its length. But it is solid under your feet, and it runs where you need to go. The cold finds every gap in your coat as you go. So you keep walking into it, head down, step after step after step."},
  "c": ["Press on.", "Someone's in trouble ahead.", "The whole mountain, white and still."]},
}


def main():
    d = json.load(open(P, encoding="utf-8"))
    by = {n["id"]: n for n in d["nodes"]}
    done = 0
    for nid, spec in D.items():
        n = by[nid]
        n["text"] = spec["t"]
        ch = n.get("choices") or []
        for j, c in enumerate(ch):
            if j < len(spec["c"]):
                t = spec["c"][j]
                c["text"] = {"A2": t, "B1": t, "B2": t}
        done += 1
    json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"batch A: wrote prose for {done} nodes")


if __name__ == "__main__":
    main()
