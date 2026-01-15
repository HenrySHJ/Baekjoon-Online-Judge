import sys
input = sys.stdin.readline

MOD = 100000

w,h = map(int,input().split())

# DP[i][j][k][l] : i,j에 도달할 수 있는 경우의 수 (k : 마지막 움직임, l : 방향전환 가능상태) 
DP = [[[[0]*2 for _ in range(2)] for _ in range(h+1)] for _ in range(w+1)]

for i in range(1,w+1):
    DP[i][1][0][0] = 1

for j in range(1,h+1):
    DP[1][j][1][0] = 1

for i in range(2,w+1):
    for j in range(2,h+1):
        DP[i][j][0][0] = (DP[i-1][j][0][0] + DP[i-1][j][0][1]) % MOD
        DP[i][j][0][1] = DP[i-1][j][1][0]

        DP[i][j][1][0] = (DP[i][j-1][1][0] + DP[i][j-1][1][1]) % MOD
        DP[i][j][1][1] = DP[i][j-1][0][0]

ans = (DP[w][h][0][1] + DP[w][h][1][0] + DP[w][h][1][1] + DP[w][h][0][0]) % MOD
print(ans)