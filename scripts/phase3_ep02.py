#!/usr/bin/env python3
"""Phase 3: pour leveled prose into the episode-02 skeleton.

Holds the A2/B1/B2 prose for each node (and each choice, in the skeleton's choice
order) in PROSE, then writes it onto content/episode-02.json in place. Nodes absent
from PROSE keep their stub text, so this grows batch by batch (Act I, II, III, endings),
re-running after each with the validator to keep every level inside its CEFR band.

Run: python3 scripts/phase3_ep02.py
"""
import json, os, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BOOK = os.path.join(ROOT, "content", "episode-02.json")


def t(a2, b1, b2):
    return {"A2": a2, "B1": b1, "B2": b2}


# node id -> {"text": t(...), "choices": [ t(...), ... ]}  (choices in skeleton order)
PROSE = {}

def P(nid, text, choices):
    PROSE[nid] = {"text": text, "choices": choices}


# ============================ ACT I — MORNING ==============================

P(1,
  t("You wake early in the cheap hotel. There is a note under the door. The room is booked from tonight. You have to leave. In your pocket there is one week's pay. It is enough for a deposit and almost nothing more. You have the job now. You do not have a home.",
    "You wake early in the cheap hotel by the yellow agency sign. There is a note under your door: the room is booked from tonight, so you have to be out. In your pocket is one week's pay from Kessler and Rowe — enough for a deposit and almost nothing else. You have the job. What you do not have, yet, is anywhere to live.",
    "You wake early in the cheap hotel by the yellow agency sign, the one you learned to distrust on your first night here. A note has been pushed under your door: the room is booked from tonight, and there is someone after you, so you have to be out by evening. In your pocket is one week's pay from Kessler and Rowe — precisely enough for a deposit and almost nothing else. You have the job, which still surprises you. What you do not have, yet, is anywhere in this city to call your own."),
  [t("Ask the hotel man where to look.",
     "Ask the hotel man where a stranger looks for a room.",
     "Ask the hotel man where a stranger is meant to look for a room."),
   t("Go to the kiosk for a newspaper.",
     "Go to the corner kiosk for the local paper.",
     "Go to the corner kiosk and buy the local paper."),
   t("Look at rooms on your phone.",
     "Check the room listings on your phone.",
     "Check the room listings on your phone instead.")])

P(2,
  t("You ask the hotel man. He once let you sit by the radiator all night, so he is kind. He tells you the truth. \"Stay away from the flashy agents,\" he says. \"They take your money. Try the paper. Or try the canal side. The rooms there are cheap and real.\"",
    "You ask the hotel man, the one who let you sit by the radiator on a cold night once. He is honest with you. \"Keep away from the flashy agents,\" he says. \"They'll take your deposit and give you nothing. Try the paper, or try the canal side — the rooms down there are cheap and they're real.\"",
    "You ask the hotel man — the one who, on your first night, let you sit by the lobby radiator until it was light. He is honest with you, which is not something this city hands out freely. \"Keep away from the flashy agents,\" he says. \"They'll take your deposit and give you nothing back. Try the paper, or try the canal side; the rooms down there are cheap, and, more to the point, they're real.\""),
  [t("First count exactly what you have.",
     "Count exactly what you have before you spend a coin.",
     "Count exactly what you have before you spend a single coin."),
   t("Go to the kiosk for the paper.",
     "Head to the kiosk for the paper he means.",
     "Head to the kiosk for the paper he's talking about."),
   t("Look at your phone anyway.",
     "Look at your phone anyway.",
     "Look at your phone anyway, against his advice.")])

P(3,
  t("The kiosk woman is at her corner. You know her from your first night. She gives you the local paper. She circles two rooms with her pen. Then she sees a third advert — it says KEYS TODAY — and draws a hard line through it. \"Not that one,\" she says.",
    "The kiosk woman from your first night is at her corner again. She hands you the local paper and circles two rooms with her pen. Then her eye falls on a third advert — KEYS TODAY, in big letters — and she draws a firm line straight through it. \"Not that one,\" she says.",
    "The kiosk woman from your first night is at her corner again, as though she never leaves it. She hands you the local paper and circles two rooms with a stub of pencil. Then her eye catches a third advert — KEYS TODAY, set in the sort of big, warm letters that ought to make you suspicious — and she draws a firm line straight through it. \"Not that one,\" she says, and does not explain."),
  [t("Read the two rooms she circled.",
     "Read the two rooms she circled.",
     "Read the two rooms she's circled."),
   t("Dania from work is here too.",
     "Dania from the firm is here too, also looking.",
     "Dania from the firm is here too, also looking for a room."),
   t("Walk to the canal side early.",
     "Walk to the canal side before the crowds.",
     "Walk to the canal side to look before the crowds arrive.")])

P(4,
  t("Your phone shows a bright, cheap room. The photos are beautiful. They are almost too good for the price. Under them there is a name: Mr Vann. The advert says: pay a deposit today to hold the room, and get the keys today. It feels quick. It feels easy.",
    "Your phone shows a bright, cheap room — photos far too good for the price. Below them is a name, Mr Vann, and a line that reads: deposit today to hold it, keys today. It's quick, it's easy, and something about how quick and easy it is makes you slow down.",
    "Your phone shows a bright, cheap room, the photos far too good for the asking price. Below them sits a name — Mr Vann — and a line designed to move you fast: deposit today to hold it, keys today. It is quick, it is easy, and the very speed of it is the thing that makes some careful part of you slow right down."),
  [t("Go to Vann's office now.",
     "Go to Vann's office and see the room.",
     "Go to Vann's office and ask to see the room."),
   t("Look Vann up first.",
     "Look Vann up before you go anywhere.",
     "Look Vann up properly before you go anywhere near him."),
   t("You know this trick. Ignore it.",
     "You have met this trick before. Ignore it.",
     "You have met this exact trick before. Ignore it.")])

P(5,
  t("Dania is a new worker at Kessler and Rowe, like you. She is also new to the city. She also has no room yet. She looks tired but she smiles. \"Two of us can look at more rooms than one,\" she says. \"And it is nicer than looking alone.\"",
    "Dania started at Kessler and Rowe the same week you did. She's as new to the city as you are, and just as roomless. She looks tired, but she smiles. \"Two of us can cover more rooms than one,\" she says, \"and it beats looking on your own all day.\"",
    "Dania started at Kessler and Rowe the same week you did — as new to the city as you are, and every bit as roomless. She looks tired in the grey morning light, but she smiles at you. \"Two of us can cover twice the rooms,\" she says, \"and, honestly, it beats trudging round on your own all day.\""),
  [t("Look together. Two sets of eyes.",
     "Agree to look together — two sets of eyes.",
     "Agree to look together — two sets of eyes are better than one."),
   t("Wish her luck. Look alone.",
     "Wish her luck and look on your own.",
     "Wish her luck and look on your own instead."),
   t("Check your phone first.",
     "Check your phone listings first.",
     "Check your phone listings first, before deciding.")])

P(6,
  t("The canal is grey in the morning light. There is an old rope-works with dark windows. Washing hangs on a line above the water. The air smells of tar and cold water. It is quiet here. It is poor, but it is honest. You could live in a street like this.",
    "The canal lies grey in the morning light. An old rope-works stands with dark windows; washing hangs on a line above the water; the air is thick with tar and cold. It's quiet down here, and poor, but it feels honest. This is the kind of street where a room might actually be what the advert says.",
    "The canal lies grey in the early light. An old rope-works stands with dark, patient windows; washing hangs on a line above the water; the air is heavy with tar and cold. It's quiet down here, and plainly poor, but it has an honest feel. This is the kind of street where a room might turn out to be exactly what the advert claims — no more, and no less."),
  [t("Decide how to spend your money.",
     "Decide how to spend the day and the fare money.",
     "Decide how to spend the day, and the fare money, before you move."),
   t("A delivery man knows every door.",
     "A delivery man here seems to know every door.",
     "A delivery man here looks as though he knows every door on the street.")])

P(7,
  t("The kiosk woman circled two rooms. One is a room by the canal. A Mrs Halloran owns it. You can see it at noon. The other is a bedsit. It is cheap, and you can see it now. Two rooms, two roads across the city. You cannot see both at the same time.",
    "She circled two rooms. One is by the canal — a Mrs Halloran, viewing at noon. The other is a bedsit, cheaper still, and you could see it right now. Two rooms, two directions across the city, and only one of you to walk them.",
    "She has circled two rooms. One sits by the canal — a Mrs Halloran, viewing at noon — and the other is a bedsit, cheaper still, that you could go and see this minute. Two rooms, two directions across a city that doesn't know you, and only one pair of legs to walk them on."),
  [t("See the cheap bedsit now.",
     "The bedsit — see it now while it's going.",
     "The bedsit — go and see it now, while it's still going."),
   t("Wait for the canal room at noon.",
     "Hold out for the canal room at noon.",
     "Hold out for the canal room at noon instead."),
   t("A third advert: a room to share.",
     "A third advert: a room to share, very cheap.",
     "A third advert: a room to share, and very cheap."),
   t("Work out your money and route first.",
     "Work out your money and your route first.",
     "Work out your money and your route across the city first.")])

P(8,
  t("You stand at the door of Vann's office. Inside there is a queue of people. On the wall is a board of glossy rooms, all bright and cheap. Everyone waits. Everyone hopes. A room like the photos would change your whole week. You put your hand on the door.",
    "You stand at the door of Vann's office. Inside, a queue of tired people waits under a board of glossy rooms, every one of them bright and cheap. They're all hoping. A room like those photos would change your whole week, and you know it, and that is exactly the problem.",
    "You stand at the door of Vann's office. Inside, a queue of tired people waits beneath a board of glossy rooms — every one of them bright, cheap, and just out of reach. They are all hoping, quietly and hard. A room like the ones in those photographs would change your entire week, and you know it, and knowing it is precisely the hook the whole place is built on."),
  [t("Go in and hear the pitch.",
     "Step inside and hear the pitch.",
     "Step inside and hear the pitch out."),
   t("Wait on the step.",
     "Hesitate on the step.",
     "Hesitate on the step a moment longer.")])

P(9,
  t("You look Vann up first. A man comes out of the office. He is angry. \"I paid him and I never got my keys,\" he says quietly. On your phone, the reviews are bad. Star after star, all one star, all the same story: money in, nothing out.",
    "You look Vann up before you commit. A man leaving the office mutters, almost to himself, that he paid and never got his keys. On your phone the reviews are a wall of single stars, all telling the same story: money handed over, nothing given back.",
    "You look Vann up before you commit to anything. A man on his way out mutters, half to himself and half to you, that he paid his deposit and never once saw a key. On your phone the reviews are a solid wall of single stars, every one of them the same short story told again: money handed over, and nothing whatever given back."),
  [t("Ask a few more people.",
     "Ask around a little more.",
     "Ask around a little more before deciding."),
   t("Decide it's a trap. Walk away.",
     "Decide it's a trap and walk away.",
     "Decide it's plainly a trap and walk away."),
   t("Risk it anyway. The room looked good.",
     "The room looked so good — risk it anyway.",
     "The room looked so good — risk it anyway, against the evidence.")])

