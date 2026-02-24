import sys
input = sys.stdin.readline

N, K = map(int, input().split())

kettle = [int(input()) for _ in range(N)]

start = 1
end = max(kettle)
ans = 0

while start <= end:
    mid = (start + end) // 2

    count = 0
    for i in range(N):
        count += kettle[i] // mid

    if count >= K:
        ans = mid
        start = mid + 1

    else:
        end = mid - 1

print(ans)