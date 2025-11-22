import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
A = [[0]*(M+1) for _ in range(N+1)]
DP = [[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        A[i][j] = (i-1)*M + j

for i in range(1,M+1):
    DP[1][i] = 1

for i in range(1,N+1):
    DP[i][1] = 1

for i in range(2,N+1):
    for j in range(2,M+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1]

if K == 0:
    print(DP[N][M])
else:
    kx = (K-1)// M + 1
    ky = (K-1) % M + 1

    print(DP[kx][ky]*DP[N-kx+1][M-ky+1])