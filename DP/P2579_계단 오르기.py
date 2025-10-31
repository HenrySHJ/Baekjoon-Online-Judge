import sys
input = sys.stdin.readline

N = int(input())

stairs = [0] * (N+1)
for i in range(1, N+1):
    stairs[i] = int(input())

DP1 = [0]*(N+1)  # 전에 계단을 밟은 경우 MAX
DP2 = [0]*(N+1)  # 전에 계단을 안 밟은 경우 MAX

DP1[1] = stairs[1]
DP2[1] = stairs[1]

for i in range(2,N+1):
    DP1[i] = DP2[i-1] + stairs[i]
    DP2[i] = max(DP1[i-2],DP2[i-2]) + stairs[i]

print(max(DP1[N],DP2[N]))