import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

DP = [[0]*21 for _ in range(N)]
DP[0][A[0]] = 1

for i in range(1,N-1):
    for v in range(21):
        # 전에 계산된 경우가 있을 때
        if DP[i-1][v] > 0:
            if v + A[i] <= 20:
                DP[i][v + A[i]] += DP[i-1][v]
            if v - A[i] >= 0:
                DP[i][v - A[i]] += DP[i-1][v]

print(DP[N-2][A[N-1]])