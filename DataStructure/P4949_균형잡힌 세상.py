import sys
input = sys.stdin.readline

while True:
    A = input().rstrip()
    if A == '.':
        break

    stack = []
    ans = True

    for i in A:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                ans = False
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                ans = False
                break

    if ans and not stack:
        print("yes")
    else:
        print("no")