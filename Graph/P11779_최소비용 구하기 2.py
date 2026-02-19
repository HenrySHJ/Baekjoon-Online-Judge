import sys
import heapq
input = sys.stdin.readline

# 다익스트라
def dijkstra(start, end):
    heap = []
    heapq.heappush(heap, (0, start))
    dist[start] = 0
    visited[start] = True

    while heap:
        cost, now = heapq.heappop(heap)

        if now == end:
            break
        
        for nxt, weight in graph[now]:
            if dist[nxt] > cost + weight:
                visited[nxt] = True
                dist[nxt] = cost + weight
                parent[nxt] = now
                heapq.heappush(heap, (dist[nxt], nxt))

# 역추적
def backtrack(end, start):
    city = [end]
    now = end

    while now != start:
        now = parent[now]
        city.append(now)

    return city
N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

visited = [False] * (N + 1)
dist = [sys.maxsize] * (N + 1)
parent = [0] * (N + 1)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

s, e = map(int, input().split())

dijkstra(s, e)

print(dist[e])

ans = backtrack(e, s)
print(len(ans))

for i in range(len(ans) - 1, -1, -1):
    print(ans[i], end = " ")