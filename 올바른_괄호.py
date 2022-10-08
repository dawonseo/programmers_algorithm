def solution(s):
    tmp = 0
    for c in s:
        if c == "(":
            tmp += 1
        else:
            tmp -= 1
        
        if tmp < 0:
            return False
    
    if tmp != 0:
        return False
    
    return True
