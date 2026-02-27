import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

beer = [tuple(map(int, input().split())) for _ in range(K)]
beer.sort(key = lambda x: -x[0])

start = 1
end = 2**31
ans = -1

while start <= end:
    mid = (start + end) // 2

    preference = 0
    day = 0
    for v, c in beer:
        if c <= mid:
            preference += v
            day += 1

        if day == N:
            break

    if preference >= M and day == N:
        ans = mid
        end = mid - 1

    else:
        start = mid + 1

print(ans)