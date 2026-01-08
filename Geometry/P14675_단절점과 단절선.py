import sys
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
edges = []
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    indegree[a] += 1
    indegree[b] += 1
    edges.append((a,b))

Q = int(input())

for _ in range(Q):
    t,k = map(int,input().split())

    if t == 1:
        if indegree[k] > 1:
            print('yes')
        else:
            print('no')
    elif t == 2:
        print('yes')