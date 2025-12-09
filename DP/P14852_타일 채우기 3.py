import sys
input = sys.stdin.readline

N = int(input())

MOD = 1000000007

DP1 = [0]*(N+1)
DP2 = [0]*(N+1)   # 현재까지의 누적합

DP1[0] = 1
DP1[1] = 2
if N >= 2: DP1[2] = 7

DP2[0] = 1
DP2[1] = 3
if N >= 2: DP2[2] = 10

for i in range(3,N+1):
    DP1[i] = (DP1[i-1]*2 + DP1[i-2]*3 + DP2[i-3]*2) % MOD
    DP2[i] = (DP2[i-1] + DP1[i]) % MOD
    
print(DP1[N])