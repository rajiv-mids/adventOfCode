def find(remain, st, end):
    if end == st:
        return st
    for ch in remain:
        if ch == 'F' or ch == 'L':
            end = int((st + end)/2)
        else:
            st = int((st + end)/2)+1
        return find(remain[1:], st, end)

# calc all seat IDs except first and last row for part 2
seats = set()
for r in range(4,111): # these numbers input from min and max discovered in input (loop below)
    for c in range(8):
        seats.add(r*8 + c)
max = None
# find min and max rows to find threshold
m_r, x_r = None, None
ids = set()
with open("/home/rajivn/adventOfCode/05/input", "r") as input:
    for line in input.readlines():
        r = find(line[:7], 0, 127)
        c = find(line[7:], 0, 7)
        if m_r is None or r < m_r:
            m_r = r
        if x_r is None or r > x_r:
            x_r = r
        m = r * 8 + c
        ids.add(m)
        if max is None or m > max:
            max = m
        if m in seats:
            seats.remove(m)


print(max)
print("seating starts", m_r, "seating ends", x_r)
print("seat missing", seats)