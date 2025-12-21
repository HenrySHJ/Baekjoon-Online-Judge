import sys
input = sys.stdin.readline

N,M = map(int,input().split())

K = int(input())

work = []
for _ in range(K):
    work.append(tuple(map(int,input().split())))

# DP[i][j] : i,j 좌표에 도달하는 방법
DP = [[0]*(M+1) for _ in range(N+1)]

for i in range(N+1):
    DP[i][0] = 1
    if (i,0,i+1,0) in work or (i+1,0,i,0) in work:
        break   

for j in range(M+1):
    DP[0][j] = 1
    if (0,j,0,j+1) in work or (0,j+1,0,j) in work:
        break
        
for i in range(1,N+1):
    for j in range(1,M+1):
        if (i,j,i-1,j) not in work and (i-1,j,i,j) not in work:
            DP[i][j] += DP[i-1][j]
        if (i,j,i,j-1) not in work and (i,j-1,i,j) not in work:
            DP[i][j] += DP[i][j-1]

print(DP[N][M])