def solution(arr):
    INF = 1e9
    MIN_DP = [[INF for _ in range(len(arr))] for _ in range(len(arr))]
    MAX_DP = [[-INF for _ in range(len(arr))] for _ in range(len(arr))]
    
    for step in range(0, len(arr)-1, 2):
        for i in range(len(arr)-1):
            j = i + step
            
            if i == j:
                MIN_DP[i][j] = arr[i]
                MAX_DP[i][j] = arr[i]
