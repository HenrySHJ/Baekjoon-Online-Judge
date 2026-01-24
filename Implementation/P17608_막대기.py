import sys
input = sys.stdin.readline

N = int(input())

stack = [int(input()) for _ in range(N)]

ans = 1
max_h = stack[-1]

for i in range(N-1,-1,-1):
    if max_h < stack[i]:
        ans += 1
        max_h = stack[i]

print(ans)