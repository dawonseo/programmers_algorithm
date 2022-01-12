import math

def solution(n):
    sq = math.sqrt(n)
    return (int(sq) + 1)**2 if sq == int(sq) else -1