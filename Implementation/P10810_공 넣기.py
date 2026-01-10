import sys
input = sys.stdin.readline

N,M = map(int,input().split())

ball = [0]*(N+1)
for _ in range(M):
    i,j,k = map(int,input().split())

    for l in range(i,j+1):
        ball[l] = k

for i in range(1,N+1):
    print(ball[i],end=' ')