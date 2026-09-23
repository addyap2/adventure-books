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


# ============================ ACT II — THE LONG RUSH =======================

P(42,
  t("The counter is three deep now. Hands wave money. Voices call orders over each other. Steam and smoke sting your eyes. You have two hands and twenty customers. You can work steadily and keep every bowl right. You can go faster and cut a corner. Or you can call for help before you drown.",
    "The counter is three deep now, hands waving money, voices calling orders over one another. Steam and smoke sting your eyes. You have two hands and twenty customers, and something has to give. You can work steadily and keep every bowl right, go faster and cut a corner, or call for help before you go under.",
    "The counter is three deep now — hands waving money, voices calling orders over one another, everyone at once. Steam and smoke sting your eyes and the noise is a wall. You have two hands and twenty hungry customers, and something has to give. You can work steadily and keep every single bowl right; you can go faster and cut a corner to survive; or you can call for a hand before you go under entirely."),
  [t("Work steadily. Keep it right.", "Work steadily, keep it right.", "Work steadily, and keep it right."),
   t("Go faster. Cut a corner.", "Rush it — cut a corner to go faster.", "Rush it — cut a corner to go faster."),
   t("Call for help.", "Call for a hand.", "Call for a hand.")])

P(43,
  t("The arcade is packed shoulder to shoulder. People push past with bags and children. The air is hot with steam and frying. Your little stall is an island in the noise. There is no time to think now, only to move. You take a breath and step into it.",
    "The arcade is packed shoulder to shoulder, people pushing past with bags and sleepy children. The air is thick and hot with steam and frying oil. Your little stall is an island in all the noise. There's no time to think now, only to move — so you take a breath and step into it.",
    "The arcade is packed shoulder to shoulder, people shoving past with bags and sleepy children hoisted on hips. The air is thick and hot with steam and frying oil and a hundred voices. Your little stall is an island of order in all the noise. There's no time to think now, only to move — so you take a breath, square your shoulders, and step into it."),
  [t("Meet the rush.", "Meet the rush.", "Meet the rush."),
   t("Work steadily.", "Work steadily.", "Work steadily.")])

P(44,
  t("You find a rhythm. Ladle, bowl, dumplings, coins, next. Your hands learn the moves and stop shaking. You look each person in the eye. You call them 'friend' like Auntie does. People feel it, and they smile. You are not just selling bowls now. You are winning a crowd, one face at a time.",
    "You find a rhythm at the burners: ladle, bowl, dumplings, coins, next. Your hands learn the moves and stop shaking. You catch each person's eye, call them 'friend' the way Auntie does, and they feel it and smile back. You're not just selling bowls now — you're winning a crowd, one face at a time.",
    "You find a rhythm at the burners, and it carries you: ladle, bowl, dumplings, coins, next. Your hands learn the moves and finally stop shaking. You catch each person's eye, call them 'friend' the way Auntie always does, and they feel the difference and smile back at you. You're not merely selling bowls any more — you're winning a crowd, one warmed face at a time, and it feels like flying."),
  [t("Work steadily. Win them over.", "Work steadily and win the crowd over.", "Work steadily, and win the crowd over."),
   t("Just keep up.", "Just keep up.", "Just try to keep up.")])

P(45,
  t("You speed up too much. One bowl goes out half-cooked. You short a customer their change, by accident or not. You tell yourself it's the rush, everyone does it. But cutting corners is a hole in a bucket. It leaks your good name, one small cut at a time, until there is none left.",
    "You speed up too much. One bowl goes out half-cooked; you short a customer their change, whether by accident or not. You tell yourself it's just the rush, that everyone does it. But cutting corners is a hole in the bucket — it leaks your good name, one small cut at a time, until there's none left.",
    "You speed up too much, and it shows. One bowl goes out half-cooked; you short a customer their change, whether quite by accident or not you couldn't say. You tell yourself it's only the rush, that everyone does it on a night like this. But cutting corners is a hole in the bucket — it leaks your good name quietly, one small cut at a time, until one night you look and there's none left."),
  [t("Keep going.", "Keep going.", "Keep going."),
   t("A customer notices.", "A customer notices.", "A customer notices."),
   t("You burn your hand.", "You burn your hand in the hurry.", "You burn your hand in the hurry.")])

P(46,
  t("You call out for help. Your voice cracks over the noise. Who can come? The market kid is near, quick on their feet, always hungry, always ready to run for a coin. Or the tea woman next door — but one glance shows she is as swamped as you. You have a second to choose.",
    "You call out for help, your voice cracking over the noise. But who can come? The market kid is near — quick on their feet, always hungry, always ready to run an errand for a coin. Or the tea woman next door, though one glance shows she's as swamped as you are. You've a second to choose.",
    "You call out for help, your voice cracking over the noise before you can stop it. But who is there to come? The market kid is near — quick on their feet, perpetually hungry, always ready to run an errand for a single coin. Or the tea woman next door, though one glance across shows she's every bit as swamped as you are. You have about a second to choose."),
  [t("Send the kid on an errand.", "Send the market kid on an errand.", "Send the market kid on an errand."),
   t("The tea woman is swamped too.", "The tea woman is swamped too.", "The tea woman is swamped too.")])

P(47,
  t("The rush rolls on and on. Your arms ache. Your back aches. But the money box is getting heavy, and that sound — coins on coins — keeps you going. Bowl after bowl, face after face. You are in the middle of it now, and holding. You did not think you could. But here you are.",
    "The rush rolls on and on. Your arms ache, your back aches — but the money box is getting heavy, and that sound, coins falling on coins, keeps you going. Bowl after bowl, face after face. You're in the thick of it now, and holding your own. You didn't think you could. But here you are.",
    "The rush rolls on and on and on. Your arms ache and your back aches — but the money box is growing satisfyingly heavy, and that sound, coins falling on coins, is what keeps you upright. Bowl after bowl, face after face, order after order. You're in the very thick of it now, and holding your own. You didn't think you could do this. But here you are, doing it."),
  [t("Keep serving.", "Keep serving.", "Keep serving."),
   t("A brief lull.", "A brief lull.", "A brief lull."),
   t("A regular asks for Auntie.", "A regular asks for Auntie.", "A regular asks after Auntie.")])

P(48,
  t("\"Hey — that's not right.\" The customer holds out their hand. They counted the change, and it is short. A few heads turn to watch. Your face goes hot. This is the moment. You can say sorry and fix it fast. Or you can argue, and hope they back down before more people hear.",
    "\"Hey — that's not right.\" The customer holds out their hand, palm up. They've counted the change, and it's short. A few heads turn to watch how you'll handle it. Your face goes hot. This is the moment: you can say sorry and fix it at once, or argue and hope they back down before more people hear.",
    "\"Hey — that's not right.\" The customer holds out their hand, palm up, unhurried. They've counted the change, and it's short. A few heads turn to watch how you'll handle it. Your face goes hot. This is the moment, and everyone near can feel it: you can say sorry and fix it at once, or you can argue and hope they back down before more people hear."),
  [t("Say sorry and fix it.", "Apologise and fix it.", "Apologise and fix it."),
   t("Argue it out.", "Brazen it out.", "Brazen it out.")])

P(49,
  t("You glance at the stock and your stomach drops. The pork is nearly gone. The greens are down to a handful. The night is not half over, and you are running out. You can make smaller bowls to stretch it. You can send someone for more. Or the steamer chooses for you and runs dry.",
    "You glance at the stock and your stomach drops. The pork is nearly gone, the greens down to a last handful. The night isn't half over, and already you're running out. You can make smaller bowls to stretch what's left, send someone out for more, or watch the steamer run dry and decide for you.",
    "You glance at the stock and your stomach drops. The pork is nearly gone, the greens down to a last sad handful. The night isn't even half over, and already you're running low. You can make smaller bowls to stretch what's left, you can send someone out for more, or you can let the steamer run dry and make the decision for you."),
  [t("Make smaller bowls.", "Eke it out in small bowls.", "Eke it out in smaller bowls."),
   t("Send for more.", "Send for more.", "Send out for more."),
   t("The steamer runs dry.", "The steamer runs dry.", "The steamer runs dry.")])

P(50,
  t("For a moment, the crowd thins. You can breathe. You wipe the sweat from your face and the counter clean. The lanterns swing a little in the wind. It will not last — the midnight rush is still to come. But a lull is a gift. Use it well, and be ready when the wave returns.",
    "For a moment the crowd thins, and you can breathe. You wipe the sweat off your face and the counter clean. The lanterns sway a little in the night wind. It won't last — the real midnight rush is still to come — but a lull is a gift. Use it well, and be ready when the wave rolls back in.",
    "For a moment the crowd thins out, and you can actually breathe. You wipe the sweat off your face and the counter down clean. The red lanterns sway a little in the cold night wind. It won't last — the real midnight rush is still to come — but a lull is a gift all the same. Use it well, wipe down, restock, and be ready when the wave rolls back in."),
  [t("Back to serving.", "Back to serving.", "Back to serving."),
   t("Take a breath.", "Take a breath.", "Take a breath."),
   t("A quiet stretch.", "A quiet stretch.", "A quiet stretch.")])

P(51,
  t("\"You're right — I'm sorry.\" You count the change again, slowly, and put the missing coin in their hand. \"Long night. Thank you for your patience.\" The customer softens. The watching heads turn away. A mistake fixed fast and kindly is not a black mark. It can even become a small point in your favour.",
    "\"You're right — I'm sorry.\" You count the change again, slowly this time, and press the missing coin into their hand. \"Long night. Thanks for your patience.\" The customer softens; the watching heads turn away. A mistake fixed fast and kindly isn't a black mark — handled well, it can even count a little in your favour.",
    "\"You're right — I'm sorry.\" You count the change out again, slowly and clearly this time, and press the missing coin into their hand. \"Long night. Thanks for your patience.\" The customer softens; the watching heads turn away, satisfied. A mistake fixed fast and kindly isn't a black mark at all — handled well, it can even end up counting a little in your favour."),
  [t("Back to serving.", "Back to serving.", "Back to serving."),
   t("On through the rush.", "On through the rush.", "On through the rush.")])

