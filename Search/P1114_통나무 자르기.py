import sys
input = sys.stdin.readline

L, K, C = map(int, input().split())

points = (set(map(int, input().split())))

# 뒤에서부터 계산하기 위해 L 추가
points = list(points)
points.sort()

if points[-1] != L:
    points.append(L)

# points의 간격 배열 만들기
diff = [points[0]]
for i in range(1, len(points)):
    diff.append(points[i] - points[i - 1])
max_diff = max(diff)

start = max_diff
end = L
ans_len = L
ans_cut = 0

# 통나무 조각의 최대 길이에 대해 이분 탐색
while start <= end:
    mid = (start + end) // 2

    count = 0
    length = 0
    last_cut = 0

    # 최대 간격이 mid보다는 클 수가 없음
    if max_diff > mid:
        count = -1
        last_cut = -1

    else:
        for i in range(len(points) - 1, -1, -1):
            # 자른 길이가 mid보다 크면 이전 지점에서 자르기
            if length + diff[i] > mid:
                count += 1
                length = diff[i]
                last_cut = points[i]

            # 자른 길이가 mid보다 작으면 최근 지점만 기록하기
            else:
                length += diff[i]

        # 최소 한 번 더 자를 수 있으면 가장 왼쪽 지점 자르기
        if count < C:
            last_cut = points[0]

    if count >= 0 and count <= C:
        ans_len = mid
        ans_cut = last_cut
        end = mid - 1
    else:
        start = mid + 1

print(ans_len, ans_cut)