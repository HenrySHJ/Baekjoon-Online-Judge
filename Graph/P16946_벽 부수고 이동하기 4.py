from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [list(input()) for _ in range(N)]
ans = [[0]*M for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

group = [[-1] * M for _ in range(N)]
group_size = {}
group_id = 0

def BFS(i, j, gid):
    queue = deque()
    queue.append((i,j))
    group[i][j] = gid
    size = 1
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == '0' and group[nx][ny] == -1:
                group[nx][ny] = gid
                size += 1
                queue.append((nx, ny))
    group_size[gid] = size

# 0에서 상하좌우 이동 시 0이면 그룹으로 지정
for i in range(N):
    for j in range(M):
        if graph[i][j] == '0' and group[i][j] == -1:
            BFS(i, j, group_id)
            group_id += 1

# 벽에서 이동하기
for i in range(N):
    for j in range(M):
        if graph[i][j] == '1':
            near_group = set()
            # 좌표 기준 상하좌우 그룹 확인, 그룹 사이즈만큼 답에 추가
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < N and 0 <= ny < M and group[nx][ny] != -1:
                    near_group.add(group[nx][ny])
            total = 1
            for gid in near_group:
                total += group_size[gid]
            ans[i][j] = total % 10

for i in range(N):
    for j in range(M):
        print(ans[i][j],end='')
    print()