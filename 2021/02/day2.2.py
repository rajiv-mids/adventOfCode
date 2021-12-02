#!/home/rajivn/anaconda3/bin/python
data = None
with open("/home/rajivn/dev/adventOfCode/2021/02/input1", "r") as inp:
    data = inp.readlines()
data = [row.split(" ") for row in data]
data = [(k, int(v.strip())) for k, v in data]
x, y, aim = 0, 0, 0

for move, val in data:
    if move == "forward":
        x += val
        y += aim * val
    elif move == "down":
        aim += val
    elif move == "up":
        aim -= val

print(x * y)
