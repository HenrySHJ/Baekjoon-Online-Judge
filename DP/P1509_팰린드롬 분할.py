import sys
input = sys.stdin.readline

A = list(input().strip())
N = len(A)

# DP[i][j] : i~j 팰린드롬 검사
DP = [[False]*(N) for _ in range(N)]

# 문자 개수 == 1
for i in range(N):
    DP[i][i] = True

# 문자 개수 == 2
for i in range(N-1):
    if A[i] == A[i+1]:
        DP[i][i+1] = True

# 문자 개수 >= 3
for length in range(3,N+1):
    for i in range(N-length+1):
        j = i + length - 1
        # 추가되는 마지막이 처음과 같고 & 제외한 부분이 팰린드롬이면
        if A[i] == A[j] and DP[i+1][j-1]:
            DP[i][j] = True

# 분할 개수 측정
DP_test = [sys.maxsize]*N

for i in range(N):
    for j in range(i+1):
        if DP[j][i]:
            if j == 0:
                DP_test[i] = 1
            else:
                DP_test[i] = min(DP_test[i], DP_test[j-1] + 1)

print(DP_test[N-1])