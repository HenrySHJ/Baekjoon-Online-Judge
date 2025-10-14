import heapq, sys

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dijkstra(i,j):
    heap = []
    loopy[i][j] = cave[i][j]
    heapq.heappush(heap,(loopy[i][j],i,j))
    visited[i][j] = True
    while heap:
        nowNode = heapq.heappop(heap)
        x = nowNode[1]
        y = nowNode[2]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 좌표 유효성 검사
            if 0 <= nx < N and 0 <= ny < N:
                if loopy[nx][ny] > loopy[x][y] + cave[nx][ny]:
                    loopy[nx][ny] = loopy[x][y] + cave[nx][ny]
                    visited[nx][ny] = True
                    heapq.heappush(heap,(loopy[nx][ny],nx,ny))
    return loopy[N-1][N-1]

no = 1
while True:
    N = int(input())

    # 반복 종료
    if N == 0:
        break

    cave = [list(map(int,input().split())) for _ in range(N)]
    loopy = [[sys.maxsize]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]


    print("Problem",str(no)+":",dijkstra(0,0))
    no += 1