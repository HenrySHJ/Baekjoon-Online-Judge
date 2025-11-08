import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

DP = [1]*N

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            DP[i] = max(DP[i], DP[j] + 1)

print(max(DP))