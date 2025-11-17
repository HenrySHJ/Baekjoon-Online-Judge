import sys
input = sys.stdin.readline

N = int(input())
a,b,c = map(int,input().split())
DP1 = [a,b,c]   # max
DP2 = [a,b,c]   # min

for i in range(N-1):
    a,b,c = map(int,input().split())

    n_DP1 = [0]*3
    n_DP2 = [0]*3

    n_DP1[0] = max(DP1[0],DP1[1]) + a
    n_DP2[0] = min(DP2[0],DP2[1]) + a

    n_DP1[1] = max(DP1[0],DP1[1],DP1[2]) + b
    n_DP2[1] = min(DP2[0],DP2[1],DP2[2]) + b

    n_DP1[2] = max(DP1[1],DP1[2]) + c
    n_DP2[2] = min(DP2[1],DP2[2]) + c

    DP1 = n_DP1
    DP2 = n_DP2

print(max(DP1),min(DP2))