import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

cost = list(map(int,input().split()))
road = [list(input().strip()) for _ in range(N)]

# 정방향 그래프, 역방향 그래프
graph = [[] for _ in range(N)]
rev_graph = [[] for _ in range(N)]

# 입력받은 road를 인접 그래프 형태로 변환
for i in range(N):
    for j in range(N):
        if road[i][j] == '1':
            graph[i].append(j)
            rev_graph[j].append(i)

# 정방향 DFS
def DFS(now):
    visited[now] = True

    for nxt in graph[now]:
        if not visited[nxt]:
            DFS(nxt)

    # 종료시점 순으로 stack에 담기
    stack.append(now)

# 역방향 DFS
def rev_DFS(now,count):
    visited[now] = True
    scc_id[now] = count

    for nxt in rev_graph[now]:
        if not visited[nxt]:  
            rev_DFS(nxt,count)

# 정방향 그래프에서 종료시점 순으로 stack
stack = []
visited = [False]*N

for i in range(N):
    if not visited[i]:
        DFS(i)

# 역방향 그래프에서 SCC끼리 묶기
scc_id = [0]*N
visited = [False]*N
count = 0

# 한 탐색에서 나오는 노드끼리 SCC 형성
while stack:
    now = stack.pop()
    if not visited[now]:
        rev_DFS(now,count)
        count += 1

# scc 그룹별 최소 금액
scc_cost = [sys.maxsize]*count
for i in range(N):
    scc_cost[scc_id[i]] = min(scc_cost[scc_id[i]],cost[i])

print(sum(scc_cost))