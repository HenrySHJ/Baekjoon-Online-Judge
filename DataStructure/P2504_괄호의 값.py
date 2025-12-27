import sys
input = sys.stdin.readline

S = input().strip()

stack = []
ans = 0
tmp = 1

# 열린 괄호의 누적 개수로 미리 계산, 올바르지 않은 괄호 나타나면 즉시 종료
for i in range(len(S)):
    if S[i] == '(':
        stack.append('(')
        tmp *= 2

    elif S[i] == '[':
        stack.append('[')
        tmp *= 3

    elif S[i] == ')':
        # 올바르지 않은 괄호 검사
        if not stack or stack[-1] != '(':
            ans = 0
            break

        # 바로 직전이 열린 괄호였다면 정답에 현재 tmp 추가
        if S[i-1] == '(':
            ans += tmp
        stack.pop()
        tmp //= 2

    elif S[i] == ']':
        # 올바르지 않은 괄호 검사
        if not stack or stack[-1] != '[':
            ans = 0
            break

        # 바로 직전이 열린 괄호였다면 정답에 현재 tmp 추가
        if S[i-1] == '[':
            ans += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(ans)