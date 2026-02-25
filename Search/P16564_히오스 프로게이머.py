import sys
input = sys.stdin.readline

N, K = map(int, input().split())
X = [int(input()) for _ in range(N)]

start = min(X)
end = max(X) + K
ans = 0

# 탐색할 매개변수 : 팀 레벨(T)
while start <= end:
    mid = (start + end) // 2

    count = 0
    for x in X:
        if x < mid:
            count += mid - x

    if count <= K:
        ans = mid
        start = mid + 1

    else:
        end = mid - 1

print(ans)