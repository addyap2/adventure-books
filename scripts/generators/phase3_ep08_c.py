#!/usr/bin/env python3
"""Phase 3 prose for The Refuge (episode-08), batch C: Act II part 1, nodes 40-58.
Run: python3 scripts/generators/phase3_ep08_c.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-08.json")

D = {
 40: {"t": {
  "A2": "Vane turns his wide, easy smile on you. 'Cold work, this,' he says. 'I've fuel to sell, and a strong back to lend. The refuge isn't really your job tonight, friend.' His lantern swings. His smile never reaches his eyes.",
  "B1": "Vane turns his wide, easy smile on you. 'Cold work, this,' he says. 'I've fuel to sell, and a strong back to lend — and the refuge isn't really your job tonight, friend.' His lantern swings. His smile never reaches his eyes.",
  "B2": "Vane turns his wide, easy smile on you. 'Cold work, this,' he says. 'I've fuel to sell, and a strong back to lend — and the refuge isn't really your job tonight, friend.' His lantern swings in the wind. His smile never once reaches his eyes, and you notice that it never does."},
  "c": ["Hear the price.", "Refuse and go round."]},
 42: {"t": {
  "A2": "You turn your back on him and leave him to his cold trade. It feels good to walk away. He calls after you, but you do not turn round. His kind always finds someone, in the end. But it will not be you, not tonight.",
  "B1": "You turn your back on him and leave him to his cold trade. It feels good to walk away. He calls after you, but you don't turn round. His kind always finds someone, in the end. But it won't be you, not tonight.",
  "B2": "You turn your back on him and leave him to his cold trade. It feels good to walk away from it. He calls something after you, but you don't turn round. His kind always finds someone, in the end — someone cold and frightened enough. But it won't be you, not tonight."},
  "c": ["On the way.", "To the fuel store instead."]},
 43: {"t": {
  "A2": "You take his fuel and his deal. Your hands close on them, and something in you already knows. His smile widens. 'Wise,' he says. But it does not feel wise at all. It feels like a door quietly shutting.",
  "B1": "You take his fuel and his deal. Your hands close on them, and something in you already knows. His smile widens. 'Wise,' he says. But it doesn't feel wise at all. It feels like a door quietly shutting.",
  "B2": "You take his fuel and his deal. Your hands close on them, and something in you already knows the truth of it. His smile widens. 'Wise,' he says. But it doesn't feel wise at all. It feels, in the cold, like a door being quietly shut somewhere behind you."},
  "c": ["Carry it out to the stove.", "A doubt already."]},
 44: {"t": {
  "A2": "You ask him straight: what does he really want, and why should the refuge fail? He smiles and looks off into the snow. 'Land comes cheap after a bad year,' he says. 'A night like this is a kindness — to a buyer like me.'",
  "B1": "You ask him straight: what does he really want, and why should the refuge fail? He smiles and looks off into the snow. 'Land comes cheap after a bad year,' he says. 'A night like this is a kindness — to a buyer like me.'",
  "B2": "You ask him straight out: what does he really want, and why should the refuge fail tonight? He smiles and looks off into the driving snow. 'Land comes cheap after a bad winter,' he says. 'A condemned hut, a night like this — it's a kindness, really. To a buyer like me.'"},
  "c": ["That's your answer — refuse.", "Take it anyway."]},
 45: {"t": {
  "A2": "You carry his fuel to the stove. But when you pour it in, the flame chokes and spits. The fuel is thin, cut with water. It will not feed the fire. The flame sinks low and useless.",
  "B1": "You carry his fuel to the stove. But when you pour it in, the flame chokes and spits. The fuel is thin, cut with water — it won't feed the fire. The flame sinks low and brown and useless.",
  "B2": "You carry his fuel back to the stove. But when you pour it in, the flame chokes and spits and nearly dies. The fuel is thin, cut with water — it won't feed the fire at all. The flame sinks low and brown and useless, and the cold begins, at once, to come back in."},
  "c": ["Try to work it.", "On with nothing."]},
 46: {"t": {
  "A2": "You open the can, and the smell hits you — thin, sour, cut with water. This fuel will never feed a flame. You paid good money for it, and it is worthless. The doubt in your gut was right all along.",
  "B1": "You open the can, and the smell hits you — thin, sour, cut with water. This fuel will never feed a flame. You paid good money for it, and it's worthless. The doubt in your gut was right all along.",
  "B2": "You open the can, and the smell hits you — thin, sour, cut with water. This fuel will never feed a flame, not for a minute. You paid good money for it, out here, and it's worthless. The doubt you felt in your gut was right about him all along. You tip the thin stuff out into the snow."},
  "c": ["On to the hut.", "Back to have it out with him."]},
 47: {"t": {
  "A2": "You look for him, but Vane's lantern is already gone, off into the snow. He was never helping you at all. He was waiting for the storm, the failed night, the cheap land after. You were fooled, plain and simple.",
  "B1": "You look for him, but Vane's lantern is already gone, off into the snow. He was never helping you at all. He was waiting for the storm, the failed night, the cheap land after. You were fooled, plain and simple.",
  "B2": "You look for him, but Vane's lantern is already gone, swallowed off into the driving snow. He was never helping you at all. He was waiting for the storm, the failed night, the cheap land that comes after. You were fooled, out here, plain and simple. And now you are out on the hill with nothing to show for it."},
  "c": ["On to the hut, fooled.", "Fling the fouled can down."]},
 48: {"t": {
  "A2": "He's gone, and the slope is empty. Only the cold now, the dark, and what you gave him for nothing. You learned a hard lesson tonight. And you paid far too much for it. Now you go on with less than you started.",
  "B1": "He's gone, and the slope is empty — only the cold now, the dark, and what you handed him for nothing. You learned a hard lesson tonight. And you paid far too much for it. Now you go on with less than you started.",
  "B2": "He's gone, and the slope is empty — only the cold now, the dark, and what you handed him for nothing at all. You learned a hard lesson tonight, out here. And you paid far too much for it. Now you go on with less than you started, and the night no shorter."},
  "c": ["On to the hut.", "Stand a moment in the dark."]},
 49: {"t": {
  "A2": "The frightened folk press their money on him. Hands full of notes, voices begging for fuel. He takes it slow, with that same smile. He chooses who to help by who can pay the most.",
  "B1": "The frightened folk press their money on him. Hands full of notes, voices begging for fuel. He takes it slow, with that same smile. He chooses who to help by who can pay the most.",
  "B2": "The frightened folk press their money on him. Hands full of notes, voices begging him for fuel, for a lift down, for anything. He takes it slow, with that same unhurried smile. He chooses who to help by who can pay the most — and you see the whole of him in it."},
  "c": ["Hear the price anyway.", "Refuse and go round."]},
 50: {"t": {
  "A2": "Far out on the cornice, the far side seems nearer at last — or does it? You can't be sure any more. The dark plays tricks, and so do your tired eyes. And you are a long way now from either edge.",
  "B1": "Far out on the cornice, the far side seems nearer at last — or does it? You can't be sure any more. The dark plays tricks, and so do your tired eyes. And you're a long way now from either edge.",
  "B2": "Far out on the cornice, the far side seems nearer at last — or does it? You can't be sure of anything any more. The dark plays tricks, and so do your tired eyes, and so does the wind. And you're a long way now from either edge, with the drop on both sides."},
  "c": ["Nearly across.", "The snow cracks under you."]},
 51: {"t": {
  "A2": "The cornice, the dark, the long drop below — and a crack runs out from under your foot. This is the moment. You can go down with the snow into the dark. Or you can throw yourself back from the crack, while you still can.",
  "B1": "The cornice, the dark, the long drop below — and a crack runs out from under your foot. This is the moment. You can go down with the snow into the dark. Or you can throw yourself back from the crack, while you still can.",
  "B2": "The cornice, the dark, the long drop below — and a crack runs out, fast, from under your front foot. This is the moment, and it is a short one. You can go down with the breaking snow into the dark. Or you can throw yourself back from the crack, right now, while you still can."},
  "c": ["You go with the cornice.", "Throw yourself back while you can."]},
 52: {"t": {
  "A2": "You reach the far side at last. You are soaked and shaking, your hands torn raw — but across. Somehow, you made it. Now you must decide. Push on, spent as you are? Or face what you lost out on the cornice?",
  "B1": "You reach the far side at last, soaked and shaking, your hands torn raw — but across. Somehow, you made it. Now you have to decide: push on, spent as you are, or face what you lost out on the cornice.",
  "B2": "You reach the far side at last, soaked and shaking, your hands torn raw on the ice — but across. Somehow, against the odds, you made it. Now you have to decide: push on, spent as you are, or face what you lost out there on the cornice in the dark."},
  "c": ["Push on, spent.", "You dropped the fuel out there."]},
 53: {"t": {
  "A2": "You throw yourself back from the crack while you still can — the hard, right choice. You crawl the last stretch on hands and knees. You reach the edge shaken and slow. The night isn't lost. But it cost you time you will miss.",
  "B1": "You throw yourself back from the crack while you still can — the hard, right choice. You crawl the last stretch on hands and knees, and reach solid ground shaken and slow. The night isn't lost. But it cost you time you'll miss.",
  "B2": "You throw yourself back from the crack while you still can — the hard choice, and the right one. You crawl the last stretch on hands and knees, and reach solid ground again shaken and slow. The night isn't lost. But it cost you time, out there, that you will badly miss."},
  "c": ["The long path after all.", "Too spent to go on."]},
 54: {"t": {
  "A2": "You try to get their stove going. You block the worst of the draughts with packs and an old board. It holds back a little of the cold. But there is still no lamp to leave them. And the night is far from over.",
  "B1": "You try to get their stove going, and block the worst of the draughts with packs and an old board. It holds back a little of the cold. But there's still no lamp to leave them, and the night is far from over.",
  "B2": "You try to get their little stove going, and block the worst of the draughts with packs and an old board jammed under the door. It holds back a little of the cold. But there's still no lamp to leave them, out here, and the night is a long way from over."},
  "c": ["Give them your own lamp and coat.", "Promise to send help."]},
 55: {"t": {
  "A2": "You hand over your own coat and lamp. The party huddle round the small flame. Relief spreads across their faces. The child stops crying at last. 'Thank you,' the mother says. Then she points you to a light, out on the slope.",
  "B1": "You hand over your own coat and lamp, and the party huddle round the small flame, relief spreading across their faces. The child stops crying at last. 'Thank you,' the mother says — and then she points you toward a light, out on the slope.",
  "B2": "You hand over your own coat and your lamp, and the party huddle round the small flame, relief spreading slowly across their faces. The child stops crying at last. 'Thank you,' the mother says, over and over — and then she points you toward a light, far out on the slope."},
  "c": ["On, colder now.", "Ask about the light on the slope."]},
 56: {"t": {
  "A2": "Without your coat, the cold and wet find you fast — teeth chattering, fingers going stiff. You gave it away to help, and you would do it again. But the storm doesn't care about any of that. It just bites harder.",
  "B1": "Without your coat, the cold and wet find you fast — teeth chattering, fingers going stiff. You gave it away to help, and you'd do it again. But the storm doesn't care about any of that. It just bites harder.",
  "B2": "Without your coat, the cold and the wet find you fast — teeth chattering, fingers going stiff and clumsy. You gave it away to help, and you'd do it again in a heartbeat. But the storm doesn't care about any of that. It just bites harder, and keeps on biting. You pull your collar up against it and go on."},
  "c": ["Keep moving, keep your head.", "A lit doorway offers a minute."]},
 57: {"t": {
  "A2": "A stranger waves you into a lit doorway. 'Just a minute,' they say. 'Out of the cold. Catch your breath.' It is warm and dry. Your whole body begs you to stay. But a minute like this can quietly slide into an hour.",
  "B1": "A stranger waves you into a lit doorway. 'Just a minute,' they say. 'Out of the cold — catch your breath.' It's warm and dry, and your whole body begs you to stay. But a minute like this can quietly slide into an hour.",
  "B2": "A stranger waves you into a lit doorway, out of the wind. 'Just a minute,' they say. 'Out of the cold — catch your breath.' It's warm and dry in there, and your whole body begs you to stay. But a minute like this one can slide, quietly and without your noticing, into an hour."},
  "c": ["Warm up, then on.", "Refuse, press on."]},
 58: {"t": {
  "A2": "You press on into the storm, chilled to the bone. The cold fights every step. Your eyes water and sting. Each step is a small battle on its own. But you keep them coming, one after another, toward the hut.",
  "B1": "You press on into the storm, chilled to the bone. The cold fights every step. Your eyes water and sting. Each step is a small battle on its own. But you keep them coming, one after another, toward the hut.",
  "B2": "You press on into the storm, chilled to the bone, the cold fighting you for every step, your eyes watering and stinging in the wind. Each step is a small battle on its own now. But you keep them coming, one after another after another, toward the hut and its window."},
  "c": ["The last of the watch.", "On toward the far store."]},
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
    print(f"batch C: wrote prose for {len(D)} nodes")


if __name__ == "__main__":
    main()
