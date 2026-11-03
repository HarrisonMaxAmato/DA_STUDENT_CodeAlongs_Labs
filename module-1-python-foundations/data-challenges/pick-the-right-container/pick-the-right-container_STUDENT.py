#!/usr/bin/env python3
"""Pick the Right Container: see DataChallengeOverview&Steps.md."""

import json

DATA_FILE = "/Users/Marcy_Student/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/data/station_taps.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    rows = [line.split(",") for line in f.read().splitlines() if line]

header = rows[0]
taps = rows[1:]


# ===== Day 1 =====

# Step 1: Write `scan_for()` and Count Its Comparisons for Three Tap IDs
def scan_for(tap_id, records):
    comparisons = 0
    for row in records:
        comparisons += 1
        if row[0] == tap_id:
            return comparisons
    return comparisons
    # TODO: assign `comparisons` to 0
    # TODO: loop over `records`; add 1 to `comparisons` for every row
    # TODO: inside the loop, return `comparisons` when row[0] == tap_id
    # TODO: after the loop, return `comparisons`
    pass


print("columns:", header)
print("rows in the log:", len(taps))
print("comparisons to find T001:", scan_for("T001", taps))
print("comparisons to find T040:", scan_for("T040", taps))
print("comparisons to find T999:", scan_for("T999", taps))

# Step 1, answer 1:
# we can see that the number of comparisons made by the scan_for function is equal to the position of the tap_id in the records list. For T001, it is found at the first position, so it takes 1 comparison. For T040, it is found at the 40th position, so it takes 40 comparisons. For T999, which is not in the list, it takes 100 comparisons (the length of the list) before returning.
# Step 1, answer 2:
# we should plan for the worst case scenario, which is when the tap_id is not found in the records. In this case, the function will have to check every record, resulting in a number of comparisons equal to the length of the records list. Therefore, we should expect that the worst case scenario will require 100 comparisons.


# Step 2: Print Scan Cost at 5 to 40 Rows, Then Count a Nested Pair Loop
for size in [5, 10, 20, 40]:
    worst = scan_for("T999", taps[:size])
    print("rows:", size, "| worst-case comparisons:", worst)
Pairs = 0
for i in taps: 
    for j in taps:
        Pairs += 1
print(len(taps), Pairs)
big = len(taps) * 10
print("scan's worst case on", big, "rows:", scan_for("T999", taps[:big]))
    # TODO: print "rows:", `size`, "| worst-case comparisons:", `worst`
# TODO: assign `pairs` to 0; loop over `taps` with a loop over `taps` inside
# TODO: add 1 to `pairs` in the inner loop
# TODO: print len(taps) and `pairs`
# TODO: assign `big` to len(taps) * 10
# TODO: print the scan's worst case and the pair loop's count on `big` rows

# Step 2, answer 1:

#in the first loop, we are checking the worst-case comparisons for different sizes of the taps list. As the size increases, the number of comparisons also increases linearly. For example, with 5 rows, it takes 5 comparisons; with 10 rows, it takes 10 comparisons; and so on. This shows that the scan_for function has a linear time complexity of O(n) in the worst case.
# Step 2, answer 2:
we are counting the number of pairs of taps using a nested loop. the amount of pairs is equal to the swuare of the number of taps, in this case 10000 which comes from 100^2.
#


# ===== Day 2 =====

# Step 3: Count Taps Per Card With Two Parallel Lists, and Their Comparisons
# TODO: assign `card_ids` to an empty list (each card, first-seen order)
# TODO: assign `tap_counts` to an empty list (the count for card_ids[i])
# TODO: assign `comparisons` to 0
# TODO: loop over `taps`; assign `card` to row[1] and `found` to False
# TODO: inside it, loop over range(len(card_ids)); add 1 to `comparisons`
# TODO: if card_ids[i] == card, add 1 to tap_counts[i], set found, break
# TODO: after the inner loop, if not found, append `card` and 1 to the lists
card_ids = []
tap_counts = []
comparisons = 0
for row in taps:
    card = row[1]
    found = False
    for i in range(len(card_ids)):
        comparisons += 1
        if card_ids[i] == card:
            tap_counts[i] += 1
            found = True
            break
    if not found:
        card_ids.append(card)
        tap_counts.append(1)
'''busiest = tap_counts.index(max(tap_counts))
print("distinct cards:", len(card_ids))
print("comparisons the two parallel lists needed:", comparisons)
print("busiest card:", card_ids[busiest], "with", max(tap_counts), "taps")'''

