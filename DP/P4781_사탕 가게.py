import sys
input = sys.stdin.readline

while True:
    N, M = input().split()

    # 부동소수점 오차 주의
    N, M = int(N), int(float(M) * 100 + 0.5)

    if N == 0 and M == 0.00:
        break

    # DP[i] : i원으로 얻을 수 있는 최대 칼로리
    DP = [0] * (M + 1)

    for _ in range(N):
        c, p = input().split()
        c, p = int(c), int(float(p) * 100 + 0.5)

        for i in range(p, M + 1):
            DP[i] = max(DP[i], DP[i - p] + c)

    print(DP[M])