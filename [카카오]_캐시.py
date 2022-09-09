from collections import deque


def solution(cacheSize, cities):
    cache = deque()
    ans = 0

    # cacheSize가 0일 때
    if cacheSize == 0:
        return 5 * len(cities)

    # 목록을 모두 소문자로 바꾸기
    cities = list(map(lambda x: x.lower(), cities))

    for c in cities:
        # cache에 있음
        if c in cache:
            cache.remove(c)
            cache.append(c)
            ans += 1
        # cache에 없음
        else:
            # cache 공간이 있음
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(c)
            ans += 5

    return ans
