import sys
input = sys.stdin.readline

N = int(input())

DP = [sys.maxsize]*(N+1)
DP[0] = 0
coins = [1,2,5,7]

for c in coins:
    for i in range(c,N+1):
        DP[i] = min(DP[i],DP[i-c] + 1)
    
print(DP[N])