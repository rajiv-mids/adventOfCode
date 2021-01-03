#!/home/rajivn/anaconda3/bin/python

cmds = {"N": (1, 1), "S":(1, -1), "E":(0, 1), "W":(0, -1)}
coord = [0, 0]
rots = ["E", "N", "W", "S"]
rot_pos = 0

"""
Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.
"""


with open("/home/rajivn/adventOfCode/12/input", "r") as inp:
    for line in inp.readlines():
        d, n = line[0], int(line[1:])
        print(d,n)
        if d in "NSEW":
            p = cmds[d]
            coord[p[0]] += n * p[1]
        elif d == "F":
            p = cmds[rots[rot_pos]]
            coord[p[0]] += n * p[1]
        elif d == "L":
            x = int(n/90)
            rot_pos = (rot_pos + x) %4
        elif d == "R":
            x = int(n/90)
            rot_pos = (rot_pos - x) %4
        print(rots[rot_pos], coord)
    print(coord)
    print(abs(coord[0])+ abs(coord[1]))