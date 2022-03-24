def solution(n, lost, reserve):
    # 체육복 도난당했지만 여벌 체육복 가지고 있는 학생 모두 제거
    r_set = set(reserve) - set(lost)
    l_set = set(lost) - set(reserve)

    # 여벌 체육복 가지고 있는 학생 set를 돌며, 전 번호와 뒤 번호 학생이 체육복을 도난당했는지 확인
    # 이때, 전 번호 먼저 확인해 봐야 한다
    # 전 번호 or 뒤 번호 학생이 도난당했다면 set에서 삭제(체육복을 빌려준 것으로 처리)
    for i in r_set:
        if i - 1 in l_set:
            l_set.remove(i - 1)
        elif i + 1 in l_set:
            l_set.remove(i + 1)
            
    # 총 학생 수에서 남은 학생(체육복 도난당하고 빌리지도 못한 학생) 수를 빼서 return
    return n - len(l_set)
