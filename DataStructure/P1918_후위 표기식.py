import sys
input = sys.stdin.readline

expression = input().strip()
stack = []
ans = ""

# 연산자 우선순위 
prior = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

for exp in expression:
    # 피연산자인 경우 바로 정답에 입력
    if 'A' <= exp <= 'Z':
        ans += exp
    
    # 여는 괄호인 경우
    elif exp == '(':
        stack.append(exp)
    
    # 닫는 괄호인 경우 
    elif exp == ')':
        # '('를 만날 때까지 pop
        while stack and stack[-1] != '(':
            ans += stack.pop()

        # '(' 털어내기
        stack.pop() 
    
    # 일반 연산자인 경우
    else:
        # 스택에 우선순위가 높거나 같은 연산자가 있다면 다 꺼냄
        while stack and prior[stack[-1]] >= prior[exp]:
            ans += stack.pop()
        stack.append(exp)

# 남은 연산자 모두 비우기
while stack:
    ans += stack.pop()

print(ans)