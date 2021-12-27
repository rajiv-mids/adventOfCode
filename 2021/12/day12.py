import os
from collections import defaultdict, deque
from copy import deepcopy

path = os.path.dirname(os.path.abspath(__file__))
data = []
graph = defaultdict(set)
with open(path+"/input", "r") as inp:
    for line in inp:
        st, en = line.strip().split("-")
        if en == "start":
            st, en = en, st
        if st == "end":
            st, en = en, st

        graph[st].add(en)
        if st != 'start' and en != 'end':
            graph[en].add(st)

myq = deque()
myq.append(["start", graph, "start"])
paths = []
while(len(myq)) > 0:
    st, g1, path = myq.popleft()
    for node in g1[st]:
        pc = deepcopy(path)
        pc += "," + node
        if node == 'end':
            paths.append(pc)
        else:
            g2 = deepcopy(g1)
            if node.islower():
                for ss in g2.values():
                    if node in ss:
                        ss.remove(node)
            myq.appendleft([node, g2, pc])
print(len(paths))