from collections import deque


def solution(n, t, m, timetable):
    new_timetable = deque([])
    tl = []
    timetable.sort()

    for i in range(len(timetable)):
        new_timetable.append(int(timetable[i][:2]) * 60 + int(timetable[i][3:]))

    for i in range(n):
        tl.append(540 + i * t)

    for i in range(len(tl)):
        if i == (len(tl) - 1):
            ans = tl[i]
            for j in range(m):
                if len(new_timetable) and new_timetable[0] <= tl[i]:
                    ans = new_timetable.popleft() - 1
                else:
                    ans = tl[i]
        for j in range(m):
            if len(new_timetable) and new_timetable[0] <= tl[i]:
                new_timetable.popleft()
            else:
                break

    return '{0:0>2}:{1:0>2}'.format(str(ans // 60), str(ans % 60))

