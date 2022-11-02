def solution(arr):
    INF = 1e9
    MIN_DP = [[INF for _ in range(len(arr))] for _ in range(len(arr))]
    MAX_DP = [[-INF for _ in range(len(arr))] for _ in range(len(arr))]
    
    for i in range(0, len(arr), 2):
        MIN_DP[i][i] = int(arr[i])
        MAX_DP[i][i] = int(arr[i])
    
    for step in range(2, len(arr), 2):
        for i in range(0, len(arr)-step, 2):
            j = i + step
            for k in range(i+1, j, 2):
                if arr[k] == '+':
                    MIN_DP[i][j] = min(MIN_DP[i][j], MIN_DP[i][k-1] + MIN_DP[k+1][j])
                    MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k-1] + MAX_DP[k+1][j])
                elif arr[k] == '-':
                    MIN_DP[i][j] = min(MIN_DP[i][j], MIN_DP[i][k-1] - MAX_DP[k+1][j])
                    MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k-1] - MIN_DP[k+1][j])
        
    return MAX_DP[0][-1]
            
