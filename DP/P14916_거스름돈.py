import sys
input = sys.stdin.readline

N = int(input())

DP = [sys.maxsize]*(N+1)
DP[0] = 0
coins = [2,5]

for i in coins:
    for j in range(i,N+1):
        if DP[j-i] != sys.maxsize:
            DP[j] = min(DP[j],DP[j-i] + 1)

print(DP[N] if DP[N] != sys.maxsize else -1)