import sys, heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    ans = 0
    K = int(input())
    A = list(map(int,input().split()))
    heapq.heapify(A)

    while len(A) > 1:
        # A의 최솟값 두 개 뽑아 합치고 다시 A에 넣기
        X = heapq.heappop(A)
        Y = heapq.heappop(A)
        # 합친 값은 답에 추가
        ans += X + Y
        heapq.heappush(A,X+Y)

    print(ans)