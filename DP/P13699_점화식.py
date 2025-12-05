N = int(input())

DP = [0]*(N+1)
DP[0] = 1

for i in range(1,N+1):
    total = 0
    for j in range(i):
        total += DP[j]*DP[i-1-j]
    DP[i] = total

print(DP[N])