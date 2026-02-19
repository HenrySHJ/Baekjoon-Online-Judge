import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1 ,0]
dy = [0, 1, 0, -1]

# BFS로 외부 공기 배열 반환 (가장자리는 무조건 외부 공기)
def BFS():
    # 외부 공기 체크
    isExternal = [[False] * M for _ in range(N)]
    queue = deque()
    queue.append((0, 0))
    isExternal[0][0] = True

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 좌표 유효성 검사
            if 0 <= nx < N and 0 <= ny < M:
                # 치즈가 아닌 곳(0)만 타고 나감 -> 내부 구멍은 못 들어감
                if not isExternal[nx][ny] and fridge[nx][ny] == 0:
                    isExternal[nx][ny] = True
                    queue.append((nx, ny))

    return isExternal

N, M = map(int, input().split())
fridge = [list(map(int, input().split())) for _ in range(N)]

time = 0

# 치즈가 사라질 때까지
while True:
    # 외부 공기 배열
    is_external = BFS()
    
    melt = []
    check = False

    # 냉장고 내부 좌표 치즈 탐색
    for i in range(N):
        for j in range(M):
            # 치즈를 찾으면 4방향으로 탐색
            if fridge[i][j] == 1:
                check = True
                count = 0
                
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]

                    # 좌표 유효성 검사
                    if 0 <= ni < N and 0 <= nj < M:
                        # 외부 공기와 접촉했을 때
                        if is_external[ni][nj]:
                            count += 1
                
                # 2방향 이상 접촉 시 녹일 대상에 추가
                if count >= 2:
                    melt.append((i, j))

    # 녹일 치즈가 없거나 치즈가 아예 없으면 종료
    if not check:
        break

    # 녹일 치즈 동시에 녹이기
    for x, y in melt:
        fridge[x][y] = 0

    if check:
        time += 1

print(time)