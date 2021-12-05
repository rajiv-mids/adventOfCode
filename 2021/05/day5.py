import os
from collections import defaultdict
import numpy

def getEquidistantPoints(p1, p2, parts):
    return zip(numpy.linspace(p1[0], p2[0], parts+1),
               numpy.linspace(p1[1], p2[1], parts+1))

path = os.path.dirname(os.path.abspath(__file__))
with open(path+"/input", "r") as inp:
    data = inp.readlines()

def buildcoords(line, coords):
    c1, c2 = line.split("->")
    c1, c2 = c1.strip(), c2.strip()
    x1, y1 = c1.split(",")
    x1, y1 = int(x1), int(y1)
    x2, y2 = c2.split(",")
    x2, y2 = int(x2), int(y2)

    if x1 == x2: #vertical line
        rang = range(y1, y2+1) if y1<=y2 else range(y2, y1+1)
        for y in rang:
            coords[(x1, y)] +=1
    elif y1 == y2: #horizontal line
        rang = range(x1, x2+1) if x1<=x2 else range(x2, x1+1)
        for x in rang:
            coords[(x, y1)] +=1
    else: #diagonal
        xdir, ydir = 0, 0
        xdir = 1 if x1 < x2 else -1
        ydir = 1 if y1 < y2 else -1
        cur = (x1, y1)
        coords[cur] += 1
        while cur != (x2, y2):
            cur = (cur[0]+xdir, cur[1]+ydir)
            coords[cur] += 1

coords = defaultdict(int)

for line in data:
    buildcoords(line, coords)
print(sum([1 for cnt in coords.values() if cnt >=2]))