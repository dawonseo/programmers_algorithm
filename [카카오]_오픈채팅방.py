def solution(record):
    record_list = []
    nickname_dict = {}
    ans = []

    for r in record:
        r_list = list(map(str, r.split()))

        if len(r_list) >= 3:
            nickname_dict[r_list[1]] = r_list[2]

        record_list.append(r_list)

    for record in record_list:
        if record[0] == 'Enter':
            ans.append(nickname_dict[record[1]] + "님이 들어왔습니다.")
        elif record[0] == 'Leave':
            ans.append(nickname_dict[record[1]] + "님이 나갔습니다.")

    return ans
