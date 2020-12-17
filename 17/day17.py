from collections import defaultdict
from copy import deepcopy
import itertools
with open("/home/rajivn/adventOfCode/17/input", "r") as inp:
    lines = inp.read()
state = set()
for y, line in enumerate(lines.split()):
    for x, st in enumerate(line):
        if st == "#":
            state.add((x, y, 0))
mx, my, mz = [0,2],[0,2],[0,1]

def getminmax(states):
    _mx, _my, _mz = [0,0], [0,0], [0,0]
    for x,y,z in states:
        if x < _mx[0]: _mx[0] = x
        if y < _my[0]: _my[0] = y
        if z < _mz[0]: _mz[0] = z

        if x > _mx[1]: _mx[1] = x
        if y > _my[1]: _my[1] = y
        if z > _mz[1]: _mz[1] = z
    return _mx, _my, _mz

def printstates(states):
    print("=============")
    mx, my, mz = getminmax(states)
    for z in range(mz[0], mz[1]+1):
        print("z = ", z)
        for y in range(my[0], my[1]+1):
            for x in range(mx[0], mx[1]+1):
                if (x,y,z) in states:
                    print("#", end="")
                else:
                    print(".", end="")
            print("\n")
        print("\n")

print("original ")
printstates(state)

for step in range(6):
    newstate = deepcopy(state)
    neighbors = defaultdict(int)
    explore = set()
    for x, y, z in state:
        [explore.add((x+e,y+f,z+g)) for e in range(-1, 2) for f in range(-1, 2) for g in range(-1, 2) ]
    for x,y,z in explore:
        # check neighbor states
        n = [(e,f,g) for e in range(-1, 2) for f in range(-1, 2) for g in range(-1, 2) ]
        count=0
        for dx, dy, dz in n:
            if dx == 0 and dy == 0 and dz==0:
                continue
            count+=1
            if (x+dx, y+dy, z+dz) in state:
                neighbors[(x,y,z)] +=  1

        if (x, y, z) in state and neighbors[(x,y,z)] not in (2,3):
            if (x, y, z) in newstate: newstate.remove((x, y, z))

        if (x, y, z) not in state and neighbors[(x,y,z)] == 3:
            newstate.add((x, y, z))
    
    print("cycle = ", step+1)
    printstates(newstate)
    state = deepcopy(newstate)
print(len(state))