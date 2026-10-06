#!/usr/bin/env python3
"""Fix choices that narrated an event instead of offering the reader a decision.

Some connector choices added while building the skeleton read as narration ("She shows
you into her office", "The agency man notices you watching") rather than an action the
reader chooses. This rewrites each into a real reader choice, at all three levels. Targets
are matched by (node id, goto) so the graph is unchanged — only the choice wording.
"""
import json, os

EP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "episode-01.json")
book = json.load(open(EP, encoding="utf-8"))
by = {n["id"]: n for n in book["nodes"]}

# (node, goto) : {A2, B1, B2}
FIX = {
 (35, 85):  ("Follow her into her office.", "Follow her into her office.", "Follow her through into her office."),
 (35, 120): ("Let her ask you questions first.", "Let her ask her questions first.", "Let her put her questions to you first."),
 (84, 35):  ("Ask to see Ms Rowe.", "Ask to see Ms Rowe.", "Ask whether you can see Ms Rowe."),
 (84, 37):  ("Leave your name and go.", "Leave your details and go.", "Leave your details and step back out."),
 (84, 91):  ("Talk to the person waiting with you.", "Talk to the candidate waiting beside you.", "Strike up a word with the candidate beside you."),
 (85, 86):  ("Ask about the letter on the desk.", "Ask about the letter on the desk.", "Ask her about the letter squared on the desk."),
 (85, 120): ("Talk about yourself instead.", "Talk about yourself instead.", "Turn the talk to yourself instead."),
 (85, 92):  ("Look out at the river.", "Look out at the river.", "Look out at the river a moment."),
 (86, 94):  ("Ask who sends the old address.", "Ask who keeps sending the old address.", "Ask who has been sending the old address."),
 (94, 141): ("Offer to fix the letters yourself.", "Offer to fix the letters yourself.", "Offer to be the one who fixes the letters."),
 (94, 37):  ("Say nothing, and talk about the job.", "Let it drop, and talk about the job.", "Let the matter drop, and turn to the job."),
 (60, 107): ("Watch the woman in front of you.", "Watch what the woman ahead of you does.", "Watch what the woman near the front decides."),
 (68, 90):  ("Let him see that you saw him.", "Let him see that you have seen him.", "Hold his eye, and let him know you saw."),
 (120, 37): ("Say you are too tired to talk much.", "Admit you are too tired to say much.", "Admit that, after the night, you can barely speak."),
}

fixed = 0
for (nid, goto), (a2, b1, b2) in FIX.items():
    for c in by[nid]["choices"]:
        if c.get("goto") == goto:
            c["text"] = {"A2": a2, "B1": b1, "B2": b2}
            fixed += 1
            break
    else:
        print(f"  WARNING: no choice §{nid}→{goto}")

json.dump(book, open(EP, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(f"Rewrote {fixed} narration-style choices into reader decisions.")
