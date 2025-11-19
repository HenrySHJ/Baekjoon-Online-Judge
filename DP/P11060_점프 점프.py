import sys
input = sys.stdin.readline

N = int(input())
A = [0]+list(map(int,input().split()))

# 1~i로 점프할때 최소
DP = [sys.maxsize]*(N+1)
DP[1] = 0
for i in range(1,N+1):
    for j in range(i+1,i+A[i]+1):
        if j <= N:
            DP[j] = min(DP[j],DP[i]+1) 

print(DP[N] if DP[N] != sys.maxsize else -1)