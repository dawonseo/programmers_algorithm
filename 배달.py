import heapq
import sys


def solution(N, road, K):
    cost = [sys.maxsize for _ in range(N + 1)]
    node = [[] for _ in range(N + 1)]

    # node의 n번 인덱스에 (n과 연결된 노드, 비용)을 추가한다.
    for i in road:
        [a, b, c] = i
        node[a].append((b, c))
        node[b].append((a, c))

    q = []
    # 1번 노드(시작 노드)의 최단 경로를 0으로 설정, 큐에 삽입
    # (거리, 경로)
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

    ans = 0

    for i in cost[1:]:
        if i <= K:
            ans += 1

    return ans