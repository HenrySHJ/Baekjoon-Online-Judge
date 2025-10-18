import heapq,sys

M,N = map(int,input().split())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dijkstra(i,j):
    heap = []
    heapq.heappush(heap,(0,i,j))
    wall_break[i][j] = 0
    visited[i][j] = True
    while heap:
        nowNode = heapq.heappop(heap)
        x = nowNode[1]
        y = nowNode[2]
        visited[x][y] = True
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 좌표 유효성 검사
            if 1 <= nx <= N and 1 <= ny <= M:
                if wall_break[nx][ny] > wall_break[x][y] + int(A[nx][ny]):
                    wall_break[nx][ny] = wall_break[x][y] + int(A[nx][ny])
                    heapq.heappush(heap,(wall_break[nx][ny],nx,ny))
    return wall_break[N][M]

A = [['0']*(M+1)]  # 미로
for _ in range(N):
    temp = list('0'+input())
    A.append(temp)

wall_break = [[sys.maxsize]*(M+1) for _ in range(N+1)]
visited = [[False]*(M+1) for _ in range(N+1)]

ans = dijkstra(1,1)
print(ans)