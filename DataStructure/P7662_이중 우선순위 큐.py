import sys,heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    max_heap = []  # 최대 힙
    min_heap = []  # 최소 힙

    # 둘 다 존재하는 수일때 True, 아닐때는 False
    visited = [False]*N

    for i in range(N):
        Q = list(input().split())

        if Q[0] == 'I':
            heapq.heappush(max_heap,(-int(Q[1]),i))
            heapq.heappush(min_heap,(int(Q[1]),i))
            visited[i] = True

        elif Q[0] == 'D':
            if int(Q[1]) == 1:
                # 최소힙에 없는 쓰레기 값이면 미리 처리
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)

                # 최대값 처리, 최소힙에 남아있는 같은 값 쓰레기값으로
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

            elif int(Q[1]) == -1:
                # 최대힙에 없는 쓰레기 값이면 미리 처리
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)

                # 최솟값 처리, 최대힙에 남아있는 같은 값 쓰레기값으로
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    # 쓰레기 값이 최종 처리
    while min_heap and not visited[min_heap[0][1]]: 
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]: 
        heapq.heappop(max_heap)
        
    if not min_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])