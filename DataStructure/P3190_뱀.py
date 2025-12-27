import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())

apple = set()
for _ in range(K):
    x,y = map(int,input().split())
    apple.add((x,y))

L = int(input())

turn = deque()
for _ in range(L):
    X,C = input().split()
    turn.append((int(X),C))

ans = 0
snake = [[False]*(N+1) for _ in range(N+1)]
snake_body = deque([(1,1)])
snake[1][1] = True

dx = [0,1,0,-1]
dy = [1,0,-1,0]
idx_dir = 0

x,y = 1,1
while True:
    ans += 1
    nx = x + dx[idx_dir]
    ny = y + dy[idx_dir]

    # 유효 좌표 확인 & 몸통 충돌 확인
    if nx <= 0 or nx > N or ny <= 0 or ny > N or snake[nx][ny]:
        break

    # 사과가 존재하는지 확인
    if (nx,ny) in apple:
        apple.remove((nx,ny))
    # 사과가 없으면 기존 꼬리 삭제
    else:
        tx,ty = snake_body.popleft()
        snake[tx][ty] = False

    snake_body.append((nx,ny))
    snake[nx][ny] = True
    x, y = nx, ny

    # 방향 전환
    if turn and turn[0][0] == ans:
        _, c = turn.popleft()
        if c == 'L':
            idx_dir = (idx_dir - 1) % 4
        elif c == 'D':
            idx_dir = (idx_dir + 1) % 4

print(ans)