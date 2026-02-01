import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    h = N % H
    w = N // H + 1

    if h == 0:
        h = H
        w -= 1

    room = 100 * h + w
    print(room)