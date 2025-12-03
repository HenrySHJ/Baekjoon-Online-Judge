import sys
import math
input = sys.stdin.readline

N,M = map(int,input().split())

board = [input().strip() for _ in range(N)]

ans = -1

for i in range(N):
    for j in range(M):
        # 가능한 공차(dx) : -N ~ N
        for dx in range(-N, N+1):
            # 가능한 공차(dy) : -M ~ M
            for dy in range(-M, M+1):
                # 공차가 모두 0이면 숫자 못 이룸
                if dx == 0 and dy == 0:
                    continue

                x, y = i, j
                num = ""

                while 0 <= x < N and 0 <= y < M:
                    num += board[x][y]
                    val = int(num)

                    # 정수 제곱근 찾기
                    r = int(math.isqrt(val))
                    if r * r == val:
                        ans = max(ans, val)

                    x += dx
                    y += dy

print(ans)