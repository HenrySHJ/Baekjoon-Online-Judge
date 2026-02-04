import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [[-1] * M for _ in range(N)]


dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 시작지점 찾기
x = -1
y = -1
for i in range(N):
    for j in range(M):
        if A[i][j] == 2:
            x, y = i, j
        elif A[i][j] == 0:
            B[i][j] = 0

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    B[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 좌표 유효성 검사
            if 0 <= nx < N and 0 <= ny < M:
                # 갱신되지 않은 B / 벽이 아니여야함
                if B[nx][ny] == -1 and A[nx][ny] == 1:
                        B[nx][ny] = B[x][y] + 1
                        queue.append((nx, ny))

BFS(x, y)

for i in range(N):
    print(*B[i])