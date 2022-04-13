import heapq


def solution(scoville, K):
    # scoville 배열을 heapq로
    heapq.heapify(scoville)
    ans = 0

    while len(scoville) >= 2:
        if scoville[0] < K:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville) * 2
            heapq.heappush(scoville, a + b)
            ans += 1
            # 남은 값이 1개일 때 종료
            if len(scoville) == 1 and scoville[0] >= K:
                return ans
        else:
            return ans

    return -1