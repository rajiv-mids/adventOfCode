#!/home/rajivn/anaconda3/bin/python
from collections import deque
import operator
with open("/home/rajivn/adventOfCode/13/input", "r") as inp:
    line = inp.readlines()
    sched, rl = int(line[0]), line[1]
routes = [int(r) for r in rl.split(",") if r != "x"]
earliest = {}
for r in routes:
    earliest[r] = ((sched//r) +1) * r
bus_num, bus_time= sorted(earliest.items(), key = operator.itemgetter(1))[0]
print("part1", bus_num * (bus_time-sched))

# part 2
routes = [(int(r), i) for i, r in enumerate(rl.split(",")) if r != "x"]
# find time t such that t mod bus number = index. Once found, then, 
# multiply it with tot found so far which should be fine since all are primes
# increment by tot and repeat until all are found
ts = 0
step = 1
acc = 0
for route, idx in routes:
    while (ts+idx)%route != 0:
        ts += step
    step *= route
    print("step=", step, "ts=", ts)
print(ts)