import sys,heapq
input = sys.stdin.readline

N, M = map(int,input().split())

univ = list(input().split())
univ.insert(0,"")

parent = [i for i in range(N+1)]
heap = []  # 거리, 시작점, 끝점, 대학생 성별
for _ in range(M):
    u,v,d = map(int,input().split())
    heapq.heappush(heap,(d,u,v))

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
while useEdge < N-1 and len(heap) > 0:
    d,u,v = heapq.heappop(heap)
    if find(u) != find(v) and univ[u] != univ[v]:
        union(u,v)
        result += d
        useEdge += 1

if useEdge != N-1:
    print(-1)
else:
    print(result)