import sys
input = sys.stdin.readline

INF = sys.maxsize

N,M = map(int,input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    u,v,c = map(int,input().split())
    graph[u-1].append((v-1,c))

# DP[i][mask] : 현 위치 i번 도시, 비트상태 mask일때 최대 정점 연결 비용의 최솟값
DP = [[INF]*(1<<N) for _ in range(N)]
DP[0][1] = 0  # 순회이기 때문에 출발지 고정해도 문제 없음

# parent[i][mask] : (이전 도시, 이전 mask)
parent = [[(-1,-1)]*(1<<N) for _ in range(N)]

for mask in range(1<<N):
    # 출발지를 포함하지 않은 경우
    if not (mask & 1):
        continue

    for i in range(N):
        # 현재 도시가 지나온 상태에 없는 경우
        if not mask & (1<<i):
            continue
        # 현재 도시 & 상태가 갱신된 적이 없는 경우
        if DP[i][mask] == INF:
            continue
        
        for j,cost in graph[i]:
            # 이동할 도시를 이미 지난 경우
            if mask & (1<<j):
                continue
            nmask = mask | (1<<j)
            new_cost = max(DP[i][mask], cost)
            # 값이 갱신되는 경우
            if DP[j][nmask] > new_cost:
                DP[j][nmask] = new_cost
                parent[j][nmask] = (i, mask)

# 정점 거리의 최댓값의 최솟값 출력           
ans = INF
end_i = -1
for i in range(N):
    for j,cost in graph[i]:
        if j != 0:
            continue
        # 모든 도시를 지난 적이 있는 경우
        if DP[i][(1<<N)-1] != INF:
            candidate = max(DP[i][(1<<N)-1],cost)
            if ans > candidate:
                ans = candidate
                end_i = i

print(ans if ans != INF else -1)

# 경로 역추적
path = []
cur_i = end_i
cur_mask = (1<<N)-1

while cur_i != -1:
    path.append(cur_i+1)

    prev_i, prev_mask = parent[cur_i][cur_mask]
    cur_i = prev_i
    cur_mask = prev_mask

for i in range(len(path)-1,-1,-1):
    print(path[i],end=' ')