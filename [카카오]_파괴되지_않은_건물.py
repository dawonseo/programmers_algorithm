def solution(board, skill):
    n = len(board)
    m = len(board[0])
    skill_board = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for s in skill:
        if s[0] == 1: t = -1
        else: t = 1
        skill_board[s[1]][s[2]] += s[5] * t
        skill_board[s[1]][s[4]+1] += s[5] * t * -1
        skill_board[s[3]+1][s[2]] += s[5] * t * -1
        skill_board[s[3]+1][s[4]+1] += s[5] * t
        print(skill_board)

    
    for x in range(n+1):
        for y in range(1, m+1):
            skill_board[x][y] = skill_board[x][y-1] + skill_board[x][y]
    
    for x in range(1, n+1):
        for y in range(m+1):
            skill_board[x][y] = skill_board[x-1][y] + skill_board[x][y]
    
    cnt = 0
    
    for x in range(n):
        for y in range(m):
            if board[x][y] + skill_board[x][y] > 0:
                cnt += 1
    
    return cnt
