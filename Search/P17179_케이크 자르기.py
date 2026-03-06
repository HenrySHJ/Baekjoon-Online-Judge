import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
S = [int(input()) for _ in range(M)]
S.append(L)

for _ in range(N):
    start = 1
    end = L
    ans = 0

    cut = int(input())
    
    while start <= end:
        mid = (start + end) // 2

        count = 0
        last_cut = 0
        for s in S:
            if s - last_cut >= mid:
                count += 1
                last_cut = s

        if count > cut:
            ans = mid
            start = mid + 1

        else:
            end = mid - 1

    print(ans)