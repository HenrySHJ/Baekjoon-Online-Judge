import sys
input = sys.stdin.readline

word = list(input().strip())
bomb = list(input().strip())
len_bomb = len(bomb)

stack = []
for alp in word:
    stack.append(alp)

    if len(stack) >= len_bomb:
        check = True
        for i in range(len_bomb,0,-1):
            if stack[-i] != bomb[-i]:
                check = False
                break
        
        if check:
            for i in range(len_bomb):
                stack.pop()

if stack:       
    for i in range(len(stack)):
        print(stack[i],end='')
else:
    print("FRULA")