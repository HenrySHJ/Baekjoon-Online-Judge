import sys
input = sys.stdin.readline

N = int(input())
height = list(map(int,input().split()))

signal = [0]*N

stack = []
for i in range(N):
    # 스택의 마지막 높이보다 현재 높이가 더 크면
    while stack and stack[-1][1] < height[i]:
        stack.pop()

    if stack:
        signal[i] = stack[-1][0] + 1

    stack.append((i,height[i]))

print(*signal)