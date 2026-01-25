import sys
input = sys.stdin.readline

N, M = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

# N을 더 큰 수로 두기
if M > N:
    A, B = B, A
    N, M = M, N

A.sort()
B.sort()

# DP[i][j] : 남자 i명, 여자 j명일때 최소 차이 합
DP = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        # 인원수가 같으면 1:1 매칭
        if i == j:
            DP[i][j] = DP[i-1][j-1] + abs(A[i-1] - B[j-1])

        # 남자 i, 여자 j : 짝 또는 남자 i : 짝 X
        else:
            DP[i][j] = min(DP[i-1][j-1] + abs(A[i-1] - B[j-1]), DP[i-1][j])

print(DP[N][M])