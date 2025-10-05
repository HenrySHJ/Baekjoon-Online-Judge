import heapq

N = int(input())

# (-w,d)를 힙에 넣어 점수의 내림차순으로 힙 구현
task = []
for _ in range(N):
    d,w = map(int,input().split())
    heapq.heappush(task,(-w,d))

total = [0]*(1001)
while task:
    now = heapq.heappop(task)
    point = -now[0]
    deadline = now[1]

    # deadline에 가까운 순으로 비어있으면 과제 넣기
    for i in range(deadline,0,-1):
        if total[i] == 0:
            total[i] = point
            break

print(sum(total))