import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    p,c = map(int,input().split())
    graph[p].append(c)

tree = list(map(int,input().split()))

DP = [0]*(N+1)

def DFS(now):
    DP[now] = tree[now]

    for next in graph[now]:
        DFS(next)
        DP[now] += max(DP[next],0)

DFS(0)
print(DP[0])