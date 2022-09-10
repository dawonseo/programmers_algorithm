def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    str1_list, str2_list = [], []
    cnt = 0

    if str1 == str2:
        return 65536

    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            str1_list.append(str1[i:i + 2])

    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            str2_list.append(str2[i:i + 2])

    str2_len = len(str2_list)

    # str1_list의 원소들을 돌며 str2_list 안에 있는지 확인
    # 있을 때마다 cnt 증가 --> 교집합 개수
    # str1_list의 길이 + (str2_list의 길이 - cnt) --> 합집합 개수

    for s in str1_list:
        if s in str2_list:
            cnt += 1
            str2_list.remove(s)
        else:
            continue

    return int((cnt / (len(str1_list) + (str2_len - cnt))) * 65536)
