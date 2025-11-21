import sys
input = sys.stdin.readline

T,W = map(int,input().split())
tree = [0]+[int(input()) for _ in range(T)]

# DP[i][j][k] : i초에 j번 움직였고 k번 나무 밑에 있을 때 최대자두 개수
DP = [[[-1]*3 for _ in range(W+1)] for _ in range(T+1)]

# 초기화
DP[0][0][1] = 0

for i in range(T):
    for j in range(W+1):
        if DP[i][j][1] != -1:
            DP[i+1][j][1] = max(DP[i+1][j][1],DP[i][j][1] + (1 if tree[i+1] == 1 else 0))
            if j+1 <= W:
                DP[i+1][j+1][2] = max(DP[i+1][j+1][2],DP[i][j][1] + (1 if tree[i+1] == 2 else 0))

        if DP[i][j][2] != -1:
            DP[i+1][j][2] = max(DP[i+1][j][2],DP[i][j][2] + (1 if tree[i+1] == 2 else 0))
            if j+1 <= W:
                DP[i+1][j+1][1] = max(DP[i+1][j+1][2],DP[i][j][2] + (1 if tree[i+1] == 1 else 0))


ans = 0
for j in range(W+1):
    for k in range(1,3):
        ans = max(ans,DP[T][j][k])

print(ans)