import sys
input = sys.stdin.readline

T = int(input())
MOD = 1000000009
N = 1000000

DP = [0]*(N+1)
DP[1] = 1
DP[2] = 2
DP[3] = 4

for i in range(4,N+1):
    DP[i] = (DP[i-1] + DP[i-2] + DP[i-3]) % MOD

for _ in range(T):
    n = int(input())
    print(DP[n])