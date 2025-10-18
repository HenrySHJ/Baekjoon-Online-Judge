import heapq, sys

T = int(input())

def dijkstra(start):
    heap = []
    heapq.heappush(heap,(0,start))
    time[start] = 0  # 시작 부분의 감염시간 : 0
    while heap:
        nowNode = heapq.heappop(heap)
        now = nowNode[1]
        if not infected[now]:  # pop한 노드의 컴퓨터 번호는 감염
            infected[now] = True
            for n in Rely[now]:  # 의존 관계의 컴퓨터까지 감염시간 갱신
                if time[n[0]] > time[now] + n[1]:
                    time[n[0]] = time[now] + n[1]
                    heapq.heappush(heap,(time[n[0]],n[0]))

    infect_count = 0
    for i in range(1,len(infected)):
        if infected[i]:
            infect_count += 1

    total_time = 0
    for i in range(1,len(time)):
        if time[i] < sys.maxsize:
            total_time = max(total_time,time[i])
    return infect_count,total_time

for _ in range(T):
    N,D,C = map(int,input().split())
    Rely = [[] for _ in range(N+1)]
    time = [sys.maxsize]*(N+1)
    time[0] = 0
    infected = [False]*(N+1)

    for _ in range(D):
        a,b,s = map(int,input().split())
        Rely[b].append((a,s))

    ans1, ans2 = dijkstra(C)
    print(ans1,ans2)