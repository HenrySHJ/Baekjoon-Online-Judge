import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
DP = [1]*(N)
for i in range(N):
    for j in range(i+1,N):
        if A[j] > A[i]:
            DP[j] = max(DP[j],DP[i]+1)

print(max(DP))

ans = []
c = max(DP)
for i in range(N-1,-1,-1):
    if c == DP[i]:
        c -= 1
        ans.append(A[i])

for i in range(len(ans)-1,-1,-1):
    print(ans[i],end=' ')