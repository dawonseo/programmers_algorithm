import heapq


def solution(operations):
    h = []
    heapq.heapify(h)

    for i in operations:
        if i == "D 1":
            if len(h) >= 1:
                h.remove(max(h))
        elif i == "D -1":
            if len(h) >= 1:
                heapq.heappop(h)
        else:
            heapq.heappush(h, int(i[2:]))

    if len(h) == 0:
        return [0, 0]
    else:
        return [max(h), heapq.heappop(h)]