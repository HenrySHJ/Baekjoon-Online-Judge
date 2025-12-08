import sys
input = sys.stdin.readline

N = int(input())

# DP[i] : i가 0이면 선공 승, 1이면 후공 승
DP = [0]*(N+1)
DP[1] = 1

# 기저값 작성
if N >= 2: DP[2] = 0
if N >= 3: DP[3] = 1
if N >= 4: DP[4] = 0
if N >= 5: DP[5] = 0
if N >= 6: DP[6] = 0
if N >= 7: DP[7] = 0

# 메모제이션
for i in range(8,N+1):
    if DP[i-1] == 1 or DP[i-3] == 1 or DP[i-4] == 1:
        DP[i] = 0
    else:
        DP[i] = 1

print("SK" if DP[N] == 0 else "CY")