import sys
input = sys.stdin.readline

N,M = map(int,input().split())

A = [[0]+list(map(int,input().split())) for _ in range(N)]
A.insert(0,[0]*(N+1))

S = [[0]*(M+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        S[i][j] = S[i-1][j] + S[i][j-1] + A[i][j] - S[i-1][j-1]

K = int(input())
for _ in range(K):

    i,j,x,y = map(int,input().split())
    print(S[x][y] - S[x][j-1] - S[i-1][y] + S[i-1][j-1])