P(10,
  t("You sit on the bed and lay the money out. One week's pay. A deposit will take most of it. There will be almost nothing left for food, or for the bus, or for a mistake. You count it twice. One wrong move today, and you will have no room and no way home.",
    "You sit on the bed and lay the money out in a row. One week's pay; a deposit will swallow most of it, leaving almost nothing for food or fares or errors. You count it twice, the way you count things that frighten you. One wrong move today and you'll have neither a room nor the fare to keep looking.",
    "You sit on the bed and lay the money out in a neat row, as if seeing it clearly might make it more. One week's pay; a deposit will swallow most of it and leave almost nothing for food, or fares, or the kind of mistake this city seems to specialise in. You count it twice, the way you count things that frighten you. One wrong move today and you'll be left with neither a room nor the fare to go on looking for one."),
  [t("Go out and look, carefully.",
     "Go out and look, carefully.",
     "Go out and look, carefully, now that you know the stakes."),
   t("Get the paper first.",
     "Get the paper first.",
     "Get the paper first, then set out.")])

P(11,
  t("You know this game now. You learned it on your first night, from the job agency. Bright, cheap, and today — that is the trap. You put the phone in your pocket. You will trust the paper, your feet, and the people who help for free.",
    "You know this game now; you learned it on your first night, from the job agency with the yellow sign. Bright, cheap, and 'today' is always the trap. You put the phone away and decide to trust the paper, your own feet, and the few people in this city who help for nothing.",
    "You know this game now — you learned it on your first night, from the job agency behind the yellow sign, and you paid for the lesson in fear if not in money. Bright, cheap, and available 'today' is always, always the trap. You put the phone away and resolve to trust the paper, your own two feet, and the handful of people in this city who help a stranger for nothing at all."),
  [t("Read the paper's real rooms.",
     "Read the paper's real ads.",
     "Read the paper's real advertisements."),
   t("Walk to the canal side.",
     "Walk to the canal side.",
     "Walk down to the canal side.")])

P(12,
  t("How you cross the city is how your money lasts. The bus is fast, but every ride costs coins you may need. Your feet are slow, but they are free. You look at the map and the grey sky. It might rain. You decide.",
    "How you cross the city today is how far your money stretches. The bus is quick but every ride costs coins you might need for the deposit; your feet are slow but free. You glance at the map, then at the grey sky that might yet rain, and you decide.",
    "How you choose to cross the city today is, in the end, how far your money will stretch. The bus is quick, but every fare is a coin you might want back later for the deposit; your own feet are slow, but they cost nothing at all. You glance at the map, then at the low grey sky that looks as if it might rain before noon, and you make up your mind."),
  [t("Walk everywhere. Keep the fare.",
     "Walk everywhere and keep the fare money.",
     "Walk everywhere and keep the fare money for the deposit."),
   t("Take the bus. See more rooms.",
     "Take the bus so you can see more rooms.",
     "Take the bus so you can see more rooms in the time you have."),
   t("Go back for the paper first.",
     "Go back for the paper first.",
     "Go back for the paper first, then move.")])

P(13,
  t("The delivery man leans on his trolley. You ask him about the rooms here. \"Halloran's?\" he says. \"Over the rope-works. Good stair. Ask for the room at the top.\" He knows the street the way only a delivery man can.",
    "The delivery man leans on his trolley and listens. \"Halloran's?\" he says, when you ask. \"Over the rope-works. Good stair, clean building. Ask for the room at the top.\" He knows this street the way only someone who delivers to every door can.",
    "The delivery man leans on his trolley and hears you out. \"Halloran's?\" he says, when you finally get the question out. \"Over the rope-works. Good stair, clean building — ask for the room at the top.\" He knows this street the way only a man who has delivered to every single door on it possibly could."),
  [t("Thank him. Note the stair.",
     "Thank him and note the stair.",
     "Thank him and note the stair for noon."),
   t("Take the bus to the centre first.",
     "Catch the bus into the centre first.",
     "Catch the bus into the centre first, then come back.")])

P(14,
  t("The bedsit is close. You could be there in ten minutes on foot. It is cheap, and it is free right now. A room in the hand is worth a lot when the hotel wants you out tonight. But the canal room might be better.",
    "The bedsit is close — ten minutes on foot, and free to view right now. A room in the hand is worth a great deal when the hotel wants you out by tonight. Still, the canal room at noon might be the better bet, if you can bear to wait.",
    "The bedsit is close — ten minutes on foot, and free to view this minute. A room in the hand is worth a good deal when the hotel wants its key back by nightfall. And yet the canal room at noon might well be the better prospect, if you can stand to wait the morning out for it."),
  [t("Go straight up to see it.",
     "Go straight up to see it now.",
     "Go straight up and see it now."),
   t("Read the canal advert again first.",
     "Read the canal ad once more first.",
     "Read the canal advertisement once more before deciding.")])

P(15,
  t("The canal viewing is at noon. That is hours away. You have a whole city to wait in, and a whole city between you and the river. You could go there early and wait by the water. Or you could fill the time in the busy market square.",
    "The canal viewing isn't until noon. That's hours off, with a whole cold city to wait in and a good half of it between you and the river. You could set off early and wait by the water. Or you could fill the empty hours in the busy market square.",
    "The canal viewing isn't until noon. That's hours away yet, with a whole cold city to wait in and a good half of it lying between you and the river. You could set off early and wait out the morning by the water. Or you could kill the empty time in the noise and warmth of the market square."),
  [t("Set off for the canal early.",
     "Set off for the canal early.",
     "Set off for the canal early and wait."),
   t("Wait in the market square.",
     "Kill the time in the market square.",
     "Kill the time in the market square meanwhile.")])

P(16,
  t("You ask the kiosk woman about Vann. Her face closes like a door. \"That one,\" she says. \"Keep your money in your pocket.\" She does not want to say more. She has seen too many people go in bright and come out empty.",
    "You ask the kiosk woman about Vann. Her face closes like a door. \"That one,\" she says. \"Keep your money in your pocket.\" She won't say more. You sense she has watched too many hopeful people walk in and come out with nothing.",
    "You ask the kiosk woman about Vann, and her face closes like a door in a draught. \"That one,\" she says, and the two words carry a weight of history. \"Keep your money in your pocket.\" She won't be drawn further; you get the distinct sense she has watched too many hopeful strangers walk into that office and come out again with empty hands."),
  [t("Take her word. Leave it.",
     "Take her word and leave it.",
     "Take her word for it and leave it there."),
   t("Go to the square to think.",
     "Head into the square to think.",
     "Head into the square to think it over.")])

P(17,
  t("You cross Vann off your list. It stings a little. The photos were lovely, and the price was low. But lovely, and cheap, and today — that is the whole trick. You know it. You have paid to learn it once. You will not pay again.",
    "You cross Vann off your list. It stings a little; the photos were lovely and the price was low. But lovely and cheap and 'today' is the entire trick, and you know it. You paid to learn that lesson once already. You don't intend to pay for it twice.",
    "You cross Vann off your list, and it stings more than you'd like — the photographs were genuinely lovely and the price genuinely low. But lovely, and cheap, and available 'today' is the whole of the trick, and you know it in your bones by now. You paid once to learn that lesson, on a colder night than this; you have no intention of paying for it a second time."),
  [t("Back to the real rooms.",
     "Back to the paper's real rooms.",
     "Back to the paper's real rooms, then."),
   t("Into the square.",
     "Into the square.",
     "Into the square to regroup.")])

P(18,
  t("You walk. By midday you reach the market square. Your feet are sore and your shoes are wet. But the fare money is still in your pocket, every coin of it. You saved it, step by step. It might be a deposit one day soon. It feels good to have kept it.",
    "You walk, and by midday you reach the market square. Your feet are sore and your shoes are wet. But every coin of the fare money is still in your pocket, saved step by step. It might be part of a deposit by tonight. There's a quiet satisfaction in having kept it.",
    "You walk, and by midday you've reached the market square with sore feet, wet shoes, and every last coin of the fare money still in your pocket, saved one weary step at a time. It might yet be part of a deposit by nightfall. There is a quiet, stubborn satisfaction in having kept hold of it when the bus would have been so much kinder to your feet."),
  [t("Into the square. Choose a way.",
     "Into the square to choose a direction.",
     "Into the square to choose your next direction."),
   t("Straight on to the canal.",
     "Straight on to the canal.",
     "Press straight on to the canal."),
   t("The clock says the morning's gone.",
     "The square clock says the morning's gone.",
     "The square clock warns you the morning's already gone.")])

P(19,
  t("The bus sets you down at the square. It was fast, and your feet are dry. But there are fewer coins in your pocket now. Each ride is quick, and each ride is gone. You saved time, but you spent money. In this city, you cannot always keep both.",
    "The bus drops you at the square — fast, and your feet are dry for it, but the coins in your pocket are fewer now. Each ride is quick and each ride is gone. You bought time with money, and in this city you can rarely keep both at once.",
    "The bus drops you at the square — quick, and your feet are dry for it — but the little pile of coins in your pocket is noticeably thinner now. Each ride is fast, and each ride is simply gone. You've bought time with money, which is a fair trade until the evening comes and you find you needed the money more than the hour."),
  [t("Into the square.",
     "Into the square.",
     "Into the square, then."),
   t("On to the canal.",
     "On to the canal.",
     "Straight on to the canal.")])

P(20,
  t("The delivery man points you to Halloran's stair. \"Top room,\" he says again. \"Good building.\" Then he rattles his trolley away toward the centre. Now you know the door. You just have to wait for noon, and hope the room is still free.",
    "The delivery man points you to Halloran's stair — \"top room, good building,\" he says again — then rattles his trolley off toward the centre. Now you know the door. All that's left is to wait for noon and hope the room is still going.",
    "The delivery man points you firmly to Halloran's stair. \"Top room, good building,\" he tells you again, as if repetition were a kind of guarantee. Then he rattles his trolley away toward the centre and is gone. Now, at least, you know the door. All that remains is to wait out the hours until noon and hope the room hasn't gone to someone quicker."),
  [t("Go up to the canal building.",
     "Go up to the canal building.",
     "Go up to the canal building early."),
   t("Wait in the square first.",
     "Fill the time in the square first.",
     "Fill the time in the square first, then return.")])

