import sys
input = sys.stdin.readline

A = ['']+list(input().strip())
B = ['']+list(input().strip())
DP = [[0]*(len(B)+1) for _ in range(len(A)+1)]

ans = 0
for i in range(1,len(A)):
    for j in range(1,len(B)):
        if A[i] == B[j]:
            DP[i][j] = DP[i-1][j-1] + 1
            ans = max(ans,DP[i][j])

print(ans)