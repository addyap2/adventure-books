#!/usr/bin/env python3
"""Phase 3: pour leveled prose into The Night Market skeleton.

Holds A2/B1/B2 prose for each node (and each choice, in skeleton order) in PROSE, then
writes it onto content/episode-02.json in place. Nodes absent from PROSE keep their stub,
so this grows batch by batch (Act I, II, III, endings); re-run after each and validate to
keep every level inside its CEFR band.

Run: python3 scripts/phase3_ep02.py
"""
import json, os, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BOOK = os.path.join(ROOT, "content", "episode-02.json")


def t(a2, b1, b2): return {"A2": a2, "B1": b1, "B2": b2}
PROSE = {}
def P(nid, text, choices): PROSE[nid] = {"text": text, "choices": choices}


# ============================ ACT I — LIGHTING UP ==========================

P(1,
  t("The market opens at dusk. Tonight the stall is yours. Auntie burned her hand two days ago, so she cannot cook. She has run pitch 24 for thirty years. The season's fee is due to the market master by dawn. If you do not pay it, the family loses the corner. You have never run the stall alone before.",
    "The market opens at dusk, and tonight the stall is yours. Auntie scalded her hand two days ago and cannot hold a ladle, so the cooking falls to you. She has run pitch 24 for thirty years. The season's fee is due to the market master by dawn — miss it, and the family loses the corner. You have never run the stall alone.",
    "The market opens at dusk, and tonight, for the first time, the stall is yours. Auntie scalded her hand badly two days ago and cannot so much as hold a ladle, so the whole night's cooking falls to you. She has held pitch 24 for thirty years. The season's fee is due to the market master by the time the lanterns go out at dawn — and if you don't pay it, the family loses the corner for good. You have never once run the stall on your own."),
  [t("Light the stall and start.", "Light the stall and get started.", "Light the stall and get started."),
   t("Call Auntie first.", "Call Auntie for instructions first.", "Call Auntie for instructions first."),
   t("Check the money and the fee.", "Check the money box and the fee.", "Check the money box and the fee owed.")])

P(2,
  t("You lift the shutter and light the burners. Blue flames catch under the big pot. You hang the two red lanterns. You wipe the counter and set out the bowls. The back shelf is empty, waiting. The market is waking up around you: voices, smoke, the smell of frying.",
    "You lift the shutter and light the burners; blue flames catch under the big pot. You hang the two red lanterns and wipe down the counter. On the back shelf, one space stands empty, waiting. All around you the market is waking — voices, smoke, the smell of hot oil and frying garlic.",
    "You lift the heavy shutter and light the burners, and blue flames catch, one by one, under the big pot. You hang the two red lanterns, wipe down the long counter, and set the bowls out in their stacks. On the back shelf, one space stands empty, as if it were waiting for something. All around you the market is coming awake — voices, smoke, the smell of hot oil and frying garlic."),
  [t("The tea woman says hello.", "The tea woman next door leans over.", "The tea woman next door leans over to you."),
   t("The supplier's van arrives.", "The supplier's van pulls up.", "The supplier's van pulls up at the kerb."),
   t("The big burner won't light.", "The big burner won't catch.", "The big burner splutters and won't catch.")])

P(3,
  t("You call Auntie. Her voice is tired but clear. \"Taste the broth before you sell it. Buy from Old Han, not the cheap van. And set a bowl aside for Mr Behn.\" You want to ask more. But she is in pain, and rings off.",
    "You call Auntie. Her voice is tired but clear. \"Taste the broth before you sell it. Buy from Old Han, not the cheap van. And set a bowl aside for Mr Behn.\" You want to ask what that last part means. But she is in pain, and she rings off before you can.",
    "You call Auntie, and her voice comes down the line tired but perfectly clear. \"Taste the broth before you sell a drop of it. Buy from Old Han, never the cheap van. And set one bowl aside, on the back shelf, for Mr Behn.\" You want to ask what that last part means, and who Mr Behn is. But she is in pain, and she rings off before you can get the question out."),
  [t("Ask about the good supplier.", "Ask about the good supplier.", "Ask her about the good supplier."),
   t("Ask what else to know.", "Ask what else you must know.", "Ask what else you need to know."),
   t("Taste the broth first.", "Taste her broth to learn it.", "Taste her broth to learn the balance.")])

