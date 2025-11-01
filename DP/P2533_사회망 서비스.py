import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)

DP = [[0,0] for _ in range(N+1)]
visited = [False]*(N+1)

def DFS(v):
    visited[v] = True

    DP[v][0] = 0    # 얼리어답터가 아닐때
    DP[v][1] = 1    # 얼리어답터 일때

    for next in tree[v]:
        if visited[next]: 
            continue
        DFS(next)

        DP[v][0] += DP[next][1]                   # 0이면 자식은 1 강제
        DP[v][1] += min(DP[next][0], DP[next][1]) # 1이면 자식은 0,1 둘 다 가능

DFS(1)
print(min(DP[1][0], DP[1][1]))