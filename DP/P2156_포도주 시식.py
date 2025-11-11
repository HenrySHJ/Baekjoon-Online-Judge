import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]
A.insert(0,0)

DP = [[0]*3 for _ in range(N+1)]
DP[1][1] = A[1]

# i로 인해서 j번째 streak이 이어지는 경우
for i in range(2,N+1):
    DP[i][0] = max(DP[i-1][0],DP[i-1][1],DP[i-1][2])
    DP[i][1] = DP[i-1][0] + A[i]
    DP[i][2] = DP[i-1][1] + A[i]

print(max(DP[N]))