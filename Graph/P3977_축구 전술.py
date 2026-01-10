import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

T = int(input())

# 정방향 DFS
def DFS(now):
    visited[now] = True

    for nxt in graph[now]:
        if not visited[nxt]:
            DFS(nxt)
    stack.append(now)

def rev_DFS(now,count):
    visited[now] = True
    scc_id[now] = count

    for nxt in rev_graph[now]:
        if not visited[nxt]:
            rev_DFS(nxt,count)

for _ in range(T):
    N,M = map(int,input().split())

    graph = [[] for _ in range(N)]
    rev_graph = [[] for _ in range(N)]
    for _ in range(M+1):
        try:
            A,B = map(int,input().split())
            graph[A].append(B)
            rev_graph[B].append(A)

        # 마지막 줄 빈칸 입력
        except ValueError:
            pass
    
    # 정방향 DFS로 종료 시점대로 stack
    stack = []
    visited = [False]*N
    for i in range(N):
        if not visited[i]:
            DFS(i)

    # 역방향 DFS로 SCC끼리 묶기
    visited = [False]*N
    scc_id = [-1]*N
    count = 0
    while stack:
        now = stack.pop()
        if not visited[now]:
            rev_DFS(now,count)
            count += 1

    # scc_indegree[scc 그룹 번호] = 진입차수
    scc_indegree = [0]*count
    for now in range(N):
        for nxt in graph[now]:
            if scc_id[now] != scc_id[nxt]:
                scc_indegree[scc_id[nxt]] += 1

    # scc_group[scc 그룹 번호] = [소속된 노드..]
    scc_group = [[] for _ in range(count)]
    for i in range(N):
        scc_group[scc_id[i]].append(i)

    # scc_indegree가 0인 그룹만 모으기
    result = []
    group_count = 0
    for i in range(count):
        if scc_indegree[i] == 0:
            for j in scc_group[i]:
                result.append(j)
            group_count += 1

    # scc_indegree가 0인 그룹이 2개 이상이면 출력불가
    if group_count < 2:
        for n in result:
            print(n)
    else:
        print('Confused')
    print()