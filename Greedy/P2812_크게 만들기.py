N,K = map(int,input().split())

num = list(input())
stack = []
pop_count = 0
i = 0
stack.append(num[i])
i += 1

while pop_count < K and i < len(num):
    # top보다 큰 수
    if num[i] > stack[-1]:
        while stack and num[i] > stack[-1]:
            stack.pop()
            pop_count += 1
            if pop_count == K:
                break
        stack.append(num[i])
    # top보다 작거나 같은 수
    elif num[i] <= stack[-1]:
        stack.append(num[i])
    # 다음 알파벳으로
    i+=1

# i가 먼저 최대가 됐을 때
while pop_count < K:
    stack.pop()
    pop_count += 1

# pop_count가 먼저 최대가 됐을 때
while i < len(num):
    stack.append(num[i])
    i += 1

for i in stack:
    print(i,end='')