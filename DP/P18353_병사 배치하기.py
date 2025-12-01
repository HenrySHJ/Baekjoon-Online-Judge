import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
A.reverse()

DP = [1]*N

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            DP[i] = max(DP[i], DP[j] + 1)

print(N-max(DP))