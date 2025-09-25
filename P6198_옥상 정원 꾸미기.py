import sys
input = sys.stdin.readline

N = int(input())
stack = []
ans = 0

for _ in range(N):
    h = int(input())
    while stack and stack[-1] <= h:
        stack.pop()
    ans += len(stack)   # 스택에 남아있는 건물은 현재 건물을 본다
    stack.append(h)

print(ans)