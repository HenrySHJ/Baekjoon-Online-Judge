import sys
from collections import deque
input = sys.stdin.readline

A,B = map(int,input().split())

def BFS(v):
    queue = deque()
    queue.append((v,0))
    while queue:
        now,depth = queue.popleft()
        if now == B:
            return depth+1
        
        if now*2 <= B:
            queue.append((now*2,depth+1))
        if now*10+1 <= B:
            queue.append((now*10+1,depth+1))
    return -1

print(BFS(A))
