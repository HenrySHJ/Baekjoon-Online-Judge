import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N,M = map(int,input().split())

A = list(map(int,input().split()))
A.insert(0,0)

boss = [[] for _ in range(N+1)]
praise = [0]*(N+1)

for i in range(1,N+1):
    if A[i] != -1:
        boss[A[i]].append(i)
    
def DFS(v):
    for next in boss[v]:
        praise[next] += praise[v]
        DFS(next)
        

for _ in range(M):
    i,w = map(int,input().split())
    praise[i] += w

DFS(1)

for i in range(1,N+1):
    print(praise[i], end=' ')