import sys
input = sys.stdin.readline

N = int(input())

opinion = [int(input()) for _ in range(N)]
opinion.sort()
start = int(N * 0.15 + 0.5)

ans = 0
for i in range(start, N - start):
    ans += opinion[i]

if N - start * 2 == 0:
    print(sum(opinion))
else:
    print(int(ans / (N - start * 2) + 0.5))