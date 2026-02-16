import sys
input = sys.stdin.readline

N, M = map(int, input().split())

T = [list(map(int, input().split())) for _ in range(N)]

# DP[i][j] : i번째 회차에서 이전에 사용한 무기가 j일때 클리어한 시간의 최솟값
DP = [[sys.maxsize] * M for _ in range(N)]

# DP 초기화
for j in range(M):
    DP[0][j] = T[0][j]

for i in range(1, N):
    # 최솟값과 그 당시의 인덱스, 2번째 최솟값
    m1, m2 = sys.maxsize, sys.maxsize
    m1_idx = -1

    for j in range(M):
        if DP[i - 1][j] < m1:
            m2 = m1
            m1 = DP[i - 1][j]
            m1_idx = j

        elif DP[i - 1][j] < m2:
            m2 = DP[i-1][j]

    # 현재 회차 수행
    for j in range(M):
        # 이전과 같은 무기 사용
        if j == m1_idx:
            DP[i][j] = m2 + T[i][j]
        else:
            DP[i][j] = m1 + T[i][j]

print(min(DP[N - 1]))