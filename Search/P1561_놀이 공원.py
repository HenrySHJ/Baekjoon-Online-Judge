import sys
input = sys.stdin.readline

N, M = map(int, input().split())
time = list(map(int, input().split()))

# 예외 처리
if N <= M:
    print(N)
    sys.exit()

start = 0
end = 2000000000 * 30
ans_time = 0

# 운행 시간에 대해 이분 탐색
while start <= end:
    mid = (start + end) // 2

    # 최초 M명 포함 누적 인원
    count = M
    for t in time:
        count += (mid // t)

        if count >= N:
            break

    # 시간 내 N 이상 수용 가능하면 운행 시간 줄이기
    if count >= N:
        ans_time = mid
        end = mid - 1

    # 시간 내 N 이상 수용 불가하면 운행 시간 늘려보기
    else:
        start = mid + 1

# ans_time - 1 까지의 탑승 수 계산
total = M
for t in time:
    total += (ans_time - 1) // t

# 마지막으로 탑승한 기구 찾기
for i in range(M):
    # 기구가 비는지 확인
    if ans_time % time[i] == 0:
        total += 1
        if total == N:
            print(i + 1)
            break