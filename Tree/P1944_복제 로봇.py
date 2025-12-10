import sys,heapq
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
maze = [list(input().strip()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

# 시작점 & 열쇠 지점 찾기
points = []
for i in range(N):
    for j in range(N):
        if maze[i][j] == 'S' or maze[i][j] == 'K':
            points.append([i,j])

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(v):
    i,j = points[v][0],points[v][1]
    queue = deque()
    queue.append((i,j))

    dist = [[-1]*(N) for _ in range(N)]
    dist[i][j] = 0

    while queue:    
        x,y = queue.popleft()
        d = dist[x][y]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 좌표 유효성 검사
            if 0 <= nx < N and 0 <= ny < N :
                # 그래프 벽 검사 & 갱신 여부 검사
                if maze[nx][ny] != '1' and dist[nx][ny] == -1:
                    dist[nx][ny] = d + 1
                    queue.append((nx,ny))
    
    for i in range(M+1):
        # 동일정점 패스
        if i == v:
            continue
        x,y = points[i]

        # 정점 번호와 그 사이의 거리로 변환해서 push
        if dist[x][y] != -1:
            heapq.heappush(heap,(dist[x][y],v,i))

# 유니온 파인드
def find(a):
    while a != parent[a]:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

# main
heap = []
for i in range(M+1):
    BFS(i)

parent = [i for i in range(M+1)]

# MST
result = 0
useEdge = 0
while heap and useEdge < M:
    z,x,y = heapq.heappop(heap)
    if find(x) != find(y):
        union(x,y)
        result += z
        useEdge += 1

if useEdge < M and not heap:
    print(-1)
else:
    print(result)