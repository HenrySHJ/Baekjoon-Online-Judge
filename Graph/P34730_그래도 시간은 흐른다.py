import sys, heapq
input = sys.stdin.readline

N,M,K,S,T = map(int,input().split())
graph = [[] for _ in range(N+1)]
total_time = [sys.maxsize]*(N+1)
visited = [False]*(N+1)

for _ in range(M):
    u,v,c,o = map(int,input().split())
    graph[u].append((v,c,o))

def dijkstra(start,end):
    heap = []
    total_time[start] = 0
    heapq.heappush(heap,(0,start))
    while heap:
        # 현재 시간, 현재 노드
        c_time,now = heapq.heappop(heap)
        if not visited[now]:
            visited[now] = True
            for next,est_time,open in graph[now]:
                # 이동 가능한 경우
                if c_time % open == 0:
                    # 기존 시간보다 누적 시간 + 이용 시간이 짧으면 갱신
                    if total_time[next] > c_time + est_time:
                        total_time[next] = c_time + est_time
                        heapq.heappush(heap,(total_time[next],next))
    return total_time[end]

ans = dijkstra(S,T)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)