from collections import defaultdict
from itertools import cycle
import numpy as np
import re

pairs = {"L":"R", "T": "B", "R":"L", "B":"T"}
rots = ["L", "B", "R", "T"]

class Tile:
    def __init__(self, name, data=None, np_data = None):
        self.name = name
        if data is not None:
            self.data = np.array(data)
        else:
            self.data = np_data
        self.bord_by_pos = {"T" : Tile.border_to_str(self.data[0, :]), "R" : Tile.border_to_str(self.data[:, -1]), 
            "B": Tile.border_to_str(self.data[-1, :]), "L": Tile.border_to_str(self.data[:, 0])}
        self.linked = {"T":None, "R": None, "B": None, "L": None}
        
    def getborders(self):
        return self.bord_by_pos

    @staticmethod
    def border_to_str(border):
        return "".join([str(x) for x in border.tolist()])

    def grid_to_str(self):
        to_str = ""
        for row in self.data:
            to_str += "".join([str(x) for x in row.tolist()])
            to_str += "\n"
        return to_str

    def trim(self):
        st, en = 1, len(self.data)-1
        self.data = self.data[st:en, st:en]

    def flip(self, axis):
        self.data=np.flip(self.data, axis)
        self.bord_by_pos = {"T" : Tile.border_to_str(self.data[0, :]), "R" : Tile.border_to_str(self.data[:, -1]), 
            "B": Tile.border_to_str(self.data[-1, :]), "L": Tile.border_to_str(self.data[:, 0])}

    def rotate(self, n):
        self.data=np.rot90(self.data, n)
        self.bord_by_pos = {"T" : Tile.border_to_str(self.data[0, :]), "R" : Tile.border_to_str(self.data[:, -1]), 
            "B": Tile.border_to_str(self.data[-1, :]), "L": Tile.border_to_str(self.data[:, 0])}

    def find_monsters(self):
        l1 = "..................1."
        l2 = "1....11....11....111"
        l3 = ".1..1..1..1..1..1..."

        grid = self.grid_to_str().split("\n")
        grid.pop()
        m_count = 0
        for i, line in enumerate(grid):
            if i == 0 or i == len(grid)-1:
                continue
            for m in re.finditer(l2, line):
                st, en = m.start(), m.end()
                if (re.match(l1, grid[i-1][st:en])) is not None:
                    if (re.match(l3, grid[i+1][st:en])) is not None:
                        m_count += 1
        if m_count != 0:
            return self.data.sum() - (m_count*15)
        return 0

    def link(self, other):
        self_border, other_border = None, None
        for do, bord_o in other.getborders().items():
            for ds, bord_s in self.getborders().items():
                if bord_o == bord_s or bord_o == bord_s[::-1]:
                    other_border = do
                    self_border = ds
                    break
        # figure out rotations
        rotations = 0
        start = False
        if pairs[self_border] != other_border:
            for p in cycle(rots):
                if not start and p != other_border:
                    continue
                start = True
                if pairs[p] != self_border:
                    rotations += 1
                else:
                    break
            other.rotate(rotations)

        # figure out if flip is needed
        match_border = other.getborders()[pairs[self_border]]
        if match_border != self.bord_by_pos[self_border]:
            if pairs[self_border] in ("T", "B"):
                other.flip(1)
            else:
                other.flip(0)
        match_border = other.getborders()[pairs[self_border]]
        self.linked[self_border] = other
        other.linked[pairs[self_border]] = self

tile_borders = defaultdict(list)
with open("/home/rajivn/adventOfCode/20/input", "r") as inp:
    t_inp = inp.read().split("\n\n")
    for t in t_inp:
        n_tile = []
        for r, row in enumerate(t.split("\n")):
            if r == 0:
                name = re.findall(r"\d+", row)[0]
                continue
            n_tile.append([1 if col == "#" else 0 for col in row])
        to = Tile(name, n_tile)
        for dir_, border in to.getborders().items():
            tile_borders[border].append((dir_, to))

unvisited = set(tile_borders.keys())
# pick a tile and start from there
a_tile = next(iter(tile_borders.values()))[0][1]
to_visit = set()
to_visit.add(a_tile)
all_tiles = set()
while(len(to_visit)) > 0:
    t = to_visit.pop()
    for _, b1 in t.getborders().items():
        if b1 in unvisited or b1[::-1] in unvisited:
            for b1 in (b1, b1[::-1]):
                m1 = tile_borders[b1]
                m1 = [(dir, n_tile) for dir, n_tile in m1 if n_tile.name != t.name]
                [t.link(n_tile) for _, n_tile in m1]
                [all_tiles.add(n_tile) for _, n_tile in m1]
                [to_visit.add(n) for d, n in m1]
                if b1 in unvisited:
                    unvisited.remove(b1)

corners = 1
top_left = None
for t in all_tiles:
    links = 0
    for dir, tile in t.linked.items():
        if tile is not None:
            links += 1
    if links == 2:
        corners *= int(t.name)
        if t.linked['T'] is None and t.linked['L'] is None:
            top_left = t
print("part 1", corners)

rnode = top_left
data_all = None
while rnode is not None:
    rowdata = None
    cnode = rnode
    while cnode is not None:
        cnode.trim()
        if rowdata is None:
            rowdata = cnode.data
        else:
            rowdata = np.concatenate((rowdata, cnode.data), axis=1)
        cnode = cnode.linked["R"]    
    if data_all is None:
        data_all = rowdata
    else:
        data_all = np.concatenate((data_all, rowdata), axis=0)
    rnode = rnode.linked["B"]

final = Tile("All", np_data=data_all)

monsters = 0
for _ in range(4):
    monsters += final.find_monsters()
    if monsters != 0:
        break
    final.rotate(1)
    monsters += final.find_monsters()
    if monsters != 0:
        break
    final.flip(0)
    monsters += final.find_monsters()
    if monsters != 0:
        break
    final.flip(0)
    final.flip(1)
    monsters += final.find_monsters()
    if monsters != 0:
        break
    final.flip(1)
print("part2", monsters)