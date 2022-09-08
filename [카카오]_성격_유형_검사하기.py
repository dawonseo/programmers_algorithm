def solution(survey, choices):
    my_dict = {'R': 0, 'C': 0, 'J': 0, 'A': 0, 'T': 0, 'F': 0, 'M': 0, 'N': 0}
    ans = ''

    for i in range(len(survey)):
        if choices[i] <= 3:
            my_dict[survey[i][0]] += (4 - choices[i])
        elif choices[i] >= 5:
            my_dict[survey[i][1]] += (choices[i] - 4)
        else:
            continue

    if my_dict['R'] >= my_dict['T']:
        ans += 'R'
    else:
        ans += 'T'
    if my_dict['C'] >= my_dict['F']:
        ans += 'C'
    else:
        ans += 'F'
    if my_dict['J'] >= my_dict['M']:
        ans += 'J'
    else:
        ans += 'M'
    if my_dict['A'] >= my_dict['N']:
        ans += 'A'
    else:
        ans += 'N'

    return ans
