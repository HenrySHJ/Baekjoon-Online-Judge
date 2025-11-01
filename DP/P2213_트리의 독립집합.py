import sys
input = sys.stdin.readline

N = int(input())

W = list(map(int,input().split()))
W.insert(0,0)

tree = [[] for _ in range(N+1)]
DP = [[0,0] for _ in range(N+1)]
track = [[],[]]
visited = [False]*(N+1)

for _ in range(N-1):
    s,e = map(int,input().split())
    tree[s].append(e)
    tree[e].append(s)

def DFS(v):
    visited[v] = True

    DP[v][0] = 0
    DP[v][1] = W[v]

    for next in tree[v]:
        if visited[next]:
            continue
        DFS(next)
        DP[v][0] += max(DP[next][0],DP[next][1])
        DP[v][1] += DP[next][0]

path = []

def trace(v, p):
    if p == 1:   
        choose = 0
    else:
        choose = 1 if DP[v][1] >= DP[v][0] else 0

    if choose == 1:
        path.append(v)

    for next in tree[v]:
        if visited[next]: 
            continue
        visited[next] = True
        trace(next, choose)

DFS(1)

visited = [False]*(N+1)
visited[1] = True

if DP[1][1] >= DP[1][0]:
    print(DP[1][1])
    trace(1, 0)
else:
    print(DP[1][0])
    trace(1, 1)

path.sort()
print(*path)