import heapq

def solution(n, works):
    heap = []
    result = 0
    
    for w in works:
        heapq.heappush(heap, -w)

    
    for i in range(n):
        tmp = heapq.heappop(heap)
        if tmp == 0:
            return 0
        heapq.heappush(heap, tmp + 1)
    
    while heap:
        result += (heapq.heappop(heap))**2
    
    return result
