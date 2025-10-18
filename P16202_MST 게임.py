import sys,heapq,copy
input = sys.stdin.readline

N,M,K = map(int,input().split())

heap = []
for i in range(1,M+1):
    x,y = map(int,input().split())
    heapq.heappush(heap,(i,x,y))

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

count = 0
for i in range(K):
    temp = copy.deepcopy(heap)  # 임시로 힙과 똑같은 데이터를 가진 temp 생성
    useEdge = 0
    result = 0
    parent = [i for i in range(N+1)]

    while useEdge < N-1 and len(temp) > 0:
        w,x,y = heapq.heappop(temp)
        if find(x) != find(y):
            union(x,y)
            result += w
            useEdge += 1

    if useEdge == N-1:
        print(result,end=' ')
        heapq.heappop(heap)
    else:
        count = K-i
        break

for i in range(count):
    print(0,end=' ')