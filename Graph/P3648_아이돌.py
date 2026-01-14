import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def get_node(x):
    if x > 0:
        return x*2
    else:
        return -x*2 + 1

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

while True:
    try:
        N,M = map(int,input().split())
    except ValueError:
        break

    graph = [[] for _ in range(N*2+2)]
    rev_graph = [[] for _ in range(N*2+2)]

    # 상근이는 무조건 합격 not 1 -> 1추가
    graph[get_node(-1)].append(get_node(1))
    rev_graph[get_node(1)].append(get_node(-1))

    for _ in range(M):
        a,b = map(int,input().split())
        u = get_node(a)
        v = get_node(b)

        graph[u^1].append(v)
        graph[v^1].append(u)
        rev_graph[v].append(u^1)
        rev_graph[u].append(v^1)

    # 정방향 DFS + 종료시점 stack
    visited = [False]*(N*2+2)
    stack = []
    for i in range(2,N*2+2):
        if not visited[i]:
            DFS(i)

    # 역방향 DFS + scc_id 지정
    visited = [False]*(N*2+2)
    scc_id = [0]*(N*2+2)
    scc_count = 0
    while stack:
        now = stack.pop()
        if not visited[now]:
            scc_count += 1
            rev_DFS(now,scc_count)

    ans = True
    for i in range(1,N+1):
        if scc_id[i*2] == scc_id[i*2+1]:
            ans = False
            break

    if ans:
        print('yes')
    else:
        print('no')