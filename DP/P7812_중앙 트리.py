import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
while True:
    N = int(input())
    if N == 0:
        break

    tree = [[] for _ in range(N)]
    subsize = [0]*N   # 자신 포함 하위 노드의 개수
    DP = [0]*N        # 메모제이션

    for _ in range(N-1):
        a,b,w = map(int,input().split())
        tree[a].append((b,w))
        tree[b].append((a,w))

    def DFS(v):
        visited[v] = True
        subsize[v] = 1

        for next,weight in tree[v]:
            if visited[next]:
                continue
            DFS(next)
            subsize[v] += subsize[next]
            DP[v] += DP[next] + weight*subsize[next]

    def reroot(v):
        visited[v] = True

        for next,weight in tree[v]:
            if visited[next]:
                continue
            DP[next] = DP[v] + weight*(N - 2 * subsize[next])
            reroot(next)

    visited = [False]*N
    DFS(0)
    visited = [False]*N
    reroot(0)

    ans = sys.maxsize
    for i in range(N):
        ans = min(ans,DP[i])

    print(ans)