P(21,
  t("The bedsit building has a damp stair. It smells of old cooking and cold air. The landlord waits at the top. He jingles his keys. He does not smile. Something here is not quite right, but the room is cheap, and cheap is what you can pay.",
    "The bedsit building greets you with a damp stair and a smell of old cooking. The landlord waits at the top, jingling his keys, not smiling. Something about the place isn't quite right — but the room is cheap, and cheap is all you can afford.",
    "The bedsit building greets you with a damp stair and a settled smell of old cooking and colder air. The landlord waits at the top, jingling his keys and not troubling to smile. Something about the whole set-up isn't quite right, and you can feel it — but the room is cheap, and cheap, just now, is the only thing you can actually afford."),
  [t("Go up to the room.",
     "Go up to see the room.",
     "Go up and see the room."),
   t("Back to the square. Something's off.",
     "Back to the square; something's off.",
     "Back to the square — something here is off.")])

P(25,
  t("The market square is loud and full. On one side is Vann's office. On the other side is the lane down to the canal. In the middle, Dania waves at you from a stall. Three ways to go, and the day is getting shorter with every hour.",
    "The market square is loud and crowded. Vann's office sits on one side, the canal lane on the other, and in between, Dania waves at you from a stall. Three directions, three chances, and the day getting shorter with every hour you stand here choosing.",
    "The market square is loud and crowded and warm with people. Vann's office sits on one side of it, the lane down to the canal on the other, and there, in between, Dania waves at you from behind a stall. Three directions, three different chances — and the daylight getting a little shorter with every hour you stand here in the middle, choosing."),
  [t("Vann's office.",
     "Vann's office.",
     "Try Vann's office."),
   t("The canal room.",
     "The canal room.",
     "Head for the canal room."),
   t("Go with Dania.",
     "Go with Dania.",
     "Go over to Dania."),
   t("The bedsit first.",
     "The bedsit first.",
     "The bedsit first, then.")])

P(26,
  t("The square clock strikes noon. The sound is heavy and slow. Half your daylight is spent, and you have not seen a single room yet. Winter days are short here. When the light goes, the hotel closes its door to you. You must move now.",
    "The square clock strikes noon, heavy and slow. Half your daylight is gone and you haven't seen a single room yet. The winter days are short in this city, and when the light goes the hotel shuts its door to you. You have to move.",
    "The square clock strikes noon, each stroke heavy and slow and faintly accusing. Half your daylight is spent already, and you have not so much as set foot in a single room. The winter days are miserly here, and when the last of the light goes the hotel will shut its door to you for good. There is no more time to stand about; you have to move."),
  [t("Choose a direction and move.",
     "Choose a direction and move.",
     "Choose a direction and move now."),
   t("Vann's office, quickly.",
     "Vann's office, quickly.",
     "Vann's office, and quickly.")])

P(27,
  t("Dania is wary of Vann too. You sit on a bench and put your two adverts side by side. Hers is a flat that needs a guarantor. Yours is the canal room. Together you know a little more than you did alone. That is worth something today.",
    "Dania is just as wary of Vann as you are. You share a bench and lay your two adverts side by side: hers is a flat that needs a guarantor, yours is the canal room. Between you, you know a little more than either of you did alone — and today, that's worth something.",
    "Dania, it turns out, is every bit as wary of Vann as you are. You share a bench and lay your two adverts side by side. Hers is a decent flat that needs a guarantor she doesn't have; yours is the canal room. Between you, you know a little more than either of you did alone. In a city like this, on a day like this, that small pooled knowledge is worth something real."),
  [t("View the canal room together.",
     "View the canal room together.",
     "Go and view the canal room together."),
   t("Split up to see more.",
     "Split up to cover more ground.",
     "Split up to cover more ground separately."),
   t("Both try the agent, to be sure.",
     "Both try the agent, just to be sure.",
     "Both try the agent, just to be certain.")])

P(28,
  t("With Dania beside you, the day feels less thin. Two people looking for rooms is still hard. But it is warmer than one. You talk as you walk. You share what little you know. The city feels a small step less strange with someone in it who is as lost as you.",
    "With Dania beside you, the day feels a little less thin. Two people hunting rooms is still hard going, but it's warmer than doing it alone. You talk as you walk and share what little you each know. The city feels one small step less strange for having someone in it as lost as you are.",
    "With Dania beside you, the whole day feels a little less thin. Two people hunting for rooms is still hard, discouraging work, but it is warmer than doing it alone in silence. You talk as you walk and pool what little you each know. The city feels one step less strange for holding someone in it as lost, and as hopeful, as you."),
  [t("The canal room together.",
     "Go to the canal room together.",
     "Go to the canal room together first."),
   t("Try the bedsit together first.",
     "Try the bedsit together first.",
     "Try the bedsit together first, then."),
   t("She wants one more first.",
     "She wants to see one more place first.",
     "She wants to see one more place of her own first.")])

P(29,
  t("Alone again, you keep your own counsel. It is quieter this way, and quicker. You do not wait for anyone. You do not explain your choices. But the day is long, and the streets are cold. There is no one now to share the weight of it.",
    "Alone again, you keep your own counsel. It's quieter this way, and quicker, with no one to wait for and no choices to explain. But the day is long, and the streets are cold. There's no one, now, to share the weight of it with.",
    "Alone again, you keep your own counsel, and there is something to be said for it. It's quieter this way, and quicker, with no one to wait on and no decisions to justify aloud. But the day is long, and the streets are cold and indifferent. There is no one, now, to help you carry the weight of the hours."),
  [t("The canal room.",
     "The canal room.",
     "Head for the canal room."),
   t("Vann's office.",
     "Vann's office.",
     "Try Vann's office."),
   t("The bedsit.",
     "The bedsit.",
     "The bedsit, then.")])

P(30,
  t("The room is small and grey and cheap. There is a bed, a chair, a window that looks at a wall. The landlord wants cash now. He asks you nothing. He offers you nothing. No lease, no questions, no help. Just a key, if you have the money.",
    "The room is small and grey and cheap: a bed, a chair, a window that looks straight at a wall. The landlord wants cash now and asks you nothing — no lease, no questions, no help of any kind. Just a key, if the money's in your hand.",
    "The room is small and grey and cheap — a bed, a chair, a window giving onto a blank brick wall. The landlord wants cash on the spot and asks you absolutely nothing: no lease, no references, no questions, no help of any kind. Just a key handed over, if the money happens to be in your hand. It is, you realise, the exact opposite of the canal room, in every way that turns out to matter."),
  [t("Take it now. A room is a room.",
     "Take it on the spot — a room is a room.",
     "Take it on the spot — a room is a room, after all."),
   t("Say you'll think about it.",
     "Say you'll think about it.",
     "Say you'll think it over."),
   t("Ask to look properly first.",
     "Ask to look at it properly first.",
     "Ask to look at it properly first, at least."),
   t("Ask why it's empty.",
     "Ask why it's empty; his face hardens.",
     "Ask why it's stood empty; his face hardens.")])

P(31,
  t("You give the landlord a cash hold, and the room is yours, in a way. You did not really look at it. You did not ask a single question. You were just tired of looking, and afraid of the dark coming, and it was there. Now it is done.",
    "You hand over a cash 'hold', and the room is yours, after a fashion. You didn't really look at it; you didn't ask a single question. You were simply tired of searching and afraid of the dark coming on, and the room was there. Now it's done.",
    "You hand over a cash 'hold', and the room is yours, after a fashion. You didn't really look at it, not properly; you didn't ask one honest question. You were simply worn out with searching, and quietly afraid of the dark coming on, and the room was there in front of you. Now it's done, and you feel the odd, hollow lightness of a decision made mostly out of tiredness."),
  [t("It's done. Move on.",
     "It's done. Move on with the day.",
     "It's done. Move on with the rest of the day."),
   t("A second thought, too late.",
     "Have a second thought, too late.",
     "Have a second thought about it, too late now.")])

P(32,
  t("You tell the landlord you will think about it. He shrugs. \"There's always someone,\" he says. He is right. Cheap rooms like this always find a taker by night. You have not lost it yet. But you have not kept it either.",
    "You tell him you'll think about it. He shrugs. \"There's always someone,\" he says, and he's right — cheap grey rooms like this always find a taker by nightfall. You haven't lost it yet. But you haven't held onto it, either.",
    "You tell him you'll think about it, and he shrugs, entirely unbothered. \"There's always someone,\" he says, and the awful thing is that he's right — cheap grey rooms like this one always find a taker by nightfall. You haven't lost it, exactly. But you haven't held onto it either, and the day keeps moving whether you decide or not."),
  [t("Out to look properly.",
     "Out to look properly elsewhere.",
     "Out to look properly somewhere else."),
   t("On to the canal room.",
     "On to the canal room.",
     "On, then, to the canal room.")])

P(33,
  t("You have a room, of sorts. Grey walls, a shared bathroom down the stair, a key in your pocket that is yours. It is not warm. It is not a home. But it is a door that shuts, and tonight you will not be on the street. That is not nothing.",
    "You have a room, of sorts: grey walls, a shared bathroom down the stair, a key in your pocket that is at least your own. It isn't warm, and it isn't a home — but it's a door that shuts, and tonight you won't be on the street. That is not nothing.",
    "You have a room, of sorts — grey walls, a shared bathroom down the draughty stair, a key in your pocket that is, at least, unarguably your own. It isn't warm, and it isn't remotely a home. But it is a door that shuts behind you, and tonight, whatever else is true, you won't be out on the street. In this city, on this day, that is genuinely not nothing."),
  [t("Carry on with the day anyway.",
     "Carry on with the day anyway.",
     "Carry on with the rest of the day anyway."),
   t("Wonder if you rushed it.",
     "Wonder if you rushed it.",
     "Wonder, now, if you rushed it.")])

P(34,
  t("You back out to keep looking. The bedsit will keep. Grim rooms always do. Nobody rushes for a room with a wall for a view and a landlord who does not care. You can come back if the day gives you nothing better. For now, you go on.",
    "You back out and keep looking. The bedsit will keep — grim rooms always do. Nobody rushes for a room with a wall for a view and a landlord who couldn't care less. You can come back to it if the day turns up nothing better. For now, you move on.",
    "You back out of it and keep looking. The bedsit will keep — grim rooms always do, for nobody in their right mind rushes for four grey walls with a landlord who couldn't care less. You can always come back to it if the day turns up nothing better, which is a cold sort of comfort. For now, you move on with the little daylight you have left."),
  [t("On to the canal room.",
     "On to the canal room.",
     "On, then, to the canal room."),
   t("Weigh it against the evening.",
     "Weigh it against the coming evening.",
     "Weigh it against the coming evening first."),
   t("The shared bathroom decides it.",
     "The shared bathroom decides it — no.",
     "The shared bathroom decides it for you — no.")])

