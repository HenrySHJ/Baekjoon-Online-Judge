import sys
input = sys.stdin.readline

N = int(input())
MOD = 10007

DP = [[0]*(10) for _ in range(N+1)]    # DP[자리수][일의 자리]

for i in range(10):
    DP[1][i] = 1

for i in range(2,N+1):
    for j in range(10):
        for k in range(j+1):
            DP[i][j] = (DP[i][j] + DP[i-1][k]) % MOD

print(sum(DP[N]) % MOD)