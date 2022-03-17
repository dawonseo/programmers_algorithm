def solution(N, number):
    if N == number:   # N과 number가 같을 경우 숫자 1개로 표현하는 것이 최소
        return 1

    ans = -1

    li = [set() for i in range(8)]  # 8개의 set로 이루어진 list 생성

    li[0].add(N)
    for i in range(1, 8):
        li[i].add(int(str(N) * (i + 1))) # ex) [{1}, {11}, {111}, {1111}, ... , {11111111}]

    for i in range(1, 8):
        for j in range(i):
            for a in li[j]:
                for b in li[i - j - 1]: # 5개의 N으로 이루어질 수 있는 경우의 수는 1+4, 2+3, 3+2, 4+1
                    li[i].add(a + b)     
                    li[i].add(a - b)
                    li[i].add(a * b)
                    if b != 0:  
                        li[i].add(a // b)  # b가 0일 경우는 나누기를 진행하지 않는다

        if number in li[i]:              # number가 li[i]에 있을 경우, index+1을 반환
            return i + 1

    return ans
