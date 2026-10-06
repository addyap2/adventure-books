#!/usr/bin/env python3
"""Phase 3 prose for The Orchard — batch 5 (nodes 97-114 + the 12 endings 120-131).
Completes Phase 3. Run then validate; whole book should be band-clean with no stubs."""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
EP = os.path.join(ROOT, "content", "episode-06.json")
book = json.load(open(EP, encoding="utf-8"))
nodes = {n["id"]: n for n in book["nodes"]}

P = {
 97: (
  "The flame is low and failing. You are afraid that shielding it won't be enough. You have done all you can with what you have. But it may not hold. You need more — oil, or hands, or both.",
  "The flame is low and failing, and you're afraid that shielding it alone won't be enough. You've done all you can with what you have. But it may still not hold. You need more now — more oil, more hands, or both.",
  "The flame is low and failing, and you are afraid that shielding it with your body alone will not be enough. You have done everything you can with what little you have. But it may still not hold until dawn. You need more now — more oil, more hands, or both, and quickly."),
 98: (
  "You glance out and see it. Far among the far trees, a light flares and falls. It is out where no one should be. It shows, hides, and shows again. It pulls at your eye, and at something deeper.",
  "You glance out and see it. Far among the far trees, a light flares and falls — out where no one should be, showing and hiding and showing again. It pulls at your eye. And it pulls at something deeper than that.",
  "You glance out across the rows and see it. Far among the far trees, a light flares and falls and flares again — out where no one should be on a night like this, showing and hiding in the dark. It pulls at your eye. And it pulls at something deeper and harder to name."),
 99: (
  "The light out in the trees shows again. It is where everyone says no one would be. But a light means a hand to make it. And a hand means a person. A person out there, in this cold.",
  "The light out among the trees shows again — out where everyone swears no one would be. But a light means a hand to light it, and a hand means a person. A person out there, alone, in a cold like this one.",
  "The light out among the trees shows again — out where everyone swears no one would be tonight. But a light means a hand to make it, and a hand means a person. A person out there, alone, in a killing cold like this one. You can't quite let it go."),
 100: (
  "Now comes the long hold. You keep the fires fed. You keep Edith warm. You watch the cold, hour by hour. It is not exciting. It is just steady, hard, careful work. And it is the whole job tonight.",
  "Now comes the long hold: you keep the fires fed, keep Edith warm, and watch the cold hour by hour. It isn't exciting — just steady, hard, careful work. But it is the whole job tonight, and it is yours.",
  "Now comes the long hold: you keep the fires fed, keep Edith warm and breathing, and watch the cold creep and retreat hour by hour. It isn't exciting work — just steady, hard, careful work, done over and over. But it is the whole job tonight. And tonight it is yours alone."),
 101: (
  "And then, at last, it turns. The cold eases a little. The sky greys at the edge of the ridge. The first thin light comes. The frost is losing its grip. You have nearly held the night.",
  "And then, at last, it turns. The cold eases its grip a little. The sky greys at the edge of the ridge, and the first thin light comes up. The frost is losing. You have nearly held the whole night.",
  "And then, at last, it turns. The cold eases its hard grip a little. The sky greys at the edge of the ridge, and the first thin light of the day comes creeping up. The frost is losing its hold at last. You have very nearly held the whole long night."),
 102: (
  "This is the worst hour — the one just before the break. The cold has not eased yet. Your arms ache. Your eyes burn. But you can feel the night starting to turn. Hold on a little longer.",
  "This is the worst hour, the one just before the break. The cold hasn't eased yet; your arms ache, your eyes burn. But you can feel the night beginning to turn, somewhere underneath it all. Hold on a little longer.",
  "This is the worst hour of all, the one just before the break. The cold has not eased yet; your arms ache from the pots, your eyes burn in the dark. But you can feel the night beginning to turn, somewhere underneath the cold. Just hold on a little longer now."),
 103: (
  "Along the rows you see them. Lanterns, dark figures moving, fires burning low. Other people, out in the cold too. The village got through this night as well. You were never quite alone in it.",
  "Along the rows you see them — lanterns, dark figures moving, fires burning low against the frost. Other people, out in the cold with you. The village got through this night as well. You were never quite as alone as you felt.",
  "Along the rows you see them now — lanterns, dark figures moving slowly, fires burning low against the frost. Other people, out in the cold all night, same as you. The whole village got through this night as well. And you were never quite as alone in it as you felt."),
 104: (
  "At last, help comes up the lane. A truck, more hands, more oil — real help, at real speed. You lean on a tree and watch it come. Your legs are shaking now. But the worst is behind you.",
  "At last, help comes up the lane — a truck, more hands, more oil, real help at real speed. You lean on a tree and watch it come, your legs shaking under you now. But the worst of the night is behind you.",
  "At last, help comes up the lane — a truck, more hands, more oil, real help arriving at real speed. You lean on a tree and watch it come on, your legs shaking under you now that you can let them. But the worst of the night is well behind you now."),
 105: (
  "Dawn comes up over the orchard. The light turns grey, then pale and clean. The sun climbs the ridge, and the frost lets go. The blossom is still there. The worst has passed at last.",
  "Dawn comes up over the orchard, the light turning grey, then pale and clean. The sun climbs the ridge, and the frost lets go its grip. The blossom is still there on the trees. The worst has passed at last.",
  "Dawn comes up over the orchard, the light turning grey, then pale, then clean and gold. The sun climbs slowly over the ridge, and the frost lets go its grip tree by tree. The blossom is still there, still whole. The worst of it has passed at last. You can hardly believe you made it through."),
 106: (
  "Then it comes — the first bird of the morning. It sings over the trees as if there had been no frost at all. After the night you have had, it seems almost absurd. And it is beautiful.",
  "Then it comes — the first bird of the morning, singing over the trees as if there'd been no frost at all. After the night you've had, it seems almost absurd. And it is beautiful, and you stop to listen.",
  "Then it comes — the first bird of the morning, singing out over the trees as if there had been no frost, no fear, no long cold night at all. After the night you have had, it seems almost absurd. And it is beautiful, and you stop a moment just to listen."),
 107: (
  "From the orchard you watch the far trees. A light lifts and falls out there, and slowly grows. Something is coming at last, too far yet to make out. But a light means someone. And someone is better than no one.",
  "From the orchard you watch the far trees, where a light lifts and falls and slowly grows. Something's coming at last, still too far off to make out. But a light means someone out there — and someone is far better than no one tonight.",
  "From the orchard you watch the far trees, where a light lifts and falls in the dark and slowly, slowly grows. Something is coming at last, still too far off to make out clearly. But a light means a hand, and a hand means someone — and someone is far better than no one, on a night like this."),
 110: (
  "First light comes at last. Now the night adds up to what it is. Whatever you did out there, in the cold, comes home now. Some of it to be proud of. Some of it not. Let's see what it came to.",
  "First light comes at last, and the night adds up to what it is. Whatever you did out there in the cold comes home to you now — some of it to be proud of, some of it not. Let's see, then, what it all came to.",
  "First light comes at last, and the night adds up to exactly what it is. Whatever you did out there in the cold and the dark comes home to you now — some of it to be proud of, some of it not so much. Let's see, then, what the whole long night finally came to."),
 111: (
  "The night adds up — not with one big act, but with many small ones. What you kept. What you refused. Who you went out for. It all counts in the end. It all made the night what it was.",
  "The night adds up — not always with one big act, but with many small ones. What you kept, what you refused, who you went out into the cold for. It all counts in the end. It all made the night what it was.",
  "The night adds up — not with one single grand act, but with many small ones laid end to end. What you kept going, what you refused, who you went out into the cold for. It all counts in the end. And it all made the night exactly what it was."),
 112: (
  "There is more to weigh. The night held other things too. A stranger you stopped for. A coat and a lamp you gave away with an open hand. Small choices, made in the cold, when it was easier to pass by.",
  "There's more to weigh; the night held other things too. A stranger you stopped for. A coat and a lamp you gave away with an open hand. Small choices, made in the cold, when it would have been easier to pass by.",
  "There is more to weigh; the night held other things too. A stranger you stopped for when you had no time. A coat and a lamp you gave away with an open hand. Small choices, made out in the cold, when it would have been far easier to pass them by."),
 113: (
  "And what does the night leave you? Maybe not a clean win. Maybe just this: that you went out, that you tried. When it was dark and cold and easy to stay in, you didn't. That counts for something.",
  "And what does the night leave you with? Maybe not a clean win. Maybe just the fact that you went out, that you tried. When it was dark and cold and easy to bar the door, you didn't. That counts for something.",
  "And what does the night leave you with, in the end? Maybe not a clean win at all. Maybe just the plain fact that you went out, that you tried. When it was dark and cold and so easy to bar the door and stay in, you didn't. And that counts for something."),
 114: (
  "But not every night ends well. Some choices cost more than you knew. Some doors, once opened, can't be shut again. This is the hard end of the night. This is where the worst comes home.",
  "But not every night ends well. Some choices cost more than you knew at the time; some doors, once opened, can't be shut again. This is the hard end of the night — the place where the worst of it comes home.",
  "But not every night ends well. Some choices cost far more than you knew at the time; some doors, once opened, cannot be shut again. This is the hard end of the night — the place where the worst of what you did, or didn't do, comes home to you. Some of it cannot be undone now."),
 # ---- endings ----
 120: (
  "You kept the fires burning down the rows all night. At first light, the sun comes over the ridge. The frost lifts, and the blossom comes through. A whole year's fruit is safe. And it is safe because you stayed out in the cold.",
  "You kept the fires burning down the rows all night. At first light the sun comes over the ridge, the frost lifts, and the blossom — a whole year's fruit — comes through. It all came through because you stayed out in the cold and would not let the fires die. That's the whole of it.",
  "You kept the fires burning down the rows all night long. At first light the sun comes up over the ridge, the frost lifts its grip, and the blossom — and with it a whole year's fruit — comes through alive. It all came through because you stayed out in the cold and would not let the fires die. That is the whole of it, and it is enough."),
 121: (
  "You answered the light no one could explain. You found Wren, lost and cold among the far rows, and got them warm in time. And there was more. Wren is Edith's grandchild. A door shut for years opens again, at dawn.",
  "You answered the light no one could explain. You found Wren lost and cold among the far rows, and got them warm just in time. And there was more than one life saved. Wren is Edith's grandchild. A door shut for years is opening again, there in the grey dawn.",
  "You answered the light no one could explain, out among the far trees. You found Wren lost and cold among the rows, and got them warm just in time. And there was more than one life saved out there. Wren is Edith's own grandchild, estranged for years. And a door that both sides thought shut for good is quietly opening again, there in the grey light of dawn."),
 122: (
  "There was no single brave act. There was something better. You turned a sleeping village into people with torches down every row. Together, they brought the night through. No one was left alone in it. That is what a village can be.",
  "There was no single brave act — there was something better than that. You turned a sleeping village into people with torches down every row, and together they brought the whole night through. No one was left alone in it. That, in the end, is what a village can be.",
  "There was no single brave act to point to — there was something better than that. You turned a sleeping, frightened village into people with torches down every row, and together, all of you brought the whole night through. No one was left alone in it. That, in the end, is what a village can be for."),
 123: (
  "You refused the con. You saw the buyer's trick and turned your back on it. You kept your head, and saved what you could by decent means. It was not perfect. But it was clean, and honest, and enough.",
  "You refused the con — saw the buyer's trick for what it was and turned your back on it. You kept your head, and saved what you could by decent, honest means. It wasn't a perfect night; you didn't save everyone. But you did it clean, and clean is enough.",
  "You refused the con — you saw the buyer's trick for exactly what it was and turned your back on it. You kept your head through the worst of it, and saved what you could by decent, honest means. It was not a perfect night, and you did not save everyone. But you did it clean. And clean, in the end, is enough."),
 124: (
  "You fell short of the whole orchard. But the neighbour you stopped for comes back now. They help you save the near rows, and they get Edith warm. It is not the full win. But a kindness, it turns out, comes back around.",
  "You fell short of the whole orchard. But the neighbour you stopped for earlier comes back now. They help you save the near rows and get Edith warm. It isn't the full win. But a kindness, it turns out, doesn't stay where you leave it. It comes back around.",
  "You fell short of saving the whole orchard — but the neighbour you stopped for earlier comes back now, when it matters, and helps you save the near rows and get Edith warm. It is not the full win you wanted. But a kindness, it turns out, does not stay where you leave it. It comes back around."),
 125: (
  "You gave your own coat and fuel away. Now you end the night cold yourself. You did not save everything. But you are not alone, and nor is anyone you met. Something in the village has shifted. It is a start, not a save.",
  "You gave your own coat and fuel away to those with less, and you end the night cold yourself. You didn't save everything. But you're not alone, and neither is anyone you met out there. Something in the village has quietly shifted. It's a start, not a save.",
  "You gave your own coat and fuel away to people who had less, and you end the night cold and worn through yourself. You did not save everything. But you are not alone, and neither is anyone you met out there in the dark. Something in the village has quietly shifted tonight. It is a start, not a save — and starts matter."),
 126: (
  "You scrape through the worst of it. The cold turns at last, and a thin dawn saves part of the blossom. It is not a triumph. No one will sing about it. But you got through the night. And that is a relief all its own.",
  "You scrape through the worst of it. The still air turns at last, and a thin dawn saves part of the blossom. It's no triumph, and no one will sing about it. But you got through the night — and in the end, that is a relief all of its own.",
  "You scrape through the worst of it, only just. The still air turns at last, and a thin, grudging dawn saves part of the blossom. It is no triumph, and no one will sing about it. But you got through the night — and in the end, that is a relief all of its own."),
 127: (
  "You didn't save it all. But the village saw you out among the trees when others slept. They saw you try, on the worst night of the year. From tonight, you are someone this place knows. That is not nothing.",
  "You didn't save it all. But the village saw you out among the trees when others stayed in bed — saw you try, on the worst night of the year. From tonight, you're someone this place knows. And that is not nothing.",
  "You didn't manage to save it all, far from it. But the whole village saw you out among the trees when others stayed warm in bed — saw you try, on the worst night of the year. From tonight, you are someone this place knows and nods to. And that, in the end, is not nothing at all."),
 128: (
  "You took the buyer's deal. By morning, the orchard is no longer Edith's to save. The frost did the rest. The cheque in your hand is cold. So is the ground outside. You will not forget how you earned it.",
  "You took the buyer's deal, and by morning the orchard is no longer Edith's to save. The frost did the rest. The cheque in your pocket is cold, and so is the ground by morning. You won't soon forget how you came to earn it.",
  "You took the buyer's deal, and by morning the orchard is no longer Edith's to save — it is his, in all but the signing. The frost did the rest. The cheque in your pocket is cold, and so is the hard ground by morning. You will not soon forget how you came to earn it."),
 129: (
  "The frozen pond was a trap. You went through it in the dark, and it took the night. You dragged yourself out, frozen and shaking. You reach the far rows far too late. The ice cost you everything the short cut promised.",
  "The frozen pond was a trap, just as Jack Hale warned. You went through it in the dark, and it took the whole night. You drag yourself out, frozen and shaking, and reach the far rows far too late. The ice cost you everything the short cut promised to save.",
  "The frozen pond was a trap, exactly as Jack Hale warned you it would be. You went through it in the dark, and it took the whole night with it. You drag yourself out, frozen and shaking and broken, and reach the far rows far too late to matter. The ice cost you everything the short cut ever promised to save."),
 130: (
  "You spent the night on the wrong things. The fires went out too long. By dawn, the blossom is black on every tree. The year's fruit is gone. You went out into the cold. But you didn't hold the fires when it counted.",
  "You spent the night on the wrong things, and the fires went dark too long. By dawn, the blossom is black on every tree, and the year's fruit is lost. You did go out into the cold. But you didn't hold the fires when it truly counted.",
  "You spent the night on the wrong things, and the fires went dark too long to matter. By dawn, the blossom is black on every tree, and the whole year's fruit is lost with it. You did go out into the cold, and you did try. But you did not hold the fires when it truly counted."),
 131: (
  "In the end, you stayed inside, where it was warm and safe. You told yourself it wasn't your job. That help would come at dawn. All of it was true. And all night, the fires stayed dark. Nothing bad happened to you. You will think about that for a long time.",
  "In the end, you stayed inside, where it was warm and safe. You told yourself the frost was too hard, that it wasn't your job, that help would come at dawn. All of that was true. And all night, out in the rows, the fires stayed dark. Nothing bad happened to you. You'll think about that for a long, long time.",
  "In the end, you stayed inside, where it was warm and dry and safe. You told yourself the frost was too hard, that it wasn't really your job, that help would surely come at dawn. All of that was true. And all night, out in the dark rows, the fires stayed cold. Nothing bad happened to you at all. You will think about that for a long, long time."),
}

