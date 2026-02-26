N, M = map(int, input().split())
A = list(map(int, input().split()))

start = 1
end = max(A) * M
time = 0

while start <= end:
    mid = (start + end) // 2

    count = 0
    for a in A:
        count += mid // a
    
    if count >= M:
        time = mid
        end = mid - 1

    else:
        start = mid + 1

print(time)