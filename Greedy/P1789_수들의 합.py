import sys
input = sys.stdin.readline

S = int(input())

num = 1
ans = 0
while S - num >= 0:
    S -= num
    num += 1

print(num)