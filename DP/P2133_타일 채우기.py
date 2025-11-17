import sys
input = sys.stdin.readline

N = int(input())
DP = [0]*(N+1)
DP[0] = 1
if N >= 2:
    DP[2] = 3
for i in range(4,N+1):
    for j in range(i-2,-1,-2):
        if j == i-2:
            DP[i] += DP[j]*3
        else:
            DP[i] += DP[j]*2

print(DP[N])