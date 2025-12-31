import sys
input = sys.stdin.readline

stick = list(map(int,input().split()))

stick.sort()

if stick[2] > stick[0] + stick[1] - 1:
    stick[2] = stick[0] + stick[1] - 1

print(sum(stick))