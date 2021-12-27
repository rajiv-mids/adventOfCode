import os
from collections import deque

path = os.path.dirname(os.path.abspath(__file__))
data = []
with open(path+"/input", "r") as inp:
    for row in inp:
        data.append(row.strip())
points = {")":3, "]":57, "}":1197, ">":25137}
pointsp2 = {")":1, "]":2, "}":3, ">":4}

pairs = {")":"(", "]":"[", "}":"{", ">":"<"}
pair_rev = {v: k for k, v in pairs.items()}
totscore = 0
scores = []
for line, row in enumerate(data):
    mys = deque()
    for ch in row:
        if ch in "([{<":
            mys.appendleft(ch)
        else:
            if len(mys) == 0 or mys[0] != pairs[ch]:
                totscore += points[ch]
                #print(line, mys, ch)
                break
            else:
                mys.popleft()
    else:
        missing = "".join([pair_rev[c] for c in mys] ) 
        score = 0
        for ch in missing:
            score *= 5
            score += pointsp2[ch]
        scores.append(score)
print("part1", totscore)
print("part2", sorted(scores)[len(scores)//2])