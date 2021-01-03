from collections import deque
preamble_len = 25
inp = None
s1  = set() 
with open("/home/rajivn/adventOfCode/09/input", "r") as input:
    inp = input.readlines()
inp2 = []
myq = deque()
for i, line in enumerate(inp):
    num = int(line)
    if i < preamble_len:
        myq.append(num)
        s1.add(num)
        continue
    sum_found = False
    save = set()
    while len(s1) != 0:
        n1 = s1.pop()
        save.add(n1)
        if num-n1 in s1:
            sum_found = True
            break
    if not sum_found:
        a1 = num
        print("problem1=", num)
        break

    myq.append(num)
    s1 = s1.union(save)    
    s1.remove(myq.popleft())
    s1.add(num)

# problem 2
p2 = deque()
runtot = 0
for i, line in enumerate(inp):
    num = int(line)
    if num > a1:
        p2.clear()
        runtot = 0
        continue
    elif runtot + num < a1:
        runtot += num
        p2.append(num)
    elif runtot + num > a1:
        while (runtot + num) > a1 and len(p2) > 0:
            runtot -= p2.popleft()
    if runtot+num == a1 and runtot != 0:
        p2.append(num)
        print("problem2", min(p2)+ max(p2))
        break
    else:
        runtot += num
        p2.append(num)
