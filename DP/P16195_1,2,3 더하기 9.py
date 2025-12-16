import sys
input = sys.stdin.readline

MOD = 1000000009
MAX = 1000

DP = [[0]*(MAX+1) for _ in range(MAX+1)]
DP[0][0] = 1

for n in range(1, MAX+1):
    for k in range(1, MAX+1):
        if n >= 1:
            DP[n][k] = (DP[n][k] + DP[n-1][k-1]) % MOD
        if n >= 2:
            DP[n][k] = (DP[n][k] + DP[n-2][k-1]) % MOD
        if n >= 3:
            DP[n][k] = (DP[n][k] + DP[n-3][k-1]) % MOD

T = int(input())
for _ in range(T):
    n,k = map(int,input().split())
    print(sum(DP[n][:k+1]) % MOD)