P(35,
  t("You ask why the room has stood empty. The landlord bristles. \"You want it or not?\" he says. No lease. No questions. No answers. A room this cheap, empty this long, in a city this full. That is a question, and he will not answer it.",
    "You ask why the room's stood empty so long. The landlord bristles. \"You want it or not?\" No lease, no questions, no answers. A room this cheap, empty this long, in a city this crowded. That's a question with an answer he plainly doesn't want to give.",
    "You ask why the room has stood empty so long, and the landlord bristles at once. \"You want it or not?\" is all you get. No lease, no questions permitted, no answers. A room this cheap, empty this long, in a city this crowded, is a question with an answer somewhere. His refusal to give it is, in its way, the clearest answer of all."),
  [t("Say you'll think about it.",
     "Say you'll think about it.",
     "Say you'll think it over."),
   t("Back out.",
     "Back out of it.",
     "Back out of it entirely.")])

P(36,
  t("The room-to-share advert is far out, at the edge of the city. But the price is barely half the rest. For that price you could keep money back for food and fares. It is a long way to go on a short day, though. You cannot get the time back.",
    "The room-to-share advert is far out, at the edge of the city. But the price is barely half of everything else, low enough to leave you money for food and fares. It's a long way to travel on a short day, though. Time spent going is time you can't get back.",
    "The room-to-share advert is far out, right at the ragged edge of the city. But the price is barely half of everything else you've seen, low enough to leave you actual money for food and fares. It's a long way to go on a short winter day, though. Every minute spent travelling out there is a minute of daylight you'll never get back."),
  [t("Make the trip to see it.",
     "Make the trip out to see it.",
     "Make the long trip out to see it."),
   t("Too far. Back to the real ads.",
     "Too far — back to the real ads.",
     "Too far — back to the ads you can reach.")])

P(37,
  t("You get there at last. The share was taken this morning. The door is already someone else's door. A young man says sorry, and shuts it gently. You came a long way for a closed door. The day is shorter now, and you are further from every other room.",
    "You get there at last, only to find the share was taken this morning. The door is already someone else's. A young man says sorry and shuts it gently. You came a long way for a closed door. The day is shorter for it, and you're further now from every other room in the paper.",
    "You get there at last, footsore, only to learn the share was taken first thing this morning. The door is already, firmly, someone else's. A young man says he's sorry and closes it gently in your face. You've come a long way for a closed door. The day is markedly shorter for it, and you're now further from every other room than when you set out."),
  [t("Nothing here. Move on.",
     "Nothing here. Move on.",
     "Nothing here for you. Move on."),
   t("Ask if they know of anything.",
     "Ask if they know of anything else going.",
     "Ask whether they know of anything else going.")])

P(38,
  t("You are further out than you meant to be. The houses here are strange to you, and the buses are slow. The day is shorter now, and it is spent on nothing. You have learned one street and lost three hours. You must get back before the light goes.",
    "You're further out than you meant to be, among houses you don't know, where the buses run slow. The day is shorter now and spent on nothing: one strange street learned, three good hours lost. You need to get back before the light goes for the evening.",
    "You're further out than you ever meant to be, adrift among houses you don't know and buses that seem to run to no timetable at all. The day is markedly shorter now, and spent on precisely nothing: one strange street learned, three good hours simply lost. You need to get yourself back toward the centre before the light goes and takes your last real chances with it."),
  [t("Back toward the square.",
     "Back toward the square.",
     "Head back toward the square."),
   t("It's late. Think of the evening.",
     "It's getting late — think about the evening.",
     "It's getting late — start thinking about the evening.")])

P(39,
  t("You look at the shared bathroom off the stair. One cold room, one door, and a queue of other doors that all use it too. You picture the mornings: waiting, always waiting, in a line of strangers. A room, maybe. But never, ever a home.",
    "You take in the shared bathroom off the stair: one cold room, one door, and a row of other doors that all feed into it. You picture the mornings — waiting, always waiting, in a line of strangers. A room, perhaps. But never, in any real sense, a home.",
    "You take in the shared bathroom off the stair — one cold, tiled room, one door, and a whole row of other doors that all feed into it. You picture the mornings stretching ahead: waiting, always waiting, in a shivering line of strangers you'll never quite learn the names of. A room, perhaps, at a push. But never, in any sense that means anything, a home."),
  [t("On to the canal room.",
     "On to the canal room.",
     "On, then, to the canal room."),
   t("Think about the evening.",
     "Think about the evening.",
     "Start thinking about the evening.")])


# ======================= ACT II — THE VIEWINGS =============================

# --- the agent (the scam) ---
P(40,
  t("Vann's office is warm and bright. A queue of tired people waits inside. Vann himself is all smiles and hurry. He shakes your hand. He calls you \"friend.\" On the wall, a board of glossy rooms shines down at everyone. It all moves very fast.",
    "Vann's office is warm and bright, with a queue of tired people waiting inside. Vann himself is all smiles and hurry. He shakes your hand and calls you a friend. Above the queue, a board of glossy rooms shines down on everyone. The whole place moves fast, on purpose.",
    "Vann's office is warm and bright, and full of a queue of tired, hopeful people. Vann himself is all smiles and hurry; he shakes your hand and calls you \"friend\" before he's learned your name. Above the queue, a board of glossy rooms shines down on everyone. The whole place moves at speed, and the speed, you suspect, is entirely the point."),
  [t("Listen to the pitch.", "Listen to his pitch.", "Listen to the pitch he's selling."),
   t("Talk to the people waiting.", "Talk to the people in the queue.", "Talk to the people waiting in the queue.")])

P(41,
  t("The pitch is perfect. It is the very room from the photos. It is cheap. It is yours — if you leave a deposit today, to hold it. \"Rooms like this go in an hour,\" Vann says. \"But you seem sound. Just hold it, and it's yours.\"",
    "The pitch is perfect: the very room from the photos, cheap, and yours — so long as you leave a deposit today to hold it. \"Rooms like this go in an hour,\" Vann says warmly. \"But you seem sound. Just leave a little to hold it, and it's yours.\"",
    "The pitch is perfect, which is the first thing wrong with it: the very room from the photographs, cheap, and yours — provided you leave a deposit today, to hold it. \"Rooms like this go in an hour,\" Vann says, all warmth. \"But you seem sound to me. Just leave a little to hold it, and it's as good as yours.\""),
  [t("Ask to see the room first.", "Ask to see the room before you pay.", "Ask to see the actual room before you pay a penny."),
   t("Pay the deposit now.", "Pay the deposit now, before it's gone.", "Pay the deposit now, before it can be gone."),
   t("Say you'll think, and leave.", "Say you'll think about it, and leave.", "Say you'll think it over, and leave.")])

P(42,
  t("You talk to the people in the queue. A woman leans close. She says she has been \"holding\" a room for a week now, and still has no key. A man says the opposite. \"Vann found my cousin a flat,\" he says. \"No trouble at all.\" Two stories. Only one can be the true one.",
    "You talk to the people waiting. A woman leans close and says she's been 'holding' a room for a week and still has no key. A man just behind her says the opposite: Vann found his cousin a flat, no trouble at all. Two stories, pulling opposite ways.",
    "You talk to the people in the queue. A woman leans close and murmurs that she's been 'holding' a room for a week now and still hasn't seen a key. A man just behind her says the exact opposite: Vann found his cousin a flat, no trouble at all. Two stories, pulling in opposite directions, and only one of them can be the one that's true."),
  [t("Ask to see the room first.", "Ask to see the room first.", "Ask to see the room for yourself first."),
   t("Leave; you've heard enough.", "Leave; you've heard enough.", "Leave — you've heard quite enough."),
   t("Hear the woman's story out.", "Hear the woman's story out.", "Hear the woman's whole story out.")])

P(43,
  t("You ask to see the room first, before any money. Vann's smile stays, but his eyes go to the clock. \"It'll be gone by five,\" he says. \"The deposit only holds it. You can see it after.\" He wants the money first, and the room second. That is the wrong way round.",
    "You ask to see the room first, before a penny changes hands. Vann's smile holds, but his eyes flick to the clock. \"It'll be gone by five,\" he says. \"The deposit only holds it — you can see it after.\" Money first, room second: that's the wrong way round, and you know it.",
    "You ask to see the room first, before a penny changes hands. Vann's smile holds, but his eyes flick to the clock behind you. \"It'll be gone by five,\" he says smoothly. \"The deposit only holds it. You can see it after.\" Money first, room second — and that, you know perfectly well, is exactly the wrong way round."),
  [t("Pay to hold it, to be safe.", "Better safe — pay to hold it.", "Better safe than sorry — pay to hold it."),
   t("Refuse. Ask to see it now.", "Refuse the 'hold' and insist on seeing it.", "Refuse the 'hold' and insist, plainly, on seeing it."),
   t("Walk. He never said the address.", "Walk — he never once gave an address.", "Walk out — in all that talk, he never once named a street.")])

P(44,
  t("You hand over the deposit. It is most of your week's pay. Vann gives you a receipt and a firm handshake. \"Keys tomorrow,\" he says. \"Come at nine.\" His hand is warm. His smile is wide. The money is gone from your pocket, and the room is still only a photo on a wall.",
    "You hand over the deposit — most of your week's pay. Vann gives you a receipt and a firm handshake. \"Keys tomorrow,\" he says. \"Come at nine.\" His hand is warm, his smile wide. The money is out of your pocket now, and the room is still just a photo on a wall.",
    "You hand over the deposit — most of a week's pay, gone in a single motion. Vann gives you a receipt and a firm, warm handshake. \"Keys tomorrow,\" he says. \"Come at nine sharp.\" His hand is warm and his smile is wide, and the money is out of your pocket, and the room is still nothing but a photograph on a wall."),
  [t("Pocket the receipt and go.", "Pocket the receipt and go.", "Pocket the receipt and leave."),
   t("Head out, already uneasy.", "Head out, already uneasy about it.", "Head out, already uneasy about the whole thing.")])

P(45,
  t("You leave without paying a penny. Behind you, the queue moves up one place. Someone else steps into your spot. Someone else will hear the same warm words, and see the same bright photos. You keep your money, and you keep walking. The cold air outside feels clean.",
    "You leave without paying a penny. Behind you the queue shuffles up one place. Someone else takes your spot, ready to hear the same warm words and see the same bright photos. You keep your money and keep walking, and the cold air outside feels almost clean.",
    "You leave without paying a penny. Behind you the queue shuffles up one place, and someone else steps into the spot you've left, ready to hear the same warm words and admire the same bright photographs. You keep your money and you keep walking, and the cold air outside, after all that warmth, feels almost clean."),
  [t("On to a real room.", "On to a real room.", "On, then, to a real room."),
   t("Back to the square.", "Back to the square.", "Back to the square to regroup.")])

