import sys
input = sys.stdin.readline

N, K = map(int, input().split())
X = list(map(int, input().split()))

start = 0
end = sum(X)
ans = 0

while start <= end:
    mid = (start + end) // 2

    group_sum = 0
    group_count = 1
    min_sum = mid
    for x in X:
        if group_sum + x > mid:
            min_sum = min(min_sum, group_sum)
            group_sum = 0
            group_count += 1

        else:
            group_sum += x

    if group_count <= K:
        ans = mid
        end = mid - 1

    else:
        start = mid + 1

print(ans)