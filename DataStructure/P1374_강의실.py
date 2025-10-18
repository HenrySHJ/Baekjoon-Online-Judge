import sys, heapq
input = sys.stdin.readline

N = int(input())

lecture = []
for _ in range(N):
    lec,s,t = map(int,input().split())
    lecture.append((s,t))
lecture.sort()

heap = []

for s,t in lecture:
    if heap and heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap,t)

print(len(heap))