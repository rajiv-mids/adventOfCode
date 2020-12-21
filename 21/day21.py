#!/home/rajivn/anaconda3/bin/python
from collections import defaultdict, Counter
import operator

with open("/home/rajivn/adventOfCode/21/input", "r") as inp:
    t_inp = inp.readlines()

allergies_d = defaultdict(list)
ingredients_all = []
found = set()
final = dict()
for line in t_inp:
    ingrs_list, allerg_list = line.split("(")
    ingrs_list = [w.strip() for w in ingrs_list.split()]
    ingredients_all.extend(ingrs_list)
    allerg_list = allerg_list.replace(")", "").replace("contains", "").replace(",", "").split()
    for allerg in allerg_list:
        allergies_d[allerg].append(set(ingrs_list))

ingredients_all = Counter(ingredients_all)

found_x = True
while found_x:
    found_x = False
    for allergy, ingr_lists in allergies_d.items():
        ingredient = set.intersection(*ingr_lists) - found
        if len(ingredient) == 1:
            found_x = True
            x = ingredient.pop()
            final[x] = allergy
            found.add(x)
print("part1", sum([v for k, v in ingredients_all.items() if k not in final]))
print(",".join([k for k, v in sorted(final.items(), key=operator.itemgetter(1))]))
