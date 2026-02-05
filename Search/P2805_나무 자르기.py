import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))

# 0 ~ 나무의 최대 높이 사이 탐색
start, end = 0, max(tree)
ans = 0

# 이분 탐색으로 적정 절단기 높이 찾기
while start <= end:
    # 절단기의 높이
    mid = (start + end) // 2
        
    total = 0

    # 절단기보다 큰 나무들만 자르기
    for t in tree:
        if t > mid:
            total += t - mid
    
    # ans 갱신 및 범위 조정
    if total >= M:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
            
print(ans)
