import sys
input = sys.stdin.readline

MOD = 1000000007

DP = [0] * 5001
DP[0] = 1

for n in range(2, 5001, 2):
    for i in range(0, n - 1, 2):
        DP[n] += DP[i] * DP[n - 2 - i]
        DP[n] %= MOD

T = int(input())

for _ in range(T):
    L = int(input())

    print(DP[L])