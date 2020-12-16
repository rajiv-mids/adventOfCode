#!/home/rajivn/anaconda3/bin/python
from collections import defaultdict
import operator
import numpy as np

with open("/home/rajivn/adventOfCode/16/input", "r") as inp:
    lines = inp.read()

sections = lines.split("\n\n")
rules = defaultdict(set)
for line in sections[0].split("\n"):
    rule, det = line.split(":")
    for r in det.split(" or "):
        st, en = r.strip().split("-")
        st, en = int(st), int(en)
        for x in range(st, en+1):
            rules[rule].add(int(x))

invalid = []

def is_inv(k):
    found = False
    for rule in rules.values():
        if k in rule:
            found = True
            break
    return not found

valid_t = []
for line in sections[2].split("\n")[1:]:
    inv = [int(k) for k in line.split(",") if is_inv(int(k))]
    if len(inv) == 0:
        valid_t.append([int(k) for k in line.split(",")])
    invalid.extend(inv)

print("part1", sum(invalid) )

# identify set of rules that each field satisfies
# we start with all rules for each field and remove as we find rules that do not match. 
# We should be left with at least one section with one rule. Then remove from rest of fieldd

f_rules = defaultdict(set) # rule name: set of rules

# initialize
for col in range(len(rules.keys())):
    f_rules[col] = set(list(rules.keys()))

for ticket in valid_t:
    for col, val in enumerate(ticket):
        for rule in list(f_rules[col]):
            if val not in rules[rule]:
                f_rules[col].remove(rule)

# order by column that matches least rules
ord_rules = sorted([(rule, len(f_rules[rule])) for rule in f_rules.keys()], key=operator.itemgetter(1))

removed = True
final_set = {}
while removed:
    removed = False
    for col, cnt in ord_rules:
        if cnt == 1:
            final_set[list(f_rules[col])[0]] = col
        else:
            [f_rules[col].remove(r) for r in final_set.keys() if r in f_rules[col]]
            removed = True

    ord_rules = sorted([(rule, len(f_rules[rule])) for rule in f_rules.keys()], key=operator.itemgetter(1))

cols = set([final_set[key] for key, col in final_set.items() if key.startswith("departure")])
myticket = sections[1].split("\n")[1:][0]
myticket = [int(val) for col, val in enumerate(myticket.split(",")) if col in cols]
print("part2", np.prod(myticket))