C = {
 97: ["Hold on to first light.", "Send for the rallied help."],
 98: ["See to the fires first.", "The light nags at you."],
 99: ["The fires first.", "Hold the watch."],
 100: ["Watch for first light.", "The light in the trees still nags.", "The night's worst hour."],
 101: ["First light, and what it finds.", "Dawn over the orchard."],
 102: ["Watch for first light.", "Other lights along the rows."],
 103: ["First light.", "Help coming up the lane."],
 104: ["First light.", "What the night came to."],
 105: ["First light.", "Help reaches you.", "The first bird of the morning."],
 106: ["First light.", "Help reaches you."],
 107: ["To the fires.", "Hold the watch."],
 110: ["The blossom held; the fires burned.", "You answered the light, and found Wren.", "Weigh the rest."],
 111: ["The whole village came through together.", "You did it clean — no con.", "Weigh the rest."],
 112: ["A stranger you helped sees you home.", "You gave your own lamp away.", "Weigh the rest."],
 113: ["The frost breaks at last, late.", "The village saw you out there.", "The worst of it."],
 114: ["You took the buyer's deal.", "You were simply too late.", "The frost broke before real harm."],
}

LV = ("A2", "B1", "B2")
for nid, (a2, b1, b2) in P.items():
    n = nodes[nid]
    n["text"] = {"A2": a2, "B1": b1, "B2": b2}
    if nid in C:
        for j, ct in enumerate(C[nid]):
            n["choices"][j]["text"] = {lv: ct for lv in LV}
json.dump(book, open(EP, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("Patched %d nodes (batch 5, incl. 12 endings)" % len(P))
