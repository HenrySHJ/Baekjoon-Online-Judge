import sys,heapq
input = sys.stdin.readline

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

while True:
    M,N = map(int,input().split())
    
    parent = [i for i in range(M)]

    if M == 0 and N == 0:
        break
    
    total = 0
    heap = []
    for i in range(N):
        x,y,z = map(int,input().split())
        total += z
        heapq.heappush(heap,(z,x,y))

    result = 0
    useEdge = 0

    while heap and useEdge < N-1:
        z,x,y = heapq.heappop(heap)

        if find(x) != find(y):
            union(x,y)
            result += z
            useEdge += 1

    print(total-result)