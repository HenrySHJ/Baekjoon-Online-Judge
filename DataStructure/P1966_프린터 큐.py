import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))

    queue = deque()
    for i in range(N):
        queue.append((A[i],i))

    count = 0
    while queue:
        max_priority = max(queue, key=lambda x: x[0])[0]

        now,now_idx = queue.popleft()

        if now == max_priority:
            count += 1
            if now_idx == M:
                print(count)
                break
        
        else:
            queue.append((now,now_idx))