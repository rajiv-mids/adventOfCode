#!/home/rajivn/anaconda3/bin/python
cmds = {"N": (1, 1), "S":(1, -1), "E":(0, 1), "W":(0, -1)}
wp_coord = [10,1]
s_coord = [0,0]
rots = ["E", "N", "W", "S"]
rot_pos = 0

"""
Action N means to move the waypoint north by the given value.
Action S means to move the waypoint south by the given value.
Action E means to move the waypoint east by the given value.
Action W means to move the waypoint west by the given value.
Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
Action F means to move forward to the waypoint a number of times equal to the given value.
"""

def rotate(cd, deg, direction):
    global rot_pos
    x = int(deg/90)
    rot_pos = (rot_pos + x*direction) %4

    if direction == 1:
        deg = 360 - deg
    if deg == 90:
        cd[0], cd[1] = cd[1], -cd[0]
    if deg == 270:
        cd[0], cd[1] = -cd[1], cd[0]
    if deg == 180:
        cd[0], cd[1] = -cd[0], -cd[1]

with open("/home/rajivn/adventOfCode/12/input", "r") as inp:
    for line in inp.readlines():
        d, n = line[0], int(line[1:])
        print(d,n)
        if d in "NSEW":
            p = cmds[d]
            wp_coord[p[0]] += n * p[1]
        elif d == "F":
            s_coord[0] += wp_coord[0] * n
            s_coord[1] += wp_coord[1] * n
        elif d == "L":
            rotate(wp_coord, n, 1)
        elif d == "R":
            rotate(wp_coord, n, -1)
        print(rots[rot_pos], wp_coord, s_coord)
    print(abs(s_coord[0]) + abs(s_coord[1]))