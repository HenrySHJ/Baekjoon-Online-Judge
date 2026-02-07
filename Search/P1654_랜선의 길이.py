import sys
input = sys.stdin.readline

K, N = map(int, input().split())
LAN = [int(input()) for _ in range(K)]

start, end = 1, max(LAN)

ans = 0
while start <= end:
    # mid는 절단할 길이
    mid = (start + end) // 2

    total = 0

    for l in LAN:
        total += l // mid

    if total >= N:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)