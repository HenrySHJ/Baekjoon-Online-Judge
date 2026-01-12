import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 정방향 DFS + 종료시점 순으로 stack
def DFS(now):
    visited[now] = True

    for nxt in graph[now]:
        if not visited[nxt]:
            DFS(nxt)
    stack.append(now)

# 역방향 DFS
def rev_DFS(now,count):
    visited[now] = True
    scc_id[now] = count

    for nxt in rev_graph[now]:
        if not visited[nxt]:
            rev_DFS(nxt,count)

while True:
    try:
        N,M = map(int,input().split())
    except ValueError:
        break

    E = list(map(int,input().split()))

    graph = [[] for _ in range(N+1)]
    rev_graph = [[] for _ in range(N+1)]
    for i in range(M):
        u = E[i*2]
        v = E[i*2+1]
        graph[u].append(v)
        rev_graph[v].append(u)

    # DFS + 종료시점 순으로 stack
    visited = [False]*(N+1)
    stack = []
    for i in range(1,N+1):
        if not visited[i]:
            DFS(i)

    # 역방향 DFS + SCC 그룹 지정
    visited = [False]*(N+1)
    scc_id = [0]*(N+1)
    id_count = 0
    while stack:
        now = stack.pop()

        if not visited[now]:
            id_count += 1
            rev_DFS(now,id_count)

    # scc_group : scc_id별 속한 노드
    scc_group = [[] for _ in range(id_count+1)]
    for i in range(1,N+1):
        scc_group[scc_id[i]].append(i)

    # scc_rev_indegree : scc의 역 진입차수 구하기
    scc_rev_indegree = [0]*(id_count+1)
    for now in range(1,N+1):
        for nxt in rev_graph[now]:
            if scc_id[now] != scc_id[nxt]:
                scc_rev_indegree[scc_id[nxt]] += 1

    # 정답 출력
    ans = []
    for now in range(1,id_count+1):
        if scc_rev_indegree[now] == 0:
            for node in scc_group[now]:
                ans.append(node)

    ans.sort()
    print(*ans)