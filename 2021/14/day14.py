import os
import re
from collections import Counter, defaultdict, deque

path = os.path.dirname(os.path.abspath(__file__))
data = []
input = None
rules = dict()
with open(path+"/input", "r") as inp:
    for line in inp:
        if line.strip() == "":
            continue
        if "->" in line:
            l, r = line.strip().split(" -> ")
            rules[l] = r
        else:
            input = line.strip()


def construct(inp):
    lmap = defaultdict(int)
    prev = None
    for ch in inp:
        if prev is not None:
            lmap[prev + ch]+=1
        prev = ch
    return lmap

map = construct(input)
for step in range(40):
    print("step", step)
    newmap = defaultdict(int)
    # get all nodes which match eacn rule
    for rule, ins in rules.items():
        if rule not in map:
            continue
        a, b = rule
        newmap[a+ins] += map[rule]
        newmap[ins+b] += map[rule]
        # remove old entry from map
        map.pop(rule)
    # update map to indicate new splits
    for k, v in newmap.items():
        if k in map:
            map[k] += v
        else:
            map[k] = v


counts = defaultdict(int)
for c, v in map.items():
    for a in c:
        counts[a] += v

counts = {k:v//2 for k, v in counts.items()}
counts[input[0]]+=1
counts[input[-1]]+=1
counts = {v:k for k, v in counts.items()}

print("part2", max(sorted(counts)) - min(sorted(counts)))
