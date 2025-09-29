from collections import deque

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
M = int(input())
C = list(map(int,input().split()))

queue = deque()

# A[i] == 0 인 것만 큐에 추가
for i in range(N):
    if A[i] == 0:
        queue.appendleft(B[i])

# 이후 C값을 하나씩 넣고, 맨 앞 출력
for x in C:
    queue.append(x)
    print(queue.popleft(), end=" ")