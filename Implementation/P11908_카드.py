import sys
input = sys.stdin.readline

N = int(input())
C = list(map(int, input().split()))

print(sum(C) - max(C))