import sys
input = sys.stdin.readline

MOD = 1000000000

N,K = map(int,input().split())
DP = [[0]*(N+1) for _ in range(K+1)]

# 특정 수 i를 만드는데 한 개의 수를 쓸 때
for i in range(N+1):
    DP[1][i] = 1
for i in range(K+1):
    DP[i][0] = 1

for k in range(2, K + 1):
    for n in range(1, N + 1):
        DP[k][n] = (DP[k][n-1] + DP[k-1][n]) % MOD

print(DP[K][N])