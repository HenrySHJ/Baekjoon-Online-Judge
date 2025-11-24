import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    C = int(input())

    Q = 0
    while C >= 25:
        C -= 25
        Q += 1
    print(Q,end=' ')

    D = 0
    while C >= 10:
        C -= 10
        D += 1
    print(D,end=' ')

    N = 0
    while C >= 5:
        C -= 5
        N += 1
    print(N,end=' ')

    P = 0
    while C >= 1:
        C -= 1
        P += 1
    print(P)