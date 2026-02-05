import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

# 분할 정복
def divide(x, y, n):
    global white, blue
    color = paper[x][y]
    
    # 지정된 범위 내에 다른 색이 있는지 확인
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 색이 같으면 건너뛰기
            if paper[i][j] == color:
                continue

            # 색이 다르면 4등분 후 재귀
            divide(x, y, n // 2)
            divide(x, y + n // 2, n // 2)
            divide(x + n // 2, y, n // 2)
            divide(x + n // 2, y + n // 2, n // 2)
            return
            
    # 지정 범위 내 모두 같은 색 확인
    if color == 0:
        white += 1
    else:
        blue += 1

white = 0
blue = 0

divide(0, 0, N)
print(white)
print(blue)