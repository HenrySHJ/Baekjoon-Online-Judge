import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cash = [int(input()) for _ in range(N)]

start = max(cash)
end = sum(cash)
ans = 0

while start <= end:
    mid = (start + end) // 2

    cur_cash = mid
    count = 1

    for i in range(N):
        if cash[i] <= cur_cash:
            cur_cash -= cash[i]
        
        else:
            cur_cash = mid
            cur_cash -= cash[i]
            count += 1

    if count <= M:
        ans = mid
        end = mid - 1

    else:
        start = mid + 1

print(ans)