P(46,
  t("You refuse the hold. You ask him, plainly, for the address, so you can go and see the room. Vann's warmth cools at once. He talks around it. He does not have an address to give. A room with no address is not a room. You leave, and your money leaves with you.",
    "You refuse the hold and ask him, plainly, for the address so you can go and see the room. Vann's warmth cools in an instant. He talks around it, and around it, but he has no address to give. A room with no address is no room at all. You leave, money intact.",
    "You refuse the hold and ask him, plainly, for the address, so that you can walk over and see the room with your own eyes. Vann's warmth cools in an instant. He talks around it, and around it again, but the plain fact is he has no address to give you. A room with no address is not a room. You leave, and your money leaves the building with you."),
  [t("Out the door, money safe.", "Out the door, money intact.", "Out the door, your money still your own."),
   t("Straight to the canal instead.", "Straight to the canal instead.", "Straight down to the canal instead.")])

P(47,
  t("You just walk out. On the step, it comes to you clearly. For ten whole minutes, Vann talked and talked. He named a price. He named a day. He never once named a street. You know this trick from your first night. You paid for that lesson once. Not again.",
    "You just walk out. On the step it comes to you clearly. For ten whole minutes Vann talked and talked, naming a price, naming a day — and never once naming a street. You know this trick from your first night in the city. You paid for that lesson once already, and once was enough.",
    "You just walk out. On the step it comes to you with perfect clarity: for ten solid minutes Vann talked, and named a price, and named a day, and never once, not for a second, named a street. You know this exact trick from your first night in this city. You paid for the lesson once, in fear if not in cash, and once was more than enough."),
  [t("Note it and move on.", "Note it and move on.", "Make a note of it and move on."),
   t("On to the canal.", "On to the canal.", "On, then, to the canal.")])

P(48,
  t("You are out on the street with a receipt in your hand and no keys in your pocket. The morning is gone. The money is gone. A small cold doubt starts up in you, and grows. \"Keys tomorrow,\" he said. But tomorrow the hotel will not be yours, and neither, you fear, will the room.",
    "You're out on the street with a receipt in your hand and no keys in your pocket. The morning's gone, the money's gone, and a small cold doubt is starting to grow. \"Keys tomorrow,\" he said — but tomorrow the hotel won't be yours, and, you're beginning to fear, neither will the room.",
    "You're out on the street with a receipt in your hand and no keys in your pocket, and the morning gone with the money. A small, cold doubt has started up somewhere behind your ribs and is quietly growing. \"Keys tomorrow,\" he said — but tomorrow the hotel won't be yours, and, you are beginning to fear, neither will the room he sold you."),
  [t("Go and see a real room too.", "On to see a real room too.", "Go and see a real room as well, just in case."),
   t("Read the receipt again.", "Read the receipt again.", "Read the receipt over again."),
   t("Think about the evening.", "Think about the evening ahead.", "Start thinking about the evening ahead.")])

P(49,
  t("You are out of Vann's office with your purse still full. That is something. But the clock is unkind, and half the day is gone. You did not lose money, but you lost time. Two real rooms are left to try: the canal room, and the cheap bedsit. Choose, and go.",
    "You're out of Vann's with your purse still full — no small thing. But the clock is unkind and half the day is spent. You didn't lose money; you lost time. Two real rooms are left to try, the canal room and the bedsit. Choose one and go.",
    "You're out of Vann's office with your purse still full, which is no small victory. But the clock is unkind, and a good half of the day is already spent. You didn't lose money in there; you lost something harder to get back, which is time. Two real rooms are left to try — the canal room and the cheap bedsit. Choose one, and go."),
  [t("The canal room.", "The canal room.", "Head for the canal room."),
   t("The bedsit.", "The bedsit.", "The bedsit, then."),
   t("The queue is longer now.", "Leaving, the queue is longer than before.", "On the way out, the queue is longer than when you came.")])

P(65,
  t("You hear the woman's story out. She paid a deposit. Vann gave her a date. Then another date. Then \"so sorry, it fell through.\" And no money back. She has come again today, to ask for it. She will not get it. You can see that, even if she cannot yet.",
    "You hear the woman's story out. She paid a deposit; Vann gave her a date, then another, then \"so sorry, it fell through\" — and never gave the money back. She's come again today to ask for it. She won't get it. You can see that plainly, even if she can't quite let herself yet.",
    "You hear the woman's story out. She paid a deposit; Vann gave her a date, and then another date, and then a soft \"so sorry, it fell through\" — and never once gave the money back. She has come in again today to ask for it. She won't get it, and you can see that quite plainly, even if she can't yet let herself believe it."),
  [t("Thank her. Don't pay.", "Thank her and refuse to pay.", "Thank her, and refuse to pay a penny."),
   t("Vann pushes one last time.", "Vann leans in with one last push.", "Vann leans in for one last push.")])

P(66,
  t("\"Last one at this price,\" Vann says. His hand is already out for the money. \"People like you don't get second chances in this city.\" He means it to frighten you. And it is the tell. A real room does not need a threat to sell it. You see the trick whole now.",
    "\"Last one at this price,\" Vann says, hand already out. \"People like you don't get second chances in this city.\" He means it to frighten you into paying — and that line is the tell. A real room doesn't need a threat to sell it. You can see the whole trick now.",
    "\"Last one at this price,\" Vann says, his hand already out for the money. \"People like you don't get second chances in this city.\" He means it to frighten you into reaching for your purse — and that single line is the tell. A real room does not need a threat to sell it. You see the whole shape of the trick now, laid out plain."),
  [t("Pay, against your sense.", "Pay, against your better sense.", "Pay, against every bit of your better sense."),
   t("That line is the tell. Leave.", "That line is the tell. Leave.", "That line is the tell — leave.")])

P(68,
  t("You look back on your way out. The queue has doubled since you came in. The same warm smile, the same clock on the wall, the same open hand. New faces now, all hopeful, all tired. You are glad your money is still yours. You will not be one of them.",
    "You glance back on your way out. The queue has doubled since you arrived: the same warm smile, the same clock, the same open hand. But all new faces now, hopeful and tired. You're glad your money is still your own. You won't be one of them.",
    "You glance back on your way out. The queue has doubled since you first came in: the same warm smile, the same clock on the wall, the same open, patient hand. But all new faces now — every one of them hopeful, and tired, and a little afraid. You're glad your money is still your own. Whatever else happens today, you won't be one of them."),
  [t("On to a real room.", "On to a real room.", "On, then, to a real room."),
   t("Think about the evening.", "Think about the evening.", "Start thinking about the evening.")])

# --- the canal room and the mystery ---
P(50,
  t("Halloran's building stands over the old rope-works. The stair is steep, but it is swept and clean. At the top, a door is open. A woman waits in it, grey-eyed and straight-backed. She does not smile at you. But she does not look away, either. She looks at you properly.",
    "Halloran's building stands over the old rope-works. The stair is steep but swept clean, and at the top a door stands open with a woman waiting in it — grey-eyed, straight-backed. She doesn't smile at you. But she doesn't look away, either; she looks at you properly, which is rarer.",
    "Halloran's building stands over the old rope-works, and the stair up to it is steep but swept scrupulously clean. At the top a door stands open, and a woman waits in it — grey-eyed, straight-backed, entirely still. She doesn't smile at you. But nor does she look away, which is rarer and worth more: she looks at you properly, the way this city so seldom bothers to."),
  [t("Go up for the viewing.", "Go up for the viewing.", "Climb the stair for the viewing."),
   t("You're early. Wait in the square.", "You're early — wait in the square.", "You're early — go and wait in the square.")])

P(51,
  t("Mrs Halloran is brisk and grey-eyed. She shows you in. The room has good light off the water. But someone's things are still here, half-packed. A coat hangs on a hook. A tin of buttons sits on the sill. A box waits by the wall. Someone lived here, and lately, and left in a hurry.",
    "Mrs Halloran is brisk and grey-eyed, and shows you in without ceremony. The room has good light off the water. But someone's things are still here, half-packed: a coat on a hook, a tin of buttons on the sill, a box by the wall. Someone lived here lately, and left in a hurry.",
    "Mrs Halloran is brisk and grey-eyed, and shows you in without ceremony or small talk. The room has good, clean light off the water. But someone's things are still here, only half-packed: a coat left hanging on a hook, a tin of buttons on the sill, a box waiting by the wall. Someone lived here, and lately, and by the look of it left in a considerable hurry."),
  [t("Ask about the last tenant.", "Ask about the last tenant.", "Ask her about the last tenant."),
   t("Look at the room itself first.", "Look at the room itself first.", "Look at the room itself first.")])

P(52,
  t("\"He's gone. That's all,\" she says. And she turns away to fix the window catch. Her voice is flat and closed. She does not want the question. Whatever happened here, she has folded it up and put it away. She will not take it out for a stranger.",
    "\"He's gone. That's all,\" she says, and turns away to fuss with the window catch. Her voice is flat and closed. She doesn't want the question. Whatever happened here, she's folded it up and put it away, and won't be taking it out again for a stranger.",
    "\"He's gone. That's all,\" she says, and turns away at once to busy herself with the window catch. Her voice is flat and firmly closed. She doesn't want the question, and won't have it. Whatever happened in this room, she has folded it up small and put it away somewhere, and she has no intention of taking it out again for the benefit of a stranger."),
  [t("Let it go. Ask about terms.", "Let it go; ask about the terms.", "Let it go, and ask about the terms."),
   t("Look at what he left.", "Look more closely at what he left.", "Look more closely at what he left behind.")])

P(53,
  t("The room has good light off the water. A coat is still on the hook by the door. The tin of buttons sits in the sun on the sill. Someone lived here, and not long ago. You could live here too. You can feel it. It is the first room today that has felt like a home.",
    "The room has good light off the water. A coat still hangs on the hook by the door; the tin of buttons catches the sun on the sill. Someone lived here, and not long ago. You could live here too — you can feel it. It's the first room today that has felt like a home at all.",
    "The room has good, generous light off the water. A coat still hangs on the hook by the door, and the tin of buttons catches the thin sun on the sill. Someone lived here, and not long ago, and left it warm somehow. You could live here too; you can feel it in your chest. It is the first room all day that has felt, even faintly, like a home."),
  [t("Notice the things he left.", "Notice the things he left.", "Notice the things he's left behind."),
   t("Ask what happened here.", "Ask Halloran what happened here.", "Ask Halloran what happened here."),
   t("Picture yourself living here.", "Picture yourself living here.", "Let yourself picture living here.")])

