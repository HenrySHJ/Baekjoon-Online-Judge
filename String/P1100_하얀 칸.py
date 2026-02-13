import sys
input = sys.stdin.readline

board = [list(input().strip()) for _ in range(8)]

ans = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if board[i][j] == 'F':
                ans += 1

print(ans)