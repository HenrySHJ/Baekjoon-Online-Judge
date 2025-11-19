import sys
input = sys.stdin.readline

K = int(input())

DP_A = [0]*(K+1)
DP_B = [0]*(K+1)
DP_A[0] = 1
DP_B[1] = 1

for i in range(2,K+1):
    DP_A[i] = DP_A[i-1] + DP_A[i-2]
    DP_B[i] = DP_B[i-1] + DP_B[i-2]

print(DP_A[K],DP_B[K])