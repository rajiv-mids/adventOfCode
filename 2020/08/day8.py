#!/home/rajivn/anaconda3/bin/python
from collections import deque
from copy import copy

class bootpgm:
    def __init__(self, inxs):
        self.acc_v = 0
        self.line_no = 0
        self.lines_ex = dict()
        self.lines = []
        self.cmds = {"nop": self.nop, "acc": self.acc, "jmp": self.jmp}
        self.nop_jmp = set()
        for line in inxs:
            cmd, arg = line.split()
            self.lines.append((self.cmds[cmd], int(arg)))

    def nop(self, _):
        self.line_no += 1

    def acc(self, arg):
        self.acc_v += arg
        self.line_no += 1

    def jmp(self, arg):
        self.line_no += arg

    def exec_p1(self):
        """
        returns an error code and accumulator value. return code of 0 indicates success, return code of 1 indicates error
        """
        inf_loop = False
        while not inf_loop and self.line_no < len(self.lines):
            cmd, arg = self.lines[self.line_no]
            self.lines_ex[self.line_no] = (cmd, arg)
            cmd(arg)
            if self.line_no in self.lines_ex: # check updated line number if already executed
                inf_loop = True
        if inf_loop:
            return True, self.acc_v
        else:
            return False, self.acc_v
      

inp = []
replacements = deque()
with open("/home/rajivn/adventOfCode/08/input", "r") as input:
    for r, inxs in enumerate(input.readlines()):
        inp.append(inxs)
        if inxs.find("nop") != -1:
            replacements.append((r, inxs.replace("nop", "jmp")))
        elif inxs.find("jmp") != -1:
            replacements.append((r, inxs.replace("jmp", "nop")))

inf_loop = True
while inf_loop:
    line_num, new_ins = replacements.pop()
    inp2 = copy(inp)
    inp2[line_num] = new_ins
    pgm = bootpgm(inp2)
    inf_loop, acc = pgm.exec_p1()
    if not inf_loop:
        print (acc)