def solution(tickets):
    def dfs(start, v):
        v.append(start)
        
        for node in tickets_dict[start]:
            if not visited[(start, node)]:
                visited[(start, node)] = True
                dfs(node, v)
        return v

    tickets_dict = {}
    
    for s, g in tickets:
        if s in tickets_dict.keys():
            tickets_dict[s] += [g]
            tickets_dict[s].sort()
        else:
            tickets_dict[s] = [g]
        if g not in tickets_dict.keys():
            tickets_dict[g] = []
            
    visited = {(x,y) : False for x,y in tickets}
    b = dfs("ICN", [])
    return b
  
