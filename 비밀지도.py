def solution(n, arr1, arr2):
    ans_list = []

    for i in range(n):
        s = ''
        for j in bin(arr1[i] | arr2[i])[2:]:        # for문 대신 replace 함수를 사용했어야 했다...
            if j == '1':
                s += '#'
            elif j == '0':
                s += ' '

        if len(s) != n:
            s = (n - len(s)) * ' ' + s

        ans_list.append(s)

    return ans_list
