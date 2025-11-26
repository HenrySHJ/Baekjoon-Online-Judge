import sys
from collections import deque
input = sys.stdin.readline

S = input().strip()
T = input().strip()

queue = deque()
queue.append(T)
while queue:
    now = queue.popleft()
    if len(now) == len(S):
        if now == S:
            print(1)
        else:
            print(0)
        
        break

    if now[-1] == 'A':
        now = now[:-1]
    else:
        now = now[:-1]
        now = now[::-1]

    queue.append(now)