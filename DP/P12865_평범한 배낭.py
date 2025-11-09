import sys
input = sys.stdin.readline

N,K = map(int,input().split())
A = [tuple(map(int,input().split())) for _ in range(N)]

DP = [0]*(K+1)

for w, v in A:
    for weight in range(K, w-1, -1):
        DP[weight] = max(DP[weight], DP[weight-w] + v)

print(DP[K])