import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

min_height = sys.maxsize
max_height = 0
ground = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        min_height = min(min_height, ground[i][j])
        max_height = max(max_height, ground[i][j])

ansTime = sys.maxsize
ansHeight = 0

# 최소 높이 ~ 최대 높이 사이의 값
for h in range(min_height, max_height + 1):
    inventory = B
    time = 0

    for i in range(N):
        for j in range(M):
            # 현재 높이가 목표보다 큰 경우 
            if ground[i][j] > h:
                time += (ground[i][j] - h) * 2
                inventory += ground[i][j] - h

            # 현재 높이가 목표보다 작아서 메워야하는 경우
            elif ground[i][j] < h:
                time += h - ground[i][j]
                inventory -= h - ground[i][j]
    
    # 시간 갱신
    if inventory >= 0 and time <= ansTime:
        ansTime = time
        ansHeight = h
    
print(ansTime, ansHeight)