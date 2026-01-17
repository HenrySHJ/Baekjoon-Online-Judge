import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 정방향 DFS + 종료시점 stack
def DFS(now):
    visited[now] = True
    
    for nxt in graph[now]:
        if not visited[nxt]:
            DFS(nxt)
    stack.append(now)

# 역방향 DFS + scc_id 지정
def rev_DFS(now,count):
    visited[now] = True
    scc_id[now] = count

    for nxt in rev_graph[now]:
        if not visited[nxt]:
            rev_DFS(nxt,count)

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
rev_graph = [[] for _ in range(N+1)]
for _ in range(M):
    v,w = map(int,input().split())
    graph[v].append(w)
    rev_graph[w].append(v)

# 정방향 DFS + 종료시점 stack
visited = [False]*(N+1)
stack = []
for i in range(1,N+1):
    if not visited[i]:
        DFS(i)

# 역방향 DFS + scc_id 지정
visited = [False]*(N+1)
scc_id = [0]*(N+1)
scc_count = 0
while stack:
    now = stack.pop()
    if not visited[now]:
        scc_count += 1
        rev_DFS(now,scc_count)

if scc_count == 1:
    print("Yes")
else:
    print("No")