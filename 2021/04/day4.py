import os
from collections import defaultdict

path = os.path.dirname(os.path.abspath(__file__))
with open(path+"\input", "r") as inp:
    data = inp.readlines()

def buildgrids(data, x):
    # read 5 lines starting from x and build grid
    grid = data[x:x+5]
    g1, g2 = defaultdict(list), dict()
    for r, line in enumerate(grid):
        line = line.strip().split()
        for c, val in enumerate(line):
            g1[val].append((r, c))
            g2[(r,c)] = val
    return g1, g2

def play(val, gridlist):
    remain = []
    for grid1, grid2 in gridlist:
        if val in grid1:
            matches = grid1[val]
            for row, col in matches:
                grid2.pop((row, col))
        remain.append((grid1, grid2))
    return remain

def checkifwin(grid):
    # check all rows
    for r in range(5):
        for c in range(5):
            if (r,c) in grid:
                break
        else:
            return grid
    # check all columns
    for c in range(5):
        for r in range(5):
            if (r,c) in grid:
                break
        else:
            return grid

def calc_win(grid, draw):
    tot = 0
    for v in grid.values():
        tot+=int(v)
    return int(draw)*tot

def part1():
    draws = data[0]
    gridlist = []
    for i in range(2, len(data), 6):
        grid1, grid2 = buildgrids(data,i)
        gridlist.append((grid1, grid2))

    # read in draws
    for draw in draws.strip().split(","):
        remain = play(draw, gridlist)
        w_found = False
        for grid1, grid2 in remain:
            w_grid = checkifwin(grid2)
            if w_grid is not None:
                print( "winner = ", calc_win(w_grid, draw))
                w_found = True
                break
        if w_found:
            break


def part2():
    draws = data[0]
    gridlist = []
    for i in range(2, len(data), 6):
        grid1, grid2 = buildgrids(data,i)
        gridlist.append((grid1, grid2))

    # read in draws
    for draw in draws.strip().split(","):
        remain = play(draw, gridlist)
        remove = set()
        for x, (grid1, grid2) in enumerate(gridlist):
            w_grid = checkifwin(grid2)
            if w_grid is not None:
                remove.add(x)
                winner = calc_win(w_grid, draw)
                if len(gridlist) == 1:
                    print("Final winner", winner)
                    break
        gridlist = [(g1,g2) for x, (g1, g2) in enumerate(gridlist) if x not in remove]
part2()