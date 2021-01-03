#!/home/rajivn/anaconda3/bin/python
last_d = {v: i+1 for i, v in enumerate([2,15,0,9,1])}

last = 20
for turn in range(6, 30000001):
    if turn == 30000000:
        print("30000000 turn", last)
    ls = last
    if last not in last_d:
        last_d [ last] = turn
        last = 0
    else:
        last = turn - last_d[last]
        last_d[ls] = turn
