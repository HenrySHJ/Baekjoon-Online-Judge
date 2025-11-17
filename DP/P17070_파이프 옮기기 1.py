import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
DP = [[[0]*3 for _ in range(N)] for _ in range(N)]  # 0: 가로, 1: 세로, 2: 대각
DP[0][1][0] = 1

for i in range(N):
    for j in range(1,N):
        if A[i][j] == 1:
            continue

        # 가로로 도착
        if j-1 >= 0:
            DP[i][j][0] += DP[i][j-1][0] + DP[i][j-1][2]

        # 세로로 도착
        if i-1 >= 0:
            DP[i][j][1] += DP[i-1][j][1] + DP[i-1][j][2]

        # 대각으로 도착
        if i-1 >= 0 and j-1 >= 0 and A[i-1][j] == 0 and A[i][j-1] == 0:
            DP[i][j][2] += DP[i-1][j-1][0] + DP[i-1][j-1][1] + DP[i-1][j-1][2]

print(sum(DP[N-1][N-1]))