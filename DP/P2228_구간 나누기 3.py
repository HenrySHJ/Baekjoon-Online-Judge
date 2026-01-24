import sys
input = sys.stdin.readline

INF = sys.maxsize

N, M = map(int, input().split())
A = [0] + [int(input()) for _ in range(N)]

# 누적 합
S = [0] * (N + 1)
for i in range(1, N + 1):
    S[i] = S[i-1] + A[i]

# DP 테이블 초기화
# DP[i][j]: i번째 원소까지 사용하여 j개의 구간을 나누었을 때의 최대 합
DP = [[-INF] * (M + 1) for _ in range(N + 1)]

# 0개의 구간을 만드는 합
for i in range(N + 1):
    DP[i][0] = 0

# 점화식
for j in range(1, M + 1):          
    for i in range(1, N + 1):      
        # i번째 원소를 포함하지 않는 경우
        DP[i][j] = DP[i-1][j]
        
        # i번째 원소가 마지막 구간의 끝인 경우
        # 마지막 구간 시작점 k
        for k in range(1, i + 1):
            # k번부터 i번까지 하나의 구간
            if k >= 2:
                DP[i][j] = max(DP[i][j], DP[k-2][j-1] + (S[i] - S[k-1]))

            # 첫 번째 구간이 1번부터 시작하는 특수 경우
            elif k == 1 and j == 1:
                DP[i][j] = max(DP[i][j], S[i] - S[k-1])

print(int(DP[N][M]))