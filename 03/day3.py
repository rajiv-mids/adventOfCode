#!/home/rajivn/anaconda3/bin/python
import math
map = None
with open("/home/rajivn/adventOfCode/03/input", "r") as input:
    map = input.readlines()

def traverse(y_steps, x_steps):
    print(y_steps, x_steps)
    y, x = 0, 0
    num_trees = 0
    cols = len(map[0])-1
    while(y < len(map)-1):
        y += y_steps
        x += x_steps
        x = x%cols

        if map[y][x] == "#":
            num_trees += 1
    return num_trees

steps=[(1,1), (1, 3), (1, 5), (1, 7), (2, 1)]
print(math.prod([traverse(r, c) for r, c in steps]))
