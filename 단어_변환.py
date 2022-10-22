from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = [False for _ in range(len(words))]
    l = len(words[0])
    
    queue = deque([(begin, 0)])
    
    while queue:
        x, cnt = queue.popleft()
        
        if x == target:
            return cnt
        
        for i in range(l):
            x2 = x[:i] + x[i+1:]
            for j in range(len(words)):
                y = words[j]
                if x2 == y[:i] + y[i+1:] and visited[j] == False:
                    visited[j] = True
                    queue.append((y, cnt + 1))
    
    return 0
