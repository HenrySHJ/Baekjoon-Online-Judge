import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 현 인덱스까지의 경우의 수 저장
dp = [[0]*M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 시작점 경로 수 = 1
dp[0][0] = 1

# 모든 칸을 (높이, x, y) 형태로 모아 내림차순 정렬
cells = []
for i in range(N):
    for j in range(M):
        cells.append((A[i][j], i, j))
cells.sort(reverse=True)

# 높이 내림차순 순서로 DP 갱신
for h, x, y in cells:
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if A[nx][ny] < h:
                dp[nx][ny] += dp[x][y]

print(dp[N-1][M-1])