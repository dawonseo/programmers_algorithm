from itertools import permutations


def solution(user_id, banned_id):
    user_perm = list(permutations(user_id, len(banned_id)))
    ans_list = []

    for perm in user_perm:
        is_match = True
        if tuple(sorted(perm)) in ans_list:
            continue
        for i in range(len(perm)):
            if len(perm[i]) == len(banned_id[i]):
                for j in range(len(perm[i])):
                    if perm[i][j] == banned_id[i][j] or banned_id[i][j] == '*':
                        continue
                    else:
                        is_match = False
                        break
            else:
                is_match = False
            if not is_match:
                break
        if is_match:
            ans_list.append(tuple(sorted(perm)))

    return len(set(ans_list))

