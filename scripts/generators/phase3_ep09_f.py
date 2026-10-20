#!/usr/bin/env python3
"""Phase 3 prose for The Dinner (episode-09), batch F: Act III finale (90-114)
and the 12 endings (120-131). Run: python3 scripts/generators/phase3_ep09_f.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-09.json")

D = {
 90: {"t": {
  "A2": "You're home at last, soaked and worn out, with seven almost here. Upstairs, Gran Ivy lies pale and weak in her bed. The kitchen is cold, the oven off, the table bare. This is the moment it all rests on. Everything now comes down to what you do next.",
  "B1": "You're home at last, soaked and worn out, with seven almost here. Upstairs, Gran Ivy lies pale and weak in her bed. The kitchen is cold, the oven off, the table bare. This is the moment it all rests on. Everything now comes down to what you do in the next hour.",
  "B2": "You're home at last, soaked to the skin and worn right out, with seven o'clock almost upon you. Upstairs, Gran Ivy lies pale and weak in her bed, waiting. The kitchen is cold, the oven off, the long table bare. This is the moment the whole evening rests on. Everything now comes down to what you do in the next short hour."},
  "c": ["Get the oven on.", "Dale, at the door again.", "Help arrives."]},
 91: {"t": {
  "A2": "You get to the kitchen: the oven cold, nothing on, the clock ticking hard. Out in the rain, the night is still taking people. You have to get the dinner on and the kitchen warm again. And you have to choose what matters most, right now.",
  "B1": "You get to the kitchen: the oven cold, nothing on, the clock ticking hard on the wall. Out in the rain, the night is still taking its toll. You have to get the dinner on and the kitchen warm again. And you have to choose what matters most, right now.",
  "B2": "You get to the kitchen at last: the oven cold, nothing on, the clock ticking hard on the wall. Out in the rain, the night is still taking its toll on people. You have to get the dinner going and the kitchen warm again, and fast. And you have to choose what matters most of all, right now, with no time to spare."},
  "c": ["Get it all cooking.", "Check on Gran first.", "That light outside again."]},
 92: {"t": {
  "A2": "Then help reaches you at last — more hands, friends at the door, people who know a kitchen. You're not alone with this now. Others are here to share the load. It's like setting down something heavy you carried too far, too long.",
  "B1": "Then help reaches you at last — more hands, friends at the door, people who know their way round a kitchen. You're not alone with this now. Others are here to share the load. It's like setting down something heavy you'd carried too far, for too long.",
  "B2": "Then help reaches you at last — more hands, friends at the door, people who know their way round a kitchen and aren't afraid of work. You're not alone with this any more. Others are here now to share the load with you. It's like finally setting down something heavy that you'd carried too far, and for far too long."},
  "c": ["Set them to work.", "Keep the dinner going.", "Watch the street."]},
 93: {"t": {
  "A2": "Now you keep the dinner going. What you can make depends on what you carried home. With a full basket, you've plenty to work with. Without it, you must make every last scrap count. Either way, the work is the same: keep going.",
  "B1": "Now you keep the dinner going. What you can make depends on what you carried home with you. With a full basket, you've plenty to work with. Without it, you have to make every last scrap count. Either way, the work is the same: keep going.",
  "B2": "Now you keep the dinner going, come what may. What you can actually make depends on what you carried home with you through the rain. With a full basket, you've plenty to work with. Without it, you have to make every last scrap count twice over. Either way, the work in front of you is the same: keep going, and don't stop."},
  "c": ["A full basket.", "Next to nothing."]},
 94: {"t": {
  "A2": "You go up to check on Gran Ivy. Her eyes open just a little. There's fear in them — then, seeing your face, a bit less fear. 'You're cooking,' she whispers. 'That I am,' you tell her softly. 'Now you rest.'",
  "B1": "You go up to check on Gran Ivy. Her eyes open just a little. There's fear in them — then, seeing your face, a little less fear. 'You're cooking,' she whispers. 'That I am,' you tell her softly. 'Now you rest, and leave it to me.'",
  "B2": "You go up to check on Gran Ivy in her room. Her tired eyes open just a little at the sound of you. There's fear in them at first — then, seeing your face in the doorway, a little less fear. 'You're cooking,' she whispers, almost smiling. 'That I am,' you tell her softly. 'Now you rest, and leave the rest of it to me.'"},
  "c": ["Back down to it.", "Get the food on."]},
 95: {"t": {
  "A2": "The full basket does it. You light the oven, fill the pots, and soon the smells rise — meat, gravy, bread. The kitchen glows warm and golden against the dark window. This, you think, is what a home should feel like.",
  "B1": "The full basket does it. You light the oven, fill the pots, and soon the smells rise — meat, gravy, warm bread. The kitchen glows warm and golden against the dark window. This, you think to yourself, is what a home should feel like.",
  "B2": "The full basket does the trick. You light the oven, fill the pots, and before long the smells begin to rise — meat, gravy, warm bread, all of it. The whole kitchen glows warm and golden against the dark, wet window. This, you think to yourself, is exactly what a home is supposed to feel like on a night like this."},
  "c": ["The long haul now.", "More hands arrive."]},
 96: {"t": {
  "A2": "You've not much food to work with, so you stretch every scrap. A little meat, some veg, a lot of care. You make the one pot go as far as it can. It's thin, and plain. It may be enough — or it may not.",
  "B1": "You've not much food to work with, so you stretch every last scrap. A little meat, some veg, and a lot of care. You make the one pot go as far as it possibly can. It's thin, and plain. It may just be enough — or it may not.",
  "B2": "You've not much food to work with at all, so you stretch every last scrap as far as it will go. A little meat, some veg, and a great deal of care. You make the one pot go as far as it can possibly stretch. It's thin, and plain, and honest. It may just about be enough to go round — or, then again, it may not."},
  "c": ["The long haul now.", "You need more."]},
 97: {"t": {
  "A2": "The meal is thin, and you're afraid it won't stretch to everyone. You've done all you can with what you have. But it may still fall short at the table. You need more now — more food, more hands, or both.",
  "B1": "The meal is thin, and you're afraid it won't stretch to everyone at the table. You've done all you can with what little you have. But it may still fall short in the end. You need more now — more food, more hands, or both.",
  "B2": "The meal is thin, and you're honestly afraid it won't stretch to everyone at the table tonight. You've done all you possibly can with the little you have. But even so, it may still fall short when they all sit down. You need more now — more food, more hands, or, if you're to manage this, probably both."},
  "c": ["The long haul anyway.", "Call round for more."]},
 98: {"t": {
  "A2": "You glance out the window and see it. Far down the street, a light flares and falls. It shows where no one should be, hiding and showing again. It pulls at your eye. And it pulls at something deeper than that.",
  "B1": "You glance out the window and see it. Far down the street, a light flares and falls. It shows where no one should be tonight, hiding and showing again. It pulls at your eye. And it pulls at something deeper than that.",
  "B2": "You glance out of the window and you see it. Far down the dark street, a small light flares and falls. It shows where no one on earth should be tonight, hiding itself and then showing again. It pulls at your eye, that light. And it pulls, if you're honest, at something a good deal deeper than that."},
  "c": ["Keep to the kitchen.", "Go to the light."]},
 99: {"t": {
  "A2": "The light down the street shows again. It shows where everyone says no one would be. But a light means a hand to hold it. A hand means a person. A person out there, alone, in rain and cold like this.",
  "B1": "The light down the street shows again. It shows where everyone swears no one would be. But a light means a hand to hold it. A hand means a person. A person out there, alone, in rain and cold like this one.",
  "B2": "The light down the street shows itself again. It shows where everyone swears blind that no one would be tonight. But a light means a hand to hold it up. And a hand means a person. A person out there, quite alone, in rain and cold like this — and you can't un-know that now."},
  "c": ["Check on Gran first.", "The long haul now."]},
 100: {"t": {
  "A2": "Now comes the long haul. You tend the pots, keep Gran Ivy warm upstairs, and watch the clock creep on. It's not exciting — just steady, careful, tiring work. But it's the whole job tonight. And it's yours.",
  "B1": "Now comes the long haul. You tend the pots, keep Gran Ivy warm upstairs, and watch the clock creep slowly on. It's not exciting — just steady, careful, tiring work. But it's the whole job tonight. And it's yours to do.",
  "B2": "Now comes the long haul of it. You tend the pots, keep Gran Ivy warm upstairs, and watch the clock creep slowly on toward seven. It isn't exciting work — just steady, careful, tiring work that nobody sees. But it's the whole job tonight, start to finish. And it's yours, and no one else's."},
  "c": ["Nearly there.", "That light again.", "The hardest stretch."]},
 101: {"t": {
  "A2": "And then, at last, it turns. The pots are nearly done. The table's set, the bread's warm, the smells fill the house. It's almost seven. You've nearly pulled the whole evening through.",
  "B1": "And then, at last, it turns. The pots are nearly done. The table's set, the bread's warm, and the smells fill the whole house. It's almost seven now. You've nearly pulled the whole evening through.",
  "B2": "And then, at long last, it turns. The pots are nearly done. The table's set, the bread's warm from the oven, and the good smells fill the whole house from top to bottom. It's almost seven now, almost time. You've very nearly pulled the whole long evening through on your own."},
  "c": ["Seven o'clock.", "Dawn of a sort."]},
 102: {"t": {
  "A2": "This is the hardest stretch, the last one before it's done. Nothing's ready yet. Your arms ache, your eyes burn. But you can feel it all coming together, somewhere under the rush. Hold on a little longer.",
  "B1": "This is the hardest stretch, the last one before it's all done. Nothing's quite ready yet. Your arms ache, and your eyes burn. But you can feel it all coming together, somewhere under the rush. Hold on a little longer now.",
  "B2": "This is the hardest stretch of the whole night, the last one before it's finally done. Nothing's quite ready yet, not really. Your arms ache, and your eyes burn with tiredness. But you can feel it all starting to come together, somewhere under the rush and the noise. Just hold on a little longer now."},
  "c": ["Nearly there.", "You're not alone out here."]},
 103: {"t": {
  "A2": "You look out at the street. Warm windows glow all down the row. Other kitchens lit, other families, other dinners cooking in the rain. The whole street got through tonight too. You were never quite as alone as you felt.",
  "B1": "You look out at the street. Warm windows glow all the way down the row. Other kitchens lit, other families, other dinners cooking in the rain. The whole street got through this night too. You were never quite as alone as you'd felt.",
  "B2": "You look out at the dark street. Warm windows glow all the way down the row, one after another. Other kitchens lit, other families, other dinners cooking away in the rain. The whole street got through this night as well as you did. You were never, it turns out, quite as alone out here as you'd felt."},
  "c": ["Seven o'clock.", "Help at the door."]},
 104: {"t": {
  "A2": "At last, help comes through the door. The family, early, coats dripping — more hands, and quick ones. You lean on the counter and watch them pile in, your legs shaking under you now. But the worst of the night is behind you.",
  "B1": "At last, help comes through the door. The family, early, coats dripping — more hands, and quick ones at that. You lean on the counter and watch them pile in, your legs shaking under you now. But the worst of the night is behind you.",
  "B2": "At last, help comes through the door. The family, early, their coats dripping on the mat — more hands, and quick ones at that. You lean on the counter and watch them all pile in, your legs shaking under you now that you've stopped. But the worst of the whole night is well and truly behind you."},
  "c": ["Seven o'clock.", "Too much came home at once."]},
 105: {"t": {
  "A2": "Seven o'clock comes round. The doorbell goes, and the family spill in out of the rain. The table is set, the food is hot, the house is warm. The worst has passed at last. You made it to the hour.",
  "B1": "Seven o'clock comes round. The doorbell goes, and the family spill in out of the rain. The table is set, the food is hot, and the house is warm. The worst has passed at last. You made it to the hour.",
  "B2": "Seven o'clock comes round at last. The doorbell goes, and the whole family spill in out of the rain, laughing and stamping their feet. The table is set, the food is hot, the house is warm and bright. The worst has passed at last, and you can feel it go. You made it, somehow, all the way to the hour."},
  "c": ["See it all added up.", "More hands than you need.", "A small, lovely moment."]},
 106: {"t": {
  "A2": "Then it comes — a laugh from the front room, the first of the night. It rings through the house as if there'd been no rush at all. After the evening you've had, it seems almost absurd. And it's lovely, and you stop to listen.",
  "B1": "Then it comes — a laugh from the front room, the first real one of the night. It rings through the house as if there'd been no rush at all. After the evening you've had, it seems almost absurd. And it's lovely, and you stop just to listen.",
  "B2": "Then it comes — a laugh from the front room, the first real one of the whole night. It rings out through the house as if there'd never been any rush at all. After the evening you've just had, it seems almost absurd that such a sound could exist. And it's lovely, utterly lovely, and you stop whatever you're doing just to listen."},
  "c": ["See it all added up.", "Back to the warm kitchen."]},
 107: {"t": {
  "A2": "From the window you watch the street. Lights come bobbing along, still too far to make out. Something is coming at last. But a light means someone out there. And someone is far better than no one tonight.",
  "B1": "From the window you watch the street. Lights come bobbing along it, still too far off to make out. Something is coming at last. But a light means someone out there. And someone is far better than no one tonight.",
  "B2": "From the window you watch the dark street below. Lights come bobbing along it, still too far off to make out properly. Something is coming at last, down there in the rain. But a light means someone out there, moving. And someone, on a night like this one, is far, far better than no one at all."},
  "c": ["Keep the dinner going.", "The long haul now."]},
 110: {"t": {
  "A2": "Seven o'clock, and the evening adds up to what it is. Whatever you did out there in the rain comes home to you now. Some of it to be proud of, some not. Let's see, then, what it all came to.",
  "B1": "Seven o'clock, and the evening adds up to what it is. Whatever you did out there in the rain comes home to you now. Some of it to be proud of, some of it not. Let's see, then, what it all came to.",
  "B2": "Seven o'clock, and the evening adds up to just exactly what it is. Whatever you did out there in the cold and the rain comes home to you now, all of it. Some of it to be proud of, and some of it not so much. Let's see, then, what the whole long night finally came to in the end."},
  "c": ["You got the dinner made.", "You answered the light.", "What else it came to."]},
 111: {"t": {
  "A2": "The evening adds up — not with one big act, but with many small ones. What you cooked, what you refused, who you went out into the rain for. It all counts in the end. It all made the night what it was.",
  "B1": "The evening adds up — not with one big act, but with many small ones. What you cooked, what you refused, and who you went out into the rain for. It all counts in the end. It all made the night what it was.",
  "B2": "The evening adds up — not, in the end, with one big brave act, but with a great many small ones. What you cooked, what you refused to do, and who you went out into the cold rain for. It all counts in the end, every bit of it. It all made the night into exactly what it was."},
  "c": ["You filled the kitchen.", "You did it honestly.", "What else it came to."]},
 112: {"t": {
  "A2": "There's more to weigh; the night held other things too. A stranger you stopped for in the rain. Food off your own table, given with an open hand. Small choices, made in the cold, when it would have been easier not to.",
  "B1": "There's more to weigh; the night held other things too. A stranger you stopped for out in the rain. Food off your own table, given away with an open hand. Small choices, made in the cold, when it would have been far easier not to.",
  "B2": "There's more still to weigh up; the night held other things too, quieter ones. A stranger you stopped for out in the rain. Food off your own table, given away freely with an open hand. Small choices, all of them, made out in the cold, when it would have been so much easier simply not to bother."},
  "c": ["A kindness came back.", "There was always enough.", "What it leaves you with."]},
 113: {"t": {
  "A2": "And what does the night leave you with? Maybe not a perfect dinner. Maybe just the fact that you tried, that you kept going. When it was late and cold and easy to give up, you didn't. That counts for something.",
  "B1": "And what does the night leave you with? Maybe not a perfect dinner. Maybe just the fact that you tried, and that you kept going. When it was late and cold and easy to give up, you didn't. That counts for something.",
  "B2": "And what, in the end, does the night leave you with? Maybe not a perfect dinner, no. Maybe just the plain fact that you tried, and that you kept going when you could have stopped. When it was late and cold and so easy to give the whole thing up, you simply didn't. And that, whatever else, counts for something."},
  "c": ["A bit late, but good.", "They'll remember you tried.", "The hard end of it."]},
 114: {"t": {
  "A2": "But not every night ends well. Some choices cost more than you knew at the time. Some things, once done, can't be undone. This is the hard end of the evening, where the worst of it comes home.",
  "B1": "But not every night ends well. Some choices cost more than you knew at the time. Some things, once done, simply can't be undone. This is the hard end of the evening, where the worst of it comes home.",
  "B2": "But not every night ends well, and this is the truth of it. Some choices cost a great deal more than you knew at the time you made them. Some things, once done, simply can't be undone again. This is the hard end of the evening, where the worst of it all comes home to roost."},
  "c": ["They found out.", "Burnt, and too late.", "A bit late, but good."]},

 # ---- ENDINGS ----
 120: {"t": {
  "A2": "You got the dinner made. By seven the table is full — hot food, warm bread, every chair taken. Gran Ivy comes down slow, on your arm, to a room full of her family. It all came good because you kept going and would not give up. That is the whole of it.",
  "B1": "You got the dinner made. By seven the table is full — hot food, warm bread, every chair taken. Gran Ivy comes down slowly, on your arm, to a room full of her family. It all came good because you kept going and wouldn't give up. That is the whole of it.",
  "B2": "You got the dinner made. By seven o'clock the table is full — hot food, warm bread, every last chair taken. Gran Ivy comes down slowly, leaning on your arm, into a room full of her family and their noise. It all came good, every bit of it, because you kept going when you were soaked and worn out and would not let yourself give up. That, in the end, is the whole of it."}},
 121: {"t": {
  "A2": "You answered the light no one could explain. You found Nora out in the rain, lost and freezing. You got her in and warm just in time. And more than one thing was saved tonight. At the table, Gran Ivy looks up — and sees the granddaughter she lost years ago. A door everyone thought shut swings open again.",
  "B1": "You answered the light no one could explain. You found Nora out in the rain, lost and freezing, and got her in and warm just in time. And more than one thing was saved tonight. At the table, Gran Ivy looks up — and sees the granddaughter she lost years ago. A door everyone thought shut for good swings open again.",
  "B2": "You answered the light that no one could explain. You found Nora out in the rain, lost and freezing, and got her in and warm again just in time. And more than one thing was saved tonight, as it turns out. At the table, Gran Ivy looks up — and sees the granddaughter she lost years ago, standing in her kitchen. A door everyone had thought shut for good swings quietly open again, and the dinner becomes something far bigger than a meal."}},
 122: {"t": {
  "A2": "There was no clever trick — there was something better. You turned a quiet, tired street into a kitchen full of people. Neighbours peeling, friends stirring, kids laying the table. Together you brought the whole evening through. No one sat alone tonight, and the house has not felt so full in years.",
  "B1": "There was no clever trick — there was something far better. You turned a quiet, tired street into a kitchen full of people. Neighbours peeling, friends stirring, kids laying the table. Together you brought the whole evening through. No one sat alone tonight, and the house hasn't felt so full in years.",
  "B2": "There was no single clever trick that saved the night — there was something far better than that. You turned a quiet, tired street into a kitchen full of warm bodies and noise. Neighbours peeling, friends stirring the pots, kids squabbling over who lays the table. Together, all of you, you brought the whole evening through. No one sat alone tonight, not one soul, and the old house has not felt this full in years."}},
 123: {"t": {
  "A2": "You refused the con — saw Dale's trick for what it was and turned your back on it. You kept your head, and got the dinner on the table by honest work. It wasn't a perfect evening. You burned the odd thing and ran it close. But all of it was yours, and real, and that's worth more than any shortcut.",
  "B1": "You refused the con — saw Dale's trick for what it was and turned your back on it. You kept your head, and got the dinner on the table by honest work. It wasn't a perfect evening. You burned the odd thing, and ran it close. But every bit of it was yours, and real, and that's worth more than any shortcut.",
  "B2": "You refused the con outright — saw Dale's little trick for exactly what it was and turned your back on it. You kept your head, and you got the dinner on the table by honest work and nothing else. It wasn't a perfect evening, mind. You burned the odd thing, and you ran it close to the wire. But every last bit of it was yours, and real, and that is worth a great deal more than any shortcut he was ever selling."}},
 124: {"t": {
  "A2": "You fell short of doing it all alone. But the stranger you stopped for earlier comes back now. They're at the door, a dish warm in their hands. They help you finish the dinner and warm the house. It's not the perfect evening. But a kindness, it turns out, has a way of coming back round.",
  "B1": "You fell short of doing it all on your own. But the stranger you stopped for earlier comes back now, at the door, with a dish in their hands. They help you finish the dinner and warm the house. It's not quite the perfect evening. But a kindness, it turns out, has a way of coming back round.",
  "B2": "You fell short of doing it all on your own, in the end. But the stranger you stopped for earlier comes back now, knocking at the door, with a covered dish warm in their hands. They stay, and help you finish the dinner and warm the house through. It's not quite the perfect evening you'd pictured. But a kindness, it turns out, has a quiet way of coming back round to you when you least expect it."}},
 125: {"t": {
  "A2": "You gave your own food away to those with less. So your table is plainer tonight — bread and soup, not the feast you planned. You didn't manage everything. But no one you met tonight goes to bed hungry. And somehow, shared out, there was always just about enough.",
  "B1": "You gave your own food away to those with less. So your table is plainer tonight — bread and soup, not the feast you'd planned. You didn't manage everything. But no one you met tonight goes to bed hungry. And somehow, shared out, there was always just about enough.",
  "B2": "You gave your own food away to those with less than you. So your table is a plainer one tonight — bread and soup, not the feast you'd planned and shopped for. You didn't manage everything you set out to do. But no one you met out there tonight goes to bed hungry. And somehow, shared out between all those hands, there turned out to be always just about enough to go round."}},
 126: {"t": {
  "A2": "You scrape through the worst of it. The dinner's late, and a bit rough round the edges. But it lands on the table in the end. It's no triumph, and no one will tell stories about it. But the family ate, and laughed, and stayed warm. You got through the night, and that'll do.",
  "B1": "You scrape through the worst of it. The dinner's late, and a bit rough round the edges, but it lands on the table in the end. It's no triumph, and no one will tell stories about it. But the family ate, and laughed, and stayed warm. You got through the night, and that will do.",
  "B2": "You scrape through the worst of it, somehow. The dinner's late, and a bit rough round the edges here and there, but it lands on the table in the end, which is what counts. It's no triumph, and no one will be telling stories about it in years to come. But the family ate, and laughed, and stayed warm and dry. You got through the night in one piece, and tonight, that will do nicely."}},
 127: {"t": {
  "A2": "You didn't pull off all you wanted. But the people round that table saw you try. They saw you come home soaked, and cook, and keep going when you could have stopped. They won't forget it. From tonight, you're the one who tried your heart out for them. And that stays.",
  "B1": "You didn't pull off all you wanted. But the people round that table saw you try — saw you come home soaked, and cook, and keep going when you could have stopped. They won't forget it. From tonight on, you're the one who tried your heart out for them. And that stays.",
  "B2": "You didn't pull off all that you wanted to, not quite. But the people round that table saw you try — saw you come home soaked to the skin, and cook, and keep going when you could so easily have stopped and sat down. They won't forget it in a hurry. From tonight on, you're the one who tried your heart out for them, on the worst of nights. And that, whatever else, stays with people."}},
 128: {"t": {
  "A2": "You took Dale's deal, and at the table it all comes out. Someone tastes it, frowns, and asks where it's really from. The lie unravels, dish by dish. The money's gone, the food's cold, and the evening dies in an awkward hush. You won't forget the look on Gran's face in a hurry.",
  "B1": "You took Dale's deal, and at the table it all comes out. Someone tastes it, frowns, and asks where it's really from. The lie unravels, dish by dish. The money's gone, the food's cold, and the evening dies in an awkward hush. You won't forget the look on Gran's face in a hurry.",
  "B2": "You took Dale's deal, and at the table it all comes out in the end. Someone tastes it, frowns, and asks, quite innocently, where it's really from. The lie unravels after that, dish by dish, in front of everyone. The money's gone, the food's cold, and the whole evening dies away into an awkward, horrible hush. You won't forget the look on Gran's face tonight in a hurry — nor, you suspect, will she."}},
 129: {"t": {
  "A2": "The main road was a trap, just as Joan warned. A car came too fast in the rain, and only a hard fall onto the kerb saved you. You limp home, soaked, shaken and hours too late. The family have long since gone. You should have gone the long way round, and you know it now.",
  "B1": "The main road was a trap, just as Joan warned you. A car came too fast in the rain, and only a hard fall onto the kerb saved you. You limp home, soaked, shaken, and hours too late. The family have long since gone. You should have gone the long way round, and you know it now.",
  "B2": "The main road was a trap, just exactly as Joan had warned you it would be. A car came too fast out of the rain, and only a hard, jarring fall back onto the kerb saved you at the very last second. You limp home after that, soaked, shaken, and hours too late for any of it. The family have long since given up and gone. You should have gone the long way round, like she said, and you know it now, too late."}},
 130: {"t": {
  "A2": "You spent the evening on the wrong things, and the dinner paid for it. The oven was left too long; the pots caught and burned. By the time the family come, the kitchen is full of smoke and the table is bare. You did try, in your way. But trying, tonight, was not quite enough.",
  "B1": "You spent the evening on the wrong things, and the dinner paid for it. The oven was left too long; the pots caught and burned. By the time the family come, the kitchen is full of smoke and the table is bare. You did try, in your own way. But trying, tonight, was not quite enough.",
  "B2": "You spent the evening on the wrong things, one after another, and the dinner paid the price for it. The oven was left too long; the pots caught and burned black. By the time the family finally come in, the kitchen is full of smoke and the long table is bare. You did try, in your own way, you really did. But trying, tonight of all nights, was not quite enough to get a meal on the table."}},
 131: {"t": {
  "A2": "In the end, you gave up. You sat down, put the telly on, and told yourself it was all too much for one person. You said no one could blame you. You said they'd understand. And maybe they would. But the chairs stayed empty, and the oven stayed cold. You never found out what the evening might have been.",
  "B1": "In the end, you gave up. You sat down, put the telly on, and told yourself it was all too much for one person. You said no one could blame you. You said they'd understand. And maybe they would have. But the chairs stayed empty, the oven stayed cold, and you never found out what the evening might have been.",
  "B2": "In the end, you simply gave up. You sat down, put the telly on, and told yourself it was all far too much for one person to manage alone. You said no one could possibly blame you. You said, over and over, that they'd understand. And maybe, in time, they would have. But the chairs stayed empty, the oven stayed stone cold, and you never did find out what the evening might have been, if only you'd kept going."}},
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
