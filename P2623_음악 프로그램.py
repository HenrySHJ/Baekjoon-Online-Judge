import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)

for _ in range(M):
    seq = list(map(int,input().split()))

    for i in range(1,seq[0]):
        graph[seq[i]].append(seq[i+1])
        indegree[seq[i+1]] += 1
    
queue = deque()
for i in range(1,N+1):
    if indegree[i] == 0:
        queue.append(i)

result = []
while queue:
    now = queue.popleft()
    result.append(now)
    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)

if len(result) == N:
    for i in range(N):
        print(result[i])
else:
    print(0)