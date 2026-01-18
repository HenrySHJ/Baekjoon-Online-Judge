import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

operation = list(map(int,input().split()))

queue = deque()
queue.append((A[0],0,0,0,0,0))

max_ans = -sys.maxsize
min_ans = sys.maxsize

while queue:
    cur, idx, a, s, m, d = queue.popleft()

    if idx == N - 1:
        max_ans = max(max_ans,cur)
        min_ans = min(min_ans,cur)
        continue

    for i in range(4):
        if i == 0:
            if operation[i] > a:
                queue.append((cur + A[idx + 1], idx + 1, a + 1, s, m, d))
        elif i == 1:
            if operation[i] > s:
                queue.append((cur - A[idx + 1], idx + 1, a, s + 1, m, d))

        elif i == 2:
            if operation[i] > m:
                queue.append((cur * A[idx + 1], idx + 1, a, s, m + 1, d))

        elif i == 3:
            if operation[i] > d:
                if cur < 0:
                    queue.append((-(abs(cur) // A[idx + 1]), idx + 1, a, s, m, d + 1))
                else:
                    queue.append((cur // A[idx + 1], idx + 1, a, s, m, d + 1))

print(max_ans)
print(min_ans)