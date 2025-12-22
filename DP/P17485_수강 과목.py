import sys
input = sys.stdin.readline

N,K = map(int,input().split())

subject = []
for _ in range(K):
    I,T = map(int,input().split())
    subject.append((I,T))

# DP[i] : i의 시간 동안 얻을 수 있는 최대 중요도
DP = [0]*(N+1)

for i,t in subject:
    for day in range(N,t-1,-1):
        DP[day] = max(DP[day],DP[day-t]+i)

print(DP[N])