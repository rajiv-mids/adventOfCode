#!/home/rajivn/anaconda3/bin/python
from collections import defaultdict
nums = defaultdict(list)
nums_orig = list()
with open("/home/rajivn/adventOfCode/01/data", "r") as input:
    for i, v in enumerate(input.readlines()):
        nums[int(v)].append(int(i))
        nums_orig.append(int(v))


def lookfor(nums_map, nums_orig, num, skip):
    # look for number
    for k, v in enumerate(nums_orig):
        look = num-v
        if look in nums:
            arr =  nums[look]
            for i, l in enumerate(arr):
                if i != k and i != skip:
                    return (v , look)
    return None, None

#part 1
for i, v in enumerate(nums_orig):
    n2, n3 = lookfor(nums, nums_orig, 2020, i)
    if n2 is not None:
        print( n2 * n3)
        break
#part 2
for i, v in enumerate(nums_orig):
    lf = 2020-v
    n2, n3 = lookfor(nums, nums_orig, lf, i)
    if n2 is not None:
        print(v * n2 * n3)
        break