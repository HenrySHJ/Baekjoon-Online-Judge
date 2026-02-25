import sys
input = sys.stdin.readline

S, C = map(int, input().split())
green_onion = [int(input()) for _ in range(S)]

start = 1
end = max(green_onion)
ans_go = 0

while start <= end:
    mid = (start + end) // 2

    count = 0
    for go in green_onion:
        count += go // mid

    if count >= C:
        ans_go = mid
        start = mid + 1

    else:
        end = mid - 1

ans = 0
for go in green_onion:
    ans += go % ans_go

ans = sum(green_onion) - (ans_go * C)

print(ans)