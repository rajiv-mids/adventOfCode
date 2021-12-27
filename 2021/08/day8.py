import os
from collections import Counter

nums = {2:1, 4:4, 3:7, 7:8}

path = os.path.dirname(os.path.abspath(__file__))
count = 0
with open(path+"/input", "r") as inp:
    data = inp.readlines()
    for d in data:
        _, b = d.strip().split("|")
        res = b.split(" ")
        for r in res:
            if len(r) in nums:
                count+=1

