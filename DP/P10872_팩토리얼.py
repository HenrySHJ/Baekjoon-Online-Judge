N = int(input())

DP = [0]*(N+1)
DP[0] = 1

for i in range(1,N+1):
    DP[i] = DP[i-1] * i

print(DP[N])