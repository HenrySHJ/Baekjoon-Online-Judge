import sys
input = sys.stdin.readline

N = int(input())
DP = [0]*(N+1)
DP[1] = DP[2] = sys.maxsize
DP[3] = 1
if N >= 4:
    DP[4] = sys.maxsize
if N >= 5:
    DP[5] = 1
ans = 0
for i in range(6,N+1):
    if DP[i-3] != sys.maxsize or DP[i-5] != sys.maxsize:
        DP[i] = min(DP[i-3]+1,DP[i-5]+1)
    else:
        DP[i] = sys.maxsize

print(DP[N] if DP[N] != sys.maxsize else -1)