import sys
input = sys.stdin.readline

N = int(input())

power_plant = [list(map(int,input().split())) for _ in range(N)]
act = list(input().strip())
P = int(input())

# 시작 시점 발전소 비트마스크
start = 0
for i in range(N):
    if act[i] == 'Y':
        start |= (1 << i)

# 시작시점 켜져있는 발전소 개수
start_count = act.count('Y')

# DP[i][j] : i개가 켜져있을 때, 현재 비트 j일때 -> 최소 비용

INF = sys.maxsize
DP = [[INF]*(1 << N) for _ in range(N+1)]

# DP 초기화
DP[start_count][start] = 0

# DP 갱신하기
for on in range(start_count,N+1):
    for mask in range(1<<N):
        if DP[on][mask] == INF:
            continue

        # 이미 P개 이상 켜졌으면 더 돌 필요 없음
        if on >= P:
            continue

        # 켜져 있는 발전소 x에서, 꺼져 있는 y를 켜기
        for x in range(N):
            # x가 꺼져있으면 skip
            if not (mask & (1 << x)):   
                continue
            
            # x로 y 켜기
            for y in range(N):
                # y가 이미 켜져있으면 skip
                if mask & (1 << y):    
                    continue
                
                # 새로운 비트와 최소 비용 계산 후 갱신
                new_mask = mask | (1<<y)
                new_cost = DP[on][mask] + power_plant[x][y]

                DP[on+1][new_mask] = min(DP[on+1][new_mask],new_cost)


# 정답 계산
ans = INF
for on in range(P,N+1):
    for mask in range(1 << N):
        ans = min(ans, DP[on][mask])

print(ans if ans != INF else -1)