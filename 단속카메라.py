def solution(routes):
    ans = 0
    routes.sort(key = lambda x: x[1])
    
    i = 0
    
    while i < len(routes):
        camera = routes[i][1]
        
        j = i+1
        while j < len(routes):
            if routes[j][0] <= camera <= routes[j][1]:
                del routes[j]
            else:
                j += 1
        
        i += 1
    
    return len(routes)
    
