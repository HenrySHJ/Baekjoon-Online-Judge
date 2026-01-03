import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
RGB = [list(input().strip()) for _ in range(N)]


dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(i,j,count,color):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    area[i][j] = count

    while queue:
        x,y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and RGB[nx][ny] == color:
                    visited[nx][ny] = True
                    area[nx][ny] = count
                    queue.append((nx,ny))

def BFS_colorblind(i,j,count,color):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    area[i][j] = count

    while queue:
        x,y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    if RGB[nx][ny] == 'R' or RGB[nx][ny] == 'G':
                        visited[nx][ny] = True
                        area[nx][ny] = count
                        queue.append((nx,ny))

# 일반인 기준
check = 1
area = [[0]*N for _ in range(N)]
visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            color = RGB[i][j]
            BFS(i,j,check,color)
            check += 1

print(check-1,end=' ')

# 적록색맹 기준
check = 1
area = [[0]*N for _ in range(N)]
visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            color = RGB[i][j]
            if color == 'B':
                BFS(i,j,check,color)
            else:
                BFS_colorblind(i,j,check,color)
            check += 1

print(check-1)