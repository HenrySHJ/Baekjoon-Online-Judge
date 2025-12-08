import sys
input = sys.stdin.readline

N = int(input())

DP = [0]*(N+1)
DP[1] = 1

if N >= 2:
    DP[2] = 1

if N >= 3:
    DP[3] = 1

for i in range(4,N+1):
    DP[i] = DP[i-1] + DP[i-3]

print(DP[N])