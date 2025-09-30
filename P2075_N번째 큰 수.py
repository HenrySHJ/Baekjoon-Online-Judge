import sys, heapq
input = sys.stdin.readline

N = int(input())

table = [list(map(int,input().split())) for _ in range(N)]

heap = []

for i in range(N):
    for j in range(N):
        if len(heap) == N and heap[0] < table[i][j]:
            heapq.heappop(heap)
            heapq.heappush(heap,table[i][j])
        elif len(heap) < N:
            heapq.heappush(heap,table[i][j])

print(heap[0])