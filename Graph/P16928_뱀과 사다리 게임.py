import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

ladder = []
snake = []

for _ in range(N):
    x, y = map(int, input().split())
    ladder.append((x, y))

for _ in range(M):
    x, y = map(int, input().split())
    snake.append((x, y))

def BFS(now):
    global ans
    queue = deque()
    queue.append((now, 0))

    while queue:
        now, roll = queue.popleft()

        if now == 100:
            ans = min(ans, roll)
            break

        for k in range(1,7):
            if (now + k) <= 100:
                if visited[now + k]:
                    continue

                visited[now + k] = True
                move = False
                
                for l in ladder:
                    if now + k == l[0]:
                        visited[l[1]] = True
                        queue.append((l[1], roll + 1))
                        move = True
                        break
                
                for s in snake:
                    if now + k == s[0]:
                        visited[s[1]] = True
                        queue.append((s[1], roll + 1))
                        move = True
                        break

                if not move:
                    queue.append((now + k, roll + 1))

ans = sys.maxsize
visited = [False] * 101
BFS(1)
print(ans)