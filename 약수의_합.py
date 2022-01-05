def solution(n):
    if n == 0 or n == 1:
        return n

    arr = [i for i in range(1, (n // 2) + 1) if n % i == 0]
    arr.append(n)
    return sum(arr)