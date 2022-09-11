import math


def solution(fees, records):
    ans = {}
    cars = {}

    for r in records:
        time, num, rec = r.split()
        # 입차
        if rec == "IN":
            cars[num] = time
        # 출차
        else:
            # ((출차 시간 시 * 60) + 출차 시간 분) - ((입차 시간 시 * 60) + 입차 시간 분)
            use_time = (int(time[:2]) * 60 + int(time[-2:])) - ((int(cars[num][:2]) * 60) + int(cars[num][-2:]))

            # 이미 있으면 추가하고, 없으면 넣기
            if num in ans.keys():
                ans[num] += use_time
            else:
                ans[num] = use_time

            # 차 빼기
            del cars[num]

    # 출차하지 않은 차 처리
    for n in cars.keys():
        # 23:59 --> 1439분
        use_time = 1439 - ((int(cars[n][:2]) * 60) + int(cars[n][-2:]))

        if n in ans.keys():
            ans[n] += use_time
        else:
            ans[n] = use_time

    # 요금 계산
    for num, t in ans.items():
        if t <= fees[0]:
            ans[num] = fees[1]
        else:
            ans[num] = fees[1] + (math.ceil((t - fees[0]) / fees[2]) * fees[3])

    return ans