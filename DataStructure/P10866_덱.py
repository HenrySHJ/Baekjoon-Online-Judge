import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

queue = deque()
for _ in range(N):
    order = list(input().split())

    # 정수 X를 덱의 앞에 넣는다.
    if order[0] == 'push_front':
        X = order[1]
        queue.appendleft(X)

    # 정수 X를 덱의 뒤에 넣는다.
    elif order[0] == 'push_back':
        X = order[1]
        queue.append(X)

    # 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif order[0] == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    # 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif order[0] == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)

    # 덱에 들어있는 정수의 개수를 출력한다.
    elif order[0] == 'size':
        print(len(queue))

    # 덱이 비어있으면 1을, 아니면 0을 출력한다.
    elif order[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    # 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif order[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    # 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif order[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)