P(4,
  t("You open the money box. Inside is a card in Auntie's hand. On it is the fee: the number you must reach by dawn. It is a big number. A bowl of broth is only a few coins. You count in your head. It will take a full, busy night to make it.",
    "You open the money box. Inside is a card in Auntie's writing, with the fee on it — the number you must reach by dawn. It's a big number, and a bowl of broth is only a few coins. You do the sum in your head: it will take a full, busy night to get there.",
    "You open the money box. Inside, in Auntie's careful hand, is a card with the fee written on it — the number you have to reach by the time the lanterns go out. It is a big number. A single bowl of broth is only a few coins, and you do the arithmetic in your head with a sinking feeling: it will take a full, hard, busy night to get anywhere near it."),
  [t("Match it by dawn. Cook.", "You must match it by dawn. Get cooking.", "You must match it by dawn. Get cooking."),
   t("Work out what a bowl earns.", "Work out what a bowl earns.", "Work out what a single bowl earns."),
   t("Auntie worries on the phone.", "Auntie frets down the line.", "Auntie frets away down the line.")])

P(5,
  t("The tea woman at pitch 25 leans over. She has sold tea here for years. \"So it's you tonight,\" she says, kindly. \"Your auntie's hand — how bad?\" She looks at your empty counter and your nervous hands, and she smiles. \"Don't worry. I'll keep an eye on you.\"",
    "The tea woman at pitch 25 leans over — she's sold tea on this corner for years. \"So it's you tonight,\" she says kindly. \"Your auntie's hand, how bad is it?\" She takes in your empty counter and your nervous hands, and smiles. \"Don't fret. I'll keep half an eye on you.\"",
    "The tea woman at pitch 25 leans over — she has sold tea on this corner longer than you've been alive. \"So it's you tonight,\" she says, kindly enough. \"Your auntie's hand — how bad is it?\" She takes in your empty counter and your visibly nervous hands, and something in her face softens. \"Don't fret. I'll keep half an eye on you.\""),
  [t("Talk with her a moment.", "Chat a moment.", "Chat with her a moment."),
   t("Go to the supplier.", "Get to the supplier.", "Get on to the supplier.")])

P(6,
  t("The supplier's van is here. Old Han has good pork and fresh greens, but they cost more. The cheap van next to him sells end-of-day stock. It is half the price. But some of it has turned, and it does not smell fresh. Good food costs money. Cheap food costs your name.",
    "The supplier's van pulls up. Old Han has good pork and fresh greens, but they cost more. Beside him, the cheap van is selling off end-of-day stock at half the price. Some of it has turned, though, and none of it smells quite fresh. Good stock costs money now. Cheap stock costs your name later.",
    "The supplier's van pulls up at the kerb. Old Han has good pork and greens, fresh that morning, but they cost more than you'd like. Beside him, the cheap van is selling off end-of-day stock at half the price. Some of it has quietly turned, though, and none of it smells the way it should. Good stock costs you money tonight. Cheap stock costs you the stall's name, which took thirty years to build."),
  [t("Buy the good stock.", "Buy the good stock.", "Buy the good stock from Old Han."),
   t("Buy the cheap stock.", "Buy the cheap stock to save money.", "Buy the cheap stock to save money."),
   t("Buy some of each.", "Buy a little of each.", "Buy a little of each, to hedge.")])

P(7,
  t("You ask about Mr Behn. The line goes quiet. \"An old friend,\" Auntie says at last. \"He used to come every night. Just keep his bowl. Please.\" There is something in her voice. You do not push. Some things wait for the right moment.",
    "You ask who Mr Behn is. The line goes quiet for a moment. \"An old friend,\" Auntie says at last. \"He used to come every night, and then he stopped. Just keep his bowl for me. Please.\" There's something under her voice you can't read. You don't push it.",
    "You ask who Mr Behn is, and the line goes quiet for a long moment. \"An old friend,\" Auntie says at last. \"He came every night for years, and then, one day, he stopped. Just keep his bowl for me. Please.\" There is something running under her voice that you can't quite read, and you decide not to push it. Some questions wait for their moment."),
  [t("Set his bowl aside now.", "Go and set his bowl aside.", "Go and set his bowl aside now."),
   t("Say you will, and go.", "Say you will, and hang up.", "Say you will, and hang up.")])

P(8,
  t("You work it out. One bowl earns only a few coins. The fee needs many, many bowls. You will have to sell all night, without stopping, and waste nothing. It can be done. Auntie does it every season. But she is fast, and you are not — not yet.",
    "You work it out. A single bowl earns only a few coins. The fee will take many, many bowls — a whole night of selling without a pause, and wasting nothing. It can be done; Auntie does it every season. But she is fast and sure, and you are neither, not yet.",
    "You work it out, and the sums are sobering. A single bowl earns only a few coins, so the fee will take many, many bowls — a whole night of selling without a pause, and not a scrap wasted. It can be done; Auntie does it every single season. But she is fast, and sure, and reads a crowd in a glance, and you are none of those things, not yet."),
  [t("Get cooking.", "Get cooking.", "Get cooking, then."),
   t("Ask the tea woman for tips.", "Ask the tea woman for tips.", "Ask the tea woman for some tips.")])

