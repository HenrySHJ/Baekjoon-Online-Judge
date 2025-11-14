import sys
input = sys.stdin.readline

N,K = map(int,input().split())
coins = [int(input()) for _ in range(N)]

DP = [sys.maxsize]*(K+1)
DP[0] = 0
for i in range(N):
    for j in range(coins[i],K+1):
        DP[j] = min(DP[j],DP[j-coins[i]]+1)

if DP[K] != sys.maxsize:
    print(DP[K])
else:
    print(-1)