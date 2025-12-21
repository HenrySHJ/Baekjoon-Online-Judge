import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())

history = [[False]*(N+1) for _ in range(N+1)]

for _ in range(K):
    s,e = map(int,input().split())
    history[s][e] = True

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if history[i][k] and history[k][j]:
                history[i][j] = True

S = int(input())

for _ in range(S):
    qs,qe = map(int,input().split())

    if history[qs][qe]:
        print(-1)
    elif history[qe][qs]:
        print(1)
    else:
        print(0)