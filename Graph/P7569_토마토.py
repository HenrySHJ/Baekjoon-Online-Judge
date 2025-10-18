from collections import deque
M, N, H = map(int, input().split())

# box[z][x][y] 구조
box = [[list(input().split()) for _ in range(N)] for _ in range(H)]

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def BFS(start_point):
    queue = deque(start_point)
    day = 0
    ripe_count = 0
    
    while queue:
        x, y, z, d = queue.popleft()
        day = max(day, d)
        ripe_count += 1
        
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]
            nd = d + 1
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if box[nz][nx][ny] == '0':
                    box[nz][nx][ny] = '1'
                    queue.append((nx, ny, nz, nd))
    
    return day if ripe_count == tomato else -1

# 출발점
start_point = []
empty = 0
for z in range(H):
    for x in range(N):
        for y in range(M):
            if box[z][x][y] == '1':
                start_point.append((x, y, z, 0))
            elif box[z][x][y] == '-1':
                empty += 1

tomato = N*M*H - empty
print(BFS(start_point))