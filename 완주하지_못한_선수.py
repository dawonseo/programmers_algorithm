def solution(participant, completion):
    h = {}

    for i in participant:
        if i not in h.keys():
            h[i] = 0
        else:
            h[i] += 1

    for i in completion:
        h[i] -= 1

    for k, v in h.items():
        if v == 0:
            return k