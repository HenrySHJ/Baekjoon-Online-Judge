import sys
input = sys.stdin.readline

N = int(input())

stack = []   # (숫자, 연속 횟수)
ans = 0

for i in range(N):
    h = int(input())

    # 마지막 숫자가 h보다 작으면 쌍 형성, 해당 값 pop
    while stack and stack[-1][0] < h:
        ans += stack.pop()[1]

    # 스택이 비어있으면 push
    if not stack:
        stack.append((h,1))

    else:
        # 마지막 숫자랑 h가 같은 경우 누적 개수만큼 쌍
        if stack[-1][0] == h:
            cnt = stack.pop()[1]
            ans += cnt

            # h의 마지막 쌍 형성
            if stack:
                ans += 1

            stack.append((h,cnt+1))

        # 한 쌍 형성 & push
        else:
            ans += 1
            stack.append((h,1))

print(ans)