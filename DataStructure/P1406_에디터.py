import sys
input = sys.stdin.readline

start = list(input().strip())

M = int(input())

cursor = len(start)

left = []
right = []
for i in range(cursor):
    left.append(start[i])

for _ in range(M):
    order = list(input().split())

    if order[0] == 'L':
        if left:
            right.append(left.pop())

    elif order[0] == 'D':
        if right:
            left.append(right.pop())

    elif order[0] == 'B':
        if left:
            left.pop()

    elif order[0] == 'P':
        left.append(order[1])

for i in range(len(left)):
    print(left[i],end='')
for i in range(len(right)-1,-1,-1):
    print(right[i],end='')