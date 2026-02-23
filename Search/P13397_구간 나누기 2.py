import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

start = 0
end = max(arr) - min(arr)
ans = end

# 구간의 점수에 대해 이분탐색
while start <= end:
    # 구간의 점수
    mid = (start + end) // 2

    # 구간의 개수 세기
    count = 1
    min_val = arr[0]
    max_val = arr[0]

    for i in range(1, N):
        min_val = min(min_val, arr[i])
        max_val = max(max_val, arr[i])

        # 조건에 안 맞으면 새로운 구간을 나누기
        if max_val - min_val > mid:
            count += 1

            # 새로운 구간
            min_val = arr[i]
            max_val = arr[i]

    # 구간의 개수에 따른 범위 재설정
    if count <= M:
        ans = mid
        end = mid - 1
        
    else:
        start = mid + 1

print(ans)