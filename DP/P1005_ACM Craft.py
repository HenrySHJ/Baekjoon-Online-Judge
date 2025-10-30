import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N,K = map(int,input().split())

    time = list(map(int,input().split()))
    time.insert(0,0)

    total_time = [0]*(N+1)
    order = [[] for _ in range(N+1)]
    indegree = [0]*(N+1)

    for _ in range(K):
        s,e = map(int,input().split())
        order[s].append(e)
        indegree[e] += 1

    W = int(input())

    queue = deque()

    for i in range(1,N+1):
        if indegree[i] == 0:   
            queue.append(i)
            total_time[i] = time[i]

    while queue:
        now = queue.popleft()
        for next in order[now]:
            indegree[next] -= 1
            total_time[next] = max(total_time[next],total_time[now]+time[next])
            if indegree[next] == 0:
                queue.append(next)

    print(total_time[W])