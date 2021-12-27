import os
from collections import defaultdict, deque
part2 = True

path = os.path.dirname(os.path.abspath(__file__))

minpaths = dict()

grid = []
with open(path+"/input", "r") as inp:
    for line in inp:
        grid.append([int(x) for x in line.strip()])

o_dim = len(grid), len(grid[0])

if part2:
    row = [None for _ in range(len(grid[0]))]
    for r in grid:
        r.extend(row * 4)

    for i in range(1, 5):
        for row in range(o_dim[0]):
            for col in range(o_dim[1]):
                val = grid[row][col] + i
                if val >= 10:
                    val = (val % 10) +1
                    if val == 10:
                        val = 1

                grid[row][col+(i*o_dim[1])] = val
    d_row = [None for _ in range(len(grid[0]))]
    for i in range(1, 5):
        for row in range(o_dim[0]):
            for col in range(len(grid[0])):
                val = grid[row][col] + i
                if val >= 10:
                    val = (val % 10) +1
                    if val == 10:
                        val = 1
                r_num = row+(i*o_dim[0])
                if r_num >= len(grid):
                    grid.append(d_row[:])
                grid[r_num][col] = val

print(grid[-1])

start, end = (0,0), (len(grid)-1, len(grid[0])-1)

myq = deque()
myq.append((start, 0))

moves = [(-1,0), (0, 1), (1, 0), (0, -1)]
def checkbounds(r, c, grid):
    if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]):
        return True
    return False

while myq:
    curr, cost = myq.pop()
    #print(curr, cost)
    for move in moves:
        nr, nc = (move[0]+curr[0], move[1]+curr[1])
        if not checkbounds(nr, nc, grid):
            continue
        n_cost = grid[nr][nc] + cost
        if (nr, nc) not in minpaths:
            minpaths[(nr, nc)] = n_cost
            myq.appendleft(((nr, nc), n_cost))
            if (nr, nc) == end:
                pass
                #print(minpaths[end])
        elif n_cost < minpaths[(nr, nc)]:
            minpaths[(nr, nc)] = n_cost
            myq.appendleft(((nr, nc), n_cost))
            if (nr, nc) == end:
                pass
                #print(minpaths[end])

print("part 1", minpaths[end])