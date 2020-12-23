#!/home/rajivn/anaconda3/bin/python
from itertools import cycle
from copy import deepcopy

def part1(circle, moves):
    size = len(circle)
    idx = cycle([i for i in range(size)])
    with open("/home/rajivn/adventOfCode/23/out.csv", "w") as out:
        for move in range(0, moves):
            out.write(",".join(circle))
            out.write("\n")
            cur_pos = next(idx)
            curr = circle[cur_pos]
            ci = deepcopy(idx)
            pickidx = [next(ci) for _ in range(3)]
            pick = []
            [pick.append(circle[i]) for i in pickidx]
            nextidx = next(ci)
            nextele = circle[nextidx]
            print("move = ", move, "pick = ", pick, "circle = ", circle, "curr = ", curr)
            to_remove = [circle[i] for i in pickidx]
            [circle.pop(circle.index(r)) for r in to_remove]
            look = int(curr) - 1 if int(curr) - 1 > 0 else size
            look = str(look)
            while look not in circle:
                look = int(look) - 1 if int(look) > 0 else size
                look = str(look)
            li = circle.index(look)
            print('destination', look)

            circle = circle[:li+1] + pick + circle[li+1:]

            #rearrange
            x = circle.index(nextele)
            c2 = [None for _ in range(size)]
            nextidx = (cur_pos +1) % size
            for _ in range(size):
                c2[nextidx] = circle[x]
                x = (x + 1) % size
                nextidx = (nextidx + 1) % size
            circle = c2


    for i, c in enumerate(circle):
        if c == "1":
            #res = "".join(circle[i+1:]  + circle[:i])
            res = circle[i+1:]  + circle[:i]
    return res

circle = list("157623984")

#print("part1", part1(circle, 100))
circle = list("12345")
for i in range(6,21):
    circle.append(str(i))

print("part2", part1(circle, 100))