P(52,
  t("You lean on the counter and breathe. The box under it is heavy now — heavier than you dared hope an hour ago. You could count it, to see how close you are. Or you could save the counting for later. Get back in, while the crowd is here and hungry and spending.",
    "You lean on the counter and just breathe for a second. The box beneath it is heavy now — heavier than you'd dared hope an hour ago. You could stop and count it, to see how close you are to the fee. Or you could save the counting for later and get back in while the crowd is here and spending.",
    "You lean on the counter and just breathe for a second or two. The box beneath it is heavy now — heavier than you'd have dared hope an hour ago. You could stop and count it, to see how close you are to the fee. Or you could save the counting for later and get straight back in, while the crowd is still here and hungry and spending."),
  [t("Count so far.", "Count so far.", "Count what you have."),
   t("Back in.", "Back in.", "Back in, then.")])

P(54,
  t("\"The change was right,\" you say, and hold their eye. The customer stares, then shrugs and walks off, muttering. You won — but you didn't. They will tell people. In a market, a name travels faster than any customer. You saved one coin tonight and spent something worth far more than a coin.",
    "\"The change was right,\" you say, and hold their eye until they look away. The customer stares, then shrugs and walks off muttering. You won — except you didn't. They'll tell people, and in a market a name travels faster than any customer. You saved a single coin tonight, and spent something worth far more.",
    "\"The change was right,\" you say flatly, and hold their eye until they look away. The customer stares a moment, then shrugs and walks off muttering to whoever will listen. You won the argument — except that you didn't, not really. They'll tell people, and in a market a name travels faster and further than any single customer. You saved yourself one coin tonight, and spent something worth a great deal more."),
  [t("Back to serving.", "Back to serving.", "Back to serving."),
   t("On through the rush.", "On through the rush.", "On through the rush.")])

P(55,
  t("You press coins into the kid's hand and send them running for more pork and greens. They know every back way in the market and are gone before you finish the sentence. Now you must hold the stall alone until they return. You hope the stock lasts. You hope the kid is quick and honest. You think they are.",
    "You press coins into the kid's hand and send them running for more pork and greens. They know every back way in the market and are gone before you've finished the sentence. Now you must hold the stall alone until they're back. You hope the stock lasts, and that the kid is as quick and honest as you think.",
    "You press coins into the kid's grubby hand and send them running for more pork and greens. They know every back way and shortcut in the market, and are gone before you've even finished the sentence. Now you must hold the stall alone until they get back — hoping the stock lasts the gap, and that the kid is every bit as quick and honest as you've decided to believe."),
  [t("The kid returns, hungry.", "The kid returns, hungry.", "The kid returns, hungry."),
   t("On through the rush.", "On through the rush.", "On through the rush.")])

P(56,
  t("You make the bowls a little smaller. More broth, fewer dumplings, a touch less pork. Most people won't notice on a busy night. It stretches your stock and buys you time. It is not cheating — the bowl is still good, still honest. It is just a cook being careful with what she has. Auntie would nod.",
    "You make the bowls a little smaller — more broth, fewer dumplings, a touch less pork. Most people won't notice on a night this busy. It stretches your stock and buys you time. It isn't cheating; the bowl is still good, still honest and hot. It's just a cook being careful with what she's got, and Auntie would nod at that.",
    "You make the bowls a little smaller — more broth, fewer dumplings, a touch less pork in each. Most people won't notice a thing on a night this busy. It stretches your dwindling stock and buys you precious time. It isn't cheating; the bowl is still good, still honest and hot and generous enough. It's just a cook being careful with what she has, and Auntie would nod at that."),
  [t("On through the rush.", "On through the rush.", "On through the rush."),
   t("A quiet moment.", "A quiet moment.", "A quiet moment.")])

P(57,
  t("The rush rolls on. You lose track of time inside it. Just steam, faces, bowls, coins, and the burn of the burners on your arms. Somewhere out there it is getting late. Somewhere the fee is still waiting. But right now there is only the next bowl, and the next, and the next.",
    "The rush rolls on, and you lose track of time inside it. Just steam, faces, bowls, coins, and the heat of the burners on your arms. Somewhere out there it's getting late; somewhere the fee is still waiting to be met. But right now there's only the next bowl, and the next, and the next.",
    "The rush rolls on, and you lose all track of time somewhere inside it — just steam, faces, bowls, coins, and the steady heat of the burners on your bare arms. Somewhere out there the night is getting late; somewhere the fee still sits waiting to be met. But right now there is only the next bowl, and the next after that, and the next."),
  [t("The tea woman's urn spills.", "The tea woman's urn spills.", "The tea woman's urn spills."),
   t("A quiet moment.", "A quiet moment.", "A quiet moment.")])

P(58,
  t("A crash next door. The tea woman's big urn has gone over. Hot tea everywhere, her stall in chaos, a queue of cross customers. She looks across at you, just for a second. She would never ask. But she helped you all night, in small ways. You have your own crowd. You have seconds to decide.",
    "A crash next door. The tea woman's big urn has gone over — hot tea everywhere, her stall in chaos, a queue of cross customers building. She glances across at you, just for a second, and looks away. She'd never ask. But she's helped you all night in small ways, and you have your own crowd waiting. Seconds to decide.",
    "A crash next door. The tea woman's big urn has gone clean over — hot tea everywhere, her stall in sudden chaos, a queue of cross customers building fast. She glances across at you, just for a second, and then looks away. She would never ask. But she's helped you all night in a dozen small ways, and you have your own crowd waiting and your own fee to make. Seconds to decide."),
  [t("Help her right now.", "Drop everything and help her.", "Drop everything and help her."),
   t("You can't. Keep serving.", "You can't; keep serving.", "You can't — keep serving.")])

P(59,
  t("In a gap between customers, your eye falls on the back shelf. The saved bowl sits there, going cold. Below it, the end stool stands empty, as it has all night. Mr Behn's stool. Who is he? Why does Auntie keep his bowl? The rush pulls at you. But the empty stool pulls too, in a quieter way.",
    "In a gap between customers, your eye falls on the back shelf. The saved bowl sits there, slowly going cold. Below it, the end stool stands empty, as it has all night — Mr Behn's stool. Who is he? Why does Auntie still keep his bowl? The rush pulls at you, but the empty stool pulls too, in a quieter way.",
    "In a brief gap between customers, your eye falls on the back shelf. The saved bowl sits there, slowly going cold. Below it, the end stool stands empty, as it has all night long — Mr Behn's stool. Who is he? Why does Auntie still keep a bowl for a man who never comes? The rush keeps pulling at you, but the empty stool pulls too, in its own quieter way."),
  [t("Check the saved bowl.", "Check the saved bowl.", "Go and check the saved bowl."),
   t("Back to work.", "Back to work.", "Back to work."),
   t("The stool, empty all night.", "The stool has been empty all night.", "The stool has been empty all night.")])

P(60,
  t("At last the rush peaks and breaks. The crowd thins from a wave to a trickle. You look up, blinking, like someone coming out of deep water. You are still standing. The stall is still yours. But the night is not done with you yet. Something always comes in the quiet after a rush.",
    "At last the rush peaks and breaks. The crowd thins from a wave to a trickle, and you look up, blinking, like someone surfacing from deep water. You're still standing; the stall is still yours. But the night isn't done with you yet — something always comes in the quiet after a rush.",
    "At last the rush peaks and breaks. The crowd thins from a wave to a trickle, and you look up, blinking, like someone surfacing from deep water into air. You're still standing. The stall is still yours, the box still filling. But the night is not done with you yet — something always comes in the strange quiet after a rush."),
  [t("Stock is nearly gone.", "The stock is nearly gone.", "The stock is nearly gone."),
   t("Rain sweeps in.", "Rain sweeps the arcade.", "Rain sweeps the arcade."),
   t("A rival stall undercuts you.", "A new stall opposite undercuts you.", "A new stall opposite undercuts you.")])

P(26,
  t("Orders come from every side at once. \"Two bowls!\" \"Extra dumplings!\" \"How long?\" You can't hold them all in your head. You need a system, fast: take them in order, say each one back, keep the line moving. Panic loses bowls. Calm keeps them. You pick calm, and start again from the front.",
    "Orders fly at you from every side at once. \"Two bowls!\" \"Extra dumplings!\" \"How long's the wait?\" You can't possibly hold them all in your head. You need a system, and fast: take them in order, say each one back, keep the line moving. Panic loses bowls; calm keeps them. You choose calm and start again from the front.",
    "Orders fly at you from every side at once. \"Two bowls!\" \"Extra dumplings!\" \"How long's the wait?\" You can't possibly hold them all in your head at speed. You need a system, and you need it fast: take them in strict order, say each one back aloud, keep the line moving. Panic loses bowls; calm keeps them. You choose calm, breathe, and start again from the front of the queue."),
  [t("Meet the rush.", "Meet the rush.", "Meet the rush."),
   t("Work steadily.", "Work steadily.", "Work steadily.")])

P(27,
  t("\"Where's Sim?\" a regular asks, looking for her face. \"Is she all right?\" You can tell the truth. Or you can just smile and serve, and keep it light. People come here for the food. But they also come for her.",
    "\"Where's Sim?\" a regular asks, looking past you for her face. \"Is she all right?\" You can tell the truth — her hand, the burn, you standing in tonight. Or just smile, serve, and keep it light. People come here for the food, but they come for her too. How you answer says what kind of stall this is tonight.",
    "\"Where's Sim?\" a regular asks, craning past you for her face. \"Is she all right?\" You can tell the truth — her hand, the burn, you standing in for her tonight. Or you can just smile and serve and keep it light. People come here for the food, of course, but a good few of them come for her. How you answer says what kind of stall this is going to be tonight."),
  [t("Tell the truth.", "Tell them the truth.", "Tell them the truth."),
   t("Just serve and smile.", "Just serve, and smile.", "Just serve, and smile.")])

