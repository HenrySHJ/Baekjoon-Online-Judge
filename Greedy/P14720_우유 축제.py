import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

milk = [1, 2, 0]
idx = 0
ans = 0

for i in range(N):
    if A[i] == idx:
        idx = milk[idx]
        ans += 1

print(ans)