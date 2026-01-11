import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
rev_graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    rev_graph[b].append(a)

ATM = [0]+[int(input()) for _ in range(N)]

S,P = map(int,input().split())
res = list(map(int,input().split()))

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

# 출발지 기준 정방향 DFS
visited = [False]*(N+1)
stack = []
DFS(S)

# 출발지에서 못 가는 정점에 대한 DFS
for i in range(1,N+1):
    if not visited[i]:
        DFS(i)

# 역방향 DFS로 scc끼리 묶기
visited = [False]*(N+1)
scc_id = [0]*(N+1)
scc_count = 0

while stack:
    now = stack.pop()
    if not visited[now]:
        scc_count += 1
        rev_DFS(now,scc_count)

# scc_group[scc 그룹 번호] = [구성 노드..]
scc_group = [[] for _ in range(scc_count+1)]
for i in range(1,N+1):
    scc_group[scc_id[i]].append(i)

# scc_max[scc 그룹 번호] = scc 그룹별 인출 가능한 현금 합
scc_max = [0]*(scc_count+1)
for i in range(1,N+1):
    scc_max[scc_id[i]] += ATM[i]

# scc 진입차수 계산
queue = deque()
scc_indegree = [0]*(scc_count+1)

# scc_graph : scc(vertex)의 인접그래프
scc_graph = [[] for _ in range(scc_count+1)]
for now in range(1,N+1):
    for nxt in graph[now]:
        if scc_id[now] != scc_id[nxt]:
            scc_indegree[scc_id[nxt]] += 1
            scc_graph[scc_id[now]].append(scc_id[nxt])

for i in range(1,scc_count+1):
    if scc_indegree[i] == 0:
        queue.append(i)

# DP[i] : scc_id가 i번인 그룹에서의 최대 인출 가능한 현금 합
DP = [-1]*(scc_count+1)
DP[scc_id[S]] = scc_max[scc_id[S]]

# DP 갱신 & 위상정렬
while queue:
    now = queue.popleft()

    for nxt in scc_graph[now]:
        # 출발지로부터 도달 가능한 경우만 갱신
        if DP[now] != -1:
            DP[nxt] = max(DP[nxt],DP[now] + scc_max[nxt])

        # 진입차수 0 되면 append
        scc_indegree[nxt] -= 1
        if scc_indegree[nxt] == 0:
            queue.append(nxt)    

# 최종 출력
ans = 0
for r in res:
    ans = max(ans,DP[scc_id[r]])

print(ans)