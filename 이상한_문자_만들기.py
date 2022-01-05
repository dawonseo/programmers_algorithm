def solution(s):
    arr = s.split(' ')

    for i in range(len(arr)):
        if arr[i] != ' ':
            arr2 = [arr[i][j].upper() if j % 2 == 0 else arr[i][j].lower() for j in range(len(arr[i]))]
            arr[i] = ''.join(arr2)

    return " ".join(arr)