import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int,input().split()))
    M = int(input())

    DP = [0]*(M+1)
    DP[0] = 1
    for coin in coins:
        for i in range(coin,M+1):
            DP[i] += DP[i-coin]

    print(DP[M])