import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

print(min(N, N + 1 - S.count('LL')))