#!/home/rajivn/anaconda3/bin/python
from collections import defaultdict
import re


mem = defaultdict(int)
mask = None

def do_mask(val, mask):
    b_val = str(bin(val)).replace("0b", "").zfill(36)
    zeros = [m.start() for m in re.finditer('0', mask)] 
    ones = [m.start() for m in re.finditer('1', mask)] 
    for i in zeros:
        b_val = b_val[:i]+"0"+b_val[i+1:]
    for i in ones:
        b_val = b_val[:i]+"1"+b_val[i+1:]
    return int(b_val, 2)
    

with open("/home/rajivn/adventOfCode/14/input", "r") as inp:
    lines = inp.readlines()
    for line in lines:
        inx, val = line.split("=")
        if inx == "mask ":
            mask = val.strip()
        else:
            # apply mask and write value
            loc = inx[inx.index("[")+1:inx.index("]")].strip()
            val = int(val.strip())
            mem[loc] = do_mask(val, mask)
    print("Part 1: ", sum([v for v in mem.values()]))