# Step 3, answer 1:
# i expected the number of comparisons to be equal to the number of taps, since we are checking each tap against the list of card_ids. However, the actual number of comparisons is higher because for each new card, we have to check against all previously seen cards, leading to a quadratic growth in comparisons as more unique cards are added.
#



# Step 4: Count Taps Per Card With a Dictionary, and Stations With a Set
# TODO: assign `taps_by_card` to an empty dict (card ID: tap count)
# TODO: assign `lookups` to 0
# TODO: loop over `taps`; add 1 to `lookups`
# TODO: add 1 to row[1]'s count in `taps_by_card`, or set it to 1 if new
# TODO: assign `stations` to set(); loop over `taps` and .add() row[2]
# TODO: assign `repeat_riders` to 0
# TODO: loop over `taps_by_card`; add 1 to `repeat_riders` if a count is > 1
taps_by_card = {}
lookups = 0
for row in taps:
    lookups += 1
    card = row[1]
    if card in taps_by_card:
        taps_by_card[card] += 1
    else:
        taps_by_card[card] = 1
for row in taps:
    stations = set()
    stations.add(row[2])
repeat_riders = 0
for count in taps_by_card.values():
    if count > 1:
        repeat_riders += 1   

print("distinct cards:", len(taps_by_card))
print("lookups the dictionary needed:", lookups)
print("unique stations:", len(stations), sorted(stations))
print("cards that tapped more than once:", repeat_riders)
print("taps for C001:", taps_by_card["C001"])

# Step 4, answer 1:
# the rule behind the number of lookups is that it is equal to the number of taps, since we are checking each tap against the dictionary. Each tap results in one lookup, regardless of whether the card is new or already exists in the dictionary.
# Step 4, answer 2:
# As the input size grows, the number of lookups will grow linearly with the number of taps. This is because each tap results in a single lookup in the dictionary, so if the number of taps doubles, the number of lookups will also double. The time complexity for this operation is O(n), where n is the number of taps.
# Step 4, answer 3:
# 
# Step 4, answer 4:
# The card that explains the gap is C001, which has 3 taps. This card is the only one that tapped more than once, and it accounts for the difference between the total number of distinct cards and the number of cards that tapped more than once. The other cards each tapped only once, so they do not contribute to the count of repeat riders.
# ===== Day 3 =====

# Step 5: Save the Summary as JSON and Read the TypeError a Set Causes
# TODO: replace each None with your Day 2 value; keep `stations` a set
summary = {
    "service_day": "2026-03-02",
    "total_taps": None,
    "distinct_cards": None,
    "stations": None,
    "taps_by_card": None,
}

print("about to serialize", len(summary), "keys")
# TODO: run the file and answer below before you change anything
# TODO: then put # in front of the next two lines so Step 6 can run
text = json.dumps(summary, indent=2)
print(text)
#with open("tap_summary.json", "w") as f:
#    json.dump(summary, f, indent=2)

# Step 5, answer 1:
# TypeError: Object of type set is not JSON serializable
# Step 5, answer 2:
#The set called stations caused it, because JSON doesn't support sets.
# Step 5, answer 3:
#Yes it printed before because the json file can handle dict but not the set.


# Step 6: Write `tap_summary.json`, Reload It, and Check Which Types Survived
# TODO: assign summary["stations"] to a type JSON can hold; keep the key
# TODO: json.dump() `summary` into a with open("tap_summary.json", "w")
# TODO: replace None with json.load() of "tap_summary.json"
reloaded = None

summary["stations"] = list(stations)
with open("tap_summary.json", "w") as f:
    json.dump(summary, f, indent=2)
print("total_taps came back as:", reloaded["total_taps"])
print("taps_by_card came back as a", type(reloaded["taps_by_card"]).__name__)
print("C001 straight out of the file:", reloaded["taps_by_card"]["C001"])
print("stations came back as a", type(reloaded["stations"]).__name__)
print("round trip identical:", reloaded["taps_by_card"] == taps_by_card)

# Step 6, answer 1:
#Yes, because we already calculated how many total taps one card has (like c001) this new code only stores the results from the summary and not the taps we used in day 1
# Step 6, answer 2:
# Taps_by_card survived the round trip
# Stations came back as a list because JSON can't write a set, so it had to change into a list.
