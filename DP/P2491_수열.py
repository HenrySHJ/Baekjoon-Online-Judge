import sys
input = sys.stdin.readline

N = int(input())
A = [0]+list(map(int,input().split()))

max_DP = [1]*(N+1)
min_DP = [1]*(N+1)

for i in range(1,N):
    if A[i] <= A[i+1]:
        max_DP[i+1] = max_DP[i] + 1
    if A[i] >= A[i+1]:
        min_DP[i+1] = min_DP[i] + 1

print(max(max(max_DP),max(min_DP)))