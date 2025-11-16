import sys
input = sys.stdin.readline

N = int(input())
T = [0]*(N+2)
P = [0]*(N+2)
DP = [0]*(N+2)

for i in range(1,N+1):
    T[i],P[i] = map(int,input().split())

for i in range(1,N+2):
    DP[i] = max(DP[i],DP[i-1])

    # 오늘 시작하는 상담이 기간 내에 끝나면
    if i + T[i] <= N + 1:
        DP[i + T[i]] = max(DP[i + T[i]], DP[i] + P[i])

print(DP[N+1])