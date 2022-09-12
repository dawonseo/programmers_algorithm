def solution(m, n, board):
    new_board = [[] for i in range(n)]
    ans = 0

    for i in reversed(range(len(board))):
        for j in range(len(board[i])):
            new_board[j].append(board[i][j])

    while True:
        pop_list = []

        for x in range(len(new_board) - 1):
            if len(new_board[x]) <= 1 or len(new_board[x + 1]) <= 1:
                continue
            else:
                for y in range(len(new_board[x]) - 1):
                    if len(new_board[x + 1]) - 1 <= y:
                        continue
                    else:
                        this = new_board[x][y]
                        if this == new_board[x][y + 1] and this == new_board[x + 1][y] and this == new_board[x + 1][
                            y + 1]:
                            pop_list.extend([(x, y), (x, y + 1), (x + 1, y), (x + 1, y + 1)])

        if len(pop_list) == 0:
            return ans
        else:
            pop_list = list(set(pop_list))
            ans += len(pop_list)

        for x, y in pop_list:
            new_board[x][y] = 'X'

        for i in new_board:
            while 'X' in i:
                i.remove('X')
