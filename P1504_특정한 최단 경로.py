import sys, heapq

N,E = map(int,input().split())

myList = [[] for _ in range(N+1)]

for _ in range(E):
    a,b,c = map(int,input().split())
    myList[a].append((b,c))
    myList[b].append((a,c))

def dijkstra(start,end):
    visited = [False]*(N+1)   # 방문 여부
    dist = [sys.maxsize]*(N+1)  # 인덱스까지 거리
    
    heap = []
    heapq.heappush(heap,(0,start))
    dist[start] = 0
    while heap:
        nowNode = heapq.heappop(heap)
        now = nowNode[1]
        if not visited[now]:
            visited[now] = True
            for n in myList[now]:
                if dist[n[0]] > dist[now] + n[1]:
                    dist[n[0]] = dist[now] + n[1]
                    heapq.heappush(heap,(dist[n[0]],n[0]))
    return dist[end]

v1,v2 = map(int,input().split())

path1 = dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,N)
path2 = dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,N)

if min(path1,path2) >= sys.maxsize:
    print(-1)
else:
    print(min(path1,path2))