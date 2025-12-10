import sys,heapq
input = sys.stdin.readline

N = int(input())
cost = [[0]+list(map(int,input().split())) for _ in range(N)]
cost.insert(0,[0]*(N+1))

parent = [i for i in range(N+1)]

heap = []
for i in range(1,N+1):
    for j in range(1,i):
        if i != j:
            heapq.heappush(heap,(cost[i][j],i,j))

def find(a):
    while a != parent[a]:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

result = 0
useEdge = 0
while heap and useEdge < N-1:
    c,i,j = heapq.heappop(heap)
    if find(i) != find(j):
        union(i,j)
        result += c
        useEdge += 1

print(result)