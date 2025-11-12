import sys
input = sys.stdin.readline

N = int(input())
pack = list(map(int,input().split()))
pack.insert(0,0)

DP = [0]*(N+1)  # idx개를 사는데 드는 최고 비용

# 완전 knapsack
for i in range(1,N+1):
    for j in range(i,N+1):
        DP[j] = max(DP[j],DP[j-i]+pack[i])

print(DP[N])