P(54,
  t("She names the terms. The rent is fair. The deposit is steep, but not unfair. Then she says the word you were waiting for and dreading: references. \"People who'll say you're sound,\" she says. You have been in this city three days. You know no one who could say it.",
    "She names the terms. The rent is fair; the deposit is steep but not unreasonable. Then comes the word you were both waiting for and dreading: references. \"People who'll say you're sound,\" she explains. You've been in this city three days. You know no one who could say any such thing.",
    "She names the terms plainly. The rent is fair; the deposit is steep but not unreasonable. Then comes the word you were both waiting for and quietly dreading: references. \"People who'll vouch that you're sound,\" she explains, as if it were the simplest thing in the world. You have been in this city precisely three days. You know no one alive here who could say it."),
  [t("Face the references problem.", "Face the references problem.", "Face the references problem head-on."),
   t("Look around once more.", "Look around once more as she talks.", "Look around once more while she talks.")])

P(55,
  t("Among his things, a notebook lies open on the sill. You look at it. Page after page of names and addresses, in a careful, patient hand. Someone wrote these to remember people by. Someone meant to write to all of them. And then, it seems, he did not get the chance.",
    "Among his things, a notebook lies open on the sill. You glance at it: page after page of names and addresses, in a careful, patient hand. Someone wrote these to remember people by — someone who meant to write to all of them, and then, it seems, never got the chance.",
    "Among his things, a notebook lies open on the sill. You glance down at it: page after page of names and addresses, all in a careful, patient hand. Someone wrote these to remember people by — someone who plainly meant to write to every one of them, and then, by the look of the half-packed room, never quite got the chance."),
  [t("Pick it up to return to him.", "Pick it up to give back to him.", "Pick it up, meaning to give it back to him."),
   t("Leave it; not your business.", "Leave it; it's not your business.", "Leave it be; it's not your business."),
   t("Ask Halloran about it.", "Ask Halloran about it.", "Ask Halloran about it directly.")])

P(56,
  t("References. You turn the word over. You know no one in this whole city who could vouch for you. You have been here three days. Three days of stations and streets and closed doors. The one person who might speak for you is Ms Rowe. And she is your boss of three days, no more.",
    "References. You turn the word over in your mind. You know no one in this whole city who could vouch for you. You've been here three days — days of stations and streets and closed doors. The one person who might speak for you is Ms Rowe, and she's been your employer for all of three days.",
    "References. You turn the word over and over in your mind. You know no one in this entire city who could honestly vouch for you: you've been here three days, days made of cold stations and strange streets and doors closing softly in your face. The one person who might conceivably speak for you is Ms Rowe — and she has been your employer for exactly three days, no more."),
  [t("She names her condition.", "She names her one condition — unless.", "She names her one condition — unless."),
   t("She softens a little.", "She softens a little as you take it in.", "She softens a little as she watches you take it in.")])

P(57,
  t("You slip the notebook into your bag, to give back to him. It does not feel like taking. It feels like keeping it safe. Wherever he has gone, these names mattered to him once. If you ever find him, you will hand them back. Until then, you will look after them.",
    "You slip the notebook into your bag to give back to him. It doesn't feel like taking; it feels like keeping it safe. Wherever he's gone, these names mattered to him once. If you ever find him, you'll hand them straight back. Until then, you'll look after them for him.",
    "You slip the notebook into your bag, meaning to give it back to him. It doesn't feel like taking, exactly; it feels more like keeping something safe. Wherever he's gone, these names mattered to him once, enough to write down and carry. If you ever find him, you'll hand them straight back. Until then, you'll look after them for him."),
  [t("Turn back to Halloran.", "Turn back to Halloran.", "Turn back to Mrs Halloran."),
   t("Ask her about it, holding it.", "Ask her about it, holding it.", "Ask her about it, the notebook still in your hand.")])

P(58,
  t("You put the notebook down again, exactly where it lay. Whatever it is, whoever he was, it is not yours to take. You have enough to carry today without another stranger's names in your bag. You step back from the sill and turn to the room, and the woman, and the day.",
    "You set the notebook down again, exactly where it lay. Whatever it is, whoever he was, it's not yours to take. You have quite enough to carry today without a stranger's names in your bag. You step back from the sill and turn to the room, and the woman, and the day ahead.",
    "You set the notebook down again, exactly where it was lying. Whatever it is, and whoever he was, it isn't yours to take. You have more than enough to carry today without adding a stranger's carefully written names to your bag. You step back from the sill and turn instead to the room, and the woman, and the long day still ahead of you."),
  [t("Turn back to Halloran.", "Turn back to Halloran.", "Turn back to Mrs Halloran."),
   t("Ask about him instead.", "Ask about him instead.", "Ask her about him instead.")])

P(59,
  t("\"No references, no room,\" she says. Her voice is not unkind. It is just plain. \"Unless,\" she adds, \"you give me a reason to trust my own eyes.\" She looks at you, waiting. This is a door held open just a crack. What you say next decides if it opens or shuts.",
    "\"No references, no room,\" she says — not unkindly, just plainly. \"Unless,\" she adds, \"you give me a reason to trust my own eyes.\" She looks at you and waits. It's a door held open just a crack; what you say next decides whether it opens or closes.",
    "\"No references, no room,\" she says, not unkindly but quite plainly. \"Unless,\" she adds, after a moment, \"you give me some reason to trust my own eyes.\" She looks at you steadily and waits. It's a door held open just a crack — and what you choose to say next is what decides whether it swings open or shuts in your face."),
  [t("Mention Kessler and Rowe.", "Mention Kessler and Rowe.", "Mention the firm, Kessler and Rowe."),
   t("Just be honest about yourself.", "Just be honest about who you are.", "Just be honest about who you really are.")])

P(60,
  t("She watches how you move through the room. You move carefully, as if it were already someone's home — because it is, or was. You do not touch what is not yours. Something in her grey face eases, just a little. She has seen a great many people. She knows how to read one.",
    "She watches how you move through the room — carefully, as if it were already someone's home, which it is, or was. You don't touch what isn't yours. Something in her grey face eases, just a little. She's seen a great many people through that door, and she knows how to read one.",
    "She watches, closely, how you move through the room — carefully, quietly, as if it were already someone's home, which of course it is, or lately was. You don't touch what isn't yours to touch. Something in her grey, guarded face eases, just a little. She has seen a great many people come through that door over the years, and she knows exactly how to read one."),
  [t("Mention your job at the firm.", "Mention your job at the firm.", "Mention your job at the firm."),
   t("Be honest: new, no one, a chance.", "Be honest: new here, no one, need a chance.", "Be honest — new here, no one to vouch for you, in need of a chance.")])

P(61,
  t("You mention Kessler and Rowe. Her eyebrows lift. \"Rowe,\" she says slowly. \"I know that name.\" She looks at you with new eyes. If Rowe would speak for you, that would change things. A name can open a door your face cannot.",
    "You mention Kessler and Rowe. Her eyebrows lift. \"Rowe,\" she says slowly. \"I know that name.\" She looks at you again with new eyes. \"If she'd say a word for you, that would be a different matter.\" A name has opened a door your face alone couldn't.",
    "You mention Kessler and Rowe, and her eyebrows lift a fraction. \"Rowe,\" she says, slowly, tasting it. \"I know that name.\" She looks at you again, with different eyes this time. \"If she'd say a word for you, well — that would be another thing entirely.\" A name has opened a door your face alone could never have shifted."),
  [t("A reference from the firm — how?", "A reference from the firm — but how?", "A reference from the firm — but how would you get one?"),
   t("Say you'll be honest instead.", "Say you'll just be honest instead.", "Say you'd rather just be honest with her instead.")])

P(62,
  t("You tell her the plain truth. Three days in this city. No one to vouch for you. A week's pay in your pocket. You have this one day to find a home before the hotel shuts you out. You do not dress it up. You just say it, and let it stand there between you.",
    "You tell her the plain truth. Three days in this city, no one to vouch for you. A week's pay in your pocket, and one day to find a home before the hotel shuts you out. You don't dress it up or ask for pity. You just say it, and let it stand there between you.",
    "You tell her the plain truth of it. Three days in this city. No one alive here to vouch for you. A week's pay in your pocket and this one short day to find a home before the hotel shuts you out for good. You don't dress it up, and you don't ask for pity. You simply say it, and let it stand there in the good light between you."),
  [t("She says: come back at dusk.", "She says: come back at dusk.", "She tells you to come back at dusk."),
   t("She studies you a moment more.", "She studies you a moment longer.", "She studies you a long moment more.")])

P(63,
  t("\"Come back when the light goes,\" she says. \"I'll have thought by then.\" It is not a yes. But it is not a no. On the stair as you go down, a neighbour is struggling. She has heavy bags and a small, tired child. She is losing the fight with the stairs.",
    "\"Come back when the light goes,\" she says. \"I'll have thought by then.\" It isn't a yes; but it isn't a no, either. On the stair as you head down, a neighbour is wrestling heavy shopping bags and a small, tired child. She is plainly losing the fight with the steps.",
    "\"Come back when the light goes,\" she says. \"I'll have thought it over by then.\" It isn't a yes; but, importantly, it isn't a no either. On the stair as you head back down, a neighbour is wrestling with heavy shopping bags and a small, tired child at once, and quite plainly losing her fight with the steps."),
  [t("Fill the hours till dusk.", "Fill the hours until dusk.", "Go and fill the hours until dusk."),
   t("Help the neighbour on the stair.", "Help the neighbour on the stair.", "Stop and help the neighbour on the stair.")])

P(64,
  t("Hours to kill before dusk. A whole cold city that still does not know your name. You could go back to the square and its noise. You could sit somewhere and think ahead to the evening. Or you could add up, honestly, what this long day has already cost you.",
    "Hours to kill before dusk, in a whole cold city that still doesn't know your name. You could go back to the square and its noise. You could sit somewhere and think ahead to the evening. Or you could add up, honestly, what this long day has already cost you.",
    "Hours yet to kill before dusk, in a whole cold city that still doesn't know your name or care to. You could go back to the square and its noise. You could find somewhere quiet to sit and think ahead to the evening. Or you could sit down and add up, honestly, exactly what this long grey day has already cost you."),
  [t("Back to the square.", "Back to the square.", "Head back to the square."),
   t("Think ahead to the evening.", "Think ahead to the evening.", "Sit and think ahead to the evening."),
   t("Count what the day has cost.", "Count what the day has cost you.", "Add up what the day has already cost you.")])

P(80,
  t("You ask Halloran, outright, what happened here. She stiffens. She straightens the coat on its hook, though it does not need it. Then she changes the subject to the rent, the stair, the water bill. The room holds its breath. There is a story here, and she is sitting on it.",
    "You ask Halloran outright what happened here. She stiffens. She straightens the coat on its hook, though it needs no straightening, and changes the subject to the rent, the stair, the water. The room seems to hold its breath. There's a story here, and she is sitting hard on it.",
    "You ask Halloran, outright, what happened in this room. She stiffens visibly. She reaches out and straightens the coat on its hook, though it doesn't need straightening at all, and then changes the subject briskly to the rent, the stair, the water bill. The room itself seems to hold its breath. There is a story here, plainly, and she is sitting on it with her whole weight."),
  [t("Press gently.", "Press her gently.", "Press her, gently."),
   t("Let it drop.", "Let it drop.", "Let the matter drop.")])

