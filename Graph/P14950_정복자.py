import sys,heapq
input = sys.stdin.readline

N,M,T = map(int,input().split())

parent = [i for i in range(N+1)]

heap = []
for _ in range(M):
    A,B,C = map(int,input().split())
    heapq.heappush(heap,(C,A,B))

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

t = 1
while t < N - 1:
    result += t
    t += 1
result *= T

while useEdge < N-1:
    C,A,B = heapq.heappop(heap)
    if find(A) != find(B):
        union(A,B)
        result += C
        useEdge += 1

print(result)