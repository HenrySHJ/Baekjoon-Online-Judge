import sys
input = sys.stdin.readline

INF = sys.maxsize
N,M = map(int,input().split())

fuel = [list(map(int,input().split())) for _ in range(N)]

# DP[i][j][k] : i,j 좌표를 지나고 마지막 행동이 k일때 최소 연료
DP = [[[INF]*3 for _ in range(M)] for _ in range(N)]

# 초기값 설정
for j in range(M):
    DP[0][j][0] = fuel[0][j]
    DP[0][j][1] = fuel[0][j]
    DP[0][j][2] = fuel[0][j]

for i in range(1,N):
    for j in range(M):
        if j > 0:
            DP[i][j][0] = fuel[i][j] + min(DP[i-1][j-1][1], DP[i-1][j-1][2])
        DP[i][j][1] = fuel[i][j] + min(DP[i-1][j][0],DP[i-1][j][2])
        if j < M-1:
            DP[i][j][2] = fuel[i][j] + min(DP[i-1][j+1][0], DP[i-1][j+1][1])

print(min(DP[N-1][j][d] for j in range(M) for d in range(3)))