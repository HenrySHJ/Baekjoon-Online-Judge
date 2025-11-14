import sys
input = sys.stdin.readline

N = int(input())
DP = [sys.maxsize]*(N+1)
DP[0] = 0

k = 1
while k**2 < N:
    k += 1

num = [0]*(k+1)
for i in range(1,k+1):
    num[i] = i**2

for i in range(1,N+1):
    for j in range(1,int(i**0.5)+1):
        DP[i] = min(DP[i],DP[i-num[j]]+1)

print(DP[N])