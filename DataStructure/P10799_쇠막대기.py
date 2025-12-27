import sys
input = sys.stdin.readline

S = list(input().strip())

stack = []
ans = 0
for i in range(len(S)):    
    if S[i] == '(':
        stack.append('(')
        if S[i-1] == '(':
            ans += 1
    
    else:
        if S[i-1] == '(':
            if stack:
                stack.pop()
                ans += len(stack)

        if S[i-1] == ')':
            if stack:
                stack.pop()

print(ans)