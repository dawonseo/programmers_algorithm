import math

def solution(n, stations, w):
    last = 1
    ans = 0
    
    for station in stations:
        a = station - w
        b = a - last
        if a > 1 and b > 0:
            ans += math.ceil(b / ((2 * w) + 1))
        last = station + w + 1
    
    if last <= n:
        ans += math.ceil(((n + 1) - last) / ((2 * w) + 1))
    
    return ans