P(9,
  t("The tea woman tells you how the night goes. \"Busy at nine, busy again at midnight,\" she says. \"Price fair. Be quick. Don't waste.\" Then she lowers her voice. \"And Mr Sould will come. He offers help. Loans. A quiet word. Say no. His help is a hook.\"",
    "The tea woman runs you through the night. \"Busy about nine, busy again at midnight,\" she says. \"Price it fair, be quick, waste nothing.\" Then she drops her voice. \"And Mr Sould will come round. He'll offer help — a loan, a quiet word with a rival. Say no. His help is a hook.\"",
    "The tea woman runs you through the shape of the night. \"Busy about nine, quiet, then busy again at midnight,\" she says. \"Price it fair, be quick, and waste nothing.\" Then she drops her voice and leans in. \"And Mr Sould will come round, he always does. He'll offer to help — a loan, a quiet word with a rival, a fee smoothed over. Say no to all of it. His help is a hook, and the price is never named until it's too late.\""),
  [t("Thank her.", "Thank her.", "Thank her for the warning."),
   t("Sould is coming over now.", "Sould is already coming over.", "Sould is already coming over.")])

P(10,
  t("The good pork is pink and fresh. The greens are crisp and green. You store them in the cold box. It cost more than you wanted. But you can taste the difference already, and so will they. Good food is how Auntie kept this corner for thirty years.",
    "Old Han's pork is pink and fresh, his greens crisp and bright. You pack them into the cold box. It cost more than you'd have liked — but you can already taste the difference, and so will the customers. Good food is how Auntie has held this corner for thirty years.",
    "Old Han's pork is pink and fresh, his greens crisp and bright with the morning still on them. You pack it all carefully into the cold box. It cost more than you'd have liked — but you can already taste the difference it will make, and so, you're sure, will the customers. Good food, honestly made, is how Auntie has held this corner for thirty years, and you mean to hold it the same way tonight."),
  [t("Back to the stall.", "Back to the stall.", "Back to the stall."),
   t("Set up the counter.", "Set up the counter.", "Set up the counter.")])

P(11,
  t("The cheap stock is half the price. You carry it back. But the pork smells wrong, and the greens are going soft. You saved money. Did you save the wrong thing? A bad bowl is not cheap. A bad bowl is one lost customer, and everyone they tell.",
    "The cheap stock is half the price, so you carry it back to the stall. But the pork has a smell you don't trust, and the greens are already going soft. You saved money — but maybe the wrong money. A bad bowl isn't cheap: it's a lost customer, and everyone that customer tells.",
    "The cheap stock is half the price, so you carry it back to the stall telling yourself it will be fine. But the pork has a smell you don't quite trust, and the greens are already going soft at the edges. You saved money tonight — but perhaps the wrong money. A bad bowl is never really cheap: it costs you a customer, and everyone that customer ever mentions it to."),
  [t("Use it anyway.", "Use it anyway.", "Use it anyway."),
   t("Regret it.", "Regret it.", "Regret it already.")])

P(12,
  t("You buy some good and some cheap. It feels safe. Half your bowls will be fine. But half will be less than Auntie's best. On a slow night, that might be enough. On a busy night, one bad bowl at the wrong moment can turn the crowd. You will have to be careful.",
    "You buy some good and some cheap, to hedge your bets. It feels like the safe middle. But half your bowls will fall short of Auntie's best. And on a busy night, one weak bowl at the wrong moment can turn a whole crowd. You'll have to watch which stock goes into which bowl.",
    "You buy some of the good and some of the cheap, hedging your bets. It feels like the safe middle path. But half your bowls will fall short of Auntie's best, and on a busy night a single weak bowl at the wrong moment can turn a whole crowd against you. You'll have to keep careful track of which stock goes into which pot."),
  [t("Back to the stall.", "Back to the stall.", "Back to the stall."),
   t("Set up the counter.", "Set up the counter.", "Set up the counter.")])

P(13,
  t("The back shelf waits. Auntie keeps one bowl there every night, for Mr Behn. She has done it for years, even when he stopped coming. It is a small thing. It costs one bowl. But it is her habit, and habits like this are how people stay in each other's lives.",
    "The back shelf waits, empty. Every night for years, Auntie has kept one bowl there for Mr Behn — even now, even though he stopped coming a season ago. It's a small thing; it costs a single bowl. But it's her habit, and habits like that are how people stay in each other's lives.",
    "The back shelf waits, empty. Every night for years, without fail, Auntie has kept one bowl there for Mr Behn — even now, even though his stool has stood empty for a whole season. It is a small thing, and it costs you a single bowl of broth. But it is her habit, kept quietly when no one is watching, and habits like that are how people stay in one another's lives."),
  [t("Set a bowl aside, like Auntie.", "Set a bowl aside now, as she does.", "Set a bowl aside now, exactly as she does."),
   t("You're too busy for that.", "You're too busy for that.", "You're too busy for that tonight.")])

