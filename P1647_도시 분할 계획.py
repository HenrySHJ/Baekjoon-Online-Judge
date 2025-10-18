import heapq

N,M = map(int,input().split())

parent = [0]*(N+1)
for i in range(1,N+1):
    parent[i] = i

heap = []
for _ in range(M):
    s,e,w = map(int,input().split())
    heapq.heappush(heap,(w,s,e))

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

useEdge = 0
result = 0
while useEdge < N-2:  # 최대 가중치 간선 제외
    w,s,e = heapq.heappop(heap)
    if find(s) != find(e):
        union(s,e)
        result += w
        useEdge += 1

print(result)