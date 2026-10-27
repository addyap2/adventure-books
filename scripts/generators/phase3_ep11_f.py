#!/usr/bin/env python3
"""Phase 3 prose for Moving Day (episode-11), batch F: Act III finale (90-114)
and the 12 endings (120-131). Run: python3 scripts/generators/phase3_ep11_f.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-11.json")

D = {
 90: {"t": {
  "A2": "You're at the new flat at last, arms dead, the last load at the kerb. The dark is almost here. Inside, the rooms are bare and cold, waiting to be filled. Mum sits in the van, wrapped up, trusting you. This is the moment it all rests on. Everything now comes down to what you do next.",
  "B1": "You're at the new flat at last, arms dead, the last load at the kerb, the dark almost here. Inside, the rooms are bare and cold, waiting to be filled. Mum sits in the van, wrapped up, trusting you. This is the moment it all rests on. Everything now comes down to what you do in the last of the light.",
  "B2": "You're at the new flat at last, your arms dead, the last load at the kerb, and the dark almost here. Inside, the rooms are bare and cold, waiting to be filled. Mum sits in the van, wrapped up warm, trusting you to get it right. This is the moment the whole day rests on. Everything now comes down to what you do in the last of the light."},
  "c": ["Get the door open.", "Bray, one more time.", "Cass takes an end."]},
 91: {"t": {
  "A2": "You get to the new door and work the stiff key: it catches, then turns. Out at the kerb, the light is nearly gone. You have to get the last of it in, and the rooms warm. And you have to choose what matters most, right now.",
  "B1": "You get to the new door and work the stiff key: it catches, then turns. Out at the kerb, the light is nearly gone. You have to get the last of it in, and the rooms warm again. And you have to choose what matters most, right now.",
  "B2": "You get to the new door and work the stiff key in the lock: it catches, then finally turns. Out at the kerb, the light is nearly gone. You have to get the last of it in, and the bare rooms warm. And you have to choose what matters most of all, right now, with no light to spare."},
  "c": ["Start carrying in.", "See to Mum first.", "That figure again."]},
 92: {"t": {
  "A2": "Then help takes the weight at last. Cass at one end, a neighbour at the other — hands you didn't have an hour ago. You're not carrying it alone now. Others are here to share the load. It's like setting down something heavy you'd carried too far, too long.",
  "B1": "Then help takes the weight at last — Cass at one end, a neighbour at the other, hands you didn't have an hour ago. You're not carrying it alone now. Others are here to share the load. It's like setting down something heavy you'd carried too far, for too long.",
  "B2": "Then help takes the weight at last — Cass at one end, a neighbour at the other, hands you didn't have an hour ago. You're not carrying it alone any more. Others are here now to share the load with you. It's like finally setting down something heavy that you'd carried too far, and for far too long."},
  "c": ["Set to carrying.", "The last long haul.", "Watch the gate."]},
 93: {"t": {
  "A2": "Now you get the place filled. What you can do depends on how the day went. With a full van and hands to help, you've plenty to work with. Alone and half-loaded, you make every trip count. Either way, the work is the same: keep going, keep carrying.",
  "B1": "Now you get the place filled. What you can do depends on how the day has gone. With a full van and hands to help, you've plenty to work with. Alone and half-loaded, you have to make every trip count. Either way, the work is the same: keep going, keep carrying.",
  "B2": "Now you get the place filled, come what may. What you can do depends on how the day has gone for you. With a full van and hands to help, you've plenty to work with. Alone and half-loaded, you have to make every single trip count. Either way, the work in front of you is the same: keep going, and keep carrying."},
  "c": ["A full van, hands to help.", "Alone, and half-loaded."]},
 94: {"t": {
  "A2": "You go to the van and see to Mum. Her eyes are tired and a little afraid. Then, seeing your face, a bit less afraid. 'Nearly home,' she whispers. 'Nearly, Mum,' you tell her softly. 'You stay warm. Leave the rest to me.'",
  "B1": "You go to the van and see to Mum. Her eyes are tired and a little afraid. Then, seeing your face, a little less afraid. 'Nearly home,' she whispers. 'Nearly, Mum,' you tell her softly. 'You stay warm. Leave the rest to me.'",
  "B2": "You go out to the van and see to Mum. Her tired eyes are a little afraid, there in the dark. Then, seeing your face at the window, a little less afraid. 'Nearly home,' she whispers. 'Nearly, Mum,' you tell her softly. 'You stay warm, and leave the rest of it to me.'"},
  "c": ["Back to carrying.", "Get her chair in first."]},
 95: {"t": {
  "A2": "The full van does it. You carry in the bed, the chair, the boxes, and the bare rooms start to fill. A lamp goes on. The place warms and softens against the dark window. This, you think, is what a home is made of.",
  "B1": "The full van does it. You carry in the bed, the chair, the boxes, and the bare rooms start to fill. A lamp goes on. The place warms and softens against the dark window. This, you think to yourself, is what a home is made of.",
  "B2": "The full van does the trick. You carry in the bed, the big chair, the boxes, and the bare rooms slowly start to fill. A lamp goes on in the corner. The whole place warms and softens against the dark window. This, you think to yourself, is exactly what a home is made of."},
  "c": ["The last long haul.", "More hands arrive."]},
 96: {"t": {
  "A2": "You've not much left in the van, so you make every trip count. The bed, the chair, one box of Mum's things, and a lot of care. You carry the important things first. It's bare, and plain. It may be enough for tonight — or it may not.",
  "B1": "You've not much left in the van, so you make every trip count. The bed, the chair, one box of Mum's things, and a lot of care. You carry the important things first. It's bare, and plain. It may just be enough for tonight — or it may not.",
  "B2": "You've not much left in the van at all, so you make every trip count. The bed, the chair, one box of Mum's own things, and a great deal of care. You carry the important things in first. It's bare, and plain. It may just about be enough for tonight — or, then again, it may not."},
  "c": ["The last long haul.", "You need more."]},
 97: {"t": {
  "A2": "What's in is thin, and you're afraid it won't do for tonight. You've carried all you can on your own. But the rooms still feel empty and cold. You need more now — more hands, more trips, or both.",
  "B1": "What's in is thin, and you're afraid it won't do for tonight. You've carried all you can on your own. But the rooms still feel empty and cold. You need more now — more hands, more trips, or both.",
  "B2": "What's in is thin, and you're honestly afraid it won't do for tonight. You've carried all you possibly can on your own. But the rooms still feel empty and cold around you. You need more now — more hands, more trips, or, if it's to be a home tonight, probably both."},
  "c": ["The last haul anyway.", "Knock round for help."]},
 98: {"t": {
  "A2": "You glance back at the gate and see it. There, by the wall, that figure again — still, half-turned, waiting. It's where no one you'd expect would be. It pulls at your eye. And it pulls at something deeper than that.",
  "B1": "You glance back at the gate and see it. There, by the wall, that figure again — still, half-turned, waiting. It's where no one you'd expect to see would be. It pulls at your eye. And it pulls at something deeper than that.",
  "B2": "You glance back at the gate and you see it. There, by the wall, that figure again — quite still, half-turned, waiting in the dusk. It's standing where no one you'd ever expect to see would be. It pulls at your eye, that figure. And it pulls, if you're honest, at something a good deal deeper than that."},
  "c": ["Keep carrying.", "Go to the figure."]},
 99: {"t": {
  "A2": "The figure at the gate stands again. It stands where you'd swear no one you knew would be. But a face you half know means a story. A story means a choice. A person right there, from your past, on today of all days.",
  "B1": "The figure at the gate stands there again. It stands where you'd swear no one you knew would be. But a face you half know means a story. A story means a choice. A person right there, from your past, on today of all days.",
  "B2": "The figure at the gate shows itself again. It stands where you'd swear blind that no one you knew would be. But a face you half know means a story behind it. And a story means a choice to make. A person standing right there, out of your past, on today of all days — and you can't un-see it now."},
  "c": ["See to Mum first.", "The last long haul."]},
 100: {"t": {
  "A2": "Now comes the last long haul. You carry, you climb, you set things down, and watch the light drop over the roofs. It's not easy — just steady, heavy, tiring work. But it's the whole job now. And it's yours to do.",
  "B1": "Now comes the last long haul. You carry, you climb, you set things down, and watch the light drop over the roofs. It's not easy — just steady, heavy, tiring work. But it's the whole job now. And it's yours to do.",
  "B2": "Now comes the last long haul of it. You carry, you climb the stairs, you set things down, and watch the light drop slowly over the roofs. It isn't easy work — just steady, heavy, tiring work that nobody sees. But it's the whole job now, start to finish. And it's yours, and no one else's."},
  "c": ["Nearly there.", "That figure again.", "The hardest stretch."]},
 101: {"t": {
  "A2": "And then, at last, it turns. The van is nearly empty. The bed is up, the chair's by the window, the kettle's found. It's almost dark now. You've nearly got the whole move done.",
  "B1": "And then, at last, it turns. The van is nearly empty. The bed is up, the chair's by the window, the kettle's found. It's almost dark now. You've nearly got the whole move done. Soon it'll just be the two of you and a cup of tea.",
  "B2": "And then, at long last, it turns. The van is nearly empty. The bed is up, the chair's by the window, the kettle's been found and filled. It's almost dark now, almost done. You've very nearly got the whole move done. Soon it'll just be the two of you and a cup of tea in the warm."},
  "c": ["See it all added up.", "Mum comes in."]},
 102: {"t": {
  "A2": "This is the hardest stretch, the last one before it's done. The heaviest things are left, and you're spent. Your back aches, your hands are raw. But you can feel it all coming together, somewhere under the tiredness. Hold on a little longer.",
  "B1": "This is the hardest stretch, the last one before it's all done. The heaviest things are left, and you're spent. Your back aches, and your hands are raw. But you can feel it all coming together, somewhere under the tiredness. Hold on a little longer now.",
  "B2": "This is the hardest stretch of the whole day, the last one before it's done. The heaviest things are left, and you're utterly spent. Your back aches, and your hands are raw from the boxes. But you can feel it all starting to come together, somewhere under the tiredness. Just hold on a little longer now."},
  "c": ["Nearly there.", "You're not alone in this."]},
 103: {"t": {
  "A2": "You look down the street from the new door. Warm windows glow all along the row. Other homes, other families, other lives behind the glass. This is your row now, and your light's going on too. You were never quite as alone as you felt.",
  "B1": "You look down the street from the new door. Warm windows glow all along the row. Other homes, other families, other lives behind the glass. This is your row now, and your own light's going on too. You were never quite as alone as you'd felt.",
  "B2": "You look down the street from the new door. Warm windows glow all along the row, one after another. Other homes, other families, other lives behind the lit glass. This is your row now, and your own light's going on too. You were never, it turns out, quite as alone as you'd felt."},
  "c": ["See it all added up.", "Mum at the door."]},
 104: {"t": {
  "A2": "At last, the last of it comes in. Cass and a neighbour carry Mum's chair between them, and you bring her in on your arm. You stand in the new hall, your legs shaking under you now. But the worst of the day is behind you.",
  "B1": "At last, the last of it comes in. Cass and a neighbour carry Mum's chair between them, and you bring her in on your arm. You stand in the new hall, your legs shaking under you now. But the worst of the day is behind you.",
  "B2": "At last, the very last of it comes in. Cass and a neighbour carry Mum's chair between them, and you bring her in slowly on your arm. You stand together in the new hall, your legs shaking under you now that you've stopped. But the worst of the whole day is well and truly behind you."},
  "c": ["See it all added up.", "Too much came at once."]},
 105: {"t": {
  "A2": "The light goes, and you get Mum in before the dark. You settle her in her chair by the window, a blanket over her knees. The rooms are filling, the lamp is warm, the place is hers. The worst has passed at last. You got her home in time.",
  "B1": "The light goes, and you get Mum in just before the dark. You settle her in her chair by the window, a blanket over her knees. The rooms are filling, the lamp is warm, the place is hers now. The worst has passed at last. You got her home in time.",
  "B2": "The light goes, and you get Mum in just before the dark closes in. You settle her into her chair by the window, a blanket over her knees. The rooms are filling, the lamp is warm, and the place is hers now. The worst has passed at last, and you can feel it go. You got her home, somehow, in time."},
  "c": ["See it all added up.", "A last hand with the rest.", "A small, good moment."]},
 106: {"t": {
  "A2": "Then it comes — Mum laughs at something, the first laugh all day. It fills the bare room as if there'd been no rush at all. After the day you've had, it seems almost absurd. And it's lovely, and you stop to listen.",
  "B1": "Then it comes — Mum laughs at something, the first real laugh all day. It fills the bare room as if there'd been no rush at all. After the day you've had, it seems almost absurd. And it's lovely, and you stop just to listen.",
  "B2": "Then it comes — Mum laughs at something, the first real laugh of the whole day. It fills the bare new room as if there'd never been any rush at all. After the day you've just had, it seems almost absurd that such a sound could exist. And it's lovely, utterly lovely, and you stop whatever you're doing just to listen."},
  "c": ["See it all added up.", "Back to the last of it."]},
 107: {"t": {
  "A2": "From the new door you watch the gate. People come and go in the dusk, carrying, leaving, too far to make out. Someone is coming up the path. But a shape at the gate means someone's here. And someone, today, is better than doing it all alone.",
  "B1": "From the new door you watch the gate. People come and go in the dusk, carrying, leaving, too far off to make out. Someone is coming up the path. But a shape at the gate means someone's here. And someone, today, is better than doing it all alone.",
  "B2": "From the new door you watch the gate below. People come and go in the dusk, carrying, leaving, still too far off to make out properly. Someone is coming up the path. But a shape at the gate means someone's here. And someone, on a day like this one, is far better than doing it all alone."},
  "c": ["Keep carrying.", "The last long haul."]},
 110: {"t": {
  "A2": "The light's gone, and the day adds up to what it is. Whatever you did out there comes home with you now. Some of it to be proud of, some not. Let's see, then, what it all came to.",
  "B1": "The light's gone, and the day adds up to what it is. Whatever you did out there comes home with you now. Some of it to be proud of, some of it not. Let's see, then, what it all came to.",
  "B2": "The light's gone, and the day adds up to just exactly what it is. Whatever you did out there, on the stairs and at the kerb, comes home with you now, all of it. Some of it to be proud of, and some of it not so much. Let's see, then, what the whole long day finally came to."},
  "c": ["You got her home.", "You let your sister back in.", "What else it came to."]},
 111: {"t": {
  "A2": "The day adds up — not with one big lift, but with many small ones. What you carried, what you refused, who you stopped for on the way. It all counts in the end. It all made the day what it was.",
  "B1": "The day adds up — not with one big lift, but with many small ones. What you carried, what you refused, and who you stopped for on the way. It all counts in the end. It all made the day what it was.",
  "B2": "The day adds up — not, in the end, with one big lift, but with a great many small ones. What you carried, what you refused to do, and who you stopped for along the way. It all counts in the end, every bit of it. It all made the day into exactly what it was."},
  "c": ["The whole block came out.", "You did it honestly.", "What else it came to."]},
 112: {"t": {
  "A2": "There's more to weigh; the day held other things too. A neighbour you stopped for on the stairs. Your own van and hands, given to someone with less. Small choices, made when you were tired, when it would have been easier not to.",
  "B1": "There's more to weigh; the day held other things too. A neighbour you stopped for on the stairs. Your own van and hands, given to someone with less. Small choices, made when you were tired, when it would have been far easier not to.",
  "B2": "There's more still to weigh up; the day held other things too, quieter ones. A neighbour you stopped for on the stairs. Your own van and hands, given freely to someone with less. Small choices, all of them, made when you were dead tired, when it would have been so much easier simply not to bother."},
  "c": ["A kindness came back.", "You travelled lighter.", "What it leaves you with."]},
 113: {"t": {
  "A2": "And what does the day leave you with? Maybe not a perfect move. Maybe just the fact that you tried, that you kept carrying. When your back ached and the light went and it was easy to stop, you didn't. That counts for something.",
  "B1": "And what does the day leave you with? Maybe not a perfect move. Maybe just the fact that you tried, and that you kept carrying. When your back ached and the light went and it was easy to stop, you didn't. That counts for something.",
  "B2": "And what, in the end, does the day leave you with? Maybe not a perfect move, no. Maybe just the plain fact that you tried, and that you kept carrying when you could have stopped. When your back ached and the light went and it was so easy to give the whole thing up, you simply didn't. And that, whatever else, counts for something."},
  "c": ["A bit late, but home.", "They'll remember you tried.", "The hard end of it."]},
 114: {"t": {
  "A2": "But not every day ends well. Some choices cost more than you knew at the time. Some things, once dropped, can't be mended. This is the hard end of the day, where the worst of it comes home.",
  "B1": "But not every day ends well. Some choices cost more than you knew at the time. Some things, once dropped, simply can't be mended. This is the hard end of the day, where the worst of it comes home.",
  "B2": "But not every day ends well, and this is the truth of it. Some choices cost a great deal more than you knew at the time you made them. Some things, once dropped, simply can't be mended again. This is the hard end of the day, where the worst of it all comes home to roost."},
  "c": ["Bray took you for a ride.", "Too late, too dark.", "A bit late, but home."]},

 # ---- ENDINGS ----
 120: {"t": {
  "A2": "You got her home by dark. By nightfall the rooms are full. The bed made, the chair by the window, a lamp warm in the hall. Mum sits in it all, home, her hand finding yours. It all came good because you kept carrying and wouldn't give up. That is the whole of it.",
  "B1": "You got her home by dark. By nightfall the rooms are full — the bed made, the chair by the window, a lamp warm in the hall. Mum sits in it all, home at last, her hand finding yours. It all came good because you kept carrying and wouldn't give up. That is the whole of it.",
  "B2": "You got her home by dark. By nightfall the rooms are full — the bed made, the chair by the window, a lamp warm in the hall. Mum sits in the middle of it all, home at last, her hand finding yours in the quiet. It all came good, every bit of it, because you kept carrying when you were spent and would not let yourself give up. That, in the end, is the whole of it."}},
 121: {"t": {
  "A2": "You let your sister back in. You faced Cass at the gate. You said the thing you'd left unsaid for years, and let the old rift heal. And more than one thing was mended today. In the new front room, Mum looks up and sees her two children carrying her home together. A door everyone thought shut swings open.",
  "B1": "You let your sister back in. You faced Cass at the gate, said the thing you'd left unsaid for years, and let the old rift heal. And more than one thing was mended today. In the new front room, Mum looks up and sees her two children carrying her home together. A door everyone thought shut for good swings open.",
  "B2": "You let your sister back in. You faced Cass at the gate, said the thing you'd left unsaid for years, and let the old rift finally heal. And more than one thing was mended today, as it turns out. In the new front room, Mum looks up and sees her two children carrying her home together, side by side. A door everyone had thought shut for good swings quietly open, and the day becomes something far bigger than a move."}},
 122: {"t": {
  "A2": "There was no quick fix — there was something far better. You turned a street of strangers into a chain of hands on the stairs. One carried, one packed, one kept Mum company at the window. Together you got it all in before dark. No one did it alone today, and the block won't forget who started it.",
  "B1": "There was no quick fix — there was something far better. You turned a street of strangers into a chain of hands on the stairs. One carried, one packed the van, one kept Mum company at the window. Together you got it all in before dark. No one did it alone today, and the block won't forget who started it.",
  "B2": "There was no quick fix that saved the day — there was something far better than that. You turned a street of strangers into a chain of willing hands on the stairs. One carried, one packed the van tight, one kept Mum company at the window. Together, all of you, you got it all in before dark. No one did it alone today, not one of them, and the block won't soon forget who started it."}},
 123: {"t": {
  "A2": "You saw off the con. You read Bray for what he was and turned him down. You did it yourself, by honest sweat and a bit of help. It wasn't a perfect move. You dropped the odd thing and left it late. But every box went in by your own hands, and that's worth more than any shortcut.",
  "B1": "You saw off the con. You read Bray for what he was and turned him down flat. You did it yourself, by honest sweat and a bit of help. It wasn't a perfect move. You dropped the odd thing and left it late. But every box went in by your own hands, and that's worth more than any shortcut.",
  "B2": "You saw off the con outright. You read Bray for exactly what he was and turned him down flat. You did it yourself, by honest sweat and a bit of good help. It wasn't a perfect move, mind. You dropped the odd thing and ran it late. But every last box went in by your own hands, and that is worth a great deal more than any shortcut he was ever selling."}},
 124: {"t": {
  "A2": "You fell short of doing it all on your own. But the neighbour you helped on the stairs turns up at your gate. He's got two strong mates and a spare hour. They carry the last of it in. It's not quite the perfect day. But a kindness, it turns out, has a way of coming back round.",
  "B1": "You fell short of doing it all on your own. But the neighbour you helped on the stairs turns up at your gate — with two strong mates and a spare hour. They carry the last of it in for you. It's not quite the perfect day. But a kindness, it turns out, has a way of coming back round.",
  "B2": "You fell short of doing it all on your own, in the end. But the neighbour you helped on the stairs turns up at your gate — with two strong mates and a spare hour to give. They carry the last of it in for you. It's not quite the perfect day you'd pictured. But a kindness, it turns out, has a quiet way of coming back round to you when you least expect it."}},
 125: {"t": {
  "A2": "You gave what you couldn't take to those with less. The spare chairs, the old table, a hand with their load. So you move in lighter than you planned, bare rooms and room to breathe. You didn't get everything in. But no one you met today was left stuck. And somehow, shared out, there was enough.",
  "B1": "You gave what you couldn't take to those with less — the spare chairs, the old table, a hand with their load. So you move in lighter than you'd planned, with bare rooms and room to breathe. You didn't get everything in. But no one you met today was left stuck. And somehow, shared out, there was enough.",
  "B2": "You gave what you couldn't take to those with less — the spare chairs, the old table, a hand with their load. So you move in lighter than you'd ever planned, with bare rooms and room to breathe. You didn't get everything in. But no one you met today was left stuck with their own. And somehow, shared out between you all, there turned out to be just enough."}},
 126: {"t": {
  "A2": "You scrape through the worst of it. The move runs late, and it's dark by the time the last box is in. But it gets done. It's no triumph, and no one will tell stories about it. But Mum's in her chair, warm and home, and you're both still standing. You got through the day, and that'll do.",
  "B1": "You scrape through the worst of it. The move runs late, and it's dark by the time the last box is in, but it gets done. It's no triumph, and no one will tell stories about it. But Mum's in her chair, warm and home, and you're both still standing. You got through the day, and that will do.",
  "B2": "You scrape through the worst of it, somehow. The move runs late, and it's fully dark by the time the last box is in, but it gets done, which is what counts. It's no triumph, and no one will be telling stories about it. But Mum's in her chair, warm and home, and the two of you are still standing. You got through the day in one piece, and today, that will do nicely."}},
 127: {"t": {
  "A2": "You didn't get it all done today. But Mum, and the neighbours, and Cass saw you try. They saw you carry till your arms gave out, and keep going when you could have stopped. They won't forget it. The rest can wait for morning. From today, you're the one who carried her home. And that stays.",
  "B1": "You didn't get it all done today. But Mum, and the neighbours, and Cass saw you try. They saw you carry till your arms gave out, and keep going when you could have stopped. They won't forget it. The rest can wait for morning. From today on, you're the one who carried her home. And that stays.",
  "B2": "You didn't get it all done today, not quite. But Mum, and the neighbours, and Cass saw you try — saw you carry till your arms gave out, and keep going when you could so easily have stopped. They won't forget it in a hurry. The rest can wait for morning. From today on, you're the one who carried her home. And that, whatever else, stays with people."}},
 128: {"t": {
  "A2": "You took Bray's deal, and by dark it all comes out. Half your boxes are crushed and Mum's lamp is broken. He wants more before he'll hand back the rest. The money's gone, the trust is gone, and the new flat is a mess of damage. You won't forget the look on Mum's face in a hurry.",
  "B1": "You took Bray's deal, and by dark it all comes out. Half your boxes are crushed, Mum's lamp is broken, and he wants more money before he'll hand back the rest. The money's gone, the trust is gone, and the new flat is a mess of damage. You won't forget the look on Mum's face in a hurry.",
  "B2": "You took Bray's deal, and by dark it all comes out in the end. Half your boxes are crushed, Mum's lamp is broken, and he wants more money before he'll hand back the rest. The money's gone, the trust is gone, and the new flat is a mess of damage and regret. You won't forget the look on Mum's face today in a hurry — nor, you suspect, will she."}},
 129: {"t": {
  "A2": "The overloaded pile was a trap, just as Tom warned. It went over on the stairs, and you went with it. You come round sore and shaken, Mum's box of your dad's things smashed across the steps. You limp through the rest, hours behind, in the dark. You should have made two trips, and you know it now.",
  "B1": "The overloaded pile was a trap, just as Tom warned you. It went over on the stairs, and you went with it. You come round sore and shaken, Mum's box of your dad's things smashed across the steps. You limp through the rest, hours behind, in the dark. You should have made two trips, and you know it now.",
  "B2": "The overloaded pile was a trap, just exactly as Tom had warned you it would be. It went over on the stairs, and you went down with it. You come round sore and shaken, Mum's box of your late dad's things smashed across the steps. You limp through the rest of it, hours behind now, in the dark. You should have made two trips, like he said, and you know it now, too late."}},
 130: {"t": {
  "A2": "You spent the day on the wrong things, and the move paid for it. Dark falls with half of it still at the old place and the new rooms cold and bare. Mum waits in the van, worn out. You did try, in your own way. But trying, today, was not quite enough.",
  "B1": "You spent the day on the wrong things, and the move paid for it. Dark falls with half of it still at the old place and the new rooms cold and bare. Mum waits in the van, worn right out. You did try, in your own way. But trying, today, was not quite enough.",
  "B2": "You spent the day on the wrong things, one after another, and the move paid the price for it. Dark falls with half of it still at the old place and the new rooms cold and bare. Mum waits in the van, worn right out and quiet. You did try, in your own way, you really did. But trying, today of all days, was not quite enough to get her home."}},
 131: {"t": {
  "A2": "In the end, you walked away. You left the last of it and drove Mum to yours for the night. You told yourself the day was too much for one person. You said no one could blame you. You said you'd finish tomorrow. And maybe you will. But the new flat stayed dark and empty, and you never found out what today might have been.",
  "B1": "In the end, you walked away. You left the last of it, drove Mum to yours for the night, and told yourself the day was too much for one person. You said no one could blame you. You said you'd finish tomorrow. And maybe you will. But the new flat stayed dark and empty, and you never found out what today might have been.",
  "B2": "In the end, you simply walked away. You left the last of it, drove Mum to yours for the night, and told yourself the day was far too much for one person to manage alone. You said no one could possibly blame you. You said, over and over, that you'd finish it tomorrow. And maybe, in time, you will. But the new flat stayed dark and empty, and you never did find out what today might have been, if only you'd kept carrying."}},
}


def main():
    d = json.load(open(P, encoding="utf-8"))
    by = {n["id"]: n for n in d["nodes"]}
    for nid, spec in D.items():
        n = by[nid]; n["text"] = spec["t"]
        cs = spec.get("c")
        if cs:
            for j, c in enumerate(n.get("choices") or []):
                if j < len(cs):
                    t = cs[j]; c["text"] = {"A2": t, "B1": t, "B2": t}
    json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"batch F: wrote prose for {len(D)} nodes")


if __name__ == "__main__":
    main()
