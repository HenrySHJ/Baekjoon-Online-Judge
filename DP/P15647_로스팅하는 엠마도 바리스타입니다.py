import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())

tree = [[] for _ in range(N+1)]
DP = [0]*(N+1)
connected = [0]*(N+1)

for _ in range(N-1):
    u,v,d = map(int,input().split())
    tree[u].append((v,d))
    tree[v].append((u,d))

def DFS(v):
    visited[v] = True

    for next,dist in tree[v]:
        if visited[next]:
            continue
        
        DFS(next)
        # 하위 노드 개수 찾기
        connected[v] += 1 + connected[next]
        DP[v] += DP[next] + dist*(connected[next]+1)

def DFS_reroot(v):
    visited[v] = True
    for next, dist in tree[v]:
        if visited[next]:
            continue
        
        DP[next] = DP[v] + dist*(N - 2*(connected[next] + 1))
        DFS_reroot(next)

visited = [False]*(N+1)
DFS(1)

visited = [False]*(N+1)
DFS_reroot(1)

# 정답 출력
for i in range(1,N+1):
    print(DP[i])