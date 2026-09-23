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
