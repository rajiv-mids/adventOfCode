#!/home/rajivn/anaconda3/bin/python
from collections import defaultdict
import re
import itertools
mem = defaultdict(int)
mask = None
memvals = dict()

def do_mask_1(val, mask):
    """ returns tuple of (a) locations of zeros (b) location of ones (c) masked value itself"""
    b_val = str(bin(val)).replace("0b", "").zfill(36)
    ones = [m.start() for m in re.finditer('1', mask)] 
    for i in ones:
        b_val = b_val[:i]+"1"+b_val[i+1:]
    floats = [m.start() for m in re.finditer('X', mask)]
    for i in floats:
        b_val = b_val[:i]+"X"+b_val[i+1:]
    return b_val


actuals = {}

def apply(mask_1, val):
    floats = [m.start() for m in re.finditer('X', mask)]
    c = itertools.product("01", repeat=len(floats))
    for combo in c:
        key = mask_1
        for l, v in zip(combo, floats):
            key = key[:v]+l+key[v+1:]
        memvals[key] = val

with open("/home/rajivn/adventOfCode/14/input", "r") as inp:
    lines = inp.readlines()
    tot = 0
    for line in lines:
        inx, val = line.split("=")
        if inx == "mask ":
            mask = val.strip()
        else:
            # apply mask and write value
            loc = int(inx[inx.index("[")+1:inx.index("]")].strip())
            val = int(val.strip())
            l_mask1 = do_mask_1(loc, mask)

            floats = [m.start() for m in re.finditer('X', l_mask1)]
            cur_tot = pow(2, len(floats)) * val
            
            apply(l_mask1, val)
    print("verify", sum([v for v in memvals.values()]))
