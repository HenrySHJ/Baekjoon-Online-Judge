import sys
input = sys.stdin.readline

D,K = map(int,input().split())
DP = [[0,0] for _ in range(D+1)]

DP[1] = [1,0]
DP[2] = [0,1]

for i in range(3,D+1):
    DP[i] = [DP[i-1][0]+DP[i-2][0],DP[i-1][1]+DP[i-2][1]]

a = 0
b = 0
while K > 0:
    K -= DP[D][0]
    a += 1
    if K % DP[D][1] == 0:
        b = K // DP[D][1]
        break

print(a)
print(b)