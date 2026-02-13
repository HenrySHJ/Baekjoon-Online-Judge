import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

indexed_A = []
for i in range(N):
    indexed_A.append((A[i], i))

indexed_A.sort()

P = [0] * N
for new_idx in range(N):
    val, idx = indexed_A[new_idx]
    P[idx] = new_idx

print(*P)