import sys
input = sys.stdin.readline

M = int(input())
N = list(map(int, input().split()))
A = list(map(int, input().split()))

for i in range(M):
    # 특별 예외처리
    if A[i] == 0:
        print(0, end = " ")

    # 1 + 1이면 무한히 살 수 있음
    elif N[i] == 1:
        print(1, end = " ")

    # N + 1보다 적게 사는 경우
    elif N[i] >= A[i]:
        print(A[i], end = " ")
    
    else:
        ans = 0
        start = 0
        end = A[i]

        # 구매 개수에 대해 이분탐색 
        while start <= end:
            mid = (start + end) // 2

            count = mid + (mid - 1) // N[i]
            # 수령 개수
            count = N[i] + 1          

            # 첫 단위 이후부터 N[i] - 1개만 필요 & 나머지 처리
            count += N[i] * ((mid - N[i]) // (N[i] - 1))
            count += (mid - N[i]) % (N[i] - 1)

            if count >= A[i]:
                ans = mid
                end = mid - 1

            else:
                start = mid + 1

        print(ans, end = " ")