P(14,
  t("You thank her. \"We look after each other on this corner,\" she says. \"Your auntie would do the same for me. She has, many times.\" It is good to know you are not quite alone tonight. One friendly face is worth a lot when the crowd comes.",
    "You thank her. \"We look after each other on this corner,\" she says. \"Your auntie's done the same for me more times than I can count.\" It's good to know you're not alone tonight. One friendly face is worth a great deal once the crowd comes.",
    "You thank her, and mean it. \"We look after each other on this corner,\" she says simply. \"Your auntie's done the same for me more times than I could count.\" It's good to know you aren't quite alone tonight. One friendly face two feet away is worth a great deal once the crowd comes pressing in."),
  [t("Back to the stall.", "Back to the stall.", "Back to the stall."),
   t("Open for business.", "Open for business.", "Open for business.")])

P(15,
  t("A man in a clean coat stops at your counter. He smiles like an old friend. \"You must be Sim's family. Terrible, her hand. Don't worry. I look after this market. Anything you need tonight, you come to Mr Sould.\" His smile is warm. His eyes are not.",
    "A man in a clean coat stops at your counter, smiling like an old friend. \"You must be Sim's family. Terrible thing, her hand. Don't you worry — I look after this market. Anything you need tonight, you come straight to Mr Sould.\" His smile is warm. His eyes, you notice, are not.",
    "A man in a clean, pressed coat stops at your counter, smiling like an old friend you can't quite place. \"You must be Sim's family. Terrible thing, her hand. Don't you worry now — I look after this market, everyone on it. Anything you need tonight, anything at all, you come straight to Mr Sould.\" His smile is warm and easy. His eyes, you can't help noticing, are doing something else entirely."),
  [t("Hear him out.", "Hear him out.", "Hear him out."),
   t("Wave him off politely.", "Wave him off politely.", "Politely wave him off.")])

P(16,
  t("The stall is ready. The lanterns glow red. The broth steams. The bowls are stacked and waiting. Out in the market, the crowd is thick now, moving past in the smoke and noise. Some of them are hungry. Some of them will stop here. It is time to open.",
    "The stall is ready at last. The lanterns glow red, the broth steams, the bowls stand stacked and waiting. Out in the arcade the crowd is thick now, flowing past in the smoke and the noise and the smell of a hundred kitchens. Some of them are hungry. Some will stop here, if you're quick and the food is good.",
    "The stall is ready at last. The lanterns glow red overhead, the broth steams and mutters, the bowls stand stacked and waiting in their neat towers. Out in the arcade the crowd is thick now, flowing past in the smoke and the noise and the mingled smell of a hundred kitchens. Some of them are hungry. Some of them will stop here — if you're quick enough, and the food is good enough, and you don't lose your nerve."),
  [t("Open for business.", "Open for business.", "Open for business."),
   t("Set a bowl aside first.", "Set a bowl aside first.", "Set a bowl aside first."),
   t("The regulars want the usual.", "The regulars will want the usual.", "The regulars will want the usual.")])

P(17,
  t("You throw out the worst of the cheap stock. It hurts to waste money you already spent. But a bad bowl would hurt more. You keep the parts that still look good. The rest goes in the bin. Better a smaller night than a bad name. Auntie would do the same.",
    "You bin the worst of the cheap stock. It stings to throw away money you've already spent — but a bad bowl would cost far more. You keep what still looks and smells right, and the rest goes. Better a smaller night than a stained name. Auntie would have done exactly the same.",
    "You bin the worst of the cheap stock. It genuinely stings to throw away money you've already handed over — but a single bad bowl, on a night like this, would cost you far more than a few coins. You keep what still looks and smells right, and the rest goes in the bin without ceremony. Better a smaller, honest night than a stained name. Auntie would have done exactly the same."),
  [t("Back to the stall.", "Back to the stall.", "Back to the stall."),
   t("Open for business.", "Open for business.", "Open for business.")])

