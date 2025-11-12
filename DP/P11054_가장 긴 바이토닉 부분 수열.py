import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
DP1 = [1]*N
DP2 = [1]*N

# A[i]를 마지막으로 하는 증가수열
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            DP1[i] = max(DP1[i],DP1[j]+1)

# A[i]를 시작으로 하는 감소수열
for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if A[j] < A[i]:
            DP2[i] = max(DP2[i],DP2[j]+1)

ans = 0
for i in range(N):
    ans = max(ans,DP1[i]+DP2[i]-1)
print(ans)