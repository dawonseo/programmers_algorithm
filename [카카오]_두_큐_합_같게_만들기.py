from collections import deque


def solution(queue1, queue2):
    n = len(queue1)
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1_sum = sum(q1)
    hqs = (q1_sum + sum(q2)) // 2
    ans = 0

    while len(q1) >= 1 and len(q2) >= 1 and ans < n * 2:
        if q1_sum == hqs:
            return ans
        elif q1_sum > hqs:
            p = q1.popleft()
            q1_sum -= p
            q2.append(p)
            ans += 1
        else:
            p = q2.popleft()
            q1_sum += p
            q1.append(p)
            ans += 1

    return -1