import sys
input = sys.stdin.readline

T = int(input())

DP = [[0]*4 for _ in range(10001)]

# 1로만 만드는 경우 : 1가지
for i in range(10001):
    DP[i][1] = 1

# 1~2로 만드는 경우
for i in range(2,10001):
    DP[i][2] = DP[i-2][2] + DP[i-2][1]

# 1~3로 만드는 경우
for i in range(3,10001):
    DP[i][3] = DP[i-3][3] + DP[i-3][2] + DP[i-3][1]

for _ in range(T):
    N = int(input())
    print(DP[N][1]+DP[N][2]+DP[N][3])