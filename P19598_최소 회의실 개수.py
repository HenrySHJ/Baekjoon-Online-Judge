import sys, heapq
input = sys.stdin.readline

N = int(input())

conf = [tuple(map(int,input().split())) for _ in range(N)]
conf.sort()

heap = []
for s,t in conf:
    if heap and heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap,t)

print(len(heap))