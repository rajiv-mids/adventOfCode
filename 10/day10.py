#!/home/rajivn/anaconda3/bin/python
input = None
with open("/home/rajivn/adventOfCode/10/input", "r") as inp:
    input = [int(n) for n in inp.readlines()]
inp_sort = sorted(input)
inp_sort = inp_sort + [inp_sort[-1] + 3]
last = 0
diffs_1, diffs_3 = 0, 0
ways_to_get_to = {0:1}
for v in inp_sort:
    diff = v-last
    if diff == 3:
        diffs_3 += 1
    if diff == 1:
        diffs_1 += 1
    ways_to_get_to[v] = ways_to_get_to.get(v-1, 0) + ways_to_get_to.get(v-2, 0) + ways_to_get_to.get(v-3, 0)
    last = v

print("answer 1", diffs_1 * diffs_3)
print("answer 2", ways_to_get_to[inp_sort[-1]])
