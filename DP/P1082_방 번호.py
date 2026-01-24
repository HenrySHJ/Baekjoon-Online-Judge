import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())

# DP[i] : i원으로 만들 수 있는 가장 큰 숫자
DP = [-1]*(M + 1)

# DP 초기화: 한자리 숫자만 사용
for i in range(N-1,-1,-1):
    cost = A[i]

    # 구매할 수 있는 숫자면 갱신
    if cost <= M:
        DP[cost] = max(DP[cost], i)

# 모든 비용에 대한 처리 (knapsack)
for i in range(1,M+1):
    for j in range(N):
        cost = A[j]

        # 카드를 구매할 수 있고, 그 전 상태가 존재하는 경우에 갱신
        if i >= cost and DP[i - cost] != -1:
            DP[i] = max(DP[i], int(str(DP[i - cost]) + str(j)))

# 정답 출력
print(max(DP))