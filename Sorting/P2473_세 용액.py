import sys
input = sys.stdin.readline

N = int(input())
fluids = list(map(int, input().split()))
fluids.sort()

min_diff = sys.maxsize
ans = []

for i in range(N - 2):
    # 투 포인터
    l = i + 1
    r = N - 1
    
    # i보다 인덱스가 큰 포인터 두 개가 만날때까지 탐색
    while l < r:
        cur_sum = fluids[i] + fluids[l] + fluids[r]
            
        # 최솟값 갱신
        if abs(cur_sum) < min_diff:
            min_diff = abs(cur_sum)
            ans = [fluids[i], fluids[l], fluids[r]]
            
        # 포인터 이동
        if cur_sum < 0:
            l += 1

        elif cur_sum > 0:
            r -= 1

        else:
            # 0을 찾은 경우
            print(*ans)
            sys.exit()

print(*ans)