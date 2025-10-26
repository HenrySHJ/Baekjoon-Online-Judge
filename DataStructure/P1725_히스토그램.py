import sys
input = sys.stdin.readline

N = int(input())
height = []

for _ in range(N):
    height.append(int(input()))

stack = []
area = 0

for i in range(N):
    while stack and height[stack[-1]] > height[i]:
        h = height[stack.pop()]
        if stack:
            w = i - stack[-1] - 1
        else:
            w = i
        area = max(area,h*w)
    stack.append(i)

while stack:
    h = height[stack.pop()]
    if stack:
        w = N - stack[-1] - 1
    else:
        w = N
    area = max(area,h*w)

print(area)    