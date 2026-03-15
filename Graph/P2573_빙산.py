import sys
from collections import deque
input = sys.stdin.readline

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 인접이 방문하지 않은 빙산인 경우
            if not visited[nx][ny] and A[nx][ny] != 0:
                visited[nx][ny] = True
                queue.append((nx, ny))

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

year = 0
change = True

# 빙산에 변화가 존재할때까지 
while True:
    change = False

    # 빙산 덩어리 개수 계산
    visited = [[False] * M for _ in range(N)]
    group = 0

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and A[i][j] != 0:
                BFS(i, j)
                group += 1

    # 그룹이 2개가 되서 종료
    if group >= 2: 
        print(year)
        break
    
    # 그룹이 없으므로 종료
    if group == 0: 
        print(0)
        break
    
    # 빙산이 녹는 과정
    temp = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            # 바다인 경우 건너뛰기
            if A[i][j] == 0:
                continue
        
            # 주변의 바다에 따른 temp에 계산
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]

                if A[ni][nj] == 0:
                    temp[i][j] -= 1

    # 빙산 상태 갱신
    for i in range(N):
        for j in range(M):
            if temp[i][j] != 0:
                A[i][j] = max(A[i][j] + temp[i][j], 0)
                change = True

    year += 1