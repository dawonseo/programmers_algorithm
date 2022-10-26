def solution(name):
    if set(name) == {"A"}:
        return 0
    ans = 0
    prev = ''
    n = len(name)
    s = 0
    e = n - 1
    while s < n:
        if name[s] != 'A':
            break
        else:
            s += 1
    while e >= 0:
        if name[e] != 'A':
            break
        else:
            e -= 1
    m = min(e, n - s)
    
    for i in range(s, e+1):
        this = name[i]
        this_word = ord(this)
        ans += min(91 - this_word, this_word - 65)
        if prev == 'A':
            if this == 'A':
                continue
            else:
                end = i-1
                m = min(m, (start - 1) + (2 * ((n - end) - 1)), 2 * (start - 1) + ((n - end) - 1))
        else:
            if this == 'A':
                start = i
        prev = this

    return ans + m
