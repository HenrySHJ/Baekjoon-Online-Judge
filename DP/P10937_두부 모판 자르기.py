import sys
input = sys.stdin.readline

# 등급에 따른 점수표
grade = {'A' : 0, 'B' : 1, 'C' : 2, 'F' : 3}

score = [[100, 70, 40, 0],
         [70, 50, 30, 0],
         [40, 30, 20, 0],
         [0, 0, 0, 0]]

N = int(input())

tofu = []
for _ in range(N):
    tofu += list(input().strip())

# DP[i][mask] : i번째 칸 이후의 N개 비트가 mask일때 최대 점수
DP = [[-1] * (1 << N) for _ in range(N ** 2 + 1)]
DP[0][0] = 0

# i를 기준으로 다음 인덱스가 중심이 될 때
for i in range(N ** 2):
    for mask in range(1 << N):
        # 갱신된 적이 없는 상태인 경우 건너뛰기
        if DP[i][mask] == -1:
            continue
        
        # mask에 다음 인덱스가 포함되어 있는 경우
        if mask & 1:
            DP[i + 1][mask >> 1] = max(DP[i + 1][mask >> 1], DP[i][mask])

        else:
            # 현재 칸 그대로 두기
            DP[i + 1][mask >> 1] = max(DP[i + 1][mask >> 1], DP[i][mask])
            
            # 가로로 자르기
            # 마지막 열이면 불가 / 다다음 인덱스가 포함되면 불가
            if i % N != N - 1 and not (mask & 2):
                price = score[grade[tofu[i]]][grade[tofu[i + 1]]]

                ni = i + 2
                if ni <= N ** 2:
                    DP[ni][mask >> 2] = max(DP[ni][mask >> 2], DP[i][mask] + price)

            # 세로로 자르기
            # 마지막 행이면 불가
            if i + N < N * N:
                price = score[grade[tofu[i]]][grade[tofu[i + N]]]
                
                nmask = (mask >> 1) | (1 << (N - 1))
                DP[i + 1][nmask] = max(DP[i + 1][nmask], DP[i][mask] + price)

print(DP[N ** 2][0])