import sys
input = sys.stdin.readline

N,M = map(int,input().split())

chap = [[0,0] for _ in range(M+1)]

for i in range(1,M+1):
    d,p = map(int,input().split())
    chap[i] = [d,p]

chap.sort(key = lambda x:x[0])
# DP[i] : i일 동안 읽을 수 있는 최대 페이지 수
DP = [0]*(N+1)

for d,p in chap:              
    for day in range(N, d-1, -1):
        DP[day] = max(DP[day], DP[day-d] + p)

print(DP[N])