import sys,heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

heap = []
parent = [0]*(N+1)
for i in range(1,N+1):
    parent[i] = i

# 가중치에 따른 정렬을 위한 heapq
for i in range(M):
    s,e,w = map(int,input().split())
    heapq.heappush(heap,(w,s,e))

# 유니온 파인드
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

while useEdge < N-1:
    w,s,e = heapq.heappop(heap)
    if find(s) != find(e):
        union(s,e)
        result += w
        useEdge += 1

print(result)