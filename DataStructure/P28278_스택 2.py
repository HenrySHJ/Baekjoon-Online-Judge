import sys
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())

result = []
stack = []

for _ in range(N):
    A = list(map(int,input().split()))

    if A[0] == 1:
        stack.append(A[1])

    elif A[0] == 2:
        if stack:
            result.append(str(stack.pop()))
        else:
            result.append("-1")

    elif A[0] == 3:
        result.append(str(len(stack)))

    elif A[0] == 4:
        result.append("1" if not stack else "0")

    elif A[0] == 5:
        if stack:
            result.append(str(stack[-1]))
        else:
            result.append("-1")

# 한 번에 출력
write("\n".join(result))