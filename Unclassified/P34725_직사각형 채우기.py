import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = [[0]*M for _ in range(N)]

num = 1
for i in range(N//2):
    for j in range(M//2):
        A[i][j] = num
        A[i][M-1-j] = num
        A[N-1-i][j] = num
        A[N-1-i][M-1-j] = num
        num += 1

for i in range(N):
    print(*A[i])