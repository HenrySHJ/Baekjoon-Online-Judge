import sys
input = sys.stdin.readline

N = int(input())

A, B, C, D = [0] * N, [0] * N, [0] * N, [0] * N

for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())

ans = 0

sum_AB = {}
for i in range(N):
    for j in range(N):
        sum_AB[A[i] + B[j]] = sum_AB.get(A[i] + B[j], 0) + 1

ans = 0
for i in range(N):
    for j in range(N):
        num = C[i] + D[j]

        if -num in sum_AB:
            ans += sum_AB[-num]

print(ans)