lzw_dict = {chr(i + 64): i for i in range(1, 27)}
next_idx = 27

# 재귀함수 사용
def compression(msg, start, end):
    global lzw_dict
    global next_idx

    # end가 msg의 가능 인덱스를 넘어가면 return
    if end > len(msg):
        return lzw_dict[msg[start:end]], 0

    # 딕셔너리 안에 있으면 다음 문자 포함하여 탐색
    if msg[start:end] in lzw_dict.keys():
        return compression(msg, start, end + 1)
    # 딕셔너리 안에 없으면 추가하고, 직전 색인값 return
    else:
        lzw_dict[msg[start:end]] = next_idx
        next_idx += 1
        return lzw_dict[msg[start:end - 1]], end - start - 1


def solution(msg):
    global lzw_dict
    ans = []
    i = 0

    while i <= len(msg):
        com = compression(msg, i, i + 2)
        ans.append(com[0])
        if com[1]:
            i += com[1]
        else:
            break

    return ans