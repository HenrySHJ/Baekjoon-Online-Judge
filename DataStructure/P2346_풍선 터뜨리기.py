import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

queue = deque()
for i in range(N):
    queue.append((i + 1, A[i]))

# 최초 처리
now, balloon = queue.popleft()
print(now, end = " ")

num = balloon
while queue:
    if num >= 1:
        now, balloon = queue.popleft()
    else:
        now, balloon = queue.pop()

    if num == 1 or num == -1:
        print(now, end = " ")
        num = balloon

    elif num >= 1:
        num -= 1
        queue.append((now, balloon))

    else:
        num += 1
        queue.appendleft((now, balloon))