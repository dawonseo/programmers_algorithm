def convert_iter(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    return convert_iter(q, base) + T[r] if q else T[r]


def solution(n, t, m, p):
    num_list = []
    ans = ''

    for i in range(t * m):
        num_list.extend(list(convert_iter(i, n)))

    order = 0

    while len(ans) < t:
        if order % m == (p - 1):
            ans += num_list[order]
        order += 1

    return ans