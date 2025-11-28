import sys
input = sys.stdin.readline

N = int(input())
point = [int(input()) for _ in range(N)]

ans = 0
for i in range(N-1,0,-1):
    if point[i] <= point[i-1]:
        ans += point[i-1] - point[i] + 1
        point[i-1] = point[i] - 1

print(ans)