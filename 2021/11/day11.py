import os
from collections import defaultdict, deque
import numpy as np

path = os.path.dirname(os.path.abspath(__file__))
data = []

with open(path+"/input", "r") as inp:
    for r, row in enumerate(inp):
        data.append([])
        for c, col in enumerate(row.strip()):
            data[-1].append(int(col))

def isvalid(r,c,data):
    if r >= 0 and r < len(data) and c >= 0 and c < len(data[0]):
        return True
    return False

def checkallflash(data):
    nd = np.array(data)
    if nd.sum() == 0:
        return True
    return False

def dostep(data):
    flashed = set()
    flashes = 0
    myq = deque()
    for r, row in enumerate(data):
        for c, val in enumerate(row):
            data[r][c] = val+1
            if data[r][c] == 10:
                myq.appendleft((r,c))
    
    adj = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]    
    while len(myq) != 0:
        r, c = myq.popleft()

        for ar, ac in adj:
            nr, nc = r+ar, c+ac
            if isvalid(nr, nc, data) and (nr, nc) not in flashed:
                data[nr][nc] += 1
                if data[nr][nc] == 10:
                    myq.appendleft((nr, nc))
        flashes +=1
        flashed.add((r,c))
        data[r][c] = 0
    allflash = checkallflash(data)
    return allflash, flashes

totflash = 0
firstflash = None
for step in range(1000):
    allflash, flashes = dostep(data)
    totflash += flashes
    if not firstflash and allflash:
        firstflash = step+1
print("part 1", totflash)
print("part 2", firstflash)