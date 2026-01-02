import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]
temp_graph = [[0] * M for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

virus = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append((i,j))

def BFS():
    queue = deque(virus)

    for i in range(N):
        for j in range(M):
            temp_graph[i][j] = graph[i][j]

    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] = 2
                queue.append((nx,ny))

    ans = 0
    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 0:
                ans += 1

    return ans

max_safe = 0

# BruteForce 벽 세우기
def make_wall(count):
    global max_safe
    
    # 벽 3개가 다 세워지면 바이러스 퍼뜨리기
    if count == 3:
        max_safe = max(max_safe, BFS())
        return

    # 맵 전체를 돌며 빈칸에 벽 세우기
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(count + 1) 
                graph[i][j] = 0

make_wall(0)
print(max_safe)