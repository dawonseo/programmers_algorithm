def solution(places):
    ans = [1 for _ in range(len(places))]
    dx = [1, -1, 0, 0, 2, -2, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 0, 0, 2, -2, 1, 1, -1, -1]

    for i in range(len(places)):
        for j in range(len(places[i])):
            for h in range(len(places[i][j])):
                if places[i][j][h] == 'P':
                    tmp = []
                    for k in range(4):
                        if 0 <= (j + dy[k]) <= len(places[i]) - 1 and 0 <= (h + dx[k]) <= len(places[i][j]) - 1:
                            tmp.append(places[i][j + dy[k]][h + dx[k]])
                        else:
                            tmp.append('*')

                    print(tmp)

                    if 'P' in tmp:
                        ans[i] = 0
                        break

                    for k in range(4, 8):
                        if 0 <= (j + dy[k]) <= len(places[i]) - 1 and 0 <= (h + dx[k]) <= len(places[i][j]) - 1:
                            if places[i][j + dy[k]][h + dx[k]] == 'P':
                                if tmp[k - 4] != 'X':
                                    ans[i] = 0
                                    break

                    tmp_list = [(0, 2), (1, 2), (0, 3), (1, 3)]
                    for k in range(8, 12):
                        a, b = tmp_list[k - 8]
                        if 0 <= (j + dy[k]) <= len(places[i]) - 1 and 0 <= (h + dx[k]) <= len(places[i][j]) - 1:
                            if places[i][j + dy[k]][h + dx[k]] == 'P':
                                print("P 있음")
                                print(k)
                                if tmp[a] != 'X' or tmp[b] != 'X':
                                    ans[i] = 0
                                    print(j+dy[k])
                                    print(h+dx[k])
                                    print(places[i][j + dy[k]][h + dx[k]])
                                    print(a, b)
                                    print(tmp[a], tmp[b])
                                    break

    return ans


solution([["PXPXP", "XPXPX"]])