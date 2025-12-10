import sys,heapq
input = sys.stdin.readline

N = int(input())
planet = [list(map(int,input().split()))+[i] for i in range(N)]

sx = sorted(planet,key=lambda x:x[0])
sy = sorted(planet,key=lambda x:x[1])
sz = sorted(planet,key=lambda x:x[2])

# 유니온 파인드
parent = [0]*(N)
for i in range(N):
    parent[i] = i

# 파인드 함수
def find(a):
    while a != parent[a]:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

# 유니온 함수
def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

heap = []
for i in range(N-1):
    cost1 = abs(sx[i][0]-sx[i+1][0])
    heapq.heappush(heap,(cost1,sx[i][3],sx[i+1][3]))

    cost2 = abs(sy[i][1]-sy[i+1][1])
    heapq.heappush(heap,(cost2,sy[i][3],sy[i+1][3]))

    cost3 = abs(sz[i][2]-sz[i+1][2])
    heapq.heappush(heap,(cost3,sz[i][3],sz[i+1][3]))

result = 0
useEdge = 0
while useEdge < N-1:
    cost,a,b = heapq.heappop(heap)
    if find(a) != find(b):
        union(a,b)
        result += cost
        useEdge += 1

print(result)