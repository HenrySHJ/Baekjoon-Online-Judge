import sys,heapq
input = sys.stdin.readline

INF = sys.maxsize

N,M,K = map(int,input().split())
S,D = map(int,input().split())

graph = [[] for _ in range(N+1)]  # 인접 그래프

for _ in range(M):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))

# DP[i][j] : i에 도달하는데 j개를 간선을 지나 도착했을때의 최소 비용
DP = [[INF]*(N+1) for _ in range(N+1)]

# 다익스트라
def dijkstra(start):
    heap = []
    DP[start][0] = 0
    heapq.heappush(heap,(0,start,0))

    while heap:
        cur_dist,now,count = heapq.heappop(heap)

        # 기록 갱신이 불가능한 경우 건너뛰기
        if DP[now][count] < cur_dist:
            continue
        
        # 정점까지의 비용도 더 적고 간선 개수도 더 적은 경우 건너뛰기
        jump = False
        for i in range(count):
            if DP[now][i] <= cur_dist:
                jump = True
                break
        if jump:
            continue

        # 정점 개수 이상의 간선 개수면 건너뛰기
        if count + 1 >= N:
            continue
                
        for nxt,add_dist in graph[now]:
            if DP[nxt][count+1] > cur_dist + add_dist:
                DP[nxt][count+1] = cur_dist + add_dist
                heapq.heappush(heap,(DP[nxt][count+1],nxt,count+1))

dijkstra(S)

candidate = []
for j in range(1,N+1):
    if DP[D][j] != INF:
        candidate.append((DP[D][j],j))

# 세금 0일때 따로 처리
tax = 0
ans = INF
for cand,j in candidate:
    ans = min(ans,cand)
print(ans)

# 세금 누적 계산
for _ in range(K):
    p = int(input())
    tax += p
    ans = INF
    for cand,j in candidate:
        ans = min(ans,cand+tax*j)

    print(ans)