import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

T = int(input())

def DFS(v):
    visited[v] = True
    subsize[v] = 1

    for next in tree[v]:
        if visited[next]:
            continue
        DFS(next)
        subsize[v] += subsize[next]
        DP[v] += DP[next] + subsize[next]*(A[v]^A[next])

def reroot(v):
    visited[v] = True

    for next in tree[v]:
        if visited[next]:
            continue
        DP[next] = DP[v] + (A[v]^A[next])*(N - 2*subsize[next])
        reroot(next)

for _ in range(T):
    N = int(input())

    A = list(map(int,input().split()))
    A.insert(0,0)

    tree = [[] for _ in range(N+1)]
    subsize = [0]*(N+1)   # 서브트리 개수
    DP = [0]*(N+1)    # 누적 시행 비용

    for _ in range(N-1):
        a,b = map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)

    visited = [False]*(N+1)
    DFS(1)
    visited = [False]*(N+1)
    reroot(1)

    for i in range(1,N+1):
        print(DP[i],end=' ')
    print()