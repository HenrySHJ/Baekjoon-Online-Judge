import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
DP = [0]*N
DP[0] = A[0]

for i in range(1,N):
    DP[i] = A[i]
    DP[i] = max(DP[i],DP[i-1]+A[i])

print(max(DP))