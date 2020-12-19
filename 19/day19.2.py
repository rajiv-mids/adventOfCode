#!/home/rajivn/anaconda3/bin/python
from collections import deque
import re
rules = {}
with open("/home/rajivn/adventOfCode/19/input", "r") as inp:
    rl, messages = inp.read().split("\n\n")
    for rule in rl.split("\n"):
        rules[rule.split(":")[0].strip()] = rule.split(":")[1].strip()

from copy import deepcopy

class Job:
    def __init__(self, sofar, rule):
        self.sofar = sofar
        self.stack = deque([rule])


def getstrings(rule_num, rule42 = None, rule31 = None):
    to_process = [Job("", rules[rule_num])]
    final_set = set()
    while(len(to_process) > 0):
        cur_job = to_process.pop()
        #print("to_process", len(to_process))
        while (len(cur_job.stack) > 0):
            #print("cur_job.stack", len(cur_job.stack))
            rule = cur_job.stack.popleft()
            if rule.find("|") != -1:
                r1, r2 = rule.split("|")
                for r in (r1, r2):
                    c2 = deepcopy(cur_job)
                    c2.stack.appendleft(r)
                    to_process.append(c2)
                break
            rulelist = []
            for _, ch in enumerate(rule.split(" ")):
                ch = ch.strip()
                if ch =="":
                    continue
                if not ch.isdigit():
                    ch = ch.replace('"', '')
                    cur_job.sofar += ch
                    #print(cur_job.sofar)
                else:
                    rulelist.append(rules[ch])
            for r in reversed(rulelist):
                cur_job.stack.appendleft(r)

            if len(cur_job.stack) == 0 :
                final_set.add(cur_job.sofar)
    return final_set
        
rule42 = getstrings("42")
rule31 = getstrings("31")

#rule 8 = one or more rule 42
#rule 11 = one or more rule 42 rollowed by equal number of rule 31
#rule 0 = rule 8 followed by rule 11

count = 0
for n in range(1, 30):
    rgx = "("
    rgx += ")|(".join(rule42)
    rgx += ")"
    rgx = "^("+rgx+")+"
    rgx_42 = "(("+")|(".join(rule42) + ")){"+str(n)+"}"
    rgx_31 = "(("+")|(".join(rule31) + ")){"+str(n)+"}$"
    rgx += rgx_42 + rgx_31
    rgx = re.compile(rgx)
    for m in messages.split():
        if rgx.match(m):
            print(m)
            count += 1
print(count)