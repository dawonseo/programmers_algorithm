import heapq
import sys


def solution(n, vertex):
    cost = [sys.maxsize for _ in range(n + 1)]
    node = [[] for _ in range(n + 1)]

    for i in vertex:
        [a, b] = i
        node[a].append((b, 1))
        node[b].append((a, 1))

    q = []
    heapq.heappush(q, (0, 1))
    cost[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if cost[now] < dist:
            continue
        for i in node[now]:
            c = dist + i[1]
            if c < cost[i[0]]:
                cost[i[0]] = c
                heapq.heappush(q, (c, i[0]))

    return cost.count(max(cost[1:]))