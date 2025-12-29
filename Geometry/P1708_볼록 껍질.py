import sys
input = sys.stdin.readline

N = int(input())

dots = []
for _ in range(N):
    x,y = map(int,input().split())
    dots.append((x,y))

def ccw(a,b,c):
    return (a[0]*b[1]+b[0]*c[1]+c[0]*a[1]) - (a[1]*b[0]+b[1]*c[0]+c[1]*a[0])

# 볼록 껍질
def convex_hull(points):
    # 점이 2개 이하일때 그 자체로 반환
    if len(points) <= 2:
        return points

    # 점 정렬하기
    points = sorted(points)

    # x 기준 오름차순
    lower = []
    for p in points:
        # lower에 2개 이상의 값이 있고 마지막 두 개의 값이랑 p가 시계 방향을 이루는 경우
        while len(lower) >= 2 and ccw(lower[-2],lower[-1],p) <= 0:
            lower.pop()
        lower.append(p)

    # x 기준 내림차순 
    upper = []
    for p in reversed(points):
        # upper에 2개 이상의 값이 있고 마지막 두 개의 값이랑 p가 시계 방향을 이루는 경우
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # 시작점/끝점 중복 제거
    return lower[:-1] + upper[:-1]

print(len(convex_hull(dots)))