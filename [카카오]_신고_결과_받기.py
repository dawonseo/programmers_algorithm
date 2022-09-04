def solution(id_list, report, k):
    id_dict = {i: [[], 0, 0] for i in id_list}

    for i in set(report):
        reporter, reportee = i.split()
        id_dict[reportee][0] += [reporter]
        id_dict[reportee][1] += 1

    for user_id, value in id_dict.items():
        if value[1] >= k:
            for i in value[0]:
                id_dict[i][2] += 1

    return [val[2] for val in id_dict.values()]