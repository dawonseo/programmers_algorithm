def solution(prices):
    answer = []

    for i in range(len(prices) - 1):
        p = 0
        for j in range(i + 1, len(prices)):
            p += 1
            if prices[i] > prices[j]:
                break
        answer.append(p)
    answer.append(0)

    return answer