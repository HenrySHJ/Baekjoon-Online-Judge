import sys
from collections import deque
input = sys.stdin.readline

# 상, 좌, 우, 하 순으로
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

N = int(input())

area = [list(map(int, input().split())) for _ in range(N)]


# 상어의 최초 위치 찾기
size = 2
shark_x = -1
shark_y = -1
for i in range(N):
    for j in range(N):
        if area[i][j] == 9:
            area[i][j] = 0
            shark_x = i
            shark_y = j
            break

# 너비 우선 탐색으로 가장 가까운 물고기 찾기
def BFS(i, j):
    dist = [[-1] * N for _ in range(N)]
    queue = deque()
    queue.append((i, j))
    dist[i][j] = 0
    candidates = []
    
    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 좌표 유효성 검사 & 방문 여부 확인
            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
                # 지나갈 수 있는지 확인
                if area[nx][ny] <= size:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
                    
                    # 먹을 수 있는지 확인
                    if 0 < area[nx][ny] < size:
                        candidates.append((dist[nx][ny], nx, ny))

    # 후보군 정렬 후 답 찾기
    if candidates:
        candidates.sort()
        return candidates[0]
    
    else:
        return None
    
time = 0
eat_count = 0

while True:
    result = BFS(shark_x, shark_y)

    # 물고기 탐색 실패하면 종료
    if not result:
        break
    
    d, shark_nx, shark_ny = result
    
    # 실제 이동 거리만큼 시간 추가
    time += d
    area[shark_nx][shark_ny] = 0
    eat_count += 1

    # 상어 크기 업그레이드
    if eat_count == size:
        size += 1
        eat_count = 0

    shark_x, shark_y = shark_nx, shark_ny

print(time)