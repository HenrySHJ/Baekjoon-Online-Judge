import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

treasure = [list(input().strip()) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(i,j):
    visited = [[False]*M for _ in range(N)]
    
    queue = deque()
    queue.append((i,j,0))
    visited[i][j] = True

    ans = 0
    while queue:
        x,y,z = queue.popleft()
        ans = max(ans,z)

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + 1
            # 좌표 유효성 검사
            if 0 <= nx < N and 0 <= ny < M:
                # 아직 방문하지 않았고 이동 가능할때
                if not visited[nx][ny] and treasure[nx][ny] == 'L':
                    visited[nx][ny] = True
                    queue.append((nx,ny,nz))

    return ans

answer = 0
for i in range(N):
    for j in range(M):
        if treasure[i][j] == 'L':
            answer = max(answer,BFS(i,j))

print(answer)