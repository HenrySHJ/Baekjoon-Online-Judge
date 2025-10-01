from collections import deque

N = int(input())

A = [list(input()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def BFS(i,j):
    queue = deque()
    group_total = 0
    queue.append((i,j))
    visited[i][j] = True
    while queue:
        now = queue.popleft()
        group_total += 1
        for k in range(4):
            x = now[0]+dx[k]
            y = now[1]+dy[k]
            # 좌표 유효성 검사
            if x >= 0 and y >= 0 and x < N and y < N:
                if A[x][y] != '0' and not visited[x][y]:
                    visited[x][y] = True
                    queue.append((x,y))
    ans.append(group_total)

ans = []
for i in range(N):
    for j in range(N):
        if A[i][j] != '0' and not visited[i][j]:
            BFS(i,j)

print(len(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])