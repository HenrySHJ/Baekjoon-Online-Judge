import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dx = [1, 0, -1 ,0]
dy = [0, 1, 0, -1]
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# DFS로 넓이가 4칸 될때까지 찾기
def DFS(x, y, area, point):
    global ans

    if area == 4:
        ans = max(ans, point)
        return

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        # 좌표 유효성 & 방문 여부 검사
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            DFS(nx, ny, area + 1, point + paper[nx][ny])
            
            # 백트래킹으로 방문 루트 복구
            visited[nx][ny] = False

# 예외 : T 모양 테트리미노
def checkT(x, y):
    global ans

    # x, y 중심으로 T 모양 찾기
    for k in range(4):
        tmp = paper[x][y]
        isPossible = True

        # 한 방향을 제외한 합 구하기
        for i in range(3):
            nk = (k + i) % 4

            nx = x + dx[nk]
            ny = y + dy[nk]

            # 좌표 유효성 검사
            if 0 <= nx < N and 0 <= ny < M:
                tmp += paper[nx][ny]
            # 채우지 못하는 좌표인 경우 바로 종료
            else:
                isPossible = False
                break
        
        # 가능한 T 모양인 경우 갱신 시도
        if isPossible:
            ans = max(ans, tmp)

ans = 0
for i in range(N):
    for j in range(M):
        # 기본 모양 테트리미노 확인
        visited[i][j] = True
        DFS(i, j, 1, paper[i][j])
        visited[i][j] = False

        # T 모양 확인
        checkT(i, j)

print(ans)