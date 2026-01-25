import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

board = [[0] * (M + 1)] + [[0] + list(map(int,input().split())) for _ in range(N)]
DP = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        DP[i][j] = max(DP[i][j], DP[i-1][j] + board[i][j], DP[i][j-1] + board[i][j])

print(DP[N][M])