import sys
input = sys.stdin.readline

DP = [1]*68
DP[2] = 2
DP[3] = 4

for i in range(4,68):
    DP[i] = DP[i-1] + DP[i-2] + DP[i-3] + DP[i-4]

T = int(input())

for _ in range(T):
    N = int(input())
    print(DP[N])