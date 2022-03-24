from collections import deque
from math import ceil


def solution(people, limit):
    people.sort()
    que_p = deque(people)
    ans = 0

    if (que_p[0] + que_p[-1]) <= limit:
        return ceil(len(que_p) / 2)
    else:
        while len(que_p) >= 2:
            if que_p[0] + que_p[-1] > limit:
                que_p.pop()
                ans += 1
            else:
                que_p.popleft()
                que_p.pop()
                ans += 1

    if len(que_p) >= 1:
        ans += 1

    return ans