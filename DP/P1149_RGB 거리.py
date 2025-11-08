import sys
input = sys.stdin.readline

N = int(input())

A = [list(map(int,input().split())) for _ in range(N)]
DP = [[0]*3 for _ in range(N)]   # 최종인 답은 DP[N-1]중 최소값

for i in range(3):
    DP[0][i] = A[0][i]

for i in range(1,N):
    DP[i][0] += min(DP[i-1][1],DP[i-1][2]) + A[i][0]
    DP[i][1] += min(DP[i-1][0],DP[i-1][2]) + A[i][1]
    DP[i][2] += min(DP[i-1][0],DP[i-1][1]) + A[i][2]

print(min(DP[N-1]))