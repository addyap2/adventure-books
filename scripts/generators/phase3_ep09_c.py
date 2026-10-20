#!/usr/bin/env python3
"""Phase 3 prose for The Dinner (episode-09), batch C: Act II part 1, nodes 40-58.
Run: python3 scripts/generators/phase3_ep09_c.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-09.json")

D = {
 40: {"t": {
  "A2": "Dale leans in close, all friendly. 'Cold out here,' he says. 'I've got the lot — chicken, spuds, all hot. Tip it in your dishes, no one knows. Why make trouble for yourself?' His smile is wide. But his eyes don't smile with it.",
  "B1": "Dale leans in close, all friendly. 'Cold out here,' he says. 'I've got the lot — chicken, spuds, all hot and ready. Tip it into your dishes, and no one's any the wiser. Why make all this trouble for yourself?' His smile is wide. But his eyes don't smile with it.",
  "B2": "Dale leans in close, all friendly. 'Cold out here,' he says. 'I've got the lot — chicken, spuds, all hot and ready to go. Tip it into your own dishes, and no one's ever any the wiser. Why make all this trouble for yourself, love?' His smile is wide and easy. But his eyes don't smile along with it, and you notice that."},
  "c": ["Hear his price.", "Say no and go round."]},
 41: {"t": {
  "A2": "'Fair price,' Dale says, and names a sum that makes you blink. It's a lot. But he's quick, he's hot, and he's right here. No shop, no cooking, no mess. So: pay him, turn him down, or ask him straight what his game is?",
  "B1": "'Fair price,' Dale says, and names a sum that makes you blink. It's a lot of money. But he's quick, he's hot, and he's right here in front of you. No shop, no cooking, no mess to clear up. So what's it to be — pay him, turn him down, or ask what his game is?",
  "B2": "'Fair price,' Dale says, and names a sum that makes you blink in the rain. It's a lot of money, more than the shop would ever charge. But he's quick, he's hot, and he's right here in front of you now. No shop, no cooking, no mess to clear up after. So what's it to be — pay him, turn him down flat, or ask him straight out what his game really is?"},
  "c": ["Pay him.", "Turn him down.", "Ask him straight.", "Watch who else pays."]},
 42: {"t": {
  "A2": "You say no thanks and walk on. It feels good to turn him down. He calls after you, but you don't look back. His sort always find someone. But it won't be you, not tonight.",
  "B1": "You say no thanks and walk on past him. It feels good to turn him down. He calls something after you, but you don't look back. His sort always find someone, in the end. But it won't be you, not tonight.",
  "B2": "You say no thanks and walk on past him into the rain. It feels good to turn him down flat. He calls something after you, but you don't look back. His sort always find someone, in the end — someone tired and frightened enough. But it won't be you, not tonight."},
  "c": ["On the way.", "To the shop instead."]},
 43: {"t": {
  "A2": "You take his food and hand over the money. Your hands close on the warm bags, and part of you already knows. His smile grows. 'Smart move,' he says. But it doesn't feel smart. It feels like a small lie starting.",
  "B1": "You take his food and hand over the money. Your hands close on the warm bags, and part of you already knows. His smile grows. 'Smart move,' he says. But it doesn't feel smart at all. It feels like a small lie, just starting.",
  "B2": "You take his food and hand over the money. Your hands close on the warm bags, and part of you already knows the truth of it. His smile grows. 'Smart move,' he says. But it doesn't feel smart at all. It feels, in the cold, like a small lie being told — one you'll have to keep telling all evening."},
  "c": ["Tip it into your dishes.", "A bad feeling already."]},
 44: {"t": {
  "A2": "You ask him straight: why so keen to help? He laughs. 'Easy money, love,' he says. 'A flop tonight, and you'll be back to mine next week.' He's honest, at least. That tells you all you need to know.",
  "B1": "You ask him straight: why is he so keen to help? He laughs. 'Easy money, love,' he says. 'A flop tonight, and you'll be back to mine next week.' He laughs again. At least he's honest — and that tells you all you need to know.",
  "B2": "You ask him straight out: why is he so keen to help? He laughs, quite openly. 'Easy money, love,' he says. 'And if your dinner's a flop tonight, you'll be back to mine next week, won't you.' At least he's honest about it — and that, right there, tells you everything you need to know."},
  "c": ["That's your answer — no.", "Take it anyway."]},
 45: {"t": {
  "A2": "You tip his food into your own dishes. But up close it looks wrong — greasy, grey, nothing like Gran's. It won't fool anyone at the table. The whole thing already feels like a mistake.",
  "B1": "You tip his food into your own dishes. But up close it looks all wrong — greasy, grey, nothing like Gran's cooking. It won't fool anyone at the table for a second. The whole thing already feels like a mistake.",
  "B2": "You tip his food into your own dishes and try to make it look like yours. But up close it looks all wrong — greasy, grey, and nothing at all like Gran's cooking. It won't fool anyone at that table for a second. And the whole thing already feels, in your stomach, like a mistake."},
  "c": ["Try to dress it up.", "To the table with it."]},
 46: {"t": {
  "A2": "You open the bag, and the smell hits you — cold grease, old fat, nothing fresh. This food won't pass for home cooking. You paid good money, and it's not worth it. The bad feeling in your gut was right.",
  "B1": "You open the bag, and the smell hits you — cold grease, old fat, nothing fresh about it. This food will never pass for home cooking. You paid good money for it, and it's not worth it. The bad feeling in your gut was right all along.",
  "B2": "You open the bag, and the smell hits you — cold grease, old fat, nothing fresh about any of it. This food will never pass for home cooking, not at Gran's table. You paid good money for it, out here in the rain, and it's not worth it. The bad feeling in your gut was right about him all along."},
  "c": ["To the table anyway.", "Go back and have words."]},
 47: {"t": {
  "A2": "You turn to find Dale, but he's already gone, off into the rain. He was never really helping. He just wanted the sale, and a flop tonight so you'd come back. You've been had, plain and simple.",
  "B1": "You turn to find Dale, but he's already gone, off into the rain. He was never really helping you. He just wanted the sale — and a flop tonight, so you'd come back to him. You've been had, plain and simple.",
  "B2": "You turn to find Dale, but he's already gone, melted off into the rain. He was never really helping you at all. He just wanted the sale — and a flop tonight, so you'd be back at his counter next week. You've been had, out here, plain and simple. The rain keeps on, and the money's gone with him."},
  "c": ["To the table, fooled.", "Bin the lot."]},
 48: {"t": {
  "A2": "He's gone, and the street is empty. Just the rain now, and the money you gave him for nothing. You learned something tonight. And you paid too much for it. Now you go on with less than you had.",
  "B1": "He's gone, and the street is empty — just the rain now, and the money you handed him for nothing. You learned something tonight. And you paid far too much for it. Now you go on with less than you started with.",
  "B2": "He's gone, and the street is empty — just the rain now, the dark, and the money you handed him for nothing at all. You learned something tonight, out here. And you paid far too much for it. Now you go on with less than you started with, and the clock no kinder."},
  "c": ["On to the kitchen.", "Stand a moment in the rain."]},
 49: {"t": {
  "A2": "Other tired people are buying from Dale too, hands full of money, glad of the easy way. He takes it slow, with that same smile. He only helps the ones who pay the most.",
  "B1": "Other tired people are buying from Dale too — hands full of money, glad of the easy way out. He takes it slow, with that same smile. He only ever helps the ones who can pay the most.",
  "B2": "Other tired people are buying from Dale too — hands full of money, glad of any easy way out tonight. He takes it slow, unhurried, with that same wide smile. He only ever helps the ones who can pay him the most — and you see the whole of him in it."},
  "c": ["Hear his price anyway.", "Say no and go round."]},
 50: {"t": {
  "A2": "You're halfway across the main road now. The far side looks close — or does it? The rain and the headlights play tricks. And you are a long way from both kerbs.",
  "B1": "You're halfway across the main road now. The far side looks close — or does it? The rain and the headlights play tricks on your eyes. And you're a long way from both kerbs, out in the middle.",
  "B2": "You're halfway across the main road now, and the far side looks close — or does it? The rain and the swinging headlights play tricks on your tired eyes. And you're a long way from both kerbs, out in the middle of it, with the traffic coming. You keep your feet moving, and you do not look down."},
  "c": ["Almost across.", "A car comes fast."]},
 51: {"t": {
  "A2": "A car comes fast out of the dark, its lights filling your eyes. This is the moment. You can keep going and hope it stops. Or you can jump back to the kerb, while you still can.",
  "B1": "A car comes fast out of the dark, its lights filling your eyes, its horn blaring. This is the moment. You can keep going and hope it stops in time. Or you can jump back to the kerb, while you still can.",
  "B2": "A car comes fast out of the dark, its lights filling your eyes, its horn blaring over the rain. This is the moment, and it's a short one. You can keep going and hope it stops in time. Or you can throw yourself back toward the kerb, right now, while you still can."},
  "c": ["You don't make it.", "Jump back while you can."]},
 52: {"t": {
  "A2": "You reach the far side at last, soaked and shaking — but across. Somehow you made it. Now you must choose. Push on, shaken as you are? Or go back for what you dropped in the road?",
  "B1": "You reach the far side at last, soaked and shaking, your heart going hard — but across. Somehow you made it. Now you have to decide: push on, shaken as you are, or go back for what you dropped in the road.",
  "B2": "You reach the far side at last, soaked and shaking, your heart going hard against your ribs — but across. Somehow, against the odds, you made it. Now you have to decide: push on, shaken as you are, or go back for the shopping you dropped out there in the road."},
  "c": ["Push on, shaken.", "You dropped the shopping."]},
 53: {"t": {
  "A2": "You jump back to the kerb just in time — the right, hard choice. The car roars past, close enough to feel. You stand there shaking, but safe. The night isn't lost. But you've lost time, and you'll go round now.",
  "B1": "You jump back to the kerb just in time — the hard, right choice. The car roars past, close enough to feel the wind of it. You stand there shaking, but safe. The night isn't lost. But you've lost time you'll miss — and you'll go the long way now.",
  "B2": "You throw yourself back to the kerb just in time — the hard choice, and the right one. The car roars past, close enough to feel the wind of it on your face. You stand there shaking, but safe. The night isn't lost. But you've lost time you'll badly miss — and you'll go the long way round now, like you should have."},
  "c": ["The long way after all.", "Too shaken to go on."]},
 54: {"t": {
  "A2": "You try to help with their dinner. Put a pan on, find what's in the cupboard, get something warm going. It helps a little. But they've next to nothing in, and you can't stay long. There's only one real thing you can do.",
  "B1": "You try to help with their dinner — put a pan on, see what's in the cupboard, get something warm started. It helps a little. But they've next to nothing in the house, and you can't stay long. There's really only one thing you can do for them.",
  "B2": "You try to help with their dinner — put a pan on, see what's in the near-empty cupboard, get something warm started for the kids. It helps a little. But they've next to nothing in the house, and you can't stay long tonight. There's really only one thing left that you can do for them."},
  "c": ["Give them your own food.", "Promise to send help."]},
 55: {"t": {
  "A2": "You hand over your own bags of food, and the family's faces change. The kids crowd round the table. The little one stops crying. 'Thank you,' the mum says — then she tells you someone's waiting at your gate.",
  "B1": "You hand over your own bags of food, and the family's faces change. The kids crowd round the table at the thought of a hot meal. The little one stops crying at last. 'Thank you,' the mum says — and then she tells you someone's been waiting at your gate.",
  "B2": "You hand over your own bags of food, and the family's tired faces change all at once. The kids crowd round the table at the thought of a hot meal. The little one stops crying at last. 'Thank you,' the mum says, over and over — and then she tells you someone's been waiting at your gate, in the rain."},
  "c": ["On, with less now.", "Ask who's at the gate."]},
 56: {"t": {
  "A2": "With your own food given away, your heart sinks a little. Now there's less for your own table. You gave it to help, and you'd do it again. But the clock doesn't care about that. It just keeps ticking.",
  "B1": "With your own food given away, your heart sinks a little. Now there's less for your own table at seven. You gave it to help, and you'd do it again. But the clock doesn't care about any of that. It just keeps ticking on.",
  "B2": "With your own food given away, your heart sinks a little in your chest. Now there's that much less for your own table at seven. You gave it away to help, and you'd do it again in a heartbeat. But the clock on the wall doesn't care about any of that. It just keeps ticking on toward the hour."},
  "c": ["Keep going, keep your head.", "A warm café offers a sit-down."]},
 57: {"t": {
  "A2": "A neighbour waves you into a warm café. 'Just five minutes,' they say. 'Sit down, dry off, have a cuppa.' It's warm in there. Your tired feet beg you to stop. But five minutes can turn into twenty.",
  "B1": "A neighbour waves you into a warm café. 'Just five minutes,' they say. 'Sit down, dry off, have a cup of tea.' It's warm and dry inside, and your tired feet beg you to stop. But five minutes like this can quietly turn into twenty.",
  "B2": "A neighbour waves you into a warm, bright café out of the rain. 'Just five minutes,' they say. 'Sit down, dry off, have a cup of tea.' It's warm and dry in there, and your cold, tired feet beg you to stop. But five minutes like this one can quietly turn into twenty, with the clock running."},
  "c": ["Warm up, then on.", "Say no, press on."]},
 58: {"t": {
  "A2": "You press on through the rain, cold and wet. Your bags are heavy, the clock in your head. Each step is a small effort now. But you keep them coming, one after another, toward home and the kitchen.",
  "B1": "You press on through the rain, cold and wet, your bags heavy, the clock ticking in your head. Each step is a small effort now. But you keep them coming, one after another, toward home and the warm kitchen.",
  "B2": "You press on through the rain, cold and wet to the skin, your bags heavy in your hands and the clock ticking loud in your head. Each step is a small effort on its own now. But you keep them coming, one after another after another, toward home and the warm, waiting kitchen."},
  "c": ["The last stretch.", "On toward the shop."]},
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
