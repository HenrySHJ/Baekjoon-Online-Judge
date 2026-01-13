import sys
input = sys.stdin.readline

N,M = map(int,input().split())

basket = [i for i in range(N+1)]

for _ in range(M):
    i,j = map(int,input().split())

    for k in range((j-i+1)//2):
        basket[i+k],basket[j-k] = basket[j-k],basket[i+k]

for i in range(1,N+1):
    print(basket[i],end=' ')