import sys
input = sys.stdin.readline

N = int(input())

heights = []
total = 0
max_h = 0

for _ in range(N):
    row = list(map(int, input().split()))
    for x in row:
        if x > 0:
            heights.append(x)
            total += x
            if x > max_h:
                max_h = x

start = 0
end = max_h

ans = 0 
half = 0
if total % 2 == 0:
    half = total // 2
else:
    half = total // 2 + 1

while start <= end:
    mid = (start + end) // 2

    count = 0
    for h in heights:
        count += min(h, mid)

    if count >= half:
        ans = mid
        end = mid - 1

    else:
        start = mid + 1

print(ans)