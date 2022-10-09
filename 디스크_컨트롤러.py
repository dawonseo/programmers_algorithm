import heapq

def solution(jobs):
    heapq.heapify(jobs)
    this_time = 0
    ans = 0
    size = len(jobs)
    
    while jobs:
        li = []
        
        while jobs:
            a = heapq.heappop(jobs)
            if a[0] <= this_time:
                heapq.heappush(li, [a[1], a[0]])
            else:
                heapq.heappush(jobs, a)
                break
        
        if li:
            tmp = heapq.heappop(li)
            ans += this_time - tmp[1] + tmp[0]
            this_time += tmp[0]
            
            if len(li) >= 1:
                for l in li:
                    heapq.heappush(jobs, [l[1], l[0]])
        else:
            this_time += 1
                    
    
    return ans//size
                    
            
