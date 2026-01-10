import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())

# 정방향 DFS
def DFS(now):
    visited[now] = True

    for nxt in graph[now]:
        if not visited[nxt]:
            DFS(nxt)
    stack.append(now)

# 역방향 DFS로 SCC끼리 묶기
def rev_DFS(now,group_cnt):
    visited[now] = True
    scc_id[now] = group_cnt

    for nxt in rev_graph[now]:
        if not visited[nxt]:
            rev_DFS(nxt,group_cnt)

for _ in range(T):
    N,M = map(int,input().split())

    graph = [[] for _ in range(N+1)]
    rev_graph = [[] for _ in range(N+1)]
    for _ in range(M):
        x,y = map(int,input().split())
        graph[x].append(y)
        rev_graph[y].append(x)

    # 정방향 그래프에서 그 외 finish time 정리
    visited = [0]*(N+1)
    stack = []
    for i in range(1,N+1):
        if not visited[i]:
            DFS(i)

    # 같은 SCC에 있는 정점끼리 묶기
    scc_id = [0]*(N+1)
    group_cnt = 0
    visited = [False]*(N+1)

    while stack:
        now = stack.pop()
        if not visited[now]:
            group_cnt += 1
            rev_DFS(now, group_cnt)

    # SCC에서의 진입차수 계산
    scc_indegree = [0]*(group_cnt+1)
    for now in range(1,N+1):
        for nxt in graph[now]:
            if scc_id[now] != scc_id[nxt]:
                scc_indegree[scc_id[nxt]] += 1

    # 진입차수가 0인 SCC의 개수 세기
    result = 0
    for i in range(1,group_cnt+1):
        if scc_indegree[i] == 0:
            result += 1

    print(result)