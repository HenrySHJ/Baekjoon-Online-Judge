import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

A = [list(map(int,input().split())) for _ in range(N)]

def BFS(i,j,h):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True

    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and A[nx][ny] > h:
                    visited[nx][ny] = True
                    queue.append((nx,ny))

ans = 1
for k in range(1,101):
    visited = [[False]*N for _ in range(N)]
    area = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and A[i][j] > k:
                BFS(i,j,k)
                area += 1

    ans = max(ans,area)

print(ans)