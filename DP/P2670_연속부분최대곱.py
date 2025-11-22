import sys
input = sys.stdin.readline

N = int(input())
A = [float(input().strip()) for _ in range(N)]

DP = [0]*N

for i in range(N):
    DP[i] = A[i]

for i in range(1,N):
    DP[i] = max(DP[i],DP[i-1]*A[i])

ans = max(DP)

print(f"{ans:.3f}")