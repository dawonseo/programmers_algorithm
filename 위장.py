def solution(clothes):
    c_dict = {}
    ans = 1
    
    for c in clothes:
        if c[1] in c_dict.keys():
            c_dict[c[1]] += [c[0]]
        else:
            c_dict[c[1]] = [c[0]]
    
    for v in c_dict.values():
        ans *= (len(v) + 1)
    
    return ans - 1
