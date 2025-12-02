import sys
input = sys.stdin.readline

MOD = 1000000003

N = int(input())
K = int(input())

# DP[i][j] : i개 중에 인접하지 않게 j를 고르는 경우의 수
DP = [[0]*(K+1) for _ in range(N+1)]

# j == 0,1 처리
for i in range(N+1):
    DP[i][0] = 1  # 아무 것도 안 고르는 경우
for i in range(1,N+1):
    DP[i][1] = i % MOD  # 하나만 고르는 경우

for i in range(2,N+1):
    for j in range(2,min(K,(i+1)//2)+1):
        DP[i][j] = (DP[i-1][j] + DP[i-2][j-1]) % MOD

ans = (DP[N-1][K]+DP[N-3][K-1]) % MOD
print(ans)