P(18,
  t("One bowl sits on the back shelf now, full and warm. It waits for a man who may not come. It looks small up there, and a little sad. But it also looks right. It is Auntie's stall, and this is how Auntie's stall has always been. You are keeping more than a business tonight.",
    "One bowl sits on the back shelf now, full and warm, waiting for a man who may never come. It looks small up there, and a little sad — but it also looks right. This is Auntie's stall, and this is how Auntie's stall has always been. You're keeping more than a business alive tonight.",
    "One bowl sits on the back shelf now, full and warm, waiting patiently for a man who may never come at all. It looks small up there, and a little sad — but it also, somehow, looks exactly right. This is Auntie's stall, and this is how Auntie's stall has always been, night after night, year after year. You are keeping more than a business alive tonight, though you couldn't yet say what."),
  [t("Open for business.", "Open for business.", "Open for business."),
   t("Back to the stall.", "Back to the stall.", "Back to the stall.")])

P(19,
  t("The big burner clicks and clicks but will not light. Gas hisses. No flame. You try again. Nothing. Without this burner, the broth stays cold, and cold broth sells nothing. Your hands are shaking a little. It is not a good start. But every cook has fought a bad burner before.",
    "The big burner clicks and clicks but won't light — gas hissing, no flame, nothing. You try again, and again. Without it the broth stays cold, and cold broth sells nothing to anyone. Your hands shake a little; it's not the start you wanted. But every cook alive has fought a stubborn burner before.",
    "The big burner clicks and clicks and simply won't light — gas hissing out, no flame, nothing at all. You try again, and then again, willing it. Without this burner the broth stays cold, and cold broth sells precisely nothing. Your hands are shaking a little now, and it is not the start you'd hoped for. But every cook who ever lived has fought a stubborn burner, and won."),
  [t("Coax it alight yourself.", "Coax it alight yourself.", "Coax it alight yourself."),
   t("The tea woman helps.", "The tea woman helps.", "The tea woman comes to help.")])

P(20,
  t("You taste the broth. Salt first, then ginger, then something deep and warm under it all. This is the taste people walk across the market for. This is thirty years of care in one spoon. You must not lose it tonight. Cook it the way she taught you, and the broth will do half the work.",
    "You taste the broth: salt first, then ginger, then a deep warm note under it all that you can't quite name. This is the taste people cross the whole market for. It's thirty years of care in a single spoonful, and you mustn't lose it tonight. Cook it the way she taught you, and the broth will do half your selling for you.",
    "You taste the broth: salt first, then ginger, then a deep warm note beneath it all that you couldn't name if you tried. This is the taste people cross the entire market for, elbowing through the crowd. It is thirty years of quiet care held in a single spoonful, and you must not lose it tonight of all nights. Cook it the way she taught you, exactly, and the broth will do half your selling for you."),
  [t("To the supplier.", "To the supplier.", "To the supplier."),
   t("Back to the stall.", "Back to the stall.", "Back to the stall.")])

P(21,
  t("Auntie keeps talking about the fee. \"Don't lose the corner,\" she says. \"My mother had it before me. Thirty years.\" You can hear the fear under her words. You tell her it will be fine. You are not sure it will be. But she needs to rest her hand, and worry helps no one tonight.",
    "Auntie keeps circling back to the fee. \"Don't lose the corner,\" she says. \"My mother had it before me — thirty years.\" You can hear the fear running under her words. You tell her it'll be fine, though you're not at all sure it will. But she needs to rest that hand, and worrying down the phone helps neither of you.",
    "Auntie keeps circling back to the fee, unable to let it go. \"Don't lose the corner,\" she says, and her voice thins. \"My mother had it before me. Thirty years, it's been ours.\" You can hear the fear running clear under her words now. You tell her it will be fine, though you are not remotely sure it will. But she needs to rest that scalded hand, and worrying at each other down the phone helps neither of you tonight."),
  [t("Reassure her, and cook.", "Reassure her, and cook.", "Reassure her, and cook."),
   t("Work out the numbers.", "Work out the numbers.", "Work out the numbers.")])

P(22,
  t("The regulars will come. They know Auntie's bowl by heart: how big, how hot, how much. If yours is different, they will feel it at once. You cannot be Auntie tonight. But you can make her bowl her way, and let it speak for her. That is the safest path through a busy night.",
    "The regulars will come, and they know Auntie's bowl by heart — the size, the heat, the price, the exact balance. If yours is different, they'll feel it in the first mouthful. You can't be Auntie tonight. But you can make her bowl her way and let it speak for her, and that's the safest path through a busy night.",
    "The regulars will come, and they know Auntie's bowl by heart — its size, its heat, its price, the exact balance of it on the tongue. If yours is different, even a little, they will feel it in the very first mouthful and say nothing and not come back. You can't be Auntie tonight. But you can make her bowl her way, and let it speak for her, and that is the safest path you have through a busy night."),
  [t("Open for business.", "Open for business.", "Open for business."),
   t("Ask who's who.", "Ask the tea woman who's who.", "Ask the tea woman who's who.")])

