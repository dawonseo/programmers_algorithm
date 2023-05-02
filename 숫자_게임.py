import heapq

def solution(A, B):
    heapq.heapify(A)
    heapq.heapify(B)
    ans = 0
    
    a = heapq.heappop(A)
    b = heapq.heappop(B)
    
    while True:
        if (not A) or (not B):
            if a < b:
                ans += 1
            break
        
        if a < b:
            ans += 1
            a = heapq.heappop(A)
        b = heapq.heappop(B)
    
    return ans
