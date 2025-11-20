import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

VIP = [0]*(N+1)
# VIP 대상은 데이터를 1
for _ in range(M):
    VIP[int(input())] = 1

# DP[i][j] : i번 티켓을 가진 사람이 j번 좌석에 앉는 경우
DP = [[0]*(N+2) for _ in range(N+2)]

# i == 1일때 따로 처리
if VIP[1] != 1:
    DP[1][0] = 0
    DP[1][2] = 1
DP[1][1] = 1

for i in range(2,N+1):
    if VIP[i] != 1:
        DP[i][i-1] = DP[i-1][i]
        DP[i][i+1] = DP[i-1][i-2] + DP[i-1][i-1]
    DP[i][i] = DP[i-1][i-2] + DP[i-1][i-1]

print(DP[N][N-1]+DP[N][N])