P(81,
  t("You press gently. Halloran turns away, so you turn too. On the stair, a neighbour is passing. \"The lad up top?\" he says, low. \"Went to sea. All of a sudden. She won't speak of it.\" Then he is gone down the stair.",
    "You press gently. Halloran turns away, so you turn too — and on the stair a neighbour is passing. \"The lad up top?\" the neighbour murmurs. \"Went to sea. All of a sudden. She won't speak of it, so don't you go asking her.\" And then the neighbour is gone down the stair.",
    "You press, gently. Halloran turns away from you, so you turn too, and on the stair a neighbour happens to be passing. \"The lad up top?\" the neighbour murmurs, low and quick. \"Went to sea. All of a sudden, it was. She won't speak of it, so don't you go asking her.\" And then the neighbour, too, is gone off down the stair, and you're left holding it."),
  [t("Ask the neighbour more.", "Ask the neighbour more.", "Ask the neighbour for more."),
   t("Leave it; help the neighbour.", "Leave it — help the neighbour instead.", "Leave it be, and help the neighbour instead."),
   t("Back to Halloran and the room.", "Back to Halloran and the room.", "Turn back to Halloran and the room.")])

P(82,
  t("\"Owed nothing. Harmed no one,\" the neighbour says. \"Just gone, one morning, with a bag. It's her boy, see. Her only one. She won't say his name now.\" The neighbour shakes their head, kindly. \"So mind how you go, up there. That room's got more in it than furniture.\"",
    "\"Owed nothing, harmed no one,\" the neighbour says. \"Just gone one morning with a bag. It's her boy, see — her only one. She won't say his name now.\" They shake their head, kindly. \"So mind how you go up there. That room's got more in it than furniture.\"",
    "\"Owed nothing, harmed no one,\" the neighbour says, quietly. \"Just gone, one morning, with a single bag. It's her boy, see — her only one, and grown. She won't so much as say his name now.\" They shake their head, not unkindly. \"So mind how you go, up there. That little room's got a good deal more in it than furniture.\""),
  [t("Her boy. You understand now.", "Her boy. You understand the packed box now.", "Her boy — you understand the half-packed box now."),
   t("Enough. Help with the shopping.", "Enough — help with the shopping.", "Enough of it — go and help with the shopping.")])

P(83,
  t("Her son. It all makes sense now. The half-packed room she cannot finish packing. The coat she will not take down. The notebook of addresses he meant to write to, and never did. She is not hiding a crime. She is holding a door open for someone who may never come back.",
    "Her son. It all makes sense now. The half-packed room she can't bring herself to finish. The coat she won't take down. The notebook of addresses he meant to write to, and never did. She isn't hiding a crime. She's holding a door open for someone who may never come back.",
    "Her son. It all falls into place now. The half-packed room she can't bring herself to finish. The coat she won't take down from its hook. The notebook of addresses he plainly meant to write to, and never did. She isn't hiding anything shameful. She's simply holding a door open, month after month, for someone who may never walk back through it."),
  [t("Take the notebook to return it.", "Take the notebook, to return it.", "Take the notebook, meaning to return it to her."),
   t("Say nothing; go back down.", "Say nothing, and go back down.", "Say nothing, and go quietly back down.")])

P(84,
  t("At the window, you can see it. Yourself, here, in this room. The grey water below, the good light, a kettle on the ring, a life slowly built. It is the first room today that felt like more than four walls. You catch yourself hoping, and it frightens you a little.",
    "At the window you can see it: yourself, here, in this room. The grey water below, the good light, a kettle on the ring, a life slowly built up. It's the first room today that has felt like more than four walls. You catch yourself hoping, and the hoping frightens you a little.",
    "At the window you can suddenly see it all: yourself, here, in this very room. The grey water sliding below, the good clean light, a kettle on the ring, a whole life quietly built up over time. It's the first room all day that has felt like more than four walls and a price. You catch yourself hoping, properly hoping, and the hope frightens you a little."),
  [t("Look at what he left behind.", "Look at what he left behind.", "Look again at what he left behind."),
   t("Turn back before you hope too much.", "Turn back before you hope too hard.", "Turn away before you let yourself hope too hard.")])

P(85,
  t("In the coat pocket, your fingers find a photograph. It is this same window. A young man stands at it, laughing. Beside him is Halloran — younger, softer, laughing too. You should not have looked. But now you have, and you cannot un-see whose room this is.",
    "In the coat pocket your fingers find a photograph. It's this same window — a young man standing at it, laughing, and beside him Halloran, younger and softer, laughing too. You shouldn't have looked. But now you have, and you can't un-see whose room this really is.",
    "In the coat pocket your fingers close on a photograph. It's this same window — a young man standing at it, laughing at whoever held the camera, and beside him Halloran herself, years younger and softer, laughing too. You know you shouldn't have looked. But now you have, and there's no un-seeing it, and no pretending you don't know whose room this is."),
  [t("You understand who lived here.", "You understand who lived here.", "You understand, now, who lived here."),
   t("Put it back exactly as it was.", "Put it back exactly as it was.", "Put it back exactly where it was.")])

P(86,
  t("Someone lived here, and left fast. The woman letting the room is no stranger to him. She is his mother. She lets his room to keep the rent coming in. She keeps his coat on the hook. That way the room is never quite empty of him. You hold all of this now, quietly.",
    "Someone lived here and left fast, and the woman letting the room is no stranger to him at all — she is his mother. She lets his room to keep the rent coming in. She keeps his coat on the hook, so the place is never quite empty of him. You hold all of that now, quietly.",
    "Someone lived here, and left in a hurry, and the grey-eyed woman letting the room is no stranger to him at all: she is his mother. She lets his room out to keep the rent coming in, and keeps his coat on its hook so that the place is never, quite, empty of him. You hold all of that now, quietly, and it changes how you'll speak to her."),
  [t("Take the notebook to give back.", "Take the notebook, to give it back.", "Take the notebook, meaning to give it back to her."),
   t("Say nothing yet.", "Say nothing of it yet.", "Say nothing of it yet.")])

# --- the guarantor flat & the reference ---
P(70,
  t("There is a better flat, across town. Clean, bright, a proper little home. But it needs a guarantor — someone to stand behind your rent if you cannot pay it. You have no such person in this city. Unless the firm would do it. Unless Ms Rowe would put her name to yours.",
    "There's a better flat across town — clean, bright, a proper little home. But it needs a guarantor: someone to stand behind your rent if you ever fall short. You have no such person in this city. Unless the firm would do it — unless Ms Rowe would put her name to yours.",
    "There's a better flat across town — clean, bright, a proper little home of the kind you'd almost stopped hoping for. But it needs a guarantor: someone willing to stand behind your rent if you ever fall short. You have no such person in this whole city. Unless the firm itself would do it — unless Ms Rowe, of all people, would put her name to yours."),
  [t("Think how to get the firm's word.", "Think how to get the firm's word.", "Work out how you might get the firm's word."),
   t("Give up on the good flat.", "Give up on the good flat.", "Give up on the good flat entirely.")])

P(71,
  t("You could ask. But it is your first week at the firm. It is a great deal to ask of people who barely know you. And yet — you did tell Ms Rowe everything, on your first night. The whole strange story. She listened to all of it, and hired you anyway.",
    "You could ask. But it's your first week at the firm, and it's a great deal to ask of people who barely know you. And yet — you did tell Ms Rowe everything on your first night, the whole strange story of it. She listened to every word, and hired you anyway.",
    "You could ask. But it's your first week at the firm, and it's a great deal to ask of people who barely know your face yet. And yet — you did tell Ms Rowe everything, on your first night here: the whole strange, exhausting story of it. She listened to every word without once interrupting, and hired you anyway. That has to count for something now."),
  [t("Call Ms Rowe, who trusts you.", "Call Ms Rowe, who trusts you.", "Call Ms Rowe, who has reason to trust you."),
   t("Ask a colleague instead.", "Ask a colleague at the firm instead.", "Ask a colleague at the firm instead."),
   t("Too much to ask. Let it go.", "It's too much to ask. Let it go.", "It's too much to ask in your first week. Let it go.")])

P(72,
  t("You call Ms Rowe. You explain. There is a short silence. Then: \"Of course. Put them onto me.\" That is all. No fuss, no lecture. You were straight with her once, when it would have been easier to lie. So she is straight with you now, when it matters.",
    "You call Ms Rowe and explain. There's a short silence, then: \"Of course. Put them onto me.\" That's all — no fuss, no lecture. You were straight with her once, on a night when lying would have been easier. She is straight with you now, when it matters most.",
    "You call Ms Rowe and explain the whole thing. There's a short silence on the line, and then, simply: \"Of course. Put them onto me.\" That's all. No fuss, no lecture, no making you ask twice. Because you were straight with her once, on a cold night when a lie would have been so much easier, she is straight with you now, without hesitation, when it matters most."),
  [t("A reference — you have one.", "A reference — you have one now.", "A reference — you have one now, and a real one."),
   t("Thank her; get on with the day.", "Thank her and get on with the day.", "Thank her, and get on with the day.")])

P(73,
  t("You ask a colleague at the firm. They hesitate — you are new, after all — but in the end they agree to say you are sound. It is not warm. It is a favour, done a little stiffly, for a near-stranger. But it is enough. A name is a name, and you have one now.",
    "You ask a colleague at the firm. They hesitate — you're new, after all — but in the end agree to say you're sound. It isn't warm; it's a favour done a little stiffly, for a near-stranger. But it's enough. A name is a name, and you have one now.",
    "You ask a colleague at the firm. They hesitate — you're new, after all, and this is a real thing to ask — but in the end they agree to say you're sound. It isn't warm, exactly; it's a favour done a little stiffly, for someone who's still very nearly a stranger. But it's enough for the letting man. A name is a name, and you have one now."),
  [t("A reference, of a kind.", "A reference, of a kind.", "A reference, of a kind, at least."),
   t("On with the day.", "On with the day.", "On, then, with the day.")])

P(74,
  t("You let the good flat go. You cannot ask the firm to put its name to yours. Not in your first week. Not when they barely know you. It is the right choice, maybe. But it is a door closing. You feel the cold of it as you turn back to the day's smaller chances.",
    "You let the good flat go. You can't ask the firm to put its name to yours — not in your first week, not when they barely know your face. It may be the right choice. But it's a door closing, and you feel the cold of it as you turn back to the day's smaller chances.",
    "You let the good flat go. You simply can't bring yourself to ask the firm to put its name to yours — not in your first week, not when they barely know your face yet. It may well be the right choice, the modest one. But it's a door closing all the same, and you feel the cold draught of it as you turn back to the day's smaller, humbler chances."),
  [t("Back to the day's real chances.", "Back to the day's real chances.", "Back to the day's smaller, real chances."),
   t("Into the square to think.", "Into the square to think.", "Into the square to think it through.")])

