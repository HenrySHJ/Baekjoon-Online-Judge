import sys
input = sys.stdin.readline

MOD = 9901
N = int(input())

DP = [[0]*2 for _ in range(N+1)]
DP[0][0] = 0
DP[0][1] = 1

for i in range(1,N+1):
    DP[i][0] = (DP[i-1][1]*2 + DP[i-1][0]) % MOD
    DP[i][1] = (DP[i-1][0] + DP[i-1][1]) % MOD

print((DP[N][0]+DP[N][1]) % MOD)