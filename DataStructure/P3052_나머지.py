import sys
input = sys.stdin.readline

num = [int(input()) for _ in range(10)]

rem = {}

for i in range(10):
    r = num[i] % 42
    rem[r] = rem.get(r,0) + 1

print(len(rem))