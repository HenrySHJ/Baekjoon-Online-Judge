import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

DP = [0] * 100

for i in range(N):
    for hp in range(99, A[i]-1, -1):
        DP[hp] = max(DP[hp], DP[hp - A[i]] + B[i])

print(max(DP))