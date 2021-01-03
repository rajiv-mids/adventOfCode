#!/home/rajivn/anaconda3/bin/python
with open("/home/rajivn/adventOfCode/18/input", "r") as inp:
    lines = inp.readlines()

func = {"+": lambda x, y: x+y, "*": lambda x, y: x*y}

def eval_f(pos, line, depth):
    val = 0
    op = None
    while pos[0] < len(line):
        tok = line[pos[0]]
        #print(depth*" ", "tok =", tok, "val =", val, "op = ", op)
        pos[0] += 1
        if pos[0] == len(line):
            if op is not None and isinstance(tok, int):
                return func[op](val, tok)
            else:
                return val
        elif isinstance(tok, str) and tok == ")":
            return val
        elif isinstance(tok, str) and tok == "(":
            if op is None:
                val = eval_f(pos, line, depth+1)
            else:
                val = func[op](val,  eval_f(pos, line, depth+1))
        elif isinstance(tok, str) and tok in "+*":
            op = tok
        else:
            if op is None:
                val = tok
            else:
                val = func[op](val, tok)
    return val
res = []
for line in lines:
    line = line.replace("(", " ( ").replace(")", " ) ")
    line = [int(n) if n.isdigit() else n for n in line.split()]
    res.append(eval_f([0], line, 0))
print(sum(res))