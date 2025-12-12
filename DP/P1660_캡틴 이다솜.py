import sys
input = sys.stdin.readline

N = int(input())

size = [0]
prefix_sum = [0]

idx = 1
while N >= prefix_sum[-1]:
    size.append(size[-1] + idx)
    prefix_sum.append(prefix_sum[-1] + size[-1])
    idx += 1
prefix_sum.pop()

DP = [sys.maxsize]*(N+1)
DP[0] = 0

for i in prefix_sum:
    for j in range(i,N+1):
        DP[j] = min(DP[j],DP[j-i]+1)

print(DP[N])