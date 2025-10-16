import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

road = []
graph = [[] for _ in range(N+1)]
gold = [-sys.maxsize] * (N+1)
parent = [-1] * (N+1)

for _ in range(M):
    u, v, w = map(int, input().split())
    road.append((u, v, w))
    graph[u].append(v)

def reachable_from(start_nodes):
    q = deque(start_nodes)
    visited = [False] * (N+1)
    for s in start_nodes:
        visited[s] = True

    while q:
        cur = q.popleft()
        if cur == N:
            return True
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
    return False

def bellman_ford(start):
    gold[start] = 0
    updated_nodes = []

    for i in range(N):
        updated = []
        for a, b, c in road:
            if gold[a] != -sys.maxsize and gold[b] < gold[a] + c:
                gold[b] = gold[a] + c
                parent[b] = a
                if i == N-1:
                    updated.append(b)
        if i == N-1:
            updated_nodes = updated

    # 양수 사이클이 N까지 영향을 줄 수 있는지 확인
    if updated_nodes and reachable_from(updated_nodes):
        return -1
    return 0

result = bellman_ford(1)

if result == -1 or gold[N] == -sys.maxsize:
    print(-1)
else:
    path = []
    cur = N
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    print(*path[::-1])