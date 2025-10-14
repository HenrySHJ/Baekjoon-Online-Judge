import sys, heapq

N,M,X = map(int,input().split())

myList = [[] for _ in range(N+1)]


for _ in range(M):
    s,e,t = map(int,input().split())
    myList[s].append((e,t))

def dijkstra(start,end):
    dist = [sys.maxsize]*(N+1)
    dist[0] = 0
    visited = [False]*(N+1)
    heap = []

    if start == end:
        return 0 
    
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

ans = [0]*(N+1)
for i in range(1,N+1):
    ans[i] = dijkstra(i,X)+dijkstra(X,i)

print(max(ans))