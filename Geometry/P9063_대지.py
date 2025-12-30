import sys
input = sys.stdin.readline

N = int(input())

points = []
for _ in range(N):
    points.append(tuple(map(int,input().split())))

min_x = sys.maxsize
min_y = sys.maxsize
max_x = -sys.maxsize
max_y = - sys.maxsize

for p in points:
    x = p[0]
    y = p[1]
  
    min_x = min(min_x,x)
    min_y = min(min_y,y)
    max_x = max(max_x,x)
    max_y = max(max_y,y)

print((max_x-min_x)*(max_y-min_y))