import sys
input = sys.stdin.readline

T = int(input())

DP = [0]*101
DP[1] = DP[2] = DP[3] = 1
DP[4] = DP[5] = 2

for i in range(6,101):
    DP[i] = DP[i-5] + DP[i-1]

for _ in range(T):
    N = int(input())
    print(DP[N])