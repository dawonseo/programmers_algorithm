def solution(numbers):
    ans = ''
    for i in sorted(enumerate(list(map(lambda x: x * (12 // len(x)), map(str, numbers)))), key = lambda x: -int(x[1])):
        ans += str(numbers[i[0]])
    
    return str(int(ans))
        
    
    
    
    
