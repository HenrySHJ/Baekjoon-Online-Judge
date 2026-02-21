import sys
from collections import deque
input = sys.stdin.readline

# 나이트 움직이는 경로
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

def BFS(i, j, size, visited):
    queue = deque()
    queue.append((i, j, 0))
    visited[i][j] = True

    while queue:
        x, y, act = queue.popleft()

        # 목표에 도착
        if x == tx and y == ty:
            return act
        
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            # 좌표 유효성 검사
            if 0 <= nx < size and 0 <= ny < size:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, act + 1))
T = int(input())

for _ in range(T):
    L = int(input())

    cx, cy = map(int, input().split())
    tx, ty = map(int, input().split())

    visited = [[False] * L for _ in range(L)]
    count = BFS(cx, cy, L, visited)
    print(count)