from itertools import combinations


def solution(relation):
    com_list = []
    new_relation = [[] for _ in range(len(relation[0]))]
    ans_list = []

    for i in range(1, len(relation)):
        com_list.extend(list(combinations([n for n in range(len(relation[0]))], i)))

    for r in relation:
        print(r)
        for i in range(len(r)):
            new_relation[i].append(r[i])

    for c in com_list:
        tmp_list = [[] for _ in range(len(relation))]
        for j in range(len(c)):
            for k in range(len(relation)):
                tmp_list[k].append(new_relation[c[j]][k])
        tmp_list = list(map(tuple, tmp_list))
        if len(tmp_list) == len(set(tmp_list)):
            ans_list.append(c)

    for i in range(len(ans_list)):
        for j in range(i + 1, len(ans_list)):
            if set(ans_list[i]) < set(ans_list[j]):
                ans_list[j] = 'X'
        while 'X' in ans_list: ans_list.remove('X')
        if i + 1 >= len(ans_list):
            break

    return len(ans_list)
