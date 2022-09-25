def solution(n, s, a, b, fares):
    INF = n * 100000 + 1
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if x == y:
                graph[x][y] = 0

    for i in range(len(fares)):
        x, y, z = fares[i]
        graph[x][y] = z
        graph[y][x] = z

    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

    ans = graph[s][a] + graph[s][b]

    for i in range(1, n + 1):
        tmp = graph[s][i] + graph[i][a] + graph[i][b]
        ans = min(tmp, ans)

    return ans


