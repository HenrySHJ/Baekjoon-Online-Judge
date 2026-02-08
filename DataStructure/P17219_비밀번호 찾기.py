import sys
input = sys.stdin.readline

N, M = map(int, input().split())

memo = {}
for _ in range(N):
    site, password = input().split()
    memo[site] = password

for _ in range(M):
    print(memo[input().strip()])