import sys
input = sys.stdin.readline

N,M = map(int,input().split())

A = [i for i in range(N+1)]

for _ in range(M):
    i,j = map(int,input().split())
    A[i],A[j] = A[j],A[i]

for i in range(1,N+1):
    print(A[i],end=' ')