#!/home/rajivn/anaconda3/bin/python
from collections import defaultdict
import re
import itertools
mem = defaultdict(int)
mask = None
mems = dict()
replaces = dict()
replaced_by = dict()
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

def find_msb(maskstr):
    x_id = maskstr.index("X")
    m_id = maskstr.index("1")
    return x_id if x_id < m_id else m_id

def sub_overlaps(l_mask1):
    sub = 0
    for k, v in mems.items():
        n1, n2 = find_msb(l_mask1), find_msb(k)
        rang = n1 if n1 < n2 else n2
        for a1, b1 in zip([x for x in l_mask1[rang:]], [x for x in k[rang:]] ):
            if a1 != "X" and b1 != "X" and a1!= b1:
                break
        else:
            combos_a = pow(2, len([m.start() for m in re.finditer('X', k)]) )
            tot_matches = combos_a
            for a, b in zip(k[rang:], l_mask1[rang:]):
                if a != 'X' and b!= 'X':
                    continue
                if a == "X" and b != "X" :
                    tot_matches = int(tot_matches/2)
            sub += (tot_matches * v)
    return sub

actuals = {}

def apply(mask_1, val):
    floats = [m.start() for m in re.finditer('X', mask)]
    c = itertools.product("01", repeat=len(floats))
    print("====")
    for combo in c:
        key = mask_1
        for l, v in zip(combo, floats):
            key = key[:v]+l+key[v+1:]
        print("mask", mask_1, "key", key)
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
            
            # go through prior vals and subtract
            remove = sub_overlaps(l_mask1)
            mems[l_mask1] = val
            tot += cur_tot
            tot -= remove

            #testing code
            apply(l_mask1, val)

    print("part 2", tot)
    print("verify", sum([v for v in memvals.values()]))

