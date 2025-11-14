import sys
input = sys.stdin.readline

N = int(input())

wire = [tuple(map(int,input().split())) for _ in range(N)]
wire.sort()
DP = [1]*(N+1)

for i in range(N):
    for j in range(i+1,N):
        if wire[i][0] < wire[j][0] and wire[i][1] < wire[j][1]:
            DP[j] = max(DP[j],DP[i]+1)

print(N-max(DP))