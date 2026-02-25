import sys
input = sys.stdin.readline

M, N = map(int, input().split())
L = list(map(int, input().split()))

start = 1
end = max(L)
ans = 0

while start <= end:
    mid = (start + end) // 2

    # mid보다 긴 과자 수 세기
    count = 0
    for l in L:
        count += l // mid

    if count >= M:
        ans = mid
        start = mid + 1

    else:
        end = mid - 1

print(ans)