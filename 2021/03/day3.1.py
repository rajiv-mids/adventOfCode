data = None
with open("/home/rajivn/dev/adventOfCode/2021/03/input1", "r") as inp:
    data = inp.readlines()
from collections import defaultdict, Counter
tp = defaultdict(str)
mc = 0
for r, row in enumerate(data):
    for c, col in enumerate(row.strip()):
        if c > mc:
            mc = c
        tp[c] += col

gamma_rate = ""
epsilon = ""

for i in range(mc+1):
    counts = Counter(tp[i])
    #print(counts)
    if counts.get('0', 0) > counts.get('1',0):
        gamma_rate+="0"
        epsilon +="1"
    else:
        gamma_rate+="1"
        epsilon +="0"
gamma_rate = int(gamma_rate, 2)
epsilon  = int(epsilon, 2)
print(gamma_rate * epsilon)
