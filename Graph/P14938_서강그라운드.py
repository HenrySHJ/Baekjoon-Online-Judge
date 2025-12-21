import sys, heapq
input = sys.stdin.readline

N,M,R = map(int,input().split())
T = [0] + list(map(int,input().split()))

graph = [[] for _ in range(N+1)]
for _ in range(R):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))
    graph[e].append((s,w))

def dijkstra(start):
    ans = 0
    dist = [sys.maxsize]*(N+1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap,(0,start))

    while heap:
        cur_dist,now = heapq.heappop(heap)
        ans += T[now]

        for next,cost in graph[now]:
            new_dist = cur_dist + cost
            if new_dist < dist[next] and new_dist <= M:
                dist[next] = new_dist
                heapq.heappush(heap,(new_dist,next))

    total = 0
    for i in range(1,N+1):
        if dist[i] <= M:
            total += T[i]
    return total

answer = 0
for i in range(1,N+1):
    answer = max(answer,dijkstra(i))

print(answer)