import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
rest_area = list(map(int, input().split()))
rest_area.sort()
rest_area.append(L)

diff = [rest_area[0]]
for i in range(1, N + 1):
    diff.append(rest_area[i] - rest_area[i - 1])

start = 1
end = L - 1
ans = 0

while start <= end:
    mid = (start + end) // 2

    count = 0
    for d in diff:
        if d > mid:
            count += (d - 1) // mid

    if count > M:
        start = mid + 1

    else:
        ans = mid
        end = mid - 1

print(ans)