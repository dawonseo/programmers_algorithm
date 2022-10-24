def solution(distance, rocks, n):
    left = 0
    right = distance
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()
    print(rocks)
        
    ans = 0
    
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        
        tmp = rocks[:]
        
        idx = 1
        while idx < len(tmp):
            if tmp[idx] - tmp[idx-1] < mid:
                del tmp[idx]
                cnt += 1
            else:
                idx += 1
        
        if cnt <= n:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return ans
