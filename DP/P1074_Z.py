import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, R, C = map(int, input().split())

def divide(start, end, r, c):
    if start == end:
        return 0

    mid = (start + end) // 2
    half = (end - start + 1) // 2

    # 4분할
    if r <= mid and c <= mid:
        return divide(start, mid, r, c)
    
    elif r <= mid and c > mid:
        return divide(start, mid, r, c - half) + half ** 2
    
    elif r > mid and c <= mid:
        return divide(start, mid, r - half, c) + (half ** 2) * 2
    
    else:
        return divide(start, mid, r - half, c - half) + (half ** 2) * 3

    
print(divide(0, 2 ** N - 1, R, C))