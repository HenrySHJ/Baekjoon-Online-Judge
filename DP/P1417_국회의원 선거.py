import sys,heapq
input = sys.stdin.readline

N = int(input())
A = [-int(input()) for i in range(1,N+1)]

dasom = A.pop(0)*(-1)
heapq.heapify(A)

if N == 1:
    print(0)
    sys.exit()

ans = 0
while A:
    now = heapq.heappop(A)

    if dasom > now*(-1):
        print(ans)
        break
    
    now = now + 1
    dasom += 1
    ans += 1
    heapq.heappush(A,now)