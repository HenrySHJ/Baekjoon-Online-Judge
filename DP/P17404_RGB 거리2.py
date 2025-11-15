import sys
input = sys.stdin.readline

N = int(input())

A = [list(map(int,input().split())) for _ in range(N)]

ans = sys.maxsize
for first in range(3):
    DP = [[sys.maxsize]*3 for _ in range(N)]
    DP[0][first] = A[0][first]

    for i in range(1,N):
        DP[i][0] = min(DP[i-1][1],DP[i-1][2]) + A[i][0]
        DP[i][1] = min(DP[i-1][0],DP[i-1][2]) + A[i][1]
        DP[i][2] = min(DP[i-1][1],DP[i-1][0]) + A[i][2]

    for last in range(3):
        if last != first:
            ans = min(ans, DP[N-1][last])

print(ans)