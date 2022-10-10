def solution(array, commands):
    ans = []
    
    for c in commands:
        ans.append(sorted(array[c[0]-1:c[1]])[c[2]-1])
        
    return ans
