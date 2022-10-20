def solution(money):
    dp1 = [0 for _ in range(len(money))]
    dp2 = [0 for _ in range(len(money))]

    dp1[0] = money[0]
    dp1[1] = money[1]
    if len(money) != 3:
        dp1[2] = money[0] + money[2]
    else:
        dp1[2] = money[2]
    for i in range(3, len(money)-1):
        dp1[i] = money[i] + max(dp1[i-2], dp1[i-3])

    dp2[1] = money[1]
    dp2[2] = money[2]
    for i in range(3, len(money)):
        dp2[i] = money[i] + max(dp2[i-2], dp2[i-3])
    return max(dp1+dp2)
