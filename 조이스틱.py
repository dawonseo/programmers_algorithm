def solution(name):
    cursor = 0
    ans = 0
    
    while cursor < len(name):
        this_word = ord(name[cursor])
        ans += min(91 - this_word, this_word - 65)
        cursor += 1
    
    ans += cursor - 1
    if name[1] == 'A': ans -= 1
    
    return ans
