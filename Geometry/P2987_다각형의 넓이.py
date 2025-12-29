import sys
input = sys.stdin.readline

dots = [tuple(map(int,input().split())) for _ in range(3)]
dots.append((dots[0][0],dots[0][1]))

width = 0
for i in range(3):
    width += dots[i][0]*dots[i+1][1] - dots[i][1]*dots[i+1][0]
print(abs(float(width))/2)

N = int(input())

trees = []
for _ in range(N):
    x,y = map(int,input().split())
    trees.append((x,y))

def CCW(x1,y1,x2,y2,x3,y3):
    return x1*y2 + x2*y3 + x3*y1 - (y1*x2 + y2*x3 + y3*x1)

def is_in_triangle(x1,y1,x2,y2,x3,y3,x4,y4):
    a = CCW(x1,y1,x2,y2,x4,y4)
    b = CCW(x2,y2,x3,y3,x4,y4)
    c = CCW(x3,y3,x1,y1,x4,y4)

    if a >= 0 and b >= 0 and c >= 0:
        return True
    elif a <= 0 and b <= 0 and c <= 0:
        return True
    return False

ans = 0
for i in range(N):
    if is_in_triangle(dots[0][0],dots[0][1],dots[1][0],dots[1][1],dots[2][0],dots[2][1],trees[i][0],trees[i][1]):
        ans += 1

print(ans)