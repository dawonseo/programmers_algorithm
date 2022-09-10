def convert_iter(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    return convert_iter(q, base) + T[r] if q else T[r]


def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def solution(n, k):
    new_num = n
    if k != 10:
        new_num = convert_iter(n, k)
    ans = 0

    for n in list(str(new_num).split('0')):
        if len(n) == 0:
            continue
        elif is_prime(int(n)):
            ans += 1

    return ans
