import sys
input = sys.stdin.readline

H,Y = map(int,input().split())

DP = [0]*(Y+1)
DP[0] = H

for i in range(Y+1):
    if i + 1 <= Y:
        DP[i+1] = max(DP[i+1],int(DP[i]*1.05))
    if i + 3 <= Y:
        DP[i+3] = max(DP[i+3],int(DP[i]*1.2))
    if i + 5 <= Y:
        DP[i+5] = max(DP[i+5],int(DP[i]*1.35))

print(DP[Y])