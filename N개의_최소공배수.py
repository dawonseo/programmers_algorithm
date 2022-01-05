def solution(arr):
    arr.sort()
    a = arr[0]
    lcm = arr[0]
    for i in range(1, len(arr)):
        b = arr[i]
        if a > b:
            tmp = a
            a = b
            b = tmp
        # 유클리드 호제법
        while a:
            r = b % a
            b = a
            a = r
        lcm = (lcm * arr[i]) // b
        a = lcm
    return lcm
