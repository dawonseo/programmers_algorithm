from collections import Counter


def solution(gems):
    kindOfGems = len(set(gems))
    ans = []

    l = 0

    counter = Counter()

    for r in range(len(gems)):
        counter[gems[r]] += 1
        r += 1
        while len(counter) == kindOfGems:
            counter[gems[l]] -= 1
            if counter[gems[l]] == 0:
                del counter[gems[l]]
            l += 1
            ans.append([l, r])

    return sorted(ans, key=lambda x: (x[1] - x[0], x[0]))[0]


