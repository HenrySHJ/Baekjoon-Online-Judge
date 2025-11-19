import sys
input = sys.stdin.readline

N = int(input())
pack = [0]+list(map(int,input().split()))
DP = [sys.maxsize]*(N+1)
DP[0] = 0

for i in range(1,N+1):
    for j in range(i,N+1):
        DP[j] = min(DP[j],DP[j-i]+pack[i])

print(DP[N])