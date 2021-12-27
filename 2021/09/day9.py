import os
from collections import deque

path = os.path.dirname(os.path.abspath(__file__))
data = []
with open(path+"/input", "r") as inp:
    for row in inp:
        data.append([])
        for col in row.strip():
            data[-1].append(int(col))

def isvalid(r,c, data):
    if r >= 0 and c >= 0 and r < len(data) and c <len(data[0]):
        return True
    return False

def isvalid_basin(pr, pc, r,c, data):
    if r >= 0 and c >= 0 and r < len(data) and c <len(data[0]):
        if data[r][c] != 9 and data[pr][pc] < data[r][c]:
            return True
        return False
    return False

totrisk = 0
low_coords = set()

for r, row in enumerate(data):
    for c, col in enumerate(row):
        neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        for rn, rc in neighbors:
            nr, nc = (r+rn, c+rc)
            if isvalid(nr, nc, data):
                if data[nr][nc] <= col:
                    break
        else:
            totrisk += col + 1
            low_coords.add((r,c))

def find_connected(ri,ci, data):
    # use bfs to find all connected low points
    myq = deque()
    myq.append((ri,ci))
    tot = 0
    visited = set()
    visited.add((ri,ci))
    while (len(myq) > 0):
        r,c = myq.pop()
        tot += 1
        neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        for rn, rc in neighbors:
            if (r+rn, c+rc) not in visited and isvalid_basin(r, c, r+rn, c+rc, data):
                myq.append((r+rn, c+rc))
                visited.add((r+rn, c+rc))

    return tot

sizes = []
print(low_coords)
while len(low_coords) > 0:
    vr, vc = low_coords.pop()
    size = find_connected(vr, vc, data)
    print(size)
    sizes.append(size)

sizes = sorted(sizes, reverse=True)
print("part 1", totrisk)
print("part 2", sizes[0]*sizes[1]*sizes[2])