import sys
input = sys.stdin.readline

N,K = map(int,input().split())
price = [0]*N
DP = [0]*(K+1)
DP[0] = 1

for i in range(N):
    price[i] = int(input())

for i in range(N):
    for j in range(price[i],K+1):
        DP[j] += DP[j-price[i]]

print(DP[K])