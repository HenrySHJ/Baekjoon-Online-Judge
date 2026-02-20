import sys
input = sys.stdin.readline

N, M = map(int, input().split())
J = int(input())

# 바구니의 현재 왼쪽 끝과 오른쪽 끝 위치
left = 1
right = M
total = 0

for _ in range(J):
    apple = int(input())
    
    # 사과가 바구니 범위 안에 있는 경우
    if left <= apple <= right:
        continue
    
    # 사과가 바구니의 오른쪽에 떨어지는 경우
    elif apple > right:
        dist = apple - right
        total += dist

        right = apple
        left += dist
        
    # 사과가 바구니의 왼쪽에 떨어지는 경우
    elif apple < left:
        dist = left - apple
        total += dist

        left = apple
        right -= dist

print(total)