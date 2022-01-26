def solution(answers):
    answer = []
    grades = [[1, 0], [2, 0], [3, 0]]
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i, v in enumerate(answers):
        if p1[i % 5] == v:
            grades[0][1] += 1
        if p2[i % 8] == v:
            grades[1][1] += 1
        if p3[i % 10] == v:
            grades[2][1] += 1

    grades.sort(key=lambda x: x[1], reverse=True)
    high_score = grades[0][1]

    for i in grades:
        if i[1] == high_score:
            answer.append(i[0])
        else:
            break

    return sorted(answer)