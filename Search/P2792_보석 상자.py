import sys
input = sys.stdin.readline

N, M = map(int, input().split())

color = [int(input()) for _ in range(M)]

start = 1
end = max(color)
ans = 0

while start <= end:
    mid = (start + end) // 2

    count = 0
    for i in range(M):
        count += (color[i] + mid - 1) // mid

    if count <= N:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)