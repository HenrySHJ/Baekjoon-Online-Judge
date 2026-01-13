import sys
input = sys.stdin.readline

N = int(input())

A = [0]+list(map(int,input().split()))
B = [0,0]+list(map(int,input().split()))

INF = sys.maxsize

# DP[i][j][k] : 마지막 부지 i, j개의 타워일때 k(0:타워 o, 1:타워 o, 통로x, 2:타워 o, 통로 o)
DP = [[[-INF]*3 for _ in range(N+1)] for _ in range(N+1)]

# DP 초기화
DP[0][0][0] = 0

for i in range(1,N+1):
    for j in range(i+1):
        # i번에 타워를 안 짓는 경우
        DP[i][j][0] = max(DP[i-1][j][0], DP[i-1][j][1], DP[i-1][j][2])

        # 통로 연결 가능 조건
        if j > 0:
            # i번에 타워를 혼자 짓는 경우
            DP[i][j][1] = max(DP[i-1][j-1][0], DP[i-1][j-1][1], DP[i-1][j-1][2]) + A[i]
            
            # i번에 타워를 지으면서 i-1번과 연결하는 경우
            if i > 1 and DP[i-1][j-1][1] != -INF:
                DP[i][j][2] = DP[i-1][j-1][1] + A[i] + B[i]

for j in range(1,N+1):
    print(max(DP[N][j]))