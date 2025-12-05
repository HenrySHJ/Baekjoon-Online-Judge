import sys
input = sys.stdin.readline

R,C = map(int,input().split())

A = [list(input().strip()) for _ in range(R)]

# DP[i][j] : A[i][j]의 (좌대각,우대각) 숫자 연속되는 누적합
DP = [[[0,0] for _ in range(C)] for _ in range(R)]

# DP 실행
for i in range(R):
    for j in range(C):
        # 숫자 누적이 끊기는 경우
        if A[i][j] == '0':
            DP[i][j][0] = 0
            DP[i][j][1] = 0

        # 숫자 누적이 되는 경우
        elif A[i][j] == '1':
            # 좌상단 -> 우하단
            if 0 <= i-1 < R and 0 <= j-1 <C:
                DP[i][j][0] = DP[i-1][j-1][0] + 1
            else:
                DP[i][j][0] = 1

            # 우상단 -> 좌하단
            if 0 <= i-1 < R and 0 <= j+1 < C:
                DP[i][j][1] = DP[i-1][j+1][1] + 1
            else:
                DP[i][j][1] = 1

ans = 0
# 정답 구하기
for i in range(R):
    for j in range(C):
        # 다이아몬드를 만들 수 없는 점 건너뛰기
        if A[i][j] == '0':
            continue
        
        # 현재 점이 가질 수 있는 최대 모양 크기
        max_dia = min(DP[i][j])
        
        # 정답이 갱신될 수 없는 경우 건너뛰기
        if ans >= max_dia:
            continue

        # d: 인덱스 변화량
        d = max_dia - 1

        # 다이아몬드 모양 & 크기 확인
        for k in range(d+1):
            if DP[i-k][j-k][1] >= k+1 and DP[i-k][j+k][0] >= k+1:
                ans = max(ans,k+1)

print(ans)