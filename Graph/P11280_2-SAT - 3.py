import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# x와 ㄱx에 대해서 정수로 표현
def get_node(x):
    if x > 0:
        return x*2
    else:
        return -x*2 + 1

# XOR로 node에 대해 부정형 계산
def s_not(node):
    return node^1 

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

graph = [[] for _ in range(N*2+2)]
rev_graph = [[] for _ in range(N*2+2)]
for _ in range(M):
    i,j = map(int,input().split())
    i_node = get_node(i)
    j_node = get_node(j)

    graph[s_not(i_node)].append(j_node)
    graph[s_not(j_node)].append(i_node)
    rev_graph[i_node].append(s_not(j_node))
    rev_graph[j_node].append(s_not(i_node))

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
    print(1)
else:
    print(0)