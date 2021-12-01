#!/home/rajivn/anaconda3/bin/python
data = None
with open("/home/rajivn/dev/adventOfCode/2021/01/input1", "r") as inp:
    data = inp.readlines()
    data = [int(d) for d in data]
prev = data[0]
count = 0
for n in data[1:]:
    if n > prev:
        count+=1
    prev = n
print(count)