import sys, heapq
from collections import deque
input = sys.stdin.readline

# 다익스트라 변형 : 최단 경로 모두 탐색
def dijkstra_all(start,end):
    heap = []
    dist[start] = 0
    heapq.heappush(heap,(dist[start],start))

    while heap:
        cur_dist,now = heapq.heappop(heap)
        visited[now] = True

        # 최단 경로 갱신 가능성 없으면 종료
        if cur_dist > dist[end]:
            break
        
        for nxt,add_dist in graph[now]:
            if visited[nxt]:
                continue
            
            new_dist = cur_dist + add_dist

            # 정점까지의 최단경로가 바뀌는 경우
            if new_dist < dist[nxt]:
                dist[nxt] = new_dist 
                parent[nxt] = [now]
                heapq.heappush(heap,(dist[nxt],nxt))

            # 동일한 길이의 최단경로 발견
            elif new_dist == dist[nxt]:
                parent[nxt].append(now)

# 역추적 & 사용된 edge 확인
def BFS_backtrack(D, S):
    queue = deque([D])
    visited_back = [False]*N
    visited_back[D] = True
    
    while queue:
        v = queue.popleft()
        if v == S:
            continue
            
        for u in parent[v]:
            edges[u][v] = 0
            if not visited_back[u]:
                visited_back[u] = True
                queue.append(u)

# 최종 기본 다익스트라
def dijkstra(start,end):
    heap = []
    dist[start] = 0
    visited[start] = True
    heapq.heappush(heap,(dist[start],start))

    while heap:
        cur_dist,now = heapq.heappop(heap)

        if not visited[now]:
            visited[now] = True

        for nxt,add_dist in new_graph[now]:
            visited[nxt] = True
            new_dist = cur_dist + add_dist

            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                heapq.heappush(heap,(dist[nxt],nxt))

    return dist[end]
                
while True:
    N,M = map(int,input().split())

    if N == 0 and M == 0:
        break

    S,D = map(int,input().split())

    graph = [[] for _ in range(N)]   
    parent = [[] for _ in range(N)]  
    dist = [sys.maxsize]*N
    visited = [False]*N
    edges = [[0]*N for _ in range(N)]

    for _ in range(M):
        u,v,p = map(int,input().split())
        graph[u].append((v,p))
        edges[u][v] = p

    dijkstra_all(S,D)
    BFS_backtrack(D,S)
    
    # 사용 불가한 간선이 제거된 새로운 그래프
    new_graph = [[] for _ in range(N)]
    visited = [False]*N
    dist = [sys.maxsize]*N
    for i in range(N):
        for j in range(N):
            if edges[i][j] > 0:
                new_graph[i].append((j,edges[i][j]))

    ans = dijkstra(S,D)
    if ans != sys.maxsize:
        print(ans)
    else:
        print(-1)