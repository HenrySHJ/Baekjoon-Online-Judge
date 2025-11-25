import sys
input = sys.stdin.readline

# DP[i][j] : 온전 i개, 절반 j개 남았을 때 경우
DP = [[0]*32 for _ in range(32)]
DP[0][0] = 1

for w in range(31):
    for h in range(31):
        # 온전한 알약 먹은 경우
        if w > 0:
            DP[w][h] += DP[w-1][h+1]
        # 절반 알약 먹은 경우
        if h > 0:
            DP[w][h] += DP[w][h-1]

while True:
    N = int(input())

    if N == 0:
        break

    print(DP[N][0])