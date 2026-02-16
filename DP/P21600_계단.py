import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# DP[i] : i번째 열에서의 최대 계단 길이
DP = [1] * N

for i in range(1, N):
    if DP[i - 1] < A[i]: 
        DP[i] = DP[i - 1] + 1
    else:
        DP[i] = A[i]

print(max(DP))