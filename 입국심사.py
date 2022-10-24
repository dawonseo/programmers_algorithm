def solution(n, times):
    left = 0
    right = 1e18
    ans = 1e18
    
    while left <= right:
        mid = (left + right) // 2
        people = n
        
        for i in times:
            people -= mid // i
            
        if people <= 0:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans
            
        
