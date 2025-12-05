import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    A = [0]+list(map(int,input().split()))
    S = [0]*(N+1)

    S[1] = A[1]
    for i in range(2,N+1):
        S[i] = S[i-1] + A[i]

    DP = [-sys.maxsize]*(N+1)
    DP[0] = 0
    DP[1] = S[1]

    for i in range(2,N+1):
        for j in range(i):
            DP[i] = max(DP[i],S[i-1]-S[j]+A[i])
    DP[0] = -sys.maxsize
    
    print(max(DP))