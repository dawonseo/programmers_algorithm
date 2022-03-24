from collections import deque
from math import ceil


def solution(people, limit):
    people.sort()           # 오름차순으로 정렬
    que_p = deque(people)
    ans = 0

    if que_p[-1]*2 <= limit:     # 가장 무거운 사람 몸무게*2가 limit보다 작으면 모두 2명씩 태워 보낼 수 있다
        return ceil(len(que_p) / 2)     # 사람의 수가 홀수일 경우와 짝수일 경우를 모두 고려 --> 2로 나눈 뒤 올림
    else:
        while len(que_p) >= 2:
            if que_p[0] + que_p[-1] > limit:    # 가장 가벼운 사람과 가장 무거운 사람의 합이 limit보다 크면
                que_p.pop()     # 가장 무거운 사람 혼자 타야 한다
                ans += 1
            else:
                que_p.popleft()     # 가장 가벼운 사람과 가장 무거운 사람의 합이 limit보다 크지 않으면,
                que_p.pop()     # 둘이 한 보트를 탄다 
                ans += 1

    if len(que_p) >= 1:     # 한 명이 남을 경우
        ans += 1

    return ans
