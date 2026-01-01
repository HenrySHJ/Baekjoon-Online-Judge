N,W,H = map(int,input().split())

max_l = (W**2+H**2)**0.5

for _ in range(N):
    l = int(input())

    if l <= max_l:
        print("DA")
    else:
        print("NE")