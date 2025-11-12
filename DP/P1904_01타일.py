import sys
input = sys.stdin.readline

MOD = 15746

N = int(input())

DP = [0]*(N+1)
DP[0] = DP[1] = 1
for i in range(2,N+1):
    DP[i] = (DP[i-1] + DP[i-2]) % MOD

print(DP[N])