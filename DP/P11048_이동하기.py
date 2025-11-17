import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
DP = [[0]*M for _ in range(N)]

DP[0][0] = A[0][0]
for i in range(1,N):
    DP[i][0] = DP[i-1][0] + A[i][0]
for i in range(1,M):
    DP[0][i] = DP[0][i-1] + A[0][i]

for i in range(1,N):
    for j in range(1,M):
        DP[i][j] = max(DP[i-1][j-1],DP[i-1][j],DP[i][j-1]) + A[i][j]

print(DP[N-1][M-1])