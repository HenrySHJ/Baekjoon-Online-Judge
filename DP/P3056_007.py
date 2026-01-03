import sys
input = sys.stdin.readline

N = int(input())

success_rate = [list(map(int,input().split())) for _ in range(N)]

# DP[mask] : 현재 미션을 진행한 요원을 mask로 표현했을 때 최대 성공률
DP = [-1.0]*(1<<N)
DP[0] = 1.0

for mask in range(1<<N):
    # 수행할 미션 번호
    j = 0

    # 아직 유효하지 않은 진행도에 대해 건너뛰기
    if DP[mask] == -1.0:
        continue
        
    # 아직 미션 수행을 안한 i 찾기
    for i in range(N):
        # mask에 이미 i가 처리된 경우 건너뛰기
        if mask & (1<<i):
            j += 1

    # j는 i가 처리할 미션 번호
    for i in range(N):    
        if mask & (1<<i):
            continue

        # 새로운 진행도에 대한 성공 가능성 갱신시키기
        nmask = mask | (1<<i)
        percent = (success_rate[i][j]/100)
        DP[nmask] = max(DP[nmask],DP[mask]*percent)

print(DP[(1<<N)-1]*100)