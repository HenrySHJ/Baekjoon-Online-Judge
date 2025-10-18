import math
import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(N)]
points.insert(0, (0, 0))

parent = [i for i in range(N + 1)]

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        return True
    return False

# 이미 연결된 통로
connected = 0
for _ in range(M):
    a, b = map(int, input().split())
    if union(a,b):
        connected += 1

# 모든 거리 계산
heap = []
for i in range(1, N):
    for j in range(i + 1, N + 1):
        x1, y1 = points[i]
        x2, y2 = points[j]
        dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        heapq.heappush(heap, (dist, i, j))

# MST
result = 0.0
useEdge = connected
while heap and useEdge < N - 1:
    dist, a, b = heapq.heappop(heap)
    if union(a, b):
        result += dist
        useEdge += 1

print(f"{result:.2f}")