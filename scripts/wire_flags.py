#!/usr/bin/env python3
"""Make the state model earn its keep: give the inert flags real gated payoffs, and
declare the genuine arc-carriers so the validator knows they are meant to be unread here.

- knows_river: was set 23× and read 0×. Now gates a real shortcut to the river at two
  moments (§17 morning regroup, §14 the long walk back), rewarding the reader who noticed.
- rough_night: was set 5× and read 0×. Now gates a tired-out option at the interview (§120)
  and the give-up-on-the-bench ending (§22 → §147).
- paid_scam, told_truth, knows_name, dodged_scam: declared arc-carriers (they are read by
  the next book via state_in), so being lightly-read here is intentional, not a smell.
"""
import json, os

EP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "episode-01.json")
book = json.load(open(EP, encoding="utf-8"))
by = {n["id"]: n for n in book["nodes"]}

# flags whose job is to carry into episode 2 (read via that book's state_in), so it is
# fine for them to gate little or nothing within this book.
book["arc_flags"] = ["dodged_scam", "told_truth", "knows_name", "paid_scam"]

def lv(a, b1, b2): return {"A2": a, "B1": b1, "B2": b2}

def add_gate(nid, text, goto, requires):
    by[nid]["choices"].append({"text": text, "goto": goto, "requires": requires})

def gate_existing(nid, goto, requires):
    for c in by[nid]["choices"]:
        if c.get("goto") == goto:
            c["requires"] = requires; return
    raise KeyError(f"§{nid}→{goto} not found")

# --- knows_river payoffs (a shortcut for the reader who learned they moved to the river) ---
# placed on nodes with spare room (§17 is already at four choices), so no node exceeds 2–4.
add_gate(8, lv("You know it is by the river. Head straight there and wait for light.",
              "You know they are by the river — head straight there and wait for morning.",
              "You know now that they are by the river; head straight there and wait out the dark."),
         23, ["knows_river"])
add_gate(14, lv("Head for the river you were told about.",
               "Make straight for the river you were told about.",
               "Cut your losses and make straight for the river you were told about."),
         23, ["knows_river"])

# --- rough_night payoffs (the night catches up with you) ---
add_gate(120, lv("You are too tired to say much.",
                "You are too tired, after the night, to make your case.",
                "After the night you have had, you can barely keep your eyes open, let alone make a case."),
         37, ["rough_night"])
gate_existing(22, 147, ["rough_night"])   # you only give up on the bench if the night broke you

json.dump(book, open(EP, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("Wired knows_river (§8,§14→23) and rough_night (§120→37, §22→147); "
      "declared arc_flags:", book["arc_flags"])
