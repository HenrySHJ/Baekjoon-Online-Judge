import sys
input = sys.stdin.readline

N,S,M = map(int,input().split())
V = list(map(int,input().split()))
DP = [[0]*(M+1) for _ in range(N+1)]

DP[0][S] = 1

for i in range(N):
    for j in range(M+1):
        if DP[i][j]:
            if j + V[i] <= M:
                DP[i+1][j+V[i]] = 1
            if j - V[i] >= 0:
                DP[i+1][j-V[i]] = 1

for i in range(M,-1,-1):
    if DP[N][i]:
        print(i)
        sys.exit()

print(-1)