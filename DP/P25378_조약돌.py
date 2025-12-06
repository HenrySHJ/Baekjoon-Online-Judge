import sys
input = sys.stdin.readline

INF = 10**9

N = int(input())
pebble = [0]+list(map(int,input().split()))


# DP[i] : i번째 조약돌 주울 때 최소 횟수
DP = [INF]*(N+1)
DP[0] = 0
DP[1] = 1

for i in range(2,N+1):
    # 조약돌을 중앙에서 줍기
    DP[i] = DP[i-1] + 1

    # i-1과 i의 데이터 차 확인
    cur = pebble[i]

    # 조약돌을 중앙+사이드에서 줍기
    for j in range(i-1,0,-1):
        if pebble[j] < cur:
            cur = -1
        else:
            cur = pebble[j] - cur

        if cur < 0:
            break

        if cur == 0:
            DP[i] = min(DP[i],DP[j-1]+(i-j))

print(DP[N])