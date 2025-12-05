import sys
input = sys.stdin.readline

N,T = map(int,input().split())

chap = [[0,0] for i in range(N+1)]

# DP[i] : i시간 공부해서 받을 수 있는 최대 점수
DP  = [0]*(T+1)

for i in range(1,N+1):
    K,S = map(int,input().split())
    chap[i] = [K,S]

for i in range(1,N+1):
    for j in range(T,chap[i][0]-1,-1):
        # 단일 과목으로 받는 점수 계산
        if j == chap[i][0]:
            DP[j] = max(DP[j],chap[i][1])
            continue
        # 이미 점수 계산된적이 있는 시간
        elif DP[j-chap[i][0]] != 0:
            DP[j] = max(DP[j],DP[j-chap[i][0]]+chap[i][1])

print(max(DP))