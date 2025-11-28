import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = [list(input().strip()) for _ in range(N)]
B = [list(input().strip()) for _ in range(N)]

ans = 0

def flip(i,j):
    for x in range(i,i+3):
        for y in range(j,j+3):
            if A[x][y] == '1':
                A[x][y] = '0'
            else:
                A[x][y] = '1'

for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            flip(i,j)
            ans += 1

if A == B:
    print(ans)
else:
    print(-1)
