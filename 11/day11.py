#!/home/rajivn/anaconda3/bin/python
seating = dict()
from copy import deepcopy
with open("/home/rajivn/adventOfCode/11/input", "r") as inp:
    for row, line in enumerate(inp.readlines()):
        for col, x in enumerate(line):
            seating[(row, col)] = x


max_r = row
max_c = col
changes = -1

def print_seating(s):
    for row in range(max_r + 1):
        for col in range(max_c + 1):
            print(s[(row, col)], end="")
        print()

p = 0
#print_seating(seating)
part_2_flag = True

# part 2. Each location has an array of length 8 for each surrounding cell starting from top left and going clockwise
# For first row only fill (None, None, None, X, None, None, None, None). 
# For second row fill (X,X,X,X,None, None, None, None)
# Second pass start bottom right to top left and fill in missing 
def preprocess(seating):
    ss = dict()
    for row in range(max_r+1):
        for col in range(max_c+1):
            if seating.get((row, col), "") != ".":
                continue
            ss[(row,col)]=[None]*8
            for i, (r, c) in enumerate([(-1, -1), (-1, 0), (-1, 1), (0, -1)]):
                if seating.get((row+r, col+c), "") == "#" or seating.get((row+r, col+c), "") == "L" :
                    ss[(row,col)][i] = seating.get((row+r, col+c), "")
                else:
                    ss[(row,col)][i] = ss.get((row+r, col+c), [None]* 8)[i]

    for row in range(max_r, -1, -1):
        for col in range(max_c, -1, -1):
            if seating.get((row, col), "") != ".":
                continue
            for i, (r, c) in enumerate([(0, 1), (1, -1), (1, 0), (1, 1)]):
                if seating.get((row+r, col+c), "") == "#" or seating.get((row+r, col+c), "") == "L" :
                    ss[(row,col)][i+4] = seating.get((row+r, col+c), "")
                else:
                    ss[(row,col)][i+4] = ss.get((row+r, col+c), [None]*8)[i+4]
    return ss


while changes != 0:
    changes = 0
    if (part_2_flag):
        s_flags = preprocess(seating)
    s2 = deepcopy(seating)
    for row in range(max_r + 1):
        for col in range(max_c + 1):
            if seating[(row, col)] == "L":
                for z, (r, c) in enumerate([(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]):
                    if seating.get((row+r,col+c), "") == "#":
                        break
                    if part_2_flag:
                        if (row+r,col+c) in s_flags and s_flags[(row+r,col+c)][z] == "#":
                            break
                else:
                    s2[(row,col)] = "#"
                    changes += 1
            
            if seating[(row, col)] == "#":
                cnt = 0
                for z, (r, c) in enumerate([(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]):
                    if seating.get((row+r,col+c), "") ==  "#":
                        cnt += 1
                    if part_2_flag:
                        if (row+r,col+c) in s_flags and s_flags[(row+r,col+c)][z] == "#":
                            cnt += 1
                    if (not part_2_flag and cnt == 4) or ( part_2_flag and cnt == 5):
                        s2[(row,col)] = "L"
                        changes += 1
                        break
    if changes != 0:
        seating = s2
        #print_seating(seating)
        #print("\n")
#    p+=1
s_occ = 0
for row in range(max_r + 1):
    for col in range(max_c + 1):
        if seating.get((row, col), "") == "#":
            s_occ += 1
print (s_occ)

