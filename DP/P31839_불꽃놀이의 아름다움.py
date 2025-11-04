import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())

tree = [[] for _ in range(N+1)]
DP = [0]*(N+1)        # 폭발의 아름다움

for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

fireworks = list(map(int,input().split()))
fireworks.insert(0,0)
fireworks_stack = [0]*(N+1)
for i in range(1,N+1):
    fireworks_stack[i] = fireworks[i]

def DFS(v):
    visited[v] = True

    for next in tree[v]:
        if visited[next]:
            continue
        DFS(next)
        fireworks_stack[v] += fireworks_stack[next]
        DP[v] += DP[next] + fireworks_stack[next]

def reroot(v):
    visited[v] = True

    for next in tree[v]:
        if visited[next]:
            continue
        DP[next] = DP[v] + (total - 2*fireworks_stack[next])
        reroot(next)

visited = [False]*(N+1)
DFS(1)

total = fireworks_stack[1]
visited = [False]*(N+1)
reroot(1)

print(max(DP))