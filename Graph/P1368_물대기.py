import sys, heapq
input = sys.stdin.readline

# 유니온-파인드 함수
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

N = int(input())
W = [int(input()) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

parent = [i for i in range(N + 1)]

heap = []

# 논을 파는 비용 push
for i in range(N):
    heapq.heappush(heap, (W[i], 0, i + 1))

# 최소 힙에다가 물을 대는 비용 push
for i in range(N):
    for j in range(i + 1, N):
        heapq.heappush(heap, (P[i][j], i + 1, j + 1))

# MST 실행
result = 0
useEdge = 0

while heap and useEdge < N:
    w, s, e = heapq.heappop(heap)

    # 같은 그룹이 아닌 경우 연결 & 비용 추가
    if find(s) != find(e):
        union(s, e)
        useEdge += 1
        result += w

print(result)