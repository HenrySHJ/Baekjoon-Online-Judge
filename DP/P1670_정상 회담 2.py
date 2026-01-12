import sys
input = sys.stdin.readline

MOD = 987654321

N = int(input())

DP = [0]*(N+1)
DP[0] = 1

for i in range(2,N+1,2):
    for j in range(0,i+1,2):
        DP[i] = (DP[i] + DP[i-j]*DP[j-2]) % MOD

print(DP[N])