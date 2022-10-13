from itertools import permutations

def solution(k, dungeons):
    permu = list(permutations(dungeons, len(dungeons)))
    ans = 0
    
    for p in permu:
        ft = k
        cnt = 0
        for d in p:
            if ft < d[0]:
                break
            else:
                ft -= d[1]
                cnt += 1
        if cnt > ans:
            ans = cnt
    
    return ans
                
            
            
