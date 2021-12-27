import os
import re
import pandas as pd

path = os.path.dirname(os.path.abspath(__file__))
dotmap = set()
instx = []
bounds = [0, 0]
with open(path+"/input", "r") as inp:
    for line in inp:
        if line.strip() == "":
            continue
        if "," in line:
            x, y = line.strip().split(",")
            x,y = int(x), int(y)
            if x > bounds[0]:
                bounds[0] = x
            if y > bounds[1]:
                bounds[1] = y
            dotmap.add((x,y))
        else:
            nums = re.findall(r"\d+", line)
            num = int(nums[0])
            if line.find("x=") != -1:
                instx.append(("x", num))
            if line.find("y=") != -1:
                instx.append(("y", num))

def splitx(dotmap, sx):
    rmap = set()
    for x,y in dotmap:
        tx = 0
        if x > sx:
            tx = sx - (x - sx)
        else:
            tx = x
        rmap.add((tx, y))
    return rmap

def splity(dotmap, sy):
    rmap = set()
    for x,y in dotmap:
        ty = 0
        if y > sy:
            ty = sy - (y - sy)
        else:
            ty = y
        rmap.add((x, ty))
    return rmap

p1 = None
for ins in instx:
    splitfn = splitx if ins[0] == "x" else splity
    dm2 = splitfn(dotmap, ins[1])
    if not p1:
        p1 = len(dm2)
    dotmap = dm2

maxx = max ([x for x,y in dm2])
maxy = max ([y for x,y in dm2])

grid = [[None]*(maxx+1) for r in range(maxy+1)]
for x,y in dm2:
    grid[y][x] = 1
grid = pd.DataFrame(grid)
grid.to_csv("out.csv")

print("part 1:", p1)
