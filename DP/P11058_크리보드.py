import sys
input = sys.stdin.readline

N = int(input())

DP = [0]*(N+1)

for i in range(1,N+1):
    # 기본 출력
    DP[i] = DP[i-1] + 1

    # Ctrl-A->C->V (총 3단계 고려)
    for j in range(1,i-2):
        DP[i] = max(DP[i], DP[j]*(i-j-1))

print(DP[N])