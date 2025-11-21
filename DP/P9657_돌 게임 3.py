import sys
input = sys.stdin.readline

N = int(input())
DP = [0] * (N+1)
DP[1] = 1
if N >= 2: DP[2] = 0
if N >= 3: DP[3] = 1
if N >= 4: DP[4] = 1

for i in range(5, N + 1):
    # i에서 1,3,4 뺀 수를 DP에 넣었을때 모두 이기는 수만 있다면 SK 패배 
    if DP[i-1] == 1 and DP[i-3] == 1 and DP[i-4] == 1:
        DP[i] = 0
    else:
        DP[i] = 1

print("SK" if DP[N] else "CY")