N, M, K = map(int, input().split())

print(max(0, N - M * K), end = " ")
print(max(0, N - M * K + (M - 1)))