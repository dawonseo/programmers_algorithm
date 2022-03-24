def solution(n, lost, reserve):
    r_set = set(reserve) - set(lost)
    l_set = set(lost) - set(reserve)

    for i in r_set:
        if i - 1 in l_set:
            l_set.remove(i - 1)
        elif i + 1 in l_set:
            l_set.remove(i + 1)

    return n - len(l_set)