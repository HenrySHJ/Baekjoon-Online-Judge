import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,R,Q = map(int,input().split())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

subtree = [0]*(N+1)

def DFS(v, parent):
    subtree[v] = 1  # 자기 자신 포함
    for nxt in tree[v]:
        if nxt != parent:
            subtree[v] += DFS(nxt, v)
    return subtree[v]

DFS(R, -1)

for _ in range(Q):
    q = int(input())
    print(subtree[q])