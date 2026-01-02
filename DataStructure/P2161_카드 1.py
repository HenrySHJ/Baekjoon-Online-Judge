from collections import deque

N = int(input())

cards = [i+1 for i in range(N)]

queue = deque(cards)

while queue:
    now = queue.popleft()
    print(now,end=' ')

    if len(queue) >= 2:
        nxt = queue.popleft()
        queue.append(nxt)
    else:
        if queue:
            print(queue[0])
        break