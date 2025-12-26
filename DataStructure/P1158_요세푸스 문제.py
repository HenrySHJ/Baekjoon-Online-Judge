import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())

queue = deque()
for i in range(1,N+1):
    queue.append(i)

count = 0
ans = []
while queue:
    count += 1

    now = queue.popleft()
    if count == K:
        ans.append(now)
        count = 0
    else:
        queue.append(now)

print("<",end='')
for i in range(N):
    print(str(ans[i]),end='')
    if i != N-1:
        print(",",end=' ')
print(">",end='')