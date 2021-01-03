#!/home/rajivn/anaconda3/bin/python
from collections import deque
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


to_process = [Job("", rules["0"])]
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
        for x, ch in enumerate(rule.split(" ")):
            ch = ch.strip()
            if ch =="":
                continue
            if not ch.isdigit():
                cur_job.sofar += ch.replace('"', '')
                #print(cur_job.sofar)
            else:
                rulelist.append(rules[ch])
        for r in reversed(rulelist):
            cur_job.stack.appendleft(r)

        if len(cur_job.stack) == 0:
            final_set.add(cur_job.sofar)
            

count = 0
for m in messages.split():
    if m in final_set:
        count+=1
print("Part 1:", count)