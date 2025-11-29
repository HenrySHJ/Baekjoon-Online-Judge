import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
SCV = list(map(int,input().split()))

# SCV 리스트 길이 3으로 맞춰주기
while len(SCV) < 3:
    SCV.append(0)

a,b,c = SCV

# DP[i][j][k] : a의 체력 i, b의 체력 j, c의 체력 k일때 최소 공격 횟수
DP = [[[-1]*61 for _ in range(61)] for _ in range(61)]
Mutalisk = [(9,3,1),(9,1,3),(3,9,1),(3,1,9),(1,9,3),(1,3,9)]

queue = deque()
queue.append((a,b,c))
DP[a][b][c] = 0

while queue:
    x,y,z = queue.popleft()

    # SCV가 모두 체력 0이면 정답 출력
    if x == 0 and y == 0 and z == 0:
        print(DP[0][0][0])
        break

    for i,j,k in Mutalisk:
        nx = max(0,x-i)
        ny = max(0,y-j)
        nz = max(0,z-k)
        if DP[nx][ny][nz] == -1:
            DP[nx][ny][nz] = DP[x][y][z] + 1
            queue.append((nx,ny,nz))