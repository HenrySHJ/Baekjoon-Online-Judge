import sys, heapq
input = sys.stdin.readline

N, P, K = map(int, input().split())

# 인접 그래프 & 간선 리스트 작성
graph = [[] for _ in range(N + 1)]

for _ in range(P):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
    
# 다익스트라
def dijkstra(limit):
    heap = []
    heapq.heappush(heap, (0, 1))

    # dist[i] : i까지 도달하는데 제한 금액을 넘는 선의 수
    dist = [sys.maxsize] * (N + 1)
    dist[1] = 0

    while heap:
        cur_cost, now = heapq.heappop(heap)
        
        # 갱신 가능성 없으면 건너뛰기
        if dist[now] < cur_cost:
            continue

        for nxt, weight in graph[now]:
            # 제한 금액에 따른 가중치
            cost = 0
            if weight > limit:
                cost = 1
            else:
                cost = 0

            if dist[nxt] > cur_cost + cost:
                dist[nxt] = cur_cost + cost
                heapq.heappush(heap, (dist[nxt], nxt))

    return dist[N]

ans = -1
start = 0
end = 10**6

while start <= end:
    mid = (start + end) // 2
    
    if dijkstra(mid) <= K:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)