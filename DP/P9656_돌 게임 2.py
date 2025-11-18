import sys
input = sys.stdin.readline

N = int(input())

# N-1 또는 N-3을 먼저 집으면 승자
# 따라서 N - 홀수를 먼저 집으면 승자

if N % 2 == 0:
    print("SK")
else:
    print("CY")