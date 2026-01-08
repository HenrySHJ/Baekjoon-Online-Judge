import sys,heapq
input = sys.stdin.readline

N = int(input())

min_heap = []
max_heap = []
result = []

for _ in range(N):
    num = int(input())

    # 최대 힙의 크기는 최소 힙과 같거나 하나 큰 상태로
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)
            
    # 최대 힙의 top이 최소 힙의 top보다 크면 자리를 바꾸기
    if min_heap and (-max_heap[0] > min_heap[0]):
        max_val = -heapq.heappop(max_heap)
        min_val = heapq.heappop(min_heap)
            
        heapq.heappush(max_heap, -min_val)
        heapq.heappush(min_heap, max_val)
            
    # 최대 힙의 top이 중간값
    result.append(-max_heap[0])

for i in result:
    print(i)