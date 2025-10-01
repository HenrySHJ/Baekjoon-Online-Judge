from collections import deque

T = int(input())

def BFS(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = False
    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[0]+dx[k]
            y = now[1]+dy[k]
            if x >= 0 and y >= 0 and x < M and y < N:
                if farm[x][y] != 0 and not visited[x][y]:
                    visited[x][y] = True
                    queue.append((x,y))

for _ in range(T):
    M,N,K = map(int,input().split())

    farm = [[0]*N for _ in range(M)]
    visited = [[False]*N for _ in range(M)]

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    for _ in range(K):
        x,y = map(int,input().split())
        farm[x][y] = 1

    group = 0
    for i in range(M):
        for j in range(N):
            if farm[i][j] == 1 and not visited[i][j]:
                BFS(i,j)
                group += 1
                
    print(group)