import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N,M = map(int, input().split())

graph = [[] for _ in range(N*2+2)]
rev_graph = [[] for _ in range(N*2+2)]

# 절댓값으로 반환시키기
def get_node(x):
    if x > 0: 
        return x*2
    else: 
        return abs(x)*2+1

# 2*i <-> 2*i + 1
def s_not(node):
    return node ^ 1

for _ in range(M):
    u, v = map(int, input().split())
    u_node = get_node(u)
    v_node = get_node(v)
    
    graph[s_not(u_node)].append(v_node)
    graph[s_not(v_node)].append(u_node)
    
    rev_graph[v_node].append(s_not(u_node))
    rev_graph[u_node].append(s_not(v_node))

# 정방향 DFS + stack 채우기
def DFS(now):
    visited[now] = True
    for nxt in graph[now]:
        if not visited[nxt]:
            DFS(nxt)
    stack.append(now)


def rev_DFS(now, group_id):
    visited[now] = True
    scc_id[now] = group_id
    for nxt in rev_graph[now]:
        if not visited[nxt]:
            rev_DFS(nxt, group_id)

# 정방향 DFS + stack 채우기
visited = [False]*(N*2+2)
stack = []
for i in range(2,N*2+2):
    if not visited[i]:
        DFS(i)

# 역방향 DFS + scc_id 지정
visited = [False]*(N*2+2)
scc_id = [0]*(N*2+2)
cnt = 0
while stack:
    now = stack.pop()
    if not visited[now]:
        cnt += 1
        rev_DFS(now, cnt)

# 결과 출력
ans = 1
for i in range(1,N+1):
    if scc_id[i*2] == scc_id[i*2+1]:
        ans = 0
        break

print(ans)