import sys, heapq
input = sys.stdin.readline

N = int(input())
tasks = [tuple(map(int,input().split())) for _ in range(N)]
tasks.sort()  # 데드라인 기준 오름차순

heap = []

for d, r in tasks:
    heapq.heappush(heap, r)
    if len(heap) > d:
        heapq.heappop(heap)  # 컵라면 가장 많은 과제 제거

print(sum(heap))