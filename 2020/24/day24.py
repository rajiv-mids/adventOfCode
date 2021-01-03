#!/home/rajivn/anaconda3/bin/python
from collections import defaultdict
from copy import deepcopy
with open("/home/rajivn/adventOfCode/24/input", "r") as inp:
    input = inp.readlines()

tiles = defaultdict(int)

DIR1={"se":(1, -1), "sw":(-1, -1),  "nw":(-1, 1), "ne":(1, 1)}
DIR2={"e":(1,0),"w":(-1, 0)}

def move(x, y, z, dir):
    if dir in DIR2:
        return (x+DIR2[dir][0], y, z)
    if z == 0:
        if dir in ("sw", "nw"):
            return (x, y+DIR1[dir][1], 1)
        return (x+DIR1[dir][0], y+DIR1[dir][1], 1)
    else:
        if dir in ("se", "ne"):
            return (x, y+DIR1[dir][1], 0)
        return (x+DIR1[dir][0], y+DIR1[dir][1], 0)

for line in input:
    i = 0
    cur_tile = [0,0,0]
    line = line.strip()
    while i < len(line):
        if i+2 <= len(line) and line[i:i+2] in DIR1:
            dir = line[i:i+2]
            i+=2
        elif line[i] in DIR2:
            dir = line[i]
            i+=1
        cur_tile = move(*cur_tile, dir)
    f_tile = tuple(cur_tile)
    tiles[tuple(cur_tile)] = 1 if tiles[tuple(cur_tile)] == 0 else 0
print("part1", sum( tiles.values()))

# part 2
daycount = 0
tiles = dict(tiles) # this is required since lookups can cause length of defaultdict to change    

for i in range(100):
    newtiles = defaultdict(int, tiles)
    # go through each black tile
    adjblack = defaultdict(int) # key = black cell, value = count of blacks adjacent
    adjwhite = defaultdict(int) # key = white cell, value = count of blacks adjacent

    for x, y, z in tiles.keys():
        # get all adjacent tiles
        if tiles[(x,y,z)] == 0:
            continue
        adj = [move(x,y,z, dir) for dir in DIR1 ]
        adj += [move(x,y,z, dir) for dir in DIR2]
        # count adjacent blacks and update counts of adjacent whites
        for (xa, ya, za) in adj:
            adjblack[(x, y, z)] += tiles.get((xa, ya, za), 0)
            if tiles.get((xa, ya, za), 0) == 0:
                adjwhite[(xa, ya, za)] += tiles.get((x, y, z), 0)

    # zero or more than 2 black tiles immediately adjacent to it is flipped to white
    for (xa, ya, za), count in adjblack.items():
        if count == 0 or count > 2:
            newtiles[(xa, ya, za)] = 0
    
    # white tile with exactly 2 black tiles immediately adjacent to it is flipped to black
    for (xa, ya, za), count in adjwhite.items():
        if count == 2:
            newtiles[(xa, ya, za)] = 1

    tiles = dict(newtiles)
    #print("after day ", daycount+1, " black count = ", sum(tiles.values()))
    daycount += 1
print("part2", sum(tiles.values()))