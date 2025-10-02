import heapq

N,K = map(int,input().split())
visited = [False]*(100001)

# 힙을 이용해 도달시간이 짧은 순부터 처리
def BFS(v):
    heap = []
    heapq.heappush(heap,(0,v))
    visited[v] = True
    while heap:
        sec, pos = heapq.heappop(heap)
        if pos == K:
            return sec
        next_pos = pos*2
        if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                if next_pos <= K*2:
                    heapq.heappush(heap,(sec,next_pos))

        for next_pos in (pos-1, pos+1):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                heapq.heappush(heap,(sec+1,next_pos))
        
print(BFS(N))