import sys,heapq
input = sys.stdin.readline

N,M,K = map(int,input().split())
power_plant = list(map(int,input().split()))

heap = []
for _ in range(M):
    u,v,w = map(int,input().split())
    heapq.heappush(heap,(w,u,v))

parent = [i for i in range(N+1)]

# 유니온-파인드
def find(a):
    while a != parent[a]:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

useEdge = 0
result = 0

# 발전소들끼리 union
for i in range(K-1):
    union(power_plant[i],power_plant[i+1])

while heap and useEdge < N-K:
    w,u,v = heapq.heappop(heap)
    
    if find(u) != find(v):
        union(u,v)
        useEdge += 1
        result += w

print(result)