import sys
input = sys.stdin.readline

N = int(input())
request = list(map(int, input().split()))
M = int(input())

# 예산의 최소 ~ 최대로 시작, 끝 설정
start = 1
end = max(request)
ans = 0

# 예산에 대한 이분 탐색 
while start <= end:
    mid = (start + end) // 2

    # 예산 계산
    budget = 0
    for r in request:
        if r >= mid:
            budget += mid
        else:
            budget += r

    # 예산에 따른 start, end 이동
    if budget <= M:
        ans = max(ans, mid)
        start = mid + 1
    else:
        end = mid - 1

print(ans)