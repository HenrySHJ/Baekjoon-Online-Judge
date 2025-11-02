import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())

tree = [[] for _ in range(N+1)]

A = list(map(int,input().split()))
A.insert(0,0)

visited = [False]*(N+1)
DP = [[0,0] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def DFS(v):
    visited[v] = True
    
    DP[v][0] = 0
    DP[v][1] = A[v]

    for next in tree[v]:
        if visited[next]:
            continue
        DFS(next)
        DP[v][0] += max(DP[next][0],DP[next][1])
        DP[v][1] += DP[next][0]

DFS(1)
print(max(DP[1][0],DP[1][1]))