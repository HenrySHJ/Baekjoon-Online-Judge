import sys
import heapq
input = sys.stdin.readline

L = int(input())
S = list(map(int, input().split()))
S.sort()
N = int(input())

ans = []
used = set()
heap = []

# S에 포함된 수는 좋은 구간 개수가 0
for x in S:
    heapq.heappush(heap, (0, x, -1, -1, 0))

# heap 초기화 : (좋은 구간 개수, 현재 수, 왼쪽 끝, 오른쪽 끝, 들어온 거리)
prev = 0
for cur in S:
    # 이전 숫자와 연속된 숫자가 아닌 경우만
    if prev + 1 < cur:
        # 왼쪽 끝(prev + 1) : 좋은 구간의 개수 구해서 push
        count = (1) * (cur - (prev + 1)) - 1
        heapq.heappush(heap, (count, prev + 1, prev, cur, 1))

        # 오른쪽 끝(cur - 1) : 왼쪽과 중복되지 않는 경우에만
        if prev + 1 < cur - 1:
            count = (cur - 1 - prev) * (1) - 1
            heapq.heappush(heap, (count, cur - 1, prev, cur, -1))

    prev = cur

# diff : 좋은 구간의 개수
while heap and len(ans) < N:
    diff, val, s, e, k = heapq.heappop(heap)

    if val in used: 
        continue

    ans.append(val)
    used.add(val)

    # 구간 끝인 경우
    if k == 0:
        continue

    # 왼쪽에서 시작
    elif k > 0: 
        nk = k + 1
        n_val = s + nk

        # 오른쪽과 겹치지 않는 경우
        if n_val < e - (nk - 1): 
            n_cnt = (n_val - s) * (e - n_val) - 1
            heapq.heappush(heap, (n_cnt, n_val, s, e, nk))

    # 오른쪽에서 시작
    else:
        nk = abs(k) + 1
        n_val = e - nk

        # 왼쪽과 겹치지 않는 경우
        if n_val > s + (nk - 1): 
            n_cnt = (n_val - s) * (e - n_val) - 1
            heapq.heappush(heap, (n_cnt, n_val, s, e, -nk)) 

# 수가 부족하면 채우기
num = S[-1] + 1
while len(ans) < N:
    if num not in used:
        ans.append(num)
    num += 1

print(*ans[:N])