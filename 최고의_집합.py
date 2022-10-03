def solution(n, s):
    if s <= n:
        return [-1]
    
    d = s // n
    m = s % n
    
    return sorted([d + 1] * m + [d] * (n - m))
