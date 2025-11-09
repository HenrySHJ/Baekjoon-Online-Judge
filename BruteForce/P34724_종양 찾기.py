import sys
input = sys.stdin.readline

N,M = map(int,input().split())

A = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if A[i][j] == '0':
            continue
        # 좌표 유효성 검사
        if i+1 <= N-1 and j+1 <= M-1:
            if A[i][j+1] == '1' and A[i+1][j] == '1' and A[i+1][j+1] == '1':
                print(1)
                sys.exit()

print(0)