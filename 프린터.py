from collections import deque


def solution(priorities, location):
    # (중요도, 원래 순서) 쌍으로 된 값들을 가진 deque
    p_deque = deque([(v, i) for i, v in enumerate(priorities)])
    ans_li = []

    # 한 루프마다 priorities에서의 max값 즉, 가장 높은 중요도를 찾아 변수 m에 저장한다
    # p_deque의 0번 인덱스가 가장 중요한 문서가 아니라면 rotate하여 가장 뒤로 보낸다
    # p_deque의 0번 인덱스가 가장 중요한 문서라면 pop하여 ans_li에 넣고, priorities에서 m을 제거한다
    # p_deque에 값이 남아있을 때까지 반복
    while p_deque:
        m = max(priorities)
        if p_deque[0][0] == m:
            ans_li.append(p_deque.popleft())
            priorities.remove(m)
        else:
            p_deque.rotate(-1)

    for i in range(len(ans_li)):
        if ans_li[i][1] == location:
            return i + 1