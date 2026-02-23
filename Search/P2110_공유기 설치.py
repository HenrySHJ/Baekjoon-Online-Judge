import sys
input = sys.stdin.readline

N, C = map(int, input().split())

house = [int(input()) for _ in range(N)]
house.sort()

# 공유기 사이의 거리
start = 1
end = house[N - 1] - house[0]
result = 0

# 공유기 거리를 이분탐색
while start <= end:
    # mid : 공유기 사이 최대 거리
    mid = (start + end) // 2
        
    # 첫 번째 집에는 항상 설치
    count = 1
    last = house[0]
        
    # 거리 유지하며 설치 가능한 공유기 개수 세기
    for i in range(1, N):
        if house[i] >= last + mid:
            count += 1
            last = house[i]
        
    # 설치한 개수가 C 이상이면 mid를 늘려보기
    if count >= C:
        result = mid
        start = mid + 1
    # 설치한 개수가 C 이하면 mid 줄여보기
    else:
        end = mid - 1

print(result)