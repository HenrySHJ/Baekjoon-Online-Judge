import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N,M = map(int,input().split())

# x에 대한 노드로의 변환
def get_node(x):
    if x > 0:
        return x*2
    else:
        return -x*2 + 1

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

graph = [[] for _ in range(M*2+2)]
rev_graph = [[] for _ in range(M*2+2)]

for _ in range(N):
    x,y = map(int,input().split())
    u = get_node(x)
    v = get_node(y)

    graph[u^1].append(v)
    graph[v^1].append(u)
    rev_graph[v].append(u^1)
    rev_graph[u].append(v^1)

# 정방향 DFS + 종료시점 stack
visited = [False]*(M*2+2)
stack = []
for i in range(2,M*2+2):
    if not visited[i]:
        DFS(i)

# 역방향 DFS + scc_id 지정
visited = [False]*(M*2+2)
scc_id = [0]*(M*2+2)
scc_count = 0
while stack:
    now = stack.pop()
    if not visited[now]:
        scc_count += 1
        rev_DFS(now,scc_count)

# 논리적 모순이 생기는지 확인
ans = True
for i in range(1,M+1):
    if scc_id[i*2] == scc_id[i*2 + 1]:
        ans = False
        break

if ans:
    print('^_^')
else:
    print('OTL')