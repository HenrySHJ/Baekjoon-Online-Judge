import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

campus = [list(input().strip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

x = -1
y = -1
for i in range(N):
    find = False
    for j in range(M):
        if campus[i][j] == 'I':
            x, y = i, j
            find = True
            break

    if find:
        break

dx = [1, 0, -1 ,0]
dy = [0, 1, 0, -1]

def BFS(i, j):
    global ans
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()

        if campus[x][y] == 'P':
            ans += 1

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if campus[nx][ny] == 'X':
                    continue

                if visited[nx][ny]:
                    continue

                visited[nx][ny] = True
                queue.append((nx, ny))

ans = 0
BFS(x, y)

if ans != 0:
    print(ans)
else:
    print("TT")