import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N,M = map(int,input().split())
    A = [tuple(map(int,input().split())) for _ in range(M)]

    # 끝 번호 기준 정렬
    A.sort(key=lambda x:x[1])

    # 기부된 책 기록
    used = [False]*(N+1)
    count = 0

    for a,b in A:
        for book in range(a,b+1):
            if not used[book]:
                used[book] = True
                count += 1
                break

    print(count)