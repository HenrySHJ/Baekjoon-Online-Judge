import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().strip())) for _ in range(N)]

# DP[mask][j][price] : 현재 상태가 mask, 마지막 구매자는 j일때 최종 가격 price일때 가능 여부
DP = [[[False]*10 for _ in range(N)] for _ in range(1<<N)]
DP[1<<0][0][0] = True

for mask in range(1<<N):
    for i in range(N):
        for price in range(10):
            # 아직 i가 그림을 받지 않은 경우
            if not DP[mask][i][price]:
                continue

            for j in range(N):
                # 그림 재소유 불가능
                if mask & (1<<j) != 0:
                    continue

                # j가 그림을 새로 받아 값을 갱신
                if A[i][j] >= price:
                    nmask = mask | (1<<j)
                    DP[nmask][j][A[i][j]] = True

ans = 0
for mask in range(1<<N):
    for last in range(N):
        for price in range(10):
            if DP[mask][last][price]:
                ans = max(ans, mask.bit_count())

print(ans)