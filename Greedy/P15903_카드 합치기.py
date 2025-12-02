import sys, heapq
input = sys.stdin.readline

N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse=True)

heapq.heapify(A)
count = 0
while count < M:
    a = heapq.heappop(A)
    b = heapq.heappop(A)

    n = a+b
    a = b = N
    heapq.heappush(A,n)
    heapq.heappush(A,n)

    count += 1

print(sum(A))