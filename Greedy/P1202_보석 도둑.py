import sys, heapq
input = sys.stdin.readline

N,K = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]
# (weight,price) 정렬 : weight 기준 오름차순으로 정렬
jewels.sort()        

bags = [int(input()) for _ in range(K)]
# bag의 용량 오름차순으로 정렬
bags.sort()

ans = 0
heap = []   # heap에서 가장 큰 price 찾기 위한 설정
idx = 0     # jewels 인덱스

for cap in bags:
    # 가방 종류의 최대까지 / 현재 가방 용량보다 작은
    while idx < N and jewels[idx][0] <= cap:
        # jewels의 가격에 음수를 붙여서 최대 힙 구현
        heapq.heappush(heap, -jewels[idx][1])
        idx += 1
    # 가능한 보석 중 가장 비싼 보석을 가방에 넣음
    if heap:
        ans += -heapq.heappop(heap)

print(ans)