import sys
from math import hypot
input = sys.stdin.readline

INF = float('inf')
N = int(input())

coor = [tuple(map(int,input().split())) for _ in range(N)]

dist = [[0.0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        dist[i][j] = hypot(coor[i][0]-coor[j][0],coor[i][1]-coor[j][1])

# DP[i][mask] : 현재 도시 i, 방문 기록이 mask일때 최소비용
DP = [[INF]*(1<<N) for _ in range(N)]
DP[0][1<<0] = 0.0

for mask in range(1<<N):
    # 출발 도시 포함 안한 경우
    if not mask & 1:
        continue

    for i in range(N):
        # 아직 도달하지 않은 경우
        if not mask & (1<<i):
            continue

        # 아직 도달하지 않은 경우
        if DP[i][mask] == INF:
            continue
        
        for j in range(N):
            # 이미 j를 방문했던 경우
            if mask & (1<<j):
                continue

            nmask = mask | (1<<j)
            DP[j][nmask] = min(DP[j][nmask],DP[i][mask]+dist[i][j])

# ans : (1<<N)-1 상태 마지막 도시에서의 복귀값 추가
ans = INF
for i in range(N):
    ans = min(ans,DP[i][(1<<N)-1]+dist[i][0])

print(ans)