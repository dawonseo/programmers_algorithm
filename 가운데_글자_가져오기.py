<<<<<<< HEAD
def solution(s):
    n = len(s) // 2
=======
def solution(s):
    n = len(s) // 2
>>>>>>> 624e21a8817cac5990c82c12f1043a9c1fa4855d
    return s[n if len(s) % 2 == 1 else n - 1: n + 1]