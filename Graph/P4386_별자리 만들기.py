import heapq

N = int(input())

star = []
parent = [i for i in range(N+1)]

for _ in range(N):
    a,b = map(float,input().split())
    star.append((a,b))

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

heap = []
for i in range(N-1):
    for j in range(i+1,N):
        x = star[i][0] - star[j][0]
        y = star[i][1] - star[j][1]
        dist = (x**2+y**2)**0.5
        heapq.heappush(heap,(dist,i,j))

useEdge = 0
result = 0
while useEdge < N-1:
    dist,x,y = heapq.heappop(heap)
    if find(x) != find(y):
        union(x,y)
        result += dist
        useEdge += 1

print(round(result,2))