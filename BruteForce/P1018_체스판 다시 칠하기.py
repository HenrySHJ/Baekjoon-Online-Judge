import sys
input = sys.stdin.readline

N,M = map(int,input().split())

chess = [list(input().strip()) for _ in range(N)]

def count_repaint(x,y):
    # 좌상단이 'W'
    cnt1 = 0
    # 좌상단이 'B'
    cnt2 = 0

    for i in range(8):
        for j in range(8):
            cur = chess[x+i][y+j]
            if (i+j) % 2 == 0:
                if cur != 'W':
                    cnt1 += 1
                if cur != 'B':
                    cnt2 += 1
            else:
                if cur != 'B':
                    cnt1 += 1
                if cur != 'W':
                    cnt2 += 1
    return min(cnt1, cnt2)

ans = float('inf')

for i in range(N-7):
    for j in range(M-7):
        ans = min(ans, count_repaint(i, j))

print(ans)