import sys
input = sys.stdin.readline

N, L = map(int, input().split())

for K in range(L, 101):
    temp = N - K*(K-1)//2
    if temp < 0:
        continue
    if temp % K == 0:
        x = temp // K
        print(*[x + i for i in range(K)])
        break
else:
    print(-1)