import sys
input = sys.stdin.readline

N = int(input())

size = list(map(int,input().split()))
T, P = map(int, input().split())

ans = 0
for i in range(6):
    if size[i] % T == 0:
        ans += size[i] // T
    else:
        ans += size[i] // T + 1

print(ans)
print(N // P, N % P)