P(28,
  t("Hot broth splashes your hand. You gasp. It burns, sharp and sudden — the same way Auntie hurt hers, you think wildly. Just like her. For a second the pain fills the world. Then you breathe. You wrap it in a wet cloth. The stall does not stop for a burn. You can push through, or let the tea woman look.",
    "Hot broth splashes across your hand and you gasp. It burns, sharp and sudden — the same way Auntie hurt hers, you think wildly. Just like her. For a second the pain fills the whole world. Then you breathe, and wrap it in a wet cloth. The stall doesn't stop for a burn. You can push through, or let the tea woman take a look.",
    "Hot broth splashes across the back of your hand and you gasp aloud. It burns, sharp and sudden — the very same way Auntie hurt hers, you think wildly. Just like her. For a second the pain fills the whole world and whites everything out. Then you breathe, and wrap it in a wet cloth. The stall doesn't stop for a burn, not tonight. You can push through it, or let the tea woman take a proper look."),
  [t("Wrap it. Carry on.", "Wrap it and carry on.", "Wrap it and carry on."),
   t("The tea woman helps.", "The tea woman helps.", "Let the tea woman help.")])

P(29,
  t("The steamer hisses and goes quiet. Dry. No water left, and the dumplings inside only half done. You catch it just in time. A minute more and they would have burned, and the smell of burning would empty your counter fast. You refill it, fast and careful. A small save. But small saves add up on a long night.",
    "The steamer hisses and falls quiet — bone dry, the dumplings inside only half done. You catch it just in time. A minute more and they'd have burned, and the smell of burning empties a counter faster than anything. You refill it fast, and carefully. A small save — but small saves add up over a long night.",
    "The steamer hisses and falls suddenly quiet — bone dry, the dumplings stacked inside only half done. You catch it just in time. A minute more and they'd have burned, and the smell of burning dumplings empties a counter faster than almost anything. You refill it fast, and carefully, hands steady now. A small save — but small saves are what add up, one after another, over a long night."),
  [t("Eke it out.", "Eke it out.", "Eke it out."),
   t("On through the rush.", "On through the rush.", "On through the rush.")])

P(30,
  t("A quieter stretch. You wipe down, restock the bowls, straighten the counter. In the calm, your mind drifts to the fee, the empty stool, Auntie's worried voice on the phone. Then a customer appears, and you are back in it. But the quiet stretches are where you think, and thinking is how you last the night.",
    "A quieter stretch. You wipe down, restock the bowls, straighten the counter. In the calm, your mind drifts — to the fee, the empty stool, Auntie's worried voice on the phone. Then a customer appears and you're back in it. But the quiet stretches are where you think, and thinking is how you last a whole night.",
    "A quieter stretch, at last. You wipe down, restock the bowls, straighten the counter into order. In the sudden calm your mind drifts — to the fee, to the empty stool, to Auntie's worried voice down the phone. Then a customer appears out of the smoke and you're back in it. But the quiet stretches are where you actually think, and thinking, tonight, is how you'll last until dawn."),
  [t("Take a breath.", "Take a breath.", "Take a breath."),
   t("On through the rush.", "On through the rush.", "On through the rush.")])

# --- the fixer, Mr Sould ---
P(61,
  t("Mr Sould leans on your counter, easy and slow. \"Hard night, running it alone,\" he says. \"I can help. A small loan to cover the fee. Or a quiet word with that rival across the way. I look after people who look after me.\" He waits, still smiling. Behind him, other stallholders line up to pay him.",
    "Mr Sould leans on your counter, easy and slow. \"Hard night, running it all alone,\" he says. \"I can help. A small loan to cover the fee, say. Or a quiet word with that rival across the way. I look after people who look after me.\" He waits, still smiling. Behind him, other stallholders queue up to hand him money.",
    "Mr Sould leans on your counter, easy and unhurried. \"Hard night, running it all on your own,\" he says, warm as ever. \"I can help, you know. A small loan to cover the fee, perhaps. Or a quiet word with that rival across the way — I can make trouble go away. I look after people who look after me.\" He waits, still smiling. Behind him, a line of other stallholders waits to hand him money."),
  [t("Hear the offer.", "Listen to the offer.", "Listen to the offer."),
   t("Say no now.", "Refuse now.", "Refuse him now."),
   t("Others line up to pay him.", "Stallholders line up to pay him.", "Stallholders line up to pay him.")])

P(62,
  t("\"Just a loan,\" Sould says. \"Pay the fee tonight, pay me back later. Easy.\" He never says the interest. He never says what 'later' costs. His help is real — but so is the hook inside it. You could take the money and breathe easy tonight. Or ask what it really costs. Or just walk away.",
    "\"Just a loan,\" Sould says smoothly. \"Pay the fee tonight, pay me back later. Easy.\" He never mentions the interest. He never says what 'later' will cost you. His help is real enough — but so is the hook buried inside it. You could take the money and breathe easy tonight, ask what it really costs, or simply walk away.",
    "\"Just a loan,\" Sould says smoothly, spreading his hands. \"Pay the fee tonight, pay me back later. Easy.\" He never once mentions the interest. He never says what 'later' will actually cost you. His help is real enough — but so is the hook buried carefully inside it. You could take the money and breathe easy tonight; you could ask what it really costs; or you could simply walk away."),
  [t("Take the loan.", "Take the loan.", "Take the loan."),
   t("Refuse it.", "Refuse it.", "Refuse it."),
   t("Ask what it costs.", "Ask what it costs.", "Ask what it really costs.")])

P(63,
  t("\"No, thank you,\" you say. \"We'll manage.\" Sould's smile stays, but his eyes cool. \"Suit yourself,\" he says, and moves on to the next stall. You feel lighter the moment he goes. Whatever happens tonight, it will be yours — the win or the loss, but no one's hook in you. That is worth something.",
    "\"No, thank you,\" you say. \"We'll manage.\" Sould's smile holds, but his eyes cool a degree. \"Suit yourself,\" he says, and moves on to the next stall. You feel lighter the moment he's gone. Whatever happens tonight will be yours — the win or the loss, but nobody's hook in you. That's worth something.",
    "\"No, thank you,\" you say, as steadily as you can manage. \"We'll manage.\" Sould's smile holds, but his eyes cool by a degree. \"Suit yourself,\" he says lightly, and moves on to the next stall down. You feel lighter the moment he's gone. Whatever happens tonight will be yours — the win or the loss, but nobody's hook set in you. That, you're fairly sure, is worth something."),
  [t("Back to the stall.", "Back to the stall.", "Back to the stall."),
   t("Into the night's work.", "Into the night's work.", "Back into the night's work.")])

P(64,
  t("You take Sould's money. The fee is covered now, whatever the night does. For one moment, the weight lifts, and you can breathe. Then the unease creeps in. You did not read the terms. You do not know what 'later' means. You have traded one worry for another — and this one has a smile and knows your name.",
    "You take Sould's money. The fee's covered now, whatever else the night does. For a moment the weight lifts and you can breathe. Then the unease creeps in. You didn't read any terms; you don't know what 'later' really means. You've traded one worry for another — and this one has a smile, and knows exactly where to find you.",
    "You take Sould's money, and it's warm from his pocket. The fee is covered now, whatever else the night throws at you. For one blessed moment the weight lifts clean off your shoulders and you can breathe. Then the unease begins to creep in. You didn't read any terms; you don't know what 'later' really means. You've traded one worry for another — and this new one has a smile, and knows your name, and knows exactly where to find you."),
  [t("Back to the stall.", "Back to the stall.", "Back to the stall."),
   t("On toward closing.", "On toward closing.", "On toward closing.")])

P(65,
  t("\"What does it cost?\" you ask. Sould only smiles wider. \"Don't worry about that now,\" he says. \"We'll sort it out later. Friends always do.\" He won't name a number. That is the whole trick, right there. A real price you can weigh. A price with no number is a rope with no end. You see it clearly now.",
    "\"What does it cost?\" you ask. Sould only smiles wider. \"Don't you worry about that now,\" he says. \"We'll sort it out later. Friends always do.\" He won't name a number, and that's the whole trick, right there. A real price you can weigh up. A price with no number is a rope with no end. You see it clearly now.",
    "\"What does it cost?\" you ask him, plainly. Sould only smiles wider. \"Don't you worry about that now,\" he says. \"We'll sort it all out later. Friends always do.\" He won't name a number, and that, right there, is the whole trick. A real price you can weigh up and decide about. A price with no number attached is a rope with no end. You can see it clearly now, and you're glad you asked."),
  [t("That's the tell. Refuse.", "That's the tell — refuse.", "That's the tell — refuse."),
   t("Take it anyway.", "Take it anyway.", "Take it anyway.")])

P(66,
  t("You watch the line of stallholders wait to pay Sould. Some look calm. Some look tired, and a little afraid. One old woman counts her coins twice before she hands them over. This is how the market really works, under the lights and the noise. A quiet man, a long line, and money moving his way all night.",
    "You watch the line of stallholders waiting to pay Sould. Some look calm enough; others look tired, and a little afraid. One old woman counts her coins twice before she hands them over. This is how the market really works, under the lanterns and the noise. A quiet man, a long line, and money moving his way all night.",
    "You watch the line of stallholders waiting their turn to pay Sould. Some look calm enough about it; others look tired, and a little afraid. One old woman counts her coins twice over before she hands them across. This, you realise, is how the market really works, under the lanterns and the noise — a quiet man, a patient line, and money moving steadily his way all night long."),
  [t("Hear his offer.", "Hear his offer.", "Hear his offer."),
   t("A stallholder warns you.", "A stallholder warns you.", "A stallholder warns you quietly.")])

P(67,
  t("The stallholder beside you leans in. \"Whatever he offers, say no,\" she murmurs. \"Sould never forgets a debt. My cousin borrowed once. Three years, he paid. Three years.\" She straightens up as Sould glances over. \"Just... be careful,\" she says, and turns back to her stall. The warning sits cold in your chest.",
    "The stallholder beside you leans in close. \"Whatever he offers, say no,\" she murmurs. \"Sould never forgets a debt. My cousin borrowed once. Three years he paid it back. Three years.\" She straightens as Sould glances over. \"Just... be careful,\" she says, and turns back to her stall. The warning sits cold in your chest.",
    "The stallholder beside you leans in close, under the noise. \"Whatever he offers, say no,\" she murmurs. \"Sould never forgets a debt. My cousin borrowed from him once. Three years he spent paying it back. Three years.\" She straightens up quickly as Sould glances over. \"Just... be careful,\" she says, and turns back to her own stall. The warning sits cold and clear in your chest."),
  [t("Refuse him.", "Refuse him.", "Refuse him."),
   t("Still hear him out.", "Still hear him out.", "Still hear him out.")])

