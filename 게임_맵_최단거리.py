from collections import deque

def solution(maps):
    queue = deque([(0, 0, 1)])
    maps[0][0] = 0
    n = len(maps)
    m = len(maps[0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y, step = queue.popleft()
        
        if (x, y) == (n-1, m-1):
            return step
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m or maps[nx][ny] == 0:
                continue
            else:
                queue.append((nx, ny, step+1))
                maps[nx][ny] = 0
    
    return -1
                
