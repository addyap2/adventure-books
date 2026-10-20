#!/usr/bin/env python3
"""Phase 3 prose for The Interview (episode-10), batch F: Act III finale (90-114)
and the 12 endings (120-131). Run: python3 scripts/generators/phase3_ep10_f.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-10.json")

D = {
 90: {"t": {
  "A2": "You reach the office at last, soaked and worn out, with two almost here. Up on the top floor, the panel is waiting behind a closed door. The waiting room is cold and quiet, the clock loud on the wall. This is the moment it all rests on. Everything now comes down to what you do next.",
  "B1": "You reach the office at last, soaked and worn out, with two almost here. Up on the top floor, the panel is waiting behind a closed door. The waiting room is cold and quiet, the clock loud on the wall. This is the moment it all rests on. Everything now comes down to what you do in the next hour.",
  "B2": "You reach the office at last, soaked to the skin and worn right out, with two o'clock almost upon you. Up on the top floor, the panel is waiting behind a closed door. The waiting room is cold and quiet, the clock loud on the bare wall. This is the moment the whole day rests on. Everything now comes down to what you do in the next short hour."},
  "c": ["Sign in and get ready.", "Reese, at the door again.", "A friendly face arrives."]},
 91: {"t": {
  "A2": "You reach the desk and sign in: your name, the time, a stiff nod from the clerk. Out there, the day is still working against you. You have to get yourself ready and your head straight. And you have to choose what matters most, right now.",
  "B1": "You reach the desk and sign in: your name, the time, a stiff nod from the clerk. Out there, the day is still working against you. You have to get yourself ready and your head straight again. And you have to choose what matters most, right now.",
  "B2": "You reach the desk and sign in at last: your name, the time, a stiff nod from the clerk. Out there, the day is still working against you. You have to get yourself ready and your head straight again, and fast. And you have to choose what matters most of all, right now, with no time to spare."},
  "c": ["Get yourself ready.", "Call home first.", "That figure again."]},
 92: {"t": {
  "A2": "Then help reaches you at last. A text, a friend in the lobby, a kind word from someone who's done this. You're not alone with it now. Others have your back. It's like setting down something heavy you carried too far, too long.",
  "B1": "Then help reaches you at last — a text, a friend in the lobby, a kind word from someone who's done this before. You're not alone with it now. Others have your back. It's like setting down something heavy you'd carried too far, for too long.",
  "B2": "Then help reaches you at last — a text, a friend waiting in the lobby, a kind word from someone who's done this before and come out the other side. You're not alone with it any more. Others have your back now. It's like finally setting down something heavy that you'd carried too far, and for far too long."},
  "c": ["Set to work on yourself.", "Settle in for the wait.", "Watch the lifts."]},
 93: {"t": {
  "A2": "Now you get yourself ready. What you can do depends on what you brought with you. With your papers in order, you've plenty to work with. Without them, you must make every word count. Either way, the work is the same: keep calm, keep going.",
  "B1": "Now you get yourself ready. What you can do depends on what you brought with you. With your papers in order, you've plenty to work with. Without them, you have to make every word count. Either way, the work is the same: keep calm, keep going.",
  "B2": "Now you get yourself ready, come what may. What you can do depends on what you carried in with you. With your papers in order, you've plenty to work with. Without them, you have to make every single word count. Either way, the work in front of you is the same: keep calm, and keep going."},
  "c": ["Papers all in order.", "Next to nothing ready."]},
 94: {"t": {
  "A2": "You step outside and call home. Your dad picks up, and his voice is there at once. There's worry in it — then, hearing you steady, a bit less worry. 'You're nearly there,' he says. 'I am,' you tell him softly. 'Now let me go and do it.'",
  "B1": "You step outside and call home. Your dad picks up, and his voice is there at once. There's worry in it — then, hearing you steady, a little less worry. 'You're nearly there,' he says. 'I am,' you tell him softly. 'Now let me go and do it.'",
  "B2": "You step outside the room and call home. Your dad picks up, and his voice is there at once, like it always is. There's worry in it at first — then, hearing you sound steady, a little less worry. 'You're nearly there,' he says. 'I am,' you tell him softly. 'Now let me go in and do it.'"},
  "c": ["Back in, ready.", "Papers in order."]},
 95: {"t": {
  "A2": "Your papers do it. You lay them out, read your notes, and slowly the answers come clear in your head. Your breathing settles. The room feels warmer, your nerves quieter. This, you think, is what being ready feels like.",
  "B1": "Your papers do it. You lay them out, read over your notes, and slowly the answers come clear in your head. Your breathing settles. The room feels warmer, your nerves quieter now. This, you think to yourself, is what being ready feels like.",
  "B2": "Your papers do the trick. You lay them out, read over your notes, and slowly the answers come clear in your head, one by one. Your breathing settles at last. The whole room feels warmer, and your nerves quieter now. This, you think to yourself, is exactly what being ready feels like."},
  "c": ["The long wait now.", "A friend checks in."]},
 96: {"t": {
  "A2": "You've not much ready, so you make the most of every scrap. A few good lines, a clear head, and a lot of nerve. You run them over and over. It's thin, and bare. It may be enough — or it may not.",
  "B1": "You've not much ready, so you make the most of every last scrap. A few good lines, a clear head, and a lot of nerve. You run them over and over. It's thin, and bare. It may just be enough — or it may not.",
  "B2": "You've not much ready at all, so you make the most of every last scrap. A few good lines, a clear head, and a great deal of nerve. You run them over and over in your mind. It's thin, and bare, and honest. It may just about be enough — or, then again, it may not."},
  "c": ["The long wait now.", "You need more."]},
 97: {"t": {
  "A2": "What you have is thin, and you're afraid it won't carry you through the room. You've done all you can with what little you brought. But it may still fall short at the table. You need more now — more notes, more calm, or both.",
  "B1": "What you have is thin, and you're afraid it won't carry you through the room. You've done all you can with the little you brought. But it may still fall short in the end. You need more now — more notes, more calm, or both.",
  "B2": "What you have is thin, and you're honestly afraid it won't carry you through the room. You've done all you possibly can with the little you brought. But even so, it may still fall short when they start to ask. You need more now — more notes, more calm, or, if you're to manage this, probably both."},
  "c": ["The long wait anyway.", "Call round for help."]},
 98: {"t": {
  "A2": "You glance across the waiting room and see it. By the far window, that figure again — still, half-turned, watching. It's where no one you'd expect would be. It pulls at your eye. And it pulls at something deeper than that.",
  "B1": "You glance across the waiting room and see it. By the far window, that figure again — still, half-turned, watching. It's where no one you'd expect to see would be. It pulls at your eye. And it pulls at something deeper than that.",
  "B2": "You glance across the waiting room and you see it. By the far window, that figure again — quite still, half-turned, watching the room. It's standing where no one you'd ever expect to see would be. It pulls at your eye, that figure. And it pulls, if you're honest, at something a good deal deeper than that."},
  "c": ["Keep to your papers.", "Go to the figure."]},
 99: {"t": {
  "A2": "The figure by the window shows again. It stands where you'd swear no one you knew would be. But a face you half know means a story. A story means a choice. A person right there, from your past, on today of all days.",
  "B1": "The figure by the window shows again. It stands where you'd swear no one you knew would be. But a face you half know means a story. A story means a choice. A person right there, from your past, on today of all days.",
  "B2": "The figure by the window shows itself again. It stands where you'd swear blind that no one you knew would be. But a face you half know means a story behind it. And a story means a choice to make. A person standing right there, out of your past, on today of all days — and you can't un-see it now."},
  "c": ["Call home first.", "The long wait now."]},
 100: {"t": {
  "A2": "Now comes the long wait. You sit, you breathe, you watch the clock crawl toward two. It's not exciting — just the slow, hard work of keeping your nerve. But it's the whole job right now. And it's yours to do.",
  "B1": "Now comes the long wait. You sit, you breathe, you watch the clock crawl slowly toward two. It's not exciting — just the slow, hard work of keeping your nerve. But it's the whole job right now. And it's yours to do.",
  "B2": "Now comes the long wait of it. You sit, you breathe, you watch the clock crawl slowly toward two o'clock. It isn't exciting work — just the slow, hard work of keeping your nerve steady. But it's the whole job right now, start to finish. And it's yours, and no one else's."},
  "c": ["Nearly your turn.", "That figure again.", "The hardest wait."]},
 101: {"t": {
  "A2": "And then, at last, it turns. The door opens. A name is called. The one before you comes out, pale and relieved. It's almost two now. You've nearly got yourself through the whole wait. Soon it will be your name on the clerk's lips.",
  "B1": "And then, at last, it turns. The door opens. A name is called. The one before you comes out, pale and relieved. It's almost two now. You've nearly got yourself through the whole wait. Soon it will be your name on the clerk's lips.",
  "B2": "And then, at long last, it turns. The door opens. A name is called out. The one before you comes out, pale and relieved, and it's over for them. It's almost two now, almost time. You've very nearly got yourself through the whole long wait. Soon it will be your name they call across the room."},
  "c": ["Your name is called.", "Two o'clock."]},
 102: {"t": {
  "A2": "This is the hardest wait, the last one before your name. Nothing has happened yet. Your heart pounds, your mouth is dry. But you can feel yourself coming together, somewhere under the fear. Hold on a little longer.",
  "B1": "This is the hardest wait, the last one before your name is called. Nothing has happened yet. Your heart pounds, and your mouth is dry. But you can feel yourself coming together, somewhere under the fear. Hold on a little longer now.",
  "B2": "This is the hardest wait of the whole day, the last one before your name is called. Nothing has happened yet, not really. Your heart pounds, and your mouth is dry as dust. But you can feel yourself starting to come together, somewhere under the fear. Just hold on a little longer now."},
  "c": ["Nearly your turn.", "You're not alone in here."]},
 103: {"t": {
  "A2": "You look round the waiting room. Other people sit with their nerves, same as you. Other hopes, other mornings just as hard. You all got here, through all of it. You were never quite as alone as you felt.",
  "B1": "You look round the waiting room. Other people sit with their nerves, same as you. Other hopes, other mornings just as hard. You all got here, through all of it. You were never quite as alone as you'd felt.",
  "B2": "You look round the waiting room at the others. Other people sit with their nerves, exactly the same as you. Other hopes, other mornings every bit as hard. You all got here in the end, through all of it. You were never, it turns out, quite as alone as you'd felt."},
  "c": ["Your name is called.", "The door opens."]},
 104: {"t": {
  "A2": "At last, the door opens and your name is said. A hand waves you in — the panel, warm light, three faces turning to you. You stand, your legs shaking under you now. But the worst of the waiting is behind you.",
  "B1": "At last, the door opens and your name is said. A hand waves you in — the panel, warm light, three faces turning to you. You stand, your legs shaking under you now. But the worst of the waiting is behind you.",
  "B2": "At last, the door opens and your name is said aloud. A hand waves you in — the panel, warm light, three faces turning to you at once. You stand, your legs shaking under you now that the moment's here. But the worst of the long waiting is well and truly behind you."},
  "c": ["See it all added up.", "Too much, too fast."]},
 105: {"t": {
  "A2": "Two o'clock comes round. The door opens, and your name is called clear. You walk in. The panel is set, the light is warm, the room is ready. The worst has passed at last. You made it to the hour.",
  "B1": "Two o'clock comes round. The door opens, and your name is called out clear. You walk in. The panel is set, the light is warm, and the room is ready. The worst has passed at last. You made it to the hour.",
  "B2": "Two o'clock comes round at last. The door opens, and your name is called out clear across the room. You walk in. The panel is set, the light is warm, the room is ready for you. The worst has passed at last, and you can feel it go. You made it, somehow, all the way to the hour."},
  "c": ["See it all added up.", "A friend's last word.", "A small, good moment."]},
 106: {"t": {
  "A2": "Then it comes — a small laugh across the table, the first of the day. The room warms, just like that. After the morning you've had, it seems almost absurd. And it's good, and you let yourself breathe at last.",
  "B1": "Then it comes — a small laugh across the table, the first real one of the day. The room warms, just like that. After the morning you've had, it seems almost absurd. And it's good, and you let yourself breathe at last.",
  "B2": "Then it comes — a small laugh across the table, the first real one of the whole day. The room warms, just like that, all at once. After the morning you've just had, it seems almost absurd that such a thing could happen. And it's good, honestly good, and you let yourself breathe at last."},
  "c": ["See it all added up.", "Back to it, steadier."]},
 107: {"t": {
  "A2": "From the waiting room you watch the lifts. People come and go, nervy and quick, too far to read. Something is coming, one way or another. But a lift means someone arriving. And someone, today, is better than facing it all alone.",
  "B1": "From the waiting room you watch the lifts. People come and go, nervy and quick, too far off to read. Something is coming, one way or another. But a lift means someone arriving. And someone, today, is better than facing it all alone.",
  "B2": "From the waiting room you watch the lifts open and close. People come and go, nervy and quick, still too far off to read properly. Something is coming, one way or another, down there. But a lift means someone arriving. And someone, on a day like this one, is far better than facing it all alone."},
  "c": ["Keep to your papers.", "The long wait now."]},
 110: {"t": {
  "A2": "Two o'clock, and the morning adds up to what it is. Whatever you did out there comes with you into the room now. Some of it to be proud of, some not. Let's see, then, what it all came to.",
  "B1": "Two o'clock, and the morning adds up to what it is. Whatever you did out there comes with you into the room now. Some of it to be proud of, some of it not. Let's see, then, what it all came to.",
  "B2": "Two o'clock, and the morning adds up to just exactly what it is. Whatever you did out there, in the cold and the rain, comes with you into the room now, all of it. Some of it to be proud of, and some of it not so much. Let's see, then, what the whole hard morning finally came to."},
  "c": ["You earned it straight.", "You faced the past.", "What else it came to."]},
 111: {"t": {
  "A2": "The morning adds up — not with one big move, but with many small ones. What you got ready, what you refused, who you stopped for on the way. It all counts in the end. It all made the day what it was.",
  "B1": "The morning adds up — not with one big move, but with many small ones. What you got ready, what you refused, and who you stopped for on the way. It all counts in the end. It all made the day what it was.",
  "B2": "The morning adds up — not, in the end, with one big move, but with a great many small ones. What you got ready, what you refused to do, and who you stopped for along the way. It all counts in the end, every bit of it. It all made the day into exactly what it was."},
  "c": ["You lifted the whole room.", "You did it honestly.", "What else it came to."]},
 112: {"t": {
  "A2": "There's more to weigh; the day held other things too. A stranger you stopped for in the rain. Your own notes, given away with an open hand. Small choices, made in the cold, when it would have been easier not to.",
  "B1": "There's more to weigh; the day held other things too. A stranger you stopped for out in the rain. Your own notes, given away with an open hand. Small choices, made in the cold, when it would have been far easier not to.",
  "B2": "There's more still to weigh up; the day held other things too, quieter ones. A stranger you stopped for out in the rain. Your own notes, given away freely with an open hand. Small choices, all of them, made out in the cold, when it would have been so much easier simply not to bother."},
  "c": ["A kindness came back.", "You gave it away.", "What it leaves you with."]},
 113: {"t": {
  "A2": "And what does the day leave you with? Maybe not the perfect interview. Maybe just the fact that you tried, that you kept going. When it was cold and late and easy to give up, you didn't. That counts for something.",
  "B1": "And what does the day leave you with? Maybe not the perfect interview. Maybe just the fact that you tried, and that you kept going. When it was cold and late and easy to give up, you didn't. That counts for something.",
  "B2": "And what, in the end, does the day leave you with? Maybe not the perfect interview, no. Maybe just the plain fact that you tried, and that you kept going when you could have stopped. When it was cold and late and so easy to give the whole thing up, you simply didn't. And that, whatever else, counts for something."},
  "c": ["A bit shaky, but good.", "They'll remember you tried.", "The hard end of it."]},
 114: {"t": {
  "A2": "But not every day ends well. Some choices cost more than you knew at the time. Some things, once done, can't be undone. This is the hard end of the day, where the worst of it comes home.",
  "B1": "But not every day ends well. Some choices cost more than you knew at the time. Some things, once done, simply can't be undone. This is the hard end of the day, where the worst of it comes home.",
  "B2": "But not every day ends well, and this is the truth of it. Some choices cost a great deal more than you knew at the time you made them. Some things, once done, simply can't be undone again. This is the hard end of the day, where the worst of it all comes home to roost."},
  "c": ["They found out.", "Too late, too thin.", "A bit shaky, but good."]},

 # ---- ENDINGS ----
 120: {"t": {
  "A2": "You earned it straight. You answered as yourself, honest and clear, and by the end the room had warmed to you. 'We'll be in touch,' they say — but the handshake says more. You'll get the call. It all came good because you went in as yourself and would not fake it. That is the whole of it.",
  "B1": "You earned it straight. You answered as yourself, honest and clear, and by the end the room had warmed to you. 'We'll be in touch,' they say — but the handshake says more. You'll get the call. It all came good because you went in as yourself and wouldn't fake it. That is the whole of it.",
  "B2": "You earned it straight. You answered as yourself, honest and clear, and by the end the whole room had warmed to you. 'We'll be in touch,' they say — but the handshake says a good deal more than that. You'll get the call, you're sure of it. It all came good, every bit of it, because you went in as yourself and would not fake a word. That, in the end, is the whole of it."}},
 121: {"t": {
  "A2": "You faced the past no one could change. You found Maya before the room. You said the thing you'd left unsaid for years, and let the old rift heal. And more than one thing was mended today. Across the table, Maya meets your eye. Not as a stranger, but as the partner you lost and found. A door everyone thought shut swings open.",
  "B1": "You faced the past no one could change. You found Maya before the room, said the thing you'd left unsaid for years, and let the old rift heal. And more than one thing was mended today. Across the table, Maya meets your eye — not as a stranger, but as the partner you lost and found again. A door everyone thought shut for good swings open.",
  "B2": "You faced the past that no one could change. You found Maya before the room, said the thing you'd left unsaid for years, and let the old rift finally heal. And more than one thing was mended today, as it turns out. Across the table, Maya meets your eye — not as a stranger, but as the partner you once lost and have somehow found again. A door everyone had thought shut for good swings quietly open, and the day becomes something far bigger than a job."}},
 122: {"t": {
  "A2": "There was no clever trick — there was something far better. You turned a room full of frightened strangers into people helping each other. One shared notes, one steadied another, one cheered the next one in. You all walked in better for it. No one faced it alone today, and they won't forget who started that.",
  "B1": "There was no clever trick — there was something far better. You turned a room full of frightened strangers into people helping each other. One shared notes, one steadied another, one cheered the next one in. You all walked in better for it. No one faced it alone today, and they won't forget who started that.",
  "B2": "There was no clever trick that got you through — there was something far better than that. You turned a whole room full of frightened strangers into people helping each other out. One shared notes, one steadied another's hands, one cheered the next one in through the door. You all walked in better for it. No one faced it alone today, not one of them, and they won't soon forget who started that."}},
 123: {"t": {
  "A2": "You refused the con. You saw Reese's trick for what it was, and turned your back on it. You kept your nerve, and earned your place in that room by honest work. It wasn't a perfect day. You stumbled on a question, and came close to the wire. But every word was yours, and real. And that's worth more than any shortcut.",
  "B1": "You refused the con — saw Reese's trick for what it was and turned your back on it. You kept your nerve, and earned your place in that room by honest work. It wasn't a perfect day. You stumbled on a question, and ran it close. But every word was yours, and real, and that's worth more than any shortcut.",
  "B2": "You refused the con outright — saw Reese's little trick for exactly what it was and turned your back on it. You kept your nerve, and earned your place in that room by honest work and nothing else. It wasn't a perfect day, mind. You stumbled badly on one question, and ran it close to the wire. But every last word was yours, and real, and that is worth a great deal more than any shortcut he was ever selling."}},
 124: {"t": {
  "A2": "You fell short of doing it all on your own. But the stranger you stopped for earlier turns up again. They quietly put in a word for you at the desk. It opens a door you couldn't. It's not quite the perfect day. But a kindness, it turns out, has a way of coming back round.",
  "B1": "You fell short of doing it all on your own. But the stranger you stopped for earlier turns up again — and quietly puts in a word for you at the desk. It opens a door you couldn't. It's not quite the perfect day. But a kindness, it turns out, has a way of coming back round.",
  "B2": "You fell short of doing it all on your own, in the end. But the stranger you stopped for earlier turns up again — and quietly puts in a word for you at the desk, where it counts. It opens a door you couldn't have opened yourself. It's not quite the perfect day you'd pictured. But a kindness, it turns out, has a quiet way of coming back round to you when you least expect it."}},
 125: {"t": {
  "A2": "You gave your own notes away to someone with less. So you walked in with less in your own hand. Just your bare words, your clear head, and nothing more. You didn't get everything you wanted. But the one you helped got their chance, and so did you. And somehow, shared out, there was just about enough.",
  "B1": "You gave your own notes away to someone with less. So you walked in with less in your own hand — your bare words, your clear head, and nothing more. You didn't get everything you wanted. But the one you helped got their chance, and so did you. And somehow, shared out, there was just about enough.",
  "B2": "You gave your own notes away to someone with less than you. So you walked in with less in your own hand — your bare words, your clear head, and nothing else besides. You didn't get everything you wanted out of the day. But the one you helped got their chance, and so, in the end, did you. And somehow, shared out between you, there turned out to be just about enough to go round."}},
 126: {"t": {
  "A2": "You scrape through the worst of it. The interview's a bit rough round the edges. A lost word here, a shaky start there. But you get through it. It's no triumph, and no one will tell stories about it. But you sat in that room, answered straight, and held your nerve. You got through the day, and that'll do.",
  "B1": "You scrape through the worst of it. The interview's a bit rough round the edges — a lost word here, a shaky start there — but you get through it in the end. It's no triumph, and no one will tell stories about it. But you sat in that room, answered straight, and held your nerve. You got through the day, and that will do.",
  "B2": "You scrape through the worst of it, somehow. The interview's a bit rough round the edges here and there — a lost word, a shaky start — but you get through it in the end, which is what counts. It's no triumph, and no one will be telling stories about it. But you sat in that room, answered straight, and held your nerve to the last. You got through the day in one piece, and today, that will do nicely."}},
 127: {"t": {
  "A2": "You didn't land it this time. But the people across that table saw you try. They saw you come in soaked, steady yourself, and keep going when you could have folded. They won't forget it. 'Not this role,' one says. 'But stay in touch.' From today, you're the one who showed up and gave it everything. And that stays.",
  "B1": "You didn't land it this time. But the people across that table saw you try — saw you come in soaked, and steady yourself, and keep going when you could have folded. They won't forget it. 'Not this role,' one says, 'but stay in touch.' From today on, you're the one who showed up and gave it everything. And that stays.",
  "B2": "You didn't land it this time, not quite. But the people across that table saw you try — saw you come in soaked to the skin, and steady yourself, and keep going when you could so easily have folded. They won't forget it in a hurry. 'Not this role,' one says, kindly, 'but do stay in touch.' From today on, you're the one who showed up and gave it everything. And that, whatever else, stays with people."}},
 128: {"t": {
  "A2": "You took Reese's deal, and in the room it all comes out. A question turns, and your borrowed answer doesn't fit. The panel glance at each other. The story unravels, line by line. The job's gone, the money's gone, and the room goes cold and quiet. You won't forget the look on Maya's face in a hurry.",
  "B1": "You took Reese's deal, and in the room it all comes out. A question turns, and your borrowed answer doesn't fit. The panel glance at each other. The story unravels, line by line. The job's gone, the money's gone, and the room goes cold and quiet. You won't forget the look on Maya's face in a hurry.",
  "B2": "You took Reese's deal, and in the room it all comes out in the end. A question turns, and your borrowed answer doesn't fit it at all. The panel glance at each other. The story unravels after that, line by line, in front of everyone. The job's gone, the money's gone, and the whole room goes cold and quiet. You won't forget the look on Maya's face today in a hurry — nor, you suspect, will she."}},
 129: {"t": {
  "A2": "The queue was a trap, just as Frank warned. The guard pulled you out of the crush, and there was no talking your way clear. By the time it's sorted, you've missed your slot and your name is mud. You limp away, soaked and shaken and hours too late. You should have waited your turn, and you know it now.",
  "B1": "The queue was a trap, just as Frank warned you. The guard pulled you out of the crush, and there was no talking your way clear. By the time it's sorted, you've missed your slot and your name is mud. You limp away, soaked and shaken, and hours too late. You should have waited your turn, and you know it now.",
  "B2": "The queue was a trap, just exactly as Frank had warned you it would be. The guard pulled you out of the crush, and there was no talking your way clear of it. By the time it's all sorted, you've missed your slot and your name is mud. You limp away after that, soaked and shaken and hours too late for any of it. You should have waited your turn, like he said, and you know it now, too late."}},
 130: {"t": {
  "A2": "You spent the morning on the wrong things, and the interview paid for it. You walked in late and unready, your head a mess, your words gone. By the time you find them, the panel have moved on. You did try, in your own way. But trying, today, was not quite enough.",
  "B1": "You spent the morning on the wrong things, and the interview paid for it. You walked in late and unready, your head a mess, your words gone. By the time you find them again, the panel have moved on. You did try, in your own way. But trying, today, was not quite enough.",
  "B2": "You spent the morning on the wrong things, one after another, and the interview paid the price for it. You walked in late and unready, your head a mess, your words gone just when you needed them. By the time you find them again, the panel have already moved on. You did try, in your own way, you really did. But trying, today of all days, was not quite enough to carry the room."}},
 131: {"t": {
  "A2": "In the end, you gave up. You turned back, went home, and told yourself the day was too much for one person. You said no one could blame you. You said they'd understand. And maybe they would. But the chair stayed empty, and the room moved on without you. You never found out what the day might have been.",
  "B1": "In the end, you gave up. You turned back, went home, and told yourself the day was too much for one person. You said no one could blame you. You said they'd understand. And maybe they would have. But the chair stayed empty, the room moved on without you, and you never found out what the day might have been.",
  "B2": "In the end, you simply gave up. You turned back, went home, and told yourself the day was far too much for one person to manage alone. You said no one could possibly blame you. You said, over and over, that they'd understand. And maybe, in time, they would have. But the chair stayed empty, the room moved on without you, and you never did find out what the day might have been, if only you'd kept going."}},
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