P(68,
  t("Near closing, Sould drifts back. \"Made the fee yet?\" he asks, gentle, like he cares. \"Because the offer's still open. Last chance tonight.\" He knows exactly how the night has gone for you. He always does. His loan would end the fear right now. But his loan never really ends. You know which way to answer.",
    "Near closing, Sould drifts back over. \"Made the fee yet?\" he asks, gentle, like he cares. \"Because the offer's still open. Last chance tonight.\" He knows exactly how the night has gone for you — he always does. His loan would end the fear right now. But his loan never really ends. You know which way you're going to answer.",
    "Near closing, Sould drifts back over, unhurried. \"Made the fee yet?\" he asks, gentle, as if he cares. \"Because the offer's still open. Last chance tonight.\" He knows exactly how the night has gone for you — he always does, that's his whole trade. His loan would end the fear right here, right now. But his loan never really ends, does it. You know which way you're going to answer."),
  [t("Take his loan.", "Take his loan.", "Take his loan."),
   t("Refuse. Take your chances.", "Refuse, and take your chances.", "Refuse, and take your chances.")])

# --- the kid ---
P(73,
  t("The kid comes back with the stock, breathing hard, proud to have been quick. Then they see the bowls, and the steam, and go still. They don't ask. They just look — the way hungry children look at food, trying not to. You have a bowl in your hand. You have a choice in the other.",
    "The kid comes back with the stock, breathing hard and proud to have been quick about it. Then they catch sight of the bowls, and the steam, and go very still. They don't ask for anything. They just look — the way hungry children look at food, trying hard not to. You've a bowl in one hand, and a choice in the other.",
    "The kid comes back with the stock, breathing hard and visibly proud to have been so quick about it. Then they catch sight of the bowls, and the rising steam, and go very still. They don't ask for anything, of course. They just look — the way hungry children look at food when they're trying hard not to be caught looking. You've a bowl in one hand, and a choice in the other."),
  [t("Give the kid a bowl.", "Give the kid a bowl.", "Give the kid a bowl."),
   t("Pay in coins only.", "Pay only in coins.", "Pay only in coins.")])

P(74,
  t("You hand the kid a full bowl. \"Eat,\" you say. \"You earned it.\" Their whole face changes. They eat fast, in the corner, like they're afraid it will vanish. It is one bowl. It costs you almost nothing. But to the kid it is the whole world for a moment. They will not forget who gave it.",
    "You hand the kid a full bowl. \"Eat,\" you say. \"You earned it.\" Their whole face changes. They eat fast, in the corner, as if afraid it might vanish. It's one bowl; it costs you almost nothing. But to the kid it's the whole world for a moment — and they won't forget who gave it to them.",
    "You hand the kid a full, hot bowl. \"Eat,\" you say. \"You earned it.\" Their whole face changes at once. They eat fast, hunched in the corner, as if afraid it might vanish before they finish. It's one bowl; it costs you almost nothing tonight. But to the kid it's the whole world for a few minutes — and they are not going to forget who gave it to them."),
  [t("Back to the rush.", "Back to the rush.", "Back to the rush."),
   t("The kid stays.", "The kid sticks around.", "The kid sticks around."),
   t("The kid tells you their name.", "The kid tells you their name.", "The kid tells you their name.")])

P(75,
  t("You pay the kid in coins, the way you agreed, and nothing more. They pocket them and nod. They understand. Coins are fair; coins are the deal. But they are still hungry, and they still look at the bowls as they go. You were fair tonight. Fair is fine. But fair is not the same as kind.",
    "You pay the kid in coins, as you agreed, and nothing more. They pocket them and nod — they understand; coins are the deal, and the deal is fair. But they're still hungry, and they still glance at the bowls as they turn to go. You were fair tonight. Fair is fine. But fair isn't quite the same as kind.",
    "You pay the kid in coins, exactly as you agreed, and nothing more than that. They pocket them and nod — they understand; coins are the deal, and the deal is fair enough. But they're still hungry, and they still glance back at the steaming bowls as they turn to go. You were fair tonight, perfectly fair. Fair is fine. But fair, you half-notice, isn't quite the same thing as kind."),
  [t("Back to the rush.", "Back to the rush.", "Back to the rush."),
   t("The kid stays.", "The kid sticks around.", "The kid sticks around.")])

P(76,
  t("The kid doesn't leave. They hang about at the edge of the stall. They watch, they learn, they fetch a cloth or a spoon before you ask. Having them near makes the work lighter. A market is full of people who slip through the cracks. Sometimes a stall is the one warm place that lets them stay.",
    "The kid doesn't leave. They hang about at the edge of the stall — watching, learning, fetching a cloth or a spoon before you even ask. Having them near makes the whole night's work feel lighter. A market is full of people who slip through the cracks, and sometimes a stall is the one warm place that lets them stay.",
    "The kid doesn't leave. They hang about at the edge of the stall — watching, learning, fetching a cloth or a spoon before you've even thought to ask. Having them near somehow makes the whole night's work feel lighter. A market is full of people who slip quietly through the cracks, and sometimes a single stall is the one warm place that lets them stand a while."),
  [t("Back to the rush.", "Back to the rush.", "Back to the rush."),
   t("On into the night.", "On into the night.", "On into the night."),
   t("The kid guards the stall.", "The kid guards the stall.", "The kid guards the stall.")])

P(77,
  t("Between bowls, the kid tells you their name. They tell you where they sleep — a dry corner behind the fish arch, most nights. They say it plainly, not asking for pity. You listen. You remember it. A name is a small thing to give and a big thing to hold. The market feels a little less like strangers now.",
    "Between bowls, the kid tells you their name. They tell you where they sleep, too — a dry corner behind the fish arch, most nights. They say it plainly, not fishing for pity. You listen, and you remember it. A name is a small thing to give and a big thing to hold, and the market feels a little less like strangers now.",
    "Between bowls, the kid tells you their name. They tell you where they sleep, too — a dry corner behind the fish arch, most nights, when the weather allows. They say it plainly, not fishing for pity, just offering it. You listen, and you remember it. A name is a small thing to give and a surprisingly big thing to hold, and the market feels a little less like a place full of strangers now."),
  [t("Back to the rush.", "Back to the rush.", "Back to the rush."),
   t("The kid stays.", "The kid sticks around.", "The kid sticks around.")])

P(78,
  t("You leave the kid to watch the stall while you duck to the back for more stock. It is a small trust, and they take it seriously. They stand tall, wave customers to wait, guard the money box with both eyes. When you come back, nothing is missing. Trust given and trust kept. It matters, in a place like this.",
    "You leave the kid to watch the stall while you duck out back for more stock. It's a small trust, and they take it seriously — standing tall, waving customers to wait, guarding the money box with both eyes. When you get back, nothing is missing. Trust given, trust kept — and that matters, in a place like this.",
    "You leave the kid to watch the stall while you duck out back for more stock. It's a small trust, and they take it entirely seriously — standing tall, waving customers to wait their turn, guarding the money box with both eyes at once. When you get back, nothing is missing, not a coin. Trust given, and trust kept — and that matters more than it sounds, in a place like this."),
  [t("Back to the rush.", "Back to the rush.", "Back to the rush."),
   t("On into the night.", "On into the night.", "On into the night.")])

# --- neighbour (result) ---
P(88,
  t("You leave your own counter and go to her. Together you right the urn, mop the hot tea, calm her cross customers, get her going again. It costs you a few minutes and a few sales. She grips your arm, breathless. \"I won't forget this,\" she says. And on this corner, that is not just words.",
    "You leave your own counter and go straight to her. Together you right the urn, mop up the hot tea, calm her cross customers, and get her going again. It costs you a few minutes and a few lost sales. She grips your arm, breathless. \"I won't forget this,\" she says — and on this corner, that isn't just words.",
    "You leave your own counter and go straight to her. Together you right the heavy urn, mop up the spreading hot tea, calm her cross customers, and get her going again. It costs you a few minutes and a handful of lost sales. She grips your arm, breathless and grateful. \"I won't forget this,\" she says — and on this corner, from her, that isn't just words."),
  [t("Back to your stall.", "Back to your stall.", "Back to your own stall."),
   t("On into the night.", "On into the night.", "On into the night.")])

# --- rain / stock / rival ---
P(79,
  t("Rain sweeps down the arcade, sudden and hard. It drums on the roofs and runs off the awnings. The crowd scatters for cover, and your counter empties in seconds. Rain can kill a night's trade. Or, handled right, it can fill your stall with cold, wet people who suddenly want something hot. It depends on you.",
    "Rain sweeps down the arcade, sudden and hard, drumming on the roofs and sheeting off the awnings. The crowd scatters for cover, and your counter empties in seconds. Rain can kill a night's trade stone dead. Or, handled right, it can pack your stall with cold, wet people who suddenly want something hot. It depends on you.",
    "Rain sweeps down the arcade, sudden and hard, drumming on the tin roofs and sheeting off the awnings in ropes. The crowd scatters for cover, and your counter empties in a matter of seconds. Rain can kill a night's trade stone dead. Or, handled right, it can pack your stall with cold, wet, miserable people who suddenly want nothing in the world so much as something hot. It depends entirely on you."),
  [t("Pull the awning. Wait.", "Pull the awning and wait it out.", "Pull the awning and wait it out."),
   t("Call people in for hot bowls.", "Call people in with cheap late bowls.", "Call people in with cheap late bowls.")])

P(80,
  t("You check the pots. The broth is low, the stock nearly finished. You have enough for a while, not for the whole night. Now you must choose how to spend what's left. Small careful bowls, to reach dawn. Or full generous bowls now, and risk running dry with hours still to go and customers still coming.",
    "You check the pots. The broth is low, the stock nearly finished — enough for a while, but not for the whole night. Now you must choose how to spend what's left. Small careful bowls, to eke your way to dawn. Or full generous bowls now, and risk running dry with hours still to go and customers still coming.",
    "You check the pots, and the news isn't good. The broth is low, the stock nearly finished — enough for a while yet, but nowhere near the whole night. Now you must choose how to spend what's left of it. Small, careful bowls, to eke your way to dawn. Or full, generous bowls now, and risk running dry with hours still to go and customers still coming through the rain."),
  [t("The pot's nearly dry.", "The pot's nearly dry.", "The pot's nearly dry."),
   t("Stretch the last broth.", "Stretch the last broth.", "Stretch the last of the broth.")])

