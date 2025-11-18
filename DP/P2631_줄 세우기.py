import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]
DP = [1]*N

for i in range(N):
    for j in range(i+1,N):
        if A[j] > A[i]:
            DP[j] = max(DP[j],DP[i]+1)

print(N-max(DP))