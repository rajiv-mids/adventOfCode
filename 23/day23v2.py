#!/home/rajivn/anaconda3/bin/python
from itertools import cycle
from copy import deepcopy


class Node:
    def __init__(self, ch):
        self.val = ch
        self.next = None

def findneighbors(node):
    for _ in range(1000000):
        if node.val == 1:
            return (node.next.val * node.next.next.val)
        node = node.next

def printcircle(node):
    print()
    for _ in range(9):
        print(str(node.val)+ " ", end="")
        node = node.next


def docircle(cur_ptr, moves, maxidx):
    for _ in range(moves):
        #pick = []
        curr = cur_ptr.val
        r_set = set()
        r_head = cur_ptr.next
        r_tail = r_head
        for x in range(3):
            #pick.append(r_tail)
            r_set.add(r_tail.val)
            if x != 2:
                r_tail = r_tail.next

        cur_ptr.next = r_tail.next
        
        look = (curr - 1) if (curr - 1) > 0 else maxidx
        while look in r_set:
            look = (look - 1) if (look-1)  > 0 else maxidx

        insnode = nodes[look]
        r_tail.next = insnode.next
        insnode.next = r_head

        #print("move = ", move, "pick = ", ",".join([str(o.val) for o in pick]), "curr = ", curr)
        #printcircle(cur_ptr)
        cur_ptr = cur_ptr.next
    return cur_ptr, findneighbors(cur_ptr)
nodes = dict()

def buildnodes(circle):
    _head, _tail = None, None
    for ch in circle:
        node = Node(int(ch))
        if not _head:
            _head = node
            _tail = node
        else:
            _tail.next = node
            _tail = _tail.next
        nodes[int(ch)] = node
    _tail.next = _head
    return _head

circle = list("157623984")
head = buildnodes(circle)
p1 = docircle(head, 100, len(circle))

print("part1", printcircle(p1[0]))

for i in range(10,1000001):
    circle.append(str(i))
head = buildnodes(circle)
p2 = docircle(head, 10000000, len(circle))
print("part2", p2[1])
