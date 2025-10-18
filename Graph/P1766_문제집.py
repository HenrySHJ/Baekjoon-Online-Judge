import heapq

N, M = map(int,input().split())

A = [[] for _ in range(N+1)]   # 인접 리스트
indegree = [0]*(N+1)  # 진입 차수

for _ in range(M):
    a,b = map(int,input().split())
    A[a].append(b)
    indegree[b] += 1

# heap 구조 사용하여 진입차수 0인 낮은 번호부터
heap = []  

# heap + 위상 정렬
for i in range(1,N+1):
    if indegree[i] == 0:
        heapq.heappush(heap,i)

while heap:
    now = heapq.heappop(heap)
    print(now, end=' ')
    for next in A[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            heapq.heappush(heap,next)