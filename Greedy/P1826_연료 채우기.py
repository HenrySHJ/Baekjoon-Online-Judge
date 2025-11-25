import sys, heapq
input = sys.stdin.readline

N = int(input())
A = [tuple(map(int,input().split())) for _ in range(N)]
L,P = map(int,input().split())

A.sort()

heap = []   # 최대힙으로 활용
ans = 0
idx = 0
fuel = P

while fuel < L:
    # 현재 연료로 도달 가능한 모든 주유소 push
    while idx < N and A[idx][0] <= fuel:
        dist, amount = A[idx]
        heapq.heappush(heap, -amount)
        idx += 1

    # 도달 가능한 주유소가 없는데 목적지를 못감 → 실패
    if not heap:
        print(-1)
        exit()

    # 가장 큰 연료를 주는 주유소를 선택해서 충전
    fuel += -heapq.heappop(heap)
    ans += 1

print(ans)