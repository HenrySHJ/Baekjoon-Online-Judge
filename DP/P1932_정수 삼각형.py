import sys
input = sys.stdin.readline

N = int(input())

DP = [[] for _ in range(N)]
DP[0] = list(map(int,input().split()))

for i in range(1,N):
    A = list(map(int,input().split()))
    for j in range(len(A)):
        if j == 0:
            DP[i].append(DP[i-1][j] + A[j])
        elif j == len(A) - 1:
            DP[i].append(DP[i-1][j-1] + A[j])
        else:
            DP[i].append(max(DP[i-1][j],DP[i-1][j-1]) + A[j])

print(max(DP[N-1]))