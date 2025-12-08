import sys
input = sys.stdin.readline

T = int(input())

# DP[i][j] : 총 i자리 숫자, 마지막 숫자 j일때
DP = [[0]*10 for _ in range(65)]

for i in range(10):
    DP[1][i] = 1

for i in range(2,65):
    for j in range(10):
        for k in range(j+1):
            DP[i][j] += DP[i-1][k]

for _ in range(T):
    N = int(input())
    print(sum(DP[N]))