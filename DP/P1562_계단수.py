import sys
input = sys.stdin.readline

MOD = 1000000000

N = int(input())

# DP[i][j][k] : i : 자릿수, j : 마지막 자리 수, k : 0~9 bitmasking
DP = [[[0]*(1<<10) for _ in range(10)] for _ in range(N+1)]

# 한 자리수 케이스 따로 처리 (0 제외)
for i in range(1,10):
    DP[1][i][1<<i] = 1

for i in range(1,N):
    for j in range(10):
        for k in range(1<<10):
            # 처리된 적이 없는 수 -> 건너뛰기
            if DP[i][j][k] == 0:
                continue
            
            # 숫자 유효 검사 & 비트 OR연산
            if j+1 <= 9:
                nk = k | (1<<(j+1))
                DP[i+1][j+1][nk] = (DP[i+1][j+1][nk] + DP[i][j][k]) % MOD

            # 숫자 유효 검사 & 비트 OR연산
            if j-1 >= 0:
                nk = k | (1<<(j-1))
                DP[i+1][j-1][nk] = (DP[i+1][j-1][nk] + DP[i][j][k]) % MOD

ans = 0
for i in range(10):
    ans = (ans + DP[N][i][1023]) % MOD

print(ans)