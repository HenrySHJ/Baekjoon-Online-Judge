import sys
input = sys.stdin.readline

N = int(input())
A = list(input().strip())
B = [int(input()) for _ in range(N)]

ans = 0
stack = []
for i in A:
    # 피연산자
    if ord(i) >= 65:
        m = B[ord(i)-65]
        stack.append(m)

    # 연산자
    else:
        a = stack.pop()
        b = stack.pop()
        if i == '+':
            stack.append(b+a)
        elif i == '-':
            stack.append(b-a)
        elif i == '*':
            stack.append(b*a)
        elif i == '/':
            stack.append(b/a)
ans = stack[0]
print(f"{ans:.2f}")