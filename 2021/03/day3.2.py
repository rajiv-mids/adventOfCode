from collections import defaultdict
from copy import deepcopy

data = None
with open("/home/rajivn/dev/adventOfCode/2021/03/input1", "r") as inp:
    data = inp.readlines()
tp = defaultdict(str)
mc = 0
for r, row in enumerate(data):
    tp[r] = row

mc = len(tp[0])

def get_bit_criteria(data, col, r_type):
    zs, os = 0, 0
    for r, dat in data.items():
        if dat[col] == "0":
            zs+=1
        else:
            os+=1
    if zs == os:
        return r_type
    else:
        if r_type == "1":
            return "0" if zs > os else "1"
        else:
            return "1" if zs > os else "0"

def filter(data, col, val):
    rnums = []
    for r, dat in data.items():
        if dat[col] != val:
            rnums.append(r)
    for k in rnums:
        data.pop(k)

tpc = deepcopy(tp)

#O2 gen rating
o2, co2 = None, None
for i in range(mc+1):
    criteria = get_bit_criteria(tpc, i, "1")
    
    filter(tpc, i, criteria)
    if len(tpc) == 1:
        o2 = list(tpc.values())[0]

#CO2 scrub rating
for i in range(mc+1):
    criteria = get_bit_criteria(tp, i, "0")
    filter(tp, i, criteria)
    if len(tp) == 1:
        co2 = list(tp.values())[0]

print(int(o2, 2)* int(co2, 2))