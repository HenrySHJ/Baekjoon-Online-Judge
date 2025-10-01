from collections import deque
M, N = map(int,input().split())

box = [list(input().split()) for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def BFS(start_point):
    queue = deque()
    for i,j,k in start_point:
        # x좌표, y좌표, 깊이
        queue.append((i,j,k))
    # 0인 토마토 개수 (0이 전부 안 익으면 return -1)
    ripe_count = 0
    # depth의 역할
    day = 0
    while queue:
        now = queue.popleft()
        day = max(day,now[2])
        ripe_count += 1
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            z = now[2] + 1
            if x >= 0 and y >= 0 and x < N and y < M:
                if box[x][y] == '0':
                    box[x][y] = '1'
                    queue.append((x,y,z))
        
    if ripe_count == tomato:
        return day
    else:
        return -1

# 출발점과 토마토가 없는 박스 구하기
start_point = []
empty = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == '1':
            start_point.append((i,j,0))
        elif box[i][j] == '-1':
            empty += 1

# 총 토마토 개수
tomato = N*M - empty
print(BFS(start_point))