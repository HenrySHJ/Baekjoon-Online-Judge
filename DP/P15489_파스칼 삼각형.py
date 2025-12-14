import sys
input = sys.stdin.readline

R,C,W = map(int, input().split())

DP = [[1]*(R+W) for _ in range(R+W)]
for i in range(2, R+W):
    for j in range(1,i):
        DP[i][j] = DP[i-1][j-1] + DP[i-1][j]

ans = 0
for i in range(W):
    for j in range(i+1):
        ans += DP[R+i-1][C+j-1]
print(ans)