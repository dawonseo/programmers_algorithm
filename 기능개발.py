import math


def solution(progresses, speeds):
    t = [0] * len(progresses)
    answer = []

    for i in range(len(progresses)):
        t[i] = math.ceil((100 - progresses[i]) / speeds[i])

    print(t)

    max = t[0]
    a = 0
    for i in t:
        if i > max:
            answer.append(a)
            a = 1
            max = i
        else:
            a += 1
    answer.append(a)

    return answer