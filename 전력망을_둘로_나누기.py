from itertools import combinations

def solution(n, wires):
    com_list = list(combinations(wires, len(wires)-1))
    ans = 100
    
    for com in com_list:
        visited = [False] * (n+1)
        graph = [[] for _ in range(n+1)]
        for i,j in com:
            graph[i].append(j)
            graph[j].append(i)

        stack = [1]
        cnt = 0

        while(stack):
            node = stack.pop()

            if not visited[node]:
                visited[node] = True
                stack.extend(graph[node])
                cnt += 1
        tmp = abs(cnt - (n - cnt))
        
        if tmp < ans:
            ans = tmp
            
    return ans
    
    
        