P(23,
  t("Your first big order: a family of six, all talking at once. Six bowls. Different ones for the children. It is a lot for your first hour. Take it slowly and get it right, and they will come back all season. Rush it and drop something, and your first story tonight is a bad one.",
    "Your very first big order: a family of six, all talking over each other. Six bowls, with small changes for the children. It's a lot to hold in your head in your first hour. Take it slowly and get it right, and they may come back all season. Rush it and drop something, and your first story of the night is a bad one.",
    "Your very first big order, and it's a hard one: a family of six, all talking over one another. Six bowls, with small changes for the children. It is a great deal to hold in your head in your first hour behind the counter. Take it slowly and get it exactly right, and they may come back all season. Rush it and drop a plate, and the first story told about you tonight is a bad one."),
  [t("Take it carefully.", "Take it carefully.", "Take it carefully, one bowl at a time."),
   t("Rush it through.", "Rush it through.", "Rush it through fast.")])

P(24,
  t("A small child stands at the counter, counting coins into a little pile. They are one coin short of a bowl. They look up at you, then down at the coins, then up again. It is a small moment. But how you answer it is the kind of thing a market remembers about a stall.",
    "A small child stands at the counter, counting coins into a careful little pile. They're one coin short of a bowl. They look up at you, then down at the coins, then up again, saying nothing. It's a tiny moment — but how you answer it is exactly the kind of thing a market remembers about a stall.",
    "A small child stands at the counter, counting coins into a careful little pile on the wood. They are one coin short of a single bowl. They look up at you, then down at the coins, then up again, and say nothing at all. It is the tiniest of moments. But how you answer it is precisely the kind of thing a market remembers, and repeats, about a stall."),
  [t("Serve them kindly.", "Serve them kindly.", "Serve them anyway, kindly."),
   t("Send them on.", "Shoo them on.", "Shoo them on.")])

# ============================ ACT I — FIRST CUSTOMERS ======================

P(31,
  t("The first real customers reach your counter, hungry and ready to pay. Now: what do you charge? Auntie has a price, fair and steady, that her regulars know. You could match it. You could go higher for the tourists. Or you could keep it low and sell more. The number you pick tonight is a kind of promise.",
    "The first real customers reach the counter, hungry and ready to pay. So — what do you charge? Auntie has a price, fair and steady, that all her regulars know by heart. You could match it, go higher for the tourists who don't know better, or keep it low and hope to sell more. The number you pick tonight is a kind of promise.",
    "The first real customers reach the counter, hungry and ready to hand over money. So — what do you charge them? Auntie has a price, fair and steady, that every one of her regulars knows by heart. You could match it exactly; you could go higher for the tourists, who won't know the difference; or you could keep it low and gamble on selling more. The number you settle on tonight is a kind of promise, and the market hears it."),
  [t("A fair price.", "A fair price.", "A fair price."),
   t("Charge high for tourists.", "Charge high for the tourists.", "Charge high for the tourists."),
   t("Auntie's usual price.", "Auntie's usual price.", "Auntie's usual price."),
   t("A big order arrives.", "A nervous first big order.", "A nervous first big order arrives.")])

P(32,
  t("You set a fair price — not too high, not too low. It feels honest, and honest is easy to defend. The customers nod and pay. No one argues with fair. It may not make the most each bowl. But it keeps people coming back, and a busy stall beats a greedy one every time.",
    "You set a fair price — not too high, not too low. It feels honest, and honest is easy to stand behind. The customers nod and pay without a fuss; no one argues with fair. It won't earn the most per bowl, but it keeps people coming back, and a busy stall beats a greedy one every single time.",
    "You set a fair price — not too high, not too low, the price you'd want to pay yourself. It feels honest, and honest is an easy thing to stand behind at midnight. The customers nod and pay without a murmur; nobody ever argues with fair. It won't earn the most on any single bowl, but it keeps people coming back through the smoke, and a busy stall beats a greedy one every single time."),
  [t("Serve them.", "Serve them.", "Serve them."),
   t("A grumble anyway.", "A grumble anyway.", "A grumble comes anyway.")])

P(33,
  t("You mark the price up. The tourists won't know. And more money per bowl means fewer bowls to reach the fee. It is tempting tonight. But word moves fast in a market. If the regulars hear you are charging double, they will feel cheated. And a stall that cheats does not hold a corner for thirty years.",
    "You mark the price up. The tourists won't know the difference, and more money per bowl means fewer bowls to reach the fee — tempting, on a night like this. But word travels fast down an arcade. If the regulars catch you charging double, they'll feel cheated, and a stall that cheats doesn't hold a corner for thirty years.",
    "You mark the price up. The tourists won't know the difference, and more money on each bowl means fewer bowls to reach the fee — genuinely tempting, on a night as tight as this one. But word travels fast down a crowded arcade. If the regulars catch you charging double, they will feel quietly cheated, and a stall that cheats its regulars does not hold a corner for thirty years."),
  [t("A grumble at the price.", "A grumble at the price.", "A grumble at the price."),
   t("Serve them.", "Serve them.", "Serve them.")])

