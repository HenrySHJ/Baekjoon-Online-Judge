import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)   # 위상 정렬
ans = [0]*(N+1)

for i in range(M):
    s,e = map(int,input().split())
    graph[s].append(e)
    indegree[e] += 1

queue = deque()
for i in range(1,N+1):
    if indegree[i] == 0:
        queue.append((i,1))

while queue:
    now,semester = queue.popleft()
    ans[now] = semester

    for subject in graph[now]:
        indegree[subject] -= 1
        if indegree[subject] == 0:
            queue.append((subject,semester+1))

for i in range(1,N+1):
    print(ans[i],end=' ')