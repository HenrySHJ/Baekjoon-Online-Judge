import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

temp = 1
kmax = 0
while temp <= N:
    temp *= 2
    kmax += 1

parent = [[0 for j in range(N+1)] for i in range(kmax+1)]
tree = [[] for _ in range(N+1)]
depth = [0]*(N+1)
dist_root = [0]*(N+1)
visited = [False]*(N+1)

def BFS(node):
    queue = deque()
    queue.append(node)
    depth[node] = 0
    visited[node] = True
    while queue:
        now = queue.popleft()
        for next,distance in tree[now]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                parent[0][next] = now
                dist_root[next] = dist_root[now] + distance
                depth[next] = depth[now] + 1

def executeLCA(a,b):
    if depth[a] < depth[b]:
        temp = a
        a = b
        b = temp

    # 깊이 맞추기
    for k in range(kmax - 1, -1, -1):
        if depth[a] - depth[b] >= 2**k:
            a = parent[k][a]

    # 공통 조상 찾기
    if a == b:
        return a

    for k in range(kmax - 1, -1, -1):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    return parent[0][a]

for _ in range(N-1):
    a,b,dist = map(int,input().split())
    tree[a].append((b,dist))
    tree[b].append((a,dist))

BFS(1)  # 루트는 어떤 수로 해도 무방

# k가 1~kmax일때를 k = 0 바탕으로 채워나가기
for k in range(1,kmax+1):
    for n in range(1,N+1):
        parent[k][n] = parent[k-1][parent[k-1][n]]

M = int(input())
for _ in range(M):
    a,b = map(int,input().split())

    # 공통 조상까지 도달하는데 거리를 누적합
    LCA = executeLCA(a,b)
    print(dist_root[a] + dist_root[b] - 2*dist_root[LCA])