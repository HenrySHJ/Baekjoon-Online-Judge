import sys, heapq
input = sys.stdin.readline

N,K = map(int,input().split())
pos = [[] for _ in range(12)]

# position 별 heap 분류
for _ in range(N):
    p,w = map(int,input().split())
    heapq.heappush(pos[p],-w)

for _ in range(K):
    for i in range(1,12):
        if pos[i]:
            v = -heapq.heappop(pos[i])
            if v > 0:
                heapq.heappush(pos[i],-(v-1))

print(sum(-heapq.heappop(pos[i]) if pos[i] else 0 for i in range(1,12)))