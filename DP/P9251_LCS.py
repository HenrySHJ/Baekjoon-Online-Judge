import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()

len_A, len_B = len(A), len(B)
DP = [[0]*(len_B+1) for _ in range(len_A+1)]

# A ~i번째, B ~j번째까지 비교했을 때의 최장부분수열
for i in range(1, len_A+1):
    for j in range(1, len_B+1):
        # 같은 문자열 추가 -> 1 증가
        if A[i-1] == B[j-1]:
            DP[i][j] = DP[i-1][j-1] + 1
        # 다른 문자열 추가 -> 붙이기 전의 최댓값
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])

print(DP[len_A][len_B])