import sys
input = sys.stdin.readline

T = int(input())

def is_inside(x1,y1,x2,y2,r):
    if ((x2-x1)**2 + (y2-y1)**2)**0.5 < r:
        return True
    return False

for _ in range(T):
    x1,y1,x2,y2 = map(int,input().split())

    N = int(input())
    planet = [tuple(map(int,input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        bool_A = is_inside(x1,y1,planet[i][0],planet[i][1],planet[i][2])
        bool_B = is_inside(x2,y2,planet[i][0],planet[i][1],planet[i][2])

        if bool_A and not bool_B:
            ans += 1
        elif not bool_A and bool_B:
            ans += 1

    print(ans)