P(81,
  t("You pull the awning low and wait. Rain sheets off the edge in a silver line. For a while, almost no one comes. You use the time: wipe down, restock, rest your feet, taste the broth. Rain always passes. When it does, the market comes back out, hungry and cold — and you will be ready and warm.",
    "You pull the awning low and wait it out. Rain sheets off the edge in a long silver line. For a while almost no one comes, so you use the time — wipe down, restock, rest your aching feet, taste the broth. Rain always passes in the end. When it does, the market comes back out, cold and hungry, and you'll be ready and warm.",
    "You pull the awning down low and wait it out. Rain sheets off the edge of it in a long silver line. For a while almost no one comes, so you use the time well — wipe down, restock, rest your aching feet, taste and adjust the broth. Rain always passes in the end. And when it does, the market comes flooding back out, cold and hungry and glad of you, and you'll be ready for them, and warm."),
  [t("The market quietens.", "The market quietens.", "The market quietens."),
   t("Toward closing.", "Toward closing.", "On toward closing.")])

P(82,
  t("You call out into the rain: \"Hot bowls! Get out of the wet!\" A few cold, soaked people duck under your awning, grateful. You sell them smaller, cheaper bowls, quick and warm. It is less money each. But a full stall pulls more people than an empty one. And warmth sells itself on a cold, wet night.",
    "You call out into the rain: \"Hot bowls! Get out of the wet!\" A few cold, soaked people duck under your awning, grateful. You sell them smaller, cheaper bowls, quick and hot. It's less money on each. But a full stall pulls in more people than an empty one, and warmth sells itself on a cold, wet night.",
    "You call out into the downpour: \"Hot bowls! Get out of the wet!\" A few cold, soaked people duck gratefully under your awning. You sell them smaller, cheaper bowls, quick and hot and cheering. It's less money on each. But a full stall pulls in far more people than an empty one, and warmth sells itself on a cold, wet night with no persuading at all."),
  [t("The market quietens.", "The market quietens.", "The market quietens."),
   t("Toward closing.", "Toward closing.", "On toward closing.")])

P(83,
  t("The big pot is nearly empty now. You can see the bottom through the last of the broth. This is the danger point of the night. Run dry too soon, and you stand at a cold stall while the market still moves. You can make the very last of it stretch. Or accept the pot is done and count what you have.",
    "The big pot is nearly empty now — you can see the bottom through the last of the broth. This is the real danger point of the night. Run dry too early, and you'll stand at a cold, closed stall while the market still moves around you. You can make the very last of it stretch, or accept the pot is done and count what you've made.",
    "The big pot is nearly empty now — you can see the bottom through the last inch of broth. This is the real danger point of the whole night. Run dry too early, and you'll stand at a cold, closed stall while the market still moves and spends all around you. You can make the very last of it stretch, or you can accept the pot is done and count up what you've made."),
  [t("Make it stretch.", "Make it stretch.", "Make it stretch."),
   t("The market quietens.", "The market quietens.", "The market quietens.")])

P(84,
  t("You stretch the last of the broth. More water, a careful hand with the spice, small bowls for small prices. It is thinner than Auntie's best, and you know it. But it is still warm, still honest, still hers in shape. Better a smaller true bowl than none at all. You keep the lantern lit and the pot going.",
    "You stretch the last of the broth — a little more water, a careful hand with the spice, small bowls at small prices. It's thinner than Auntie's best, and you know it. But it's still warm, still honest, still hers in shape. Better a smaller true bowl than none at all — so you keep the lantern lit and the pot going a while longer.",
    "You stretch the last of the broth — a little more water, a careful hand with the spice, small bowls at small honest prices. It's thinner than Auntie's best, and you know it perfectly well. But it's still warm, still honest, still hers in shape and spirit. Better a smaller true bowl than none at all — so you keep the lantern lit and the pot quietly going a while longer yet."),
  [t("The market quietens.", "The market quietens.", "The market quietens."),
   t("Toward closing.", "Toward closing.", "On toward closing.")])

P(85,
  t("The night is turning. The crowd thins, the noise softens, the market begins its slow slide toward dawn. Stalls further down are already pulling in. Soon the master will come for the fees. You feel the whole night in your arms and back. But it is nearly done, and you are nearly through it, one way or another.",
    "The night is turning now. The crowd thins, the noise softens, and the market begins its slow slide toward dawn. Stalls further down are already pulling in their shutters. Soon the master will come round for the fees. You feel the whole long night in your arms and your back — but it's nearly done, and you're nearly through it, one way or another.",
    "The night is turning now, unmistakably. The crowd thins, the noise softens, and the market begins its slow slide toward dawn. Stalls further down the row are already pulling in their shutters for the last time this season. Soon enough the master will come round for the fees. You feel the whole long night in your arms and your aching back — but it's nearly done now, and you're nearly through it, one way or the other."),
  [t("Watch the empty stool.", "Watch the empty stool.", "Watch the empty stool."),
   t("Toward closing.", "Toward closing.", "On toward closing."),
   t("Dawn grey on the roofs.", "Dawn grey on the roofs.", "Dawn grey on the roofs.")])

P(86,
  t("A new stall has opened right across from you, selling bowls at half your price. The owner calls loud, waving people over. Some of your queue drifts across to him. Cheap and loud can pull a crowd fast. You can drop your price to match him, and fight. Or hold your price, and trust your food to hold your people.",
    "A new stall has opened right across from you, selling bowls at half your price. The owner calls out loud, waving people over, and some of your queue drifts across to him. Cheap and loud can pull a crowd fast on a night like this. You can drop your price to match him and fight it out — or hold your price, and trust your food to hold your people.",
    "A new stall has opened up right across from you, selling bowls at half your price. The owner calls out loud and constant, waving people over, and some of your own queue begins to drift across to him. Cheap and loud can pull a crowd fast on a night like this. You can drop your price to match him and fight it out toe to toe — or you can hold your price steady, and trust your food to hold your people."),
  [t("Match his price.", "Match their price.", "Match their price."),
   t("Hold your price.", "Hold your price.", "Hold your price.")])

P(87,
  t("You drop your price to match him. Now you are in a price war. Bowls fly out, but each one earns almost nothing. You are busy, and going nowhere. This is a race to the bottom, and the bottom is where stalls close. You cannot win a night like this on price alone. You need another way, and soon.",
    "You drop your price to match him, and now you're in a price war. Bowls fly out of the stall, but each one earns you almost nothing. You're rushed off your feet and going nowhere. It's a race to the bottom, and the bottom is where stalls close for good. You can't win a night like this on price alone — you need another way, and fast.",
    "You drop your price to match him, and just like that you're in a price war. Bowls fly out of the stall, but each one earns you almost nothing at all. You're rushed clean off your feet and going precisely nowhere. It's a race to the bottom, and the bottom, everyone knows, is where stalls quietly close for good. You can't win a night like this on price alone — you're going to need another way, and fast."),
  [t("Hold from here.", "Hold from here.", "Stop, and hold from here."),
   t("They burn out by dawn.", "They burn out by dawn.", "They burn out by dawn.")])

P(89,
  t("You hold your price and let the cheap stall shout. Some people go to him. But your regulars stay. \"His is water,\" one says, nodding at your pot. \"Yours is the real thing.\" Good food is a slower way to win, but a surer one. You are not the cheapest stall tonight. You are the one worth queuing for.",
    "You hold your price and let the cheap stall shout itself hoarse. Some people drift to him, sure. But your regulars stay put. \"His is water,\" one says, nodding at your pot. \"Yours is the real thing.\" Good food is a slower way to win a night, but a surer one. You're not the cheapest stall tonight — you're the one worth queuing for.",
    "You hold your price steady and let the cheap stall across the way shout itself hoarse. Some people drift over to him, of course. But your regulars stay right where they are. \"His is water,\" one says, nodding contemptuously at your pot. \"Yours is the real thing.\" Good food is a slower way to win a night, but a far surer one. You're not the cheapest stall in the market tonight — you're the one worth queuing for."),
  [t("The market quietens.", "The market quietens.", "The market quietens."),
   t("Toward closing.", "Toward closing.", "On toward closing.")])

P(90,
  t("By the small hours, the cheap stall across the way goes dark. He sold everything too cheap, made nothing, and ran out of stock and heart at the same time. The owner packs up, tired and cross. Your lantern is still lit, your pot still warm. Slow and steady and honest outlasts loud and cheap, most nights.",
    "By the small hours, the cheap stall across the way goes dark. He sold everything far too cheap, made almost nothing, and ran out of stock and heart at the same time. The owner packs up, tired and cross. Your lantern is still lit, your pot still warm. Slow and steady and honest outlasts loud and cheap, most nights.",
    "By the small hours, the cheap stall across the way goes dark and quiet. He sold everything far too cheap, made almost nothing on any of it, and ran clean out of stock and heart at the same moment. The owner packs up, tired and cross and no richer. Your lantern is still lit, your pot still warm. Slow and steady and honest outlasts loud and cheap, most nights — and tonight was one of them."),
  [t("The market quietens.", "The market quietens.", "The market quietens."),
   t("Toward closing.", "Toward closing.", "On toward closing.")])


# ============================ ACT III — CLOSING ============================

P(91,
  t("Closing is near. The crowd is thin now, the noise low. On the back shelf, the saved bowl still waits — cold now, but there. Below it, the stool is still empty. Any moment, the market master will come for the fee. But your eyes keep going to that stool, and the bowl above it. And the question you never answered.",
    "Closing is near now. The crowd is thin, the noise low. On the back shelf the saved bowl still waits — cold by now, but still there. Below it, the end stool is still empty. Any moment the master will come round for the fee. But your eyes keep drifting to that stool, and the cold bowl above it, and the question you never got answered.",
    "Closing is near now. The crowd has thinned to a handful, the noise dropped to a murmur. On the back shelf the saved bowl still waits — long cold by now, but still there where you left it. Below it, the end stool stands empty. Any moment now the master will come round for the fee. But your eyes keep drifting back to that stool, and the cold bowl above it, and the question you never quite got answered."),
  [t("Watch the stool.", "Watch the stool.", "Watch the empty stool."),
   t("Sould comes for the fee.", "Sould comes for the fee.", "Sould comes for the fee."),
   t("Remember Auntie's voice.", "You remember Auntie saying his name.", "You remember Auntie saying his name.")])

