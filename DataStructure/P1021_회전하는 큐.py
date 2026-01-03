import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
A = list(map(int,input().split()))

num_list = [i+1 for i in range(N)]

queue = deque(num_list)

ans = 0
for n in A:
    length = len(queue)

    idx = -1
    for i in range(length):
        if n == queue[i]:
            idx = i
            break

    if idx <= length - idx:
        for i in range(idx):
            now = queue.popleft()
            queue.append(now)

        now = queue.popleft()
        ans += idx

    elif idx >= length - idx:
        for i in range(length-idx):
            now = queue.pop()
            queue.appendleft(now)

        now = queue.popleft()
        ans += length-idx

print(ans)