import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

# 두부에 따른 점수표
grade = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'F' : 4}

score = [[10, 8, 7, 5, 1], 
         [8, 6, 4, 3, 1], 
         [7, 4, 3, 2, 1], 
         [5, 3, 2, 2, 1], 
         [1, 1, 1, 1, 0]]

N, M = map(int, input().split())

tofu = []
for _ in range(N):
    tofu += list(input().strip())

# DP[i][mask] : i번째 칸 이후의 비트가 mask일때 최대 점수
DP = [[-1] * (1 << M) for _ in range(N * M + 1)]
DP[0][0] = 0

for i in range(N * M):
    for mask in range(1 << M):
        # 초기화 되지 않은 비트 상태에 대해서 건너뛰기
        if DP[i][mask] == -1:
            continue
        
        # 현재 비트에 다음 비트가 포함되어 있는 경우
        if mask & 1:
            DP[i + 1][mask >> 1] = max(DP[i + 1][mask >> 1], DP[i][mask])

        else:
            # 현재 칸을 안 쓰는 경우
            DP[i + 1][mask >> 1] = max(DP[i + 1][mask >> 1], DP[i][mask])

            # 가로로 자르기 (i, i + 1)
            # 마지막 열은 & 다음 인덱스가 비어있어지 않으면 불가
            if (i % M) != (M - 1) and not (mask & 2):
                price = score[grade[tofu[i]]][grade[tofu[i + 1]]]

                # i + 2 갱신시키기
                ni = i + 2
                if ni <= N * M:
                    DP[ni][mask >> 2] = max(DP[ni][mask >> 2], DP[i][mask] + price)

            # 세로로 자르기 (i, i + M)
            # 마지막 행 불가
            if i + M < N * M:
                price = score[grade[tofu[i]]][grade[tofu[i + M]]]

                # i + 1로 가면서, 아래 칸 비트는 켜주기
                nmask = (mask >> 1) | (1 << (M - 1))
                DP[i + 1][nmask] = max(DP[i + 1][nmask], DP[i][mask] + price)

print(DP[N * M][0])