import sys
import heapq
input = sys.stdin.readline

INF = sys.maxsize

N = int(input())

home_office = [[0,0] for _ in range(N)]

for i in range(N):
    ho = list(map(int,input().split()))
    home_office[i] = sorted(ho)

# 노드의 끝 부분에 따른 오름차순 정렬
home_office.sort(key=lambda x:x[1])

D = int(input())

heap = []
max_count = 0

# end에 따라 정렬된 리스트
for start, end in home_office:
    # 경로의 총 길이가 D보다 짧은 경우만 heap에 추가
    if end - start <= D:
        heapq.heappush(heap, start)
        
    # 현재 철로의 시작점(end - d)보다 앞에 있는 시작점들은 제거
    l_start = end - D
    while heap and heap[0] < l_start:
        heapq.heappop(heap)
        
    # 힙에 남아있는 노드들은 현재 [end-d, end] 구간에 완전히 포함됨
    max_count = max(max_count, len(heap))
        
print(max_count)