import sys
input = sys.stdin.readline

MOD = 1000000009

DP1 = [0]*100001
DP2 = [0]*100001
DP3 = [0]*100001

DP1[1] = 1
DP2[2] = 1
DP1[3] = DP2[3] = DP3[3] = 1

for i in range(4,100001):
    DP1[i] = (DP2[i-1] + DP3[i-1]) % MOD
    DP2[i] = (DP1[i-2] + DP3[i-2]) % MOD
    DP3[i] = (DP2[i-3] + DP1[i-3]) % MOD

T = int(input())

for _ in range(T):
    N = int(input())
    print((DP1[N]+DP2[N]+DP3[N])%MOD)