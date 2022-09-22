def solution(stones, k):
    start = 0
    end = max(stones)

    result = 0

    while start <= end:
        mid = (start + end) // 2
        cnt = 0

        for i in range(len(stones)):
            if stones[i] - mid <= 0:
                cnt += 1
            else:
                cnt = 0

            if cnt == k:
                end = mid - 1
                result = mid
                break

        if cnt < k:
            start = mid + 1

    return result