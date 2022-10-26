def solution(word):
    x = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    ans = 0
    li = [0 for _ in range(5)]
    li[0] = 1
    
    for i in range(1, 5):
        li[i] = (li[i-1] * 5) + 1
    
    li = li[::-1]
    
    for i in range(len(word)):
        ans += x[word[i]] * li[i] +1
    
    return ans
