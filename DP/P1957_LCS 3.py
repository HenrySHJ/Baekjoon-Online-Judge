import sys
input = sys.stdin.readline

A = list(input().strip())
B = list(input().strip())
C = list(input().strip())

n,m,l = len(A), len(B), len(C)

# DP[i][j][k] : 마지막 문자열이 각각 i,j,k번째일때 최장 문자열 길이
DP = [[[0]*(l+1) for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        for k in range(1,l+1):
            # 마지막 문자가 같으면 길이 +1
            if A[i-1] == B[j-1] == C[k-1]:
                DP[i][j][k] = DP[i-1][j-1][k-1] + 1
            # 최대 길이로 채우기
            else:
                DP[i][j][k] = max(DP[i-1][j][k],DP[i][j-1][k],DP[i][j][k-1])

print(DP[n][m][l])