#!/home/rajivn/anaconda3/bin/python
from collections import deque, defaultdict
import re
rules_inv = defaultdict(set)
rules = defaultdict(set)

with open("/home/rajivn/adventOfCode/07/input", "r") as input:
    for rule in input.readlines():
        cont, r = rule.split("contain")
        cont = cont.replace("bags", "")
        b_t = r.split(",")
        for b in b_t:
            if b.find("no other") != -1 :
                continue
            x = re.sub(r"\d+", "", b).replace("bags", "").replace("bag", "").replace(".","").strip()
            rules_inv[x].add(cont.strip())
            x = b.replace("bags", "").replace("bag", "").replace(".","").strip()
            num = re.findall(r"\d+", x)[0]
            x = re.sub(r"\d+", "", x).strip()
            rules[cont.strip()].add((x, int(num)))

bag_cols = set()
myq = deque()
# part 1
myq.append("shiny gold")
while len(myq) > 0:
    col = myq.pop()
    if col in rules_inv:
        myq.extend(rules_inv[col])
        [bag_cols.add(c) for c in rules_inv[col]]

print("part 1", len(bag_cols))

# part 2
myq.append(("shiny gold", 1))
tot = 0
while len(myq) > 0:
    col, cnt = myq.pop()
    if col in rules:
        for bg, num in rules[col]:
            t = cnt*num
            myq.append((bg, t))
            tot += t
print("part 2", tot)