P(92,
  t("Sould appears at your counter, right on time. \"Well?\" he says softly. \"Made the fee? Or do you need that loan after all?\" If you are short, this is the easy way out. Take his money, pay the master, keep the corner tonight. But you know the price of his help now. You have to answer him.",
    "Sould appears at your counter, right on cue. \"Well?\" he says softly. \"Made the fee yet? Or do you need that little loan after all?\" If you're short, this is the easy way out. Take his money, pay the master, keep the corner tonight. But you know the real price of his help now. You have to answer him.",
    "Sould appears at your counter, right on cue, as if he'd been counting the minutes. \"Well?\" he says softly. \"Made the fee yet? Or do you need that little loan after all?\" If you're short, this is the easy way out — take his money, pay the master, keep the corner for tonight. But you know the real price of his help now, the one he never names. You have to answer him."),
  [t("Take his loan.", "Take his loan.", "Take his loan."),
   t("Refuse. Take your chances.", "Refuse, and take your chances.", "Refuse, and take your chances."),
   t("His smile at closing.", "His smile at closing.", "His smile at closing.")])

P(93,
  t("An old man comes slowly through the thinning crowd. He is thin, grey, tired. He stops at the end stool — the empty one. He rests a hand on it, as if he knows it. He looks at you, then at the back shelf, then away. He does not sit. He does not order. He just stands there, waiting for something.",
    "An old man comes slowly through the thinning crowd. He's thin, grey, tired-looking. He stops at the end stool — the empty one — and rests a hand on it, as if he knows it well. He looks at you, then at the back shelf, then away. He doesn't sit. He doesn't order. He just stands there, waiting for something you can't name.",
    "An old man comes slowly through the thinning crowd. He's thin, grey, tired to the bone. He stops at the end stool — the empty one — and rests a hand on it, lightly, as if he has known it for years. He looks at you, then at the back shelf, then away again. He doesn't sit. He doesn't order. He just stands there, waiting for something you couldn't put a name to."),
  [t("Offer him the saved bowl.", "Offer him the saved bowl.", "Offer him the saved bowl."),
   t("Offer a fresh bowl.", "Offer a fresh bowl.", "Offer him a fresh bowl."),
   t("You have nothing left.", "You have nothing left.", "You have nothing left."),
   t("An old photo by the till.", "An old photo by the till.", "An old photo by the till.")])

P(94,
  t("You take the saved bowl from the shelf and set it before him. \"This one is yours,\" you say. \"It always has been.\" The old man looks at the bowl. Then at you. His eyes fill. \"She kept it,\" he says, very quiet. \"All this time. She kept it.\" You do not fully understand yet. But you know you did something right.",
    "You take the saved bowl down from the shelf and set it before him. \"This one is yours,\" you say. \"It always has been.\" The old man looks at the bowl, then at you, and his eyes fill. \"She kept it,\" he says, very quietly. \"All this time. She kept it.\" You don't fully understand yet — but you know you've done something right.",
    "You take the saved bowl down from the shelf and set it carefully before him. \"This one is yours,\" you say. \"It always has been.\" The old man looks at the bowl for a long moment, then at you, and his tired eyes fill. \"She kept it,\" he says, very quietly. \"All this time. She kept it for me.\" You don't fully understand it yet — but you know, all the way down, that you've done something right."),
  [t("Serve it. He stays.", "Serve it, and he stays.", "Serve it, and he stays."),
   t("Just talk to him.", "Just talk to him.", "Just talk with him.")])

P(95,
  t("You serve the old man, and he sits at last. As he eats, he talks a little. He and Auntie were close, long ago. Then there was a falling-out — small, silly, the kind that hardens over years. He stopped coming. But he never stopped wanting to. \"Tell her,\" he says. \"Tell her Behn came back.\"",
    "You serve the old man, and at last he sits. As he eats, he talks a little. He and Auntie were close once, long ago — then there was a falling-out, small and silly, the kind that hardens over the years. He stopped coming. But he never stopped wanting to. \"Tell her,\" he says. \"Tell her Behn came back.\"",
    "You serve the old man, and at last he sits down on the stool. As he eats, he talks, a little at a time. He and Auntie were close once, long ago — then there was a falling-out, small and silly, the kind that quietly hardens over the years into something neither can cross. He stopped coming. But he never once stopped wanting to. \"Tell her,\" he says at last. \"Tell her Behn came back.\""),
  [t("Toward closing.", "Toward closing.", "On toward closing."),
   t("What his return means.", "What his return means.", "What his return means.")])

P(96,
  t("The end stool has stood empty all night, while every other seat filled and emptied and filled again. One empty stool, one cold bowl above it. It is the quietest thing in a loud market — and somehow the loudest, if you let yourself notice. Auntie kept it for a reason. You wish you knew what it was.",
    "The end stool has stood empty all night, while every other seat filled and emptied and filled again. One empty stool, one cold saved bowl on the shelf above it. It's the quietest thing in a loud market — and somehow, if you let yourself notice, the loudest. Auntie keeps it for a reason. You wish you knew what.",
    "The end stool has stood empty the whole night, while every other seat filled and emptied and filled again a dozen times. One empty stool, one cold saved bowl on the shelf above it. It's the quietest thing in the whole loud market — and somehow, if you let yourself really notice it, the loudest. Auntie keeps it for a reason she wouldn't say. You find you badly want to know what."),
  [t("Watch it a while.", "Watch it a while.", "Watch it a while."),
   t("Back to work.", "Back to work.", "Back to work.")])

P(97,
  t("You think of Auntie's face on the phone, the way it changed at the name Behn. Not anger. Something softer and sadder than that. Whoever he is, he matters to her still, after all these years. The bowl on the shelf is not a habit. It is a door she keeps open, in case. You understand that much now.",
    "You think of Auntie's face on the phone — the way her voice changed at the name Behn. Not anger. Something softer and sadder than anger. Whoever he is, he still matters to her, after all these years. The bowl on the shelf isn't just a habit. It's a door she keeps open, in case. You understand that much now, at least.",
    "You think of Auntie's face on the phone — the way her voice changed, just slightly, at the name Behn. Not anger. Something softer and sadder than anger, and older. Whoever he is, he still matters to her, after all these years and all this silence. The bowl on the shelf isn't just a habit, you see now. It's a door she keeps quietly open, in case. You understand that much, at least."),
  [t("Watch the stool.", "Watch the stool.", "Watch the stool."),
   t("Serve whoever comes.", "Serve whoever comes.", "Serve whoever comes.")])

P(98,
  t("By the till, half-hidden, there is an old photo. You have passed it all night without looking. Now you do. It is Auntie, years younger, laughing. Beside her stands a young man, laughing too. On the back, in her hand, two words: me and Behn. Now the empty stool and the saved bowl make a kind of sense.",
    "By the till, half-hidden, sits an old photo. You've passed it all night without looking. Now you do. It's Auntie, years younger, laughing. Beside her stands a young man, laughing too. On the back, in her writing, two words: me and Behn. Now the empty stool and the cold saved bowl make a kind of sense.",
    "By the till, half-hidden behind the coins, sits an old photograph. You've passed it all night without once looking. Now you do. It's Auntie, years younger, laughing at whoever held the camera. Beside her stands a young man, laughing too, easy and close. On the back, in her writing, two words: me and Behn. And now the empty stool, and the cold saved bowl above it, make a kind of aching sense."),
  [t("Offer the saved bowl.", "Offer the saved bowl.", "Offer him the saved bowl."),
   t("Offer a fresh bowl.", "Offer a fresh bowl.", "Offer him a fresh bowl.")])

P(100,
  t("As Behn eats, you understand what tonight has become. It was never only about the fee. Auntie sent you to keep her stall — but also, without saying so, to keep her door open. And it worked. He came back. Whatever else happens with the money now, this part of the night is already a kind of win.",
    "As Behn eats, you begin to understand what tonight has really become. It was never only about the fee. Auntie sent you to keep her stall running — but also, without ever saying so, to keep her door open. And it worked: he came back. Whatever happens with the money now, this part of the night is already a kind of win.",
    "As Behn eats, slowly, you begin to understand what tonight has really become. It was never only about the fee, not entirely. Auntie sent you to keep her stall running — but also, without ever quite saying so, to keep a door open that she couldn't bring herself to close. And it worked: he came back. Whatever happens with the money now, this part of the night is already, quietly, a kind of win."),
  [t("Toward closing.", "Toward closing.", "On toward closing."),
   t("Talk with him.", "Talk with him a while.", "Talk with him a while.")])

P(101,
  t("Closing time. You pull the money box out and count, coin by coin, with the lantern low. Your heart beats hard. Is it enough? The number climbs. You count again, to be sure. Down the row, you can hear the market master coming. Stall to stall, taking the fees, one door at a time. Your turn is close.",
    "Closing time. You pull the money box out and count it, coin by coin, in the low lantern light. Your heart is beating hard. Is it enough? The number climbs as you count, and you count again to be sure. Down the row you can hear the master coming — stall to stall, taking the fees, one door at a time. Your turn is close.",
    "Closing time at last. You pull the money box out and count it, coin by coin, in the low lantern light, hands not quite steady. Your heart is beating hard. Is it enough? The number climbs as you count, and you count it again to be sure. Down the row you can hear the market master coming — stall to stall, taking the fees, one door at a time. Your turn is very close now."),
  [t("Face the master.", "Face the master's round.", "Face the master's round."),
   t("Watch the stool once more.", "Watch the stool once more.", "Watch the stool once more."),
   t("The master goes stall to stall.", "The master works stall by stall.", "The master works stall by stall.")])

P(102,
  t("The market master moves down the row, slow and steady. He is old, fair, and has seen every trick a stall can try. At each pitch he stops, takes the fee, marks his book, moves on. Some stalls pay easily. Some cannot pay at all. You watch him come, and you hold your money box a little tighter.",
    "The market master moves down the row, slow and steady. He's old, fair, and has seen every trick a stall can try in thirty years. At each pitch he stops, takes the fee, marks his book, and moves on. Some stalls pay easily; some can't pay at all. You watch him come closer, and hold your money box a little tighter.",
    "The market master moves down the row, slow and steady, missing nothing. He's old, and fair, and has seen every trick a stall can try in a long lifetime of them. At each pitch he stops, takes the fee, marks it in his book, and moves on. Some stalls pay easily; others can't pay at all, and he marks that too. You watch him come closer, and hold your money box a little tighter."),
  [t("Your turn comes.", "Your turn comes.", "Your turn comes."),
   t("Others fell short.", "Others who fell short pack up.", "Others who fell short pack up.")])

