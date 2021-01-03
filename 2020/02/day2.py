#!/home/rajivn/anaconda3/bin/python
from collections import Counter
correct_p1 = 0
correct_p2 = 0
with open("/home/rajivn/adventOfCode/02/input", "r") as input:
    for i, line in enumerate(input.readlines()):
        rule, passw = line.split(":") #2-5 c, ccckcc
        rule = rule.split(" ") #2-5 c => [[2-5], c]
        rule[0] = rule[0].split("-") # 2-5 c: ccckcc => [[2, 5], c]
        rule[0][0], rule[0][1] = int(rule[0][0]), int(rule[0][1])
        counts = Counter(passw)
        passw = passw.strip()
        if not(rule[1] not in counts or counts[rule[1]] <rule[0][0] or counts[rule[1]] > rule[0][1]):
            correct_p1 += 1
        count = 0
        if passw[rule[0][0] -1] == rule[1]:
            count +=1
        if passw[rule[0][1] -1] == rule[1]:
            count +=1
        if count == 1:
            correct_p2 += 1
print("correct_p1", correct_p1)
print("correct_p2", correct_p2)