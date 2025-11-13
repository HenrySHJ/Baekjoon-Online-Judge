import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

DP = [0]*N
for i in range(N):
    DP[i] = A[i]

for i in range(N):
    for j in range(i+1,N):
        if A[i] < A[j]:
            DP[j] = max(DP[j], DP[i] + A[j])

print(max(DP))