P(103,
  t("You watch a stall down the row fall short. The master shakes his head, kind but firm. The stallholder starts, slowly, to pack up — plates, pots, a lifetime of nights, boxed away. No shouting. Just a quiet ending. It could be you in an hour. The thought puts steel in you. Not tonight. Not Auntie's corner.",
    "You watch a stall down the row come up short. The master shakes his head, kind but firm. The stallholder begins, slowly, to pack up — plates, pots, a lifetime of nights, all boxed away. No shouting, no scene; just a quiet ending. It could be you in an hour. The thought puts steel in you: not tonight, not Auntie's corner.",
    "You watch a stall further down the row come up short. The master shakes his head, kind but quite firm. The stallholder begins, slowly, to pack it all up — plates, pots, a lifetime of nights, boxed away without a word. No shouting, no scene; just a quiet, final ending. It could be you in an hour, you know. The thought puts steel in you: not tonight, not Auntie's corner, not on your watch."),
  [t("Your turn.", "Your turn.", "Your turn now."),
   t("The lanterns come down.", "The lanterns come down.", "The lanterns come down.")])

P(104,
  t("One by one, down the row, the lanterns come down. The market is putting itself to bed. The bright noisy world of a few hours ago is folding into boxes and shadows. Your two red lanterns still glow, for now. Whether they hang here next season depends on the next few minutes, and the coins in your box.",
    "One by one, down the whole row, the lanterns are coming down. The market is putting itself to bed. The bright, noisy world of a few hours ago is folding away into boxes and shadows. Your own two red lanterns still glow, for now. Whether they hang here next season comes down to the next few minutes — and the coins in your box.",
    "One by one, all down the row, the lanterns are coming down. The market is quietly putting itself to bed. The bright, noisy, steaming world of a few hours ago is folding itself away into boxes and shadows. Your own two red lanterns still glow, for now. Whether they hang over this corner next season comes down to the next few minutes — and the coins counted in your box."),
  [t("Face the master.", "Face the master.", "Face the master."),
   t("The last of the night.", "The last of the night.", "The last of the night.")])

P(105,
  t("Grey light creeps over the market roofs. Dawn. The end of the night, and the end of the season. Somewhere a bird starts up. The air smells of cold ash and old steam. You have been on your feet all night, and you can feel every hour of it. But you are still here, and the stall is still yours — for now.",
    "Grey light creeps over the market roofs: dawn, the end of the night and the end of the season. Somewhere a lone bird starts up. The air smells of cold ash and old steam. You've been on your feet the whole night, and you can feel every single hour of it. But you're still here, and the stall is still yours — for now, at least.",
    "Grey light creeps up over the market roofs: dawn at last, the end of the night and the end of the whole season. Somewhere a lone bird starts up, absurdly cheerful. The air smells of cold ash and old steam and rain. You've been on your feet the entire night, and you can feel every single hour of it in your bones. But you're still here, and the stall is still yours — for now, at least."),
  [t("Watch the stool.", "Watch the stool.", "Watch the stool."),
   t("Toward closing.", "Toward closing.", "On toward closing.")])

P(110,
  t("The master stops at pitch 24. He looks at you, then at the stall, then at Auntie's empty place. \"So it's you tonight,\" he says. \"How did we do?\" This is it — the whole night, come down to one moment and one number. You take a breath and open the money box. Everything you did tonight is in it.",
    "The master stops at pitch 24. He looks at you, then at the stall, then at Auntie's empty place behind the counter. \"So it's you tonight,\" he says. \"How did we do?\" This is it — the whole night come down to a single moment and a single number. You take a breath and open the money box. Everything you did tonight is in there.",
    "The master stops at pitch 24. He looks at you, then at the stall, then at Auntie's empty place behind the counter, and something flickers over his face. \"So it's you tonight,\" he says. \"How did we do?\" This is it — the whole long night come down to a single moment and a single number. You take a breath and open the money box. Everything you did tonight is in there, one way or another."),
  [t("Pay from an honest night.", "Pay from a proud, honest night.", "Pay from a proud, honest night."),
   t("Pay cleanly, no debt.", "Pay it cleanly, no fixer, no debt.", "Pay it cleanly, no fixer, no debt."),
   t("You're not sure you made it.", "You're not sure you've made it.", "You're not sure you've made it.")])

P(111,
  t("You count it out in front of him, coin by coin. The night is all there in the money: the good bowls, the choices, the corners kept or cut. The master watches, patient, saying nothing. You are close to the fee. Close. But close is a word that can go either way at dawn. It all rests on the last count.",
    "You count it out in front of him, coin by coin. The whole night is there in the money — the good bowls, the hard choices, the corners kept or cut. The master watches, patient, saying nothing at all. You're close to the fee. Close. But close is a word that can fall either way at dawn, and it all rests on this last count.",
    "You count it out in front of him, coin by coin, under the last lantern. The whole night is there in the money — the good bowls and the bad, the hard choices, every corner kept or cut. The master watches, patient, saying nothing at all. You're close to the fee. Close. But close is a word that can fall either way at dawn, and it all rests, now, on this last count."),
  [t("Fell short, but made the name.", "You fell short, but you made the name.", "You fell short, but you made the name."),
   t("Made it — by cutting corners.", "You made it — but by cutting corners.", "You made it — but by cutting corners."),
   t("Weigh the rest.", "Weigh the rest.", "Weigh the rest.")])

P(112,
  t("The count stops short. Not by much — but short is short, and the master's book does not round up. The corner is slipping away, coin by missing coin. Unless. There is still one card or two left to play, if you played the night right. You think fast. What do you have that the money alone does not show?",
    "The count stops just short. Not by much — but short is short, and the master's book doesn't round up for anyone. The corner is slipping away, coin by missing coin. Unless — there's still a card or two left to play, if you played the rest of the night right. You think fast: what do you have that the money alone doesn't show?",
    "The count stops just short. Not by much — but short is short, and the master's book doesn't round up for anyone, however hard the night. The corner is slipping away, coin by missing coin. Unless — there's still a card or two left to play, if you played the rest of the night right. You think fast: what do you have, tonight, that the money in the box alone doesn't show?"),
  [t("Sould covered it — for a price.", "Sould has already covered it — for a price.", "Sould has already covered it — for a price."),
   t("The tea woman offers to help.", "The tea woman offers to cover you.", "The tea woman offers to cover you."),
   t("Weigh the last of it.", "Weigh the last of it.", "Weigh the last of it.")])

P(113,
  t("You are down to the last of it now. The money is short, the fixer refused, the tea woman already stretched. What's left is smaller, quieter things — a kindness done earlier, maybe, coming back around. Or nothing. Sometimes a night just does not add up, however hard you worked. You wait to see which kind of night this was.",
    "You're down to the very last of it now. The money's short, the fixer refused, the tea woman already stretched thin. What's left is smaller, quieter things — a kindness done earlier, perhaps, coming back around. Or nothing at all. Sometimes a night just doesn't add up, however hard you worked it. You wait to see which kind of night this turns out to be.",
    "You're down to the very last of it now. The money's short, the fixer refused, the tea woman already stretched too thin to ask. What's left is smaller, quieter things — a kindness done earlier in the night, perhaps, quietly coming back around. Or nothing at all. Sometimes a night just doesn't add up, however hard and honestly you worked it. You wait, heart in your mouth, to see which kind of night this turns out to have been."),
  [t("The kid's family come.", "The kid's family fill your last bowls.", "The kid's family fill your last bowls."),
   t("The master gives you a week.", "The master gives you till next week.", "The master gives you till next week."),
   t("The worst of it.", "The worst of it.", "The worst of it.")])

P(114,
  t("There is nothing left to set against the fee. No money enough, no favour, no kindness coming back. Just you, a cold box of coins, and a number you could not reach. The master waits, not unkind, for your answer. However this ends now, you worked all night for it. That has to count for something, even if not tonight.",
    "There's nothing left to set against the fee. Not enough money, no favour owed, no kindness circling back. Just you, a cold box of coins, and a number you couldn't quite reach. The master waits, not unkindly, for your answer. However this ends now, you worked all night for it — and that has to count for something, even if not tonight.",
    "There's nothing left to set against the fee. Not enough money, no favour owed, no kindness circling back to catch you. Just you, a cold box of coins, and a number you couldn't quite reach however hard you tried. The master waits, not unkindly, for your answer. However this ends now, you worked all night for it, honestly — and that has to count for something, somewhere, even if not tonight."),
  [t("Short. The pitch is lost.", "You're short; the pitch is lost.", "You're short; the pitch is lost."),
   t("The pot ran dry too soon.", "The pot ran dry hours ago.", "The pot ran dry hours ago."),
   t("Think of giving it back.", "You think about handing it back.", "You think about handing it back.")])

# ============================ ENDINGS ======================================

P(120,
  t("You pour the coins onto the counter, and they are enough — more than enough. The master counts, nods, and marks his book. \"Pitch 24, paid. Good night's work.\" You sold honest food to the very last bowl, and the corner is safe. When Auntie hears, she cries a little, and laughs. Thirty years, and one more to come.",
    "You pour the coins onto the counter, and they're enough — more than enough. The master counts, nods, and marks his book. \"Pitch 24, paid. Good night's work.\" You sold honest, good food to the very last bowl, and the corner is safe for another season. When Auntie hears, she cries a little, and then laughs. Thirty years — and one more to come.",
    "You pour the coins out onto the counter, and they're enough — more than enough. The master counts them, nods once, and marks his book. \"Pitch 24, paid. Good night's work.\" You sold honest, good food to the very last bowl in the pot, and the corner is safe for another whole season. When Auntie hears, down the phone, she cries a little, and then laughs. Thirty years — and, thanks to you, one more to come."),
  [])

