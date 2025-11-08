import sys, heapq
input = sys.stdin.readline

N,M,K = map(int,input().split())

mylist = [[] for _ in range(N+1)]
DP = [[sys.maxsize]*(K+1) for _ in range(N+1)]   # 시간

for _ in range(M):
    a,b,c = map(int,input().split())
    mylist[a].append((b,c))
    mylist[b].append((a,c))


def dijkstra(start):
    heap = []
    heapq.heappush(heap,(0,start,0))
    DP[start][0] = 0

    while heap:
        total,now,used = heapq.heappop(heap)
        if DP[now][used] != total:
            continue

        for next,time in mylist[now]:
            # 포장하지 않을 때
            new_total = total + time
            if DP[next][used] > new_total:
                DP[next][used]= new_total
                heapq.heappush(heap,(new_total,next,used))

            # 포장할 때
            if used < K:
                if DP[next][used+1] > total:
                    DP[next][used+1] = total
                    heapq.heappush(heap,(total,next,used+1))
            
dijkstra(1)
print(min(DP[N]))