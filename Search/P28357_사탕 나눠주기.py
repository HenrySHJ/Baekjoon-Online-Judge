import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

start = 0
end = max(A)
ans = end

while start <= end:
    mid = (start + end) // 2

    count = 0
    for a in A:
        if a > mid:
            count += (a - mid)

            if count > K:
                break

    if count <= K:
        ans = mid
        end = mid - 1

    else:
        start = mid + 1

print(ans)