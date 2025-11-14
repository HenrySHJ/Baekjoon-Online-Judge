import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))

DP = [0]*(sum(C)+1)

for i in range(N):
    a = A[i]
    c = C[i]
    for j in range(len(DP)-1,c-1,-1):
        DP[j] = max(DP[j], DP[j-c] + a)

for i in range(len(DP)):
    if DP[i] >= M:
        print(i)
        break