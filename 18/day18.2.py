#!/home/rajivn/anaconda3/bin/python
with open("/home/rajivn/adventOfCode/18/input", "r") as inp:
    lines = inp.readlines()

from collections import deque

def eval2(vals):
    # do the + first
    mys = deque()
    for i, v in enumerate(vals):
        if i != 0 and vals[i-1] == "+":
            mys.appendleft(v + mys.popleft())
        elif v != "+":
            mys.appendleft(v)
    result = mys.popleft()
    while len(mys) > 0:
        v = mys.popleft()
        if v == "*":
            continue
        result *= v
    return result

def eval_f(pos, line, depth):
    vals = []
    while pos[0] < len(line):
        tok = line[pos[0]]
        pos[0] += 1
        if pos[0] == len(line):
            if isinstance(tok, int):
                vals.append(tok)
            return eval2(vals)
        elif isinstance(tok, str) and tok == ")":
            return eval2(vals)
        elif isinstance(tok, str) and tok == "(":
            vals.append(eval_f(pos, line, depth+1))
        elif isinstance(tok, str) and tok in "+*":
            vals.append(tok)
        else:
            vals.append(tok)
    return eval2(vals)

res = []
for line in lines:
    line = line.replace("(", " ( ").replace(")", " ) ")
    line = [int(n) if n.isdigit() else n for n in line.split()]
    res.append(eval_f([0], line, 0))
print(sum(res))