import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
DP = [1]*N

for i in range(N):
    for j in range(i+1,N):
        if A[i] > A[j]:
            DP[j] = max(DP[j],DP[i]+1)

print(max(DP))