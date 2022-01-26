from itertools import permutations


def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(2 * i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]


def solution(numbers):
    answer = 0
    p_list = prime_list(10 ** len(numbers))

    per_list = []
    for i in range(1, len(numbers) + 1):
        per_list += list(permutations(numbers, i))

    for i in range(len(per_list)):
        per_list[i] = int(''.join(per_list[i]))

    per_list = list(set(per_list))

    for i in per_list:
        if i in p_list:
            answer += 1

    return answer