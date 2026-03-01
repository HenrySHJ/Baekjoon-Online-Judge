import sys, heapq
input = sys.stdin.readline

# 유니온 파인드
def find(a):
    if parent[a] == a:
        return a
    
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a
    
N, M = map(int, input().split())

min_heap = []
max_heap = []

max_result = 0
min_result = 0

# 나머지 도로 입력
for _ in range(M + 1):
    A, B, C = map(int, input().split())
    
    heapq.heappush(min_heap, (C, A, B))
    heapq.heappush(max_heap, (-C, A, B))

# 최소 힙으로 최소한 오르막길 찾기
parent = [i for i in range(N + 1)]
useEdge = 0

# MST
while min_heap and useEdge < N:
    w, s, e = heapq.heappop(min_heap)

    if find(s) != find(e):
        union(s, e)
        max_result += (w + 1) % 2
        useEdge += 1

# 최대 힙으로 최대한 오르막길 찾기
parent = [i for i in range(N + 1)]
useEdge = 0

# MST
while max_heap and useEdge < N:
    w, s, e = heapq.heappop(max_heap)

    if find(s) != find(e):
        union(s, e)
        min_result += (-w + 1) % 2
        useEdge += 1

print(max_result ** 2 - min_result ** 2)