import sys
input = sys.stdin.readline

MOD = 1000000

N = int(input())

# DP[i][j][k] : i일차까지 개근상이 가능한 최근 연속 j번 결석, 누적 지각 k번인 사람들
DP = [[[0]*2 for _ in range(3)] for _ in range(N+1)]
DP[1][0][0] = 1
DP[1][1][0] = 1
DP[1][0][1] = 1

for i in range(2,N+1):
    # i일차에 연속 0번 결석, 누적 0번 지각
    DP[i][0][0] = (DP[i-1][0][0] + DP[i-1][1][0] + DP[i-1][2][0]) % MOD

    # i일차에 연속 1번 결석, 누적 0번 지각
    DP[i][1][0] = DP[i-1][0][0] % MOD

    # i일차에 연속 2번 결석, 누적 0번 지각
    DP[i][2][0] = DP[i-1][1][0] % MOD
    
    # i일차에 연속 0번 결석, 누적 1번 지각
    DP[i][0][1] = (DP[i-1][0][0] + DP[i-1][1][0] + DP[i-1][2][0] + DP[i-1][0][1] + DP[i-1][1][1] + DP[i-1][2][1]) % MOD
 
    # i일차에 연속 1번 결석, 누적 1번 지각
    DP[i][1][1] = DP[i-1][0][1] % MOD

    # i일차에 연속 2번 결석, 누적 1번 지각
    DP[i][2][1] = DP[i-1][1][1] % MOD

ans = 0
for j in range(3):
    for k in range(2):
        ans = (ans + DP[N][j][k]) % MOD

print(ans)