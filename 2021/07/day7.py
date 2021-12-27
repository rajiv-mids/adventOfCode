import os
from collections import Counter

path = os.path.dirname(os.path.abspath(__file__))
with open(path+"/input", "r") as inp:
    data = inp.readlines()

input = [int(x) for x in data[0].strip().split(",")]
input = Counter(input)

def tryval(val, input):
    return sum([abs(k-val) * v for k, v in input.items()])

def tryval2(val, input):
    """
    triangular number sequence n(n+1) / 2
    """
    ret = 0
    for k, v in input.items():
        n = abs(k-val)
        tri = n * (n+1) / 2
        ret += tri * v
    return ret    

cost = None
cost2 = None
for x in range(min(input.keys()), max(input.keys()) +1 ):
    if cost is None:
        cost = tryval(x, input)
        cost2 = tryval2(x, input)
    else:
        cost = min(cost, tryval(x, input))
        cost2 = min(cost2, tryval2(x, input))
print("part 1", cost)
print("part 2", cost2)