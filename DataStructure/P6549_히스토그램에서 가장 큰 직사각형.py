import sys
input = sys.stdin.readline

while True:
    temp = list(map(int, input().split()))
    n = temp[0]
    if n == 0:
        break
    
    height = temp[1:]
    stack = []
    area_max = 0

    for i in range(n):
        # 새로운 높이가 stack[-1] 높이보다 작은 경우 -> 스택의 넓이 처리
        while stack and height[stack[-1]] > height[i]:
            h = height[stack.pop()]
            if stack:
                w = i - stack[-1] - 1
            else:
                w = i
            area_max = max(area_max, h*w)
        stack.append(i)
    
    # stack에 남은 인덱스 처리
    while stack:
        h = height[stack.pop()]
        if stack:
            w = n - stack[-1] - 1
        else:
            w = n

        area_max = max(area_max, h*w)

    print(area_max)