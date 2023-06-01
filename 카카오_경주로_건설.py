import heapq


def solution(board):
    n = len(board)
    distance = [[1e9 for _ in range(n)] for _ in range(n)]
    distance[0][0] = 0

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    q = []
    if board[1][0] == 0:
        heapq.heappush(q, (100, 1, 0, 0))
        distance[1][0] = 100
    if board[0][1] == 0:
        heapq.heappush(q, (100, 0, 1, 1))
        distance[0][1] = 100
    while q:
        dist, x, y, direction = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                if direction != (i % 2):
                    cost = dist + 600
                else:
                    cost = dist + 100
                if cost <= (distance[nx][ny]):
                    distance[nx][ny] = cost
                if cost - 400 <= (distance[nx][ny]):
                    heapq.heappush(q, (cost, nx, ny, (i % 2)))

    return distance[-1][-1]