P(34,
  t("You charge Auntie's usual price, to the penny. The first regular sees it, and something eases in his face. \"Same as always,\" he says, pleased. It tells them she is still here, in a way. The stall has not changed, even with her hand hurt. Sometimes the safest choice is also the right one.",
    "You charge Auntie's usual price, to the exact penny. The first regular clocks it, and something eases in his face. \"Same as always,\" he says, pleased. It tells them, in a small way, that she's still here — that the stall hasn't changed, even with her hand hurt. Sometimes the safest choice is also simply the right one.",
    "You charge Auntie's usual price, down to the exact penny. The first regular clocks it at once, and something visibly eases in his face. \"Same as always,\" he says, pleased. It tells them, in a small and wordless way, that she is still here — that the stall hasn't changed under new hands, even with hers hurt. Sometimes the safest choice turns out to be the right one as well."),
  [t("Serve them.", "Serve them.", "Serve them."),
   t("A regular smiles.", "A regular smiles.", "A regular smiles at you.")])

P(35,
  t("You ladle the broth, drop in the dumplings, and pass the first bowls across the counter. Steam rises into the cold air. Hands take the bowls. Coins fall into your box. It is working. You are actually doing it. For a moment, over the noise, you feel a small, fierce spark of pride.",
    "You ladle the broth, drop in the dumplings, and pass the first bowls across the counter. Steam climbs into the cold night air; hands take the bowls; coins drop into your box. It's working — you're actually doing it. And for a moment, over all the noise, you feel a small fierce spark of pride.",
    "You ladle the broth, drop in the dumplings, and pass the first bowls across the counter into waiting hands. Steam climbs into the cold night air; coins drop into your box one after another. It's working. You are actually, genuinely doing it. And for a moment, over all the noise and smoke, you feel a small, fierce, unexpected spark of pride."),
  [t("A customer loves it.", "A customer praises it.", "A customer praises it."),
   t("A customer says it's bland.", "A customer finds it bland.", "A customer finds it bland."),
   t("A child counts coins.", "A child counts out coins.", "A child counts out coins.")])

P(36,
  t("Someone grumbles that the price is too high. Heads turn. A grumble at a stall can spread, or it can die, depending on what you do next. You can drop the price back to fair and keep the peace. Or you can hold firm and hope the food speaks louder than one loud voice.",
    "Someone grumbles, loudly, that the price is too high. A few heads turn. A grumble at a stall can spread down the row or die on the spot, depending entirely on what you do next. You can drop it back to fair and keep the peace, or hold firm and trust the food to speak louder than one loud voice.",
    "Someone grumbles, loudly enough for others to hear, that the price is too high. A few heads turn your way. A grumble at a stall can spread down the whole row or die on the spot, depending entirely on what you do in the next few seconds. You can drop it back to fair and keep the peace, or you can hold firm and trust the food to speak louder than one loud, complaining voice."),
  [t("Drop it back to fair.", "Drop it back to fair.", "Drop it back to a fair price."),
   t("Hold firm.", "Hold firm.", "Hold firm.")])

P(37,
  t("A customer takes one mouthful and stops. \"That's the real thing,\" he says. \"Just like hers.\" He says it loud. A few people hear, and drift closer to your counter. Good food is its own best seller. One happy mouth can pull a whole queue behind it.",
    "A customer takes one mouthful and stops dead. \"That's the real thing,\" he says, surprised. \"Just like hers.\" He says it loud enough for others to hear, and a few people drift closer. Good food is its own best advertisement — one happy mouth can pull a whole queue in behind it.",
    "A customer takes one mouthful and stops dead, eyebrows up. \"That's the real thing,\" he says, genuinely surprised. \"Just like hers.\" He says it loud enough for the people around him to hear, and a few of them drift closer to your counter. Good food is its own best advertisement — one happy mouth, at the right moment, can pull a whole queue in behind it."),
  [t("The takings grow.", "The takings grow.", "The takings grow."),
   t("The crowd builds.", "The crowd builds.", "The crowd builds.")])

