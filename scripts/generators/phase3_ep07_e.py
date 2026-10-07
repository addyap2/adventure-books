#!/usr/bin/env python3
"""Phase 3 prose for The Refuge (episode-07), batch E (final): skipped Act I/II
beats, Act III (90-114), and the 12 endings (120-131). Completes Phase 3.
Run: python3 scripts/generators/phase3_ep07_e.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "content", "episode-07.json")

D = {
 9: {"t": {
  "A2": "Doune heaves open the fuel store and holds up the lamp. Inside are a drum of oil, matches, dry wood, and sacking. 'Take what you need,' he says. 'I'll stay by the radio and raise who I can.' He is a steady man, and tonight it shows.",
  "B1": "Doune heaves open the fuel store and holds up the lamp. Inside are a drum of oil, a box of matches, bundles of dry wood, and sacking. 'Take what you need,' he says. 'I'll stay here by the radio and raise who I can.' He's a steady man, and on a night like this it shows.",
  "B2": "Doune heaves open the fuel store and holds up the lamp. Inside are a drum of lamp-oil, a box of matches, bundles of dry wood, and dry sacking. 'Take what you need,' he says. 'I'll stay here by the radio and raise who I can.' He's a steady man, and on a night like this one it shows."},
  "c": ["Take charge of the fuel and wood.", "Just a lamp and kindling.", "Ask Doune what he knows.", "He presses the last dry lamp on you."]},
 10: {"t": {
  "A2": "You knock along the bunks, and old Breck opens up, pale in the cold. His little stove has gone out, his matches are done, and his hands shake too hard to strike one. 'I can't get it lit,' he says. You have a long night ahead. But he is here, and frightened, and asking you.",
  "B1": "You knock along the bunks, and old Breck opens up, pale in the cold. His little stove has gone out, his matches are finished, and his hands are shaking too hard to strike one. 'I can't get it lit,' he says. You have a long, hard night ahead of you. But he's here, and he's frightened, and he's asking you.",
  "B2": "You knock along the bunks, and old Breck opens up, pale in the cold. His little stove has gone out, his matches are finished, and his hands are shaking too hard to strike one. 'I can't get it lit,' he says. You have a long, hard night ahead of you — but he's here, and he's frightened, and he's asking you, and that settles it."},
  "c": ["Stop and help him.", "Say you must keep the refuge."]},
 12: {"t": {
  "A2": "You go door to door, asking each the same thing. Bring wood for the stove. Lend a hand at the hut. Help me hold the lamp in the window. Some turn away and shut the door. But a few pull on their coats and step out. Tonight, a few is enough to begin.",
  "B1": "You go door to door, asking each the same thing. Bring wood for the stove. Lend a hand at the hut. Help me hold the lamp in the window. Some turn away and shut the door. But a few pull on their coats and step out into the cold. Tonight, a few is enough to begin.",
  "B2": "You go door to door down the valley, asking each the same thing. Bring wood for the stove. Lend a hand at the hut. Help me hold the lamp in the window. Some turn away and shut the door on the cold. But a few pull on their coats and step out into it. Tonight, out here, a few is enough to begin."},
  "c": ["The valley turns out.", "No one stirs; go on alone."]},
 27: {"t": {
  "A2": "The cornice would halve the way, and the far store lies close beyond it. But the edge is thin and the snow is loose over the long drop. Doune told you to keep off it. And he was not joking.",
  "B1": "The cornice would halve the way, and the far store lies close beyond it. But the edge is thin and the snow is loose over a long, deadly drop. Doune told you to keep off it — and he wasn't joking.",
  "B2": "The cornice would halve the way, and the far store lies close beyond it. But the edge is thin and the snow loose and treacherous over the long drop into the corrie. Doune told you to keep well off it — and he wasn't joking."},
  "c": ["Risk the cornice.", "Too dangerous — back to the path."]},
 32: {"t": {
  "A2": "A party is shut in a freezing bothy — no fire, no lamp, a child crying in the dark. The two adults look at you with tired, hopeless eyes. You have a lamp and a coat of your own. Not much, but more than they have got.",
  "B1": "A party is shut in a freezing bothy — no fire, no lamp, a child crying in the dark. The adults look at you with tired, hopeless eyes. You have a lamp and a coat of your own. Not much, but more than they've got.",
  "B2": "A small party is shut in a freezing bothy — no fire, no lamp, a child crying somewhere in the dark. The two adults look at you with tired, hopeless eyes. You have a lamp and a coat of your own. Not much, out here, but more than they have got."},
  "c": ["Give them your lamp and coat.", "Promise to send help.", "Try to get their stove going."]},
 41: {"t": {
  "A2": "The offer is a hook, and you feel it set. He leans in close. 'That refuge is lost already,' he says, low. 'Let the cold take it — and there's a share in it for you.' It is a cruel thing to say. And it is meant to work on your fear.",
  "B1": "The offer is a hook, and you feel it set. He leans in close. 'That refuge is lost already,' he says, low. 'Let the cold take it — and there's a share in it for you.' It's a cruel thing to say. And it is meant to work on your fear.",
  "B2": "The offer is a hook, and you feel it set. He leans in close, out of the wind. 'That refuge is lost already,' he says, low. 'Let the cold take it — and there's a share in it for you.' It's a cruel thing to say. And it is meant, every word, to work on your fear."},
  "c": ["Take his deal.", "That's the tell — refuse.", "Ask what he really wants.", "The frightened folk press in."]},
 69: {"t": {
  "A2": "A snow-choked bivvy presses in around you — white, silent, deep cold, a place where nothing seems alive. Then you hear it: breathing, weak and close, under the snow. Someone is alive in here after all.",
  "B1": "A snow-choked bivvy presses in around you — white, silent, deep cold, a place where nothing seems left alive. Then you hear it: breathing, weak and close, under the snow. Someone is alive in here after all.",
  "B2": "A snow-choked bivvy presses in around you — white, silent, deep with old cold, a place where nothing seems left alive at all. Then you hear it: breathing, weak and close, somewhere under the snow. Someone is alive in here after all."},
  "c": ["Follow the breathing, and find them.", "It's too much — back to the hut."]},
 90: {"t": {
  "A2": "You are back at the refuge, frozen through, the hardest cold of the night pressing down on everything. By the ladder, Marta lies grey and still. The stove is burning low, the window dim. This is the hour the whole night turns on.",
  "B1": "You're back at the refuge, frozen through, the hardest cold of the night pressing down on everything. By the ladder, Marta lies grey and still. The stove is burning low, the window dim. This is the hour the whole night turns on.",
  "B2": "You're back at the refuge, frozen through, the hardest cold of the night pressing down on everything. By the loft ladder, Marta lies grey and still. The stove is burning low, and the window has gone dim. This is the hour the whole night turns on."},
  "c": ["See to the stove and lamp.", "Vane's last offer.", "Help arrives behind you."]},
 91: {"t": {
  "A2": "You reach the stove: the flame low, the window gone dark. Out on the slope, the cold is close to taking anyone still out in it. You have to get the stove full and the lamp bright again. And you have to do it now, fast.",
  "B1": "You reach the stove: the flame low, the window gone dark. Out on the slope, the cold is close to taking anyone still out in it. You have to get the stove full and the lamp bright again — and you have to do it now, fast.",
  "B2": "You reach the stove: the flame burning low, the window gone dark against the storm. Out on the slope, the cold is close to taking anyone still out in it for good. You have to get the stove full and the lamp bright again — and you have to do it now, and fast."},
  "c": ["Get the stove full.", "Check on Marta.", "The sky greys over the ridge."]},
 92: {"t": {
  "A2": "Then help reaches you at last — more hands, more fuel, steady people who know the work. You are not alone with this now. Others are here to share the weight. It is like setting down something heavy you have carried far too long.",
  "B1": "Then help reaches you at last — more hands, more fuel, steady people who know the work. You aren't alone with this now; others are here to share the weight. It's like setting down something heavy you've carried far too long.",
  "B2": "Then help reaches you at last — more hands, more fuel, steady people who know the work of a night like this. You aren't alone with it now; others are here to share the weight. It's like setting down something heavy you have carried far too long, and far too alone."},
  "c": ["To the stove together.", "Hold the watch.", "A light out on the slope."]},
 93: {"t": {
  "A2": "Now you keep the hut warm and lit — and what you can do depends on what you carried back. With proper fuel, you have plenty to work with. Without it, you must coax every last flicker of flame. Either way, the night is far from over.",
  "B1": "Now you keep the hut warm and lit — and what you can do depends on what you carried back. With proper fuel, you've plenty to work with. Without it, you must coax every last flicker of flame. Either way, the night is far from over.",
  "B2": "Now you keep the hut warm and the window lit — and what you can do depends on what you carried back here. With proper fuel, you've plenty to work with. Without it, you must coax every last flicker of flame along. Either way, the night is far from over yet."},
  "c": ["The fuel and dry wood.", "Coax the guttering flame."]},
 94: {"t": {
  "A2": "You go to check on Marta, and her eyes open just a little. There is fear in them — then, seeing your face, a little less fear. 'You kept it going,' she whispers. 'That I did,' you tell her softly. 'Now rest.'",
  "B1": "You go to check on Marta, and her eyes open just a little. There's fear in them — then, seeing your face, a little less fear. 'You kept it going,' she whispers. 'That I did,' you tell her softly. 'Now rest.'",
  "B2": "You go down to check on Marta, and her eyes open just a little. There's fear in them — then, seeing your face in the lamplight, a little less fear. 'You kept it going,' she whispers. 'That I did,' you tell her softly. 'Now rest.'"},
  "c": ["Get the stove full.", "Break out the fuel."]},
 95: {"t": {
  "A2": "The fuel does it. You feed the stove and trim the lamp, and the flame comes up full and gold. The window burns bright against the storm. Warm light, pushing back all that cold. This, you think, is what the whole hard night was for.",
  "B1": "The fuel does it. You feed the stove and trim the lamp, and the flame comes up full and gold. The window burns bright against the storm. Warm light, pushing back all that cold. This, you think, is what the whole hard night was for.",
  "B2": "The fuel does it. You feed the stove and trim the lamp, and the flame comes up full and gold at last. The window burns bright against the driving storm. Warm light, pushing back all that cold. This, you think, is what the whole hard night was for."},
  "c": ["Hold the watch.", "Help arrives."]},
 96: {"t": {
  "A2": "You have no proper fuel to pour, so you coax what little flame there is. You shield it from the draught with your own body, feeding it scraps, breath, sheer will. It burns low and thin. It may not be enough. But you won't let it die without a fight.",
  "B1": "You've no proper fuel to pour, so you coax what little flame there is. You shield it from the draught with your own body, feeding it scraps, breath, sheer will. It burns low and thin. It may not be enough. But you won't let it die without a fight.",
  "B2": "You've no proper fuel to pour, so you coax what little flame there is. You shield it from the draught with your own body, feeding it scraps, breath, and sheer will. It burns low and thin in the grate. It may not be enough. But you will not let it die without a fight."},
  "c": ["Hold the watch.", "It may not be enough."]},
 97: {"t": {
  "A2": "The flame is low and failing, and you are afraid that shielding it alone won't be enough. You have done all you can with what you have. But it may still not hold. You need more now — more fuel, more hands, or both.",
  "B1": "The flame is low and failing, and you're afraid that shielding it alone won't be enough. You've done all you can with what you have. But it may still not hold. You need more now — more fuel, more hands, or both.",
  "B2": "The flame is low and failing, and you're afraid that shielding it alone will not be enough. You've done all you can with what you have to hand. But it may still not hold through the night. You need more now — more fuel, more hands, or both."},
  "c": ["Hold on to first light.", "Send for the roused help."]},
 98: {"t": {
  "A2": "You glance out and see it. Far out on the slope, a light flares and falls — out where no one should be, showing and hiding and showing again. It pulls at your eye. And it pulls at something deeper than that.",
  "B1": "You glance out and see it. Far out on the slope, a light flares and falls — out where no one should be, showing and hiding and showing again. It pulls at your eye. And it pulls at something deeper than that.",
  "B2": "You glance out and see it. Far out on the dark slope, a light flares and falls — out where no one should be, showing and hiding and showing again through the snow. It pulls at your eye. And it pulls at something deeper than that."},
  "c": ["See to the stove first.", "The light nags at you."]},
 99: {"t": {
  "A2": "The light out on the slope shows again — out where everyone swears no one would be. But a light means a hand to light it, and a hand means a person. A person out there, alone, in a cold like this one.",
  "B1": "The light out on the slope shows again — out where everyone swears no one would be. But a light means a hand to light it, and a hand means a person. A person out there, alone, in a cold like this one.",
  "B2": "The light out on the slope shows again — out where everyone swears no one would be tonight. But a light means a hand to light it, and a hand means a person. A person out there, alone, in a cold like this one, and in real trouble."},
  "c": ["The stove first.", "Hold the watch."]},
 100: {"t": {
  "A2": "Now comes the long hold: you keep the stove fed, keep Marta warm, and watch the cold hour by hour. It is not exciting — just steady, hard, careful work. But it is the whole job tonight, and it is yours.",
  "B1": "Now comes the long hold: you keep the stove fed, keep Marta warm, and watch the cold hour by hour. It isn't exciting — just steady, hard, careful work. But it is the whole job tonight, and it is yours.",
  "B2": "Now comes the long hold: you keep the stove fed, the lamp bright, Marta warm, and watch the cold hour by hour. It isn't exciting — just steady, hard, careful work. But it is the whole job tonight, and it is yours alone."},
  "c": ["Watch for first light.", "The light on the slope still nags.", "The night's worst hour."]},
 101: {"t": {
  "A2": "And then, at last, it turns. The wind drops a little. The sky greys at the edge of the ridge, and the first thin light comes up. The cold is losing. You have nearly held the whole night.",
  "B1": "And then, at last, it turns. The wind eases its grip a little. The sky greys at the edge of the ridge, and the first thin light comes up. The cold is losing. You have nearly held the whole night.",
  "B2": "And then, at last, it turns. The wind eases its grip a little. The sky greys at the edge of the ridge, and the first thin light comes up over it. The cold is losing. You have nearly held the whole long night."},
  "c": ["First light, and what it finds.", "Dawn over the mountain."]},
 102: {"t": {
  "A2": "This is the worst hour, the one just before the break. The cold has not eased yet; your arms ache, your eyes burn. But you can feel the night beginning to turn, somewhere under it all. Hold on a little longer.",
  "B1": "This is the worst hour, the one just before the break. The cold hasn't eased yet; your arms ache, your eyes burn. But you can feel the night beginning to turn, somewhere underneath it all. Hold on a little longer.",
  "B2": "This is the worst hour, the one just before the break. The cold hasn't eased yet; your arms ache, your eyes burn in the wind. But you can feel the night beginning to turn, somewhere underneath it all. Hold on just a little longer now."},
  "c": ["Watch for first light.", "Other lights out on the hill."]},
 103: {"t": {
  "A2": "Out on the hill you see them — torches, dark figures moving, fires low against the snow. Other people, out in the cold with you. The valley got through this night as well. You were never quite as alone as you felt.",
  "B1": "Out on the hill you see them — torches, dark figures moving, fires burning low against the snow. Other people, out in the cold with you. The valley got through this night as well. You were never quite as alone as you felt.",
  "B2": "Out on the hill you see them — torches, dark figures moving, fires burning low against the snow and the dark. Other people, out in the cold with you. The valley got through this night as well. You were never quite as alone as you felt out here."},
  "c": ["First light.", "Help coming up the hill."]},
 104: {"t": {
  "A2": "At last, help comes up the hill — the team, more hands, more fuel, real help at real speed. You lean on the door and watch it come, your legs shaking under you now. But the worst of the night is behind you.",
  "B1": "At last, help comes up the hill — the team, more hands, more fuel, real help at real speed. You lean on the door and watch it come, your legs shaking under you now. But the worst of the night is behind you.",
  "B2": "At last, help comes up the hill — the rescue team, more hands, more fuel, real help at real speed. You lean on the doorframe and watch it come through the thinning snow, your legs shaking under you now. But the worst of the night is behind you."},
  "c": ["First light.", "What the night came to."]},
 105: {"t": {
  "A2": "Dawn comes up over the mountain, the light turning grey, then pale and clean. The sun climbs the ridge, and the cold lets go its grip. The lamp still burns in the window. The worst has passed at last.",
  "B1": "Dawn comes up over the mountain, the light turning grey, then pale and clean. The sun climbs the ridge, and the cold lets go its grip. The lamp still burns in the window. The worst has passed at last.",
  "B2": "Dawn comes up over the mountain, the light turning grey, then pale and clean. The sun climbs the ridge, and the cold lets go its grip at last. The lamp still burns, steady, in the window. The worst has passed at last."},
  "c": ["First light.", "Help reaches you.", "The first bird of the morning."]},
 106: {"t": {
  "A2": "Then it comes — the first bird of the morning, calling over the snow as if there had been no storm at all. After the night you have had, it seems almost absurd. And it is beautiful, and you stop to listen.",
  "B1": "Then it comes — the first bird of the morning, calling over the snow as if there'd been no storm at all. After the night you've had, it seems almost absurd. And it is beautiful, and you stop to listen.",
  "B2": "Then it comes — the first bird of the morning, calling out over the snow as if there had been no storm at all. After the night you've had, it seems almost absurd. And it is beautiful, out here, and you stop a moment to listen."},
  "c": ["First light.", "Help reaches you."]},
 107: {"t": {
  "A2": "From the window you watch the slope, where a light lifts and falls and slowly grows. Something is coming at last, still too far off to make out. But a light means someone out there — and someone is far better than no one tonight.",
  "B1": "From the window you watch the slope, where a light lifts and falls and slowly grows. Something's coming at last, still too far off to make out. But a light means someone out there — and someone is far better than no one tonight.",
  "B2": "From the window you watch the slope, where a light lifts and falls and slowly grows larger. Something's coming at last, still too far off to make out through the snow. But a light means someone out there — and someone is far better than no one tonight."},
  "c": ["To the stove.", "Hold the watch."]},
 110: {"t": {
  "A2": "First light comes at last, and the night adds up to what it is. Whatever you did out there in the cold comes home to you now — some to be proud of, some not. Let's see, then, what it all came to.",
  "B1": "First light comes at last, and the night adds up to what it is. Whatever you did out there in the cold comes home to you now — some of it to be proud of, some of it not. Let's see, then, what it all came to.",
  "B2": "First light comes at last, and the night adds up to what it is. Whatever you did out there in the cold comes home to you now — some of it to be proud of, some of it not. Let's see, then, what it all came to in the end."},
  "c": ["The refuge held; the lamp burned.", "You answered the light, and found Rowan.", "Weigh the rest."]},
 111: {"t": {
  "A2": "The night adds up — not always with one big act, but with many small ones. What you kept, what you refused, who you went out into the cold for. It all counts in the end. It all made the night what it was.",
  "B1": "The night adds up — not always with one big act, but with many small ones. What you kept, what you refused, who you went out into the cold for. It all counts in the end. It all made the night what it was.",
  "B2": "The night adds up — not always with one big act, but with many small ones. What you kept, what you refused, who you went out into the cold for. It all counts in the end. It all made the night exactly what it was."},
  "c": ["The whole valley came through together.", "You did it clean — no con.", "Weigh the rest."]},
 112: {"t": {
  "A2": "There is more to weigh; the night held other things too. A stranger you stopped for. A coat and a lamp you gave away with an open hand. Small choices, made in the cold, when it would have been easier to pass by.",
  "B1": "There's more to weigh; the night held other things too. A stranger you stopped for. A coat and a lamp you gave away with an open hand. Small choices, made in the cold, when it would have been easier to pass by.",
  "B2": "There's more to weigh; the night held other things too. A stranger you stopped for. A coat and a lamp you gave away with an open hand. Small choices, made in the cold, when it would have been so much easier to pass by."},
  "c": ["A stranger you helped sees you home.", "You gave your own lamp away.", "Weigh the rest."]},
 113: {"t": {
  "A2": "And what does the night leave you with? Maybe not a clean win. Maybe just the fact that you went out, that you tried. When it was dark and cold and easy to bar the door, you didn't. That counts for something.",
  "B1": "And what does the night leave you with? Maybe not a clean win. Maybe just the fact that you went out, that you tried. When it was dark and cold and easy to bar the door, you didn't. That counts for something.",
  "B2": "And what does the night leave you with? Maybe not a clean win. Maybe just the plain fact that you went out, that you tried. When it was dark and cold and easy to bar the door, you didn't. That counts for something, in the end."},
  "c": ["The cold breaks at last, late.", "The valley saw you out there.", "The worst of it."]},
 114: {"t": {
  "A2": "But not every night ends well. Some choices cost more than you knew at the time; some doors, once opened, can't be shut again. This is the hard end of the night — the place where the worst of it comes home.",
  "B1": "But not every night ends well. Some choices cost more than you knew at the time; some doors, once opened, can't be shut again. This is the hard end of the night — the place where the worst of it comes home.",
  "B2": "But not every night ends well. Some choices cost more than you knew at the time; some doors, once opened, cannot be shut again. This is the hard end of the night — the place where the worst of it comes home to roost."},
  "c": ["You took Vane's deal.", "You were simply too late.", "The cold broke before real harm."]},
 # --- endings ---
 120: {"t": {
  "A2": "You kept the stove drawing and the lamp bright all night. At first light the cloud lifts over the ridge, the team climbs up, and everyone the mountain held is brought through warm. It all came through because you stayed up and would not let the light die. That is the whole of it.",
  "B1": "You kept the stove drawing and the lamp bright in the window all night. At first light the cloud lifts over the ridge, the team reaches you, and everyone the mountain held tonight is brought through warm. It all came through because you stayed up and would not let the light die. That's the whole of it.",
  "B2": "You kept the stove drawing and the lamp bright in the window all night long. At first light the cloud lifts over the ridge, the team reaches the hut, and everyone the mountain held tonight is brought through warm. It all came through because you stayed up in the cold and would not let the light die. That's the whole of it."},
  "c": []},
 121: {"t": {
  "A2": "You answered the light no one could explain. You found Rowan lost and freezing below the cornice, and got them in and warm just in time. And there was more than one life saved. Rowan is Marta's grandchild. A door shut for years is opening again, there in the grey dawn.",
  "B1": "You answered the light no one could explain. You found Rowan lost and freezing below the cornice, and got them in and warm just in time. And there was more than one life saved: Rowan is Marta's grandchild. A door shut for years is opening again, there in the grey dawn.",
  "B2": "You answered the light no one could explain. You found Rowan lost and freezing below the cornice, and got them in and warm just in time. And there was more than one life saved tonight: Rowan is Marta's grandchild. A door shut for years is quietly opening again, there in the grey light of the dawn."},
  "c": []},
 122: {"t": {
  "A2": "There was no single brave act — there was something better. You turned a sleeping valley into people with torches on the hill, and together they brought the whole night through. No one was left alone in it. That, in the end, is what a valley can be.",
  "B1": "There was no single brave act — there was something better than that. You turned a sleeping valley into people with torches on the hill, and together they brought the whole night through. No one was left alone in it. That, in the end, is what a valley can be.",
  "B2": "There was no single brave act — there was something better than that. You turned a sleeping valley into people with torches on the hill, and together they brought the whole long night through. No one was left alone in it. That, in the end, is what a valley can be for one another."},
  "c": []},
 123: {"t": {
  "A2": "You refused the con — saw Vane's trick for what it was and turned your back on it. You kept your head, and held the refuge by decent, honest means. It wasn't a perfect night; you didn't save everyone. But you did it clean, and clean is enough.",
  "B1": "You refused the con — saw Vane's trick for what it was and turned your back on it. You kept your head, and held the refuge by decent, honest means. It wasn't a perfect night; you didn't bring everyone through. But you did it clean, and clean is enough.",
  "B2": "You refused the con — saw Vane's trick for exactly what it was and turned your back on it. You kept your head, and held the refuge by decent, honest means. It wasn't a perfect night; you didn't bring quite everyone through. But you did it clean, and clean, tonight, is enough."},
  "c": []},
 124: {"t": {
  "A2": "You fell short of holding it all. But the walker you stopped for earlier comes back now. They help you keep the hut and get Marta warm. It is not the full win. But a kindness, it turns out, doesn't stay where you leave it. It comes back around.",
  "B1": "You fell short of holding it all. But the walker you stopped for earlier comes back now. They help you keep the hut and get Marta warm. It isn't the full win. But a kindness, it turns out, doesn't stay where you leave it. It comes back around.",
  "B2": "You fell short of holding it all. But the walker you stopped for earlier comes back now, when it counts. They help you keep the hut going and get Marta warm. It isn't the full win. But a kindness, it turns out, doesn't stay where you leave it — it comes back around."},
  "c": []},
 125: {"t": {
  "A2": "You gave your own coat and fuel away to those with less, and you end the night cold yourself. You didn't save everything. But you are not alone, and neither is anyone you met out there. Something in the valley has quietly shifted. It's a start, not a save.",
  "B1": "You gave your own coat and fuel away to those with less, and you end the night cold yourself. You didn't save everything. But you're not alone, and neither is anyone you met out there. Something in the valley has quietly shifted. It's a start, not a save.",
  "B2": "You gave your own coat and fuel away to those with less, and you end the night cold yourself. You didn't save everything tonight. But you're not alone, and neither is anyone you met out there in the dark. Something in the valley has quietly shifted. It's a start, not a save."},
  "c": []},
 126: {"t": {
  "A2": "You scrape through the worst of it. The wind drops at last, and a thin dawn brings the team up the hill. It is no triumph, and no one will sing about it. But you got through the night — and in the end, that is a relief all of its own.",
  "B1": "You scrape through the worst of it. The wind drops at last, and a thin dawn brings the team up the hill. It's no triumph, and no one will sing about it. But you got through the night — and in the end, that is a relief all of its own.",
  "B2": "You scrape through the worst of it. The wind drops at last, and a thin grey dawn brings the team up the hill. It's no triumph, and no one will sing about it. But you got through the night — and in the end, that is a relief all of its own."},
  "c": []},
 127: {"t": {
  "A2": "You didn't bring everyone through. But the valley saw you out on the hill when others barred their doors — saw you try, on the worst night of the year. From tonight, you are someone this place knows. And that is not nothing.",
  "B1": "You didn't bring everyone through. But the valley saw you out on the hill when others barred their doors — saw you try, on the worst night of the year. From tonight, you're someone this place knows. And that is not nothing.",
  "B2": "You didn't bring everyone through tonight. But the valley saw you out on the hill when others barred their doors — saw you try, on the worst night of the year. From tonight, you're someone this place knows. And that, in the end, is not nothing."},
  "c": []},
 128: {"t": {
  "A2": "You took Vane's deal, and by morning the refuge is condemned, no longer anyone's to keep. The cold did the rest. The money in your pocket is cold, and the window is dark. You won't soon forget how you came to earn it.",
  "B1": "You took Vane's deal, and by morning the refuge is condemned — no longer anyone's to keep. The cold did the rest. The money in your pocket is cold, and the window is dark. You won't soon forget how you came to earn it.",
  "B2": "You took Vane's deal, and by morning the refuge is condemned, no longer anyone's to keep. The cold did the rest. The money in your pocket is cold, and the window is dark. You will not soon forget how you came to earn it."},
  "c": []},
 129: {"t": {
  "A2": "The cornice was a trap, just as Doune warned. It broke under you in the dark, and it took the whole night. You drag yourself out, hurt and frozen, and reach the far side far too late. The cornice cost you everything the short cut promised to save.",
  "B1": "The cornice was a trap, just as Doune warned. It broke under you in the dark, and it took the whole night. You drag yourself out, hurt and frozen, and reach the far side far too late. The cornice cost you everything the short cut had promised to save.",
  "B2": "The cornice was a trap, just as Doune warned you it was. It broke under you in the dark, and it took the whole night. You drag yourself out, hurt and frozen, and reach the far side far too late. The cornice cost you everything the short cut had promised to save."},
  "c": []},
 130: {"t": {
  "A2": "You spent the night on the wrong things, and the stove went dark too long. By dawn the hut is cold, and whoever was out on the slope was not found in time. You did go out into the cold. But you didn't keep the light when it truly counted.",
  "B1": "You spent the night on the wrong things, and the stove went dark too long. By dawn the hut is cold, and whoever was out on the slope was not found in time. You did go out into the cold. But you didn't keep the light when it truly counted.",
  "B2": "You spent the night on the wrong things, and the stove went dark too long. By dawn the hut is cold, and whoever was out on the slope was not found in time. You did go out into the cold tonight. But you didn't keep the light when it truly counted."},
  "c": []},
 131: {"t": {
  "A2": "In the end, you stayed inside, where it was warm and safe. You told yourself the storm was too hard, that it wasn't your job, that help would come at dawn. All of it was true. And all night, out on the slope, the window stayed dark. Nothing bad happened to you. You'll think about that for a long, long time.",
  "B1": "In the end, you stayed inside, where it was warm and safe. You told yourself the storm was too hard, that it wasn't your job, that help would come at dawn. All of that was true. And all night, out on the slope, the window stayed dark. Nothing bad happened to you. You'll think about that for a long, long time.",
  "B2": "In the end, you stayed inside, where it was warm and safe. You told yourself the storm was too hard, that it wasn't your job, that help would come at dawn. All of that was true. And all night, out on the slope, the window stayed dark. Nothing bad happened to you. You will think about that for a long, long time."},
  "c": []},
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
    print(f"batch E: wrote prose for {len(D)} nodes")


if __name__ == "__main__":
    main()
