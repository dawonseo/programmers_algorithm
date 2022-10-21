from collections import deque

def solution(n, computers):
    ans = 0
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
    
    print(graph)
    
    for i in range(n):
        if computers[i][i] == 1:
            computers[i][i] = 0
            ans += 1
            queue = deque(graph[i])
            
            while queue:
                x = queue.popleft()
                if computers[x][x] == 1:
                    computers[x][x] = 0
                    for v in graph[x]:
                        if computers[v][v] == 1:
                            queue.append(v)

    
    return ans
