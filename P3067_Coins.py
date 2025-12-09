import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int,input().split()))

    M = int(input())

    DP = [0]*(M+1)
    DP[0] = 1

    for c in coins:
        for i in range(0,M+1):
            if i-c >= 0 and DP[i-c] != 0:
                DP[i] += DP[i-c]

    print(DP[M])