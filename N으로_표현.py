def solution(N, number):
    if N == number:
        return 1

    ans = -1

    li = [set() for i in range(8)]

    li[0].add(N)
    for i in range(1, 8):
        li[i].add(int(str(N) * (i + 1)))

    for i in range(1, 8):
        for j in range(i):
            for a in li[j]:
                for b in li[i - j - 1]:
                    li[i].add(a + b)
                    li[i].add(a - b)
                    li[i].add(a * b)
                    if b != 0:
                        li[i].add(a // b)

        if number in li[i]:
            return i + 1

    return ans