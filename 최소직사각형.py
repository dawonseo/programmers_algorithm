def solution(sizes):
    a = b = 0
    
    for i, j in sizes:
        if i >= j:
            a = max(a, i)
            b = max(b, j)
        else:
            a = max(a, j)
            b = max(b, i)
    
    return a * b
