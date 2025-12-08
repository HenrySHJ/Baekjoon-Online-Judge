import sys
input = sys.stdin.readline

N = int(input())
train = [0]+list(map(int,input().split()))
M = int(input())

# 구간 합 구하기
prefix = [0]*(N+1)
for i in range(1,N+1):
    prefix[i] = prefix[i-1] + train[i]
sum_M = [0]*(N+1)

# 현 인덱스까지 최대 연결 시 수용 인원
for i in range(M,N+1):
    sum_M[i] = prefix[i] - prefix[i - M]

# DP[i][j] : i번째까지 연결 시 j개의 소형 기관차를 쓰는 경우 최대 인원
DP = [[0]*4 for _ in range(N+1)]

# 안 쓰는 특정 칸을 찾으며 메모제이션
for i in range(M,N+1):
    for j in range(1,4):
        # i번째 칸 안 쓰는 경우, M~i번째칸까지 쓰는 경우 중 최대
        DP[i][j] = max(DP[i-1][j],DP[i-M][j-1] + sum_M[i])

print(DP[N][3])