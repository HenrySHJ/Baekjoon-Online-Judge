import sys
input = sys.stdin.readline

N,M,C = map(int, input().split())
jewels = list(map(int, input().split()))

# DP[i][j] : 현재 비트 상태 i를 만드는데 가방 j만큼 사용했을때 남은 용량의 최댓값
DP = [[-1]*(M+1) for _ in range(1<<N)]
DP[0][1] = C

for mask in range(1<<N):
    for k in range(1,M+1):
        cap = DP[mask][k]
        # 아직 갱신되지 않은 DP는 건너뛰기
        if cap < 0:
            continue
        
        # 각 보석에 대해 담는 경우
        for i in range(N):
            # 이미 현재 비트에 i가 포함되어 있는 경우 건너뛰기
            if mask & (1<<i):
                continue
            
            jwl = jewels[i]
            nmask = mask | (1<<i)

            # 같은 가방에 넣을 때
            if cap >= jwl:
                DP[nmask][k] = max(DP[nmask][k], cap-jwl)

            # 새로운 가방이 있을 때 넣기
            if k+1 <= M:
                DP[nmask][k+1] = max(DP[nmask][k+1],C-jwl)

# 최대 보석 개수 계산
ans = 0
for mask in range(1<<N):
    for k in range(1,M+1):
        if DP[mask][k] >= 0:
            ans = max(ans, bin(mask).count("1"))

print(ans)