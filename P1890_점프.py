import sys
input = sys.stdin.readline

N = int(input())

A = [list(map(int,input().split())) for _ in range(N)]
DP = [[0]*N for _ in range(N)]
DP[0][0] = 1

for i in range(N):
    for j in range(N):
        if A[i][j] == 0 or DP[i][j] == 0:
            continue
        
        # 아래쪽 방향
        ni = i + A[i][j]
        # 좌표 유효성 검사
        if ni < N:
            DP[ni][j] += DP[i][j]

        # 오른쪽 방향
        nj = j + A[i][j]
        # 좌표 유효성 검사
        if nj < N:
            DP[i][nj] += DP[i][j]

print(DP[N-1][N-1])