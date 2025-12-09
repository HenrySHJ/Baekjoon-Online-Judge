import sys, heapq
input = sys.stdin.readline

INF = 10**18

N,M = map(int,input().split())

price = [0]+list(map(int,input().split()))   # 리터 당 가격
road = [[] for _ in range(N+1)]              # 도로 정보

# 도로 정보 입력
for i in range(M):
    s,e,l = map(int,input().split())
    road[s].append((e,l))
    road[e].append((s,l))

# DP[i][j] : 지나온 도시 중 최소 가격인 도시 j일때 i까지 도달하는 최소 가격
DP = [[INF]*(N+1) for _ in range(N+1)]
DP[1][1] = 0

# 다익스트라
def dijkstra(start):
    heap = []

    # 시작 정보 입력 (최소 가격, 도착지, 최소 가격의 도시)
    heapq.heappush(heap,(0,start,start))
    
    while heap:
        cost,now,min_city = heapq.heappop(heap)

        # 최솟값을 갱신시킬 가능성이 없는 경우 건너뛰기
        if DP[now][min_city] < cost:
            continue

        if now == N:
            return min(DP[N])
        
        # 현재 도시에서의 가격
        cur_price = price[min_city]

        # 해당 도시와 연결된 도시 확인
        for next, dist in road[now]:
            # next 도시를 포함했을 때 새로운 최소 가격 도시 계산
            if price[next] < price[min_city]:
                new_min_city = next
            else:
                new_min_city = min_city

            # 새로운 최소 가격
            new_cost = cost + dist * cur_price

            # 갱신되면 push
            if DP[next][new_min_city] > new_cost:
                DP[next][new_min_city] = new_cost
                heapq.heappush(heap,(new_cost,next,new_min_city))
    
ans = dijkstra(1)
print(ans)