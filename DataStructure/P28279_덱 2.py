import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

queue = deque()

for _ in range(N):
    order = list(map(int, input().split()))

    if order[0] == 1:
        queue.appendleft(order[1])

    elif order[0] == 2:
        queue.append(order[1])

    elif order[0] == 3:
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif order[0] == 4:
        if queue:
            print(queue.pop())
        else:
            print(-1)

    elif order[0] == 5:
        print(len(queue))

    elif order[0] == 6:
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif order[0] == 7:
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif order[0] == 8:
        if queue:
            print(queue[len(queue) - 1])
        else:
            print(-1)