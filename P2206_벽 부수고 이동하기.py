from collections import deque

N,M = map(int,input().split())

A = [list(input()) for _ in range(N)]
# 3차원 배열로 해서 벽을 부순 채로 도달했는지 여부까지 확인
visited = [[[False]*2 for _ in range(M)] for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(i,j):
    queue = deque()
    queue.append((i,j,1,0))
    visited[i][j][0] = True
    while queue:
        x,y,dist,broken = queue.popleft()

        if x == N-1 and y == M-1:
            return dist
        
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            # 좌표 유효성 검사
            if 0 <= nx < N and 0 <= ny < M:
                # 벽을 안 마주쳤고, 아직 안 부순 경우
                if A[nx][ny] == '0' and not visited[nx][ny][broken]:
                    visited[nx][ny][broken] = True
                    queue.append((nx,ny,dist+1,broken))
                # 벽을 마주쳤고, 아직 안 부순 경우
                elif A[nx][ny] == '1' and broken == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    queue.append((nx,ny,dist+1,1))
                
    return -1

print(BFS(0,0))