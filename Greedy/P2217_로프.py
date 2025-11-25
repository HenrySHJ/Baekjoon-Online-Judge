import sys
input = sys.stdin.readline
N = int(input())

rope = [0]*N

for i in range(N):
    rope[i] = int(input())
rope.sort()

for i in range(N):
    rope[i] *= N-i

print(max(rope))