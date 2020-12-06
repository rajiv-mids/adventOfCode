g_list_1 = list()
g_list_2 = list()
with open("/home/rajivn/adventOfCode/06/input", "r") as input:
    for groups in input.read().split("\n\n"):
        g_ans_1 = set()
        g_ans_2 = None
        for person in groups.split("\n"):
            g_ans_1.update(person)
            if g_ans_2 is None:
                g_ans_2 = set(person)
            else:
                g_ans_2 = g_ans_2.intersection(set(person))
        g_list_1.append(len(g_ans_1))
        g_list_2.append(len(g_ans_2))
print(sum(g_list_1))
print(sum(g_list_2))