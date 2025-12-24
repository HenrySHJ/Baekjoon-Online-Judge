import sys
input = sys.stdin.readline

MOD = 10**9+7

N,M = map(int,input().split())

DP = [[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    DP[i][1] = 1

for j in range(2,M+1):
    DP[1][j] = 1

for i in range(2,N+1):
    for j in range(2,M+1):
        DP[i][j] = (DP[i-1][j] + DP[i][j-1] + DP[i-1][j-1]) % MOD

print(DP[N][M])