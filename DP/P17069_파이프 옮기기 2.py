import sys
input = sys.stdin.readline

N = int(input())
A = [[0]+list(map(int,input().split())) for _ in range(N)]
A.insert(0,[0]*(N+1))

# DP[i][j][k] : 현재 끝점 i,j에 파이프가 있고, k가 (0: 가로, 1: 세로, 2: 대각)일때 
DP = [[[0]*3 for _ in range(N+1)] for _ in range(N+1)]
DP[1][2][0] = 1

for j in range(3,N+1):
    if A[1][j] == 0:
        DP[1][j][0] = 1
    else:
        break

for i in range(2,N+1):
    for j in range(3,N+1):
        # 가로 & 세로
        if A[i][j] != 1:
            DP[i][j][0] = DP[i][j-1][0] + DP[i][j-1][2]
            DP[i][j][1] = DP[i-1][j][1] + DP[i-1][j][2]
        if A[i][j] != 1 and A[i-1][j] != 1 and A[i][j-1] != 1:
            DP[i][j][2] = DP[i-1][j-1][0] + DP[i-1][j-1][1] + DP[i-1][j-1][2]

print(sum(DP[N][N]))