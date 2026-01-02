import sys
input = sys.stdin.readline

N,K = map(int,input().split())

height = list(map(int,input().split()))

# diff[i] : i-1과의 차이
diff = [0]*N
for i in range(1,N):
    diff[i] = height[i] - height[i-1]

diff.sort()

idx = -1
for i in range(K-1):
    diff[idx-i] = 0

print(sum(diff))