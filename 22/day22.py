#!/home/rajivn/anaconda3/bin/python
from collections import deque
import copy
players = None
with open("/home/rajivn/adventOfCode/22/input", "r") as inp:
    players = inp.read().split("\n\n")
players[0] = deque([int(x) for x in players[0].split("\n")[1:]])
players[1] = deque([int(x) for x in players[1].split("\n")[1:]])

def part1(p1, p2):
    while len(p1) > 0 and len(p2) > 0:
        a, b = p1.popleft(), p2.popleft()
        if a > b:
            p1.append(a)
            p1.append(b)
        else:
            p2.append(b)
            p2.append(a)
    return p1 if len(p1) > 0 else p2

def to_str(cards):
    return "".join([str(c) for c in cards])

def rcombat(p1, p2, prior1, prior2, depth):
    round = 0
    while True:
        round += 1
        if to_str(p1) in prior1 or to_str(p2) in prior2:
            return 1, p1
        prior1.add(to_str(p1))
        prior2.add(to_str(p2))
        a, b = p1.popleft(), p2.popleft()
        if a <= len(p1) and b <= len(p2):
            p1c = deque(list(p1)[:a])
            p2c = deque(list(p2)[:b])
            winner, _ = rcombat(p1c, p2c, set(), set(), depth+1)
        else:
            winner = 1 if a > b else 2
        if winner == 1:
            p1.append(a); p1.append(b)
        else:
            p2.append(b); p2.append(a)
        if len(p1) == 0:
            return 2, p2
        if len(p2) == 0:
            return 1, p1


winner = part1(copy.copy(players[0]), copy.copy(players[1]))
print("part1", sum([(i+1)*v for i, v in enumerate(reversed(winner))]))

_, winner = rcombat(copy.copy(players[0]), copy.copy(players[1]), set(), set(), 0)
print("part2", sum([(i+1)*v for i, v in enumerate(reversed(winner))]))