import sys
input = sys.stdin.readline

N, M = map(int, input().split())
marble = list(map(int, input().split()))

start = max(marble)
end = sum(marble)
ans = sum(marble)

while start <= end:
    mid = (start + end) // 2

    cur_sum = 0
    count = 1
    for m in marble:
        if cur_sum + m > mid:
            cur_sum = m
            count += 1

        else:
            cur_sum += m

    if count <= M:
        ans = mid
        end = mid - 1

    else:
        start = mid + 1

print(ans)

count = 0
cur_sum = 0
result = []
remain = N

for i in range(N):
    cur_sum += marble[i]
    count += 1
    remain -= 1 
    
    cut = False
    
    # 다음 구슬 합이 기준치를 넘기는 경우 자르기
    if i + 1 < N and cur_sum + marble[i + 1] > ans:
        cut = True
    
    # 나누지 않으면 M개를 못 채우게 될 경우 자르기
    if remain < M:
        cut = True
    
    if cut:
        result.append(count)
        M -= 1
        cur_sum = 0
        count = 0

print(*result)