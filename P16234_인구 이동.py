from collections import deque

N,L,R = map(int,input().split())

A = [list(map(int,input().split())) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    
    union = [(i,j)]  # 이번 연합을 따로 저장
    population = A[i][j]

    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(A[x][y]-A[nx][ny]) <= R:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    union.append((nx,ny))
                    population += A[nx][ny]

    if len(union) == 1:  # 국경 안 열림
        return False
    
    new_population = population // len(union)
    for x,y in union:
        A[x][y] = new_population
    return True


count = 0
while True:
    visited = [[False]*N for _ in range(N)]
    change = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if BFS(i,j):   # 이번 BFS에서 국경이 열렸으면
                    change = True
    
    if not change:  # 국경 더이상 안 열리면 종료
        break
    count += 1

print(count)