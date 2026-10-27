#!/usr/bin/env python3
"""Phase 3 prose for Moving Day (episode-11), batch D: Act II part 1, nodes 40-58.
Run: python3 scripts/generators/phase3_ep11_d.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-11.json")

D = {
 40: {"t": {
  "A2": "Bray leans on the van, all friendly. 'Tell you what,' he says. 'I'll take the lot — stairs, heavy bits, all of it, done in half an hour. Put your feet up. Why do your back in?' His smile is wide. But his eyes are already on your stuff.",
  "B1": "Bray leans on the van, all friendly. 'Tell you what,' he says. 'I'll take the lot — stairs, heavy bits, all of it, done in half an hour. Just put your feet up. Why do your back in?' His smile is wide. But his eyes are already on your stuff.",
  "B2": "Bray leans on the van, all friendly. 'Tell you what,' he says. 'I'll take the whole lot — stairs, heavy bits, all of it, done in half an hour flat. Just say the word and put your feet up. Why do your back in?' His smile is wide and easy. But his eyes are already running over your stuff, pricing it up."},
  "c": ["Hear his price.", "Say no and carry on."]},
 41: {"t": {
  "A2": "'Good price,' Bray says, and names a sum that makes you blink. It's a lot. But he's quick, he's strong, and he's right here. No stairs, no strain, no risk to your back. So: pay him, turn him down, or ask him straight what his game is?",
  "B1": "'Good price,' Bray says, and names a sum that makes you blink. It's a lot of money. But he's quick, he's strong, and he's right here in front of you. No stairs, no strain, no risk to your back. So what's it to be — pay him, turn him down, or ask what his game is?",
  "B2": "'Good price,' Bray says, and names a sum that makes you blink. It's a lot of money, more than you'd budgeted. But he's quick, he's strong, and he's right here in front of you now. No stairs, no strain, no risk to your bad back. So what's it to be — pay him, turn him down flat, or ask him straight out what his game really is?"},
  "c": ["Pay him.", "Turn him down.", "Ask him straight.", "Watch who else pays."]},
 42: {"t": {
  "A2": "You say no thanks and turn back to the boxes. It feels good to turn him down. He calls after you, but you don't look round. His sort always find someone. But it won't be you, not today.",
  "B1": "You say no thanks and turn back to the boxes. It feels good to turn him down. He calls something after you, but you don't look round. His sort always find someone, in the end. But it won't be you, not today.",
  "B2": "You say no thanks and turn back to the boxes. It feels good to turn him down flat. He calls something after you, but you don't look round. His sort always find someone, in the end — someone tired and stuck enough. But it won't be you, not today. You go back to the stairs, and the honest work."},
  "c": ["Back to the stairs.", "Carry it in yourself."]},
 43: {"t": {
  "A2": "You shake on it and hand over the cash. The notes leave your hand, and part of you already knows. His smile grows. 'Smart move,' he says. But it doesn't feel smart. It feels like a small mistake, just starting.",
  "B1": "You shake on it and hand over the cash. The notes leave your hand, and part of you already knows. His smile grows. 'Smart move,' he says. But it doesn't feel smart at all. It feels like a small mistake, just starting.",
  "B2": "You shake on it and hand over the cash. The notes leave your hand, and part of you already knows the truth of it. His smile grows. 'Smart move,' he says. But it doesn't feel smart at all. It feels, standing there, like a small mistake being made — one you'll be paying for all evening."},
  "c": ["Let him load the van.", "A bad feeling already."]},
 44: {"t": {
  "A2": "You ask him straight: why so keen to help? He laughs. 'Easy money, love,' he says. 'Folk in a fix pay whatever I ask.' He laughs again. At least he's honest — and that tells you all you need to know.",
  "B1": "You ask him straight: why is he so keen to help? He laughs. 'Easy money, love,' he says. 'Folk in a fix pay whatever I ask.' He laughs again. At least he's honest — and that tells you all you need to know.",
  "B2": "You ask him straight out: why is he so keen to help? He laughs, quite openly. 'Easy money, love,' he says. 'Folk in a fix pay whatever I ask, don't they.' He laughs again. At least he's honest — and that, right there, tells you everything you need to know."},
  "c": ["That's your answer — no.", "Take it anyway."]},
 45: {"t": {
  "A2": "You let Bray load the van his way. But he throws it in fast and rough. Boxes on their sides, Mum's chair wedged under the heavy stuff. Nothing's safe in there. The whole thing already feels like a mistake.",
  "B1": "You let Bray load the van his way. But he throws it in fast and rough — boxes on their sides, Mum's chair wedged under the heavy stuff. Nothing's safe in there. The whole thing already feels like a mistake.",
  "B2": "You let Bray load the van his own way. But he throws it in fast and rough — boxes on their sides, Mum's good chair wedged under the heavy stuff. Nothing's safe in there at all. The whole thing already feels, in your stomach, like a mistake. You should have loaded it yourself."},
  "c": ["Try to sort it.", "Off to the new place with it."]},
 46: {"t": {
  "A2": "You look in the van, and your heart sinks. He's piled it in anyhow — glass boxes under the wardrobe, Mum's lamp on its side. Nothing will come out whole. You paid good money for this, and it's not worth it. The bad feeling in your gut was right.",
  "B1": "You look in the van, and your heart sinks. He's piled it in anyhow — glass boxes under the wardrobe, Mum's lamp on its side. Nothing will come out whole. You paid good money for this, and it's not worth it. The bad feeling in your gut was right all along.",
  "B2": "You look in the back of the van, and your heart sinks. He's piled it in anyhow — glass boxes crushed under the wardrobe, Mum's good lamp on its side. Nothing in there will come out whole. You paid good money for this, and it's not worth it. The bad feeling in your gut was right about him all along."},
  "c": ["To the new place anyway.", "Have it out with him."]},
 47: {"t": {
  "A2": "You turn to stop him, but Bray's already pulling away, your deposit in his pocket. He was never really helping. He saw someone stuck and in a hurry, and he cashed in. You've been had, plain and simple.",
  "B1": "You turn to stop him, but Bray's already pulling away, your deposit in his pocket. He was never really helping you. He saw someone stuck and in a hurry, and he cashed in. You've been had, plain and simple.",
  "B2": "You turn to stop him, but Bray's already pulling away from the kerb, your deposit in his pocket. He was never really helping you at all. He saw someone stuck and in a hurry, and he cashed in on it. You've been had, out here, plain and simple. The dusk settles, and the van's gone."},
  "c": ["To the new place, fooled.", "Shout after the van."]},
 48: {"t": {
  "A2": "He's gone, and the kerb is empty. Just the dusk now, and the money you handed him for nothing. You learned something today. And you paid too much for it. Now you carry on with less than you had.",
  "B1": "He's gone, and the kerb is empty — just the dusk now, and the money you handed him for nothing. You learned something today. And you paid far too much for it. Now you carry on with less than you started with.",
  "B2": "He's gone, and the kerb is empty — just the dusk now, the cold, and the money you handed him for nothing at all. You learned something today, out here. And you paid far too much for it. Now you carry on with less than you started with, and the light no kinder."},
  "c": ["On to the new place.", "Stand a moment at the kerb."]},
 49: {"t": {
  "A2": "Other tired movers are paying Bray too — cash in hand, glad to put their feet up. He takes it slow, with that same smile. He only ever helps the ones who pay the most.",
  "B1": "Other tired movers are paying Bray too — cash in hand, glad to put their feet up. He takes it slow, with that same smile. He only ever helps the ones who can pay the most.",
  "B2": "Other tired movers are paying Bray too — cash in hand, glad of any chance to put their feet up today. He takes it slow, unhurried, with that same wide smile. He only ever helps the ones who can pay him the most — and you see the whole of him in it."},
  "c": ["Hear his price anyway.", "Say no and carry on."]},
 50: {"t": {
  "A2": "You're halfway up the stairs now, the pile swaying in your arms. The landing looks close — or does it? You can't see the steps past the boxes. And you're a long way up, with no free hand.",
  "B1": "You're halfway up the stairs now, the pile swaying in your arms. The landing looks close — or does it? You can't see the steps past the boxes. And you're a long way up, with no free hand to grab the rail.",
  "B2": "You're halfway up the stairs now, the whole pile swaying in your arms. The landing looks close — or does it? You can't see the steps at all past the boxes. And you're a long way up, with no free hand to grab the rail if you slip. You keep climbing, and you do not look down."},
  "c": ["Almost there.", "The top box slips."]},
 51: {"t": {
  "A2": "The top box slides, and the whole pile lurches. This is the moment. You can grab for it and hope you keep your feet. Or you can let it go and save yourself, while you still can.",
  "B1": "The top box slides, and the whole pile lurches. This is the moment. You can grab for it and hope you keep your feet. Or you can let it go and save yourself, while you still can.",
  "B2": "The top box slides, and the whole pile lurches in your arms. This is the moment, and it's a short one. You can grab for it and hope you keep your feet on the steps. Or you can let the lot go and save yourself, right now, while you still can."},
  "c": ["You don't catch it.", "Let it go, save yourself."]},
 52: {"t": {
  "A2": "You reach the landing at last, arms shaking, heart going hard — but up. Somehow you made it. Now you must choose. Push on, shaken as you are? Or go back down for what you dropped on the stairs?",
  "B1": "You reach the landing at last, arms shaking, heart going hard — but up. Somehow you made it. Now you have to decide: push on, shaken as you are, or go back down for what you dropped on the stairs.",
  "B2": "You reach the landing at last, your arms shaking, your heart going hard against your ribs — but up. Somehow, against the odds, you made it. Now you have to decide: push on, shaken as you are, or go back down for the box you dropped on the stairs. Either way, the light will not wait."},
  "c": ["Push on, shaken.", "You dropped a box."]},
 53: {"t": {
  "A2": "You let the pile go and step clear just in time — the hard, right choice. The boxes tumble down; you stay on your feet. You're shaken, but whole. The move isn't lost. But you've lost time you'll miss — and you'll do it one at a time now.",
  "B1": "You let the pile go and step clear just in time — the hard, right choice. The boxes tumble down the stairs; you stay on your feet. You're shaken, but whole. The move isn't lost. But you've lost time you'll miss — and you'll do it one at a time now.",
  "B2": "You let the whole pile go and step clear just in time — the hard choice, and the right one. The boxes tumble down the stairs; you stay on your feet. You're shaken, but whole, and nothing of Mum's is broken. The move isn't lost. But you've lost time you'll badly miss — and you'll do it one at a time now, like you should have."},
  "c": ["One at a time now.", "Too shaken to go on."]},
 54: {"t": {
  "A2": "You try to help the young mum get started. Tape a box, take the baby a minute, shift the heavy things to the door. It helps a little. But she's barely begun, and you can't stay long. There's really only one thing you can do for her.",
  "B1": "You try to help the young mum get started — tape a box, take the baby a minute, shift the heavy things to the door. It helps a little. But she's barely begun, and you can't stay long. There's really only one thing you can do for her.",
  "B2": "You try to help the young mum get started — tape up a box, hold the baby a minute, shift the heavy things over to the door. It helps a little. But she's barely begun, and you can't stay long today. There's really only one thing left that you can do for her."},
  "c": ["Lend her your van and hands.", "Promise to come back."]},
 55: {"t": {
  "A2": "You run her boxes down in your van alongside your own, and her face changes. Two trips become one. The weight lifts off her. 'Thank you,' she says — then she tells you someone's been asking for you, downstairs.",
  "B1": "You run her boxes down in your van alongside your own, and her face changes. Two trips become one. The weight lifts off her. 'Thank you,' she says — and then she tells you that someone's been asking for you, downstairs.",
  "B2": "You run her boxes down in your van alongside your own, and her tired face changes all at once. Two trips become one. The weight lifts clean off her. 'Thank you,' she says, over and over — and then she tells you that someone's been asking for you, downstairs, by name."},
  "c": ["On, with less time now.", "Ask who's asking."]},
 56: {"t": {
  "A2": "With her load shifted too, your own time is tighter. Now the light is lower and the van's half yours. You helped because you could, and you'd do it again. But the dusk doesn't care about that. It just keeps falling.",
  "B1": "With her load shifted too, your own time is tighter. Now the light is lower and the van's half hers. You helped because you could, and you'd do it again. But the dusk doesn't care about any of that. It just keeps falling.",
  "B2": "With her load shifted too, your own time is that much tighter. Now the light is lower and the van's half hers. You helped because you could, and you'd do it again in a heartbeat. But the dusk doesn't care about any of that. It just keeps falling toward dark."},
  "c": ["Keep going, keep your head.", "A neighbour calls you in for tea."]},
 57: {"t": {
  "A2": "A neighbour waves you in for a cup of tea. 'Just five minutes,' they say. 'Sit down, warm up, catch your breath.' The room is warm. Your aching back begs you to stop. But five minutes can turn into twenty.",
  "B1": "A neighbour waves you in for a cup of tea. 'Just five minutes,' they say. 'Sit down, warm up, catch your breath.' It's warm and dry inside, and your aching back begs you to stop. But five minutes like this can quietly turn into twenty.",
  "B2": "A neighbour waves you in for a cup of tea out of the cold. 'Just five minutes,' they say. 'Sit down, warm up, catch your breath.' It's warm and dry in there, and your aching back begs you to stop a while. But five minutes like this one can quietly turn into twenty, with the light going.",
  }, "c": ["Warm up, then on.", "Say no, press on."]},
 58: {"t": {
  "A2": "You press on in the cooling dusk. Your arms are sore, your back stiff, the light in your head. Each box is a small effort now. But you keep them coming, one after another, toward the new flat and home.",
  "B1": "You press on in the cooling dusk, arms sore, your back stiff, the fading light in your head. Each box is a small effort now. But you keep them coming, one after another, toward the new flat and home.",
  "B2": "You press on in the cooling dusk, your arms sore, your back stiff, the fading light loud in your head. Each box is a small effort on its own now. But you keep them coming, one after another after another, toward the new flat and home. You will not stop until it's done."},
  "c": ["The last stretch.", "On up the stairs."]},
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
