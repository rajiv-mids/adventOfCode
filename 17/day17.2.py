from collections import defaultdict
from copy import deepcopy
import itertools
with open("/home/rajivn/adventOfCode/17/input", "r") as inp:
    lines = inp.read()
state = set()
for y, line in enumerate(lines.split()):
    for x, st in enumerate(line):
        if st == "#":
            state.add((x, y, 0, 0))
mx, my, mz, mw = [0,2],[0,2],[0,1],[0,1]

for step in range(6):
    newstate = deepcopy(state)
    neighbors = defaultdict(int)
    explore = set()
    for x, y, z, w in state:
        [explore.add((x+e,y+f,z+g, w+h)) for e in range(-1, 2) for f in range(-1, 2) for g in range(-1, 2) for h in range(-1, 2)]

    for x,y,z,w in explore:
        # check neighbor states
        n = [(e,f,g,h) for e in range(-1, 2) for f in range(-1, 2) for g in range(-1, 2) for h in range(-1, 2)]
        count=0
        for dx, dy, dz, dh in n:
            if dx == 0 and dy == 0 and dz==0 and dh == 0:
                continue
            count+=1
            if (x+dx, y+dy, z+dz, w+dh) in state:
                neighbors[(x,y,z,w)] +=  1

        if (x, y, z, w) in state and neighbors[(x,y,z,w)] not in (2,3):
            if (x, y, z, w) in newstate: newstate.remove((x, y, z, w))

        if (x, y, z, w) not in state and neighbors[(x,y,z,w)] == 3:
            newstate.add((x, y, z, w))    
    print("cycle = ", step+1)
    state = deepcopy(newstate)
print(len(state))