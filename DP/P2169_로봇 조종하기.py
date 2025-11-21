import sys
input = sys.stdin.readline

N,M = map(int,input().split())
robot = [list(map(int,input().split())) for _ in range(N)]

DP = [[-sys.maxsize]*M for _ in range(N)]
DP[0][0] = robot[0][0]

# 첫째 줄은 우로만 이동
for j in range(1, M):
    DP[0][j] = DP[0][j-1] + robot[0][j]

for i in range(1, N):
    left = [-sys.maxsize]*M
    right = [-sys.maxsize]*M
    
    # 좌 -> 우 방향으로 실행
    left[0] = DP[i-1][0] + robot[i][0]

    for j in range(1, M):
        left[j] = max(left[j-1], DP[i-1][j]) + robot[i][j]

    # 우 -> 좌 방향으로 실행
    right[M-1] = DP[i-1][M-1] + robot[i][M-1]

    for j in range(M-2, -1, -1):
        right[j] = max(right[j+1], DP[i-1][j]) + robot[i][j]

    # j 기준 최댓값 고르기
    for j in range(M):
        DP[i][j] = max(left[j], right[j])

print(DP[N-1][M-1])