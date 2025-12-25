import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

# now를 정점으로 잡았을때의 거리
def DFS(now):
    dist = [-1]*(N+1)
    dist[now] = 0
    stack = [now]

    while stack:
        now = stack.pop()
        for nxt,weight in graph[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + weight
                stack.append(nxt)

    return dist
    
# 정점 1로부터 최장 거리에 있는 정점과 거리
dist_1 = DFS(1)

idx_u = 0
longest_u = 0
for i in range(1,N+1):
    if longest_u < dist_1[i]:
        idx_u = i
        longest_u = dist_1[i]

# 1로부터 최장거리 정점 u에서 다시 길이 측정
dist_idx_u = DFS(idx_u)

idx_v = 0
longest_v = 0
for i in range(1,N+1):
    if longest_v < dist_idx_u[i]:
        idx_v = i
        longest_v = dist_idx_u[i]

# u로부터 최장거리 정점 v에서 다시 길이 측정
dist_idx_v = DFS(idx_v)

# 정점에 대해 u,v로부터의 길이 중 큰 값 출력
for i in range(1,N+1):
    print(max(dist_idx_u[i],dist_idx_v[i]))