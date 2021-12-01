#!/home/rajivn/anaconda3/bin/python
data = None
with open("/home/rajivn/dev/adventOfCode/2021/01/input2", "r") as inp:
    data = inp.readlines()
    data = [int(d) for d in data]
last = 0
ptot = sum(data[:3])
count = 0
for v in data[3:]:
    newtot = ptot - data[last]
    newtot += v
    if newtot > ptot:
        count +=1
    ptot = newtot
    last += 1
print(count)