P(38,
  t("A customer frowns into the bowl. \"It's a bit flat,\" they say. \"Not like usual.\" Maybe it's the cheap stock. Maybe your hand with the ginger. Either way, it stings to hear. You can fix the seasoning now, before the next bowl. Or you can let it go and hope the rush hides it.",
    "A customer frowns down into the bowl. \"It's a bit flat,\" they say. \"Not like the usual.\" Maybe it's the cheap stock; maybe it's your hand with the ginger. Either way, it stings to hear on your first night. You can fix the seasoning now, before the next bowl, or let it go and hope the rush covers it.",
    "A customer frowns down into the bowl, unconvinced. \"It's a bit flat,\" they say. \"Not like the usual.\" Maybe it's the cheap stock talking; maybe it's your own unsteady hand with the ginger. Either way, it stings to hear on your first night alone. You can fix the seasoning right now, before the next bowl goes out, or you can let it slide and hope the rush covers it."),
  [t("The takings grow.", "The takings grow.", "The takings grow."),
   t("The crowd builds.", "The crowd builds.", "The crowd builds.")])

P(39,
  t("You glance at the money box between orders. There are coins in it now — real ones, earned by your own hands. It is not much yet, not against that fee. But it is a start, and a start is more than you had an hour ago. You close the lid and turn back to the steam and the crowd.",
    "Between orders, you steal a glance at the money box. There are coins in it now — real ones, earned by your own two hands. It's nowhere near the fee, not yet, but it's a start, and a start is a great deal more than you had an hour ago. You shut the lid and turn back to the steam and the crowd.",
    "Between orders, you steal a quick glance into the money box. There are coins in it now — real ones, earned by your own two hands in your own first hour. It's nowhere near the fee, not yet, not remotely. But it's a start, and a start is a great deal more than you had when the lanterns first went up. You shut the lid and turn back to the steam and the noise and the endless waiting faces."),
  [t("Count so far.", "Count so far.", "Count what you have so far."),
   t("The crowd builds.", "The crowd builds.", "The crowd builds.")])

P(40,
  t("You count quickly. It's a start — but only a start. At this rate, you will not reach the fee by dawn. You need the rush, and you need it soon: the big midnight crowd, hungry and quick to spend. Everything now depends on the next few hours. You breathe, and get ready.",
    "You count quickly, under the counter. It's a start — but only a start. At this rate you won't reach the fee by dawn; you need the rush, and you need it to be a good one. The big midnight crowd, hungry and quick to spend, is what makes or breaks a night like this. Everything now rides on the next few hours.",
    "You count quickly, under the lip of the counter. It's a start — but only a start, and a modest one. At this rate you won't come close to the fee by dawn; you need the rush, and you need it to be a good one. The big midnight crowd, hungry and quick to spend and forgiving of a queue, is what makes or breaks a night like this. Everything now rides on the next few hours, and you know it."),
  [t("Into the rush.", "Into the rush.", "On into the rush."),
   t("A word with the tea woman.", "A word with the tea woman.", "A quick word with the tea woman.")])

P(41,
  t("And then the crowd comes. Not a trickle now but a wave: office workers, families, night workers, all pouring in at once. The noise doubles. Ten faces wait at your counter, then twenty. Orders fly at you from every side. This is the rush. This is the night. Here it is.",
    "And then the crowd comes — not a trickle now but a wave. Office workers, families, night-shift workers, all pouring into the arcade at once, and the noise doubles. Ten faces wait at your counter, then twenty. Orders come flying at you from every side. This is the rush. This is the night. Here it comes.",
    "And then the crowd comes — not a trickle any more but a wave. Office workers, families, night-shift workers off the late trains, all pouring into the arcade at once, and the noise simply doubles. Ten faces wait at your counter, then twenty, then more than you can count. Orders come flying at you from every side at once. This is the rush. This is the whole night, arriving all together. Here it comes."),
  [t("Meet the rush.", "Meet the rush.", "Meet the rush head-on."),
   t("The arcade fills up.", "The arcade packs in.", "The arcade packs in tight."),
   t("Orders from all sides.", "Orders shouted from all sides.", "Orders shouted from all sides.")])


# ============================ apply ========================================
def main():
    book = json.load(open(BOOK, encoding="utf-8"))
    by_id = {n["id"]: n for n in book["nodes"]}
    applied, mism = 0, []
    for nid, p in PROSE.items():
        n = by_id.get(nid)
        if not n:
            print(f"!! node {nid} not in book", file=sys.stderr); continue
        n["text"] = p["text"]
        chs, pcs = n.get("choices") or [], p.get("choices") or []
        if len(chs) != len(pcs):
            mism.append((nid, len(chs), len(pcs))); continue
        for c, pc in zip(chs, pcs):
            c["text"] = pc
        applied += 1
    json.dump(book, open(BOOK, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"Applied prose to {applied} node(s).")
    for nid, a, b in mism:
        print(f"CHOICE MISMATCH §{nid}: book {a} vs prose {b}")


if __name__ == "__main__":
    main()
