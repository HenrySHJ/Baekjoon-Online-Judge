N = int(input())
A = list(map(int, input().split()))

cur = 1
stack = []
output = 'Nice'

for a in A:
    while stack and stack[-1] == cur:
        stack.pop()
        cur += 1

    if a == cur:
        cur += 1

    else:
        stack.append(a)

# 남은 번호 처리
while stack:
    if cur == stack.pop():
        cur += 1

    else:
        output = 'Sad'
        break

print(output)