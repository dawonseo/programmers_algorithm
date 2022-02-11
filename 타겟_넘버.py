# 프로그래머스 타겟 넘버

def solution(numbers, target):

    s_list = [0]
    n = 0
    lim = 0
    i = 0
    for num in numbers:
        while i <= lim:
            s_list.append(s_list[i] + num)
            s_list.append(s_list[i] - num)
            i += 1
        n += 1
        lim += 2**n

    return s_list[-(2**len(numbers)):].count(target)
