import sys
input = sys.stdin.readline

N = int(input())
WL = [list(map(int,input().split())) for _ in range(N)]

# DP[i][mask] : 마지막 꼬리 선수 i, 현재 방문 mask 상태일때 최대 길이
DP = [[0]*(1<<N) for _ in range(N)]
DP[0][1] = 1

# parent[i][mask] : 마지막 꼬리 선수 i, 현재 방문 mask일때 (이전 도시, 이전 mask)
parent = [[(-1,-1)]*(1<<N) for _ in range(N)]

for mask in range(1<<N):
    # 시작 선수 미포함 상태 건너뛰기
    if not mask & 1:
        continue

    for i in range(N):
        # 마지막 꼬리가 미방문 상태인 경우 건너뛰기
        if not mask & (1<<i):
            continue
        
        # 갱신이 된적이 없는 경우 건너뛰기
        if DP[i][mask] == 0:
            continue

        for j in range(N):
            # 이미 j가 mask에 있던 경우
            if mask & (1<<j):
                continue

            # i번이 j번을 이긴 경우 j를 마지막 꼬리로 붙이기
            if WL[i][j] == 1:
                nmask = mask | (1<<j)
                DP[j][nmask] = max(DP[j][nmask],DP[i][mask]+1)
                parent[j][nmask] = (i, mask)

# 최장 길이
ans = 0
end_i = -1
end_mask = -1
for mask in range(1<<N):
    # 시작 선수 미포함
    if not (mask & 1):
        continue
    for i in range(N):
        # 최장길이, 꼬리 선수와 mask 갱신
        if DP[i][mask] > ans:
            ans = DP[i][mask]
            end_i = i
            end_mask = mask
print(ans)

# 최장 길이일때의 경로 역추적
path = []
cur_i, cur_mask = end_i, end_mask

while cur_i != -1:
    path.append(cur_i + 1)
    prev_i, prev_mask = parent[cur_i][cur_mask]
    cur_i, cur_mask = prev_i, prev_mask

for i in range(len(path)-1,-1,-1):
    print(path[i],end=' ')