P(75,
  t("You have a reference now. A name that will answer for you when your own face cannot. It is a strange, warm feeling. Someone will vouch for you, in a city where you know almost no one. It changes what doors will open tonight. You carry it carefully, like the money in your pocket.",
    "You have a reference now — a name that will answer for you when your own face can't. It's a strange, warm feeling, being vouched for in a city where you know almost no one. It changes which doors will open tonight, and you carry it as carefully as the money in your pocket.",
    "You have a reference now: a name that will answer for you when your own unknown face cannot. It's a strange and genuinely warm feeling, being vouched for in a city where you know almost no one at all. It changes which doors will open to you tonight — and you carry it as carefully as you carry the money folded in your pocket."),
  [t("Carry it to the evening.", "Carry it into the evening.", "Carry it carefully into the evening."),
   t("Into the square first.", "Into the square first.", "Into the square first, then.")])

# --- the neighbour ---
P(76,
  t("The neighbour is losing her fight with the stairs. Her bags are splitting. A small child clings to her leg on the step. Three floors still to climb, and no free hand to do it with. She looks at you as you pass. She does not ask. But her eyes do.",
    "The neighbour is losing her fight with the stairs. Her bags are splitting and a small child clings to her leg. There are three floors still to climb, with no free hand to do it. She looks at you as you pass. She doesn't ask for help — but her eyes do.",
    "The neighbour is quietly losing her fight with the stairs. Her shopping bags are splitting at the corners, and a small child clings hard to her leg on the step. There are three whole floors still to climb, with no free hand left to do it. She looks at you as you pass her on the landing. She doesn't ask for anything — but her tired eyes do."),
  [t("Take the bags and help up.", "Take the bags and help her up.", "Take the bags and help her up the stairs."),
   t("You're in a hurry. Pass by.", "You're in a hurry — pass by.", "You're in a hurry — pass her by."),
   t("Mind the child, she takes the bags.", "Mind the child while she manages the bags.", "Offer to mind the child while she manages the bags.")])

P(77,
  t("You take the heavy bags and carry them up, all three floors. The child watches you gravely from below. At her door, the woman is breathless with thanks. \"You're a good one,\" she says. \"I'll not forget it. You need anything on this stair, you knock. You hear?\"",
    "You take the heavy bags and carry them up all three floors, the child watching you gravely from below. At her door the woman is breathless with thanks. \"You're a good one,\" she says. \"I'll not forget it. Anything you need on this stair, you knock — you hear me?\"",
    "You take the heavy, splitting bags and carry them up, all three floors, the small child watching you gravely from below. At her door the woman is breathless with gratitude. \"You're a good one,\" she says, gripping your arm. \"I'll not forget it, mind. Anything you need on this stair, ever, you knock on my door — you hear me?\""),
  [t("Wave it off; back to the day.", "Wave it off and get back to the day.", "Wave it off, and get back to the day."),
   t("She points you back to Halloran.", "She points you back toward Halloran.", "She points you back toward Halloran's door.")])

P(78,
  t("You pass by with a small nod. Not unkind, just busy. You have your own day to save, and no room in it for anyone else's bags. The stair swallows the sound of her struggling up behind you. By the top, you have half-forgotten her. Almost.",
    "You pass by with a small nod — not unkind, just busy. You've your own day to save and no room in it for anyone else's shopping. The stair swallows the sound of her struggling up behind you, and by the top you've half-forgotten her. Almost.",
    "You pass her by with a small nod — not unkind, exactly, just busy. You've your own long day to save, and no room in it for a stranger's shopping. The stair swallows the sound of her struggling up behind you, and by the time you reach the top you've very nearly forgotten her. Almost, but not quite."),
  [t("Back to the day.", "Back to the day.", "On, back to the day."),
   t("Into the square.", "Into the square.", "Into the square, then.")])

P(79,
  t("You go back to the day. The good turn leaves a small warmth. Passing by leaves a small guilt. Either way, it goes with you. It is a little thing. But little things add up, in a city, into who you are in it. The light is starting, slowly, to change.",
    "You go back to the day, the small warmth of the good turn — or the small guilt of passing by — going with you either way. It's a little thing. But little things add up, in a city, into who you turn out to be in it. The light is beginning, slowly, to change.",
    "You go back to the day, and the small warmth of the good turn — or, if you passed on, the small cold guilt of it — goes with you either way. It's a little thing, easily forgotten. But little things add up, in a strange city, into who you turn out to be in it. The light is beginning, slowly and surely, to change toward evening."),
  [t("Think toward the evening.", "Think toward the evening.", "Turn your thoughts toward the evening."),
   t("Back to Halloran's at dusk.", "Back to Halloran's block at dusk.", "Back toward Halloran's block for dusk.")])

P(92,
  t("You offer to mind the child while she wrestles the bags. The child takes your hand and holds it, solemn and trusting, the way small children do. It is a tiny trust, freely given, and it warms you more than you expect. Together, the three of you make slow progress up.",
    "You offer to mind the child while she wrestles the bags. The child takes your hand and holds it, solemn and trusting, the way small children do without thinking. It's a tiny trust, freely given, and it warms you more than you'd expect. Together, the three of you make slow progress up.",
    "You offer to mind the child while she wrestles the splitting bags. The child takes your hand at once and holds it, solemn and entirely trusting, the way small children give their trust without thinking to weigh it. It's a tiny thing, freely given, and it warms you rather more than you'd expect it to. Together, the three of you make slow, careful progress up the stairs."),
  [t("See them both safely up.", "See them both safely up.", "See them both safely up to the top."),
   t("Hand the child back; hurry on.", "Hand the child back and hurry on.", "Hand the child back, and hurry on.")])

# --- Dania ---
P(90,
  t("Dania wants to see a place round the corner first. You go with her. It is small, and dark, and not right for her. But she has to see it to know that. This is how looking works. You walk it with her. Two lost people are still two, and that helps.",
    "Dania wants to see a place round the corner first, so you go with her. It's small and dark and not right for her — but she has to see it to know that; this is how looking works. You walk it with her anyway. Two lost people are still two, and that helps a little.",
    "Dania wants to see a place round the corner first, so you go along with her. It's small, and dark, and plainly not right for her — but she has to see it with her own eyes to know that, because this is simply how the looking works. You walk it with her anyway, uncomplaining. Two lost people are still, at least, two, and on a day like this that helps more than a little."),
  [t("On to the canal room after.", "On to the canal room after.", "On to the canal room after this."),
   t("She's found something; you haven't.", "She's found something; you're still looking.", "She's found something of her own; you're still looking.")])

P(91,
  t("Dania takes a small room she likes, and hugs you goodbye. You are glad for her, honestly glad. But when she is gone, the day feels wider and colder. You are more alone in it than before. One of you has a home tonight. The other is still walking.",
    "Dania takes a small room she likes and hugs you goodbye. You're glad for her — honestly glad. But once she's gone the day feels wider and colder, and you're more alone in it than before. One of you has a home tonight. The other is still walking the streets.",
    "Dania takes a small room she likes the look of, and hugs you goodbye on the pavement. You're glad for her — honestly, uncomplicatedly glad. But once she's gone the day feels suddenly wider and colder, and you're more alone in it than you were before you met her this morning. One of you has a home tonight. The other is still out walking the streets."),
  [t("Back to the square.", "Back to the square.", "Head back to the square."),
   t("On to the evening.", "On to the evening.", "On, then, to the evening."),
   t("She texts you a listing.", "She texts you a listing to try.", "She texts you a listing to try before it goes.")])

P(118,
  t("Dania's text comes through: a room near hers, going tonight. It is kind of her to think of you. But \"going tonight\" is a hard promise to catch. Her part of the city is a long, cold way from here. It is probably gone already. Probably. But maybe not.",
    "Dania's text comes through: a room near hers, going tonight. Kind of her to think of you. But 'going tonight' is a hard promise to catch, and her part of the city is a long cold way off. It's probably gone already. Probably. But maybe not.",
    "Dania's text comes through: a room near hers, going tonight. It's kind of her to have thought of you at all. But 'going tonight' is a very hard promise to catch, and her part of the city is a long, cold way from where you're standing. It's probably gone already. Probably. But then again — maybe, just maybe, not."),
  [t("Think toward the evening.", "Think toward the evening.", "Turn your mind toward the evening."),
   t("Chase it. Back to the square.", "Back to the square to chase it.", "Head back to the square to chase it down.")])

P(117,
  t("You read Vann's receipt again, slowly. The company name means nothing; you cannot find it anywhere. The phone number rings and rings and no one answers. The cold doubt in you hardens into something worse, something like knowing. You gave that man most of a week's pay for a piece of paper.",
    "You read Vann's receipt again, slowly. The company name means nothing — you can't find it listed anywhere — and the phone number just rings and rings. The cold doubt hardens into something worse, something like knowledge. You gave that man most of a week's pay for a slip of paper.",
    "You read Vann's receipt over again, slowly this time. The company name means nothing — you can't find it listed anywhere at all — and the phone number simply rings and rings into silence. The cold doubt in your chest hardens into something worse, something uncomfortably like knowledge. You gave that man most of a week's pay in exchange for a printed slip of paper."),
  [t("Try to salvage the day.", "Try to salvage the day.", "Try to salvage what's left of the day."),
   t("Face the evening with it.", "Face the evening with it.", "Face the evening with it as it is.")])


# ============================ apply ========================================
def main():
    book = json.load(open(BOOK, encoding="utf-8"))
    by_id = {n["id"]: n for n in book["nodes"]}
    applied, choice_mismatch = 0, []
    for nid, p in PROSE.items():
        n = by_id.get(nid)
        if not n:
            print(f"!! node {nid} not in book", file=sys.stderr); continue
        n["text"] = p["text"]
        chs = n.get("choices") or []
        pcs = p.get("choices") or []
        if len(chs) != len(pcs):
            choice_mismatch.append((nid, len(chs), len(pcs)))
            continue
        for c, pc in zip(chs, pcs):
            c["text"] = pc
        applied += 1
    json.dump(book, open(BOOK, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"Applied prose to {applied} node(s).")
    if choice_mismatch:
        print("CHOICE COUNT MISMATCH (fix these):")
        for nid, a, b in choice_mismatch:
            print(f"  §{nid}: book has {a} choices, prose has {b}")


if __name__ == "__main__":
    main()
