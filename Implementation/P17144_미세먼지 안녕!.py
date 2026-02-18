import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 위치 찾기
top = -1
for r in range(R - 1):
    if A[r][0] == -1:
        top = r
        break

bot = top + 1

sec = 0

dx = [1, 0, -1 ,0]
dy = [0, 1, 0, -1]

# 매초에 따른 진행
while sec < T:
    # 확산하는 먼지 따로 구해서 후에 합치기
    temp = [[0] * C for _ in range(R)]

    # 먼지 확산
    for i in range(R):
        for j in range(C):
            # 먼지가 없는 장소면 건너뛰기
            if A[i][j] == 0 or A[i][j] == -1:
                continue

            count = 0

            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]

                # 좌표 유효성 검사
                if 0 <= ni < R and 0 <= nj < C:
                    # 청정기 좌표 검사
                    if A[ni][nj] != -1:
                        count += 1
                        temp[ni][nj] += (A[i][j] // 5)

            # 확산한만큼 차감
            A[i][j] = A[i][j] - (A[i][j] // 5) * count
    
    # 확산받은 먼지 합치기
    for i in range(R):
        for j in range(C):
            A[i][j] += temp[i][j]

    # 윗 부분 청정기
    x, y = top, 0

    while x - 1 >= 0:
        A[x][0] = A[x - 1][0]
        x -= 1

    while y + 1 <= C - 1:
        A[0][y] = A[0][y + 1]
        y += 1
    
    while x + 1 <= top:
        A[x][y] = A[x + 1][y]
        x += 1

    while y - 1 >= 1:
        A[x][y] = A[x][y - 1]
        y -= 1

    A[top][1] = 0
    A[top][0] = -1

    # 아랫부분 청정기
    x, y = bot, 0

    while x + 1 <= R - 1:
        A[x][0] = A[x + 1][0]
        x += 1

    while y + 1 <= C - 1:
        A[x][y] = A[x][y + 1]
        y += 1
    
    while x - 1 >= bot:
        A[x][y] = A[x - 1][y]
        x -= 1

    while y - 1 >= 1:
        A[x][y] = A[x][y - 1]
        y -= 1

    A[bot][1] = 0
    A[bot][0] = -1

    # 시간 증가
    sec += 1

ans = 0
for i in range(R):
    for j in range(C):
        ans += A[i][j]

print(ans + 2)