P(121,
  t("Behn eats the saved bowl slowly, like it is the first warm thing in a long time. When the master comes, the money is short. But Behn stands. He speaks for you, and for Auntie. He pays what's short himself. \"For old friends,\" he says. The corner is safe. And so, it seems, is something long broken. Tell her Behn came back.",
    "Behn eats the saved bowl slowly, as if it's the first warm thing he's had in a long time. When the master comes and the money falls short, Behn stands up. He speaks for you, and for Auntie, and pays what's missing himself. \"For old friends,\" he says. The corner is safe — and so, it seems, is something between them that was broken a long time ago. Tell her Behn came back.",
    "Behn eats the saved bowl slowly, as if it's the first warm thing he's had in a very long time. When the master comes and the money falls a little short, Behn stands up from the stool. He speaks for you, and for Auntie, and quietly pays what's missing himself. \"For old friends,\" he says. The corner is safe — and so, it seems, is something between the two of them that was broken a long, long time ago. Tell her Behn came back, you think. Tell her tonight."),
  [])

P(122,
  t("The coins are enough — just. No loan, no favour, no corner cut. You made the fee with your own two hands, your own honest bowls, your own long night. The master marks his book: \"Pitch 24, paid.\" You lean on the counter, empty and proud. Nobody carried you tonight. You carried the stall yourself.",
    "The coins are enough — just enough. No loan, no favour called in, no corner cut. You made the fee with your own two hands, your own honest bowls, your own long night on your feet. The master marks his book: \"Pitch 24, paid.\" You lean on the counter, wrung out and quietly proud. Nobody carried you tonight — you carried the stall yourself.",
    "The coins are enough — just enough, and no more. No loan, no favour called in, no corner cut anywhere. You made the fee with your own two hands, your own honest bowls, your own long night on your aching feet. The master marks his book: \"Pitch 24, paid.\" You lean on the counter, wrung out and quietly, fiercely proud. Nobody carried you tonight. You carried the stall yourself, all the way to dawn."),
  [])

P(123,
  t("The money is a little short. But as the master counts, the regulars speak up. \"That one cooked us Sim's own bowl all night,\" one says. \"Same as always.\" The master looks at you a long moment. Then he marks his book. \"A name is worth a few coins,\" he says. \"Pitch 24 stays. Don't be short next time.\"",
    "The money's a little short. But as the master counts, your regulars speak up for you. \"That one cooked us Sim's own bowl all night,\" one says. \"Same as always.\" The master looks at you a long moment, then marks his book. \"A good name is worth a few coins,\" he says. \"Pitch 24 stays. Don't be short next time.\"",
    "The money's a little short. But as the master counts, your regulars speak up for you, one after another. \"That one cooked us Sim's own bowl all night long,\" one says. \"Same as always.\" The master looks at you a long, measuring moment, then marks his book. \"A good name is worth a few coins,\" he says. \"Pitch 24 stays. But don't be short next time.\""),
  [])

P(124,
  t("The coins reach the fee. Just. The master counts, nods, marks his book. \"Pitch 24, paid.\" You kept the corner. But you cut corners to do it. Half-cooked bowls, short change, a regular or two who won't come back. The pitch is safe. The name is a little poorer. You saved the corner, and spent some of what made it worth saving.",
    "The coins reach the fee — just. The master counts, nods, and marks his book. \"Pitch 24, paid.\" You kept the corner. But you cut corners to do it: half-cooked bowls, short change, a regular or two who won't be back. The pitch is safe, and the name is a little poorer for the night. You saved the corner, and spent some of what made it worth saving.",
    "The coins reach the fee — just barely. The master counts, nods, and marks his book. \"Pitch 24, paid.\" You kept the corner. But you cut corners to do it: half-cooked bowls, short change slipped across, a regular or two who quietly won't be back. The pitch is safe, and the name is a little poorer for the night's work. You saved the corner, and spent some of the very thing that made it worth saving."),
  [])

P(125,
  t("The count comes up short. Before you can speak, the tea woman is there. She puts her own coins on the counter, enough to close the gap. \"You helped me tonight,\" she says. \"Now I help you.\" The master allows it. The corner is safe — not by your money, but by a kindness returned. You will not forget this, either.",
    "The count comes up short. But before you can even speak, the tea woman is there beside you. She puts her own coins on the counter, just enough to close the gap. \"You helped me tonight,\" she says. \"Now I help you.\" The master allows it. The corner is safe — not by your money, but by a kindness returned. You won't forget this either.",
    "The count comes up short. But before you can even speak, the tea woman is there at your side. She lays her own hard-earned coins on the counter, just enough to close the gap. \"You helped me tonight,\" she says simply. \"Now I help you.\" The master allows it, with the ghost of a smile. The corner is safe — not by your money, in the end, but by a kindness given and returned. You won't forget this, either."),
  [])

P(126,
  t("The money is short, and the corner is lost tonight. But then the kid appears — with their whole ragged crew. Hungry and grinning, coins in their fists for your last bowls. It is not enough to save the pitch. But it is a start of something. You fed one child tonight, and it fed you back. The stall will find a way.",
    "The money's short, and the corner is lost for tonight. But then the kid appears — with a whole ragged crew in tow, hungry and grinning, coins in their fists for your last bowls. It isn't enough to save the pitch, not now. But it's the start of something. You fed one child tonight, and it's feeding you back. The stall will find a way.",
    "The money's short, and the corner is lost for tonight. But then the kid appears out of the dark — with a whole ragged crew in tow, hungry and grinning, coins clutched in their fists for your very last bowls. It isn't enough to save the pitch, not now, not tonight. But it's the start of something real. You fed one hungry child tonight, without asking anything, and now it's quietly feeding you back. The stall will find a way."),
  [])

P(127,
  t("The count falls short, and the master sees it. But he also sees the night you had — alone, new, and still standing at dawn. \"Auntie's kept this corner clean for thirty years,\" he says. \"You've earned one more market day. Bring the rest then.\" It is not a win. But it is not a loss. It is another chance, and you will take it.",
    "The count falls short, and the master sees it plainly. But he also sees the night you've had — alone, new, and still on your feet at dawn. \"Sim's kept this corner honest for thirty years,\" he says. \"You've earned one more market day. Bring the rest then.\" It isn't a win. But it isn't a loss either. It's another chance, and you'll take it.",
    "The count falls short, and the master sees it plainly enough. But he also sees the night you've had — alone, brand new to it, and still on your feet at dawn. \"Sim's kept this corner honest for thirty years,\" he says, after a moment. \"You've earned one more market day. Bring the rest of it then.\" It isn't a win. But it isn't a loss, either. It's another chance, freely given, and you'll take it with both hands."),
  [])

P(128,
  t("The master takes his fee, and the corner is safe — on paper. But the money that paid it was Sould's, and Sould's money is never really yours. Tomorrow he will smile and call you 'friend' and start to name his price. You kept the pitch tonight. But the ground under it belongs to him now, and he does not forget.",
    "The master takes his fee, and the corner is safe — on paper. But the money that paid it was Sould's, and Sould's money is never really yours. Tomorrow he'll smile, and call you 'friend', and begin, slowly, to name his price. You kept the pitch tonight. But the ground beneath it belongs to him now, and Sould never forgets a debt.",
    "The master takes his fee, and the corner is safe — on paper, at least. But the money that paid it was Sould's, and Sould's money is never, ever really yours. Tomorrow he'll smile, and call you 'friend', and begin, slowly and pleasantly, to name his price. You kept the pitch tonight. But the ground beneath it belongs to him now, and Sould, as everyone warned you, never forgets a debt."),
  [])

P(129,
  t("The coins fall short of the fee. The master counts twice, to be fair, but the number does not change. \"I'm sorry,\" he says, and he means it. \"Pitch 24 goes to the morning list.\" Thirty years, ended on your one night. You did not do anything wrong, exactly. The night was just longer than the money. It happens. It still hurts.",
    "The coins fall short of the fee. The master counts them twice, to be fair, but the number doesn't change. \"I'm sorry,\" he says, and he means it. \"Pitch 24 goes on the morning list.\" Thirty years, ended on your one night in charge. You didn't do anything wrong, exactly — the night was just longer than the money. It happens. It still hurts like anything.",
    "The coins fall short of the fee. The master counts them twice over, to be fair to you, but the number doesn't change. \"I'm sorry,\" he says, and he plainly means it. \"Pitch 24 goes on the morning list.\" Thirty years, ended on your one night in charge of it. You didn't do anything wrong, exactly — the night was simply longer than the money would stretch. It happens, to better cooks than you. It still hurts like anything."),
  [])

P(130,
  t("You ran out too soon. Hours before dawn, the pot was empty, the stock gone, the counter cold. You stood there while the market moved on around you, unable to sell a thing. By the time the master comes, the box is far short. You didn't lose the night to bad luck. You lost it to bad planning. Next time, you will know better.",
    "You ran out far too soon. Hours before dawn the pot was empty, the stock gone, the counter cold. You stood there while the market moved on around you, unable to sell a single thing. By the time the master comes, the box is well short. You didn't lose the night to bad luck — you lost it to bad planning. Next time, if there is one, you'll know better.",
    "You ran out far too soon. Hours before dawn the pot stood empty, the stock gone, the counter going cold. You stood there while the whole market moved on and spent around you, unable to sell a single thing. By the time the master comes, the box is well short. You didn't lose the night to bad luck — you lost it to bad planning, plain and simple. Next time, if there is a next time, you'll know better."),
  [])

P(131,
  t("The fee is out of reach, and something in you gives way. You are so tired. The night beat you — the crowd, the fixer, the fear, the endless bowls. As the master marks his book, you think of giving the stall up. Just for a moment. For good. Of telling Auntie you couldn't. You don't say it out loud. But tonight, you think it.",
    "The fee is out of reach, and something in you quietly gives way. You're so tired. The night beat you — the crowd, the fixer, the fear, the endless bowls. As the master marks his book, you think, just for a moment, about giving the stall up for good. About telling Auntie you couldn't do it. You don't say it out loud. But tonight, for the first time, you think it.",
    "The fee is out of reach, and something in you quietly gives way. You're so tired you can barely stand. The night beat you — the crowd, the fixer, the fear, the endless, endless bowls. As the master marks his book, you think, just for a moment, about giving the stall up for good. About telling Auntie, gently, that you couldn't do it. You don't say it out loud, of course. But tonight, for the first time, you let yourself think it."),
  [])


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
