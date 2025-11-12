import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    stickers = [list(map(int,input().split())) for _ in range(2)]
    DP = [[0]*3 for _ in range(N)]
    DP[0][0] = 0
    DP[0][1] = stickers[0][0]
    DP[0][2] = stickers[1][0]

    for i in range(1,N):
        DP[i][0] = max(DP[i-1][0], DP[i-1][1], DP[i-1][2])
        DP[i][1] = max(DP[i-1][0], DP[i-1][2]) + stickers[0][i]
        DP[i][2] = max(DP[i-1][0], DP[i-1][1]) + stickers[1][i]
    
    print(max(DP[N-1]))