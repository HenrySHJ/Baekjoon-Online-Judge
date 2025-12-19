import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    s,e,w = map(int,input().split())
    tree[s].append((e,w))
    tree[e].append((s,w))

def BFS(start,end):
    queue = deque()
    queue.append((start,0))

    while queue:
        now,dist = queue.popleft()
        visited[now] = True

        if now == end:
            return dist
        
        for nxt,weight in tree[now]:
            if not visited[nxt]:
                queue.append((nxt,dist+weight))

for _ in range(M):
    a,b = map(int,input().split())
    visited = [False]*(N+1)
    print(BFS(a,b))