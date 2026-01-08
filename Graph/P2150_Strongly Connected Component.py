import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V,E = map(int,input().split())

graph = [[] for _ in range(V+1)]       # 정방향 그래프
rev_graph = [[] for _ in range(V+1)]   # 역방향 그래프
for _ in range(E):
    u,v = map(int,input().split())
    graph[u].append(v)
    rev_graph[v].append(u)

# finish_time 순서대로 stack에 넣기
stack = []
visited = [False]*(V+1)

# 정방향 DFS로 finish_time순으로 채우기
def DFS(now):
    visited[now] = True
    for nxt in graph[now]:
        if not visited[nxt]:  
            DFS(nxt)
    stack.append(now)

for i in range(1,V+1):
    if not visited[i]:
        DFS(i)

# 역방향 DFS 준비 작업
visited = [False]*(V+1)
result = []

# 역방향 DFS로 SCC
def rev_DFS(now,scc):
    visited[now] = True
    scc.append(now)
    for nxt in rev_graph[now]:
        if not visited[nxt]:
            rev_DFS(nxt,scc)

# finish_time이 늦은 순서부터 scc 연결
while stack:
    now = stack.pop()
    if not visited[now]:
        scc = []
        rev_DFS(now, scc)
        result.append(sorted(scc))

# 정답 출력
result.sort()
print(len(result))

for scc in result:
    print(*(scc), -1)