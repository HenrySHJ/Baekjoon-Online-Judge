import sys
input = sys.stdin.readline

N, M = map(int, input().split())
T = list(int(input()) for _ in range(N))

start = 1
end = min(T) * M
ans = min(T) * M

# 걸리는 시간에 대해 이분탐색
while start <= end:
    mid = (start + end) // 2

    # 각 계산대별 계산 가능한 총 인원의 누적합
    total = 0
    for t in T:
        total += mid // t

        if total >= M:
            break
        
    # M명 이상 심사가 가능하다면 시간 단축
    if total >= M:
        ans = mid
        end = mid - 1

    # 심사 인원이 부족하면 시간 연장
    else:
        start = mid + 1

print(ans)